# Exact-head review of the later-result summary and claim ledger

20 October 2026. The checked Git HEAD was
17d7b5b617027cffa4869b47eb898c14eb89e7b9.
This receipt concerns the bytes at that commit, not future additions.

Reviewed summary files:

* ../LATER_RESULTS.md, SHA256
  34328ad4979a2b2416dd05aa5dbd0d5cb11afa7f51d96fccd6a60999f30e2ca2;
* ../CLAIMS.md, SHA256
  439a76ae83b402c78043efd640f5bb9c1f529888e6ebbc3eec19f4cf80d4a52e.

The claims are consistent with the frozen scoped proofs checked here.
No correction to those frozen proofs is requested.
This is a summary-to-proof review; it is not a new independent
certification of every upstream analytic theorem.

The opposite-cubic assertion uses the actual positive cubic conductor,
which is fixed by its local reflection. The stated domain remains
\(0<\delta<2/9\), and angular order zero stays excluded.
At \(\delta=1/6\), I independently recomputed all ratios:
for \(R\le H\), the terms are \(RH,RH,R^{1/2}H\);
for \(R\ge H\), they are
\(RH,R^{2/3}H^{4/3},R^{5/6}H^{2/3}\).
All are at most a fixed multiple of \(RH\) for \(R,H\ge1\).
Thus the all-ratio natural-count mean on \(\Re s=2/3\), and
the consumer \(A^{2/3}RH\) with its stated small losses and angular
factor, follow from the frozen theorem. No selected-prime column
or quadratic/sextic detector identification is made.

The signed common-divisor summary matches
../global/SIGNED_MOBIUS_GCD_TAIL.md, SHA256
803307e8281f1015b403a8532301db64340e1b4521bb7e2405821c9902efdc84.
Its \(s\)-character is finite-order cubic with a fixed finite ray
twist, and the optional norm factor is only a vertical translation.
The inherited common finite-order boundary therefore suffices:
the all-unitary angular extension is not silently needed here.
Its variable punctures are retained, including zeros canceled at
the level of the primitive inducing character.
The full smooth kernel supplies the frequency scale
\(D^2Nd'/(HNC^2)\); multiplying its full frequency count, the two
normalized column counts, the signed \(s\)-bound, and the outer
factor gives \(D^2C^{-2}S^{\beta-2}\).
The summary correctly restricts this to the complete signed
unselected component and leaves the short-divisor sector.

The signed complementary-factor summary uses a different expression,
with nonzero angular degree in two Hecke factors. Its common
actual-family premise, all three contour inequalities, and unsaved
full-divisor term agree with SIGNED_MOBIUS_COMPLEMENT.md.
It does not replace that premise by the finite-order statement
sufficient for the preceding common-divisor estimate.

The sector formula, positivity buffers, and comparison with \(a/4\)
agree with the frozen CONDITIONAL_ANGULAR_SECTORS.md.
Its zero-angular mode is subtracted exactly and its free inner
column is smooth. The separate prime-sector consequence has its
own full-family and Perron inputs; the ledger does not conflate
these two statements.

The quadratic/sextic exponent \(28/11\) is explicitly labeled as
recoverable from the supplied recursive source plus the operator
sieve, so it is not retained as a new best conductor bound.
The pure cubic comparison is restricted to the supplied completed
label interface and generic sieve; it is not an exhaustive
literature-priority assertion.

Finally the numerical zero-free endpoint is expressly unchanged,
all analytic statements remain proposed and source-dependent, and
RH remains unproved. Finite exact replay is described as checking
finite identities rather than certifying the analytic conclusions.
Those distinctions are necessary and present in the checked bytes.
