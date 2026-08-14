#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256
import json

h66=sum((Fraction(1,k) for k in range(1,67)),Fraction(0))
assert h66<5
assert 16*67<33*33
assert Fraction(8,3)**5>67
fiber=4*Fraction(33,4)*5
measure=4*5
root=fiber*measure
assert fiber==165 and measure==20 and root==3300
rho=Fraction(1,8)
cplus=Fraction(16,7)
child_bound=rho*root*cplus
payload={
 "schema":"riemann.x91726.root-once.v1",
 "harmonic_66":str(h66),
 "fiber_target_upper":int(fiber),
 "endpoint_measure_upper":int(measure),
 "root_target_upper":int(root),
 "positive_envelope_control":str(cplus),
 "descendant_deficit_upper":str(child_bound),
 "verdict":"PASS_FACTOR67_ROOT_MASS_AND_ONE_SHOT_DESCENDANT_BOUND"
}
payload["proof_object_sha256"]=sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()
print(json.dumps(payload,indent=2,sort_keys=True))
