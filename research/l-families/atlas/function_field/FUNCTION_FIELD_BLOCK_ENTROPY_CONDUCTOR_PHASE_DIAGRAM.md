# Closed-place block entropy versus conductor: the all-rank phase diagram

Status: **exact ambient squarefree order-statistic theorem and conditional
conductor-loss optimization; no transfer to the frozen weighted FFPS source,
relative-complex construction, signed trace estimate, individualization, RH,
or GRH**

Bounded replay:
[`function_field_block_entropy_conductor_phase_diagram.py`](function_field_block_entropy_conductor_phase_diagram.py).

## 0. Outcome

The growing closed-place construction has a scale-free obstruction.  It is
not peculiar to the earlier choice `r=alpha log n`, and dividing the rank
among many bands does not change it.

Let `F` be uniformly distributed among monic squarefree degree-`n`
polynomials over `F_q`, with `q` odd.  Let `E` be the closed places whose
residue field supports the quadratic orientation on
`k_v^times/{+-1}`.  Their logarithmic density is

\[
 \delta=
 \begin{cases}
 1,&q=1\pmod4,\\
 1/2,&q=3\pmod4.
 \end{cases}
\tag{0.1}
\]

Write `d_(r)(F)` for the degree of the `r`-th smallest distinct eligible
factor, with value infinity if it does not exist.  If

\[
 r=r(n)\longrightarrow\infty,
 \qquad r=o(\log n),
\tag{0.2}
\]

then

\[
 \boxed{
 {\log d_{(r)}(F)\over r}
 \ \xrightarrow{\Pr}\ {1\over\delta}.}
\tag{0.3}
\]

At the same time, the ambient probability of having fewer than `r`
eligible factors is

\[
 \Pr(\omega_E(F)<r)\le n^{-\delta+o(1)}.
\tag{0.4}
\]

Thus supply is abundant, but its order statistic is exponentially expensive
in rank:

\[
 d_{(r)}=\exp((1/\delta+o_{\Pr}(1))r).
\tag{0.5}
\]

The formal hard-block leverage is `exp(-a r)`, where

\[
 a=\log(5/4).
\]

If a trace theorem loses a factor `d_(r)^theta`, its net rank exponent is

\[
 \boxed{a-{\theta\over\delta}.}
\tag{0.6}
\]

Consequently a growing-rank gain is possible in this model exactly below

\[
 \boxed{\theta<\delta\log(5/4).}
\tag{0.7}
\]

The thresholds are only `0.223143...` for `q=1 mod 4` and `0.111571...`
for `q=3 mod 4`.  A linear or square-root dependence on the largest branch
degree loses decisively.  The live escape is an exact cancellation of the
large-degree constituents inside a joint relative complex *before* a
modewise conductor is paid.

Equation (0.3) is an ambient squarefree theorem.  The weighted-source
firewall proves that it cannot be silently transferred through the frozen
FFPS Boolean/depth observation.  That requires the separate
`FFPS-RICH-CARLESON(alpha)` gate.

## 1. Exact first and second moments of the truncated factor count

Let

\[
 X_D(F)=\#\{P\mid F:P\in E,\ \deg P\le D\}.
\tag{1.1}
\]

The squarefree generating series is rational:

\[
 S(u)=\prod_P(1+u^{\deg P})={1-qu^2\over1-qu}.
\tag{1.2}
\]

For a squarefree product `A` of at most two distinct primes, put
`a=deg A`.  The generating series for squarefree multiples of `A` is

\[
 u^aS(u)\prod_{P\mid A}(1+u^{\deg P})^{-1}.
\tag{1.3}
\]

Move the pole at `u=1/q` explicitly and bound the remaining coefficient on
`|u|=q^(-1/2)`.  Uniformly for such `A`,

\[
 \Pr(A\mid F)
 =\prod_{P\mid A}{1\over |P|+1}
 +O_q\!\left(q^{-(n+a)/2}\right).
\tag{1.4}
\]

Only one- and two-prime cases are needed, so the inverse factors in (1.3)
are uniformly bounded on that circle.  Summing (1.4), using

\[
 I_q(d)={q^d\over d}+O_q(q^{d/2}/d),
\]

gives, whenever `D=o(n)`,

\[
 \boxed{
 \mathbb E X_D=\delta\log D+O_q(1),\qquad
 \operatorname{Var}X_D=\delta\log D+O_q(1)+o(1).}
\tag{1.5}
\]

Indeed, the main two-prime term in (1.4) is the product of the one-prime
terms, so it cancels from the covariance.  The sum of all pair errors is
`O_q(q^(D-n/2))`; the diagonal square-probability sum converges.  Eligible
degrees are all degrees in the first case of (0.1), and exactly the even
degrees in the second, producing the coefficient `delta`.

## 2. Proof of the order-statistic law

Fix `epsilon>0` and set

\[
 D_\pm=\left\lfloor
 \exp\left({(1\pm\epsilon)r\over\delta}\right)
 \right\rfloor.
\tag{2.1}
\]

Under (0.2), both cutoffs are `n^o(1)`, so (1.5) applies.  Their means are
`(1+-epsilon)r+O_q(1)` and their variances are `O(r)`.  Chebyshev therefore
gives

\[
 \Pr(X_{D_-}\ge r)+\Pr(X_{D_+}<r)=O_{q,\epsilon}(1/r).
\tag{2.2}
\]

Except on that event,

\[
 D_-<d_{(r)}\le D_+,
\]

which proves (0.3).

For (0.4), use the full bivariate squarefree Euler product.  For each fixed
`0<t<1`, coefficient transfer gives

\[
 \mathbb E[t^{\omega_E(F)}]\ll_{q,t}n^{\delta(t-1)}.
\tag{2.3}
\]

On `omega_E(F)<r`, `1<=t^{-(r-1)}t^omega`.  Since `r=o(log n)`, the
factor `t^(-r)` is `n^o(1)`.  Taking fixed `t` arbitrarily close to zero
proves (0.4) in the standard `n^(-delta+o(1))` upper-bound sense.

This separation is important:

- almost every ambient core has `r` eligible factors;
- nevertheless the final required factor has degree `exp(r/delta)`;
- and the frozen FFPS source measure is not the ambient measure.

## 3. Every natural rank schedule has the same threshold

The exact two-place block factor is below `4/5`, hence

\[
 L_r<(4/5)^r=e^{-ar}.
\tag{3.1}
\]

Suppose only for this exponent ledger that the surviving relative trace
costs at most a power `d_(r)^theta`.  Equation (0.3) makes the product

\[
 d_{(r)}^\theta L_r
 =\exp\left[-\left(a-{\theta\over\delta}
 +o_{\Pr}(1)\right)r\right].
\tag{3.2}
\]

This proves (0.6)--(0.7).  Two useful schedules are:

### 3.1 Sublogarithmic rank

For `r=kappa log log n`,

\[
\begin{aligned}
 d_{(r)}&=(\log n)^{\kappa/\delta+o_{\Pr}(1)},\\
 L_r&=(\log n)^{-\kappa\log(5/4)+o(1)},\\
 d_{(r)}^\theta L_r
 &=(\log n)^{-\kappa(\log(5/4)-\theta/\delta)+o_{\Pr}(1)}.
\end{aligned}
\tag{3.3}

The poor-core ambient error in (0.4) is much smaller than this polylogarithmic
gain.  But a source-weighted Carleson theorem and a relative trace estimate
are still missing.

### 3.2 Power rank

For `r=alpha log n`, the earlier one-sided supply theorem gives

\[
 d_{(r)}\ge n^{\alpha/\delta-o_{\Pr}(1)},
\tag{3.4}
\]

while the ambient poor-core exponent is

\[
 c_\delta(\alpha)
 =\delta-\alpha+\alpha\log(\alpha/\delta).
\tag{3.5}

Conditional on a source transfer and a `d^theta` relative trace loss, the
best exponent available from this two-term ledger is

\[
 \min\left\{
 c_\delta(\alpha),
 \alpha\left(\log(5/4)-{\theta\over\delta}\right)
 \right\}.
\tag{3.6}

If `theta<delta log(5/4)`, the optimum is the unique crossing.  Put

\[
 b=\log(5/4)-\theta/\delta,
 \qquad x=\alpha/\delta.
\]

Then `x` is the unique root in `(0,1)` of

\[
 1-x+x\log x=bx.
\tag{3.7}

Equivalently,

\[
 x=-{1\over W_{-1}(-e^{-(1+b)})}.
\tag{3.8}

The optimized exponent is `delta*x*b`.  At `theta=0`, this recovers exactly
the previously found panels

\[
\begin{array}{c|c|c}
\delta&\alpha_*&\text{exponent}\\ \hline
1/2&0.274064461784&0.061155717291\\
1&0.548128923568&0.122311434583.
\end{array}
\tag{3.9}

As `theta` approaches the threshold in (0.7), the optimized exponent tends
to zero.  Above it, increasing rank only worsens the conductor ledger.

## 4. Why multiscale banding does not alter the theorem

The multiscale single-square theorem classifies the obvious workaround.
If ranks `r_1,...,r_J` in disjoint degree bands are kept coherent until one
square, their quotient is exactly

\[
 C_2^{r_1+\cdots+r_J}.
\]

The product leverage survives, but so do all cross-band characters; for
bounded band rank their fraction tends to one.  The largest selected degree
and the threshold (0.7) remain.

If instead the bands are squared separately, multiplying the inequalities
creates a `2J`-th moment.  Taking the `J`-th root to return to a quadratic
scale retains only the geometric-mean leverage, not the product leverage.

Thus the scale-free conclusion is:

\[
\boxed{
 \text{banding cannot trade branch entropy for quadratic leverage.}}
\tag{4.1}

The only currently visible escape is a genuinely joint virtual complex in
which the common high-degree inertia constituents cancel before the trace
theorem measures conductor.

## 5. Interpretation and theorem ledger

Proved for ambient squarefree polynomial cores:

- the one/two-prime divisibility estimate (1.4);
- the truncated mean and variance (1.5);
- the sublogarithmic order-statistic law (0.3);
- the ambient abundance estimate (0.4).

Exact algebra or conditional exponent bookkeeping:

- block leverage `exp(-r log(5/4))` from the hard Gram theorem;
- the universal conductor threshold (0.7), conditional on a
  `d_(r)^theta` trace loss;
- the optimized power-rank crossing (3.6)--(3.9);
- the multiscale no-escape conclusion from the joint-quotient theorem.

Not proved:

- `FFPS-RICH-CARLESON(alpha)` for the frozen Boolean/depth source;
- a relative sheaf whose large-degree local inertia cancels;
- a uniform varying-place Frobenius trace bound;
- `CYSEL`, `WCADD`, `WCKUM`, principal-member individualization;
- RH or GRH.

The packet changes the next experimental question.  The useful target is no
longer “find more short places.”  It is:

\[
\boxed{
 \text{compute the local inertia class of hard minus selected and decide
 whether its degree-}d\text{ branch cancels in }K_0.}
\]
