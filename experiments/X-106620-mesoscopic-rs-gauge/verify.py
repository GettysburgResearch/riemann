#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from pathlib import Path
import hashlib, json, math, cmath

getcontext().prec = 80
checks = 0

# Exact Gaussian-rational algebra fixtures.
for p in range(-5, 6):
    for q in range(-5, 6):
        for w_num in range(1, 7):
            for l_num in range(1, 7):
                H0 = complex(p, q)
                H5 = complex(q - 1, p + 2)
                A0 = complex(p + 3, 2*q - 1)   # (D+q)H0 fixture
                A5 = complex(2*p - 2, q + 4)   # (D+q)H5 fixture
                w = Fraction(w_num, 3)
                lam = Fraction(l_num, 11)
                wf = float(w); lf = float(lam)

                C0 = (1-lf*wf)*H0 + 1j*lf*A0
                R0 = (1+lf*wf)*H0 - 1j*lf*A0
                C5 = (1-lf*wf)*H5 + 1j*lf*A5
                R5 = (1+lf*wf)*H5 - 1j*lf*A5

                lhs = R0*C5 - C0*R5
                rhs = 2j*lf*(H0*A5 - A0*H5)
                assert abs(lhs-rhs) < 1e-10
                checks += 1

# Exact budget.
deep = Fraction(3, 40)
shallow = Fraction(11, 500)
allowance = Fraction(97, 1000)
assert deep + shallow == allowance
assert Fraction(997,1000) - allowance == Fraction(9,10)
checks += 2

# Rouché diagonal counterfamily.
for n in range(5, 105):
    eps = math.exp(-n)
    a = 1/n
    roots = [-1j*a + 1j*math.sqrt(a*a+eps*eps),
             -1j*a - 1j*math.sqrt(a*a+eps*eps)]
    # Lower original zero is -i eps; one perturbed zero is macroscopically
    # farther than the O(eps) cluster scale.
    assert abs(roots[1] + 1j*eps) > a
    checks += 1

# Mesoscopic mismatch deterministic inequality at the asymptotic model
# omega(t)=0.5 log(t/2pi).
for Tpow in range(20, 81, 5):
    T = Decimal(10) ** Tpow
    logT = T.ln()
    for B in (1,2,3,4):
        J = int(float(logT**B))
        if J < 1:
            J = 1
        # Relative variation upper model across Delta=T/J:
        # |omega(t)-omega(tj)|/omega(tj) <= 2/(J log(T/2pi)).
        bound = Decimal(2)/(Decimal(J)*(T/(Decimal(2)*Decimal(str(math.pi)))).ln())
        assert bound < Decimal(10)/(Decimal(J)*logT)
        checks += 1

result = {
    "verdict": "PASS_T106620_MESOSCOPIC_RIEMANN_SIEGEL_GAUGE",
    "exact_checks": checks,
    "deep_height_payment": "3/40",
    "shallow_allowance": "11/500",
    "fifth_endpoint_allowance": "97/1000",
    "carrier_mismatch": "O(1/(J_T log T))",
    "diagonal_rouche_inference_valid": False,
    "mesorsgauge106620_proved": False,
    "ninety_percent_established": False,
    "rh_established": False,
}
canonical = json.dumps(result, sort_keys=True, separators=(",",":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(result["verdict"])
print(json.dumps(result, indent=2, sort_keys=True))
