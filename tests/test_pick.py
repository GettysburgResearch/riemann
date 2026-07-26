"""
Adversarial tests for the Nevanlinna-Pick criterion (T-0005).

Runnable with pytest or directly:  python3 tests/test_pick.py

The tests that matter here are the NEGATIVE controls.  A detector that reports
NOT_PSD for an off-line zero is worthless unless it stays PD for every
configuration that is genuinely Herglotz -- otherwise it is measuring zero
count, or degeneracy, and not off-line-ness.  So for each planted off-line pair
there are three matched controls with the same zeros at the same height:

    LEHMER  the pair split vertically   (on-line, exactly Herglotz)
    DOUBLE  a double zero               (on-line, exactly Herglotz)
    SINGLE  one simple zero             (on-line, exactly Herglotz)

`test_float_ldl_manufactures_a_false_negative_pivot` is the R-0009 regression:
at 53 bits the near-singular Pick matrix produced a spurious negative pivot, and
an entire (wrong) detection table was built on it before ball arithmetic
exposed it.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

from flint import acb, arb, ctx  # noqa: E402

import certzeta as cz  # noqa: E402
import li  # noqa: E402
import pick as PK  # noqa: E402

HALF = arb(1) / 2
G = 100.0


def model(delta, mode, gam=G, spacing="0.9", m=90):
    """xi'/xi for a finite symmetric zero set.  A truncated sum of on-line
    1/(s-rho) is still exactly Herglotz, so the controls remain valid."""
    zs, d, g0 = [], arb(delta), arb(repr(gam))
    for k in range(-m, m + 1):
        g = g0 + k * arb(spacing)
        if k == 0:
            loc = {"OFF": [acb(HALF - d, g), acb(HALF + d, g)],
                   "LEHMER": [acb(HALF, g - d), acb(HALF, g + d)],
                   "DOUBLE": [acb(HALF, g), acb(HALF, g)],
                   "SINGLE": [acb(HALF, g)]}[mode]
            zs += loc + [z.conjugate() for z in loc]
        else:
            zs += [acb(HALF, g), acb(HALF, -g)]

    def F(s):
        return sum(1 / (acb(s) - r) for r in zs)
    return F


def probes(D, N, gam=G):
    return PK.probe_cluster(gam + D, gam + 2 * D, N)


def test_off_line_pair_is_detected_from_a_distance():
    """The claim of T-0005: probes held 0.8 away see delta = 1e-6."""
    ctx.prec = 3000
    for delta in ("0.01", "0.0001", "0.000001"):
        c = PK.pick_certificate(probes(0.8, 16), F=model(delta, "OFF"))
        assert c["verdict"] == "NOT_PSD", (delta, c["verdict"], c["min_pivot"])


def test_herglotz_controls_never_fire():
    """The test that makes the previous one mean something."""
    ctx.prec = 3000
    for delta in ("0.01", "0.0001", "0.000001"):
        for mode in ("LEHMER", "DOUBLE", "SINGLE"):
            for D in (0.05, 0.8):
                c = PK.pick_certificate(probes(D, 16), F=model(delta, mode))
                assert c["verdict"] == "PD", (delta, mode, D, c["verdict"],
                                              c["min_pivot"])


def test_pick_matrix_of_k_on_line_poles_has_rank_k():
    """Structure, and the explanation of the floor law.

    For a single on-line pole, writing a' = alpha - 1/2 and rho = 1/2 + i gamma,

        F(a) + conj(F(b))  =  (a' + conj(b')) / ((a' - i gamma)(conj(b') + i gamma))

    so dividing by (a' + conj(b')) leaves P_jk = v_j conj(v_k) with
    v_j = 1/(a_j' - i gamma):  the Pick matrix is EXACTLY rank one.  A sum of k
    on-line poles gives rank <= k.

    So with more probes than nearby zeros the matrix is PSD but SINGULAR, and an
    honest interval LDL must abstain rather than claim PD.  That is also why the
    baseline floor in T-0005 decays geometrically in N: the extra pivots are the
    numerical rank tail, not noise."""
    ctx.prec = 2000
    rho = acb(HALF, arb("14.134725"))

    def F(s):
        return 1 / (acb(s) - rho) + 1 / (acb(s) - rho.conjugate())

    # exactly two poles -> two probes see a nonsingular (rank 2) matrix
    c = PK.pick_certificate(PK.probe_cluster(1.0, 2.0, 2), F=F)
    assert c["verdict"] == "PD", (c["verdict"], c["min_pivot"])

    # more probes than poles -> rank deficient, so PD is not available, but
    # NOT_PSD must never be reported, at any geometry
    for al in [PK.probe_cluster(1.0, 2.0, 6),
               PK.probe_cluster(14.0, 14.3, 6),
               PK.probe_cluster(-30.0, 30.0, 6),
               PK.probe_cluster(14.13, 14.14, 4, u="2.0")]:
        c = PK.pick_certificate(al, F=F)
        assert c["verdict"] == "UNDECIDED", (c["verdict"], c["min_pivot"])


def test_one_point_case_matches_the_targeted_li_coefficient():
    """N = 1 is Re F(alpha) >= 0, which T-0004 says is lambda_1^(alpha)/(2u).
    Ties T-0005 to T-0004 through two unrelated code paths."""
    cz.set_prec(1200)
    for u, v in [("0.5", "0"), ("0.05", "100.0")]:
        al = acb(arb("0.5") + arb(u), arb(v))
        F = PK.xi_logderiv(al, tol_bits=300)
        lam1 = li.li_general(al, 1, tol_bits=300)[0].real
        assert lam1.overlaps(2 * arb(u) * F.real), (u, v, str(lam1), str(F.real))
        P = PK.pick_matrix([al], tol_bits=300)
        assert P[0][0].real.overlaps(F.real / arb(u)), (u, v)


def test_real_zeta_pick_matrices_are_positive_definite():
    """The certified statement of X-0011 part 3.  A failure here is either a
    bug or a counterexample to RH -- see the verification protocol before
    claiming the latter."""
    cz.set_prec(1500)
    for v0 in (100.0, 1977.0):
        c = PK.pick_certificate(probes(0.8, 12, gam=v0), tol_bits=300)
        assert c["verdict"] == "PD", (v0, c["verdict"], c["min_pivot"])
        assert c["min_pivot_rad"] < abs(c["min_pivot"]), (v0, "no margin")


def test_float_ldl_manufactures_a_false_negative_pivot():
    """R-0009 regression.

    At 53 bits the N = 8, D = 1.0 Pick matrix of an ON-LINE configuration has a
    pivot of about 3e-4 with an uncertainty of about 7e-6.  Rounding at that
    scale produced a spurious NOT_PSD and an entire wrong detection table.  In
    ball arithmetic the verdict must be PD or UNDECIDED -- never NOT_PSD."""
    for prec in (53, 80, 3000):
        ctx.prec = prec
        c = PK.pick_certificate(PK.probe_cluster(G + 1.0, G + 2.0, 8),
                                F=model("0.001", "DOUBLE"))
        assert c["verdict"] != "NOT_PSD", (prec, c["verdict"], c["min_pivot"])
    ctx.prec = 3000


def test_rank_one_decomposition_identity():
    """L-0008(i): G(rho) = uu* - 2 beta D_u C D_u*, entrywise, in balls.

    This identity is what makes the T-0005 refutation direction citation-free,
    so it is checked at deliberately asymmetric configurations: probes at
    unequal heights and depths, zeros on and off the line, above and below the
    probe cluster."""
    ctx.prec = 400
    probes = [acb(arb("0.53"), arb("99.1")), acb(arb("0.71"), arb("101.7")),
              acb(arb("0.55"), arb("95.2")), acb(arb("1.40"), arb("103.001"))]
    for rho in (acb(arb("0.5"), arb("100.3")),          # on line
                acb(arb("0.48"), arb("100.3")),         # left of line
                acb(arb("0.507"), arb("97.77")),        # off, right
                acb(arb("0.5"), arb("-61.03"))):        # conjugate side
        def F(s, rho=rho):
            return 1 / (acb(s) - rho)
        G = PK.pick_matrix(probes, F=F)
        u = [1 / (a - rho) for a in probes]
        beta = rho.real - HALF
        n = len(probes)
        for j in range(n):
            for k in range(n):
                Cjk = 1 / ((probes[j] - acb(1) / 2)
                           + (probes[k] - acb(1) / 2).conjugate())
                rhs = (u[j] * u[k].conjugate()
                       - 2 * acb(beta) * u[j] * Cjk * u[k].conjugate())
                assert G[j][k].real.overlaps(rhs.real), (j, k, str(rho))
                assert G[j][k].imag.overlaps(rhs.imag), (j, k, str(rho))


def test_gram_matrix_C_is_PD():
    """L-0008(ii): C_jk = 1/(a_j' + conj(a_k')) is positive definite for
    pairwise distinct probes -- it is the Gram matrix of e^{-a' t} on
    (0, inf)."""
    ctx.prec = 400
    probes = [acb(arb("0.53"), arb("99.1")), acb(arb("0.71"), arb("101.7")),
              acb(arb("0.55"), arb("95.2")), acb(arb("1.40"), arb("103.001"))]
    C = [[1 / ((a - acb(1) / 2) + (b - acb(1) / 2).conjugate())
          for b in probes] for a in probes]
    verdict, _ = PK.ldl_hermitian(C)
    assert verdict == "PD", verdict


def test_witness_extraction_from_a_firing_ldl():
    """X-0015b: when the LDL fires, x = L^{-*} e_k converts the matrix
    verdict into a certified scalar q = x*Px/x*x < 0.  Soundness of the
    scalar does not depend on the extraction (L-0008), but the extraction
    must actually produce a negative q -- two plausible alternatives
    (unshifted and pivot-shifted inverse iteration) do not, and are recorded
    in experiments/X-0015-tuned-detector/extract.py."""
    ctx.prec = 3000
    Fm = model("0.0001", "OFF")
    al = probes(0.8, 16)
    cert = PK.pick_certificate(al, F=Fm)
    assert cert["verdict"] == "NOT_PSD", cert
    P = PK.pick_matrix(al, F=Fm)
    x = PK.ldl_witness_direction(P)
    assert x is not None
    q = PK.tuned_form(al, x, F=Fm)
    assert q < 0, str(q)


def test_witness_extraction_returns_none_when_psd():
    ctx.prec = 3000
    P = PK.pick_matrix(probes(0.8, 8), F=model("0.0001", "DOUBLE"))
    assert PK.ldl_witness_direction(P) is None


def test_tuned_form_nonnegative_on_herglotz_configurations():
    """L-0008: with every zero on the line the Pick matrix is a sum of PSD
    matrices, so the scalar form is >= 0 along EVERY direction -- including
    arbitrary untuned ones."""
    ctx.prec = 2000
    al = probes(0.8, 5)
    v = [acb(arb("0.3"), arb("-1.1")), acb(arb("0.7"), arb("0.2")),
         acb(arb("-0.4"), arb("0.55")), acb(arb("0.9"), arb("0.05")),
         acb(arb("0.1"), arb("0.8"))]
    for mode in ("LEHMER", "DOUBLE", "SINGLE"):
        q = PK.tuned_form(al, v, F=model("0.001", mode))
        assert not (q < 0), (mode, str(q))


def test_ldl_hermitian_detects_a_known_indefinite_matrix():
    """Unit test of the verdict function itself, independent of zeta."""
    ctx.prec = 300
    bad = [[acb(1), acb(2)], [acb(2), acb(1)]]          # eigenvalues 3, -1
    assert PK.ldl_hermitian(bad)[0] == "NOT_PSD"
    good = [[acb(2), acb(1)], [acb(1), acb(2)]]         # eigenvalues 3, 1
    assert PK.ldl_hermitian(good)[0] == "PD"
    herm = [[acb(2), acb(0, 1)], [acb(0, -1), acb(2)]]  # eigenvalues 3, 1
    assert PK.ldl_hermitian(herm)[0] == "PD"
    sing = [[acb(1), acb(1)], [acb(1), acb(1)]]         # eigenvalues 2, 0
    assert PK.ldl_hermitian(sing)[0] == "UNDECIDED"


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS  {name}")
            except Exception as e:
                fails += 1
                print(f"FAIL  {name}: {type(e).__name__}: {e}")
    print("\nall passed" if not fails else f"\n{fails} FAILURES")
    sys.exit(1 if fails else 0)
