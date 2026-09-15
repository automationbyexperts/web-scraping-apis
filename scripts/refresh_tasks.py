"""Snapshot the public Apify task landing pages into data/tasks.json.

Local only. It authenticates with APIFY_TOKEN when set, otherwise it calls the API through the
logged-in Apify CLI. Never run it in CI and never commit a token: the snapshot holds only task
names, titles, descriptions and inputs, with credential-looking keys removed.
Standard library only.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'data' / 'tasks.json'
USERNAME = 'fayoussef'
API = 'https://api.apify.com/v2'
SECRET_KEY = re.compile(r'token|api_?key|password|secret|cookie', re.IGNORECASE)


def load_token() -> str | None:
    """APIFY_TOKEN if set. Otherwise None, and calls go through the logged-in Apify CLI,
    which keeps its token in the OS keychain rather than in ~/.apify/auth.json."""
    token = os.environ.get('APIFY_TOKEN')
    if token:
        return token
    auth = Path.home() / '.apify' / 'auth.json'
    if auth.exists():
        return json.loads(auth.read_text(encoding='utf-8')).get('token')
    return None


def cli_command() -> list[str]:
    npm = shutil.which('npm')
    if not npm:
        sys.exit('No Apify token: set APIFY_TOKEN, or install the Apify CLI and run `apify login`.')
    root = subprocess.run([npm, 'root', '-g'], capture_output=True, text=True, check=True).stdout.strip()
    script = Path(root) / 'apify-cli' / 'dist' / 'apify.js'
    if not script.exists():
        sys.exit('No Apify token: set APIFY_TOKEN, or install the Apify CLI and run `apify login`.')
    # Call node directly: the apify.cmd shim re-parses arguments through cmd.exe.
    return ['node', str(script), 'api', 'GET']


def get(path: str, token: str | None, cli: list[str] | None):
    last = None
    for attempt in range(4):
        try:
            if token:
                req = urllib.request.Request(f'{API}/{path}', headers={'Authorization': f'Bearer {token}'})
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return json.loads(resp.read().decode('utf-8'))
            out = subprocess.run([*cli, path], capture_output=True, text=True, encoding='utf-8', check=True).stdout
            start = min(i for i in (out.find('{'), out.find('[')) if i >= 0)
            return json.loads(out[start:])
        except Exception as exc:
            last = exc
            print(f'  {path}: attempt {attempt + 1} failed ({type(exc).__name__}), retrying in {min(2 ** attempt, 8)}s')
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f'GET {path} failed after 4 attempts: {type(last).__name__}')


def strip_secrets(value):
    if isinstance(value, dict):
        return {k: strip_secrets(v) for k, v in value.items() if not SECRET_KEY.search(k)}
    if isinstance(value, list):
        return [strip_secrets(v) for v in value]
    return value


def main() -> None:
    token = load_token()
    cli = None if token else cli_command()

    tasks, offset = [], 0
    while True:
        page = get(f'actor-tasks?limit=500&offset={offset}', token, cli)['data']
        tasks.extend(page['items'])
        offset += len(page['items'])
        if not page['items'] or offset >= page['total']:
            break

    public = [t for t in tasks if t.get('isPublic') and t.get('actUsername') == USERNAME]
    public.sort(key=lambda t: (t['actName'], t['createdAt']))

    def detail(task):
        info = get(f"actor-tasks/{task['id']}", token, cli)['data']
        try:
            run_input = get(f"actor-tasks/{task['id']}/input", token, cli)
        except Exception:
            run_input = {}
        return {
            'actor': task['actName'],
            'name': task['name'],
            'title': info.get('title') or task.get('title') or task['name'],
            'description': info.get('description') or '',
            'input': strip_secrets(run_input if isinstance(run_input, dict) else {}),
        }

    with ThreadPoolExecutor(max_workers=8 if token else 2) as pool:
        rows = list(pool.map(detail, public))

    snapshot: dict[str, list] = {}
    for row in rows:
        snapshot.setdefault(row.pop('actor'), []).append(row)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Wrote {len(rows)} public tasks for {len(snapshot)} actors to {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
