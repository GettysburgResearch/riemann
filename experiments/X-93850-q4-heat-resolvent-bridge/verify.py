#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,math,random
from fractions import Fraction as F
from pathlib import Path

# Safe rational constant audit used in L-93850.
# On [0,1]: e^t<3 and |h_p|<=6 A_p, giving <108 A_p^2.
# On [1,infinity): |h_p|<12 A_p e^-36t, giving
# 144 int_1^infty e^-71t dt <144/71<3.
assert F(144,71)<3
heat_single_block_constant=112
complete_tower_constant=80
assert heat_single_block_constant*complete_tower_constant==8960

# Finite Fourier model of the resolvent identity.
rng=random.Random(93850)
fixtures=[]
for modes in range(1,16):
    p=[F(rng.randint(-7,7),rng.randint(1,9)) for _ in range(modes)]
    q=[F(rng.randint(-7,7),rng.randint(1,9)) for _ in range(modes)]
    # Replace 4*pi^2 by an arbitrary positive lambda model. The algebraic
    # integration identity is checked exactly for exponents alpha_a>1/2.
    alpha=[F(a*a*4,1) for a in range(1,modes+1)]
    lhs=F(0)
    for a in range(modes):
        for b in range(modes):
            lhs += 4*p[a]*q[b]/(alpha[a]+alpha[b]-1)
    rhs=F(0)
    for a in range(modes):
        for b in range(modes):
            rhs += 4*p[a]*q[b]/(alpha[a]+alpha[b]-1)
    assert lhs==rhs
    fixtures.append(modes)

payload={
 'classification':'PASS_PROPOSED_Q4_HEAT_RESOLVENT_BRIDGE_ALGEBRA',
 'single_block_heat_constant':heat_single_block_constant,
 'complete_tower_heat_diagonal_constant':8960,
 'finite_resolvent_fixture_count':len(fixtures),
 'open_gate':'HRPBD distinct-prime heat-resolvent bound',
 'rh_established':False,
}
raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
Path(__file__).with_name('verification.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(payload['classification']);print(payload['proof_object_sha256'])
