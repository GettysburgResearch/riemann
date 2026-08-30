# Exact-source review of the actual Xi-kernel concentration proof

Reviewed scientific source: 3b6972320899a82c6caa3a98e2ada5ff703a605a.

Reviewer: root / codex-two-programmes, independent of the author.

Verdict: PASS for XL1--XL21 with the fixed-order and real-frequency
quantifiers in the source. One separately identified metadata repair below
does not change any analytic formula or scientific control.

The mathematical note at that frozen source has LF-normalized SHA-256
f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246.
The review read the complete note, source manifest, producer, tests, and the
literal L-106500 and L-106710 source formulas. All six source blobs were
authenticated independently by the source checker. No historical claim
file was edited.

## Analytic reconstruction

1. The standard full-line Fourier normalization really requires
   Phi_Xi = 2 phi_0. Differentiating
   f(u) = exp(u/2) psi(exp(2u)) gives
   (D^2 - 1/4) f = exp(u/2) [6x psi'(x) + 4x^2 psi''(x)].
   Thus the historical series is half that differential expression.
   Its Mellin integral is one half of standard xi_R. Theta inversion
   makes the resulting kernel even; the negative-infinity boundary terms
   vanish for Re z > 1 before analytic continuation. The factors two
   and four are amplitude corrections, not frequency rescalings.

2. The theta-series majorant uses n <= 2^(n-1) and
   n^2 - 1 >= 3(n-1), both valid for every n >= 1. The strict bounds
   pi > 3 and e > 2 give 16 exp(-9) < 1/32. The constants 64/31
   and 512/31 therefore follow from a geometric series, and the
   first-orbit asymptotic has an explicitly nonnegative tail.

3. The global product estimate does include the unbalanced region.
   For d >= xi the exact extra exponent is
   9(d-xi)/2 - 2 pi sinh(d-xi), which is nonpositive.
   Hence the common upper bound
   9 exp[-2 pi exp(xi)(cosh(d)-1)] applies on the whole real line,
   not just near the saddle. Reflection handles negative d.

4. On |d| <= exp(-xi/2), xi >= 1, both kernel arguments are
   nonnegative. The lower theta bound and cosh(d)-1 <= d^2
   give the claimed explicit positive denominator bound after
   integrating the leading current term kappa_K xi^(K-1) d^2.
   Its coefficient is 2 exp(-2 pi)/27. In particular, no later
   asymptotic is used to assert positivity of the normalization.

5. After d = (pi exp(xi))^(-1/2) y, the exact kernel ratio tends
   to exp(-y^2). The global majorant with an additional fixed
   polynomial and exp(h|y|) is integrable. Dominated convergence
   therefore proves the moment integrals, including exponential
   weights. The current begins with d^2, so its normalized second
   moment is asymptotic to 3/(2 pi exp(xi)), not the unweighted
   value 1/(2 pi exp(xi)).

6. The half-convolution and change of variables in the source give
   L_K = Z/4 and exactly the two formulas in XL6. Taking the
   unweighted zeroth-to-second moment ratio gives
   g_K ~ pi xi^2 exp(xi)/K. Expanding P_K/Q_K gives the coefficient
   (K^2-1)/(3K); the fourth-moment bound controls the global
   remainder. Thus the correction to p_K, including the K=1 edge,
   agrees with XL9.

7. The mismatch identity is exact. Subtracting p_K before expanding
   gives XL19 and the transition limit
   1/(2K) - 2 pi c/K. Solving the two quadratic inequalities,
   rather than inverting a pointwise asymptotic, proves the tolerance
   endpoints and width. The zero shift 1/(4 pi) is independent of K.
   M=0 is an exact singleton; no positive-width asymptotic is claimed.

8. For 0 < h <= h_0 the hyperbolic-sine remainder is bounded by
   a constant times h^4 d^4 exp(h_0 |d|). Dividing the resulting
   error by h^2 exp(-xi) is uniform on that interval. Inverting
   1+O(h^2 exp(-xi)) preserves this uniformity. There is no
   inserted causal translation factor.

Every K, moment order, and exponential weight is fixed as xi tends to
infinity. The proof does not establish a bound uniform in growing K,
growing moment order, or unbounded h. Those stronger assertions were
not used.

## External formulas checked

The reviewer checked the actual displayed formulas in
[DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4),
[DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), and
[DLMF 20.10.2](https://dlmf.nist.gov/20.10.E2).
Theta inversion is the specialization z=0, tau=i x of 20.7.32.
The Mellin formula in 20.10.2 has Re s > 1, the domain used here.
No external asymptotic theorem or historical complex-ray theorem was
imported.

The historical kernel source is explicitly pinned at
686e23d9e5b1005aae83e3362ac1ed53a28a0352, blob
dfe76fc1985d3366f50489ce21bdcc2cfdd325ff.
It is not asserted to be resident in the PR731 scientific tree.
Only its literal series is used; its stronger historical claims remain
outside this review.

## Reproduction and separately identified metadata repair

At the reviewed frozen source, the root reviewer reproduced all 14 tests
in normal Python and all 14 under -O. The producer check passed in both
modes; Ruff lint and format checks passed.

The producer's arithmetic label was not a canonical repository value.
This audit's repair changes it to EXACT_RATIONAL and adds explicit
arithmetic-domain and rounding-contract fields: pi and exp(-2*pi)
are unevaluated symbolic labels, and no transcendental inequality is
machine-certified. A hostile regression rejects both the old label and
DIRECTED_INTERVAL promotion. The repaired fixture is a complete rebuild;
only metadata and bound code/test hashes change. The mathematical note,
all six primitive source bindings, and every exact scientific constant
remain unchanged.

After the repair, 15 tests pass in normal Python and 15 under -O;
both producer checks and Ruff lint/format checks pass. The bounded
224 weight identities and the 8 odd-order/7 moment panels are regression
controls, not a numerical proof of the analytic limit.

## What this does and does not close

This new proof discharges the real concentration estimate used by the
near-adapted-scale scout at 939a24962a4c6a449c0b56e3b20f78b936f35f6c.
It supersedes that scout's conditional dependence for these specific
real-kernel conclusions. It does not upgrade any unrelated historical
claim or change the earlier scout review retroactively.

The outer-normalized source-Pick metric, its nonlocal phase, collective
and confluent localization, physical constant-scale transfer, and the
required free-energy bound are still open. No critical-line percentage,
density-one, RH, GRH, or novelty conclusion follows from this audit.

The load-bearing analytic checks are the all-real product majorant and
the first-orbit local limit. The bounded rational replay checks algebra
and source identity; it cannot replace those analytic proofs.
