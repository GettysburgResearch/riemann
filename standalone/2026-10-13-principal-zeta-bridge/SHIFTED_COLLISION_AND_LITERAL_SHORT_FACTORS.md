# Literal short factors do not remove the growing collision ridge

**Status:** proposed proved lower bound for the modulus of the exact
arithmetic factor in individual short row terms. This strengthens the
collision-factor obstruction by retaining the actual truncated Möbius
polynomials. It is not a lower bound for a signed row sum, the original
norm-filtered covariance, a moment, or the open CT1 trace.

**Scope:** a fixed moment order, fixed source field and ray data, and an
arbitrary polynomially sized finite collection of polynomially bounded
rows and masks. The same balanced frequency vector works for the whole
collection. An unrestricted Schwartz row tail is not included. The
exterior incidence multiplier and the smooth row weight are stated
separately because they can vanish.

**Exact dependencies:**

- `ANTI_CONJUGATE_COLLISION_GROWTH.md`, SHA-256
  `384667530dc3987f9ea77da0bac67a723d6a57d4635748286a500dc6042c87fa`,
  especially (2.2)--(2.5) and Theorem 3.1. Its fixed-field prime-ideal
  supply is retained as an explicit classical input.
- PR #911, commit `2f8b6a3898a722d0602a91dea73bac344a3bb7dd`, directory
  `research/exploratory/2026-10-10-two-hour-continuation/literature/`:
  `PRIME_SLOT_CANCELLATION.md`, P1--P4 and P8;
  `SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, SC1--SC6;
  `WIDE_SUBCRITICAL_TUBE.md`, WT1--WT5; and
  `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md`, CT1--CT6.

The collision note proves a lower bound only for the rational collision
factor. This note proves that the source's actual short factors cannot
uniformly absorb that growth. Its additional inputs are elementary ideal
counting and the elementary complex-analytic minimum-modulus argument
proved in Section 3. No RH or quasi-RH premise is used.

## 1. Exact arithmetic object and finite-family quantifiers

Keep the source Eisenstein field \(K\), fixed bad prime set \(S\), and fixed
finite-order coefficient character \(\nu\), with its conductor excluded.
For a nonzero element row \(u\), put

\[
\eta_u(\mathfrak n)=\nu(\mathfrak n)\chi_{\mathfrak n}(u),
\]

with every literal nonunit zero retained. For a squarefree mask \(Q\) prime
to \(S\), define the two actual short polynomials

\[
T^+_{Y,Q,u}(s)=
\sum_{\substack{N\mathfrak n\le Y\\(\mathfrak n,SQ)=1}}
\mu_K(\mathfrak n)\eta_u(\mathfrak n)(N\mathfrak n)^{-s},
\qquad
T^-_{Y,Q,u}(s)=
\sum_{\substack{N\mathfrak n\le Y\\(\mathfrak n,SQ)=1}}
\mu_K(\mathfrak n)\overline{\eta_u(\mathfrak n)}(N\mathfrak n)^{-s}.
\tag{1.1}
\]

These are exactly SC2, not arbitrary coefficient vectors. Define

\[
\mathcal I_{Y,Q,u}(\mathbf s)=
\mathcal Q_{Y,Q,u}(\mathbf s)
\prod_{i=1}^kT^+_{Y,Q,u}(s_i)
\prod_{i=k+1}^{2k}T^-_{Y,Q,u}(s_i),
\tag{1.2}
\]

where \(\mathcal Q\) is the literal collision factor (1.2) of the dependency.
Thus \(\mathcal I\) is the arithmetic factor of an individual CT1 short
row term. The full term is

\[
\Phi(u/\sqrt H)\,\omega_{\boldsymbol q}(u)\,
\mathcal I_{Y,Q,u}(\mathbf s).
\tag{1.3}
\]

The weight and exterior multiplier are not part of the lower-bound object
(1.2). In particular, (1.3) can be zero even when (1.2) is very large.

Fix

\[
k\ge2,\qquad \frac13<\sigma<\frac12,\qquad B,C>0,
\qquad C_0\ge1.
\tag{1.4}
\]

For each sufficiently large real \(Y\), let \(\mathscr F_Y\) be any finite
set of admissible pairs \((u,Q)\) satisfying the two separate bounds

\[
|\mathscr F_Y|\le C_0Y^B,
\qquad N(u)NQ\le Y^C\quad((u,Q)\in\mathscr F_Y).
\tag{1.5}
\]

No regularity or nesting of these collections as \(Y\) varies is required.
Constants below may depend on the fixed parameters and source data, but
not on \(Y\) or the chosen collection.

## 2. A small common shift preserves the collision lower bound

Put \(n=2\lfloor k/2\rfloor\) and \(\vartheta_Y=\pi/\log Y\). For real
\(b\), choose the left frequencies to be

\[
\underbrace{\vartheta_Y-b,\ldots,\vartheta_Y-b}_{n/2},
\quad
\underbrace{-\vartheta_Y-b,\ldots,-\vartheta_Y-b}_{n/2},
\quad
\underbrace{-b}_{\text{one slot only if }k\text{ is odd}},
\tag{2.1}
\]

and take all \(k\) right frequencies equal to \(b\). Denote this vector
by \(\mathbf t(b)\). Exactly

\[
\sum_{i=1}^{2k}t_i(b)=0,
\qquad
\max_i|t_i(b)|\le\pi/\log Y+|b|.
\tag{2.2}
\]

**Lemma 2.1 (uniform shifted collision lower bound).** There are constants
\(c_1>0\) and \(Y_1\) such that, for every \(Y\ge Y_1\), every admissible
pair with \(N(u)NQ\le Y^C\), and every
\(|b|\le(\log Y)^{-3}\),

\[
\left|\mathcal Q_{Y,Q,u}(\sigma+i\mathbf t(b))\right|
\ge\exp\!\left(c_1\frac{Y^{1-2\sigma}}{\log Y}\right).
\tag{2.3}
\]

**Proof.** At a prime of norm \(q\), the shift replaces the dependency's
local phase \(a=\eta_u(\mathfrak p)\) by
\(a_b=a\exp(i b\log q)\). All right phases are its conjugate. Thus the
complete pair-sum formula and its negative upper bound on
\(q\ge Y^{1-\varepsilon_k}\) are unchanged: they were uniform over all
\(|a|=1\). There is no accumulated high-prime perturbation loss.

For the finite set of small primes, write the numerator as

\[
N_{q,a}(b)=1-q^{-\sigma}
\bigl[A(x)a e^{ib\log q}+k\overline a e^{-ib\log q}\bigr],
\quad
A(x)=k-n+n\cos x,\quad x=\pi\log q/\log Y.
\tag{2.4}
\]

At \(b=0\), the dependency proves, uniformly over the finite possible
source phases at these fixed primes,
\(|N_{q,a}(0)|\ge c_q(\log Y)^{-2}\). This includes the case in which the
limiting numerator vanishes; its remaining term is exactly
\(nq^{-\sigma}a(1-\cos x)\). The derivative of (2.4) with respect to \(b\)
is bounded by a fixed constant at each such prime. Therefore the change
for \(|b|\le(\log Y)^{-3}\) is smaller than half the displayed lower bound
for all sufficiently large \(Y\). Deleted primes still contribute one.

The small-prime logarithmic cost remains \(O(\log\log Y)\). The uniform
large-prime expansion, its summable cubic error, the final-annulus prime
supply, and the lower-range error are exactly those in the dependency's
Theorem 3.1. They prove (2.3), after reducing its positive constant if
necessary. \(\square\)

The left-slot separation remains \(2\pi/\log Y\), so these points stay
outside the paid common conjugate tube, regardless of \(b\).

## 3. A uniform lower bound for the literal short polynomials away from zeros

**Lemma 3.1 (anchored minimum modulus).** Each polynomial \(T=T^+_{Y,Q,u}\)
or \(T=T^-_{Y,Q,u}\) has a multiset \(Z_T\) of at most \(C_1\log Y\)
complex numbers, counted with multiplicity, such that for every \(A>0\),

\[
|T(s)|\ge\exp[-C_A(\log Y)^2]
\tag{3.1}
\]

whenever

\[
|s-2|\le2,
\qquad \operatorname{dist}(s,Z_T)\ge Y^{-A}.
\tag{3.2}
\]

The constants are uniform in every row and mask. One may take \(Z_T\) to
be exactly the zeros of \(T\) in \(|s-2|\le3\).

**Proof.** First establish a uniform nonzero anchor. The completely
multiplicative character coefficient \(\eta_u\), including the mask and
its zero values, together with \(\mu_K\), gives at \(s=2\) the absolutely
convergent full inverse Euler series

\[
T_\infty(2)=
\prod_{\mathfrak p\notin SQ}
\bigl(1-\eta_u(\mathfrak p)(N\mathfrak p)^{-2}\bigr)
\tag{3.3}
\]

for the plus polynomial, and its conjugate for the minus polynomial.
Since \(|\eta_u(\mathfrak p)|\le1\),

\[
|T_\infty(2)|\ge
\prod_{\mathfrak p}(1-(N\mathfrak p)^{-2})
=\zeta_K(2)^{-1}>0.
\tag{3.4}
\]

The elementary ideal count gives the uniform literal truncation error

\[
|T(2)-T_\infty(2)|
\le\sum_{N\mathfrak n>Y}(N\mathfrak n)^{-2}
\ll_K Y^{-1}.
\tag{3.5}
\]

Thus \(|T(2)|\ge m_K>0\) for every sufficiently large \(Y\), uniformly in
the row and all deletions. On the fixed larger disk \(|s-2|\le4\), direct
counting gives

\[
|T(s)|\le\sum_{N\mathfrak n\le Y}(N\mathfrak n)^2
\le M_Y,\qquad M_Y=C_KY^3,
\tag{3.6}
\]

with the constant enlarged to make \(M_Y\ge1\).

Put \(f(z)=T(2+z)\). Jensen's inequality on an intermediate circle of
radius between \(7/2\) and \(4\), chosen off the zeros, bounds the number
\(N\) of zeros \(a_j\) in \(|z|\le3\) by

\[
N\log(7/6)\le\log(M_Y/m_K)=O_K(\log Y).
\tag{3.7}
\]

Cancel those zeros with the radius-four Blaschke product

\[
B(z)=\prod_{j=1}^N\frac{4(z-a_j)}{16-\overline{a_j}z},
\qquad g(z)=f(z)/B(z).
\tag{3.8}
\]

Multiplicities are included. There is no zero at \(z=0\), by (3.4)--(3.5).
The quotient is holomorphic on \(|z|\le4\), has no zeros in \(|z|<3\),
obeys \(|g|\le M_Y\) by the maximum principle, and satisfies
\(|g(0)|\ge m_K\). Consequently the nonnegative harmonic function
\(\log(M_Y/|g(z)|)\) on \(|z|<3\) obeys, by the elementary disk Harnack
inequality, for \(|z|\le2\),

\[
\log\frac{M_Y}{|g(z)|}
\le5\log\frac{M_Y}{m_K},\qquad
|g(z)|\ge m_K^5M_Y^{-4}.
\tag{3.9}
\]

If \(|z-a_j|\ge\delta\), \(|z|\le2\), and \(|a_j|\le3\), then

\[
\left|\frac{4(z-a_j)}{16-\overline{a_j}z}\right|
\ge\frac{2\delta}{11}.
\tag{3.10}
\]

Combining (3.7)--(3.10), with \(\delta=Y^{-A}\), proves (3.1). If there
are no zeros, the empty product is one and the same conclusion follows
directly from (3.9). \(\square\)

This argument uses the actual constant coefficient and the convergent
Euler anchor of the literal short polynomials. It does not assert a lower
bound for arbitrary coefficient vectors.

## 4. One good frequency set works for every row and mask in a polynomial box

**Theorem 4.1 (literal short-factor obstruction).** Under (1.4)--(1.5),
there are constants \(c_2>0\) and \(Y_2\) such that for every
\(Y\ge Y_2\) there is a measurable set

\[
E_Y\subseteq[-(\log Y)^{-3},(\log Y)^{-3}],
\qquad |E_Y|\ge(\log Y)^{-3},
\tag{4.1}
\]

with the following simultaneous property: for every \(b\in E_Y\) and
every \((u,Q)\in\mathscr F_Y\),

\[
\boxed{
\left|\mathcal I_{Y,Q,u}(\sigma+i\mathbf t(b))\right|
\ge\exp\!\left(c_2\frac{Y^{1-2\sigma}}{\log Y}\right).
}
\tag{4.2}
\]

The frequencies in (4.2) all tend to zero and have total sum exactly zero.

**Proof.** Apply Lemma 3.1 to both literal polynomials for every pair in
\(\mathscr F_Y\). There are at most \(2C_0Y^B\) such polynomials, each
with \(O(\log Y)\) relevant zeros. Choose a fixed \(A>B+2\) and set
\(\delta=Y^{-A}\).

Every evaluation point \(s_i(b)=\sigma+it_i(b)\) moves on a vertical line
with speed one as \(b\) varies. For a given zero, the set of real \(b\)
for which the evaluation is within \(\delta\) of that zero has length at
most \(2\delta\). Summing over all required evaluations and all zeros,
the union of bad parameter intervals has measure at most

\[
C_{k,K,C_0}Y^B(\log Y)\delta
\ll Y^{-2}\log Y.
\tag{4.3}
\]

For large \(Y\), every evaluated point is in \(|s-2|\le2\), because
\(\sigma>1/3\) is fixed and its imaginary part is \(O(1/\log Y)\).
Removing the bad intervals from the interval in (4.1) leaves a set of
measure at least the asserted amount. On that common set, all \(2k\)
factors in each product have the lower bound (3.1). Hence Lemma 2.1 gives

\[
\log|\mathcal I_{Y,Q,u}|
\ge c_1\frac{Y^{1-2\sigma}}{\log Y}
   -2kC_A(\log Y)^2.
\tag{4.4}
\]

Since \(1-2\sigma>0\), the second term is smaller than half the first
for all sufficiently large \(Y\). This proves (4.2), with
\(c_2=c_1/2\). \(\square\)

The size condition and norm condition in (1.5) have different roles. The
norm condition retains enough high prime factors in the collision product;
the cardinality condition permits simultaneous zero avoidance. Neither is
silently inferred from the other in the theorem.

For example, all pairs in
\(0<N(u)\le Y^h\), \(NQ\le Y^k\), with fixed \(h,k\), form a polynomially
bounded collection by fixed-field element and ideal counting. After
enlarging fixed ceiling exponents, they satisfy (1.5). Thus a single set
\(E_Y\) works for every literal row and every source mask in any such
finite physical box. Incidence allocations with the same \(Q\) use the
same arithmetic factors, so they require no extra zero exclusions.

If a selected full term (1.3) additionally satisfies
\(|\Phi(u/\sqrt H)\omega_{\boldsymbol q}(u)|\ge Y^{-B'}\) for a fixed
\(B'\), its modulus has the same lower-bound form after reducing \(c_2\).
If the exterior multiplier is nonzero, its source character part has
modulus one; its literal zero rows remain zero. No lower bound for an
arbitrary smooth row weight is presumed.

## 5. Exact consequence for the remaining target

The collision growth cannot be absorbed merely by observing that the
actual short factors might be small: a common positive-measure set of
central shifts avoids that possibility for every member of a polynomial
row-and-mask collection. Therefore a pointwise polynomial envelope for
the arithmetic factor of each row term is false on the total-frequency
balanced set, even with the literal source Möbius coefficients.

This theorem still permits cancellation in the signed sum over rows,
including the exact radial unit projection and exterior incidence phases.
It also permits cancellation across the independent Mellin frequencies
when the physical norm tests are applied. The complete short representation
and the original finite Euler representation are equal only after those
norm tests, as SC4 states. They are not interchangeable pointwise.

In particular the theorem does not contradict the moment target and does
not prove that CT1 is false. It shows that any proof of CT1 on this set
must retain cancellation between rows or another exact joint mechanism;
bounding individual arithmetic row factors by polynomial envelopes cannot
prove it. A bound for the already norm-filtered, coupled native covariance
remains a distinct and potentially weaker arithmetic target.

All quantifiers are finite-height and polynomial-family quantifiers. No
unrestricted Schwartz tail, scale-uniform source moment, zero-free
improvement, or RH conclusion has been established.
