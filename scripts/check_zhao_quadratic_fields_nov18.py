"""Enumerate quadratic fields satisfying the GRH spectral test in Zhao §8(3).

Uses python-flint 0.9.0 (FLINT 3.6.0). The period sums and their endpoints
are exact integers in units 2^-40. Arb supplies outward enclosures.
"""
import json
from math import isqrt
from flint import acb_series, arb, arb_series, ctx, dirichlet_char, fmpz


def fundamental(d):
    if d in (-1, 0, 1):
        return False
    if d % 4 == 1:
        m = d
    elif d % 4 == 0 and (d // 4) % 4 in (2, 3):
        m = d // 4
    else:
        return False
    return all(m % (j * j) for j in range(2, isqrt(abs(m)) + 1))


def kronecker_values(d):
    q = abs(d)
    c = [0] * (q + 1)
    at_two = 0 if d % 2 == 0 else (1 if d % 8 in (1, 7) else -1)
    for n in range(1, q + 1):
        c[n] = int(fmpz(d).jacobi(n)) if n % 2 else at_two * c[n // 2]
    if sum(c):
        raise ValueError("Nonzero character period")
    return c


def zeta_test_bound(a, target):
    s = arb(7) / 4
    jet = arb_series([s, 1], prec=2).zeta()
    return arb.pi() * ((2*s - 1)*target
                       - ((s+a)/2).digamma() - 2*jet[1]/jet[0]).exp()


def exact_log_derivative(d):
    q = abs(d)
    matches = []
    for label in range(1, q):
        if label*label % q != 1:
            continue
        chi = dirichlet_char(q, label)
        if chi.is_primitive() and chi.is_real() and chi.parity() == int(d < 0):
            matches.append(chi)
    if len(matches) != 1:
        raise ValueError("Expected a unique primitive quadratic character of this parity")
    jet = acb_series([1, 1], prec=2).dirichlet_l(matches[0])
    ratio = jet[1] / jet[0]
    if not ratio.imag.contains(0):
        raise ArithmeticError("Nonreal logarithmic derivative")
    return ratio.real


def classify():
    ctx.prec = 96
    bound = 2 - (2 + arb.const_euler() - (4*arb.pi()).log())
    limits = [5969, 2915]
    if any(not zeta_test_bound(a, arb(2)) < limits[a] for a in (0, 1)):
        raise ArithmeticError("Conductor cut failed")
    scale = 2**40
    periods = 4
    last = periods * max(limits)
    term = [0] + [scale // n for n in range(1, last + 1)]
    deriv = [0] + [int(((arb(n).log()*scale)/n).floor().unique_fmpz())
                   for n in range(1, last + 1)]
    selected = []
    character_only = []
    checked = 0
    refined = 0
    for d in range(-limits[1] + 1, limits[0]):
        if not fundamental(d):
            continue
        checked += 1
        q = abs(d)
        arch = (arb(q)/arb.pi()).log() + ((arb(1) + int(d < 0))/2).digamma()
        c = kronecker_values(d)
        S = B = 0
        for v in c[1:]:
            S += v
            B = max(abs(S), B)
        nmax = q * periods
        L = Lp = 0
        for start in range(0, nmax, q):
            L += sum(v*w for v,w in zip(c[1:],term[start+1:start+q+1]))
            Lp -= sum(v*w for v,w in zip(c[1:],deriv[start+1:start+q+1]))
        # Each coefficient lost < 1 fixed-point unit. Partial sums of
        # the character beyond nmax start with a fresh complete period.
        lev = arb(arb(L)/scale, arb(nmax)/scale + arb(B)/nmax)
        dev = arb(arb(Lp)/scale, arb(nmax)/scale + arb(B)*arb(nmax).log()/nmax)
        estimate = arch + 2*dev/lev if lev > 0 else arb('0 +/- 100')
        if any(not (estimate < t or estimate > t) for t in (bound, arb(2))):
            estimate = arch + 2*exact_log_derivative(d)
            refined += 1
        if estimate < bound:
            selected.append(d)
        elif not estimate > bound:
            raise ArithmeticError(f"Could not resolve {d} at 96 bits")
        if estimate < 2 and estimate > bound:
            character_only.append(d)
        elif not (estimate < 2 or estimate > 2):
            raise ArithmeticError(f"Unresolved character threshold at {d}")
    return dict(checked=checked, jet_refinements=refined, selected=len(selected),
                negative=sum(d < 0 for d in selected), positive=sum(d > 0 for d in selected),
                discriminants=selected, character_test_only=character_only)


if __name__ == '__main__':
    print(json.dumps(classify(), indent=2))
