#!/usr/bin/env python3
"""Eight actual CLI corruption refusals in temporary copies of the packet.

Running this script under -O also runs its subprocesses under -O. Source
files in the delivered packet are never mutated. Rehashed semantic/data
mutations must still be refused, independently of the manifest checksum.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def manifest(root: Path) -> None:
    paths = sorted(p for p in root.rglob('*') if p.is_file()
                   and '__pycache__' not in p.parts and p.name != 'SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()
                                         +'  '+str(p.relative_to(root))+'\n' for p in paths))


def main() -> int:
    modes = ['-O'] if sys.flags.optimize else []
    cases = [('rh_flag','RH flag'),('gain_flag','uniform gain flag'),
             ('bool_config','frozen config drift'),('float_alias','floating/NaN'),
             ('duplicate_key','duplicate JSON key'),('interval_endpoint','does not equal reconstructed'),
             ('proof_bytes','changed bytes PROOF.md'),('unlisted_path','coverage drift')]
    for label, expected in cases:
        with tempfile.TemporaryDirectory(prefix='dilation_mutation_') as t:
            target = Path(t)/'packet'
            shutil.copytree(ROOT,target,ignore=shutil.ignore_patterns('__pycache__'))
            p=target/'verification.json'
            data=json.loads(p.read_text())
            if label=='rh_flag':
                data['rh_proved']=True
            elif label=='gain_flag':
                data['uniform_gain_proved']=True
            elif label=='bool_config':
                data['config']['max_n']=True
            elif label=='float_alias':
                data['config']['max_n']=16.0
            elif label=='interval_endpoint':
                cell=data['projections'][0]['delta']
                cell['lo']=str(int(cell['lo'])+1)
            if label in {'rh_flag','gain_flag','bool_config','float_alias','interval_endpoint'}:
                p.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
                manifest(target)
            elif label=='duplicate_key':
                p.write_text(p.read_text().replace('{','{"rh_proved": false,',1))
                manifest(target)
            elif label=='proof_bytes':
                proof=target/'PROOF.md'
                proof.write_text(proof.read_text()+'\nMUTATION\n')
            elif label=='unlisted_path':
                (target/'unlisted.txt').write_text('not in the manifest\n')
            cmd=[sys.executable,*modes,'-I','-S','-B',str(target/'scripts/replay.py'),'--check']
            result=subprocess.run(cmd,capture_output=True,text=True,timeout=45)
            text=result.stdout+result.stderr
            if result.returncode==0 or expected not in text:
                raise RuntimeError(f'corruption {label} not refused for intended reason: {text}')
            print(f'REFUSAL_VERIFIED {label}: {text.strip()}')
    print(f'PASS_ACTUAL_CLI_CORRUPTION_REFUSALS cases={len(cases)} optimized={bool(modes)}')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
