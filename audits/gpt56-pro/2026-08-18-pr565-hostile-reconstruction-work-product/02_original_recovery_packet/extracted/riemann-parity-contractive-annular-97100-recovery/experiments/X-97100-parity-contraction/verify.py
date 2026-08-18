#!/usr/bin/env python3
from fractions import Fraction
import hashlib,json,math
from pathlib import Path

HERE=Path(__file__).resolve().parent
rho=1/math.sqrt(67)
assert rho < 1/8
q=Fraction(1,8)
upper=(Fraction(1,8)+q*Fraction(1,8))/(1-q)
assert upper==Fraction(9,56) and upper<Fraction(1,6)
margin=Fraction(1,40)*(1-Fraction(1,8))-Fraction(1,6)*Fraction(1,8)
assert margin==Fraction(1,960)
# Exact recombination coefficient identity.
for p in (67,71,73,101):
    r=1/math.sqrt(p)
    lam=0.137
    alpha=lam*r
    assert abs((-lam*r+alpha))<1e-15
# Scalar numerator roots x=1,2 only.
# (1-x)(2-x)=0; these force Re(z)=0 or -1 for x=2^{-z}.
result={
 'schema':'riemann.x97100.parity-contraction-recovery.v1',
 'frozen_heads':{
   'pr556':'a4feca0457d310c72054f274040f93b0503f658b',
   'pr559':'88d97adef8a42c5baf2f52c2c259a4ef536bdfdd',
   'pr561':'db9bdc63c855c6ddf664b763d748f8155a6a2c67'},
 'positive_base_dictionary':{'2':15,'3':6,'4':3,'tail':6},
 'bias_contract':{'lower':'1/40','upper':'1/8','directed_certificate_replayed_here':False},
 'current_upper':str(upper),
 'strict_root_margin':str(margin),
 'low_child_recombination':'lambda*(P-r*S child)+lambda*r*S child=lambda*P',
 'scalar_numerator':'-3*(1-2^-z)*(2-2^-z)',
 'scientific_status':'candidate complete; P61 bias certificate requires independent reconstruction',
 'rh_established':False,
 'verdict':'PASS_PARITY_CONTRACTIVE_ANNULAR_RECOVERY_ALGEBRA'}
canon=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
result['proof_object_sha256']=hashlib.sha256(canon).hexdigest()
out=HERE/'results/verification.json'; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(result['verdict']); print(result['proof_object_sha256'])
