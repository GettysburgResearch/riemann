"""Classify the strict GRH zero-weight condition for octic dihedral Galois fields."""

import argparse
from ast import literal_eval
import json
import subprocess

from flint import arb, arb_series, ctx
from check_zhao_field_weight_nov18 import primes_through, weight_bounds


def run_gp(executable, program):
    result = subprocess.run(
        [executable, "-fq"], input=program + "\n", text=True, capture_output=True, check=True
    )
    if result.stderr:
        raise RuntimeError(result.stderr)
    return [literal_eval(line) for line in result.stdout.splitlines() if line.strip()]


def discriminant_bounds():
    s = arb(7)/2
    series = arb_series([s, 1], 2).zeta()
    slope = series[1]/series[0]
    pole = 4*(s-arb(1)/2)-2/s-2/(s-1)
    real = arb.pi().log()-(s/2).digamma()-2*slope
    complex_place = 2*(2*arb.pi()).log()-2*s.digamma()-4*slope
    assert (pole+8*real).exp() < 270_000_000
    assert (pole+4*complex_place).exp() < 74_000_000
    assert 16432**2 > 270_000_000


def candidates(executable):
    program = r"""
v=nflist("D4",[1,16432]); print(#v);
for(i=1,#v,f=v[i]; dc=nfdisc(f); sub=nfsubfields(f,2); if(#sub!=1,error("quartic quadratic subfield")); e=nfdisc(sub[1][1]); b=coredisc(dc); h=coredisc(e*b); dl=abs(e*b*h)*(dc/e)^2; isreal=(polsturm(f)==4); if(dl<if(isreal,270000000,74000000),g=polredabs(nfsplitting(f)); if(poldegree(g)!=8 || abs(nfdisc(g))!=dl,error("closure discriminant")); print([Vec(g),dl,Vec(f),isreal])))
"""
    count, *rows = run_gp(executable, program)
    fields = {}
    for polynomial, disc, quartic, real in rows:
        polynomial = tuple(polynomial)
        if polynomial not in fields:
            fields[polynomial] = (disc, real, [])
        old_disc, old_real, representatives = fields[polynomial]
        assert (disc, real) == (old_disc, old_real)
        representatives.append(quartic)
    assert count == 719 and len(rows) == 26 and len(fields) == 13
    assert len({item[0] for item in fields.values()}) == len(fields)
    assert all(len(item[2]) == 2 for item in fields.values())
    return count, fields


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gp", default="gp")
    args = parser.parse_args()
    ctx.prec = 96
    discriminant_bounds()
    count, fields = candidates(args.gp)
    records = []
    for polynomial, (disc, real, representatives) in sorted(fields.items(), key=lambda row: row[1][0]):
        for cutoff in (50, 200, 800):
            program = (f"q=Pol({list(polynomial)}); K=nfinit(q); "
                       f"p=primes([1,{cutoff}]); "
                       "print(vector(#p,j,z=idealprimedec(K,p[j]);vector(#z,k,z[k].f)));")
            (decompositions,) = run_gp(args.gp, program)
            primes = primes_through(cutoff)
            assert len(primes) == len(decompositions)
            lower, _ = weight_bounds(disc, 8 if real else 0, 0 if real else 4,
                                     cutoff, dict(zip(primes, decompositions)))
            if lower > 2:
                break
        else:
            raise ArithmeticError(f"Unresolved field {polynomial}")
        floor = int((lower * 1000).lower().floor().unique_fmpz())
        assert lower > arb(floor)/1000 and floor > 2000
        records.append(dict(discriminant=disc, coefficients=list(polynomial),
                            quartic_representatives=sorted(representatives), prime_cutoff=cutoff,
                            lower_bound_thousandths=floor))
    print(json.dumps(dict(quartics_enumerated=count, excluded_closures=records, passing_closures=[]),
                     indent=2))


if __name__ == "__main__":
    main()
