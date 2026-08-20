#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math
from pathlib import Path

VERDICT = "PASS_T100100_TWO_ROUTE_CLOSURE_SYNTHESIS"

def primes_upto(n: int) -> list[int]:
    a = bytearray(b"\x01") * (n + 1)
    a[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if a[p]:
            a[p*p:n+1:p] = b"\x00" * (((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if a[i]]

def kappa(y: float) -> float:
    return 16.0 if y < 1.0 else 24.0/math.sqrt(y)-9.0/y

def psi(y: float) -> float:
    return 64.0*(3*y-y**1.5) if y <= 1 else 64.0*(3*math.sqrt(y)-1)

def main() -> None:
    completion_checks = 0
    for k in range(2,9):
        # (1-x)(1+x+...+x^(k-1)) = 1-x^k
        lhs = [0]*(k+1)
        for j in range(k):
            lhs[j] += 1
            lhs[j+1] -= 1
        want = [0]*(k+1); want[0]=1; want[-1]=-1
        assert lhs == want
        completion_checks += 1

    harnack_checks = 0
    for p in (2,3,5,7,67,101):
        for y in (0.125,0.5,0.999999,1.0,1.000001,p-1e-6,float(p),p+1e-6,10*p,1e5):
            assert p**-1.5*kappa(y/p) <= p**-1*kappa(y) + 1e-10
            assert p**-0.5*psi(y/p) <= p**-1*psi(y) + 1e-8
            harnack_checks += 2

    ps = primes_upto(200000)
    exponents = {}
    for k in range(2,7):
        pk = sum(p**(-k) for p in ps)
        exponents[k] = math.exp(math.asinh(1)-pk-67**(-k))
    assert all(exponents[k+1] > exponents[k] for k in range(2,6))
    assert all(v < 1+math.sqrt(2) for v in exponents.values())

    zero_free_checks = 0
    for k in range(2,6):
        for sig in (0.1,0.5,0.75,1.0):
            for gam in (0.0,1.0,14.0):
                z = complex(sig,gam)
                value = 1+0j
                for p in (2,3,5,67):
                    value *= sum(p**(-j*z) for j in range(k))
                assert abs(value) > 1e-12
                zero_free_checks += 1

    core = {
        "schema":"riemann.x100100.two-route-synthesis.v1",
        "classification":VERDICT,
        "completion_checks":completion_checks,
        "carrier_harnack_checks":harnack_checks,
        "finite_multiplier_zero_free_checks":zero_free_checks,
        "corridor_exponent_diagnostics":{str(k):exponents[k] for k in exponents},
        "limiting_corridor_exponent":1+math.sqrt(2),
        "dce100100_proved":False,
        "qpet100101_proved":False,
        "rh_established":False,
    }
    canon=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    result={**core,"proof_object_sha256":hashlib.sha256(canon).hexdigest()}
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(VERDICT)
    print(result["proof_object_sha256"])

if __name__ == "__main__":
    main()
