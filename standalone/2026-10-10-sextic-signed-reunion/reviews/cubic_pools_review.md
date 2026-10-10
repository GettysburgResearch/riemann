# Independent review: joint physical cubic pools and incidence selectors

Reviewer: `signed_auxiliary_attack`.

Reviewed mathematical source:
`/workspace/scratch/6ec6134c1535/pass2_higher_balanced_cubic_pools.md`.

Exact SHA-256:
`622cf846a961aed28ac0363f91766045f328c99700931621f123c17347c6bc23`.

## Verdict and scope

**PASS for the component theorems with precisely the declared inputs.**

I independently reconstructed the all-row cubic reduction, the physical
higher cubic norms, the mixed-sign coefficient identity, the norm composition,
the fixed-order selector summation, and the signed Hermitian bound. I found no
load-bearing mathematical error at the reviewed hash. The numerical triangle
comparisons also agree with the independently fetched pinned predecessor.

The counting specialization uses the stated classical squarefree cubic sieve
and elementary counting. The improved pointwise specialization remains
conditional on the stated uniform reciprocal/zero-free input. The hybrid
versions additionally retain the imported native second moment in its actual
height and smooth-test domain. This review does not validate the entire
imported canonical theorem or promote any of these premises to unconditional
results.

The result is about complete one-sided polynomial portions and the explicitly
specified complete signed Hermitian blocks. It does not establish a full
fourth or sixth moment, a cofinal moment hierarchy, or the long initial signed
covariance. It gives no permission to cut arbitrary terms from a signed block.

## 1. Sources independently checked

I read the complete reviewed source at the hash above and re-read the relevant
local sections of the pinned PR #921 `HERMITIAN_INCIDENCE.md`, including its
native second-moment domain, optional pointwise hypothesis, finite test
seminorms, moving exclusions, exact forward Euler correction, and Schwartz
annulus adapter.

I fetched the following exact GitHub objects through the connected GitHub
tool during this review:

- PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`,
  `standalone/2026-10-10-sextic-separated-cores/SUBSET_PRODUCT_INCIDENCE.md`,
  returned Git blob `f3e4eb59a3f8ffb1c742de5a627704f169d7cc00`.
  I checked its physical singleton-product argument, forward correction,
  exact triangle parameters, exponent `623/720`, and the distinction between
  a fixed shared-ideal core and the full triangle portion after Minkowski.
- PR #917, commit `6b4723042b3d250024eef45cb1924f88f28e902c`,
  `standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/OSCILLATING_OVERLAPS.md`,
  returned Git blob `aa3137869abcee4b380bb0b621e56e93e2072d71`.
  I checked its squarefree cubic input and its full all-element deduction,
  including the exact cube mask and the repeated bad-prime powers.

The classical squarefree cubic large sieve is retained as an explicit analytic
input. I did not independently rebuild the proof of that external theorem.
The reviewed note correctly uses it at order three; no order-six improvement
or GRH-dependent dispersion estimate is needed for the new cubic pool.

## 2. All rows in the cubic sieve

The decomposition

\[
u=\varepsilon v^3ab^2
\]

is unique after fixing the multiplicative ideal generators. The ideals
\(a,b\) are squarefree and coprime, while \(v\) is arbitrary and may meet
either. The row identity retains exactly

\[
\chi_n(u)^2=
\chi_n(\varepsilon)^2\mathbf1_{(n,v)=1}
\chi_n(a)^2\chi_n(b)^4.
\]

In particular, an exponent divisible by three is not replaced by an
everywhere-one value. Freezing \(v\), the unit, the fixed bad parts, and the
smaller squarefree row component gives a coefficient multiplier of modulus at
most one. The only coprimality condition dropped at that stage restricts a
positive outer row sum, which is legitimate.

With \(P=V^3AB^2\), \(F=VAB\), \(M=\max(A,B)\), I recomputed

\[
\frac{(F/M)^3}{P}=\frac{A^2B}{M^3},
\qquad
\frac{(F/M^{1/3})^3}{P^2}=\frac{A}{MV^3B}.
\]

Both are at most one on the dyadic ranges, and \(F\le P\). The resulting
three terms are \(H\), \(H^{1/3}L\), and \((HL)^{2/3}\). The six units,
all good valuation classes, all cube copies, and every bad-prime power are
included. The number of dyads has only a fixed logarithmic cost.

## 3. The physical cubic product and its higher norms

Lemma 2.1 applies to the actual product of the squarefree cubic polynomials,
including collisions between different factors. Its proof does not replace
that physical product by a pairwise-coprime restriction.

For a repeated incidence \(I\), the frozen coefficient has a bounded row
multiplier with its original zero. The residual singleton product is
squarefree. Its coefficient is independent of the row, with a fixed-order
divisor multiplicity and squared mass bounded by the remaining product
length. The all-row cubic sieve therefore applies with the moving exclusion
inside its arbitrary coefficient.

The three norm powers of the shortened product length are

\[
\frac12,\qquad 1,\qquad \frac56.
\]

Consequently a repeated ideal of multiplicity \(m\ge2\) has weights
\(m/2,m,5m/6\), respectively. Only the first weight at \(m=2\) is critical;
it costs a harmonic logarithm. Every other repeated-ideal sum converges.
Minkowski supplies the asserted physical-product estimate with a subpower
loss.

Applying this argument to \(q\) literal copies of every cubic polynomial is
valid for each fixed integer \(q\). The identity
\(|\prod_jU_j|^{2q}=|\prod_jU_j^q|^2\) then gives the claimed physical
\(L^{2q}\) bound with product length \(R^q\). This is a derived classical
cubic estimate. It is not a new native inverse \(2q\)-th moment hypothesis.
The constant may depend on \(q\), as stated.

Hard endpoints cause no difficulty here: these classical estimates require
only bounded fixed-support coefficients. Nonempty factor scales below one
remain in a fixed compact interval; they change the support constants rather
than a power of the large parameter.

## 4. The mixed mu / mu-squared correction is exact

At a good prime, an independent squarefree factor has Euler polynomial
\(1+s_jz_j\), where \(s_j=-1\) for the inverse singleton and \(s_j=+1\)
for the positive squarefree cubic factor. Pairwise coprimality requires
\(1+\sum_js_jz_j\).

I independently expanded

\[
\frac{1+\sum_js_jz_j}{\prod_j(1+s_jz_j)}.
\]

For a nonzero exponent vector \(\mathbf e\), its coefficient is exactly

\[
(1-|\operatorname{supp}\mathbf e|)
\prod_j(-s_j)^{e_j}.
\]

Each numerator contribution changes the corresponding denominator coefficient
by a factor \(-1\). Thus a monomial with support size \(t\) has factor
\(1-t\), and no one-axis term remains. At a moving mask prime the numerator
is one, giving the displayed mask coefficient. The absolute coefficients are
therefore precisely those used in the earlier all-inverse correction.

The finite correction sum is controlled at every weight at least one half by
raising all weights by a fixed small \(\delta\), paying the actual finite
support horizon, and using an absolutely convergent product at the increased
weights. The proof does not claim convergence at the critical weights.
Moving mask factors have only a subpower cost under the stated polynomial
norm bound.

I also checked the location of this correction in the analytic proof. The
physical product norms are proved first. The exact coefficient identity is
then inserted, and its shifted products are estimated by those norms. No
claim that deleting columns contracts a native norm is made. Exterior row
characters have modulus at most one with literal zeros, so their contraction
is legitimate.

## 5. The one-sided cubic-pool estimates

The incidence scales satisfy

\[
R^2XT=D^k
\]

because each pair ideal occurs twice and each frozen higher ideal occurs its
stated multiplicity. The original coupled tests are separated by Mellin
inversion after inserting a smooth singleton cutoff equal to one on the
required support. This yields smooth inverse tests with polynomial frequency
seminorms and bounded hard pair tests. No hard inverse truncation is inserted.

For the first estimate, the pre-normalized energy is

\[
D^\epsilon X^{2b}
\left[HR+H^{1/3}R^2+H^{2/3}R^{5/3}\right].
\]

Dividing by \(HD^k/T=HR^2X\) gives exactly

\[
X^{2b-1}
\left[R^{-1}+H^{-2/3}+H^{-1/3}R^{-1/3}\right].
\]

For the hybrid, interpolation of the native \(L^2\) estimate with the
pointwise bound gives

\[
\|A_i(Y_i)\|_{2q/(q-1)}
\ll D^\epsilon H^{(q-1)/(2q)}
Y_i^{1/2+(2b-1)/(2q)}.
\]

Its reciprocal exponent plus that of the full cubic \(L^{2q}\) norm is
one half. Squaring their product gives precisely equation (4.14) of the
reviewed note. I checked the normalization

\[
R^{-1}
\left[1+R^qH^{-2/3}+R^{2q/3}H^{-1/3}\right]^{1/q}
=\rho_q(H,R)^{1/q}.
\]

All shifted correction weights are at least one half. The selected inverse
weight is \(1/2+(2b-1)/(2q)\); the cubic weights are still
\(1/2,1,5/6\). Therefore the preceding finite correction estimate applies
uniformly before summing Mellin frequencies.

The old native option follows by counting all cubic factors and placing one
inverse factor in \(L^2\). The maximizing singleton scale is the best one
because its exponent in the normalized cost is negative. These facts verify
Theorem 4.1 and its stated source-conditional separation.

## 6. Exact sixth-moment arithmetic and predecessor comparison

I independently evaluated the rational exponents using Python `Fraction`.
The checked values are:

| Quantity | Verified exact value |
| --- | --- |
| Classical triangle cutoff at \(h=21/20\) | \(23/60\) |
| Earlier frozen-pair cutoff | \(33/80\) |
| New \(q=1\) triangle excess | \(181/240\) |
| New \(q=2\) triangle excess | \(119/160\) |
| Saving from the pinned \(623/720\) | \(35/288\) |
| Optional \(b=7/8\) diagonal cutoff | \(19/55\) |

The pointwise piecewise cutoff was also checked at both branch endpoints and
interior examples. Its switch is exactly \(h=27/26\), where the proposed
cutoff equals \(h/3\). On the upper branch the bound is
\((27-4h)/66\), and on the lower branch it is
\(1/2-4h/27\).

The predecessor #923 gives `623/720` for the complete triangle portion,
after counting all three shared pair ideals. It is therefore the correct
quantity to compare with the new pool estimate. The reviewed proof does not
compare a fixed-core bound against a whole-portion bound by accident.

These are exact rational bookkeeping checks. They do not numerically certify
the analytic inequalities or an infinite moment theorem.

## 7. Complete selectors and their summation

For a fixed finite list \(1\le q\le q_*\), one may minimize the valid
costs. The constant can depend on \(q_*\); no growing-order uniformity is
claimed. The selector depends only on the frozen higher ideals and the pair
dyads, so each inverse singleton sum remains complete.

After taking square roots, the frozen higher ideals have weights
\((Nc_I)^{-|I|/2}\). Since \(|I|\ge3\), their product sum converges.
Pair dyads have only a fixed logarithmic count because their arithmetic
variables were retained in the physical cubic pool. This verifies the
normalization and the uniform threshold in Theorem 6.1.

At \(R\ge H\), all three terms of \(\rho_1\) are bounded by a constant
times \(H^{-2/3}\). Thus the stated condition on the singleton product
does give diagonal-size energy. Feasibility is still subject to the original
factor supports and \(R^2XT=D^k\), as the note explicitly says. At order
four the one-pair specialization recovers the earlier retained-cubic
mechanism; the new numerical examples exploit a genuine joint higher-order
pair pool.

The positive one-sided estimate permits an exact polynomial split, followed
by the usual norm inequality before smoothing. It does not imply that an
arbitrary subset of the corresponding signed Hermitian expansion is bounded
in absolute value. The reviewed text preserves this distinction.

## 8. The signed Hermitian extension

For a full Hermitian incidence, the parity of its total multiplicity supplies
the prime sign, while the left-minus-right multiplicity supplies the finite
and row character powers. These are different quantities, and the proof
uses both correctly.

The retained even-incidence group has a common residue exponent, all two or
all four modulo six. Its full physical product is therefore a cubic product
of the type already proved. Opposite orientations are not silently combined
into one squarefree cubic column.

The Hölder allocation in Proposition 7.1 is

\[
\frac12+\frac{q-1}{2q}+\frac1{2q}=1.
\]

Its three factors are a full native axis, a partly interpolated native axis,
and the higher physical cubic pool. For \(q=1\), the middle factor is only
pointwise; that case needs only the first native axis. The other odd axes
retain their separately stipulated pointwise inputs, including odd quadratic
powers, and the other even axes are counted.

I recomputed the ratio to the earlier two-native-axis bound. It is exactly

\[
\left[Q_L^{2b-1}\rho_q(H,R)\right]^{1/(2q)}.
\]

Thus the declared condition gives a true improvement for a complete signed
block. No extra native \(L^2\) factor is implicitly assumed.

## 9. Schwartz extension and final limits

The annular argument keeps the original column lengths, arithmetic labels,
and base selector. Only the positive norm majorant is enlarged to the next
row height. Applying the inputs at the larger reference parameter is allowed
by their explicitly repeated smaller-scale quantifiers. The actual
pre-normalized expressions have row-height powers at most one, apart from an
arbitrarily small preliminary loss, so fixed Schwartz decay sums the annuli.

For a signed row profile, this statement is read with its absolute Schwartz
majorant in the norm estimates; for the source's nonnegative profile it is
literally a weighted norm. No positivity of a signed arithmetic sector is
needed.

At the all-singleton balanced core, \(R=1\), the new finite-
\(q\) hybrid cost is never better than the existing native option. This is
consistent with the declared remaining gap. The reviewed proof gives neither
a diagonal estimate for that core nor the long-dual signed covariance needed
for the full target.

No repository file was edited during this review. This is an independent
AI-agent mathematical audit at the stated hash, not external human peer
review or formal proof verification.
