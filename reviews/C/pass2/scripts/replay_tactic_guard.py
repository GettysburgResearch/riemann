#!/usr/bin/env python3
"""Exercise only the real GNU grep policy expression; no Lean compilation claimed."""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = 'b1ef22a399fd9b2a8f8eab6c8eaf53d4da6a410b'
OLD = r'\b(by\?|exact\?|apply\?|simp\?|aesop\?)\b'
# Candidate lexical correction, not a complete Lean lexer or production patch.
CANDIDATE = r"\b(?:by|exact|apply|simp|aesop)\?(?![A-Za-z0-9_'])"

def main() -> None:
    source=(ROOT/'replay/references/formal/check_no_sorry.sh').read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(source)).encode()+b'\0'+source).hexdigest()
    if actual != EXPECTED or OLD not in source.decode():
        raise ValueError('guard source is not the pinned file')
    fixtures=[{'text': t+end, 'expected_lexical_match': True}
              for t in ['by?', 'exact?', 'apply?', 'simp?', 'aesop?']
              for end in ['\n', ' h\n']]
    fixtures += [{'text': t+'\n', 'expected_lexical_match': False}
                 for t in ['by', 'exact h', 'simp', 'myexact?', 'apply?x']]
    results=[]
    for fixture in fixtures:
        row=dict(fixture)
        for name,pattern in [('baseline',OLD),('candidate',CANDIDATE)]:
            proc=subprocess.run(['grep','-nP',pattern],input=fixture['text'],text=True,
                                capture_output=True,timeout=5)
            if proc.returncode not in [0,1]:
                raise RuntimeError(proc.stderr)
            row[name+'_matches']=proc.returncode==0
            row[name+'_exit_code']=proc.returncode
            row[name+'_stdout']=proc.stdout
            row[name+'_stderr']=proc.stderr
        results.append(row)
    candidate_ok=all(r['candidate_matches']==r['expected_lexical_match'] for r in results)
    if not candidate_ok:
        raise ValueError('candidate did not pass the bounded fixtures')
    report={'schema':'riemann.review.C.lexical-guard.v1','source_git_blob':EXPECTED,
            'subprocesses':len(results)*2,'baseline_pattern':OLD,'candidate_pattern':CANDIDATE,
            'baseline_false_negatives':sum(r['expected_lexical_match'] and not r['baseline_matches'] for r in results),
            'baseline_false_positives':sum(not r['expected_lexical_match'] and r['baseline_matches'] for r in results),
            'candidate_all_fixtures_pass':candidate_ok,'fixtures':results,
            'gnu_grep_version':subprocess.check_output(['grep','--version'],text=True).splitlines()[0],
            'whole_release_script_executed':False,'lean_executed':False,
            'kernel_unsoundness_claimed':False,
            'scope':'Lexical policy guard only. Candidate still scans comments and strings; not a Lean parser.'}
    (ROOT/'reports/tactic_guard_replay.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:report[k] for k in ['subprocesses','baseline_false_negatives','baseline_false_positives','candidate_all_fixtures_pass','kernel_unsoundness_claimed']}))

if __name__=='__main__':
    main()
