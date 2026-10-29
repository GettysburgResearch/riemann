"""Exact bottleneck dominance of every admissible cap from PR94's count face."""
import argparse, hashlib
from pathlib import Path
import sympy as s
p=argparse.ArgumentParser();p.add_argument('--formulas',required=True);a=p.parse_args()
assert hashlib.sha256(Path(a.formulas).read_bytes()).hexdigest()=='e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b'
R=s.Rational; D=R(223,500); p=R(1,2); B=R(96232839,100000000); L=R(3853,2000); v=R(5,6)-D; z=s.symbols('z',real=True)
d=3-p; J=v*d+D*(1-p)*2; T=J+D*(1-p)*(1-2*p*z); RN=2*T+(2*p*z-p)*J; M=d*T-RN; DJ=d*J
plain_guard=s.factor((B-L*z)/2-M/DJ)
count_cap=s.factor(1-D+v*D*(1-p)*(1-2*p*z)/J)
count_C=R(137478360780643,225606975000000)
diff=s.factor(count_cap-count_C)
assert s.factor(plain_guard+(451213950000*z-42115935877)/848600000000)==0
assert s.factor(diff+129563*(451213950000*z-42115935877)/957250394925000000)==0
assert s.factor(diff/plain_guard)>0
zstar=R(42115935877,451213950000)
assert plain_guard.subs(z,zstar)==0 and diff.subs(z,zstar)==0
print('plain guard:',plain_guard)
print('capped count minus C:',diff)
print('ratio:',s.factor(diff/plain_guard))
print('equality cap:',zstar,'≈',float(zstar))
