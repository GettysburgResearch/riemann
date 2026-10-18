# Positive Hermite-square blocks with real Fourier zeros

**Status: PROPOSED analytic model family; finite fitting is reconnaissance.**
The family is classical orthogonal-polynomial mathematics, not an RH
result. It supplies a positive-law alternative to the independent
quadratic Gaussian factors excluded in FACTOR_OBSTRUCTION.md.

Write `He_n` for the probabilists' Hermite polynomial and `L_n` for the
ordinary Laguerre polynomial. The normalized density

\[
 d\mu_n(x)=\frac{\operatorname{He}_n(x)^2}{n!}
             \frac{e^{-x^2/2}}{\sqrt{2\pi}}\,dx
\]

is positive, symmetric and has characteristic function

\[
 \phi_n(z)=e^{-z^2/2}L_n(z^2). \tag{1}
\]

One derivation uses the Hermite bilinear generating identity followed by
one Gaussian integration: for `|t|<1`, the generating function of the
left side of (1) is

\[
 \frac1{1-t}\exp\left[-\frac{z^2(1+t)}{2(1-t)}\right]
 =e^{-z^2/2}\sum_{n\ge0}L_n(z^2)t^n.
\]

Equality of coefficients proves (1), initially on the real axis and then
everywhere by entire continuation. The relevant classical identities are
recorded in the primary NIST sources
[Hermite bilinear generating sum](https://dlmf.nist.gov/18.18.E28) and
[Laguerre generating function](https://dlmf.nist.gov/18.12.E13).

For `n>=1`, `0<=p<=1`, `s>0`, a positive mixture of adjacent such densities,
scaled by `sqrt(s)`, has characteristic function

\[
 f_{n,p,s}(z)=e^{-sz^2/2}
     \{pL_n(sz^2)+(1-p)L_{n-1}(sz^2)\}. \tag{2}
\]

All zeros of (2) are real. Here is a direct orthogonality proof of the
only extension beyond the usual Laguerre zero theorem. For `0<p<=1`, let
`Q=pL_n+(1-p)L_(n-1)`. Laguerre orthogonality makes `Q` orthogonal to
every polynomial of degree at most `n-2` for the positive weight
`e^(-x)` on `(0,infinity)`. Thus it has at least `n-1` distinct positive
sign-changing zeros: otherwise multiplication by the product of all its
positive sign-changing factors would give a nonzero integral of fixed
sign, contradicting orthogonality. Since `Q` has degree`n`, its remaining
zero is real (nonreal zeros occur in conjugate pairs). Moreover

\[
 L_n(-x)=\sum_{k=0}^n\binom nk\frac{x^k}{k!}>0
 \quad(x\ge0),
\]

so no remaining zero is nonpositive. The endpoint `p=0` is simply
`L_(n-1)`. This agrees with the
[NIST positive-zero statement for Laguerre polynomials](https://dlmf.nist.gov/18.16.E9).

Putting `v=s(2n-1+2p)` gives a convenient continuous variance/shape chart.
Its complete even moments are explicit rational polynomials:

\[
 E X^{2r}=(2r)!s^r
 \sum_{k=0}^{\min(n,r)}
 \frac{\binom{n-1}k+p\binom{n-1}{k-1}}
      {k!\,2^{r-k}(r-k)!}. \tag{3}
\]

Binomial coefficients outside their natural range mean zero. Equation (3)
follows by multiplying the Gaussian and Laguerre moment generating
series. It is the formula implemented, with analytic derivatives, in
hermite_scout.py. Saved optimizer residuals do not establish existence.

## Gaussian growth is automatic for this family

Write the Fourier polynomial in (2) as `product_j(1-a_jz^2)` with `a_j>0`.
Then `Var(X)=s+2sum a_j`. Consequently

\[
 |f_{n,p,s}(z)|\le
   \exp[(s/2+\sum_j a_j)|z|^2]
 =\exp[\operatorname{Var}(X)|z|^2/2]. \tag{4}
\]

Independent finite products inherit (4) with their total variance. Thus
cofinal exact theta moment feasibility in this class would automatically
supply complex normality, followed by the same identity/Hurwitz consumer
as the existing real-zero programme. Cofinal feasibility remains open.
The growing graph and bounded-support hypotheses are not relevant to this
different, explicitly Gaussian-polynomial class.

The Gaussian variance `sum s_j` cannot stay bounded below in a cofinal
limit equal to the actual theta law; the latter has no nonzero Gaussian
convolution factor, as proved below. Therefore any successful construction in this family
would need increasing polynomial complexity and vanishing residual
Gaussian variance. Fixed shape complexity must not silently be frozen.

## A further finite complexity constraint

In one block the sum of its Fourier reciprocal-square zero parameters is
`S_1=(n-1+p)s`, whereas its variance is `(2(n-1+p)+1)s`. If every block has
`n<=N`, independence gives

\[
 S_1\le\frac{N}{2N+1}\operatorname{Var}(X). \tag{5}
\]

The power-sum witness method from FACTOR_OBSTRUCTION.md can compare (5)
directly with finitely many actual theta cumulants. For example, the
integer coefficient vectors

```text
[375,-35859,1305830,-19223562,91738523]
[929,-232857,24361269,-1233811672,31243955787,-370336951380,1564944275303]
```

give lower bounds approximately`.402766` from degree22 and`.431062`
from degree30, respectively, using exactly the same pointwise square
witness as in FACTOR_OBSTRUCTION.md. The fresh complete-source checker
certify_hermite_obstruction.py reconstructs through30 and verifies strict
margins above`2/5` and`3/7` by more than`.001`. Consequently products with
`n<=2` cannot match through22, and products with`n<=3` cannot match
through30. The degree14 obstruction to`n<=1` is also included, with its
independent earlier certificate retained.

```text
python standalone/2026-10-18-three-direction-sprint/theta/certify_hermite_obstruction.py --emit standalone/2026-10-18-three-direction-sprint/theta/hermite_obstruction30.json
```

## Why the actual theta law has no Gaussian convolution factor

This fact has a short complete-source tail proof. For `t>=0`, dropping
the negative term in each theta-density summand gives

\[
 \Phi(t)\le8\pi^2e^{9t/2}\sum_{n\ge1}n^4e^{-\pi n^2e^{2t}}
       <640e^{9t/2-3e^{2t}}. \tag{6}
\]

Indeed `n^4<=16^(n-1)`, `n^2-1>=n-1`, `pi>3`, and `e^3>20` bound the
remaining geometric sum by5; `pi<4` completes (6). Evenness covers
negative`t`. The positive source normalization is a fixed constant.
For `q=(|u|+9/2)/2`, substituting `x=e^(2t)` bounds the normalized MGF by
a fixed constant times

\[
 \frac12\int_1^\infty x^{q-1}e^{-3x}\,dx.
\]

Bounding `x^(q-1)e^(-3x/2)` by its maximum at`2(q-1)/3` and integrating
the remaining `e^(-3x/2)` gives logarithm `O(q log(q+1))`. Hence

\[
 \log E e^{uT}=O(|u|\log(|u|+2))=o(u^2). \tag{7}
\]

If `T=G+Z` were an independent convolution with a centered Gaussian of
variance`sigma^2>0`, then `Z` would be centered and Jensen's inequality
would give
`E exp(uT)=exp(sigma^2 u^2/2) E exp(uZ)>=exp(sigma^2 u^2/2)`,
contradicting (7). Finite MGFs of`T` ensure those of`Z` by independence.

Finally, if a sequence of variance1 independent Gaussian-polynomial models
had Gaussian variances bounded below by a positive constant, both those
variances and the residual symmetric laws have subsequences converging
weakly: the residual variances are at most1, so Chebyshev supplies
tightness. Any weak limit retains a nonzero Gaussian convolution factor.
Thus such a sequence cannot converge to the theta law. This is a
constraint on a possible cofinal construction, not a proof that a suitable
construction exists.
