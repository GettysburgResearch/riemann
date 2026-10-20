"""Exploratory finite Eisenstein canonical norms; no asymptotic claim.

All ideals are represented by their unique generator congruent to 1
modulo 3, avoid 2 and 3, and are squarefree. Rows are every nonzero
Eisenstein element in a norm ball, retaining all six unit classes.
Character exponents and factorization are exact; Gauss sums and norms
use floating arithmetic. The window is an explicit smooth annulus.
"""

from pathlib import Path
import cmath
import json
import math
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "python-deps"))
import numpy as np


def norm(z):
    a, b = z
    return a*a-a*b+b*b


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def divide(x, y):
    a, b = y
    q = norm(y)
    c, d = mul(x, (a-b, -b))
    return None if c % q or d % q else (c//q, d//q)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def elements(bound, primary=False):
    radius = math.ceil(math.sqrt(4*bound/3))+1
    result = []
    for a in range(-radius, radius+1):
        for b in range(-radius, radius+1):
            q = norm((a,b))
            if 0 < q <= bound and (not primary or (a % 3 == 1 and b % 3 == 0)):
                result.append((a,b))
    return sorted(result, key=lambda z: (norm(z), z))


def fmul(x, y, p):
    a,b = mul(x,y)
    return (a % p, b % p)


def fpow(x, e, p):
    y = (1,0)
    while e:
        if e & 1:
            y = fmul(y,x,p)
        x = fmul(x,x,p)
        e >>= 1
    return y


UNITS = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
ZETA = np.exp(2j*np.pi*np.arange(6)/6)


class PrimeIdeal:
    def __init__(self, z):
        self.z = z
        self.q = norm(z)
        a,b = z
        self.split = prime(self.q)
        if self.split:
            p = self.q
            self.p = p
            self.omega = (-a*pow(b % p,-1,p)) % p
            roots = {(u+self.omega*v) % p: i for i,(u,v) in enumerate(UNITS)}
            self.table = np.full(p,-1,dtype=np.int16)
            for x in range(1,p):
                self.table[x] = roots[pow(x,(p-1)//6,p)]
            self.gauss = sum(ZETA[(2*int(self.table[x])) % 6]
                             * cmath.exp(-2j*math.pi*b*x/p)
                             for x in range(1,p))/math.sqrt(p)
        else:
            p = math.isqrt(self.q)
            self.p = p
            roots = {(u % p,v % p): i for i,(u,v) in enumerate(UNITS)}
            self.table = np.full((p,p),-1,dtype=np.int16)
            g = 0j
            for x in range(p):
                for y in range(p):
                    if x or y:
                        digit = roots[fpow((x,y),(p*p-1)//6,p)]
                        self.table[x,y] = digit
                        g += ZETA[2*digit % 6]*cmath.exp(-2j*math.pi*y/p)
            self.gauss = g/p
        if abs(abs(self.gauss)-1) > 1e-10:
            raise ArithmeticError("Bad primitive Gauss norm")

    def digits(self, rows):
        if self.split:
            return self.table[(rows[:,0]+self.omega*rows[:,1]) % self.p]
        return self.table[rows[:,0] % self.p, rows[:,1] % self.p]

    def digit(self,z):
        return int(self.digits(np.array([z],dtype=np.int64))[0])


def window(y):
    # C-infinity bump on (1,2), normalized to maximum one.
    return math.exp(4-1/((y-1)*(2-y))) if 1 < y < 2 else 0.0


def main():
    max_d = 500
    ideals = [z for z in elements(2*max_d,True) if math.gcd(norm(z),6)==1]
    prime_ideals = []
    for z in ideals:
        q = norm(z)
        p = math.isqrt(q)
        if prime(q) or (p*p == q and prime(p) and p % 3 == 2):
            prime_ideals.append(PrimeIdeal(z))
    columns = []
    for z in ideals:
        rem = z
        factors = []
        squarefree = True
        gauss = 1+0j
        for i,p in enumerate(prime_ideals):
            if p.q > norm(rem):
                break
            quot = divide(rem,p.z)
            if quot is None:
                continue
            if divide(quot,p.z) is not None:
                squarefree = False
                break
            # g_3(p*quot)=g_3(p)g_3(quot) chi_p(quot)^4.
            d = p.digit(quot)
            if d < 0:
                raise ArithmeticError("Lost squarefree mask")
            gauss *= p.gauss*ZETA[4*d % 6]
            factors.append(i)
            rem = quot
        if squarefree:
            if rem != (1,0):
                raise ArithmeticError(("Unfactored primary ideal",z,rem))
            columns.append((z,factors,gauss))
    max_k = 8*max_d
    rows = np.array(elements(max_k),dtype=np.int64)
    row_norm = rows[:,0]**2-rows[:,0]*rows[:,1]+rows[:,1]**2
    characters = [p.digits(rows) for p in prime_ideals]
    results = []
    for dscale in (30,60,120,250,500):
        for ell in (-1,1,2):
            values = np.zeros(len(rows),dtype=np.complex128)
            diagonal = np.zeros(len(rows),dtype=np.float64)
            column_count = 0
            for z,factors,g in columns:
                q = norm(z)
                weight = window(q/dscale)
                if weight == 0:
                    continue
                column_count += 1
                digit = np.zeros(len(rows),dtype=np.int16)
                active = np.ones(len(rows),dtype=bool)
                for i in factors:
                    active &= characters[i] >= 0
                    digit += characters[i]
                angle = complex(z[0]-.5*z[1],math.sqrt(3)*z[1]/2)/math.sqrt(q)
                coefficient = angle**ell*g*weight/math.sqrt(q)
                values[active] += coefficient*ZETA[digit[active] % 6]
                diagonal[active] += abs(coefficient)**2
            for ratio in (1,2,4,8):
                k = ratio*dscale
                retained = row_norm <= k
                total = float(np.sum(abs(values[retained])**2))
                diag = float(np.sum(diagonal[retained]))
                results.append({"D":dscale,"K":k,"ell":ell,
                                "columns":column_count,"rows":int(np.sum(retained)),
                                "norm":total,"diagonal":diag,
                                "norm_over_diagonal":total/diag,
                                "centered":total-diag})
    receipt={"status":"EXPLORATORY_NUMERICAL_ONLY",
             "scope":"Exact finite character masks; floating Gauss sums/norms; no asymptotic theorem.",
             "fixed_bad_primes":"2 and 3", "row_unit_classes":"all six",
             "window":"exp(4-1/((y-1)(2-y))) on 1<y<2, zero elsewhere",
             "results":results}
    path=Path(__file__).with_name("CENTERED_CANONICAL_PROBE.json")
    path.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(path),"samples":len(results),
                      "physical_ell_minus_one":[r for r in results if r["ell"]==-1]},indent=2))


if __name__ == "__main__":
    main()
