#!/usr/bin/env python3
"""SKEPTIC replay of C2-13 (non-real zeros of H_t, t < 0) by an INDEPENDENT representation:
heat-flow / Gaussian convolution of H_0 = xi(1/2 + i w/2)/8 (mpmath zeta; no Phi, no u-integral):
    H_t(z) = (4 pi |t|)^{-1/2} int_R H_0(z - x) exp(-x^2 / (4|t|)) dx,     t < 0.
(Fourier transform of e^{t u^2} with t<0.)  NON-RIGOROUS (mpmath quad, dps 30).
Checks: (i) |H_t| at the investigator's certified midpoints vs at distance 1e-3;
(ii) Newton (secant) from a perturbed start converges to the same zero;
(iii) argument-principle count on a small circle (16 points)."""
import sys, os, json, time
import mpmath as mp
mp.mp.dps = 30


def xi(s):
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def H0(w):
    return xi(mp.mpf(1) / 2 + 1j * w / 2) / 8


def Ht(t, z):
    a = -mp.mpf(t)
    L = mp.sqrt(4 * a) * 9          # Gaussian truncation at ~ e^{-81}
    pts = [-L + k * (2 * L) / 24 for k in range(25)]   # Gaussian is centred at x = 0
    f = lambda x: H0(z - x) * mp.e ** (-x * x / (4 * a))
    return mp.quad(f, pts) / mp.sqrt(4 * mp.pi * a)


def main():
    t0 = time.time()
    out = {}
    # sanity: t -> 0^- limit check against H_0 at a real point (small |t|)
    out['check_t=-1e-3_vs_H0(10)'] = [mp.nstr(Ht(-1e-3, mp.mpf(10)), 12), mp.nstr(H0(mp.mpf(10)), 12)]
    cases = {'-20': mp.mpc('59.9341564005516729238731453730', '4.35624274468846131606718862929'),
             '-50': mp.mpc('81.3910374611188455295303217787', '13.4245153078415711904052702379')}
    for tt, z in cases.items():
        t = mp.mpf(tt)
        f0 = abs(Ht(t, z))
        f1 = min(abs(Ht(t, z + d)) for d in (mp.mpf('1e-3'), mp.mpc(0, '1e-3')))
        rec = dict(abs_H_at_mid=mp.nstr(f0, 5), min_abs_H_at_dist_1em3=mp.nstr(f1, 5), ratio=mp.nstr(f0 / f1, 5))
        try:
            zr = mp.findroot(lambda w: Ht(t, w), z + mp.mpc('0.2', '-0.15'), tol=1e-20)
            rec['secant_from_perturbed_start'] = [mp.nstr(mp.re(zr), 18), mp.nstr(mp.im(zr), 18)]
        except Exception as e:
            rec['secant_error'] = str(e)[:200]
        # argument principle on circle radius 0.05, 16 points (non-rigorous)
        K = 16
        vals = [Ht(t, z + mp.mpf('0.05') * mp.expjpi(2 * mp.mpf(k) / K)) for k in range(K)]
        w = sum(mp.arg(vals[(k + 1) % K] / vals[k]) for k in range(K)) / (2 * mp.pi)
        rec['winding_circle_r0.05'] = mp.nstr(w, 8)
        out[f't={tt}'] = rec
        print(tt, rec, round(time.time() - t0, 1), flush=True)
    out['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(out, open(os.path.join(sys.argv[1], 'sk_dbn.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
