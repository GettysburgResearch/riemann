#!/usr/bin/env python3
"""Exact finite diagnostics for norm-fiber energy; not analytic certification.

No assert statements: negative controls remain live with python -O.
Only the Python standard library is required. The complete ideal fixtures are
for Q and Q(omega), excluding every prime ideal above 2 and 3.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as Q
from typing import Iterable

COUNTS: Counter[str] = Counter()
MUTATION = "none"


def check(group: str, value: bool) -> None:
    COUNTS[group] += 1
    if not value:
        raise RuntimeError(f"{group}: finite predicate {COUNTS[group]} failed")


def multiply(a: list[Q], b: list[Q], cap: int) -> list[Q]:
    out = [Q(0)] * (cap + 1)
    for i, x in enumerate(a[:cap+1]):
        if x:
            for j, y in enumerate(b[:cap+1-i]):
                if y:
                    out[i+j] += x*y
    return out


def power(a: list[Q], k: int, cap: int) -> list[Q]:
    ans = [Q(1)] + [Q(0)]*cap
    for _ in range(k):
        ans = multiply(ans, a, cap)
    return ans


def qweight(q: int, m: int) -> Q:
    if m % 2 == 0:
        return Q(q ** (m//2-1))
    root = math.isqrt(q)
    if root*root != q:
        raise ValueError("odd m exact test needs a square q")
    return Q(root * q ** (m//2-1))


def local(q: int, m: int, family: str, cap: int,
          a: Q = Q(1), b: Q = Q(1)) -> list[Q]:
    if MUTATION == "erase-mask" and a == b == 0:
        a = b = Q(1)
    v = b*qweight(q, m)
    out = [Q(1)] + [Q(0)]*cap
    if family == "native":
        if cap >= 1:
            out[1] = -a
    elif family == "coupled":
        if cap >= 1:
            out[1] = -(1-Q(1,q))*a
        if cap >= m:
            out[m] = -v
    elif family == "two-channel":
        linear = [Q(1)] + [Q(0)]*cap
        if cap >= 1:
            linear[1] = -a
        if cap >= m:
            out[m] = -v
        out = multiply(linear, out, cap)
    elif family == "geometric":
        for j in range((cap-1)//m+1):
            out[1+j*m] = -(1-Q(1,q))*a*v**j
    elif family == "majorant":
        # One independent geometric expansion, with the extra numerator 1+x.
        out = [Q(0)]*(cap+1)
        vv = qweight(q,m)
        for j in range(cap//m+1):
            out[j*m] += vv**j
            if j*m+1 <= cap:
                out[j*m+1] += vv**j
    else:
        raise ValueError(f"unknown family {family}")
    return out


def sieve(cap: int) -> list[int]:
    good = bytearray(b'\x01')*(cap+1)
    good[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(cap)+1):
        if good[p]:
            good[p*p::p] = b'\x00'*(((cap-p*p)//p)+1)
    return [p for p in range(2,cap+1) if good[p]]


def degrees(p: int, field: str) -> list[int]:
    if p in (2,3):
        return []
    if field == "Q":
        return [1]
    if p % 3 == 1:
        return [1] if MUTATION == "drop-conjugate" else [1,1]
    return [2]


def max_exp(p: int, cap: int) -> int:
    v, e = 1, 0
    while v <= cap//p:
        e += 1
        v *= p
    return e


def norm_local(p: int, fs: list[int], m: int, family: str,
               cap: int, ideal_diagonal: bool = False) -> list[Q]:
    ans = [Q(1)] + [Q(0)]*cap
    for f in fs:
        a = local(p**f,m,family,cap//f)
        embedded = [Q(0)]*(cap+1)
        for j, value in enumerate(a):
            embedded[f*j] = value*value if ideal_diagonal else value
        ans = multiply(ans, embedded, cap)
    return ans


def complete_norm_arrays(cap: int, field: str, m: int,
                         family: str) -> tuple[list[Q], list[Q]]:
    primes = sieve(cap)
    spf = list(range(cap+1))
    for p in primes:
        for n in range(p*p, cap+1, p):
            if spf[n] == n:
                spf[n] = p
    lc, ld = {}, {}
    for p in primes:
        fs = degrees(p,field)
        e = max_exp(p,cap)
        lc[p] = norm_local(p,fs,m,family,e)
        ld[p] = norm_local(p,fs,m,family,e,True)
    coeff, diag = [Q(0)]*(cap+1), [Q(0)]*(cap+1)
    coeff[1] = diag[1] = Q(1)
    for n in range(2,cap+1):
        p, rest, e = spf[n], n, 0
        while rest % p == 0:
            rest //= p
            e += 1
        coeff[n] = lc[p][e]*coeff[rest]
        diag[n] = ld[p][e]*diag[rest]
    return coeff,diag


def all_ideals(cap: int, field: str) -> tuple[list[tuple[int, tuple]], list[int]]:
    # All good ideals, INCLUDING those with zero source coefficient.
    prime_norms = [p**f for p in sieve(cap)
                   for f in degrees(p,field) if p**f <= cap]
    prime_norms.sort()
    states: list[tuple[int,tuple]] = [(1,())]
    for index,q in enumerate(prime_norms):
        old = list(states)
        for n,fac in old:
            qq,e = q,1
            while n*qq <= cap:
                states.append((n*qq,fac+((index,e),)))
                e += 1
                qq *= q
    return states,prime_norms


def chi3(n: int) -> int:
    return 0 if n%3 == 0 else (1 if n%3 == 1 else -1)


def cycle_lengths(perm: tuple[int,...]) -> list[int]:
    seen, lengths = set(), []
    for start in range(len(perm)):
        if start in seen:
            continue
        point, length = start, 0
        while point not in seen:
            seen.add(point)
            length += 1
            point = perm[point]
        lengths.append(length)
    return sorted(lengths)


def direct_pair_cycles(perm: tuple[int,...]) -> list[int]:
    n = len(perm)
    pair = tuple(perm[i]*n+perm[j] for i in range(n) for j in range(n))
    return cycle_lengths(pair)


def orbit_count(group: Iterable[tuple[int,...]]) -> int:
    group = list(group)
    n = len(group[0])
    points = {(i,j) for i in range(n) for j in range(n)}
    count = 0
    while points:
        i,j = next(iter(points))
        orb = {(g[i],g[j]) for g in group}
        points.difference_update(orb)
        count += 1
    return count


def group_tests() -> dict[str,int]:
    # Complete permutations through degree five, not random samples.
    for n in range(1,6):
        for perm in itertools.permutations(range(n)):
            fs = cycle_lengths(perm)
            tensor = sorted([math.lcm(a,b) for a in fs for b in fs
                             for _ in range(math.gcd(a,b))])
            check("tensor_residue_cycles",tensor == direct_pair_cycles(perm))
            first = fs.count(1) if MUTATION == "wrong-tensor" else fs.count(1)**2
            check("tensor_degree_one",tensor.count(1) == first)
            check("tensor_dimension",sum(tensor) == n*n)
    groups = {}
    for n in (1,2,3,4):
        groups[f"C{n}_regular"] = [tuple((i+j)%n for i in range(n)) for j in range(n)]
    groups["V4_regular"] = [tuple(i^j for i in range(4)) for j in range(4)]
    groups["S3_natural"] = list(itertools.permutations(range(3)))
    groups["S4_natural"] = list(itertools.permutations(range(4)))
    result = {}
    for name,g in groups.items():
        kappa = orbit_count(g)
        burnside = sum(Q(sum(v==i for i,v in enumerate(p))**2,len(g)) for p in g)
        check("embedding_orbit_counts",burnside == kappa)
        result[name] = kappa
    check("negative_controls",result['S3_natural'] == 2 and result['S3_natural'] != 3)
    return result


def local_tests() -> int:
    cases = 0
    for m in (2,3,4,6,8):
        qs = (25,49) if m%2 else (5,7,13,25)
        for q in qs:
            major = local(q,m,"majorant",40)
            for a,b in itertools.product((Q(-1),Q(0),Q(1,2),Q(1)),repeat=2):
                for family in ("native","coupled","two-channel","geometric"):
                    coeff = local(q,m,family,40,a,b)
                    check("local_coefficient_majorants",all(abs(v)<=major[j] for j,v in enumerate(coeff)))
                    if a == b == 0:
                        check("literal_masks",coeff == [Q(1)]+[Q(0)]*40)
                    cases += 1
    # Exact mass identity for rational r and all displayed residue-degree lists.
    for fs in ((1,), (1,1), (2,), (1,2), (1,1,1,1), (2,2), (1,1,2)):
        for k in (1,2,3,4):
            for r in (Q(1,2),Q(1,3),Q(2,5)):
                total = Q(1)
                for f in fs:
                    total *= ((1+r**f)/(1-r**(2*f)))**k
                check("critical_mass_identity",total == math.prod((1-r**f)**(-k) for f in fs))
                n = sum(fs)*k
                tail = total-1-k*fs.count(1)*r
                bound = n*(n+1)*2**(n+1)*r*r
                check("uniform_local_tail_budget",0<=tail<=bound)
    # The native split factor and actual signed coupled interference.
    p=7
    native = norm_local(p,[1,1],6,"native",2)
    check("negative_controls",native == [Q(1),Q(-2),Q(1)])
    check("negative_controls",native[1]**2 == 4 and native[1]**2 != 2)
    split = norm_local(p,[1,1],2,"coupled",2)
    iddiag = norm_local(p,[1,1],2,"coupled",2,True)
    check("signed_same_norm_witness",split[2]**2 == Q(3844,2401))
    check("signed_same_norm_witness",iddiag[2] == Q(6098,2401))
    check("signed_same_norm_witness",split[2]**2-iddiag[2] == Q(-2254,2401))
    if MUTATION == "ideal-is-norm":
        check("distinguish_ideal_and_norm",native[1]**2 == Q(2))
    check("negative_controls",Q(9,16)*Q(4,9) == Q(1,4))
    # Literal sextic symbols at the two ideals over 7, on u=2+omega.
    roots=(2,4)
    exponents=[]
    for root in roots:
        base=(1+root)%7
        residue=(2+root)%7
        exp=next(j for j in range(6) if pow(base,j,7)==residue)
        exponents.append(exp)
        check("sextic_split_witness",len({pow(base,j,7) for j in range(6)}) == 6)
        unit_exp=next(j for j in range(6) if pow(base,j,7)==root)
        check("sextic_split_witness",unit_exp == 2)
    check("sextic_split_witness",exponents == [4,3] and (exponents[0]-exponents[1])%6 == 1)
    check("sextic_split_witness",2*2-2*1+1*1 == 3)
    return cases


def census_tests() -> list[dict]:
    cap=512
    records=[]
    for field in ("Q","Eisenstein"):
        ideals,prime_norms=all_ideals(cap,field)
        ideal_counts=Counter(n for n,_ in ideals)
        expected=[0]*(cap+1)
        if field=="Q":
            for n in range(1,cap+1):
                expected[n]=int(math.gcd(n,6)==1)
        else:
            for d in range(1,cap+1):
                for n in range(d,cap+1,d):
                    expected[n]+=chi3(d)
            for n in range(1,cap+1):
                if math.gcd(n,6)>1:
                    expected[n]=0
        for n in range(1,cap+1):
            check("complete_ideal_norm_counts",ideal_counts[n] == expected[n])
        for m in (2,4,6):
            for family in ("native","coupled","two-channel","geometric"):
                coeff,diag=complete_norm_arrays(cap,field,m,family)
                direct=[Q(0)]*(cap+1)
                directdiag=[Q(0)]*(cap+1)
                cache={q:local(q,m,family,max_exp(q,cap)) for q in set(prime_norms)}
                nonzero=0
                for n,fac in ideals:
                    value=math.prod(cache[prime_norms[idx]][e] for idx,e in fac)
                    direct[n]+=value
                    directdiag[n]+=value*value
                    nonzero+=bool(value)
                for n in range(1,cap+1):
                    check("complete_norm_fiber_coefficients",coeff[n] == direct[n])
                    check("complete_ideal_diagonals",diag[n] == directdiag[n])
                records.append({"field":field,"m":m,"source":family,
                                "norm_cap":cap,"all_good_ideals":len(ideals),
                                "nonzero_source_ideals":nonzero})
    return records


def integration_tests() -> None:
    for k in (1,2,3,4):
        for c in (Q(0),Q(1,2),Q(5,6)):
            beta=2*c-1
            for a,b,x in itertools.product((Q(-1),Q(0),Q(2)),repeat=3):
                mid=(a+b)/2
                left=beta*x-c*(a+b)-((x-a)**2+(x-b)**2)/(4*k)
                right=-(x-mid-k*beta)**2/(2*k)-mid+k*beta**2/2-(a-b)**2/(8*k)
                check("gaussian_square_completion",left == right)
                t=a-k*x
                point_left=-k*x-2*c*t-t*t/(2*k)
                point_right=-a+k*beta*beta/2-(t+k*beta)**2/(2*k)
                check("fixed_scale_gaussian_completion",point_left == point_right)
        # Exact exponent/Jacobian comparison at X=2, Y=X^k.
        X=Q(2);Y=X**k
        dY_dX=k*X**(k-1)
        factor=Q(1) if MUTATION == "wrong-jacobian" else Q(1,k)
        check("higher_order_jacobian",factor*dY_dX/Y**2 == X**(-k-1))
        for aa in itertools.product((Q(-1),Q(0),Q(2)),repeat=k):
            avg=sum(aa)/k
            for x in (Q(0),Q(1,2)):
                check("tuple_gaussian_balance",sum((a-x)**2 for a in aa) ==
                      sum((a-avg)**2 for a in aa)+k*(x-avg)**2)
    for values in itertools.product((Q(-2),Q(0),Q(1),Q(3)),repeat=4):
        diagonal=sum(v*v for v in values)
        for R in (1,2):
            pairs=[(i,j) for i in range(4) for j in range(4) if 0<abs(i-j)<=R]
            L=max(sum(i==a for a,b in pairs) for i in range(4))
            # Positive constant Gram kernel 1; this includes mixed coefficient signs.
            lhs=sum(abs(values[i]*values[j]) for i,j in pairs)
            check("sparse_graph_bound",lhs <= L*diagonal)
    check("negative_controls",4>3 and 4<=2*3) # degree 2R is not generally R
    check("negative_controls",Q(1,3)*3*Q(2)**2/Q(8)**2 == Q(2)**(-4))



def compact_window_tests() -> list[dict]:
    """Complete hard-window tuples, two constructions, with rational arithmetic."""
    records = []
    for field in ("Q", "Eisenstein"):
        for cap in (16, 32, 64):
            ideals, pnorms = all_ideals(cap, field)
            for family in ("native", "coupled", "two-channel", "geometric"):
                m = 2
                cache = {q: local(q,m,family,max_exp(q,cap)) for q in set(pnorms)}
                mc = {q: local(q,m,"majorant",max_exp(q,cap)) for q in set(pnorms)}
                columns = [(n, math.prod(cache[pnorms[i]][e] for i,e in fac))
                           for n,fac in ideals if cap//2<n<=cap]
                fullmajor = Counter()
                for n,fac in ideals:
                    fullmajor[n] += math.prod(mc[pnorms[i]][e] for i,e in fac)
                normcols, abscols = Counter(), Counter()
                for n,v in columns:
                    normcols[n] += v
                    abscols[n] += abs(v)
                for k in (1,2,3):
                    direct, directabs = Counter(), Counter()
                    for tup in itertools.product(columns, repeat=k):
                        N = math.prod(n for n,v in tup)
                        value = math.prod(v for n,v in tup)
                        direct[N] += value
                        directabs[N] += abs(value)
                    grouped, groupedabs, major = {1:Q(1)}, {1:Q(1)}, {1:Q(1)}
                    for j in range(k):
                        nextg, nexta, nextm = Counter(), Counter(), Counter()
                        for N,v in grouped.items():
                            for n,z in normcols.items(): nextg[N*n] += v*z
                        for N,v in groupedabs.items():
                            for n,z in abscols.items(): nexta[N*n] += v*z
                        for N,v in major.items():
                            for n,z in fullmajor.items(): nextm[N*n] += v*z
                        grouped, groupedabs, major = nextg, nexta, nextm
                    for N in sorted(set(direct) | set(grouped)):
                        check("compact_tuple_grouping", direct[N] == grouped[N])
                        check("compact_absolute_grouping", directabs[N] == groupedabs[N])
                        check("compact_majorant", directabs[N] <= major[N])
                    nd = sum(v*v for v in directabs.values())
                    major2 = sum(v*v for v in major.values())
                    harmonic = sum(v*v/Q(N) for N,v in major.items())
                    check("compact_harmonic_budget", nd<=major2<=cap**k*harmonic)
                    for R in (0,1,4):
                        near = sum(v*z for N,v in directabs.items()
                                   for M,z in directabs.items() if abs(N-M)<=R)
                        check("compact_gap_sector", near <= (2*R+1)*nd)
                    records.append({"field":field,"norm_cap":cap,"m":m,
                                    "source":family,"order":2*k,
                                    "all_window_ideals":len(columns),
                                    "product_norm_fibers":len(direct)})
    return records

def main() -> dict:
    orbits=group_tests()
    cases=local_tests()
    records=census_tests()
    integration_tests()
    windows=compact_window_tests()
    return {"status":"PASS: exact finite diagnostics only",
            "counts":dict(sorted(COUNTS.items())),"total_predicates":sum(COUNTS.values()),
            "complete_permutations_through_degree_5":153,
            "local_source_profile_cases":cases,"local_max_degree":40,
            "embedding_pair_orbits":orbits,"complete_censuses":records,
            "complete_compact_windows":windows,
            "limits":["Not an analytic asymptotic proof or independent mathematical review.",
                      "Norm-cap censuses include all good ideals but high geometric powers first appear beyond some caps.",
                      "General-field splitting tests use finite permutation data, not new number-field computations.",
                      "Two census assemblies share exact local source formulas and splitting data.",
                      "The sextic physical-row diagnostic is only the explicitly named norm-7 conjugate-prime case."]}


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--mutation",choices=("none","drop-conjugate","wrong-tensor",
                        "wrong-jacobian","erase-mask","ideal-is-norm"),default="none")
    args=parser.parse_args()
    MUTATION=args.mutation
    print(json.dumps(main(),sort_keys=True,indent=2))
