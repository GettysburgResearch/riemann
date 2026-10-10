"""Tables for the end-to-end test of paper2 eq:reflection (OCT5_REFLECTION_E2E.md).

Status: EXPLORATORY.  FLOAT = ordinary double precision (not directed, not certified).
Builds, for all m in O = Z[omega] with 0 < N(m) <= NM:
  D_sigma(m) := d_sigma(m / lambda^4), sigma in {0,+,-}   (cusp coefficients of conj(theta), paper2
      eq:cusp-coefficient-definition, eq:conjugate-cusp-coefficients: d_sigma(l) = conj(t_sigma(-l)),
      t_0 = tau, t_- (l) = w^2 tau_1(w^2 l) echeck(l), t_+(l) = w tau_2(w l) echeck(l));
  and the squarefree primary n, (n,6)=1, N(n) <= NM, with gamma_2(n) (paper2 eq:intro-gauss-sum).
tau, tau_1, tau_2 are the DR (5.7), (5.13), (5.14) transcriptions of reviews/oct5_r3_theta_checks.py
(validated there by automorphy checks A, B, E, F); this file re-implements them from one factorisation
per lattice point and checks the re-implementation against the R3 functions for small norms.
Prime cubic Gauss sums come from oct5_reflection_e2e_gauss.c (checked against R3 g1_prime).
Usage: python3 -I oct5_reflection_e2e_tables.py NM OUT.npz GAUSS_BINARY
"""
import sys, os, math, cmath, time, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'a2'))
import oct5_r3_theta_checks as r3          # read before use; used as a library only
from eis import mul, conj, norm, is_primary, primary, divides, UNITS
import eis

OM = r3.OM
LAM = (1, 2)
ONE = (1, 0)
E29 = cmath.exp(2j * math.pi / 9)


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def rational_primes(N):
    isp = np.ones(N + 1, dtype=bool); isp[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = False
    return np.nonzero(isp)[0]


def spf_sieve(N):
    spf = np.zeros(N + 1, dtype=np.int32)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
            if i * i > N:
                # remaining zeros are primes
                z = np.nonzero(spf == 0)[0]
                z = z[z >= 2]
                spf[z] = z
                break
    return spf


def build_primes(NM):
    """primary primes of norm <= NM (prime 2 and lambda excluded from 'split'/'inert' lists as noted)."""
    out = []           # (elt, q, r) r = omega mod p for split, None for inert
    from sympy.ntheory import sqrt_mod
    for q in rational_primes(NM):
        q = int(q)
        if q == 3:
            continue
        if q % 3 == 1:
            s = sqrt_mod((-3) % q, q)
            w0 = ((-1 + s) * pow(2, -1, q)) % q
            g = r3.egcd((q, 0), (-w0, 1))[0]
            assert norm(g) == q
            for P in (primary(g), primary(conj(g))):
                a, b = P
                rr = (-a * pow(b, -1, q)) % q
                assert (rr * rr + rr + 1) % q == 0
                out.append((P, q, rr))
        elif q * q <= NM:
            out.append((primary((q, 0)), q * q, None))
    return out


def gauss_sums(primes, binary):
    inp = ''.join('%d %d\n' % P[0] for P in primes)
    res = subprocess.run([binary], input=inp, capture_output=True, text=True, check=True)
    g = {}
    for line in res.stdout.split('\n'):
        if not line.strip():
            continue
        a, b, re_, im_ = line.split()
        g[(int(a), int(b))] = complex(float(re_), float(im_))
    assert len(g) == len(primes)
    return g


def main():
    NM = int(sys.argv[1]); outp = sys.argv[2]; binary = sys.argv[3]
    t0 = time.time()
    primes = build_primes(NM)
    log('primes', len(primes))
    G1 = gauss_sums(primes, binary)
    log('gauss sums done', time.time() - t0)
    # check C Gauss sums against R3 g1_prime (numpy / python) for small primes
    errs = []
    for P, q, rr in primes:
        if q <= 3000:
            errs.append(abs(G1[P] - r3.g1_prime(P)) / math.sqrt(q))
    log('C gauss vs R3 g1_prime: n=%d max normalised err %.2e' % (len(errs), max(errs)))
    gauss_check = {'n': len(errs), 'max_err': max(errs)}
    r3._g1p.update(G1)
    # per prime: q, r, k_omega = (omega/p)_3, k_lam = (lambda/p)_3 exponents
    info = {}
    for P, q, rr in primes:
        if rr is not None:
            def c3(t):
                v = pow(t % q, (q - 1) // 3, q)
                return 0 if v == 1 else (1 if v == rr else 2)
            info[P] = (q, rr, c3(rr), c3(1 + 2 * rr))
        else:
            info[P] = (q, None, r3.cub_prime((0, 1), P), r3.cub_prime(LAM, P))
    # split-prime lookup by rational prime
    by_q = {}
    for P, q, rr in primes:
        by_q.setdefault(q if rr is not None else int(round(math.sqrt(q))), []).append(P)

    def cub_exp(a, P):
        """(a/P)_3 exponent; None if P | a."""
        q, rr, _, _ = info[P]
        if rr is not None:
            t = (a[0] + a[1] * rr) % q
            if t == 0:
                return None
            v = pow(t, (q - 1) // 3, q)
            return 0 if v == 1 else (1 if v == rr else 2)
        return r3.cub_prime(a, P)

    gt = {(): 1 + 0j}

    def gtilde(cs):
        """normalised g~(c), c = prod cs squarefree primary; g~(c1 c2) = conj((c1/c2)_3) g~(c1) g~(c2)."""
        v = gt.get(cs)
        if v is not None:
            return v
        if len(cs) == 1:
            v = G1[cs[0]] / math.sqrt(info[cs[0]][0])
        else:
            a = cs[0]; rest = cs[1:]
            k = sum(cub_exp(a, Q) for Q in rest) % 3
            v = (OM ** k).conjugate() * gtilde((a,)) * gtilde(rest)
        gt[cs] = v
        return v

    MU = {'1': (0, 0), 'L2': (0, 2), 'wL2': (1, 2), 'w2L2': (2, 2)}   # mu = omega^a lambda^b -> (a, b)

    def conj_g(mu, cs, Nc):
        a, b = MU[mu]
        k = (a * sum(info[Q][2] for Q in cs) + b * sum(info[Q][3] for Q in cs)) % 3
        g1 = gtilde(cs) * math.sqrt(Nc)
        return ((OM ** k).conjugate() * g1).conjugate()

    def tau_nu3(ui, e, cs, Nc, dc):
        """R3 tau_nu3 logic; nu = unit_ui * lambda^e * prod; L = e - 3."""
        L = e - 3
        if L % 3 == 2:
            n = (L + 4) // 3
            f = 3 ** (n / 2 + 2) * dc
            if ui in (0, 3):
                return conj_g('L2', cs, Nc) * f
            if ui in (2, 5):
                return E29.conjugate() * conj_g('wL2', cs, Nc) * f
            return E29 * conj_g('w2L2', cs, Nc) * f
        if L % 3 == 0:
            n = (L + 3) // 3
            if ui in (0, 3):
                return conj_g('1', cs, Nc) * dc * 3 ** (n / 2 + 2.5)
            return 0j
        return 0j

    def tau12_nu4(ui, e, cs, Nc, dc, which):
        if e != 0:
            return 0j
        if which == 1:
            if ui == 0:
                return 9 * OM * conj_g('L2', cs, Nc) * dc
            if ui == 2:
                return 9 * E29.conjugate() * OM ** 2 * conj_g('wL2', cs, Nc) * dc
            if ui == 4:
                return 9 * E29 * conj_g('w2L2', cs, Nc) * dc
            return 0j
        if ui == 3:
            return 9 * OM ** 2 * conj_g('L2', cs, Nc) * dc
        if ui == 5:
            return 9 * E29.conjugate() * conj_g('wL2', cs, Nc) * dc
        if ui == 1:
            return 9 * OM * E29 * conj_g('w2L2', cs, Nc) * dc
        return 0j

    spf = spf_sieve(NM)
    log('spf done')
    U3 = {(u[0] % 3, u[1] % 3): k for k, u in enumerate(UNITS)}
    keyf = lambda Q: (norm(Q), Q)

    def factor_m(m):
        """returns (unit index of m / lambda^e, e, cs sorted, N(cs), |b|^2 = N(b)) or None if some exponent == 2 mod 3."""
        x, y = m
        N = x * x - x * y + y * y
        e = 0; fac = []
        n = N
        while n > 1:
            q = int(spf[n]); k = 0
            while n % q == 0:
                n //= q; k += 1
            if q == 3:
                e = k
            elif q % 3 == 2:
                fac.append(((-q, 0), k // 2))
            else:
                P1, P2 = by_q[q]
                q_, rr, _, _ = info[P1]
                # v_{P1}(m): divide repeatedly
                mm = m; k1 = 0
                while (mm[0] + mm[1] * rr) % q == 0:
                    mm = r3.exact_div(mm, P1); k1 += 1
                if k1:
                    fac.append((P1, k1))
                if k - k1:
                    fac.append((P2, k - k1))
        if any(k % 3 == 2 for _, k in fac):
            return None, e
        mp_ = m
        for _ in range(e):
            mp_ = r3.exact_div(mp_, LAM)
        ui = U3[(mp_[0] % 3, mp_[1] % 3)]
        cs = tuple(sorted((P for P, k in fac if k % 3 == 1), key=keyf))
        Nc = 1
        for P in cs:
            Nc *= norm(P)
        Nb = 1
        for P, k in fac:
            Nb *= norm(P) ** (k // 3)
        return (ui, cs, Nc, Nb), e

    ymax = int(math.sqrt(4 * NM / 3)) + 2
    MX, MY, NN, D0, DP, DMm = [], [], [], [], [], []
    LX, LY, LN, LG = [], [], [], []
    cnt = 0
    for y in range(-ymax, ymax + 1):
        for x in range(-ymax - abs(y), ymax + abs(y) + 1):
            N = x * x - x * y + y * y
            if N > NM or N == 0:
                continue
            cnt += 1
            fm, e = factor_m((x, y))
            if fm is None:
                continue
            ui, cs, Nc, Nb = fm
            dc = math.sqrt(Nb / Nc)
            # D_0(m) = conj(tau(-l)), -l = -m/lambda^4 = nu/lambda^3 with nu = -m/lambda: unit index +3, e-1
            d0 = 0j
            if e >= 1:
                t = tau_nu3((ui + 3) % 6, e - 1, cs, Nc, dc)
                d0 = t.conjugate()
            # echeck(l), l = m/9:  exp(2 pi i * 2 Re(m)/9) = exp(2 pi i (2x - y)/9)
            ech = cmath.exp(2j * math.pi * ((2 * x - y) % 9) / 9)
            # D_+(m) = conj(w) conj(tau_2(-w l)) echeck(l);  -w m: unit index +5
            t2 = tau12_nu4((ui + 5) % 6, e, cs, Nc, dc, 2)
            dp = OM.conjugate() * t2.conjugate() * ech
            # D_-(m) = conj(w^2) conj(tau_1(-w^2 l)) echeck(l);  -w^2 m: unit index +1
            t1 = tau12_nu4((ui + 1) % 6, e, cs, Nc, dc, 1)
            dm = OM * t1.conjugate() * ech
            if d0 != 0 or dp != 0 or dm != 0:
                MX.append(x); MY.append(y); NN.append(N); D0.append(d0); DP.append(dp); DMm.append(dm)
            # LHS data: m primary squarefree, prime to 6
            if ui == 0 and e == 0 and Nb == 1 and Nc == N and N % 2 == 1:
                kl = sum(info[Q][3] for Q in cs) % 3
                LX.append(x); LY.append(y); LN.append(N); LG.append(OM ** kl * gtilde(cs))
        if y % 100 == 0:
            log('row y=%d points=%d kept=%d lhs=%d' % (y, cnt, len(MX), len(LX)))
    log('lattice loop done', cnt, len(MX), len(LX), time.time() - t0)
    # self-check of the re-implementation against R3 functions (small norms)
    nchk = 0; worst = 0.0
    for i in range(len(MX)):
        if NN[i] > 1500:
            continue
        nu = (MX[i], MY[i])
        ell = r3.toc(nu) / r3.LAMC ** 4
        ref0 = r3.tau_nu3(r3.exact_div(r3.neg(nu), LAM)).conjugate() if divides(LAM, nu) else 0j
        ech = cmath.exp(4j * math.pi * ell.real)
        refp = (OM * r3.tau12_nu4(mul((0, 1), r3.neg(nu)), 2) * cmath.exp(-4j * math.pi * ell.real)).conjugate()
        refm = (OM ** 2 * r3.tau12_nu4(mul((-1, -1), r3.neg(nu)), 1) * cmath.exp(-4j * math.pi * ell.real)).conjugate()
        worst = max(worst, abs(ref0 - D0[i]), abs(refp - DP[i]), abs(refm - DMm[i]))
        nchk += 1
    log('reimplementation vs R3 tau functions: n=%d max abs err %.2e' % (nchk, worst))
    # gamma_2 check against direct eis.gamma for small n
    gerr = 0.0; ng = 0
    for i in range(len(LX)):
        if LN[i] > 400:
            continue
        n = (LX[i], LY[i])
        u, e, fac = r3.factor(n)
        ref = eis.gamma(2, list(fac.keys()))
        gerr = max(gerr, abs(ref - LG[i])); ng += 1
    log('gamma_2 vs direct: n=%d max err %.2e' % (ng, gerr))
    np.savez(outp, NM=NM, mx=np.array(MX, dtype=np.int64), my=np.array(MY, dtype=np.int64), N=np.array(NN, dtype=np.int64),
             d0=np.array(D0), dp=np.array(DP), dm=np.array(DMm),
             lx=np.array(LX, dtype=np.int64), ly=np.array(LY, dtype=np.int64), lN=np.array(LN, dtype=np.int64), lg=np.array(LG),
             checks=np.array([gauss_check['n'], gauss_check['max_err'], nchk, worst, ng, gerr]))
    log('saved', outp, time.time() - t0)


if __name__ == '__main__':
    main()
