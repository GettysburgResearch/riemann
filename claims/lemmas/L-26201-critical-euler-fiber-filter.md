# L-26201 — Critical Euler-fiber filter for the carry Green source

Claim ID: `L-26201`  
Status: `PROPOSED COMPLETE — exact transform, finite-source, and distributional algebra pending independent review`  
Scope: bridge between the continuum carry inverse, fixed-ratio Möbius shells, and reflected sources  
Date: 2026-08-08  
Depends on: PR #243 `L-23602` at `225c5e3d231ac23b6f487cd43e0dc89d48d3db1c`; PR #234 `L-23401/L-23405` at `2d5043070e15fe6be94307381f4023eaa48c17a5`

## 1. The carry Green kernel

Put

\[
h=\log 2
\]

and let `tau` denote right translation by `h` on causal distributions:

\[
(\tau f)(t)=f(t-h),
\qquad f(t)=0\quad(t<0).
\tag{L-26201.1}
\]

Its Laplace multiplier is

\[
\mathcal L(\tau f)(s)=2^{-s}\widehat f(s).
\tag{L-26201.2}
\]

The logarithmic carry Green kernel from `L-23602` is

\[
\boxed{
H(t)=
\left(
8e^t-7e^{t/2}-\frac32t e^{t/2}
\right)\mathbf 1_{t\ge0}.}
\tag{L-26201.3}
\]

For `Re s>1`, direct integration gives

\[
\begin{aligned}
\widehat H(s)
&=\frac8{s-1}-\frac7{s-1/2}-\frac{3/2}{(s-1/2)^2}\\
&=\boxed{
\frac{s(s+1)}{(s-1)(s-1/2)^2}.}
\end{aligned}
\tag{L-26201.4}
\]

Thus the three continuous models in the carry Green kernel are exactly

```text
e^t,

e^(t/2),

t e^(t/2).
```

They are the pole model and the double half-pole model that defeated the undifferenced conditional-Hankel proposal.

## 2. One fixed annihilating Euler fiber

Define

\[
\boxed{
\mathcal E
=(I-2\tau)(I-\sqrt2\,\tau)^2.}
\tag{L-26201.5}
\]

Its Laplace multiplier is

\[
\boxed{
P(s)
=(1-2^{1-s})(1-2^{1/2-s})^2.}
\tag{L-26201.6}
\]

The factor `I-2 tau` annihilates `e^t`.  The double factor
`(I-sqrt(2) tau)^2` annihilates both `e^(t/2)` and `t e^(t/2)`.  Consequently

\[
\boxed{
\mathcal E H(t)=0
\qquad(t\ge3\log2),}
\tag{L-26201.7}
\]

apart from the distributional endpoint structure already included in the causal translation convention.

This is a fixed-order identity.  It does not use a moving packet order, a bounded-rank assertion, or an asymptotic face count.

## 3. Positive compact Green factor

For `alpha in {1,1/2}`, put

\[
u_\alpha(t)=e^{\alpha t}\mathbf 1_{0\le t\le h}.
\tag{L-26201.8}
\]

Then

\[
\widehat u_\alpha(s)
=\frac{1-2^{\alpha-s}}{s-\alpha}.
\tag{L-26201.9}
\]

Define the compact convolution

\[
\boxed{
W=u_1*u_{1/2}*u_{1/2}.}
\tag{L-26201.10}
\]

It satisfies

\[
W(t)\ge0,
\qquad
\operatorname{supp}W\subset[0,3\log2],
\tag{L-26201.11}
\]

and

\[
\widehat W(s)
=rac{1-2^{1-s}}{s-1}
\left(
\frac{1-2^{1/2-s}}{s-1/2}
\right)^2.
\tag{L-26201.12}
\]

Combining (L-26201.4), (L-26201.6), and (L-26201.12) gives the exact factorization

\[
\boxed{
P(s)\widehat H(s)=s(s+1)\widehat W(s).}
\tag{L-26201.13}
\]

Therefore, as causal distributions,

\[
\boxed{
\mathcal E H=(\partial_t^2+\partial_t)W.}
\tag{L-26201.14}
\]

This is the first load-bearing connection:

```text
failed carry Green spline
--fixed critical Euler fiber-->
second derivative of one nonnegative compact window.
```

The negative Hankel determinant in the frozen PR #243 argument is not being ignored.  Its offending half-pole terms have been annihilated before a positivity statement is requested.

## 4. Exact source identity

Define the continuum carry source in logarithmic coordinates by

\[
\boxed{
\mathscr C(t)
=\sum_{n\ge1}\mu(n)H(t-\log n).}
\tag{L-26201.15}
\]

Every sum is finite at fixed `t`, and

\[
\mathscr C(\log y)=\sqrt y\,\mathfrak C(y)
\]

for the profile `mathfrak C` of `L-23602`.

Put

\[
\boxed{
\mathscr Y(t)
=\sum_{n\ge1}\mu(n)W(t-\log n).}
\tag{L-26201.16}
\]

Then (L-26201.14) gives

\[
\boxed{
\mathcal E\mathscr C
=(\partial_t^2+\partial_t)\mathscr Y.}
\tag{L-26201.17}
\]

Thus the Euler-filtered carry state and one compact fixed-ratio Möbius-window signal are the same source in two explicit Green gauges.

## 5. Moving the filter to the arithmetic source

Expanding (L-26201.6) as a polynomial in `2^(-s)` gives

\[
P(s)
=1-(2+2\sqrt2)2^{-s}
 +(2+4\sqrt2)4^{-s}
 -4\,8^{-s}.
\tag{L-26201.18}
\]

Define

\[
\boxed{
\begin{aligned}
b_{\mathcal E}(n)
={}&\mu(n)
 -(2+2\sqrt2)\mathbf1_{2\mid n}\mu(n/2)\\
&+(2+4\sqrt2)\mathbf1_{4\mid n}\mu(n/4)
 -4\mathbf1_{8\mid n}\mu(n/8).
\end{aligned}}
\tag{L-26201.19}
\]

Then

\[
\boxed{
\sum_{n\ge1}\frac{b_{\mathcal E}(n)}{n^s}
=\frac{P(s)}{\zeta(s)},
\qquad \Re s>1,}
\tag{L-26201.20}
\]

and finite reindexing gives

\[
\boxed{
\mathcal E\mathscr C(t)
=\sum_{n\ge1}b_{\mathcal E}(n)H(t-\log n).}
\tag{L-26201.21}
\]

Its summatory function is the explicit four-scale fiber

\[
\boxed{
\begin{aligned}
B_{\mathcal E}(x)
={}&M(x)
 -(2+2\sqrt2)M(x/2)\\
&+(2+4\sqrt2)M(x/4)
 -4M(x/8).
\end{aligned}}
\tag{L-26201.22}
\]

For odd `n`,

\[
\boxed{b_{\mathcal E}(n)=\mu(n).}
\tag{L-26201.23}
\]

Hence the filter does not silently delete the same-sign odd Möbius cubes of the PR #239 mutation.  It adds one fixed dyadic fiber around them.

## 6. Fixed-ratio and RH scope

The zeros of `P(s)` lie only on the two boundary lines

\[
\Re s=1,
\qquad
\Re s=\frac12.
\tag{L-26201.24}
\]

Therefore

\[
P(s)\ne0
\qquad
\left(\frac12<\Re s<1\right).
\tag{L-26201.25}
\]

Every hypothetical off-line zero of `zeta` remains an uncancelled pole of
`P(s)/zeta(s)`.  Consequently the following are equivalent, subject only to the standard block-Laplace argument already used for the fixed-ratio shell on PR #234:

\[
\mathrm{RH},
\tag{L-26201.26}
\]

\[
B_{\mathcal E}(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad(\varepsilon>0),
\tag{L-26201.27}
\]

and, for any fixed `L>0`,

\[
\boxed{
\int_J^{J+L}e^{-t}
\left|B_{\mathcal E}(e^t)\right|^2dt
=e^{o(J)}.}
\tag{L-26201.28}
\]

Likewise the compact signal `mathscr Y` is RH-equivalent, because its transform is `widehat W(s)/zeta(s)` and `widehat W` has no zero in the open critical strip.

## 7. Proof boundary

Closed in this claim:

- exact annihilation of the pole and double half-pole Green modes;
- positive compact factor `W`;
- exact source/filter transference;
- the four-scale Mertens fiber;
- preservation of every off-line pole and of the odd Möbius-cube firewall.

Not closed:

- a subexponential block bound for `B_E` or `mathscr Y`;
- a reflected forcing estimate for the new source;
- RH.
