# Independent audit: Hardy translation and physical-inner band bounds

Status: exact-source review passed; no mathematical or machine repair needed.
This accepts the stated finite-degree theorem, not the native Xi free-energy
or reverse-Rolle gates.

Reviewed source: a07e9c3ba093abb348b849e0356f6babdf591e84.
Programme copy: bedb31c6235635b010db3de0f3f0b546c4a12290.
Review date: 2026-08-30.

The root read the complete note, producer, tests and source manifest, rebuilt
the mathematical argument, and reran the bounded source-authenticated checks.
A separate exact-SHA reviewer independently checked the same frozen packet;
a further reviewer supplied independent complex/collision controls.

## Frozen identities

The [proof note](HARDY_TRANSLATION_PHYSICAL_BAND_BOUND.md) has Git blob
95338634d08fb5bde4d56d10197833b44ec64788.
The producer, fixture, manifest and tests have blobs, respectively:

- 3e8dcb2ea93cfdf7421fef2e6e33fcd20774dc2a;
- 532118ecc1a4fbd4f6ac732cdf121a505c31f1f1;
- b6fcefacca9e6577167bb246b6682dc904a831a0;
- 40dd0e2c66c34eb3a0057f27dad784d00e32b654.

The five programme files are unchanged from this reviewed source. All
thirteen declared repository source/review bindings authenticate by frozen
commit, Git blob and LF hash. The earlier coarse confluent proof and its
review remain unchanged; this is a separate stronger result.

## Mathematical review

1. On a finite-dimensional continuous left-translation-invariant subspace
   of L2(0,infinity), left translation is a contraction. The evaluation
   identity therefore makes the evaluation-kernel diagonal decreasing.
   Its integral is the dimension N, giving t K(t,t)<=N. This argument
   allows arbitrary stable complex exponents and all confluent orders.
2. Decreasing averages give the interval trace bound N(B-A)/B, which is
   stronger than N log(B/A). This is a uniform dimension-paid statement,
   not a claim of an optimal numerical constant.
3. The row-basis generator has the stated superdiagonal convention.
   Integration of (w* w)' gives A*G+GA=-c*c; multiplication by the inverse
   Gram gives the negative-square kernel derivative. Complex conjugations,
   the origin identity K(0,0)=2 sum q_j Re z_j, and total integral N agree.
4. The orthogonal product-model decomposition places the physical image
   B_plus K_Bminus inside K_(Bplus Bminus). The latter has total dimension
   d=m+n. Kernel domination and positivity give HT8--HT9; the physical
   image itself need not be translation invariant.
5. The literal jets C=J_O and V=J_Bplus commute in the jet algebra, not
   with the Gram or frequency projection. With J_R=VC and G_O=C*GC,
   cyclicity gives HT10. Applying the Loewner bound before taking the
   positive trace gives HT11 with no source-vector freedom or loss of O.
6. The frozen actual-Xi accepted-set enclosure is uniform over the full
   accepted set. Its relative width is (KM/pi+o(1)) exp(-X)/X^2, so the
   degree hypothesis d=o(X^2 exp(X)) implies the stated vanishing mass
   and relative source-band energy. No monotonicity of rho or connectedness
   of the accepted set is required.

The primary product-model formulas were checked directly in
[Fricain--Hartmann--Ross, equations (2.12), (2.18)--(2.19)](https://arxiv.org/pdf/1605.07418v2).
The attribution to the classical dimension/evaluation/translation mechanism
is appropriately limited; the related
[Borwein--Erdelyi paper](https://people.tamu.edu/~terdelyi/papers-online/shift_sub.pdf)
does not get credited with an unverified exact half-line constant.

The fixed-height rank-one delay counterexample has the correct Fourier sign.
For each fixed T, the finite Blaschke products converge on the boundary to
exp(iTx). Dominated convergence and Plancherel give the delayed exponential
in L2. Its fixed positive mass in [T,T+L], followed by T tending to infinity,
rules out a bound using denominator rank alone. The order is fixed L, then
T, then sufficiently large finite m. It is not an actual-Xi configuration
or a quantitative converse to the sufficient degree hypothesis.

## Code and reproduction

The root reran 33 tests normally and 33 with Python -O; both full producers,
Ruff lint and format checks passed. The programme-copy producer also passed.
The separate frozen reviewer independently reported the same results and
whitespace checks. The author additionally reported a clean fresh detached
CRLF checkout with both producer modes and all 33 tests in both modes.

The producer's five predeclared physical cases contain ten inclusion columns.
Exact partial fractions are checked against the full cross-multiplied
polynomial identity, not point samples; the independent Gram isometry is
checked separately. Near collisions, complex phases, confluence, zero
numerator degree and a maximum-degree held-out case are exercised.

The further reviewer independently reconstructed four additional complex/
collision configurations, nine inclusion columns in total, at degree at most
six, using pole-residue formulas and SymPy. It also checked both Lyapunov
identities and the delay control. These were separate memory-only review
controls, not additions to the frozen fixture.

The complex covariance example has exact trace 41/8. Its commuting C,V do
not commute with G or H; dropping the outer metric changes the trace.
These are synthetic analytic jets and an abstract positive weight, not
asserted realizable samples of an inner function or the actual Xi source.

## Acceptance boundary

Accept HT1--HT13 under their explicit finite-Blaschke and degree hypotheses.
In that scope the physical band Gram left open by the coarse packet is now
controlled. The older q-squared estimate is strengthened to q in the single
unweighted cluster and to total degree in the physical finite-inner case.

The full native numerator need not be finite inner. An infinite model space
has no finite-dimension bound; approximation error and a compatible cofinal
degree ledger are still needed. The height-sum ledger does not count very
shallow zeros. No actual companion degree bound, X-to-log-T conversion, or
total Pick/free-energy estimate has been inferred. The forced topological
factor remains. This result supplies neither curvature descent nor a new
critical-line proportion, RH, GRH, or novelty claim.
