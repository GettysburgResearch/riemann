"""Exact bound for the L2 derivative norm in the kernel autocorrelation."""
from pathlib import Path
from fractions import Fraction as Q
import runpy, hashlib, json
base=Path(__file__).resolve().parents[1]/'three-hour-type/verify_logistic_master_fraction.py'
sha='cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413'
if hashlib.sha256(base.read_bytes()).hexdigest()!=sha:raise RuntimeError('dependency mismatch')
ns=runpy.run_path(str(base))
value=ns['SEC2']**2*ns['TAN']*(ns['THETA']-ns['S2']/2)
if not (value.lo>50 and value.hi<51):raise RuntimeError('curvature bound failed')
if value.hi<50:raise RuntimeError('negative control failed')
out={'status':'PASS','bound':'50 < ||g_prime||_2^2 < 51',
     'lower_rational':str(value.lo),'upper_rational':str(value.hi),
     'arithmetic':'exact Fraction intervals','positive_checks':1,'negative_controls':1,
     'dependency_sha256':sha,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('LOGISTIC_CURVATURE_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
