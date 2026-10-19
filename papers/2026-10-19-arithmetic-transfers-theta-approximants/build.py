#!/usr/bin/env python3
"""Build the manuscript locally and optionally create a clean arXiv source ZIP."""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parent

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arxiv',type=Path,help='Write a source-only ZIP after a successful build.')
    args=parser.parse_args()
    executable=shutil.which('pdflatex')
    if not executable:
        raise SystemExit('pdfLaTeX was not found. Install a standard TeX distribution first.')
    subprocess.run([sys.executable,'-I','-S','-B',str(ROOT/'verify_paper.py')],check=True,cwd=ROOT)
    for iteration in range(3):
        result=subprocess.run([executable,'-interaction=nonstopmode','-halt-on-error',
                              '-no-shell-escape','main.tex'],cwd=ROOT,capture_output=True,text=True,timeout=180)
        if result.returncode:
            sys.stderr.write(result.stdout[-12000:]+result.stderr)
            raise SystemExit(f'pdfLaTeX pass {iteration+1} failed. Inspect main.log.')
    log=(ROOT/'main.log').read_text(errors='replace')
    forbidden=[r'LaTeX Warning: (?:Reference|Citation) .* undefined',
               r'There were undefined references',r'Overfull \\[hv]box',r'^!']
    for pattern in forbidden:
        if re.search(pattern,log,re.MULTILINE):
            raise SystemExit('Build preflight failed: '+pattern+'; inspect main.log.')
    print('Built',ROOT/'main.pdf')
    if args.arxiv:
        archive=args.arxiv.expanduser().resolve()
        if archive.exists():
            raise SystemExit(f'Refusing to overwrite existing archive: {archive}')
        files=[ROOT/'main.tex',ROOT/'main.bbl',ROOT/'references.bib']+sorted((ROOT/'sections').glob('*.tex'))
        archive.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for file in files:
                z.write(file,file.relative_to(ROOT).as_posix())
        print('Wrote',archive,'with',len(files),'local source files; no PDF, logs, or font files.')

if __name__=='__main__':
    main()
