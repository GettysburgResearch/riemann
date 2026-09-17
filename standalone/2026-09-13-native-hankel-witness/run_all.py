"""Fresh complete source reconstruction followed by the bounded/adverse suite.

Run: python -S -B run_all.py
     python -S -B -O run_all.py
Each command freshly recomputes every one of the 785 gamma cells in eight
subprocesses, plus the theta source and complete analytical suffix. Temporary
partition files are never accepted as a replacement for this reconstruction.
"""
from pathlib import Path
import subprocess, sys, tempfile

ROOT=Path(__file__).resolve().parent


def main():
    flags=['-S','-B']+(['-O'] if sys.flags.optimize else [])
    with tempfile.TemporaryDirectory(prefix='native-hankel-') as folder:
        parts=Path(folder)
        for i in range(8):
            subprocess.run([sys.executable,*flags,str(ROOT/'native_check.py'),
                            '--part',str(i),'--write',str(parts/f'part_{i}.json')],check=True)
        subprocess.run([sys.executable,*flags,str(ROOT/'native_check.py'),
                        '--finish-parts',str(parts),'--check',str(ROOT/'certificate.json')],check=True)
        subprocess.run([sys.executable,*flags,str(ROOT/'test_checks.py'),
                        '--parts',str(parts)],check=True)
    print('COMPLETE_SOURCE_RECONSTRUCTION_AND_TESTS_PASS')


if __name__=='__main__':main()
