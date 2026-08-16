from pathlib import Path
import json, subprocess, sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/'verify.py'),'--limit','200000','--output',str(root/'results/test-verification.json')],check=True)
d=json.loads((root/'results/test-verification.json').read_text())
assert d['verdict'].startswith('PASS')
assert d['rh_established'] is False
assert d['two_row_noncancellation']['open_strip_common_zero'] is False
assert d['normalization_counterexample']['proved_upper_bound']=='-289/5000'
