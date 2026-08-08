# L-30503 — Critical cutoff annulus profile and norm separation

Claim ID: `L-30503`  
Title: The first stopped critical boundary has a positive macroscopic annulus, forcing linear divisor-source atomic norm while retaining bounded local central variation  
Status: **PROPOSED COMPLETE ASYMPTOTIC LEMMA — DIRECTED CONSTANT GATE REPLAYED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #286 `L-28401/L-28402`; elementary eta/Hasse series and Möbius inversion on multiples  
Scope: first complete aggregate boundary; refutes the atomic-norm closure but does not lower-bound cycle-optimized debt

## 1. The complete first boundary

Put

\[
 f_N(x)=x^{-1/2}\log(N/x),
\]

using its analytic continuation for `x>N`.  For `q<=M=floor((N+1)/2)`, the difference between the infinite shifted central operator and the stopped finite operator is

\[
 \boxed{
 Q_N(q)=
 \sum_{2kq-1>N}f_N(2kq-1)
 -\sum_{(2k+1)q>N}f_N((2k+1)q).
 }
 \tag{L-30503.1}
\]

This is the same complete aggregate boundary denoted `b_X` in `L-30501`, up to the fixed sign convention used when the omitted tail is moved across the finite/infinite identity.

Fix

\[
 \frac{2N}{5}\le q\le\frac{4N}{9},
 \qquad r=\frac Nq\in\left[\frac94,\frac52\right].
 \tag{L-30503.2}
\]

Then the first omitted odd index is `1` and the first omitted shifted-even index is `2`. Hence

\[
 \boxed{
 \sqrt q\,Q_N(q)
 =-\phi_r(3)
 +\sum_{k\ge2}
  [\phi_r(2k-1/q)-\phi_r(2k+1)],
 }
 \tag{L-30503.3}
\]

where

\[
 \phi_r(x)=x^{-1/2}\log(r/x).
\]

## 2. Uniform limiting profile

The derivative satisfies, uniformly for `r in [9/4,5/2]` and `x>=3`,

\[
 |\phi_r'(x)|
 \le x^{-3/2}[1+\tfrac12\log x].
 \tag{L-30503.4}
\]

The right side is summable on the shifted even lattice. Therefore

\[
 \boxed{
 \sqrt q\,Q_N(q)=H(r)+O(1/q)
 }
 \tag{L-30503.5}
\]

uniformly on the complete annulus, where

\[
 H(r)=-\phi_r(3)+\sum_{k\ge2}[\phi_r(2k)-\phi_r(2k+1)].
 \tag{L-30503.6}
\]

More explicitly, if

\[
 P(s)=1-\eta(s)-2^{-s},
\]

then termwise differentiation of the convergent eta series gives

\[
 \boxed{
 H(r)=P(1/2)\log r+P'(1/2).
 }
 \tag{L-30503.7}
\]

The elementary majorant

\[
 \sum_{k\ge2}k^{-3/2}[1+\tfrac12\log(2k)]<6
\]

makes the error in (L-30503.5) at most `6/q`.

## 3. Directed positive moat

`X-30502` evaluates the globally convergent Hasse series

\[
 \eta(s)=\sum_{n\ge0}2^{-n-1}\Delta^n[(k+1)^{-s}]_{k=0}
\]

with rational square-root and logarithm enclosures.  It proves

\[
 \begin{aligned}
 P(1/2)&<0,\\
 H(5/2)&>\frac1{1000}.
 \end{aligned}
 \tag{L-30503.8}
\]

Because `P(1/2)<0`, `H(r)` is decreasing in `r`; hence

\[
 H(r)>\frac1{1000}
 \qquad(9/4\le r\le5/2).
 \tag{L-30503.9}
\]

For all sufficiently large `N`, every integer `q` in the annulus therefore satisfies

\[
 \boxed{
 Q_N(q)>\frac1{2000\sqrt q}.
 }
 \tag{L-30503.10}
\]

## 4. Linear atomic norm

Suppose the boundary load is represented on the next endpoint by an ordinary divisor source

\[
 Q_N(q)=\sum_{\substack{m\le M\\q\mid m}}\sigma_N(m).
 \tag{L-30503.11}
\]

Multiples-Möbius inversion makes `sigma_N` unique.  On the annulus one has `2q>M`, so no proper multiple of `q` occurs in (L-30503.11). Therefore

\[
 \boxed{
 \sigma_N(q)=Q_N(q)
 }
 \tag{L-30503.12}
\]

there.  Since the annulus contains at least `2N/45-2` integers,

\[
 \boxed{
 \sum_{m\le M}\sqrt m\,|\sigma_N(m)|
 \ge \frac{N}{50000}
 }
 \tag{L-30503.13}
\]

for all sufficiently large `N`.

This independently contradicts the polylogarithmic atomic-norm assertion in frozen PR #304 `L-30403/T-30401`.

## 5. The correct norm is not the atomic norm

The same calculation reveals why this obstruction does not automatically lower-bound Cycle Debt.  On a fixed ratio cell,

\[
 Q_N(q)=N^{-1/2}B(q/N)+O(N^{-3/2}),
 \qquad
 B(\theta)=\theta^{-1/2}H(1/\theta),
 \tag{L-30503.14}
\]

with a continuously differentiable profile. Consequently

\[
 \sum_{q\text{ in the annulus}}
 \sqrt q\,|Q_N(q+1)-Q_N(q)|=O(1).
 \tag{L-30503.15}
\]

Thus the boundary is macroscopic in the isolated divisor-source value norm but smooth in the first-difference coordinate used by central carry flows.  A viable repair must preserve this coupled flow structure and optimize in Pascal-cycle space before measuring negative capacity, exactly as stated in `L-30502`.

## 6. Proof boundary

Closed here:

1. the exact first-index formula on a macroscopic annulus;
2. the uniform eta profile and directed positive moat;
3. a linear lower bound for the unique divisor-source atomic norm;
4. bounded local first-difference variation of the same boundary.

Not closed here:

1. the global cycle-optimized boundary debt;
2. a repaired all-generation recurrence;
3. RH.
