# A complete logarithmic-derivative moment, its annular defect, and the feedback barrier

25 October 2026.

**Status.** Algebraic identities and source-dependent moment consequences.
The complete-convolution moment in Proposition 1 is a genuine bound for the
original inverse coefficients. Its annular prime-square error also has a
proved upper bound. The separate agent `fractional_global` independently checked
Proposition 1 and (12)--(14), including signs, normalization, original masks,
and all residual scales. The remaining discussion has author-side review.
No improved zero-free region, literature novelty, or formal verification
is claimed; the imported moment theorem was not independently reproved.

**Scope.** The physical sixth-power-free rows over `E = Q(omega)`, both source
orientations, fixed finite ray twists, common smooth norm profiles, and the
source's literal zero extensions. All asymptotic assertions have cofinal
scale scope. The scalar calculation at the end is illustrative, not an
analytic certificate.

**Exact sources.**

* `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
  `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
  blob `268c4e3206d460c617d3d2129742a72b831b3def`; labels
  `lem:marked`, `eq:raw-moment`, `lem:inverse-amplification`,
  `prop:detector-witness`, and `prop:detector-counts`.
* `GettysburgResearch/riemann@5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`,
  PR 1022,
  `standalone/2026-10-25-hlc-zero-free-transfer/second-pass/CAPPED_NATIVE_MOMENT.md`
  and the adjacent `DETECTOR_CONSUMER.md`.
* Liu, *Zero-free half-planes for Hecke L-functions over number fields*,
  [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), Sections 14
  and 15.2, for the identification of the critical amplitude class.

**What ran.** Fresh reading of the source's marked moment, exact detector,
physical amplification, the capped-moment note, and the critical-class
consumer. One short floating-point calculation evaluated the explicitly
displayed algebraic critical class. No large-scale experiment was used.

**Smallest remaining gap in this route.** Prove that a large product of a
detected inverse annulus and the selected prime annuli forces a comparable
large value of the complete, signed convolution in Proposition 1, with the
required total length below the row length and without changing its
coefficients. The identity alone does not provide that lower bound.

## 1. Native notation

For each physical row `u`, write its original zero-extended multiplicative
character as

\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\varepsilon_\chi}
             1_{(n,Q_0)=1},\qquad \varepsilon_\chi\in\{-1,1\}.
\]

Every statement below uses one such character throughout a product. The
puncture is retained in `psi_u`; its prime support is never restored. The
same argument applies when the puncture is absent. Its uniformity must be
licensed by the moment being used.

For an annular smooth profile `W`, a common real height `v`, and `Y >= 1`, set

\[
 M_u(Y,v;W)=Y^{-1/2}\sum_n\mu_E(n)\psi_u(n)(Nn)^{iv}W(Nn/Y).
\]

Let `I(U,Y,v;W)` be its nonnegative weighted second moment over the original
sixth-power-free rows `U <= Nu < 2U`, with bounded nonnegative row weights.
The unmarked source estimate supplies, after an arbitrarily small power,

\[
 I(U,Y,v;W)\ll (UY)^\epsilon(1+|v|)^A p_J(W)^2
                 [U+U^{1/6}Y^{5/6}].                 \tag{1}
\]

Here the relevant bounded length ranges, derivative order, height order,
and original mask hypotheses are fixed first. At `Y=U^r`, `r >= 1`, the
capped native estimate, at its more extensive stated source dependencies,
replaces the exponent `(1+5r)/6` by

\[
 e_{\rm new}(r)=\min\{(1+5r)/6,\;2/7+3r/4\}.        \tag{2}
\]

## 2. An actual joint bound after complete divisor reassembly

Define the complete von Mangoldt convolution

\[
 \mathcal J_u(Y,v;W)=Y^{-1/2}\sum_{d,m}
   \mu_E(d)\Lambda_E(m)\psi_u(dm)(N(dm))^{iv}
   W(N(dm)/Y).                                       \tag{3}
\]

The sum is finite for an annular compactly supported `W`. There is no
independent cutoff in `d` or `m`, and `m` runs over all prime powers with
their von Mangoldt weights.

**Proposition 1.** With exactly these hypotheses,

\[
 \mathcal J_u(Y,v;W)
  =-\log Y\,M_u(Y,v;W)-M_u(Y,v;W\log).               \tag{4}
\]

Here `(W log)(x)=W(x) log x`. Consequently

\[
 \sum_u w(u)|\mathcal J_u(Y,v;W)|^2
 \ll (1+\log Y)^2 (UY)^\epsilon(1+|v|)^A p_{J'}(W)^2
                  [U+U^{1/6}Y^{5/6}],                \tag{5}
\]

and the same complete convolution inherits (2). This is a moment at total
length `Y`, without an additional separate prime-length cost.

**Proof.** The ideal convolution identity is

\[
                    \mu_E*\Lambda_E=-\mu_E\log N.    \tag{6}
\]

For example, it follows by differentiating `1/zeta_E(s)` in its half-plane
of absolute convergence and comparing Dirichlet coefficients. Multiplying
each coefficient by the completely multiplicative, zero-extended
`psi_u(n)(Nn)^{iv}` preserves (6), including all nonunit zeros. Substitution
in (3) gives (4). The inequality `|a+b|^2 <= 2|a|^2+2|b|^2`, followed by
(1), proves (5). On a fixed compact annular support, multiplication by
`log x` is a bounded operation between the relevant finite smooth
seminorms. The proof of the capped version is identical. QED.

Thus one can reassemble all divisor-length pieces first and obtain a real
joint estimate. It is not permissible to replace (3) by one separately
chosen inverse/prime annulus in (5).

This adapter is reversible. Once `Y` is large enough that `log(Yx)` is
bounded below on the fixed annular support,

\[
 M_u(Y,v;W)=-\mathcal J_u\!\left(Y,v;
                              \frac{W(x)}{\log(Yx)}\right).      \tag{5a}
\]

The new profile has fixed-order seminorms `O(p_J(W)/log Y)`. Consequently
the complete-convolution moment contains precisely the same native norm
information, up to logarithms, as the unmarked moment. Its possible
utility requires a stronger detector lower bound for this common total
length; it does not constitute an improved moment exponent by itself.

## 3. Exact defect when the two heights differ

Let the inverse factor have norm height `v`, and the von Mangoldt factor
height `v+Delta`. After removing the common factor `(Nn)^{iv}`, the
coefficient of `psi_u(n)` is

\[
 a_\Delta(n)=\sum_{p^k\mid n}\mu_E(n/p^k)\log Np\,(Np)^{ik\Delta}.
                                                               \tag{7}
\]

If `n` is squarefree, this is

\[
 a_\Delta(n)=-\mu_E(n)\sum_{p\mid n}\log Np\,(Np)^{i\Delta}.
                                                               \tag{8}
\]

If `n=p^a b`, `a >= 2`, `b` squarefree, and `(p,b)=1`, it is

\[
 a_\Delta(n)=\mu_E(b)\log Np\,
       [(Np)^{ia\Delta}-(Np)^{i(a-1)\Delta}].          \tag{9}
\]

If two different primes divide `n` to exponent at least two, it is zero.
Equations (8)--(9) follow by listing the nonzero Mobius terms in (7).
They show exactly why the prime-power cancellation at `Delta=0` is lost
when the incoming heights differ. A small-height expansion gives a
coefficient error at most

\[
        |a_\Delta(n)+\mu_E(n)\log Nn|
               \le |\Delta|(\log Nn)^2.              \tag{10}
\]

A coefficientwise small error is not automatically small in the native
second moment. In particular, `Delta=O(1)` or even `O(1/log U)` does not
license a fixed-power saving by (10). The source detector allows its
height and the incoming prime-polynomial height to be different. Merely
renaming a height as part of a rowwise profile does not repair (4): the
remaining factor then depends on the divisor, not only on the total norm.

## 4. One prime annulus: the exact squarefree part and its square error

Let

\[
 P_u(L,v;V)=L^{-1/2}\sum_{p\ {\rm prime}}
       \log Np\,\psi_u(p)(Np)^{iv}V(Np/L).
\]

Both profiles have fixed compact annular support. For aligned heights,
opening `M_u(D,v;W) P_u(L,v;V)` and writing `n=dp` gives the following
exact squarefree contribution:

\[
 -(DL)^{-1/2}\sum_{n\ {\rm sf}}\mu_E(n)\psi_u(n)(Nn)^{iv}
   \sum_{p\mid n}\log Np\,W\!\left(\frac{Nn}{NpD}\right)
                         V(Np/L).                   \tag{11}
\]

The remaining terms have `d=pb`, with `b` squarefree and `(p,b)=1`, and
are exactly

\[
 \mathcal E_u=-(DL)^{-1/2}\sum_p\log Np\,
    \psi_u(p^2)(Np)^{2iv}V(Np/L)
    \sum_{\substack{b\ {\rm sf}\\(b,p)=1}}
       \mu_E(b)\psi_u(b)(Nb)^{iv}W(Np\,Nb/D).         \tag{12}
\]

Every original zero remains in (11)--(12). No other nonsquarefree pattern
can occur, since `d` is squarefree and the second factor is a prime.

There is a useful paid estimate for (12). Suppose `D/L` lies in a fixed
bounded exponent range and the basic inverse estimate is available with
the indicated profiles. Put `X_p=D/Np`. Then (12) is a weighted sum of
the inverse polynomials at `X_p`, with coefficients

\[
      (L Np)^{-1/2}\log Np\,V(Np/L)\psi_u(p^2)(Np)^{2iv}.
\]

The sum of their absolute values is `O(log(2L))` by elementary ideal
counting, which is already sufficient here. The single-prime deletion
can be removed without changing coefficients arbitrarily: if `M^(p)`
denotes the inverse with `(b,p)=1`, then

\[
 M^{(p)}_u(X,v;W)
   =\sum_{k\ge0}\psi_u(p)^k(Np)^{k(iv-1/2)}
                       M_u(X/(Np)^k,v;W).            \tag{13}
\]

Only finitely many terms meet the fixed annular support. Formula (13)
is the literal identity `1/L^(p)=(1/L)/(1-psi_u(p)(Np)^(-s))` in the
absolute half-plane, then a coefficient identity. Minkowski's inequality,
the geometric factor `(Np)^(-k/2)`, and (1) give

\[
 \sum_u w(u)|\mathcal E_u|^2
  \ll (UDL)^\epsilon(1+|v|)^A p_J(W)^2p_J(V)^2
       [U+U^{1/6}(D/L)^{5/6}],                        \tag{14}
\]

with harmless fixed comparison constants for `Np asymp L`. Terms with
scale below the shortest possible supported norm are zero. If a residual
scale is below one but still meets the fixed annular support, it lies in
a fixed compact positive range, contains only boundedly many ideal
indices, and its second moment is `O_W(U)` by direct counting; no
large-scale source estimate is invoked there. The proof
uses no character moment in the prime variable and no cancellation of
`psi_u(p^2)`; Cauchy/Minkowski absorbs those unit-modulus phases. When
`D/L <= U`, the error therefore has row-size second moment.

The positive result in (14) does not bound (11). At `L=U^ell`, `ell>0`
fixed, the number of divisors `p` in (11) is bounded by a constant
depending on the bounded total exponent range and `ell`. Nevertheless,
its inner divisor weight depends on the factorization of `n`. It is
not a common smooth function of `Nn/(DL)`.

## 5. Why complete reassembly still has no annular lower bound

If all prime powers and all inverse/prime splits are summed with the same
profile of the product, (11) and its prime-power analogues reconstruct
(4). If one prime annulus is retained, the factor

\[
    b(n)=\sum_{p\mid n}\log Np\,
            W(Nn/(NpD))V(Np/L)
\]

remains. The source unmarked inverse estimate is specific to the Mobius
coefficient and a norm-smooth profile. It does not assert its stability
under multiplication by a bounded factorization-dependent `b(n)`.

This is a genuine logical issue even when `b(n)` is nonnegative. A
positive-semidefinite Gram matrix controls the quadratic form for one
coefficient vector; it need not control that form after a diagonal
coefficient multiplier. The two-column row `(1,1)` and vector `(1,-1)`
already exhibit a vanishing form whose value becomes nonzero after the
multiplier `(1,0)`. This example is only a warning about the inference,
not a counterexample in the actual Hecke family.

The same problem affects a putative detector for (3): a large value of
one annular product does not force a large value of the signed sum of
all the products. Maximal prime-amplitude exponent does not, by itself,
supply their relative phases. An explicit formula identifying a nearby
zero also does not automatically give a lower bound for its inverse
residue or exclude cancellation with the other zeros. Those facts would
need their own quantitative proof with the source's common profiles.

## 6. Exact obstruction to moment-density feedback from these marginals

This obstruction covers the selected-prime counts, not just the
unselected Xu--Sang count.

Consider any finite buffered collection of row classes indexed by `j`.
Suppose the existing data give a count exponent `R_j` and pointwise
exponents `w_j(lambda)` for the same nonnegative polynomial weight
`A_lambda(u)`:

\[
 \#B_j\ll U^{R_j+o(1)},\qquad
 A_\lambda(u)\ll U^{w_j(\lambda)+o(1)}\quad(u\in B_j).
\]

The moment obtained solely by summing these two facts has exponent

\[
                 E(\lambda)=\max_j[R_j+w_j(\lambda)]. \tag{15}
\]

If a target class `B_i` has a saturated lower bound for that same weight,
`A_lambda >= U^(w_i(lambda)-o(1))`, division by that lower bound produces

\[
 E(\lambda)-w_i(\lambda)\ge R_i.                    \tag{16}
\]

Taking the best `lambda` cannot reverse (16). Feeding the resulting
counts back into (15) cannot start a strict improvement. For a product
of an inverse value and selected prime values, the exact exponent is

\[
       w_j(r,\mathbf z)=\delta_j r+2\sum_k q_{j,k}z_k.
\]

Thus the same-bin term survives the complete amplitude vector. Applying
the observation only to `q=0` understates the obstruction. It applies
also after refining bins, retaining correlations *only as class labels*,
or taking Holder combinations of moments generated from those same
pointwise bounds. It does not exclude a genuinely new joint mean such
as one exploiting the signed arithmetic in (3), or a strict
nonsaturation theorem. It explains why a density-to-reciprocal-to-density
cycle using no additional inequality cannot supply either.

## 7. The actual critical lengths

At moment parameter `kappa=3/4`, the critical maximal-amplitude class has

\[
 \delta=\frac{147-\sqrt{8289}}{144}
          =0.388583712271\ldots,\qquad x=1/2.
\]

It is the smaller root of `288 delta^2 - 588 delta + 185 = 0`. Define

\[
 t_* =\frac{185-96\delta}{185-138\delta},\qquad
 r_* =\frac{28t_*-5}{37},\qquad
 m_* =\frac{9t_*+5}{37}.
\]

Then, approximately,

| Quantity | Value |
| --- | ---: |
| zero real-part bin `a=(1+delta)/2` | 0.694291856136 |
| detecting cutoff `t_*` | 1.124228051742 |
| short inverse witness `r_*` | 0.715632039156 |
| coupled ordinary witness `m_*` | 0.408596012586 |
| current inverse prime capacity `(1-r_*)/2` | 0.142183980422 |
| ordinary prime capacity `(1-2m_*)/(6kappa)` | 0.040623994406 |
| optimized count `R_*` | 2/3 |

These are far from the long-inverse region `r>10/7` improved by (2).
For example, a pointwise ordinary bound `|S_m| <= U^theta` would have to
have `theta < delta*m_*/2 = 0.07939...` to eliminate this actual short
split. Neither a Burgess exponent nor a Weyl exponent approaches that
requirement. Moreover the Weyl theorem
[arXiv:2108.12283v5](https://arxiv.org/abs/2108.12283v5) concerns totally
real fields and cannot simply be transferred to `Q(omega)`.

The complete convolution in (5) would be useful if the detector could
legitimately retain a total inverse/prime length approaching one instead
of being restricted by `r+2z<1`. At maximal amplitude its lower-bound
exponent would then be `delta(r+z)`. Equations (11)--(16) identify what
has and has not been proved in trying to make that possibility concrete.

The established content of this note is the complete native moment,
the exact height and annular defects, the paid prime-square correction,
and the feedback obstruction. The signed annular coupling needed to
improve the critical count remains open.
