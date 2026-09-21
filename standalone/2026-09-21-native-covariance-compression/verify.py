#!/usr/bin/env python3
"""NRC32: exact identities and directed finite native covariance panels.

Standard library only. Future Mobius values are used ONLY by the independent
comparison sieve, never by the Newton producer. No floating arithmetic enters
acceptance. This program does not verify any infinite native energy bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import sys

BITS = 96
Q = 1 << BITS
D = Q * Q
COUNTS: dict[str, int] = {}
MUTATION = "none"


def require(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(label)
    COUNTS[label.split(":", 1)[0]] = COUNTS.get(label.split(":", 1)[0], 0) + 1


def icbrt(n: int) -> int:
    if n < 0:
        raise ValueError("negative cube-root input")
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def mesh(b: int, precision: int = 1) -> list[tuple[int, int]]:
    if b < 2 or precision < 1:
        raise ValueError("mesh requires b>=2 and precision>=1")
    if b < precision**3:
        raise ValueError("precision theorem requires b>=precision^3")
    a, stop, blocks = b, b*b, []
    while a < stop:
        nominal = max(1, icbrt(a*a // (precision**3*b)))
        h = min(nominal, stop-a)
        require(h >= 1 and h**3*precision**3*b <= a*a, "mesh_step")
        blocks.append((a, h))
        a += h
    require(a == stop and len(blocks) < 10*precision*b, "mesh_cover_count")
    return blocks


def mobius_trial(nmax: int) -> list[int]:
    """Primitive producer input, queried only through the previous cutoff."""
    out = [0]*(nmax+1)
    for n in range(1, nmax+1):
        r, p, value = n, 2, 1
        while p*p <= r:
            if r % p == 0:
                r //= p
                value = -value
                if r % p == 0:
                    value = 0
                    break
            p += 1
        if value and r > 1:
            value = -value
        out[n] = value
    return out


def mobius_checker(nmax: int) -> list[int]:
    """Independent full-length sieve, used exclusively for comparison."""
    out, composite = [1]*(nmax+1), bytearray(nmax+1)
    out[0] = 0
    for p in range(2, nmax+1):
        if not composite[p]:
            for n in range(p, nmax+1, p):
                composite[n] = 1
                out[n] = -out[n]
            for n in range(p*p, nmax+1, p*p):
                out[n] = 0
    return out


def newton(y: int) -> tuple[list[int], list[int], list[int]]:
    g = mobius_trial(y)
    z = [0]*(y*y+1)
    nz = [(r, g[r]) for r in range(1, y+1) if g[r]]
    for i, (r, cr) in enumerate(nz):
        for s, cs in nz[i:]:
            z[r*s] += cr*cs*(1 if r == s else 2)
    if MUTATION == "drop_mixed_product" and len(z) > 6:
        z[6] = 0
    end = (y+1)**2-1
    v = [0]*(end+1)
    for r, cr in nz:
        v[r] = 2*cr
    for d, zd in enumerate(z):
        if d and zd:
            for n in range(d, end+1, d):
                v[n] -= zd
    return g, z, v


def harmonic(n: int) -> list[F]:
    h = [F(0)]
    for j in range(1, n+1):
        h.append(h[-1]+F(1,j))
    return h


def primitive(d: int, t: int, harmonics: list[F]) -> F:
    if d < 1 or t < 1:
        raise ValueError("primitive requires d,t>=1")
    r = (t-1)//d
    linear = 0 if MUTATION == "drop_primitive_linear_term" else d*r
    return t*harmonics[r]-linear


def exact_checks() -> None:
    for n in range(2001):
        r = icbrt(n)
        require(r**3 <= n < (r+1)**3, "integer_cube_root")
    for h in range(1,129):
        pairs = sum((j-i)**2 for i in range(h) for j in range(i+1,h))
        require(12*pairs == h*h*(h*h-1), "pair_distance_sum")
    for a in range(1,6):
        for h in range(1,8):
            for signs in itertools.product((-1,1), repeat=h-1):
                vals = [F(2,7)]
                for j, sign in enumerate(signs, start=1):
                    vals.append(vals[-1]+F(sign,a+j))
                mean = sum(vals,F(0))/h
                detail = sum(((x-mean)**2 for x in vals),F(0))
                pairs = sum(((vals[j]-vals[i])**2 for i in range(h)
                             for j in range(i+1,h)),F(0))/h
                require(detail == pairs, "variance_pair_identity")
                require(detail <= F(h*(h*h-1),12*a*a), "variance_bound")
                require(sum((x*x for x in vals),F(0)) == h*mean*mean+detail,
                        "orthogonal_energy_identity")
    hs = harmonic(128)
    for d in range(1,33):
        total = F(0)
        for t in range(1,129):
            total += hs[(t-1)//d]
            require(primitive(d,t,hs) == total, "harmonic_primitive")
    for y in (2,3,7,15):
        g,z,v = newton(y)
        end, b = len(v)-1, y+1
        hs = harmonic(end)
        vals, m = [F(0)], F(0)
        for k in range(1,end+1):
            m += F(v[k],k)
            vals.append(m)
        for sigma in (2,3,4):
            cutoff = end+1
            cells = sum((vals[k]*(F(1,k**(sigma-1))
                         -F(1,(k+1)**(sigma-1)))/(sigma-1)
                         for k in range(1,end+1)),F(0))
            tail = vals[end]*F(1,sigma*cutoff**(sigma-1))
            polynomial = sum((F(v[n],n**sigma) for n in range(1,end+1)),F(0))
            transformed = (sigma*polynomial-vals[end]*F(1,cutoff**(sigma-1)))/(sigma*(sigma-1))
            require(cells+tail == transformed, "endpoint_mellin_identity")
        z_items = [(d,zd) for d,zd in enumerate(z) if d and zd]
        for a,h in mesh(b):
            formula = 2*vals[y]-sum((F(zd,d)*(primitive(d,a+h,hs)
                       -primitive(d,a,hs)) for d,zd in z_items),F(0))/h
            direct = sum(vals[a:a+h],F(0))/h
            require(formula == direct, "native_block_mean")
    # Symbolic integration: pairs are (rational part, coefficient of log(q)).
    for length in (1,2,5,17):
        for ratio in (F(5,4),F(3,2),F(2),F(5,2)):
            head = (length*(ratio-1/ratio), -2*length)
            tail = (length*(ratio-1)**2/ratio, 0)
            require((head[0]+tail[0],head[1]+tail[1])
                    == (2*length*(ratio-1),-2*length), "taper_translation_identity")
    for precision in (1,2,3,4):
        for b in sorted(set((max(2,precision**3), max(3,precision**3+1),
                             max(16,precision**3+7)))):
            blocks = mesh(b,precision)
            zbound = sum((F(h*(h*h-1),12*a*a) for a,h in blocks),F(0))
            require(zbound < F(5,6*precision*precision), "precision_mesh_bound")


def square_bounds(lo: int, hi: int) -> tuple[int,int]:
    if lo > hi:
        raise ValueError("reversed interval")
    return (0 if lo <= 0 <= hi else min(lo*lo,hi*hi), max(lo*lo,hi*hi))


def ceil_div(n: int, d: int) -> int:
    return -((-n)//d)


def decimal_endpoint(n: int, den: int, upward: bool) -> str:
    scale = 10**12
    v = ceil_div(n*scale,den) if upward else (n*scale)//den
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v//scale}.{v%scale:012d}"


def interval(lo: int, hi: int) -> dict:
    require(lo <= hi, "directed_interval")
    return {"lower_numerator":str(lo), "upper_numerator":str(hi),
            "denominator_power_two":2*BITS,
            "outward_decimal":[decimal_endpoint(lo,D,False),
                               decimal_endpoint(hi,D,True)]}


def native_panel(y: int) -> dict:
    g,z,v = newton(y)
    end, b = len(v)-1, y+1
    independent = mobius_checker(end)
    for n in range(1,end+1):
        require(v[n] == independent[n], "native_coefficient")
    # No independent future values enter the following energy calculation.
    ml = mu = 0
    fl = fu = 0
    for n in range(1,y+1):
        ml += (v[n]*Q)//n
        mu += ceil_div(v[n]*Q,n)
        sl,su = square_bounds(ml,mu)
        fl += sl
        fu += su
    prefix = interval(fl,fu)
    al = au = cl = cu = zl = zu = 0
    blocks = mesh(b)
    for a,h in blocks:
        bl = bu = 0
        for n in range(a,a+h):
            ml += (v[n]*Q)//n
            mu += ceil_div(v[n]*Q,n)
            sl,su = square_bounds(ml,mu)
            al += sl
            au += su
            bl += ml
            bu += mu
        sl,su = square_bounds(bl,bu)
        cl += sl//h
        cu += ceil_div(su,h)
        zn,zd = h*(h*h-1),12*a*a
        zl += zn*D//zd
        zu += ceil_div(zn*D,zd)
    dl,du = max(0,al-cu),au-cl
    require(du >= 0, "native_detail_nonnegative")
    require(du <= zl, "native_detail_within_exact_budget")
    require(6*zu < 5*D, "native_mesh_budget_below_five_sixths")
    return {"Y":y,"last_native_index":end,"block_count":len(blocks),
            "prefix_input_limit":y,"arithmetic":"integer outward, 96-bit source grid",
            "F_Y":prefix,"annular_F":interval(al,au),
            "coarse_S":interval(cl,cu),"detail_D":interval(dl,du),
            "mesh_budget_Z":interval(zl,zu)}


def build(quick: bool = False) -> dict:
    COUNTS.clear()
    exact_checks()
    cutoffs = (2,3,7,15) if quick else (2,3,7,15,31,63,127,255,511,1023)
    panels = [native_panel(y) for y in cutoffs]
    return {"packet":"NRC32", "status":"finite checks; universal proofs require review",
            "full_native_coarse_bound_proved":False,
            "future_mobius_used_by_producer":False,
            "future_mobius_used_by_comparison_checker":True,
            "quick_campaign":quick,"counts":dict(sorted(COUNTS.items())),
            "panels":panels}


def strict_load(path: Path) -> dict:
    def unique(pairs):
        out = {}
        for key,value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out
    return json.loads(path.read_text(),object_pairs_hook=unique,
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))


def encoded(value: dict) -> str:
    return json.dumps(value,sort_keys=True,indent=2,ensure_ascii=True)+"\n"


def main() -> None:
    global MUTATION
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write",type=Path)
    ap.add_argument("--check",type=Path)
    ap.add_argument("--receipt",type=Path)
    ap.add_argument("--quick",action="store_true")
    ap.add_argument("--mutation",choices=("none","drop_mixed_product",
                         "drop_primitive_linear_term"),default="none")
    args = ap.parse_args()
    MUTATION = args.mutation
    result = build(args.quick)
    text = encoded(result)
    if args.check is not None and encoded(strict_load(args.check)) != text:
        raise ValueError("reconstructed report differs from supplied report")
    if args.receipt is not None:
        expected = strict_load(args.receipt).get("report_sha256")
        actual = hashlib.sha256(text.encode()).hexdigest()
        if not isinstance(expected,str) or expected != actual:
            raise ValueError("reconstructed report does not match receipt")
    if args.write is not None:
        args.write.write_text(text)
    print(json.dumps({"status":"PASS","sha256":hashlib.sha256(text.encode()).hexdigest(),
                      "counts":result["counts"],"largest_index":result["panels"][-1]["last_native_index"]},
                     sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"REFUSED: {exc}",file=sys.stderr)
        sys.exit(1)
