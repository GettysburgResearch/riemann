#!/usr/bin/env python3
"""C2 countermodel zoo -- de Bruijn-Newman deformations H_t, t < 0.

H_t(z) = int_0^inf e^{t u^2} Phi(u) cos(z u) du,
Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u})       (Rodgers-Tao 2020 normalisation;
H_0(z) = (1/8) xi(1/2 + i z/2)).  Lambda >= 0 (Rodgers-Tao) => for every t < 0, H_t has a non-real zero.
This script
  (a) NON-RIGOROUS: for a list of t < 0, finds zeros of H_t in a box via Newton from a grid (mpmath quad);
  (b) RIGOROUS: Arb (acb.integral) enclosure of H_t and H_t' on a complex ball with explicit truncation bounds,
      used in the Krawczyk test (zoo_common) to certify one non-real zero for selected t;
  (c) NON-RIGOROUS: Turan inequalities b_m^2 >= ((2m-1)/(2m+1)) b_{m-1} b_{m+1} for the moments
      b_m(t) = int_0^inf u^{2m} e^{t u^2} Phi(u) du, m = 1..M, for several t (incl. t < 0), and the
      log-concavity of v -> Phi(sqrt v) on a grid (second differences).
Usage: python3 dbn_Ht.py OUTDIR
"""
import sys, os, json, time, hashlib
import mpmath as mp
import flint
from flint import acb, arb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_common import certify_zero, versions

# ---------------- non-rigorous (mpmath) ----------------
mp.mp.dps = 30


def Phi_mp(u, N=8):
    return mp.fsum((2 * mp.pi ** 2 * n ** 4 * mp.e ** (9 * u) - 3 * mp.pi * n ** 2 * mp.e ** (5 * u))
                   * mp.e ** (-mp.pi * n ** 2 * mp.e ** (4 * u)) for n in range(1, N + 1))


def H_mp(t, z, deriv=False):
    if deriv:
        f = lambda u: -u * mp.e ** (t * u * u) * Phi_mp(u) * mp.sin(z * u)
    else:
        f = lambda u: mp.e ** (t * u * u) * Phi_mp(u) * mp.cos(z * u)
    return mp.quad(f, [0, 0.25, 0.5, 0.75, 1.0, 1.5])


def find_zeros_mp(t, xmax=60, ymax=12, nx=31, ny=7):
    zs = []
    for i in range(nx):
        for j in range(ny):
            z0 = mp.mpc(2 + (xmax - 2) * i / (nx - 1), ymax * j / (ny - 1))
            z = z0
            ok = False
            for _ in range(40):
                try:
                    step = H_mp(t, z) / H_mp(t, z, True)
                except ZeroDivisionError:
                    break
                z -= step
                if abs(step) < mp.mpf(10) ** (-20):
                    ok = True
                    break
                if abs(z) > 4 * xmax:
                    break
            if ok and z.real > 0 and -1e-15 < z.imag and z.real < xmax + 5:
                if all(abs(z - w) > 1e-8 for w in zs):
                    zs.append(z)
    zs.sort(key=lambda w: float(w.real))
    return [(float(w.real), float(w.imag), float(abs(H_mp(t, w)))) for w in zs]


# ---------------- rigorous (Arb) ----------------
U = 1          # integrate over [0, U]
NN = 6         # terms n <= NN of Phi


def _phi_acb(u):
    tot = acb(0)
    pi = arb.pi()
    e4 = (4 * u).exp(); e5 = (5 * u).exp(); e9 = (9 * u).exp()
    for n in range(1, NN + 1):
        tot += (2 * pi ** 2 * n ** 4 * e9 - 3 * pi * n ** 2 * e5) * (-pi * n * n * e4).exp()
    return tot


def _err_bound(ymax):
    """Upper bound (arb) for |error| in H_t and H_t' from (i) n > NN on [0,U], (ii) u > U, for |Im z| <= ymax, t<=0."""
    pi = arb.pi()
    Ua = arb(U)
    B = lambda n: (2 * pi ** 2 * n ** 4 * (9 * Ua).exp() + 3 * pi * n * n * (5 * Ua).exp()) * (-pi * n * n).exp()
    # ratio B(n+1)/B(n) < 1/2 for n >= NN+1 >= 2, so sum_{n>NN} B(n) <= 2 B(NN+1)
    e1 = Ua * 2 * B(NN + 1) * (arb(ymax) * Ua).cosh() * (1 + Ua)   # (1+U) covers the extra factor u in H_t'
    # (ii) u >= U: |integrand| <= 5 pi^2 n^4 e^{(10+y)u} e^{-pi n^2 e^{4u}};  int_U^inf <= e^{-(pi n^2 e^{4U}-(10+y)U)}
    #      / (4 pi n^2 e^{4U} - (10+y)) (convexity of the exponent);  sum over n bounded by 2x first term.
    y = arb(ymax)
    a = pi * (4 * Ua).exp()
    e2 = 2 * 5 * pi ** 2 * (-(a - (10 + y) * Ua)).exp() / (4 * a - (10 + y))
    return e1 + e2


def H_acb(t, z, deriv=False):
    """Enclosure of H_t(z) (or H_t'(z)) valid for every point of the complex ball z (t <= 0 real)."""
    tt = arb(t)
    if deriv:
        g = lambda u, _: -u * (tt * u * u).exp() * _phi_acb(u) * (z * u).sin()
    else:
        g = lambda u, _: (tt * u * u).exp() * _phi_acb(u) * (z * u).cos()
    val = acb.integral(g, 0, U)
    ymax = float(abs(z.imag).upper()) + 1e-30
    eb = _err_bound(ymax)
    return val + acb(arb(0, eb), arb(0, eb))


def fd_factory(t):
    return lambda z: (H_acb(t, z), H_acb(t, z, True))


# ---------------- moments / Turan ----------------
def moments_mp(t, M):
    return [mp.quad(lambda u: u ** (2 * m) * mp.e ** (t * u * u) * Phi_mp(u), [0, 0.25, 0.5, 1, 1.5, 2])
            for m in range(M + 2)]


def turan(t, M=40):
    b = moments_mp(t, M)
    worst = None
    out = []
    for m in range(1, M + 1):
        r = b[m] ** 2 / (b[m - 1] * b[m + 1]) - mp.mpf(2 * m - 1) / (2 * m + 1)
        out.append(float(r))
        if worst is None or r < worst[1]:
            worst = (m, float(r))
    return dict(t=t, M=M, min_margin=worst, all_hold=all(x > 0 for x in out))


def logconcavity_check(vmax=2.0, npts=400):
    """Second differences of log Phi(sqrt v) on (0, vmax] (non-rigorous, mpmath)."""
    h = mp.mpf(vmax) / npts
    vals = [mp.log(Phi_mp(mp.sqrt(h * k))) for k in range(1, npts + 2)]
    d2 = [vals[k - 1] - 2 * vals[k] + vals[k + 1] for k in range(1, npts)]
    return dict(vmax=vmax, npts=npts, max_second_difference=float(max(d2)), all_negative=all(x < 0 for x in d2))


def main():
    outdir = sys.argv[1]
    tlist = [float(x) for x in (sys.argv[2].split(',') if len(sys.argv) > 2 else ['-100', '-50', '-20'])]
    t0 = time.time()
    rep = dict(model='de Bruijn-Newman H_t, t<0', versions=versions(), params=dict(U=U, NN=NN, mp_dps=mp.mp.dps))
    # sanity: H_0(z) = xi(1/2 + i z/2)/8
    z = mp.mpf(10)
    xi = lambda s: s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    rep['check_H0_vs_xi_at_z10'] = [float(H_mp(0, z)), float(mp.re(xi(mp.mpf(0.5) + 1j * z / 2)) / 8)]
    res = {}
    for t in tlist:
        zs = find_zeros_mp(t)
        nonreal = [w for w in zs if w[1] > 1e-6]
        res[str(t)] = dict(zeros_found=zs, nonreal=nonreal)
        print(t, 'nonreal', nonreal[:4], round(time.time() - t0, 1), flush=True)
    rep['zeros_mp'] = res
    # rigorous certificates for the first non-real zero at each t
    flint.ctx.prec = 96
    certs = {}
    for t in tlist:
        nr = res[str(t)]['nonreal']
        if not nr:
            continue
        w = complex(nr[0][0], nr[0][1])
        c = certify_zero(fd_factory(t), w, radii=(1e-3, 1e-6, 1e-10), want_off_line=None)
        c['approx'] = [w.real, w.imag]
        if c.get('ok'):
            c['imag_part_lower_bound'] = c['im_lo']
            c['nonreal_certified'] = float(c['im_lo']) > 0
        certs[str(t)] = c
        print('cert', t, c.get('ok'), c.get('im_lo'), round(time.time() - t0, 1), flush=True)
    rep['certificates'] = certs
    rep['turan'] = [turan(t) for t in [0.0, -1.0, -20.0, -100.0, 0.5]]
    rep['logconcavity_Phi_sqrt'] = logconcavity_check()
    rep['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'dbn_Ht.json')
    json.dump(rep, open(fn, 'w'), indent=1, default=str)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn, rep['runtime_s'])


if __name__ == '__main__':
    main()
