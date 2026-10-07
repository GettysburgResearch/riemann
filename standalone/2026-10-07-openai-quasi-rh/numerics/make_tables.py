"""
make_tables.py -- print Markdown tables from the JSON output of
check_identities.py and mean_square.py (used to assemble RESULTS.md).

Usage:  python3 -I make_tables.py identities.json mean_square.json
"""

import json
import math
import sys


def main():
    ident = json.load(open(sys.argv[1]))
    ms = json.load(open(sys.argv[2]))

    print(f"### Identities (all squarefree primary n, (n,6)=1, N(n) <= {ident['bound']}: "
          f"{ident['n_tested']} values of n)\n")
    print("| identity | max abs error |")
    print("|---|---|")
    names = {
        "a": "(a) gamma_2(n)^3 = mu(n) alpha(n)",
        "b": "(b) gamma_1 gamma_2 = mu alpha G, G = conj(chi_n(4)) gamma_3",
        "c": "(c) gamma_1 gamma_{-1} = chi_n(-1)",
        "d": "(d) mu gamma_{-1} = chi_n(-1) G^{-1} conj(alpha) gamma_2",
        "absG": "abs(G(n)) = 1",
        "gamma3_closed": "gamma_3(a+b w) = (1 + i^{-b} + i^a + i^{b-a})/2",
        "chi4_mod2": "chi_n(4) = (n mod 2) in {1, w, w^2}",
    }
    for k, v in ident["max_errors"].items():
        print(f"| {names[k]} | {v:.1e} |")
    r = ident["reciprocity"]
    print(f"| (e) chi_b(a)/chi_a(b) in {{+-1}} ({r['n_pairs']} coprime ordered pairs, N <= {r['pair_bound']}) "
          f"| {r['max_R_err']:.1e} |")
    print(f"| (e) R(a,b) vs (-1)^(eh+fg+fh) on square classes | {r['mismatches_with_bicharacter_formula']} mismatches |")
    print(f"| (e) R(a,b) constant on (a mod 4, b mod 4) | {r['inconsistent_class_pairs']} of "
          f"{r['n_class_pairs']} class pairs inconsistent |")
    print(f"| G(ab) = G(a)G(b)R(a,b) ({r['G_multiplicativity_pairs']} pairs) | {r['G_multiplicativity_max_err']:.1e} |")
    print(f"| eq:crt-a, a(ab) = a(a)a(b)chi_b(a)^4 (xi = 1) | {r['crt_a_max_err']:.1e} |")
    print(f"| chi_n(-1) = R(n,n) | {ident['max_err_chi_minus1_vs_R_nn']:.1e} |")
    print(f"| class level: G(ab)=G(a)G(b)R(a,b), all 144 class pairs mod 4 | {ident['class_level_G_mult_err']:.1e} |")
    print(f"| class level: G(a^-1) = chi_a(-1) conj G(a) (eq:quotient) | {ident['class_level_G_inverse_err']:.1e} |")
    print()
    print("| m | #classes of n mod m hit | max spread of G within a class |")
    print("|---|---|---|")
    for m, v in ident["G_mod_dependence"].items():
        print(f"| {m} | {v['G'][0]} | {v['G'][1]:.1e} |")
    print()

    print("### Mean square S(D,H), H = D^(1+theta)\n")
    print("| D | #n | sum w^2 / D | theta | H | #u | S/(DH) | S/diag | sixth-power u: S (count) "
          "| cube u | square u | rest u | max over rest u of abs(A_u)^2 / sum w^2 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for res in ms["results"]:
        for t in res["per_theta"]:
            print(f"| {res['D']} | {res['n_count']} | {res['sum_w2_over_D']:.4f} | {t['theta']:.2f} | "
                  f"{t['H']:.0f} | {t['n_u']} | {t['S_over_DH']:.4f} | {t['S_over_diag']:.4f} | "
                  f"{t['S_sixth']:.3g} ({t['n_sixth']}) | {t['S_cube']:.3g} ({t['n_cube']}) | "
                  f"{t['S_square']:.3g} ({t['n_square']}) | {t['S_rest']:.4g} ({t['n_rest']}) | "
                  f"{t['max_rest_over_sumw2']:.2f} |")
    print()
    print("Mean of abs(A_u)^2 / sum_n w_n^2 by class of u (theta = 0.1):\n")
    print("| D | unit*cube | unit*square | rest | E|A|^4/(E|A|^2)^2 (rest) | sixth-power share of S |")
    print("|---|---|---|---|---|---|")
    for res in ms["results"]:
        t = [t for t in res["per_theta"] if abs(t["theta"] - 0.1) < 1e-9][0]
        f = lambda x: "-" if x is None else f"{x:.3f}"  # noqa: E731
        print(f"| {res['D']} | {f(t['mean_cube_over_sumw2'])} | {f(t['mean_square_over_sumw2'])} | "
              f"{f(t['mean_rest_over_sumw2'])} | {t['fourth_moment_ratio_rest']:.3f} | {t['frac_S_sixth']:.1e} |")
    print()
    print("### A_1, units, amplification\n")
    print("| D | abs(A_1) | abs(A_1)/sqrt(D) | abs(A_1)/sqrt(sum w^2) | max_unit abs(A_eps) | "
          "N(p)=7: abs(A_p6 - A_1) | N(p)=13 | N(p)=19 | N(p)=25 (inert) | "
          "sum_(p|n) abs(w), N(p)=7 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for res in ms["results"]:
        amp = {}
        for a in res["amplification"]:
            amp.setdefault(a["Np"], a)
        mu = max(v[2] for v in res["A_units"].values())
        print(f"| {res['D']} | {res['absA1']:.2f} | {res['absA1']/math.sqrt(res['D']):.3f} | "
              f"{res['absA1_over_sqrt_sumw2']:.2f} | {mu:.2f} | {amp[7]['diff']:.2f} | {amp[13]['diff']:.2f} | "
              f"{amp[19]['diff']:.2f} | {amp[25]['diff']:.2f} | {amp[7]['trivial_bound']:.2f} |")
    print()
    errs = [(r["conj_symmetry_err"], r["lambda6_err"],
             max(a["check_err"] for a in r["amplification"])) for r in ms["results"]]
    print("Consistency: max |A_conj(u) - conj(A_u)| = %.1e; max |A_(eps lambda^6) - A_eps| = %.1e; "
          "max |(A_p6 - A_1) - direct formula| = %.1e" % (
              max(e[0] for e in errs), max(e[1] for e in errs if e[1] == e[1]),
              max(e[2] for e in errs)))


if __name__ == "__main__":
    main()
