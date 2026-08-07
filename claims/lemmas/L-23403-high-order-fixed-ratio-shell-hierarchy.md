# L-23403 — High-order fixed-ratio shell hierarchy

Claim ID: `L-23403`  
Title: Every finite multiplicative difference is one compact zero-safe inverse-zeta window with explicit binomial shell weights, and its block energy remains RH-equivalent  
Status: **PROPOSED — COMPLETE FINITE-DIFFERENCE ALGEBRA AND TRANSFER PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: `L-23401`, `T-23401`; PR #233 `L-23202`  
Scope: every fixed integer order `m>=1`

## 1. Multiplicative differences

Fix `0<c<1` and define

\[
(T_cf)(x)=f(cx),
\qquad
\Delta_c=I-T_c.
\]

For an integer `m>=1`, put

\[
\boxed{
I_{c,m}(x)=\Delta_c^m M(x).}
\tag{L-23403.1}

Since `I_(c,1)=I_c`, one has

\[
I_{c,m}=\Delta_c^{m-1}I_c.
\]

Expanding gives the exact shell formula

\[
\boxed{
I_{c,m}(x)
=\sum_{r=0}^{m-1}
 (-1)^r{m-1\choose r}
 \bigl[M(c^rx)-M(c^{r+1}x)\bigr].}
\tag{L-23403.2}

Equivalently, if

\[
c^{r+1}x<n\le c^rx,
\qquad0\le r<m,
\]

then the coefficient of `mu(n)` in `I_(c,m)(x)` is exactly

\[
\boxed{
(-1)^r{m-1\choose r}.}
\tag{L-23403.3}

All integers below `c^m x` cancel by the full binomial identity.

## 2. Exact compact window

Put `L=log(1/c)` and define

\[
\boxed{
H_{c,m}(u)
=e^{-u/2}
\sum_{r=0}^{m-1}
 (-1)^r{m-1\choose r}
 {\bf1}_{[rL,(r+1)L)}(u).}
\tag{L-23403.4}

Then

\[
\boxed{
e^{-t/2}I_{c,m}(e^t)
=\sum_{n\ge1}{\mu(n)\over\sqrt n}
 H_{c,m}(t-\log n).}
\tag{L-23403.5}

The support is the fixed compact interval `[0,mL]`.

## 3. Transform and zero safety

Writing `s=z+1/2`, direct integration of the `m` shell pieces gives

\[
\begin{aligned}
\widehat H_{c,m}(z)
&={1-c^s\over s}
  \sum_{r=0}^{m-1}
  (-1)^r{m-1\choose r}c^{rs}\\
&=\boxed{{(1-c^s)^m\over s}.}
\end{aligned}
\tag{L-23403.6}

Therefore

\[
\boxed{
\int_1^\infty I_{c,m}(x)x^{-s-1}dx
={(1-c^s)^m\over s\zeta(s)},
\qquad\Re s>1.}
\tag{L-23403.7}

For every fixed finite `m`, all multiplier zeros satisfy `Re(s)=0`. No off-line zeta zero in `Re(s)>1/2` is canceled.

## 4. Fixed-order RH criterion

For any fixed `m>=1`, the following are equivalent:

1. RH;
2. for every `epsilon>0`,
   \[
   \int_1^X|I_{c,m}(x)|^2dx
   \ll_{\varepsilon,c,m}X^{2+\varepsilon};
   \tag{L-23403.8}
   \]
3. every fixed logarithmic block energy of the normalized signal in (L-23403.5) is `exp(o(J))`.

The proof is identical to `T-23401`: under RH, every finite difference of `M` has square-root size; conversely the Mellin integral is holomorphic in `Re(s)>1/2`, and the numerator in (L-23403.7) cannot cancel a zero there.

Thus increasing the finite-difference order does not weaken the arithmetic content. It only changes the exact boundary moments and packet geometry.

## 5. Binomial shell concentration

The coefficient vector in (L-23403.3) has

\[
\sum_{r=0}^{m-1}
\left|{m-1\choose r}\right|
=2^{m-1},
\]

and

\[
\sum_{r=0}^{m-1}{m-1\choose r}^2
={2m-2\choose m-1}.
\tag{L-23403.9}

For fixed `m`, these are scale-independent constants. For growing `m`, the central shells carry coefficients of order `2^m/\sqrt m`.

Consequently a high-order identity cannot be estimated shell by shell in total variation. Its signed binomial packet must be recombined before any norm inequality. This is the direct fixed-ratio version of the signed-packet rule in PRs #158 and #165.

## 6. Connection to boundary-safe smooth windows

The step-exponential window `H_(c,m)` is compact and zero-safe but only of bounded variation. It may be convolved with a compact spline factor whose transform has zeros only on `Re(z)=0`, and multiplied by finite boundary-difference factors with zeros only on `Re(z)=0` or `Re(z)=1/2`.

Such smoothing:

- preserves the open-strip zero-safe property;
- supplies arbitrary Euler regularity;
- gives the half-pole moments used by the terminal closures of PR #165;
- remains a finite signed combination of translates of the same shell signal.

It does not by itself prove the balanced shell-energy bound.

## 7. Proof boundary

Closed exactly:

- the shell-binomial formula;
- the compact window representation;
- the transform and zero set;
- the fixed-order RH equivalence;
- the coefficient-growth audit.

Open:

- a uniform high-order signed energy estimate;
- the balanced Möbius core;
- RH.
