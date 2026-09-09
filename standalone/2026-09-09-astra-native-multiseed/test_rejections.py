"""Run a pristine full replay and ten actual CLI rejection cases."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def seal(root):
    lines = [sha256(p.read_bytes()).hexdigest()+'  '+p.name
             for p in sorted(root.iterdir()) if p.name != 'SHA256SUMS']
    (root/'SHA256SUMS').write_text('\n'.join(lines)+'\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--optimized', action='store_true')
    args = parser.parse_args()
    command = [sys.executable, '-I', '-S', '-B'] + (['-O'] if args.optimized else [])
    names = ['false_rh', 'duplicate_key', 'boolean_alias', 'float_alias',
             'wrong_energy', 'missing_file', 'extra_file', 'symlink_proof',
             'wrong_source', 'changed_proof_bytes']
    receipts = []
    with tempfile.TemporaryDirectory(prefix='nm26-adverse-') as tmp:
        for name in ['pristine'] + names:
            out = Path(tmp)/name
            shutil.copytree(ROOT, out)
            result = out/'result.json'
            data = json.loads(result.read_text())
            if name == 'false_rh':
                data['rh_proved'] = True
                result.write_text(json.dumps(data)); seal(out)
            elif name == 'duplicate_key':
                result.write_text('{"rh_proved":false,'+result.read_text().lstrip()[1:]); seal(out)
            elif name == 'boolean_alias':
                data['seed']['horizon'] = True
                result.write_text(json.dumps(data)); seal(out)
            elif name == 'float_alias':
                data['seed']['horizon'] = float(data['seed']['horizon'])
                result.write_text(json.dumps(data)); seal(out)
            elif name == 'wrong_energy':
                data['seed']['seed_energy_interval'][1] = ['1', '1000']
                result.write_text(json.dumps(data)); seal(out)
            elif name == 'missing_file':
                (out/'SEED.md').unlink()
            elif name == 'extra_file':
                (out/'EXTRA').write_text('not selected')
            elif name == 'symlink_proof':
                (out/'PROOF.md').unlink()
                (out/'PROOF.md').symlink_to(ROOT/'PROOF.md')
            elif name == 'wrong_source':
                source = out/'verify.py'
                before = source.read_text()
                after = before.replace('NUM = (562949953421312,', 'NUM = (562949953421313,', 1)
                if before == after:
                    raise ValueError('mutation did not change source')
                source.write_text(after); seal(out)
            elif name == 'changed_proof_bytes':
                with (out/'PROOF.md').open('a') as file:
                    file.write('\nchanged\n')
            proc = subprocess.run(command+['verify.py', '--check', 'result.json'],
                                  cwd=out, capture_output=True, text=True, timeout=90)
            expected = 0 if name == 'pristine' else 2
            if proc.returncode != expected:
                raise ValueError(name+': unexpected return '+str(proc.returncode)+' '+proc.stderr)
            if name != 'pristine' and not proc.stderr.startswith('REJECT: '):
                raise ValueError(name+': missing refusal diagnostic')
            receipts.append({'case': name, 'returncode': proc.returncode})
    print(json.dumps({'optimized': args.optimized, 'cases': receipts}, sort_keys=True))


if __name__ == '__main__':
    main()
