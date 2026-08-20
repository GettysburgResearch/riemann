# Two canonical routes after the latest hostile audits

**Scientific status:** exact reductions and new interface theorems.  
**The Riemann Hypothesis remains unproved.**

## Route A: actual-prime activation drift

Let

\[
e(y)=\sum_A(-1)^{|A|}q_A^{-3/2}f(y/q_A),
\qquad
f(v)=\begin{cases}16,&v<1,\\24v^{-1/2}-9v^{-1},&v\ge1.\end{cases}
\]

For the hereditary product-threshold ideal `q_A<=y`, put

\[
S_{3/2}(y)=\sum_{q_A\le y}(-1)^{|A|}q_A^{-3/2}.
\]

The total labelled activity is below one.  Removing a label gives
`jM_j<=RM_(j-1)`, hence every odd level is smaller than the preceding even
level and `S_(3/2)>0`.  Conversely, map each nonempty even set to the odd parent
obtained by removing its largest label.  Every parent's total preimage mass is
less than `R` times its own mass, proving

\[
\boxed{0<S_{3/2}(y)\le1.}
\]

Each activation changes its carrier from `16` to `15`; summing those jumps and
using the open-cell derivative gives

\[
\boxed{
 e(y)=16\Delta_{3/2}-S_{3/2}(y)
 -3\int_1^y[4\sqrt tS_1(t)-3S_{1/2}(t)]\frac{dt}{t^2}.
}
\]

The discontinuous activation ledger is therefore complete.  The stronger
pointwise gate is

\[
3\int_1^y[4\sqrt tS_1(t)-3S_{1/2}(t)]\frac{dt}{t^2}
\le16\Delta_{3/2}-S_{3/2}(y).
\]

This is `CDTG100320`; it implies global envelope positivity and RH.  The exact
one-sided quantity required by Landau is PR #685's cell-deficit sum
`CATD100300`, proved there RH-equivalent.  PR #684's adaptive squaring is a
local producer for the continuous drift, not a positive desmoothing theorem.

## Route B: primitive ratio-eight wavelet

For the minimal kernel `K_0`, Cauchy phase integration gives

\[
Q_X=\sum_{m,n}\mu(m)\mu(n)\sqrt{mn}
\frac{\min(m,n)}{\max(m,n)}K_0(X/m)K_0(X/n).
\]

After integrating in `X`, only `1<=n/m<=8` survives.  For `sigma>3/2`,

\[
\kappa_\sigma(r)=r^{-1/2}\int_r^8
K_0(u)K_0(u/r)u^{-2\sigma-1}du
\]

and

\[
\mathcal E(\sigma)=\kappa_\sigma(1)
\sum_m\frac{\mu(m)^2}{m^{2\sigma-1}}
+2\sum_{m<n\le8m}\mu(m)\mu(n)m^{1-2\sigma}
\kappa_\sigma(n/m).
\]

Writing `m=da,n=db`, `(a,b)=1`, removes the common sign:

\[
\mu(m)\mu(n)=\mu(a)\mu(b),
\]

and the common core is the positive factor

\[
\boxed{
\mathcal G_{a,b}(\sigma)=
\frac{\zeta(2\sigma-1)}{\zeta(4\sigma-2)}
\prod_{p\mid ab}(1+p^{1-2\sigma})^{-1}.
}
\]

All remaining sign is one primitive coprime-ratio correlation on
`1<b/a<=8`.  Physical convergence for every `sigma>1` is `PRBC100330`.
Because PR #675 proves that the wavelet energy abscissa is
`Theta+1/2`,

\[
\boxed{\mathrm{PRBC100330}\iff RH.}
\]

PR #685's zero-moment Vaughan decomposition provides another exact coordinate
for the same terminal cancellation: all Type-I terms are closed and only the
balanced trilinear `BVD100310` remains.

## Standalone rank-one recurrence firewall

For

\[
A_N=\sum_{n\le N}\frac{\beta(n)}n,
\quad B_N=\sum_{n\le N}\frac{\beta(n)}{\sqrt n},
\quad C_N=3B_N-4\sqrt N A_N,
\]

direct substitution gives

\[
\boxed{
C_{N+1}=C_N-\frac{\beta(N+1)}{\sqrt{N+1}}
-4(\sqrt{N+1}-\sqrt N)A_N.
}
\]

The simultaneous jump of `A_N` changes the isolated `+3` contribution to
`3-4=-1`.  This is retained only as an algebraic mutation firewall.

## Exact boundary

```text
CATD100300     open / RH-equivalent
CDTG100320     open / sufficient for RH
BVD100310      open / RH-equivalent
PRBC100330     open / RH-equivalent
RH             unproved
```
