"""World 'zeta': the Riemann zeta function  zeta(s) = sum_{n>=1} n^{-s}.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.zeta_build

regenerates worlds/zeta.json identically.

Structure of this file:
  1. exact local data: at EVERY prime p the local factor of zeta is
     1/(1 - p^{-s}); in the variable T = p^{-s} the Satake polynomial is
         det(1 - A T) with A = [1], i.e. satake = 1 - T = [1, -1] (low-first).
     Its coefficient expansion is the all-ones sequence a_{p^k} = 1.
  2. exact witnesses computed here with Fraction arithmetic ONLY:
       - coefficient sequence and power sums of the Satake data;
       - total multiplicativity of a_n = 1 (complete trivial proof + finite
         exact check);
       - Euler local-global reconstruction of a_n from local data (n <= 200);
       - detector runs (core.reconstruct.detect) on the all-ones coefficient
         sequence at p-level with purity weight (p, 0) for p in {2,3,5,7};
       - exact self-duality: op_dual_satake([1,-1], 1) == [1,-1];
       - exact local purity of weight 0: inverse root a = 1, a^2 == p^0;
       - exact tensor compatibility: zeta (x) zeta and zeta (x) chi_4 at p=3
         (the twist by the nontrivial character mod 4 gives L(s, chi_4)
         locally: coefficient sequence (-1)^k at p = 3).
  3. the world record: ladder cells L0..L9, mechanism cells, critical_line.
     Global analytic facts (continuation, functional equation, explicit
     formula) are IMPORTED_THEOREM with honest citations; nothing global is
     claimed as proved here.  L9: the explicit formula IS a theorem, but the
     positivity of the Weil functional is EQUIVALENT to RH, so the cell is
     CONJECTURAL with a split note.  critical_line: CONJECTURE (RH).
     rh_established = false everywhere.

No floats appear anywhere in this file.
"""

from fractions import Fraction

from core.exact import (
    F,
    coefficient_sequence_from_satake,
    power_sums_from_satake,
    op_dual_satake,
    op_tensor,
    satake_poly_from_power_sums,
)
from core.reconstruct import detect, tensor_compatibility
from core.worlds import cell, validate_world, save_world

# Satake polynomial of zeta at every prime p: det(1 - A T) with A = [1].
# Careful: with A = [1] this is 1 - T, i.e. [1, -1] low-first — NOT [1, 1].
SATAKE = [Fraction(1), Fraction(-1)]

PRIMES = [2, 3, 5, 7]          # detector primes (fixed, deterministic)
WINDOW = 12                    # detector window length (a_0 .. a_{p^11})
NCHECK = 200                   # Euler local-global check range


def factorize(n):
    """Exact integer factorization by trial division (n <= NCHECK)."""
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def build_local_witnesses():
    """All exact local computations; returns a dict of witness strings.
    Every claim is asserted before being embedded."""
    W = {}

    # --- (a) coefficient sequence of 1/(1 - T) is all ones (exact) --------
    coeffs = coefficient_sequence_from_satake(SATAKE, 16)
    assert coeffs == [Fraction(1)] * 16
    W["coeffs"] = ("coefficient_sequence_from_satake([1,-1],16) == [1]*16 "
                   "(exact Fractions): a_{p^k} = 1 for all k")

    # --- (b) power sums (traces of Frobenius powers) are all ones ---------
    psums = power_sums_from_satake(SATAKE, 16)
    assert psums == [Fraction(1)] * 16
    W["psums"] = ("power_sums_from_satake([1,-1],16) == [1]*16: "
                  "tr(A^k) = 1 for A = [1]")

    # --- (c) total multiplicativity of a_n = 1 ----------------------------
    # Complete proof: a_n is identically 1, so a_{mn} = 1 = 1*1 = a_m a_n
    # for ALL m, n — this is a one-line proof, not merely a finite check.
    # We still verify a finite window exactly as an executable witness.
    a = {n: Fraction(1) for n in range(1, NCHECK * NCHECK + 1)}
    for m in range(1, 61):
        for n in range(1, 61):
            assert a[m * n] == a[m] * a[n]
    W["mult"] = ("a_n == 1 identically, hence a_{mn} = a_m a_n for all m,n "
                 "(trivial complete proof); exact check for all m,n <= 60")

    # --- (d) Euler local-global reconstruction ----------------------------
    # a_n must equal prod over p^v || n of a_{p^v}; verified exactly n<=200.
    local = coefficient_sequence_from_satake(SATAKE, 9)  # a_{p^0..p^8}
    for n in range(1, NCHECK + 1):
        prod = Fraction(1)
        for p, v in factorize(n).items():
            prod *= local[v]
        assert prod == Fraction(1) == a[n]
    W["euler_local"] = (f"a_n = prod_p a_(p^v_p(n)) verified exactly for all "
                        f"n <= {NCHECK} from the degree-1 local data [1,-1]")

    # --- (e) self-duality of the Satake data ------------------------------
    dual = op_dual_satake(SATAKE, Fraction(1))
    assert dual == SATAKE
    W["dual"] = ("op_dual_satake([1,-1], det=1) == [1,-1]: local data is "
                 "exactly self-dual at every p (trivial character)")

    # --- (f) exact local purity of weight 0 at each detector prime --------
    # inverse root a = 1 satisfies a^2 == p^0 == 1 exactly.
    for p in PRIMES:
        aroot = -SATAKE[1]
        assert aroot * aroot == Fraction(p) ** 0 == Fraction(1)
    W["purity_local"] = ("inverse root a = 1 satisfies a^2 == p^0 exactly at "
                         "p in {2,3,5,7}: local data pure of weight 0 "
                         "(unitary normalization) — trivially, at EVERY p")

    return W


def run_detector():
    """core.reconstruct.detect on the all-ones coefficient sequence at
    p-level with purity weight (p, 0), for each detector prime.  The verdict
    dicts are embedded verbatim in the world record."""
    runs = []
    series = [Fraction(1)] * WINDOW           # a_{p^0} .. a_{p^{WINDOW-1}}
    for p in PRIMES:
        v = detect(series, mode="coefficients", weight=(p, 0), holdout=4)
        d = v.as_dict()
        # the detector must fully accept: no refusal, all five axioms pass
        assert d["refusal"] is None, (p, d)
        got = {c["axiom"]: c["status"] for c in d["cells"]}
        assert got == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                       "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                       "A5_HELD_OUT": "HOLDS"}, (p, got)
        # reconstructed object must be exactly P=1, Q=1-T of degree 1
        assert d["object"]["degree"] == 1
        assert d["object"]["numerator"] == "[1]"
        assert d["object"]["denominator"] == "[1, -1]"
        runs.append({"prime": p, "weight": [p, 0], "mode": "coefficients",
                     "series": "all-ones a_{p^k}=1, window " + str(WINDOW),
                     "verdict": d})
    return runs


def run_tensor_checks():
    """Exact A6 tensor compatibility witnesses.

    (1) zeta (x) zeta at any p: [1,-1] (x) [1,-1] must predict the all-ones
        sequence (the trivial character squared is trivial).
    (2) zeta (x) chi_4 at p = 3: chi_4(3) = -1, so the twist's Satake data
        is det(1 - (-1)T) = 1 + T = [1, 1] and the product world is
        L(s, chi_4) locally at 3, with coefficients a_{3^k} = (-1)^k.
    """
    out = []

    ones = [Fraction(1)] * 8
    t1 = tensor_compatibility(SATAKE, SATAKE, ones)
    assert t1["status"] == "HOLDS", t1
    out.append({"name": "zeta_tensor_zeta_local",
                "detail": "[1,-1] (x) [1,-1] predicts all-ones sequence",
                "result": t1})

    chi4_sat = [Fraction(1), Fraction(1)]     # 1 + T at p = 3 (chi_4(3) = -1)
    twisted = [Fraction(-1) ** k for k in range(8)]
    t2 = tensor_compatibility(SATAKE, chi4_sat, twisted)
    assert t2["status"] == "HOLDS", t2
    out.append({"name": "zeta_tensor_chi4_at_p3",
                "detail": ("twist by nontrivial character mod 4 at p=3: "
                           "[1,-1] (x) [1,1] predicts a_{3^k} = (-1)^k, "
                           "the local data of L(s, chi_4)"),
                "result": t2})

    # cross-check the predicted tensor Satake polynomial directly
    pa = power_sums_from_satake(SATAKE, 4)
    pb = power_sums_from_satake(chi4_sat, 4)
    pt = op_tensor(pa, pb, 1)
    satT = satake_poly_from_power_sums(pt, 1)
    assert satT == chi4_sat
    out.append({"name": "tensor_satake_crosscheck",
                "detail": "op_tensor power sums give Satake [1, 1] == chi_4 "
                          "local factor at 3 (exact)",
                "result": {"status": "HOLDS", "rigor": "EXACT_RATIONAL",
                           "witness": "satake_poly_from_power_sums == [1, 1]"}})
    return out


def build_world(W, detector_runs, tensor_checks):
    riemann1859 = ("B. Riemann (1859), 'Ueber die Anzahl der Primzahlen "
                   "unter einer gegebenen Groesse'")

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=W["coeffs"],
            citation=("Dirichlet series sum n^{-s} converges absolutely for "
                      "Re s > 1; Euler (1737); " + riemann1859)),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=W["mult"],
            citation=("total multiplicativity of a_n == 1 is immediate; "
                      "unique factorization: Euclid; Gauss (1801)")),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=W["euler_local"],
            citation=("L. Euler (1737): zeta(s) = prod_p (1 - p^{-s})^{-1} "
                      "for Re s > 1")),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("every local factor has degree exactly 1: detector "
                     "reconstructs P/Q = 1/(1 - T) (Berlekamp-Massey "
                     "certified on 12 terms, held-out tail predicted "
                     "exactly) at p = 2, 3, 5, 7; the same [1,-1] datum "
                     "defines the local factor at every p by construction"),
            citation=""),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=(W["dual"] + "; " + W["purity_local"] +
                     "; consistent with the self-dual functional equation "
                     "s <-> 1-s of weight-0 (Tate motive Q(0)) type"),
            citation=riemann1859),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("conductor N = 1, gamma factor pi^{-s/2} Gamma(s/2), "
                     "root number +1: xi(s) = pi^{-s/2} Gamma(s/2) zeta(s) "
                     "satisfies xi(s) = xi(1-s)"),
            citation=riemann1859),
        "L6_CONTINUATION_FE": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("zeta continues meromorphically to C with a single "
                     "simple pole at s = 1 (residue 1) and functional "
                     "equation xi(s) = xi(1-s); Hadamard product for xi"),
            citation=(riemann1859 + "; J. Hadamard (1893), product "
                      "factorization of xi")),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("exact local tensor checks embedded in "
                     "tensor_checks: zeta (x) zeta -> zeta locally, and "
                     "zeta (x) chi_4 -> L(s, chi_4) locally at p = 3; "
                     "globally, twisting zeta by any Dirichlet character "
                     "chi gives L(s, chi), which has its own continuation "
                     "and functional equation"),
            citation=("P. G. L. Dirichlet (1837), L-functions of "
                      "characters; functional equation of L(s,chi): "
                      "Hurwitz (1882) / standard")),
        "L8_REALIZATION": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("automorphic: zeta is the standard L-function of the "
                     "trivial Hecke character on GL(1)/Q, with continuation "
                     "and FE from adelic Poisson summation (Tate's thesis); "
                     "motivic: L-function of the Tate motive Q(0) = "
                     "H^0(Spec Q); classical: Mellin transform of the theta "
                     "function (Riemann's second proof)"),
            citation=("J. Tate (1950), doctoral thesis, Fourier analysis "
                      "in number fields (published in Cassels-Froehlich "
                      "1967); " + riemann1859)),
        # L9: SPLIT with care. The explicit formula relating zeros to prime
        # powers IS a theorem (Riemann 1859, proved by von Mangoldt 1895;
        # distributional form Guinand 1948, Weil 1952).  But the POSITIVITY
        # of the Weil functional on the relevant test-function class is
        # EQUIVALENT to RH (Weil's criterion) — it is not an independent
        # mechanism.  So the cell is CONJECTURAL, not HOLDS.
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "CONJECTURAL", "OPEN",
            witness=("SPLIT: (i) the explicit formula itself is a THEOREM — "
                     "sum over zeros of h(rho) = arch. terms - sum_p "
                     "log p * (g(log p^k) + g(-log p^k))/p^{k/2} as a "
                     "distribution identity; (ii) the POSITIVITY of the "
                     "Weil functional W(g*g~) >= 0 on the relevant class "
                     "is EQUIVALENT to RH (Weil's criterion) and is OPEN; "
                     "no independent positivity input (no analogue of "
                     "Frobenius weights / Castelnuovo positivity) is known "
                     "for zeta"),
            citation=("explicit formula: Riemann (1859), proved by H. von "
                      "Mangoldt (1895); distributional form: A. P. Guinand "
                      "(1948), A. Weil (1952); positivity criterion "
                      "equivalent to RH: A. Weil (1952)")),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("supplied by unique factorization in Z; local factors "
                     "degree 1; " + W["euler_local"]),
            citation="L. Euler (1737)"),
        "DUALITY_FE": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("supplied by theta inversion / Poisson summation; "
                     "self-dual: " + W["dual"]),
            citation=riemann1859),
        "TRACE_FORMULA": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("the Riemann-von Mangoldt / Guinand-Weil explicit "
                     "formula is an unconditional distribution identity "
                     "pairing zeros against prime powers — a genuine "
                     "'trace formula' shape; what it is the trace OF (a "
                     "self-adjoint operator) is not known — see "
                     "POSITIVITY_PURITY"),
            citation=("Riemann (1859); von Mangoldt (1895); Guinand "
                      "(1948); Weil (1952)")),
        "POSITIVITY_PURITY": cell(
            "OPEN", "OPEN",
            witness=("local purity of weight 0 holds trivially and exactly "
                     "(" + W["purity_local"] + "), but this is vacuous for "
                     "the global question; no independently defined "
                     "positivity mechanism known — this is precisely the "
                     "missing structure (#763). In the function-field "
                     "analogue this slot is filled by Frobenius weights "
                     "via the Castelnuovo/Hodge-index positivity (Weil "
                     "1948, Deligne 1974); no analogue over Q is known"),
            citation=("function-field contrast: A. Weil (1948), P. Deligne "
                      "(1974)")),
        "TENSOR_OPS": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("degree-1 objects: tensor operations are trivially "
                     "closed; exact checks zeta (x) zeta and zeta (x) "
                     "chi_4 at p = 3 embedded in tensor_checks (A6 HOLDS "
                     "in both); twists land in the Dirichlet L family"),
            citation="P. G. L. Dirichlet (1837)"),
        "FAMILY": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("zeta is the q = 1 member of the family of Dirichlet "
                     "L-functions {L(s, chi)}, each with Euler product, "
                     "continuation and functional equation; it is also the "
                     "Dedekind zeta of Q inside {zeta_K}"),
            citation=("P. G. L. Dirichlet (1837); functional equations: "
                      "Hurwitz (1882), Hecke (1917) for zeta_K")),
    }

    critical_line = {
        "status": "CONJECTURE",
        "detail": ("Riemann Hypothesis: every nontrivial zero of zeta has "
                   "Re s = 1/2. Open since 1859. Unconditional partial "
                   "results: infinitely many zeros on the line (Hardy "
                   "1914); a positive proportion (Selberg 1942); more than "
                   "two fifths (Conrey 1989); zero-free region Re s >= 1 - "
                   "c/log|t| (de la Vallee Poussin 1896). Numerical "
                   "verification of initial zeros exists but is not "
                   "evidence used here."),
        "rigor": "OPEN",
        "citation": ("Riemann (1859); Hardy (1914); Selberg (1942); Conrey "
                     "(1989); de la Vallee Poussin (1896)"),
        "witness": "",
    }

    world = {
        "id": "zeta",
        "title": "Riemann zeta function",
        "definition": ("zeta(s) = sum_{n>=1} n^{-s} = prod_p (1 - "
                       "p^{-s})^{-1} for Re s > 1, continued "
                       "meromorphically to C. Local Satake datum at every "
                       "prime p: A = [1], det(1 - A T) = 1 - T = [1, -1] "
                       "(low-first), so a_{p^k} = 1 and a_n = 1 for all n."),
        "arithmetic_class": "degree-1 primitive L-function over Q (GL(1), "
                            "trivial character); Tate motive Q(0)",
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "Riemann (1859), Ueber die Anzahl der Primzahlen unter einer "
            "gegebenen Groesse",
            "E. C. Titchmarsh, The Theory of the Riemann Zeta-function "
            "(2nd ed., rev. D. R. Heath-Brown, 1986)",
            "H. Davenport, Multiplicative Number Theory",
            "A. Weil (1952), explicit formula and positivity criterion",
            "J. Tate (1950), thesis (in Cassels-Froehlich 1967)",
            "H. Iwaniec, E. Kowalski (2004), Analytic Number Theory "
            "(explicit formula, ch. 5)",
        ],
        "rh_established": False,
        "notes": ("The single degree of structural freedom this world is "
                  "missing is the POSITIVITY_PURITY mechanism: every other "
                  "row of the matrix is filled by a classical theorem, and "
                  "L9 fails to close only because Weil positivity is "
                  "RH-equivalent rather than independently supplied. All "
                  "exact witnesses in this record are Fraction "
                  "computations; no floats were used anywhere in the "
                  "build. rh_established=false."),
        "detector_runs": {
            "description": ("core.reconstruct.detect on the all-ones "
                            "coefficient sequence (window 12, holdout 4) "
                            "with purity weight (p, 0), p in {2,3,5,7}; "
                            "plus exact tensor checks"),
            "runs": detector_runs,
            "tensor_checks": tensor_checks,
        },
    }
    return world


def main():
    W = build_local_witnesses()
    detector_runs = run_detector()
    tensor_checks = run_tensor_checks()
    world = build_world(W, detector_runs, tensor_checks)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector refusals:",
          [r["verdict"]["refusal"] for r in detector_runs])


if __name__ == "__main__":
    main()
