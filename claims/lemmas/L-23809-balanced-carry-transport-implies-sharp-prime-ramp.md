# L-23809 — Balanced carry transport implies the sharp prime ramp

Claim ID: `L-23809`  
Title: Filling all but subpolynomial total carry capacity with balanced binomial splits gives `4 sqrt(X)-X^o(1)` prime-ramp mass  
Status: **PROPOSED EXACT CONDITIONAL THEOREM — BCT IS THE SOLE HINGE**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`, elementary divisor summation and Stirling bounds

## 1. Balanced carry transport

Fix once and for all

\[
 0<\eta<\frac12,
\]

for example `eta=1/4`.  Let

\[
 \mathcal B_\eta(X)
 =\{(n,j):2\le n\le X,\ \eta n\le j\le(1-\eta)n\}.
 \tag{L-23809.1}
\]

For a nonnegative split flow `d=(d_(n,j))` supported on
`B_eta(X)`, define its column load

\[
 L_q(d)=\sum_{(n,j)\in\mathcal B_\eta(X)}
 d_{n,j}\chi_{n,j}(q),
 \tag{L-23809.2}
\]

and total unused carry capacity

\[
 \boxed{
 \Delta_X(d)=\sum_{q=2}^{X}\bigl[w_X(q)-L_q(d)\bigr],}
 \tag{L-23809.3}
\]

where

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

The **balanced carry transport theorem**, abbreviated `BCT`, is:

> For every sufficiently large `X`, there exists `d_X>=0`, supported on
> `B_eta(X)`, such that
> \[
> L_q(d_X)\le w_X(q)\quad(2\le q\le X)
> \tag{L-23809.4}
> \]
> and
> \[
> \boxed{\Delta_X(d_X)=X^{o(1)}.}
> \tag{L-23809.5}
> \]

This is a finite fractional packing theorem.  It does not require a common
convolution profile, an exact triangular inverse, or pointwise positivity of a
Möbius sum.

## 2. The all-integer capacity has the correct main term

Elementary integral comparison gives

\[
 \boxed{
 \sum_{q=2}^{X}w_X(q)
 =4\sqrt X+O(\log X).}
 \tag{L-23809.6}
\]

Indeed

\[
 \int_1^Xx^{-1/2}\log(X/x)dx
 =4\sqrt X-2\log X-4,
\]

and the summand has bounded total endpoint variation at the required scale.

Thus `BCT` says that a positive balanced split flow consumes asymptotically all
of the elementary all-integer capacity.

## 3. Carry count and entropy differ by only `O(sqrt(n))`

Put

\[
 C(n,j)=\sum_{q=2}^{n}\chi_{n,j}(q).
 \tag{L-23809.7}
\]

Let

\[
 D(N)=\sum_{q=1}^{N}\left\lfloor\frac Nq\right\rfloor.
\]

The `q=1` defect vanishes, so exactly

\[
 C(n,j)=D(n)-D(j)-D(n-j).
 \tag{L-23809.8}
\]

Dirichlet's hyperbola decomposition gives the elementary uniform estimate

\[
 D(N)=N\log N+(2\gamma-1)N+O(\sqrt N).
 \tag{L-23809.9}
\]

The linear terms cancel in (L-23809.8), hence

\[
 C(n,j)=nH(j/n)+O(\sqrt n),
 \tag{L-23809.10}
\]

uniformly for `1<=j<n`.  Stirling's two-sided bounds give

\[
 \log\binom nj=nH(j/n)+O(\log(n+1)).
 \tag{L-23809.11}
\]

Therefore

\[
 \boxed{
 \left|\log\binom nj-C(n,j)\right|
 \le C_0\sqrt n}
 \tag{L-23809.12}
\]

for one absolute constant `C_0` and every split.

## 4. Balanced support makes the cumulative discretization loss polylogarithmic

If `(n,j)` is in `B_eta(X)`, then for every integer

\[
 \max(j,n-j)<q\le n
\]

both children are below `q`, while the parent is at least `q`.  Thus

\[
 \chi_{n,j}(q)=1.
\]

Consequently

\[
 \sum_{q=2}^{n}q^{-1/2}\chi_{n,j}(q)
 \ge c_\eta\sqrt n
 \tag{L-23809.13}
\]

for a constant `c_eta>0`.

For any feasible balanced flow,

\[
 \begin{aligned}
 c_\eta\sum_{n,j}d_{n,j}\sqrt n
 &\le\sum_{q=2}^{X}q^{-1/2}L_q(d)\\
 &\le\sum_{q=2}^{X}q^{-1/2}w_X(q)\\
 &=\sum_{q=2}^{X}\frac1q\log(X/q)
 =O((\log X)^2).
 \end{aligned}
 \tag{L-23809.14}
\]

Hence

\[
 \boxed{
 \sum_{n,j}d_{n,j}\sqrt n=O_\eta((\log X)^2).}
 \tag{L-23809.15}
\]

Combining (L-23809.12) and (L-23809.15),

\[
 \sum_{n,j}d_{n,j}\log\binom nj
 =\sum_{n,j}d_{n,j}C(n,j)+O_\eta((\log X)^2).
 \tag{L-23809.16}
\]

## 5. BCT gives the sharp entropy packing

Since every `chi` is nonnegative, finite summation gives

\[
 \sum_{n,j}d_{n,j}C(n,j)
 =\sum_{q=2}^{X}L_q(d).
 \tag{L-23809.17}
\]

For a `BCT` certificate, (L-23809.3), (L-23809.5), and (L-23809.6) now imply

\[
 \boxed{
 \sum_{n,j}d_{n,j}\log\binom nj
 \ge4\sqrt X-X^{o(1)}.}
 \tag{L-23809.18}
\]

Applying the exact atomized valuation and packing implication of `L-23808`,

\[
 \boxed{
 \sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac{X}{p^a}
 \ge4\sqrt X-X^{o(1)}.}
 \tag{L-23809.19}
\]

This is exactly the prime-ramp estimate consumed by the square-screw/Landau
transfer.

## 6. Finite LP dual

The maximum consumed capacity is the finite packing program

\[
 \max_{d\ge0}
 \sum_{(n,j)\in\mathcal B_\eta(X)}d_{n,j}C(n,j)
 \quad\text{subject to}\quad L_q(d)\le w_X(q).
 \tag{L-23809.20}
\]

Its dual is

\[
 \boxed{
 \begin{aligned}
 \min_{y_q\ge0}\quad&\sum_{q=2}^{X}w_X(q)y_q,\\
 \text{subject to}\quad&
 \sum_{q=2}^{n}y_q\chi_{n,j}(q)\ge C(n,j)
 \quad((n,j)\in\mathcal B_\eta(X)).
 \end{aligned}}
 \tag{L-23809.21}
\]

The constant vector `y_q=1` is feasible and has value `sum_q w_X(q)`.
Therefore `BCT` is equivalently the signed finite transport statement

\[
 \boxed{
 \sum_qw_X(q)y_q
 \ge\sum_qw_X(q)-X^{o(1)}
 \quad\text{for every dual-feasible }y.}
 \tag{L-23809.22}
\]

Writing `h_q=1-y_q`, dual feasibility becomes

\[
 \sum_qh_q\chi_{n,j}(q)\le0
 \quad\text{for every balanced split,}
 \tag{L-23809.23}
\]

and the conclusion is

\[
 \sum_qw_X(q)h_q\le X^{o(1)}.
 \tag{L-23809.24}
\]

This is a source-specific signed common-cell theorem.  It is the exact bridge
to reflected Selberg, balanced Type II, Farey/Mertens, and finite transport
methods.

## 7. Why the FGCM compactness obstruction does not apply verbatim

`BCT` allows the coefficient at scale `n` to depend on the full split `j/n` and
permits Pascal four-cycle transport.  It assumes neither log-translation
covariance nor a common scalar residual law.  Thus the scalar compactness
argument `FGCM -> GCF` does not identify a limiting independent convolution
factor for `BCT`.

This is a scope distinction, not a proof of logical strictness.  `BCT` remains a
deep RH-bearing finite theorem.

## 8. Proof boundary

Proved here:

- `BCT` implies a sharp entropy packing;
- the discretization error is only polylogarithmic;
- the sharp prime-ramp lower bound follows;
- the exact primal/dual formulations.

Open and load bearing:

- `BCT`, equation (L-23809.5).
