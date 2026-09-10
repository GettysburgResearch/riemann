"""E3 validation: does the coded Weil functional reproduce sum_rho h(gamma)?

Safety net for E3. A sign or constant error would manufacture a spurious "RH
refuted", so the functional is not trusted until it matches a direct sum over
actual zeros. Zeros come from mpmath's Hardy Z function, an INDEPENDENT source;
this file is a cross-check only and is never part of an acceptance path.

Isolating tau(m): for c = e_1 + e_{1+m},
    h(r) = d^2 sinc^4(r d/2) |1 + e^{i r m d}|^2 = d^2 sinc^4 * 4 cos^2(r m d/2),
and the quadratic form equals 2 tau(0) + 2 tau(m), so
    tau(m)_from_zeros = (sum_gamma h(gamma) - 2 tau(0)_from_zeros) / 2.
"""

import sys

import mpmath as mp

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from flint import arb  # noqa: E402

from common import set_prec  # noqa: E402
from e3_weil_form import build_tau  # noqa: E402


def hardy_zeros(tmax, step=0.05):
    zs, t, prev = [], mp.mpf(1), mp.siegelz(1)
    while t < tmax:
        t2 = t + step
        cur = mp.siegelz(t2)
        if mp.sign(prev) != mp.sign(cur):
            zs.append(mp.findroot(mp.siegelz, (t, t2), solver="bisect", tol=1e-22))
        t, prev = t2, cur
    return zs


def sinc4(x):
    return mp.mpf(1) if x == 0 else (mp.sin(x) / x) ** 4


def zero_sum(gammas, d, m):
    d = mp.mpf(d)
    tot = mp.mpf(0)
    for g in gammas:
        base = d**2 * sinc4(g * d / 2)
        tot += 2 * base if m == 0 else 2 * base * 4 * mp.cos(g * m * d / 2) ** 2
    return tot


def main():
    mp.mp.dps = 25
    set_prec(320)
    d = float(sys.argv[1]) if len(sys.argv) > 1 else 0.25
    NM = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    tmax = 900
    print(f"zeta zeros to t={tmax} from Hardy Z (independent cross-check) ...",
          flush=True)
    gammas = hardy_zeros(tmax)
    print(f"  {len(gammas)} zeros; first {float(gammas[0]):.6f}, "
          f"last {float(gammas[-1]):.3f}", flush=True)
    taus, limit, npp = build_tau(NM, d, 320)
    t0m = zero_sum(gammas, d, 0)
    print(f"\ndelta={d}, prime cutoff {limit}, {npp} prime powers\n")
    print(f"{'m':>3} {'tau(m) coded':>18} {'tau(m) from zeros':>20} {'ratio':>9}"
          f" {'abs diff':>12}")
    ok = True
    for m in range(NM):
        coded = float(arb(taus[m]).mid())
        meas = float(t0m) if m == 0 else float((zero_sum(gammas, d, m) - 2 * t0m) / 2)
        r = coded / meas if meas != 0 else float("nan")
        flag = "" if abs(coded - meas) < 2e-4 else "   <-- MISMATCH"
        if flag:
            ok = False
        print(f"{m:>3} {coded:18.10f} {meas:20.10f} {r:9.4f} "
              f"{abs(coded-meas):12.3e}{flag}")
    print("\nVALIDATION:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
