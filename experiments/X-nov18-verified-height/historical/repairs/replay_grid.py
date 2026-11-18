"""Rebuild the additional sign sampler against the original verified Platt tree."""
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
REV = "d918aa093a304819a0f7d1c27bfaf67c8c0f0602"
START = "3000175658500"
STEP = 504
PRECISION = 144


def run(work, output):
    src = work / 'platt-original'
    libs = work / 'old-libs'
    inc = libs / 'usr/include'
    shared = libs / 'usr/lib/x86_64-linux-gnu'
    if (subprocess.check_output(['git','-C',src,'rev-parse','HEAD'],text=True).strip() != REV
            or subprocess.run(['git','-C',src,'diff','--quiet',REV]).returncode):
        raise RuntimeError('Expected exact historical source')
    code = (src/'arb_zeta.c').read_text()
    anchor = '      // use Turing\'s method to check all zeros accounted for'
    if code.count(anchor) != 1:
        raise ValueError('Missing original insertion location')
    code = code.replace(anchor, (HERE/'sample-grid.c').read_text() + '\n' + anchor)
    env = dict(os.environ, LD_LIBRARY_PATH=str(shared))
    with tempfile.TemporaryDirectory() as temp:
        d = Path(temp)
        (d/'sampler.c').write_text(code)
        sources = ['arb_fft.c', 'inter.c', 'turing.c', 'win_zeta.c']
        binpath = d/'arb_zeta'
        subprocess.run(['gcc','-O2',f'-I{inc}',f'-I{inc/"flint"}',f'-I{src}',
                        d/'sampler.c',*(src/f for f in sources),f'-L{shared}',
                        f'-Wl,-rpath-link,{shared}','-lflint-arb','-lflint','-lm',
                        '-o',binpath],env=env,check=True)
        proc=subprocess.run([binpath,str(PRECISION),START,'1',str(STEP)],env=env,
                            capture_output=True,text=True,check=True)
    # Remove path and timing so the certificate replays byte-for-byte.
    stable = [line for line in proc.stdout.splitlines()
              if line.startswith(('Grid signs /8:', 'looking for ', 'All ', 'Missed '))]
    body=f'{START} {STEP} {PRECISION}\n'+'\n'.join(stable)+'\n'
    if output.exists() and output.read_text()!=body:
        raise RuntimeError('Mismatch against archived sign packet')
    if not output.exists():
        output.write_text(body)
    print(hashlib.sha256(body.encode()).hexdigest(), output)


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('work', type=Path)
    p.add_argument('--output',type=Path,default=HERE/'triple.tsv')
    args=p.parse_args()
    run(args.work.resolve(),args.output)
