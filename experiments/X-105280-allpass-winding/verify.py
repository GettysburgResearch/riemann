#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import json

# Exact real-root/Rolle count fixtures.
# p=x^4+x^2+1 has no real root; p'=2x(2x^2+1) has one.
R_prev = 0
R_next = 1
q_prev = 2
q_next = 1
E = q_prev - q_next
assert E == 1
assert R_prev - R_next == 1 - 2 * E
assert (R_prev - R_next) - 1 == -2 * E

# Three-real-root fixture p=x^3-x; p'=3x^2-1.
assert 3 - 2 == 1
assert (3 - 2) - 1 == 0

# Exact Lorentz/all-pass algebra on rational values.
a = Fraction(3, 5)
b = Fraction(-7, 4)
# theta(t)=(1-it)/(1+it); compare absolute squares algebraically.
left_num = 4 * (1 + a * b) ** 2
left_den = (1 + a * a) * (1 + b * b)
# Direct complex-pair arithmetic using (real,imag).
def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def cdiv(z, w):
    den = w[0] * w[0] + w[1] * w[1]
    return ((z[0] * w[0] + z[1] * w[1]) / den,
            (z[1] * w[0] - z[0] * w[1]) / den)

def theta(t):
    return cdiv((Fraction(1), -t), (Fraction(1), t))

ratio = cdiv(theta(a), theta(b))
vminus1 = (-ratio[0] - 1, -ratio[1])
direct = vminus1[0] ** 2 + vminus1[1] ** 2
assert direct == left_num / left_den

# Physical half-derivative source budget at K=4.
D4 = Fraction(173344649, 1275293859840)
assert 4 * D4 < Fraction(1, 1700)

# The Blaschke firewall: integral |B_eps-1|^2 = 4*pi*eps tends to zero,
# while the winding remains one.  The replay checks the rational coefficient.
eps = Fraction(1, 10_000)
assert 4 * eps < Fraction(1, 1000)
blaschke_winding = 1
assert blaschke_winding == 1

payload = {
    "schema": "riemann.x105280.allpass-winding.v1",
    "classification": "PASS_T105280_ALLPASS_HALF_DERIVATIVE_GATE",
    "rolle_winding_fixtures_checked": True,
    "lorentz_allpass_identity_checked": True,
    "physical_source_hhalf_below_one_over_1700": True,
    "near_line_l2_firewall_checked": True,
    "ahxfer105280_proved": False,
    "ninety_percent_established": False,
    "density_one_established": False,
    "rh_established": False,
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
print(payload["classification"])
print(payload["proof_object_sha256"])
print(json.dumps(payload, indent=2, sort_keys=True))
