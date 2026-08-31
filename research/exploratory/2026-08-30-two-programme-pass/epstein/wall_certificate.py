"""Lane 4 — a PROVED off-critical-line zero for the Epstein lab.

Target: the rectangular modulus z = 10i, i.e. the unimodular binary
form Q(m, n) = (m^2 + 100 n^2)/10 (equivalently the integral form
m^2 + 100 n^2, discriminant -400). Completed zeta:

  Lambda(s) := pi^{-s} Gamma(s) Z_Q(s),   Z_Q(s) = sum'_{v != 0} Q(v)^{-s},

with the classical incomplete-gamma representation (theta transform,
proved in the standalone file; theta_Q is SELF-dual since Q* = Q o swap):

  Lambda(s) = 1/(s-1) - 1/s
            + sum'_{v} [ (pi Q)^{-s} Gamma(s, pi Q)
                       + (pi Q)^{s-1} Gamma(1-s, pi Q) ],  Q = Q(v).

CERTIFICATE (rigorous): evaluate Lambda at s = 3/4 and s = 17/20 in
mpmath.iv directed-rounding INTERVAL arithmetic (dps 120), with
  - Gamma(a, x) = Gamma(a) - gamma_low(a, x), the lower-gamma series
    x^a e^{-x} sum_k x^k / (a (a+1) ... (a+k)) truncated at
    K = 2 ceil(x) + 60 with tail <= last term (ratio < 1/2), added as
    an explicit interval [0, bound];
  - Gamma(a) from iv.gamma, INDEPENDENTLY CHECKED at the four needed
    points by the reflection formula (Gamma(a) Gamma(1-a) must contain
    pi / sin(pi a), an interval identity);
  - lattice cutoff Q <= X = 25 with the PROVED tail bound
    (0 < a <= 1, x > 0  =>  Gamma(a,x) <= x^{a-1} e^{-x}, since
    t^{a-1} is decreasing):  each tail term <= e^{-pi Q}/(pi Q), and
      sum_{Q > X} e^{-pi Q} <= e^{-pi X/2} * sum'_v e^{-pi Q(v)/2}
                            <= e^{-pi X/2} * ((1+2A)(1+2B) - 1),
    A = q/(1-q), q = e^{-pi/(2y)} (geometric domination of the m-sum,
    m^2 >= m), B = q'/(1-q'), q' = e^{-pi y/2} — all evaluated as
    intervals and added as [ -bound, bound ].
If the two Lambda intervals exclude 0 with opposite signs, Z_Q has a
REAL zero sigma_0 in (3/4, 17/20), strictly off the critical line
Re s = 1/2 (with its functional-equation partner in (3/20, 1/4)).

Context and honesty: real off-line zeros of Epstein zetas of this
rectangular family are a CLASSICAL phenomenon (Bateman-Grosswald;
CITATION-NEEDED for the precise threshold statement). The
contribution here is the certificate itself: the lab's first
PROVED-grade zero statement, at an exact rational modulus, fully
self-contained. Epstein zetas are not the Riemann zeta; nothing here
bears on RH. rh_established = false.

Float reconnaissance (dps 40) cross-checks the representation against
the independent Chowla-Selberg / K-Bessel formula before certifying.
"""
import json
import time

import mpmath as mp

Y = 10                       # the modulus z = i*Y, exact integer
X_CUT = 25                   # lattice cutoff on Q(v)
SIGMAS = [(3, 4), (17, 20)]  # exact rational certificate points


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---------------- Part R: float reconnaissance ----------------------

def lam_ig_float(s):
    """incomplete-gamma route, plain mpmath floats."""
    s = mp.mpf(s)
    tot = 1 / (s - 1) - 1 / s
    for m in range(-60, 61):
        for n in range(-3, 4):
            if m == 0 and n == 0:
                continue
            Q = mp.mpf(m * m + Y * Y * n * n) / Y
            x = mp.pi * Q
            if x > 120:
                continue
            tot += (x ** -s * mp.gammainc(s, x)
                    + x ** (s - 1) * mp.gammainc(1 - s, x))
    return tot


def lam_cs_float(s):
    """independent Chowla-Selberg / K-Bessel route (x = 0, y = Y):
    E(s) = 2 zeta(2s) y^s + 2 sqrt(pi) Gamma(s-1/2)/Gamma(s)
           * zeta(2s-1) y^{1-s}
         + (8 pi^s / Gamma(s)) sqrt(y) sum_{n>=1} n^{s-1/2}
           sigma_{1-2s}(n) K_{s-1/2}(2 pi n y),
    Lambda = pi^{-s} Gamma(s) E(s)."""
    s = mp.mpf(s)
    y = mp.mpf(Y)
    E = 2 * mp.zeta(2 * s) * y ** s
    E += (2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s)
          * mp.zeta(2 * s - 1) * y ** (1 - s))
    acc = mp.mpf(0)
    for n in range(1, 8):
        sig = sum(mp.mpf(d) ** (1 - 2 * s)
                  for d in range(1, n + 1) if n % d == 0)
        acc += (n ** (s - mp.mpf(1) / 2) * sig
                * mp.besselk(s - mp.mpf(1) / 2, 2 * mp.pi * n * y))
    E += 8 * mp.pi ** s / mp.gamma(s) * mp.sqrt(y) * acc
    return mp.pi ** -s * mp.gamma(s) * E


# ---------------- Part C: interval certificate ----------------------

iv = mp.iv


def iv_rat(p, q=1):
    return iv.mpf(p) / iv.mpf(q)


def iv_pow(x, a):
    """x^a for positive interval x."""
    return iv.exp(a * iv.log(x))


def gamma_upper_iv(a, x, gamma_a):
    """Gamma(a, x) as an interval, 0 < a <= 1, x > 0 (interval x)."""
    K = 2 * int(mp.ceil(mp.mpf(x.b))) + 60
    # lower-gamma series
    term = iv_pow(x, a) * iv.exp(-x) / a
    total = term
    for k in range(1, K + 1):
        term = term * x / (a + iv.mpf(k))
        total = total + term
    # tail <= term_K * r/(1-r), r = x/(a+K+1) < 1/2  => tail <= term_K
    tail_ub = term.b
    assert mp.mpf(x.b) / (mp.mpf(a.a) + K + 1) < 0.5
    total = total + iv.mpf([0, tail_ub])
    return gamma_a - total


def certify_sigma(p, q):
    """Interval for Lambda(p/q)."""
    s = iv_rat(p, q)
    one = iv.mpf(1)
    # reflection-formula check of iv.gamma at BOTH needed points
    ga = iv.gamma(s)
    gb = iv.gamma(one - s)
    lhs = ga * gb
    rhs = iv.pi / iv.sin(iv.pi * s)
    # containment test: the two intervals must overlap (both enclose
    # the same real number); require overlap width consistency
    assert not (mp.mpf(lhs.b) < mp.mpf(rhs.a) or
                mp.mpf(rhs.b) < mp.mpf(lhs.a)), "reflection check failed"

    tot = one / (s - one) - one / s
    # lattice sum, Q <= X_CUT  (m^2 + 100 n^2 <= 10*X_CUT)
    nv = 0
    for m in range(-60, 61):
        for n in range(-3, 4):
            if m == 0 and n == 0:
                continue
            num = m * m + Y * Y * n * n
            if num > Y * X_CUT:
                continue
            nv += 1
            Q = iv_rat(num, Y)
            x = iv.pi * Q
            t1 = iv_pow(x, -s) * gamma_upper_iv(s, x, ga)
            t2 = iv_pow(x, s - one) * gamma_upper_iv(one - s, x, gb)
            tot = tot + t1 + t2
    # tail bound
    q1 = iv.exp(-iv.pi / (2 * iv.mpf(Y)))
    A = q1 / (one - q1)
    q2 = iv.exp(-iv.pi * iv.mpf(Y) / 2)
    B = q2 / (one - q2)
    theta_half = (one + 2 * A) * (one + 2 * B) - one
    tail = (iv.mpf(2) / (iv.pi * iv.mpf(X_CUT))
            * iv.exp(-iv.pi * iv.mpf(X_CUT) / 2) * theta_half)
    tail_ub = tail.b
    tot = tot + iv.mpf([-tail_ub, tail_ub])
    return tot, nv, tail_ub


def main():
    out = {"target": {"z": "10*i", "form": "m^2 + 100 n^2 (disc -400)",
                      "normalized_Q": "(m^2 + 100 n^2)/10"},
           "rh_established": False,
           "note": ("phenomenon classical (Bateman-Grosswald real "
                    "zeros; CITATION-NEEDED); certificate new to the "
                    "lab. Epstein zeta != Riemann zeta; no bearing "
                    "on RH.")}
    # Part R
    mp.mp.dps = 40
    say("Part R: cross-checking the representation (float, dps 40)")
    xr = {}
    for sig in ("0.6", "0.8"):
        a = lam_ig_float(mp.mpf(sig))
        b = lam_cs_float(mp.mpf(sig))
        d = abs(a - b)
        xr[sig] = {"incomplete_gamma": mp.nstr(a, 25),
                   "chowla_selberg": mp.nstr(b, 25),
                   "abs_diff": mp.nstr(d, 5)}
        say(f"  sigma={sig}: |diff| = {mp.nstr(d, 5)}")
        assert d < mp.mpf('1e-25'), "representations disagree"
    out["cross_check_float"] = xr

    # Part C
    iv.dps = 120
    say("Part C: interval certificate (iv, dps 120)")
    cert = []
    signs = []
    for (p, q) in SIGMAS:
        t0 = time.time()
        val, nv, tail_ub = certify_sigma(p, q)
        lo, hi = mp.mpf(val.a), mp.mpf(val.b)
        sign = "POSITIVE" if lo > 0 else ("NEGATIVE" if hi < 0 else
                                          "INCONCLUSIVE")
        signs.append(sign)
        cert.append({"sigma": f"{p}/{q}",
                     "interval_lo": mp.nstr(lo, 30),
                     "interval_hi": mp.nstr(hi, 30),
                     "width": mp.nstr(hi - lo, 5),
                     "lattice_vectors": nv,
                     "tail_bound": mp.nstr(mp.mpf(tail_ub), 5),
                     "sign": sign})
        say(f"  Lambda({p}/{q}) in [{mp.nstr(lo, 20)}, "
            f"{mp.nstr(hi, 20)}]  -> {sign} ({time.time()-t0:.1f}s)")
    out["certificate"] = cert
    ok = signs == ["POSITIVE", "NEGATIVE"]
    # refinement: certified signs on a finer rational grid
    refine = []
    for (p, q) in [(39, 50), (79, 100), (4, 5), (81, 100), (41, 50)]:
        val, _, _ = certify_sigma(p, q)
        lo, hi = mp.mpf(val.a), mp.mpf(val.b)
        sgn = "POSITIVE" if lo > 0 else ("NEGATIVE" if hi < 0 else
                                         "INCONCLUSIVE")
        refine.append({"sigma": f"{p}/{q}", "sign": sgn,
                       "interval_lo": mp.nstr(lo, 25),
                       "interval_hi": mp.nstr(hi, 25)})
        say(f"  refine Lambda({p}/{q}): {sgn} "
            f"[{mp.nstr(lo, 12)}, {mp.nstr(hi, 12)}]")
    out["refinement"] = refine
    # the headline bracket (81/100, 41/50) rests on the refinement
    # signs — assert them in the VERIFIED gate (verification-wave fix)
    ok = ok and [r["sign"] for r in refine] == \
        ["POSITIVE", "POSITIVE", "POSITIVE", "POSITIVE", "NEGATIVE"]
    out["conclusion"] = {
        "verified": ok,
        "statement": ("Z_Q(s) has a real zero sigma_0 with "
                      "3/4 < sigma_0 < 17/20 — strictly off the "
                      "critical line Re s = 1/2 — and by the "
                      "functional equation a partner zero in "
                      "(3/20, 1/4)." if ok else "NOT ESTABLISHED")}
    out["arithmetic_class"] = ("PROVED (directed-rounding interval "
                               "arithmetic, mpmath.iv dps 120; all "
                               "truncations bounded explicitly; "
                               "iv.gamma cross-checked by the "
                               "reflection identity)" if ok else
                               "FAILED")
    json.dump(out, open('epstein/wall_certificate.json', 'w'), indent=1)
    say("VERIFIED" if ok else "NOT VERIFIED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
