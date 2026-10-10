# Independent review of the exact covariance diagnostic

**Verdict:** passes at its stated finite-diagnostic scope. I inspected the
complete checker, independently ran it in isolated normal and optimized
Python processes, and compared both regenerated reports with the saved
report. No correction to the checker is requested. This is a review of
finite identities and exponent calculations, not a certification of an
infinite arithmetic moment or of its imported analytic inputs.

## 1. Exact files reviewed

All paths below are relative to this packet. The review binds the following
bytes; a later change to a listed file requires a new comparison.

| File | SHA256 |
| --- | --- |
| checks/check_covariance_arithmetic.py | 0e6b41e2465a11eda7b23bbb405b163fec453b59ff76cb115765a7506859d16c |
| results/exact_covariance_checks.json | 6e998509315385702f789341c86de5b9c93a561f304e3e926baba2fb7a3b23d4 |
| JOINT_DIVISOR_MEAN.md | 7b42abe2c3c62acfd934b663405821748eac54bb440f1d1071671961a9e97035 |
| MOVING_AUXILIARY_ADAPTER.md | e91e0f7b3c3d885587fc9197539beaf1caa8e0c80ed9c8bba5c15340090b5eda |
| OPTIMIZED_A2_TRANSFER.md | d5a87c27959b64e62df7dd3aa2fdd33cc8b42af6e5a64e9bfb20d6b74af0277a |
| SIGNED_CONDUCTOR_PROGRESS.md | d973468a0e0a893f43327e6f3a4ac706076952ec44a2a3114423ea515bdc4e4a |

The proof files were used to check what the diagnostic formulas represent.
The checker does not read them or automatically authenticate their contents.
Its self hash binds the executing checker source only.

## 2. Independent replay

From the repository root I ran, with Python 3.12.14:

~~~sh
python -I standalone/2026-10-10-joint-divisor-covariance/checks/check_covariance_arithmetic.py --output /tmp/joint_divisor_review_normal.json
python -I -O standalone/2026-10-10-joint-divisor-covariance/checks/check_covariance_arithmetic.py --output /tmp/joint_divisor_review_optimized.json
~~~

Both processes exited with status zero. Both reports contain
"status": "passed" and exactly **22,743 successful predicates, including
the nine negative controls**. Direct byte comparison showed that the two
new reports and the saved report are identical: 2,587 bytes, with report
SHA256 6e998509315385702f789341c86de5b9c93a561f304e3e926baba2fb7a3b23d4.
The reported checker hash also agrees with a separate hash of its source.

The checker uses explicit require calls that raise RuntimeError on
failure. It contains no Python assert statements, so optimization does
not delete the predicates. It reads no saved report, imports only standard
library modules, and constructs the output after running all six checking
functions. The independent outputs were written outside the repository;
the author report and checker were not modified during this review.

The count measures executions of predicates, not independent theorems.
Many executions share the same identity or convergence inequality.

## 3. Exact ring and nonunit masks

The pair representation implements
$\mathbb Z[\omega]$, with $\omega^2+\omega+1=0$:

\[
(a+b\omega)(c+d\omega)
=(ac-bd)+(ad+bc-bd)\omega.
\]

Addition and multiplication use integers. The six powers of $1+\omega$
are checked to be distinct, and its sixth power is checked to be one.
The unit projection is then tested for all six residue exponents. There
are no floating point comparisons in this ring calculation or in the
subsequent rational calculations.

The mixed-row test covers every choice of three values from zero and the
six roots of unity, twelve physical exponents $\nu=0,\ldots,11$, and
both binary principal and auxiliary flags. Thus its 16,464 predicates are
exactly $12\cdot2\cdot2\cdot7^3$ cases. They compare the physical exponent
$\nu+6q+4f$ with its factored version. In particular:

- the principal insertion supplies the masks of all three values;
- the fourth-power auxiliary insertion supplies the twelfth-power cube
  mask, in addition to the two fourth powers;
- positive multiples of six remain zero at a zero character value.

The explicit convention power(x, 0) = ONE means that the physical prime
factor is absent. It is not used to erase a mask attached to a positive
physical exponent whose residue class is zero. The two zero-power negative
controls catch the corresponding proposed erasures.

This is an exhaustive finite test over the character-value possibilities
used in the stated identity. It does not evaluate residue symbols in
primitive finite fields, prove global reciprocity, or replay the local
Gauss-sum scalar. The identification of these values with the physical
moving-row coefficients remains a written arithmetic adapter.

## 4. Divisor correction and cutoff calculations

The correction identity is checked symbolically in the polynomial ring
$\mathbb Q[A,z,e]/(e^2-1)$ after multiplying out the denominators:

\[
\frac{1-Ae}{1-ze}
=1+\frac{(z-A)(z+e)}{1-z^2}.
\]

The checker also rejects the wrong sign $z+A$ and checks eighteen exact
rational specializations with $e=\pm1$. The relation $e^2=1$ is appropriate
only on the retained unit support. The checker does not extend it to
zero-valued characters or prove the analytic nonvanishing of denominators.

For the $A_2$ transfer, correction_powers derives the norm denominator
exponents from the child scalings of $X,\ell,m,U$, the five parent energy
monomials, the square root passing from energy to norm, and the outer
coefficient weight. It does not merely print the expected table. At
$U_{\rm child}=U/(CJ)^{1/2}$ the computed table agrees with
OPTIMIZED_A2_TRANSFER.md:

| Parent energy term | $C$ | $J$ | $E$ |
| --- | ---: | ---: | ---: |
| $HX$ | $7/4$ | $7/4$ | $5/2$ |
| $\ell H^2X^{5/12}U^{7/4}$ | $5/4$ | $5/4$ | $17/12$ |
| $mH^{4/3}X^{2/3}U^2$ | $11/6$ | $11/6$ | $11/6$ |
| $H^{1/6}X^2U^{-3}$ | $7/4$ | $7/4$ | $7/2$ |
| $H^{2/3}X^{4/3}U^{-2}$ | $3/2$ | $3/2$ | $17/6$ |

All fifteen exponents are strictly greater than one. Four interior cutoff
parameters are also tested; the parameters $0,3/14,1$ fail strict
summability as intended. The common-cutoff obstruction $13/16$ is derived
from the same scaling function. The entire open parameter interval
$3/14<\eta<1$ is established by the affine inequalities in the written
proof, not by those four samples.

The three Cartan-vector checks correctly distinguish the kernel vectors
$(1,2),(2,1)$ from $(2,2)$ modulo three. They are finite algebra checks;
they do not construct a global Weyl-group multiple Dirichlet series.

For the optimized balanced blocks, all five substituted exponents are
affine functions of $h$ on each of the two specified intervals. The
checker verifies their dominance and the two equal active terms at both
endpoints. Endpoint verification therefore controls each entire affine
interval. It also verifies the junction, the range endpoint $114/151$,
and the values

\[
r(1/2)=8/57,\qquad E(1/2)=379/228,\qquad
25/12-379/228=8/19.
\]

These checks validate the displayed choice of cutoff and its resulting
upper envelope. The all-row large sieve, the exact short and long cube
decomposition, validity for child cutoffs below one, and the permitted
smooth tests are not established by this calculation.

The joint-divisor tail test substitutes
$b=(3-a)/2+\eta$ into all four displayed powers, at seven rational values
of $a$ and $\eta=1/20$. It checks the comparison at $F=Q^{2/3}$ together
with the nonpositive remaining power of $F$. The proof supplies the
general interval and the infinite geometric summation. The explicit
exclusion of $a=5/6$ is a boundary diagnostic; it does not independently
prove a failure of an analytic estimate at that endpoint.

## 5. Incidence, actual divisors, and sector fixtures

For $k=1,\ldots,6$, the checker enumerates all nonempty binary prime
incidence patterns among $2k$ positions. It correctly uses the difference
of the two side multiplicities modulo six. Singletons are nonprincipal;
doubles are nonprincipal exactly when they occur on one side. The
inequality $m/2-103/512>1$ is checked for every higher-multiplicity
pattern. The formula $103/512$ is computed from the stated $7/64$ input.
The general fixed-order incidence argument and that external analytic
input are not proved by this enumeration.

The greedy-divisor check uses all 325 ordered selections without
repetition from the norm list $7,13,19,31,37$. The selected integer is an
actual product of entries from its input list. Integer inequalities check
both divisibility and

\[
d^3P^2\ge F,\qquad d^3\le FP.
\]

Thus the test checks the divisor selection rather than replacing it by an
arbitrary real number. This is a finite collection of integer norm
fixtures, not an enumeration of prime ideals or a proof that every
conductor has a divisor of size $F^{1/3}$. The general greedy argument
and its weaker $P(f)$-dependent bounds are in the written proof.

The two signed-sector fixtures agree with Section 5 of
SIGNED_CONDUCTOR_PROGRESS.md. They reconstruct each original factor's
unit scale, singleton and same-side double scales, the two small-gcd
inequalities, and the normalized gains:

| Fixture | Old excess | New excess | Small-gcd margin |
| --- | ---: | ---: | ---: |
| General subconvex branch | $1/400$ | $-869/204800$ | $9/700$ |
| Prime-factor branch | $1/20$ | $-1/120$ | $1/140$ |

The separate prime-factor example's general-subconvex excess $19/512$
and balanced-divisor excess $-1/40$ are also checked. The full conductor
exponent is computed as $l+g$; it is explicitly distinguished from the
complexity $l+g/2$. The stored cross-separation values are calculated from
the fixtures. The checker does not construct the corresponding prime
ideals, show a lower bound for a sector, or evaluate a signed character
sum.

## 6. Proof-source limitations

The diagnostic's own scope and not_verified fields accurately limit
its claim. Neither the successful runs nor this review verify theta
automorphy, all-scale completed mean squares, uniform angular reciprocal
estimates, classical large sieves, Hecke subconvexity, or the passage from
finite norm scalings to infinite analytic families. They do not establish
a full generalized $2k$-moment, a new zero-free half-plane, or the Riemann
Hypothesis. There is no proof-assistant formalization here.

Those analytic dependencies must be assessed in the pinned proof sources
and the separate mathematical reviews. Within the finite algebra,
cutoff arithmetic, and fixture scope actually declared by the checker,
the independent replay and source inspection pass.
