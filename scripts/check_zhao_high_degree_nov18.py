"""Screen a catalog of number fields with directed Arb prime-ideal inequalities."""

import argparse
from functools import cache
import json
from math import isqrt
import os
from pathlib import Path
import subprocess

from flint import arb, ctx, fmpz_poly, nmod_poly
from check_zhao_field_weight_nov18 import field_terms, prime_term, primes_through


def gp_rows(rows, primes):
    # Each LMFDB polynomial is constant coefficient first. PARI's Polrev has that order.
    for start in range(0, len(rows), 64):
        batch = rows[start:start+64]
        coefficients = [item["coeffs"] for item in batch]
        program = (f"V={coefficients};P={primes};\n"
                   "for(i=1,#V,F=Polrev(V[i]); K=nfinit(F); "
                   "print([K.disc,K.sign,vector(#P,j,my(Z=idealprimedec(K,P[j]));"
                   "sum(k=1,#Z,10^(Z[k].f-1))) ]));\n")
        proc = subprocess.run([os.environ.get("PARI_GP","gp"), "-fq"], input=program,
                              text=True, capture_output=True, check=True)
        if proc.stderr or len(proc.stdout.splitlines()) != len(batch):
            raise RuntimeError(f"Incomplete PARI reply: {proc.stderr}")
        for item, line in zip(batch, proc.stdout.splitlines()):
            disc, (r1, r2), codes = json.loads(line)
            degree, advertised_r1, abs_disc, _ = map(int, item["label"].split("/")[-1].split("."))
            assert (degree,r1,abs(disc)) == (r1+2*r2,advertised_r1,abs_disc)
            assert len(codes) == len(primes) and degree <= 8
            yield item, abs_disc, r1, r2, codes


@cache
def modular_weight(cutoff, p, f):
    return prime_term(cutoff, p, f)


def modular_screen(rows, cutoff=16):
    # Dedekind's factorization criterion applies at p not dividing the order index.
    g, delta, pole, a0, a1 = field_terms(cutoff)
    primes = primes_through(cutoff)
    uncertain = []
    for item in rows:
        degree,r1,disc,_ = map(int,item["label"].split("/")[-1].split("."))
        r2 = (degree-r1)//2
        coeff = item["coeffs"]
        polynomial_disc = int(fmpz_poly(coeff).discriminant())
        index = isqrt(abs(polynomial_disc)//disc)
        assert polynomial_disc == (-1)**r2 * disc * index**2
        if "index" in item:
            assert index == item["index"]
        estimate = g*arb(disc).log()+pole+(r1+r2)*a0+r2*a1
        for p in primes:
            if index % p == 0:
                estimate -= degree * modular_weight(cutoff,p,1)
            else:
                _,factors = nmod_poly(coeff,p).factor()
                estimate -= sum(modular_weight(cutoff,p,poly.degree()) for poly,_ in factors)
        if not estimate > 2*(1+delta):
            uncertain.append(item)
    return uncertain


def classify(rows, limits):
    active = modular_screen(rows)
    stages, accepted = [["modular16",0,len(rows)-len(active),len(active)]], []
    print(stages[-1],flush=True)
    for limit in limits:
        g, delta, pole, a0, a1 = field_terms(limit)
        primes = primes_through(limit)

        @cache
        def euler(p, code):
            return sum( (code//10**(f-1)%10)*prime_term(limit,p,f)
                        for f in range(1,9) if p**f <= limit and code//10**(f-1)%10 )

        good = bad = 0
        undecided = []
        for item, disc, r1, r2, codes in gp_rows(active,primes):
            estimate = g*arb(disc).log()+pole+(r1+r2)*a0+r2*a1
            for p,code in zip(primes,codes):
                estimate -= euler(p,code)
            if estimate > 2*(1+delta):
                bad += 1
            elif estimate < 2*(1-delta):
                good += 1
                accepted.append(item)
            else:
                undecided.append(item)
        stages.append([limit,good,bad,len(undecided)])
        print(stages[-1], flush=True)
        active = undecided
        if not active:
            break
    return {"enumerated":len(rows), "stages":stages, "accepted":accepted, "unresolved":active}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--limits", default="16,64,256,1024,4096,16384")
    args = parser.parse_args()
    ctx.prec = 96
    entries = json.loads(args.catalog.read_text())
    assert len({row["label"] for row in entries}) == len(entries)
    result = classify(entries, [int(x) for x in args.limits.split(",")])
    args.output.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
