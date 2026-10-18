#!/usr/bin/env python3
"""Replay the frozen finite checks, eight actual corruptions and byte manifest.
No network, external packages, or repository-wide CI are used.
"""
from __future__ import annotations
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT=pathlib.Path(__file__).resolve().parent
MUTANTS={
    "erase_projection":"primitive_projection",
    "wrong_mass":"matrix_polynomial_identity",
    "drop_prime_powers":"complete_prime_power_height",
    "unsigned_mobius":"complete_unit_corrected_regrouping",
    "omit_unit":"complete_unit_corrected_regrouping",
    "gram_factor":"gram_valuation_layers",
    "lose_conjugate":"conjugate_disk_identity",
    "wrong_continuum":"one_sided_continuum",
}

def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)

def run_check(arguments: list[str], optimized: bool=False) -> subprocess.CompletedProcess:
    cmd=[sys.executable,"-B"]+(["-O"] if optimized else [])+[str(ROOT/"verify.py")]+arguments
    return subprocess.run(cmd,cwd=ROOT,capture_output=True,timeout=120,check=False)

def main() -> int:
    expected=(ROOT/"CHECKS.json").read_bytes()
    for optimized in (False,True):
        out=run_check([],optimized)
        require(out.returncode==0,"positive replay failed: "+out.stderr.decode())
        require(out.stdout==expected,"archived CHECKS.json mismatch")
    mutations={}
    for name,gate in MUTANTS.items():
        out=run_check(["--mutant",name],True)
        require(out.returncode==2,"mutation did not fail as intended: "+name)
        require(out.stderr.decode().strip()=="REJECT:"+gate,"mutation failed at wrong gate: "+name)
        mutations[name]={"returncode":out.returncode,"gate":gate}
    require(mutations==json.loads((ROOT/"MUTATIONS.json").read_text()),"mutation archive mismatch")
    entries={}
    for line in (ROOT/"SHA256SUMS").read_text().splitlines():
        digest,name=line.split("  ",1)
        require(name not in entries,"duplicate manifest entry")
        p=ROOT/name
        require(p.resolve().is_relative_to(ROOT),"unsafe manifest path")
        require(p.is_file() and not p.is_symlink(),"missing regular payload: "+name)
        require(hashlib.sha256(p.read_bytes()).hexdigest()==digest,"manifest mismatch: "+name)
        entries[name]=digest
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and p.name!='SHA256SUMS'}
    require(set(entries)==actual,"manifest does not cover the exact regular payload set")
    report={"status":"PASS_FINITE_REPLAY","positive_modes":["ordinary","optimized"],
            "corrupted_processes_rejected":mutations,"manifested_payloads":len(entries),
            "finite_predicates":json.loads(expected)["predicates"],
            "analytic_proof_certified":False,"remote_publication":False}
    print(json.dumps(report,indent=2,sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
