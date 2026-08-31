"""C4: the boundary telescope — numerical diagnostics on the CONJECTURAL
natural boundary of D(s) = prod_p (1 + 2 a_p p^{1-s} + p^{3-2s}),
the cube-defect bridge product of T-108507 (11a1 data, good primes).

What is actually computed (all claims labelled):

1. ZERO CONSTELLATION (exact input, float display): each local factor
   vanishes where |p^s| = p |gamma_p|; tempered-A_2 primes (a_p^2 <= p)
   put zeros EXACTLY on Re s = 3/2; untempered primes put them at
   sigma_p = 1 + log(|a_p| + sqrt(a_p^2 - p))/log p in a band shrinking
   like O(1/log p) to the right. The predicted accumulation line of the
   Kurokawa-type analysis is therefore Re s = 3/2 (NOT the absolute-
   convergence edge 5/2). Histogram deposited.

2. THE CONTROL THAT KEEPS US HONEST: the m=2 analogue
   D_2(s) = prod_p (1 + p^{1-s}) has zeros dense on Re s = 1 and yet IS
   meromorphic on C (= zeta^{(11)}(s-1)/zeta^{(11)}(2s-2), Estermann's
   cyclotomic case): dense local zeros do NOT imply a natural boundary.
   The criterion's true input is the ROOT-ANGLE behavior: D_2's local
   root angle is pinned at pi (cyclotomic), D's local root angles
   phi_p = arccos(-a_p/sqrt p)... equidistribute per the deformed
   Sato-Tate law. Both angle histograms deposited.

3. PARTIAL-PRODUCT DIAGNOSTICS: log|D_X(s)| for X in {1e3, 1e4, 1e5}
   on vertical lines sigma in {1.55, 1.75, 2.0, 2.25, 2.5, 2.75}, and
   the shifted control D_2 at sigma - 1/2, measuring stabilization; with
   the explicit caveat that non-stabilization below the convergence edge
   is expected for BOTH and distinguishes nothing by itself.

FLOAT_DIAGNOSTIC arithmetic class (stated); nothing here is a zero claim
or a boundary theorem. Writes matrix/c4_boundary_telescope.json.
rh_established = false.
"""
import cmath
import json
import math
import sys
import time

BAD = 11


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def load_ap():
    with open("matrix/ap_table_11a1.json") as f:
        t = json.load(f)
    return {int(p): v for p, v in t["a_p"].items()}


def part1_constellation(ap):
    say("1: zero constellation of D(s)")
    hist = {}
    band = []
    n_temp = n_unt = 0
    for p, a in ap.items():
        if a * a <= p:
            n_temp += 1
            sig = 1.5
        else:
            n_unt += 1
            g = abs(a) + math.sqrt(a * a - p)
            sig = 1 + math.log(g) / math.log(p)
            band.append((p, sig))
        key = f"{sig:.3f}"
        hist[key] = hist.get(key, 0) + 1
    band.sort(key=lambda t: -t[1])
    say(f"  tempered (on the line 3/2): {n_temp}; untempered: {n_unt}; "
        f"max sigma = {band[0][1]:.4f} at p={band[0][0]}; "
        f"max sigma among p>1e4: "
        f"{max(s for (p, s) in band if p > 10**4):.4f}")
    return {"tempered_primes_zeros_on_3_2": n_temp,
            "untempered_primes": n_unt,
            "rightmost_zero_sigma": band[0],
            "band_shrinks_like_1_over_log_p_examples":
                [(p, round(s, 4)) for (p, s) in band[:8]]
                + [(p, round(s, 4)) for (p, s) in band if p > 5 * 10 ** 4][:4],
            "histogram_sigma_0.001_bins_truncated":
                dict(sorted(hist.items())[:40]),
            "predicted_accumulation_line": 1.5,
            "note": ("prediction of the Kurokawa-type analysis, "
                     "CONDITIONAL and unproved; the absolute-convergence "
                     "edge is 5/2 and is NOT the predicted boundary")}


def part2_angles(ap):
    say("2: root-angle dichotomy (criterion input)")
    # D's local factor 1 + 2 a_p p^{1-s} + p^{3-2s}: with u = p^{1-s} it is
    # 1 + 2 a_p u + p u^2, roots u = (-a_p +- i sqrt(p - a_p^2))/p for
    # tempered p: |u| = p^{-1/2}, angle phi_p = arg(-a_p + i sqrt(p-a_p^2))
    # i.e. cos phi_p = -a_p / sqrt p: the SIGN-FLIPPED Sato-Tate angle.
    # Control: 1 + p^{1-s} root angle identically pi (cyclotomic).
    bins = [0] * 20
    n = 0
    for p, a in ap.items():
        if a * a > p:
            continue
        c = max(-1.0, min(1.0, -a / math.sqrt(p)))
        phi = math.acos(c)
        bins[min(19, int(phi / math.pi * 20))] += 1
        n += 1
    # deformed ST law for the A_2 angle Phi = arccos(-2 cos Theta), with
    # Theta ~ Sato-Tate CONDITIONED on |cos Theta| <= 1/2 (temperedness):
    # P(Phi <= phi) = P(cos Theta <= -cos(phi)/2)
    def st_m(th):                 # unconditioned ST cdf P(Theta <= th)
        return (th - math.sin(th) * math.cos(th)) / math.pi

    lo_n, hi_n = st_m(math.pi / 3), st_m(2 * math.pi / 3)
    norm = hi_n - lo_n

    def cdf(phi):
        xthr = -math.cos(phi) / 2.0          # in [-1/2, 1/2]
        th_x = math.acos(max(-0.5, min(0.5, xthr)))
        # P(cos Theta <= xthr) = P(Theta >= th_x), clipped to the band
        return (hi_n - st_m(th_x)) / norm

    st2 = [cdf((i + 1) * math.pi / 20) - cdf(i * math.pi / 20)
           for i in range(20)]
    emp = [b / n for b in bins]
    l1 = sum(abs(e - s) for e, s in zip(emp, st2))
    say(f"  tempered-prime angle histogram vs deformed-ST prediction: "
        f"L1 = {l1:.4f} over 20 bins ({n} primes)")
    return {"empirical_bins_20": emp, "deformed_st_prediction": st2,
            "L1_distance": l1,
            "control_root_angle": ("identically pi for D_2 = "
                                   "prod(1+p^{1-s}) — the cyclotomic/"
                                   "Estermann-meromorphic case"),
            "reading": ("equidistributed p-varying root angles vs pinned "
                        "cyclotomic angle IS the input the Estermann/"
                        "Kurokawa dichotomy quantifies; deposited as "
                        "criterion data, not as a boundary proof")}


def part3_partials(ap):
    say("3: partial-product stabilization scan")
    primes = sorted(ap)
    sigmas = [1.55, 1.75, 2.0, 2.25, 2.5, 2.75]
    tvals = [2.0, 7.0, 13.0]
    out = {}
    for sig in sigmas:
        row = {}
        for tv in tvals:
            s = complex(sig, tv)
            vals = {}
            logD = 0.0 + 0.0j
            logD2 = 0.0 + 0.0j
            nextX = 10 ** 3
            for p in primes:
                if p > 10 ** 5:
                    break
                a = ap[p]
                logD += cmath.log(1 + 2 * a * p ** (1 - s)
                                  + p ** (3 - 2 * s))
                logD2 += cmath.log(1 + p ** (1 - (s - 0.5)))
                if p >= nextX:
                    vals[str(nextX)] = {"logD": [logD.real, logD.imag],
                                        "logD2_shifted":
                                            [logD2.real, logD2.imag]}
                    nextX *= 10
            vals["100000"] = {"logD": [logD.real, logD.imag],
                              "logD2_shifted": [logD2.real, logD2.imag]}
            row[f"t={tv}"] = vals
        out[f"sigma={sig}"] = row
        d1 = abs(complex(*out[f"sigma={sig}"]["t=2.0"]["10000"]["logD"])
                 - complex(*out[f"sigma={sig}"]["t=2.0"]["100000"]["logD"]))
        say(f"  sigma={sig}: |logD(1e5)-logD(1e4)| at t=2: {d1:.4f}")
    out["caveat"] = ("non-stabilization below the respective convergence "
                     "edges is expected for BOTH the bridge product and "
                     "the meromorphic control; this scan is a diagnostic "
                     "record, not evidence of a boundary")
    return out


def main():
    ap = load_ap()
    out = {"meta": {"arithmetic_class": "FLOAT_DIAGNOSTIC (labelled)",
                    "curve": "11a1", "good_primes": len(ap),
                    "rh_established": False,
                    "correction_note": (
                        "an earlier working note predicted the boundary "
                        "at Re s = 5/2; the zero-constellation analysis "
                        "here places the conjectural accumulation line at "
                        "Re s = 3/2, the absolute-convergence edge 5/2 "
                        "being a different and irrelevant line")}}
    out["part1_zero_constellation"] = part1_constellation(ap)
    out["part2_angle_dichotomy"] = part2_angles(ap)
    out["part3_partial_products"] = part3_partials(ap)
    with open("matrix/c4_boundary_telescope.json", "w") as f:
        json.dump(out, f, indent=1)
    say("C4 done")


if __name__ == "__main__":
    main()
