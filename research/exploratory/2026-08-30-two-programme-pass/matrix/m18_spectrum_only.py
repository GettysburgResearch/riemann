"""Stage 1 of the memory-lean m = 18 sieve: compute ONLY the spectrum
polynomial M_18(z; a) at b = 1 (symbolic in a) and save its
coefficients; the disc/factor stage (which OOMed the direct route at
12.7 GB) is replaced by modular interpolation in stage 2.
rh_established = false.
"""
import json
import sys
import time

sys.path.insert(0, '.')
import sympy as sp

a, z = sp.symbols('a z')


def q_seq(n):
    q = [sp.Integer(2), a]
    for j in range(2, n + 1):
        q.append(sp.expand(a * q[-1] - q[-2]))
    return q


def defect_numerator_b1(m):
    dim = m + 1
    q = q_seq(m * (dim + 1) + 1)
    ps = []
    for j in range(1, dim + 1):
        s = sp.Integer(0)
        i = 0
        while 2 * i < m:
            s += q[(m - 2 * i) * j]
            i += 1
        if m % 2 == 0:
            s += sp.Integer(1)
        ps.append(sp.expand(s))
    e = [sp.Integer(1)]
    for k in range(1, dim + 1):
        s = sp.Integer(0)
        for i in range(1, k + 1):
            s += sp.Integer(-1) ** (i - 1) * e[k - i] * ps[i - 1]
        e.append(sp.expand(s / k))
    Q = [sp.Integer(-1) ** k * e[k] for k in range(dim + 1)]
    hh = [sp.Integer(1), a]
    for k in range(2, m + 5):
        hh.append(sp.expand(a * hh[-1] - hh[-2]))

    def c(r):
        s = sp.Integer(0)
        for u in range(r + 1):
            if r - u <= dim:
                s += Q[r - u] * hh[u] ** m
        return sp.expand(s)
    N = [c(r) for r in range(m)]
    for r in range(m, m + 3):
        assert sp.expand(c(r)) == 0
    return N


def spectrum_b1(N, m):
    # verbatim from disc_slice_m18.py (the committed, validated pipeline)
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    if eps:
        quo = [sp.Integer(0)] * (len(N) - 1)
        rem = list(N)
        for i in range(len(N) - 2, -1, -1):
            quo[i] = rem[i + 1]
            rem[i] = sp.expand(rem[i] - quo[i])
            rem[i + 1] = sp.Integer(0)
        assert sp.expand(rem[0]) == 0
        N = quo
    mus = [sp.Integer(0)] * (nu + 1)
    work = list(N)
    for j in range(nu, -1, -1):
        mu = work[nu + j]
        mus[j] = mu
        for i in range(j + 1):
            work[nu + 2 * i - j] = sp.expand(work[nu + 2 * i - j]
                                             - mu * sp.binomial(j, i))
    assert all(sp.expand(v) == 0 for v in work)
    assert mus[nu] == 1
    return mus, nu


def main():
    m = 18
    t0 = time.time()
    N = defect_numerator_b1(m)
    print(f"N done ({time.time()-t0:.0f}s)", flush=True)
    mus, nu = spectrum_b1(N, m)
    print(f"spectrum done: nu = {nu} ({time.time()-t0:.0f}s)", flush=True)
    out = {}
    for j in range(nu + 1):
        p = sp.Poly(mus[j], a)
        out[str(j)] = [str(c) for c in reversed(p.all_coeffs())]
    json.dump({"m": m, "nu": nu, "coeffs_low_to_high": out,
               "rh_established": False},
              open('matrix/m18_spectrum.json', 'w'))
    print(f"saved ({time.time()-t0:.0f}s)", flush=True)


if __name__ == "__main__":
    main()
