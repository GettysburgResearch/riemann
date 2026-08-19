# A canonical scalar/native-source proof spine for the Riemann Hypothesis

## Abstract

We synthesize the strongest surviving conclusion-facing chain in the live
repository after the native-coefficient audits. The analytic consumer is one
factor-67 scalar with a zero-safe reciprocal-zeta Mellin transform. The exact
arithmetic source is represented both by sequential first ownership and by a
new symmetric random-order Euler homotopy. A second new construction introduces
a half-order tilt under which the scalar has, simultaneously, a positive
inverse renewal and a positive prime-power owner evolution. This gives an
exact positive-work majorant for its negative part and a logarithmic integrated
coefficient-energy budget.

The synthesis removes Hall, Volterra, score, capacity, terminal, prime-square,
and row-selection interfaces from the conclusion. It also proves that three
seemingly natural completions are invalid: contracted alpha children lose the
native coefficient, ordinary owner-martingale variance is degenerate on
squarefree fibres, and absolutely subcritical positive Euler smoothing cancels
the reciprocal-zeta poles. The remaining theorem is an explicit
source-root/boundary Carleson estimate `TOCE67`. We prove
`TOCE67 => RH`; we do not prove `TOCE67` or RH.

## 1. Scalar analytic spine

Let

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

and

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\]

The Dirichlet series of `beta` is `(1-67^-z)/zeta(z)`. The Mellin transform of
`T` is `(s+3/2)/(s(s-1/2))`. Absolute Fubini in `Re s>1/2` gives

\[
\widehat h(s)=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\]

The apparent singularity at `s=1/2` is removable because `1/zeta(s+1/2)`
vanishes there. The continuation is analytic for positive real `s`. At a
zero `rho` with `Re rho>1/2`, the factor `1-67^-rho` is nonzero because its
second term has modulus below one. Thus every such zero gives a genuine pole
at `s=rho-1/2`.

If the logarithmic negative mass of `h` is subpower, the Mellin transform of
`h_-` is holomorphic in `Re s>0`. The transform of the nonnegative density
`h_+` is then `widehat h + widehat h_-`; it retains every off-line pole and has
no positive-real singularity. Landau's theorem gives a contradiction.
Functional-equation symmetry completes RH. The same conclusion follows from
an eventually nonnegative multiplicative box smoothing, whose multiplier
`(1-A^-s)/s` is zero-free for `Re s>0`.

## 2. Native coefficient preservation

For commuting shifts `U_i` and activities `r_i=p_i^-1/2`, the literal rough
Euler source is

\[
F=\prod_i(I-r_iU_i).
\]

The exact sequential first-owner decomposition is

\[
F=s_kI+\sum_i\lambda_i(I-U_i)
\prod_{j>i}(I-r_jU_j).
\]

Every current retains the complete future Euler profile. This is the
coefficient-exact repair of the alpha-child mismatch.

To remove order dependence, define

\[
K_{j,t}=(1-tr_j)I-(1-t)r_jU_j.
\]

Differentiating `G_t=prod_j K_(j,t)` and integrating between `G_0=F` and
`G_1=sI` yields

\[
F=sI+\int_0^1\sum_i r_i(I-U_i)
\prod_{j\ne i}K_{j,t}\,dt.
\]

This is the average of sequential first ownership over independent random
prime priorities. It weakens the sign requirement from every ordering to one
aggregate native current without changing any coefficient.

## 3. Tilted positive renewal

The positive inverse of `beta` is

\[
g(n)=v_{67}(n)+1,
\qquad beta*g=epsilon.
\]

For `tau>=0`, define

\[
h_\tau(x)=\sum_{n\le x}
\frac{\beta(n)}{n^{\tau+1/2}}T(x/n).
\]

Because simultaneous coefficient tilting commutes with Dirichlet convolution,

\[
T(x)=\sum_{d\le x}
\frac{g(d)}{d^{\tau+1/2}}h_\tau(x/d).
\]

The logarithmic derivative of `G(z)=zeta(z)/(1-67^-z)` supplies a positive
generalized von Mangoldt function `Lambda_g`, with the 67 prime-power channel
doubled. Coefficient comparison gives

\[
beta(n)\log n=-\sum_{q\mid n}\Lambda_g(q)beta(n/q).
\]

Differentiating the finite tilted scalar therefore yields

\[
\partial_\tau h_\tau(x)=
\sum_{q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}h_\tau(x/q).
\]

Since `h_tau(x)->T(x)` as `tau->infinity`, integration gives

\[
T(x)-h(x)=\int_0^\infty\sum_{q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}h_\tau(x/q)d\tau.
\]

Taking positive and negative parts of the integrand gives

\[
h_-(x)\le[\mathcal W_+(x)-T(x)]_+,
\]

where

\[
\mathcal W_+(x)=\int_0^\infty\sum_{q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}
(h_\tau(x/q))_+d\tau.
\]

Thus the source-faithful theorem

\[
\int_1^X[\mathcal W_+(x)-T(x)]_+\frac{dx}{x}=X^{o(1)}
\]

implies subpower negative mass and hence RH.

## 4. Critical energy and the parity firewall

The complete tilt coefficient energy satisfies

\[
\int_0^\infty\sum_{2\le n\le X}
\frac{\beta(n)^2}{g(n)n^{1+2\tau}}d\tau
\le2+\log\log X.
\]

This is the exact critical budget available to a Carleson argument. It does
not close the theorem by itself. On squarefree integers coprime to 67,
`beta/g=mu` has modulus one and the alternating owner martingale is constant
along every descending trajectory. Its within-chain quadratic variation is
zero. Cancellation must therefore occur across source roots and boundary
scales, not inside one owner chain.

## 5. Why positive absolute completion cannot work

A positive Euler smoothing

\[
G_\theta(z)=\prod_p(1-\theta_pp^{-z})^{-1}
\]

with summable residual activities `1-theta_p` satisfies

\[
G_\theta(z)/\zeta(z)
=
\prod_p\frac{1-p^{-z}}{1-\theta_pp^{-z}},
\]

which is holomorphic and zero-free in the corresponding half-plane. It
therefore cancels every zeta-zero pole of the reciprocal witness. The missing
critical estimate cannot be replaced by an absolutely convergent positive
Euler completion.

## 6. Final theorem ledger

```text
factor-67 scalar transform                     proved
zero-free smoothing / negative-mass consumer   proved
native sequential first ownership              proved
symmetric random-order Euler homotopy           proved
tilted positive inverse renewal                proved
tilted prime-power owner flow                  proved
positive-work domination of h_-                 proved
integrated critical tilt energy O(log log X)    proved
ordinary Doob-to-sign shortcut                  refuted
absolute positive Euler completion              refuted
TOCE67 source-root/boundary embedding           open
Riemann Hypothesis                              unproved
```

The proof has been compressed to one open quantitative statement. That
statement is conclusion-producing and cannot honestly be renamed as a lemma
already supplied by the repository.
