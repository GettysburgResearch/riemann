# Root reconstruction of the new research deductions

**Reviewer:** root. **Date:** 2026-10-10.

**Verdict:** the three separately authored notes listed below pass the
specified mathematical reconstruction, with their imported analytic
assumptions retained. Root authored the optimized-transfer note and the
finite checker, so this document is not an independent review of either
of those objects. Their separate reviewers are recorded below.

This is an AI-agent review, not external human peer review, a Lean
certificate, or integrated mathematical acceptance.

## 1. Content identities and independent scope

| Object | Author | Reviewed SHA-256 |
|---|---|---|
| MOVING_AUXILIARY_ADAPTER.md | moving_auxiliary_attack | e91e0f7b3c3d885587fc9197539beaf1caa8e0c80ed9c8bba5c15340090b5eda |
| JOINT_DIVISOR_MEAN.md | joint_divisor_attack | 7b42abe2c3c62acfd934b663405821748eac54bb440f1d1071671961a9e97035 |
| SIGNED_CONDUCTOR_PROGRESS.md | signed_conductor_attack | d973468a0e0a893f43327e6f3a4ac706076952ec44a2a3114423ea515bdc4e4a |

I read all three complete notes. The moving-adapter review covers all
six sections. The joint-divisor review covers the analytic deduction
in Sections 1–6 and the finite A2 coefficient comparison in Section 7,
without independently replaying the global Chinta–Gunnells theory.
The signed-conductor review covers every statement, the all-order
incidence proof, both explicit configurations, and the residual
replacement.

The final joint-divisor edit corrects the primary local-polynomial
citation to include equation (2.9). The final signed-conductor edit
restricts the inadequacy statement to the intended near-critical
range. Neither changes the earlier reconstructed estimates. I checked
the actual final files, including those repairs.

For source comparison I read the exact mixed family in PR #918 at
cfa102748b26f840ccc4b963a660711424db0ec3, the all-row and cube-inverse
notes of PR #921 at 4e6d4aa57ae4cb04d76b2b31279ac367951b469a, the
all-row raw gain of PR #923 at 1a1152008706f7e24fa1efe4990588f8f99c5d8d,
the relevant A2 formulas of PR #914 at
0cc0428fedbbfc340044c7451b3d392c1da9a103, and the inherited PR #922
mathematical source at 8f2acaacddc10bd8fb053a66070a1d06d25aa922.
The imported October 5 source labels used by the new arguments were
also compared. These reads reconstruct the interfaces and their use;
they do not independently reprove theta automorphy or the imported
completed mean square.

## 2. Moving exclusions and auxiliary twists

### 2.1. Exact family and local masks

The finite physical family agrees with PR #918. Its squarefree a,n
indices obey \((a,nb)=1\), while b is unrestricted and there is no
\((n,b)=1\) condition. Every original index avoids the fixed bad set.
The reflected cusp indices are not subjected to that physical mask.

The identity replacing the moving labels by the literal row
\(kf^4q^6\) is correct including zeros: the q sixth power excludes
all three indices, and the f twelfth power on the cube index is a
coprimality indicator. It does not justify enlarging the physical row
ball to the norm of that artificial row. The proof avoids that error
by summing the actual physical row valuations.

For q,f squarefree with overlap, \(r=q/(q,f)\) and the two costs are

\[
L_{q,f}=Nr\,Nf,\qquad M_{q,f}=(Nr)^{1/3}(Nf)^{2/3}.
\]

At a prime dividing q but not f, the physical-zero-valuation principal
branch has inactive amplitude \(1-z^{-1}\), while its active branch
has amplitude \(z^{-1/2}\), the stated inverse quadratic phase, and
the additional period. The three energy costs are bounded by
\(1,z,z^{1/3}\).

At a prime of f the three pieces of the fourth-power transform have
squared-amplitude/length pairs
\((z^{-1},z^2)\), \((1,z)\), \((z^{-1},z^{-1})\).
The active squarefree and cube reindexings are different and both
are retained. Their energy costs are bounded by \(1,z,z^{2/3}\).
When q and f overlap the f case already contains the required zero
mask; multiplying by an additional q cost would be incorrect.

I checked the physical row residue classes modulo six, including
positive valuations congruent to zero, and the auxiliary shift by
four. Their amplitude, branch count, and height factors give the
listed convergent valuation sums. Ordinary repeated primes, fixed
bad-prime tails, and the finite unit classes are accounted for.
The support relation used in the scalar g sum survives the active
period changes.

### 2.2. Analytic input and both inversions

The scalar premise is applied to the actual fixed ray and angular
characters, with moving exclusions. No arbitrary g-dependent divisor
coefficient is inserted into it. The choice \(\beta=11/12\) retains
the stated source-conditional reciprocal input; the counting
alternative \(\beta=1\) is distinguished.

The completed energy, its full signed cube inverse, and the smaller
nonempty lengths have consistent normalizations. The two auxiliary
Möbius sums are not collapsed by dropping their coprimality. Their
finite local corrections produce the summable powers displayed in
the proof for \(\beta>1/2\).

I reconstructed the exact A2 child scales

\[
A_t=A/(CJ^2E^2),\quad B_t=B/(C^2JE^2),\quad
q_t=qcde,\quad f_t=ef,
\]

and the normalized outside magnitude \(1/(CJE^{3/2})\).
The overlap at e gives \(r_t=rcd\),
\(L_t=LCJE\), and \(M_t=M(CJ)^{1/3}E^{2/3}\).
Substitution in the three terms of the symmetrized energy gives the
claimed strictly summable exponents. Forward and inverse operators
therefore preserve that positive envelope.

The final diagonal convention is essential and correct: an A2 child
reconstructs the original product with \(c^3d^3e^4\), and the cube
inverse reconstructs it with the full combined cube factor. The
strict diagonal selector must be attached to that original product
before any Möbius cancellation. This identity alone supplies no
estimate for the resulting two-child signed covariance.

## 3. Joint divisor recombination

I independently checked the direction of the moving Euler factor:
removing d from the completed cube L-function requires
\(\prod_{p\mid d}(1-z_p)^{-1}\) when recovering the raw series.
Combining the old outer coefficient with its correction yields the
numerator \(1-A_p\). The exact exterior ratio and every zero mask
therefore survive in the new representation.

For the allowed quadratic row value \(\varepsilon=\pm1\),

\[
\frac{1-A_0\varepsilon}{1-z_0\varepsilon}
=1+\frac{z_0(z_0-A_0)}{1-z_0^2}
  +\frac{z_0-A_0}{1-z_0^2}\varepsilon.
\]

The strict condition
\(\min(3a-1/2,\,2b+a-1/2)>1\) supplies absolute summability
with a small positive norm weight. At deleted primes the proof
uses the original zero, not \(\varepsilon^2=1\).

Both branches of the joint block estimate follow with the stated
normalization. The first freezes the cube index and uses Gauss CRT
to combine the two coprime squarefree factors into a single column,
with divisor-bounded row-independent coefficients. The quadratic
correction expansion fixes its own small divisor before doing this
recombination. The second branch applies the completed theta mean
and finite Minkowski to the divisor block. The minimum is legitimate
because both estimates bound the same complete block.

I reconstructed the Mellin norm powers and all four crossover scales:
Q, \(QF^{1/2}\), \((QF)^{1/2}\), and \((QF)^{4/5}\).
The four resulting block norm terms are

\[
\begin{split}
&Q^{1/2}F^{1/2-b},\\
&Q^{1-a}F^{3/2-b-a/2},\\
&Q^{3/4-a/2}F^{5/4-b-a/2},\\
&Q^{1-4a/5}F^{3/2-b-4a/5}.
\end{split}
\]

With \(b=(3-a)/2+\eta\), their F powers become respectively
\(a/2-1-\eta\), \(-\eta\), \(-1/4-\eta\), and
\(-3a/10-\eta\). At \(F\ge Q^{2/3}\) they are all bounded by
\(Q^{1-a}F^{-\eta}\) for \(1/2<a<5/6\).
Dyadic summation proves the announced tail theorem.

The endpoint \(5/6\) is excluded because the Mellin argument uses a
strict summation margin. The lower divisor blocks are not controlled
by the same improved Q factor. In particular the complete positive
series still requires \(2b+a>3\). The note accurately distinguishes
a tail saving from a full-series or moment improvement.

The finite A2 polynomial and its insertion vectors match the pinned
PR #914 arithmetic conventions. The two vectors \((1,2),(2,1)\)
have zero Cartan pairing modulo three; \((2,2)\) has pairing
\((2,2)\). The separate reviewer opened the two primary
Chinta–Gunnells papers and checked their exact displayed formulas.
My approval of this section is restricted to the finite algebra and
its normalization comparison, with no new global A2 adapter inferred.

## 4. Residual conductors and the signed remainder

I opened Wu's primary v6 article and the published Blomer–Brumley
paper. Wu's Theorem 1.1 applies to all unitary Hecke characters.
Blomer–Brumley's Theorem 1 supplies \(\theta=7/64\) over every
number field, hence the exponent

\[
\beta_0=\frac14-\frac{1-2(7/64)}{16}=\frac{103}{512}.
\]

Wu's introduction explicitly quotes the divisor-sensitive Söhne
estimate used in the note for every ideal dividing the finite
conductor. This is the declared source for that input. I did not
reproduce the original 1997 proof or claim a stronger theorem than
the quoted statement.

### 4.1. Exact row adapter

Unit-nontrivial residual characters give an exactly vanishing radial
row sum. In the other case the character descends to an ideal Hecke
character; class number one and the six units give the factor six.
The nonprincipal residual conductor is the product of every prime
with nonzero signed multiplicity modulo six. It is not
\(Ng_1\sqrt{Ng_2}\).

The full principal mask becomes its finite Euler polynomial before
the contour shift. The Mellin transform is rapidly decreasing on
strict positive vertical lines, the nonprincipal L-function is entire,
and shifting to \(1/2\) crosses no pole. The finite mask costs only
an arbitrarily small conductor power. The archimedean conductor
of a vertical twist contributes polynomial t growth, absorbed by
the test. No reciprocal L-function or zero-free premise is needed.

The greedy conductor-divisor argument constructs an actual divisor
between \(F^{1/3}P(f)^{-2/3}\) and \(F^{1/3}P(f)^{1/3}\).
Inserting it into the quoted theorem gives \((FP(f))^{1/6}\).
With a stipulated divisor of size comparable to \(F^{1/3}\), the
prime factor loss disappears.

### 4.2. Incidence count and strict new domains

For fixed nonprincipal \(g_j\), every principal prime appears at least
twice, so

\[
Nq_0\le (BD)^k\prod_j(Ng_j)^{-j/2}.
\]

Counting ideals q0 and assigning their finite incidence patterns
introduces only \(D^\epsilon\) for fixed k. After the Hecke bound,
the \(g_1,g_2\) block sums are
\(L^{1/2+\beta_0}\) and \(G^{\beta_0}\).
All \(j\ge3\) ideal sums converge strictly. With the divisor-sensitive
bound these exponents become \(2/3\) and \(1/6\).

The proof only drops masks after taking a positive majorant.
Consequently each estimate applies to an arbitrary tuple subcollection.
Taking the literal union of the old and new controlled sets, counting
overlaps once, is valid. The resulting sector definitions are
Hermitian, so subtraction from the old real signed remainder
preserves its real nature and gives the stated upper and lower
bounds.

I checked both feasible fourth-moment patterns: the four factor
scales, the side gcd inequalities, the matched cross separations,
the distinction between conductor and complexity, and the old/new
exponents. The improvements relative to \(HD^2\) are
\(-869/204800\) and \(-1/120\). These are rigorous upper-bound
comparisons, not measurements or lower bounds on the true contribution.

The repaired final obstruction statement correctly restricts
\(H=D^{1+\vartheta}\) to \(0<\vartheta\le1/10\).
Neither subconvex branch bounds the entire separated singleton
collection at diagonal size there. The remaining averaged signed
covariance is still a hypothesis, so no new zero-free boundary follows.

## 5. Separate review and finite computation

The optimized-transfer note is root-authored and independently
reconstructed in OPTIMIZED_A2_TRANSFER_REVIEW.md by
moving_auxiliary_attack. That reviewer also authored its mixed-family
input; joint_divisor_attack independently reviewed that input in
MOVING_AUXILIARY_INDEPENDENT_REVIEW.md. The authorship relationship
does not substitute for either proof.

The finite checker is also root-authored. Its separate review and
normal/optimized-Python reproductions are recorded in
CHECKER_INDEPENDENT_REVIEW.md. Its exact local identities and rational
exponents diagnose specific arithmetic mistakes; they do not verify
any infinite theta estimate, large sieve, subconvexity theorem, full
moment, or RH.

The smallest still-unproved global step is the bound for the residual
signed covariance after the newly controlled sectors have been removed.
For the source-conditional auxiliary and joint-divisor theorems, the
smallest imported dependencies are the explicitly normalized completed
theta mean, local reflected coefficient framework, large sieves, and
uniform angular scalar premise stated in the relevant proof. This
review neither hides nor removes those dependencies.
