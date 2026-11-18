"""Classify S3-sextic fields and exclude quaternion fields in Zhao's bound."""
import json
from functools import cache
from pathlib import Path

from flint import arb, arb_series, ctx, dirichlet_char, fmpz

from check_zhao_abelian_fields_nov18 import spectral_weight
from check_zhao_cubic_fields_nov18 import theta_weight
from check_zhao_field_weight_nov18 import primes_through

RESEARCH = Path(__file__).resolve().parents[1] / "research/explorations"


def signed_core(d):
    core = -1 if d < 0 else 1
    for p, e in fmpz(abs(d)).factor():
        if e % 2:
            core *= int(p)
    return core if core % 4 == 1 else 4 * core


@cache
def quadratic_weight(d):
    q = abs(d)
    candidates = [dirichlet_char(q, l) for l in range(1, q) if l*l % q == 1]
    (chi,) = [c for c in candidates if c.is_primitive() and c.parity() == int(d<0)]
    return spectral_weight(chi)


def s3_fields():
    cubic = json.loads((RESEARCH / "zhao-cubic-fields-nov18.json").read_text())
    if cubic["unresolved"]:
        raise ArithmeticError("Cubic inventory incomplete")
    quadratic = set(json.loads((RESEARCH / "zhao-quadratic-fields-nov18.json").read_text())["discriminants"])
    bz = 2+arb.const_euler()-(4*arb.pi()).log()
    records = []
    evaluated = 0
    for d, coeff in cubic["accepted"]:
        k = signed_core(d)
        if k not in quadratic:
            continue
        w = 2*theta_weight(d, coeff) + quadratic_weight(k) - bz
        evaluated += 1
        if w < 2:
            records.append(dict(cubic_discriminant=d, cubic_polynomial=coeff,
                                abs_discriminant=d*d*abs(k), weight=str(w)))
        elif not w > 2:
            raise ArithmeticError(f"Unresolved Galois closure of {coeff}")
    return evaluated, records


def quaternion_exclusions():
    inventory = json.loads((RESEARCH / "zhao-abelian-fields-nov18.json").read_text())["fields"]
    results = []
    s = arb(5)/2
    z = arb_series([s, 1], prec=2).zeta()
    # The totally real bound works also in the imaginary case by digamma monotonicity.
    naive = (4*(s-arb(1)/2)-2/s-2/(s-1)
             + 8*(arb.pi().log()-(s/2).digamma()-2*z[1]/z[0]))
    for field in inventory:
        chars = field["characters"]
        if (field["degree"] != 4 or not field["totally_real"]
                or any(l*l % q != 1 for q,l in chars)):
            continue
        base = field["abs_discriminant"]
        lower = base**2
        for p, _ in fmpz(base).factor():
            if p != 2:
                lower *= int(p)**2
        upper = naive
        characters = [dirichlet_char(q,l) for q,l in chars]
        for p in primes_through(97):
            unram = [c for c in characters if int(c.modulus()) % p]
            f = 2 if any(int(c.chi_exponent(p)) for c in unram) else 1
            # The base has e0=4/(1+len(unram)). For e0>1 every inertia
            # subgroup surjecting onto it contains the quaternion center.
            if len(unram) == 3:
                if f == 1:
                    continue
                # Unramified lift of order four, or central ramification, f=2.
                local = 4/(arb(p)**(2*s)-1)
            elif len(unram) == 1:
                local = 2/(arb(p)**(f*s)-1)
            else:
                local = 1/(arb(p)**(f*s)-1)
            upper -= 2*arb(p).log()*(8/(arb(p)**s-1)-local)
        upper = upper.exp()
        if not upper < lower:
            raise ArithmeticError(f"Quaternion exclusion unresolved at {base}")
        results.append([base, int(upper.ceil().unique_fmpz()), lower])
    return sorted(results)


if __name__=="__main__":
    ctx.prec=96
    q8 = quaternion_exclusions()
    count, fields=s3_fields()
    print(json.dumps(dict(s3_evaluations=count, s3_fields=fields, q8_bounds=q8), indent=2))
