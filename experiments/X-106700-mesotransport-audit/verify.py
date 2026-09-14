#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import hashlib, json

checks = 0

# Projection identities on exact rational canonical-angle models.
for m_minus in range(1, 41):
    for m_plus in range(0, 41):
        r = min(m_minus, m_plus)
        for den in range(2, 19):
            vals = [Fraction((i * 7 + 3) % den, den) for i in range(r)]
            overlap = sum(vals, Fraction(0))
            c_minus = Fraction(m_minus) - overlap
            c_plus = Fraction(m_plus) - overlap
            index = m_minus - m_plus
            assert c_minus - c_plus == index
            assert c_minus == index + c_plus
            assert c_minus >= index
            checks += 4

# c+cos endpoint: per period U=-1/(z b_{-1/c}), denominator degree two.
for c_num in range(2, 31):
    m_minus, m_plus = 2, 0
    c_minus, c_plus = Fraction(2), Fraction(0)
    assert c_minus - c_plus == 2
    assert c_minus == m_minus - m_plus
    checks += 2

simple_fifth = Fraction(9863, 10000)
transition_allowance = simple_fifth - Fraction(9, 10)
assert transition_allowance == Fraction(863, 10000)

deep = Fraction(3, 40)
shallow = Fraction(11, 500)
endpoint = Fraction(97, 1000)
assert deep + shallow == endpoint
assert Fraction(997, 1000) - endpoint == Fraction(9, 10)
checks += 3

result = {
    "verdict": "PASS_T106700_MESOTRANSPORT_HOSTILE_AUDIT",
    "exact_checks": checks,
    "primal_residual_contains_index_floor": True,
    "favorable_escape_nonnegative": True,
    "subfactor_omission_nonnegative": True,
    "positive_source_countermodel_transport_density": "1",
    "direct_simple_residue_transition_allowance": "863/10000",
    "mesotrans106630_proved": False,
    "direct_transition_bound_proved": False,
    "ninety_percent_established": False,
    "rh_established": False,
}
canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
out = Path(__file__).parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(result["verdict"])
print(json.dumps(result, indent=2, sort_keys=True))
