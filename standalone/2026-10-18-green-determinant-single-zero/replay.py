#!/usr/bin/env python3
"""Replay the declared finite checks and seven optimized corrupted controls."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
FILES = {
    'IMPORT.md', 'README.md', 'RECTANGULAR_JETS.md', 'ZERO_PRESERVING_ROUTE.md',
    'REVIEW.md', 'VALIDATION.md', 'sources/GREEN_NOTE.md',
    'verify.py', 'replay.py', 'CHECKS.json',
}
MUTATIONS = {
    'hasse':'ordinary_derivatives', 'factor-two':'valuation_template',
    'unsigned':'primitive_integer', 'prime-powers':'primitive_integer',
    'continuum':'one_sided_continuum', 'common-zero':'common_zero_residue',
    'multiplicity':'zero_multiplicity',
}
PDF_HASH = 'd0363f662b297094aca967f23035c8a7b66ba94fcbe708a64a36b5f38fe5c098'


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pdf',type=Path,help='Optionally authenticate the unchanged supplied PDF')
    args = ap.parse_args()
    try:
        entries = {}
        for line in (ROOT/'SHA256SUMS').read_text().splitlines():
            digest,name = line.split('  ',1)
            require(name in FILES and name not in entries,'invalid manifest path')
            require(len(digest)==64 and all(x in '0123456789abcdef' for x in digest),
                    'invalid digest')
            entries[name] = digest
        require(set(entries)==FILES,'incomplete manifest')
        for name,digest in entries.items():
            p = ROOT/name
            require(p.is_file() and not p.is_symlink(),'missing/symlink payload')
            require(p.resolve().is_relative_to(ROOT),'path escape')
            require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'hash mismatch: '+name)
        wanted = (ROOT/'CHECKS.json').read_bytes()
        for options in [[],['-O']]:
            p = subprocess.run([sys.executable,'-B',*options,str(ROOT/'verify.py')],
                               cwd=ROOT,capture_output=True,timeout=45)
            require(p.returncode==0 and p.stdout==wanted and not p.stderr,
                    'positive replay mismatch')
        outcomes = {}
        for mutation,stage in MUTATIONS.items():
            p = subprocess.run([sys.executable,'-B','-O',str(ROOT/'verify.py'),
                                '--mutate',mutation],cwd=ROOT,capture_output=True,timeout=45)
            require(p.returncode==1 and p.stderr==('FAILED:'+stage+'\n').encode()
                    and not p.stdout,'negative control failed: '+mutation)
            outcomes[mutation] = stage
        pdf = 'not requested; not stored in Git text import'
        if args.pdf:
            raw = args.pdf.read_bytes()
            require(len(raw)==259286 and hashlib.sha256(raw).hexdigest()==PDF_HASH,
                    'original PDF mismatch')
            pdf = 'original bytes match'
        report = {'status':'PASS_FINITE_REPLAY','manifested_payloads':len(FILES),
                  'positive_modes':['ordinary','optimized'],
                  'corrupted_processes_rejected':outcomes,
                  'pdf':pdf,'analytic_proof_certified':False}
        print(json.dumps(report,sort_keys=True,indent=2))
        return 0
    except (ValueError,OSError,subprocess.TimeoutExpired) as exc:
        print('REPLAY_FAILED:'+str(exc),file=sys.stderr)
        return 1

if __name__=='__main__':
    raise SystemExit(main())
