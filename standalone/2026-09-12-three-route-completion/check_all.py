"""Run the finite checks for all three proposed routes and the LP bridge.

No result of this driver is an acceptance of RH or an infinite paper proof.
The optional scouts and their third-party dependencies are not run here.
"""
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
GROUPS = {
    'arithmetic': [('check.py', '--check', 'results.json'), ('test_rejections.py',)],
    'ferromagnetic': [('certify_graft.py',), ('test_graft.py',)],
    'gamma': [('check.py',)],
    'bridge': [('verify.py', '--check', 'result.json', '--self-test')],
}


def group_run(group):
    rows = []
    for args in GROUPS[group]:
        modes = [False] if args[0] == 'test_rejections.py' else [False, True]
        for optimized in modes:
            switches = ['-S', '-B'] + (['-O'] if optimized else [])
            command = [sys.executable] + switches + list(args)
            result = subprocess.run(command, cwd=ROOT/group, capture_output=True, text=True)
            output = (result.stdout + result.stderr).replace('\r\n', '\n')
            if result.returncode != 0:
                raise RuntimeError(f'{group}: {args}: {output}')
            rows.append({'command': ['python'] + switches + list(args),
                         'exit_code': result.returncode, 'output': output})
    return group, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    args = parser.parse_args()
    with ThreadPoolExecutor(max_workers=4) as pool:
        runs = dict(pool.map(group_run, GROUPS))
    bound = {}
    for group in GROUPS:
        for path in sorted((ROOT/group).iterdir()):
            if path.is_file() and path.suffix in ('.py', '.md', '.json'):
                bound[str(path.relative_to(ROOT)).replace('\\', '/')] = hashlib.sha256(path.read_bytes()).hexdigest()
    record = {'scope': 'finite exact/rational/directed controls only; no RH proof or parent native integral replay',
              'python': sys.version, 'groups': runs, 'file_sha256_at_run': bound}
    if args.write:
        args.write.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'passed': True, 'groups': list(runs),
                      'subprocess_commands': sum(len(v) for v in runs.values())}))


if __name__ == '__main__':
    main()
