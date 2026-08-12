#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    r, z = sp.symbols("r z", positive=True)
    checks = 0

    d = r*(1-r)
    T0 = 4*z-3
    S0 = 5*z-3
    Tc = r*(4*r*z-3)
    Sc = r*(5*r*z-3)
    Ta = sp.expand(T0-Tc)
    Sa = sp.expand(S0-Sc)

    Ts = (1-r)*(r+3)*(2*(r+2)/(r+3)*z-1)
    Th = r*(r+2)*(2*(r+1)/(r+2)*z-1)
    Ss = (1-r**2)*(5*z-3)
    Sh = r*((4*r+1)*z-(2*r+1))

    identities = [
        T0 - Ts - Th,
        S0 + d*(z-1) - Ss - Sh,
        Ta - Ts - d*(2*z+1),
        Th - Tc - d*(2*z+1),
        Sa - Ss - 3*d,
        Sh - Sc - d*(z+2),
        (Sh-Sc)-(Sa-Ss)-d*(z-1),
    ]
    for expression in identities:
        assert sp.factor(expression) == 0
        checks += 1

    CT=d*(2*z+1)
    CS=d*(z+2)
    assert sp.factor((2*CS-CT)/3-d) == 0
    checks += 1
    assert sp.factor((2*CT-CS)/3-d*z) == 0
    checks += 1

    q=(2*z+1)/(z+2)
    assert sp.factor(q.subs(z,1)-1) == 0
    checks += 1
    assert sp.factor(sp.diff(q,z)-3/(z+2)**2) == 0
    checks += 1
    assert sp.factor(2*(z+2)-(2*z+1)-3) == 0
    checks += 1

    result={
        "classification":"PASS_BINARY_TRANSFER_NORMAL_FORM",
        "checks":checks,
        "scope":(
            "Exact symbolic verification of the active-sector arithmetic "
            "residual/child split, the binary survival/hazard transfer, its "
            "target-null score surplus, and the positive physical coordinates "
            "of the child correction. The component-row/affine normalization "
            "and RH are not certified."
        ),
    }
    output=Path(__file__).resolve().parent/"results"/"verification.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(output)


if __name__=="__main__":
    main()
