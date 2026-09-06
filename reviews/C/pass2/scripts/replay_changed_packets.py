#!/usr/bin/env python3
"""Bounded exact-SHA packet replay. This is not an RH or asymptotic proof."""
from __future__ import annotations
import hashlib
import json
import os
import platform
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    'pr568_recorded': 'c946104810907deb55db18a4f2897e28618a04db',
    'pr568_current': 'f0e8f85e195162d745477cfb69e68b9b24443289',
    'pr599': '121a2767b0e9fe8ed0d76d6146f11807b9a4b587',
}
RESULT_BLOBS = {
    'pr568_recorded': 'faac15c97c7c39a118f5f8cf4473c9e4e22e30e4',
    'pr568_current': '16236ebf67030b3c81178ec0077c3f69e137ef0d',
    'pr599': '7082465f6e1c37bf594318528b07b7cf84d64b14',
}

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def main() -> None:
    cases = []
    outputs = {}
    for name, expected in TARGETS.items():
        source = (ROOT / 'replay/references' / name / 'verify.py').read_bytes()
        if blob(source) != expected:
            raise ValueError('source hash mismatch: ' + name)
        for optimized in (False, True):
            with tempfile.TemporaryDirectory(prefix='review-c-packet-') as tmp:
                path = Path(tmp)
                (path/'verify.py').write_bytes(source)
                cmd = [sys.executable, '-I'] + (['-O'] if optimized else []) + ['verify.py']
                proc = subprocess.run(cmd, cwd=path, text=True, capture_output=True,
                                      env={'PATH': os.defpath, 'LC_ALL': 'C.UTF-8'}, timeout=5)
                output = path/'results/verification.json'
                data = output.read_bytes() if output.is_file() else b''
                if proc.returncode or not data:
                    raise RuntimeError(name + ': replay failed: ' + proc.stderr)
                outputs[name,optimized] = data
                cases.append({'case': name, 'optimized': optimized,
                              'command': ['python', '-I'] + (['-O'] if optimized else []) + ['verify.py'],
                              'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr,
                              'source_git_blob': expected, 'output_git_blob': blob(data),
                              'retained_git_blob': RESULT_BLOBS[name],
                              'output_matches_retained_bytes': blob(data)==RESULT_BLOBS[name],
                              'output_sha256': hashlib.sha256(data).hexdigest()})
                if not optimized:
                    retained = ROOT / 'replay/reproduced' / name / 'verification.json'
                    retained.parent.mkdir(parents=True,exist_ok=True)
                    retained.write_bytes(data)
        if outputs[name,False] != outputs[name,True]:
            raise ValueError('normal/optimized output differs: '+name)
    if outputs['pr568_recorded',False] != outputs['pr568_current',False]:
        raise ValueError('PR568 old/new producer outputs differ')
    # Reconstruct only the known formatting change in the old committed artifact.
    old = outputs['pr568_current',False].decode()
    old = re.sub(r'    "([1-8])": \{\n      "current_leading_sign": (-?1),\n      "recursive_parity_canonical": (true|false)\n    \}',
                 r'    "\1": {"current_leading_sign": \2, "recursive_parity_canonical": \3}',old).encode()
    if blob(old) != RESULT_BLOBS['pr568_recorded']:
        raise ValueError('old result formatting reconstruction not authenticated')
    if json.loads(old) != json.loads(outputs['pr568_current',False]):
        raise ValueError('PR568 old/new retained JSON meanings differ')
    payload=json.loads(outputs['pr599',False])
    declared=payload.pop('proof_object_sha256')
    recomputed=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if declared != recomputed:
        raise ValueError('PR599 canonical payload self-digest differs')
    if blob(outputs['pr599',False]) != RESULT_BLOBS['pr599']:
        raise ValueError('PR599 reproduced artifact differs from observed committed blob')
    target=ROOT/'replay/reproduced/pr568_recorded/retained_original_format.json'
    target.write_bytes(old)
    report = {'schema': 'riemann.review.C.packet-replay.v2',
              'python_version': platform.python_version(), 'platform': platform.platform(),
              'subprocesses': len(cases), 'cases': cases,
              'pr568_old_new_producer_outputs_identical': True,
              'pr568_old_new_retained_json_semantically_identical': True,
              'pr568_old_retained_byte_replay_difference': 'JSON formatting only; reconstructed old bytes authenticated',
              'pr599_output_matches_retained_bytes': blob(outputs['pr599',False])==RESULT_BLOBS['pr599'],
              'scope': 'Original bounded fixtures only; exact finite algebra and unverified imported decimal endpoints / floating sanity proxies',
              'pr599_payload_digest_independently_recomputed':recomputed,
              'native_annular_source_recomputed': False, 'asymptotics_verified_by_replay': False,
              'rh_established': False}
    out=ROOT/'reports/changed_packet_replay.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:report[k] for k in ['subprocesses','pr568_old_new_producer_outputs_identical',
                    'pr568_old_new_retained_json_semantically_identical','pr599_output_matches_retained_bytes','rh_established']},sort_keys=True))

if __name__ == '__main__':
    main()
