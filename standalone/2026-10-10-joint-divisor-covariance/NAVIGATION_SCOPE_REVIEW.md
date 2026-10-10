# Independent review of the packet overview and root navigation addition

**Reviewer:** signed_conductor_attack.

**Date:** 2026-10-10.

**Verdict:** approved for mathematical scope and faithful summary at the
content identities below, after the three scope repairs recorded in
Section 5. The overview presents proposed, source-qualified deductions
and explicitly preserves the unresolved signed moment problem.
It does not claim a new full moment, zero-free half-plane, or RH.

**Review boundary:** the complete [packet overview](README.md) and only
the new section headed “Further research: joint divisors and additional
moment sectors” in the [root README](../../README.md).
No inherited root README prose is reviewed or certified here.
This is an independent AI-agent scope review, not external peer review
or formal verification.

## 1. Content identities

The reviewed files have these SHA256 identities:

| Object | Bytes | SHA256 |
|---|---:|---|
| Packet README.md | 13,910 | 011d918be3ddc0bfb290381ac3e2608a9c8f07e8404544fc968cdf66976818dc |
| Root README.md, whole-file identity only | 12,072 | c6417e230a3e7f14d8e3ca711235a001c3bd8b0f0d2168b2e0d86e97c3ea158e |
| Reviewed root addition only | 856 | 54df4d1ca6fee8120e1e1a7e331720c8e216209ea398cc8f8ff1ccc90b3bc6c8 |

The root-addition hash covers the exact UTF-8 bytes from its heading
through the two newlines immediately before the subsequent License
heading. Deleting precisely those bytes reproduces the root README at
the declared parent commit
f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32. I checked this
byte equality. It identifies the review scope; it does not validate
any inherited claim.

The four proof notes used for the comparison are:

| Proof note | SHA256 |
|---|---|
| JOINT_DIVISOR_MEAN.md | 7b42abe2c3c62acfd934b663405821748eac54bb440f1d1071671961a9e97035 |
| MOVING_AUXILIARY_ADAPTER.md | e91e0f7b3c3d885587fc9197539beaf1caa8e0c80ed9c8bba5c15340090b5eda |
| OPTIMIZED_A2_TRANSFER.md | d5a87c27959b64e62df7dd3aa2fdd33cc8b42af6e5a64e9bfb20d6b74af0277a |
| SIGNED_CONDUCTOR_PROGRESS.md | d973468a0e0a893f43327e6f3a4ac706076952ec44a2a3114423ea515bdc4e4a |

This navigation review compares the overview with these proof
statements and their explicit hypotheses. Their detailed mathematical
reviews are separate records. In particular this document does not
substitute a summary-level comparison for replay of the imported
theta, sieve, angular or subconvexity foundations.

## 2. The moment implication was checked against the exact source

I read the relevant mathematical source in PR #913 at
6498d6cc2eded03159c7332b25fd224ad07f89c1:

| Source file | SHA256 |
|---|---|
| GENERAL_MOMENT_ATTACK.md | a4ca15c0d731ef6000b19507b39b64a4786a7f8af9939864b3176221bf02b499 |
| MOMENT_OBSTRUCTIONS.md | 663c6ac878eb0fdd865389ac066ff5a23dbb33016e7061384a83fd186be3fd9b |

The general-moment note fixes the Eisenstein normalization, a finite-order
character, a fixed smooth test supported in a positive compact interval,
and every nonzero element row. Proposition 6.2 and equation (6.5)
give the extraction exponent

$$
\beta=\frac12+\frac{5h}{12k}+\frac{\epsilon}{2k}
$$

from a full $2k$-th moment bounded by $D^{k+h+\epsilon}$.
This follows by matching the premise
$D^{2k\beta+h/6}$ to that moment budget. The positive-density
sixth-power extraction must retain the copying rows and all-scale
control; neither can be removed in the summary.

The repaired overview explicitly requires every fixed
$W\in C_c^\infty((0,\infty))$, fixed finite-order $\nu$,
the fixed bad set $S$, all sufficiently large real scales $D$,
and arbitrarily small fixed positive $\vartheta$ with
$h=1+\vartheta$. Constants may depend on those fixed data.
This matches the required source quantifiers. In particular the
test used to exclude an individual zero may depend on that zero;
the overview now says so explicitly.

Letting the fixed positive $\vartheta$ and the permitted moment
loss be as small as necessary gives the stated open half-plane
boundary $1/2+5/(12k)$ through the declared source framework.
At $k=2$ this is $17/24$. An unbounded set of fixed orders
approaches $1/2$, without any requirement of uniform constants
in the order. These are conditional implications from the full
moment hypotheses, not consequences of a controlled sector.
No statement here excludes zeros on an endpoint line.

The precise hierarchy strength in MOMENT_OBSTRUCTIONS.md,
Theorem 10.1, concerns the entire fixed-twist sextic row family
and all fixed smooth tests. The overview makes the weaker
claim that the unproved hierarchy would approach $1/2$;
it does not silently claim that the packet establishes that
hierarchy or a converse from ordinary RH alone.

## 3. Comparison of the four result summaries

### Joint divisor estimate

The local quotient, both branches of the block mean, the permitted
row-independent divisor coefficients, and the squarefree row restriction
agree with JOINT_DIVISOR_MEAN.md. The omitted seminorm factor is
expressly declared to be fixed.

The tail conditions

$$
\frac12<a<\frac56,\qquad
b=\frac{3-a}{2}+\eta,\qquad
\eta>0,\qquad R\ge Q^{2/3}
$$

and its bound $Q^{1-a+\epsilon}R^{-\eta+\epsilon}$ agree
with Theorem 5.1. The $Q^{1/4}$ comparison at $a=3/4$
is restricted to that tail. The overview expressly retains the
unchanged full-series condition $2b+a>3$.
Its A2 statement remains a finite coefficient identification and
credits PR #914; no global second functional equation is inferred.

### Moving labels and optimized A2 transfer

The definitions

$$
r=q/(q,f),\quad
\ell=N\operatorname{lcm}(q,f),\quad
m=(Nr)^{1/3}(Nf)^{2/3},\quad
X=\sqrt{AB}
$$

retain the overlap and agree with both corresponding proof notes.
The all-row statement includes nonzero element rows with repeated
prime factors and bad-prime components; it is not a squarefree-row
substitution. The overview preserves the explicit $11/12$
angular assumption, polynomial bounds on the moving parameters,
and the absence of a spurious coprimality restriction between the
squarefree inner index and unrestricted cube index.

All five monomials of its equation (3.1), and the child cutoff
$U_{c,d,e}=U/(Nc\,Nd)^{1/2}$, agree with
OPTIMIZED_A2_TRANSFER.md. The convergence explanation correctly
distinguishes the improved denominator exponent $5/4$ from
the nonsummable common-cutoff exponent $13/16$.
The proof's treatment of positive subunit cutoffs and nonempty
smaller rectangles is accurately summarized.

The two explicit ranges agree with the optimized theorem:

$$
D^{6/5}H^{13/15}
\quad\hbox{and}\quad
DH^{151/114},
$$

with junction $H=D^{38/87}$ and upper stated height
$D^{19/22}$. The resulting diagonal range
$H\le D^{114/151}$, exponent $379/228$ at
$H=D^{1/2}$, and comparison saving
$25/12-379/228=8/19$ all match the proof.
The overview credits the raw-polynomial saving to PR #923.
The new assertion is its transfer to the full arithmetic A2
completion and moving mixed family.

These are positive norms. The overview does not replace the
remaining centered two-column form by such a norm, and explicitly
contrasts the reached short-row scale with the critical first-Poisson
dual length $D^{3-\vartheta}$.

### Residual conductor sectors

The repaired overview now imposes $f\ne1$ and fixes a
nonnegative smooth radial row majorant $\Phi$ that is at least
one on the unit disk. These are required by the complete smooth
row-kernel argument. Principal residual primes stay in the
separate zero mask. The true conductor is the product of the
nonprincipal incidence ideals; it is not replaced by the shorter
accounting complexity.

The exponents $359/512$ and $103/512$, the prime-factor
branch $Y^{1/6}L^{2/3}G^{1/6}$, and the three displayed
diagonal-size regions agree with SIGNED_CONDUCTOR_PROGRESS.md.
The extra balanced-divisor region retains an actual conductor
divisor of norm comparable to $(Nf)^{1/3}$.
The overview correctly identifies Söhne's input as the precise
form quoted by Wu, rather than claiming direct independent
verification of the original Söhne paper.

Both fourth-moment examples and their strict excesses match
the proof. The comparisons concern rigorous upper bounds for
incidence collections, not lower bounds for their contributions.
The statement about every fixed order allows constants depending
on that order and does not claim uniformity as $k$ grows.

## 4. The remainder and validation boundaries are preserved

The overview's inequalities for the real residual sum $V_h$
match Section 6 of the signed-conductor note. They remove a
Hermitian controlled collection by an absolute bound, not by
monotonicity of a signed sum. The requested averaged estimate
now carries both $e\ge0$ and the source's fixed universal
Mellin-factor test, with every positive loss.

The conditional boundary $1/2+5h/24+e/4$ is described
as depending on this still-unproved averaged estimate and on
the pinned detector/source framework. The overview repeatedly
states that the estimate has not been proved. Its discussion
of the fully separated singleton case is restricted to
$0<\vartheta\le1/10$, where the claimed failure of the
present conductor bounds to reach the target is correct.

The retained finite report records 22,743 successful checks
including nine negative controls, matching the overview's
numerical description. This review checked that description
against the retained report; it is not an independent execution
or audit of the checker. The overview correctly limits the
diagnostic to finite arithmetic and expressly excludes infinite
theta estimates, external subconvexity proofs and moment
certification. Checker integrity and publication receipts have
their own scoped records.

The new root README paragraph faithfully compresses these four
results. It retains imported assumptions for the theta
deductions and leaves the remaining signed covariance, full
fourth moment, generalized hierarchy and RH open. Its description
of independent reviews as AI-agent reviews is appropriately scoped.

## 5. Reported issues and final disposition

I requested three repairs before approval:

1. State the fixed-test and all-scale quantifiers needed for the
   pinned moment implication, and allow the implied constant to
   depend on the fixed character, bad set and test.
2. State $f\ne1$ and the radial smooth-majorant hypothesis in
   the conductor accounting. Omitting $f\ne1$ would allow an
   incorrect reading of the principal block at $L=G=1$.
3. Preserve $e\ge0$ and the fixed universal Mellin-factor test
   in the sufficient averaged target.

The author applied all three, and I read the repaired passages
and recomputed the final overview hashes in Section 1.
No unresolved mathematical scope issue remains in this review.

No proof note or inherited root prose was changed by this review.
The content approval is limited to the stated hashes and may be
bound to the subsequent source commit by a separate exact-commit
receipt.
