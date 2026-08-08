# L-32411 — The true Q=4 physical current has vanishing relative Selberg-reserve cost

Claim ID: `L-32411`  
Title: Exact cancellation of the ordinary and local linear densities makes the correctly typed Q=4 prefix current `o(x)`, so its balanced physical square consumes a vanishing fraction of the Q=4 Selberg–Kummer reserve  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: corrected `L-32407`; `L-32404/L-32405`; classical PNT  
Scope: correctly typed centered-interval physical coordinate; no extra floor transform and no RH assumption

## 1. Correct physical coefficient and prefix

Retain the corrected source typing of `R-32403/L-32407`:

\[
 c_4=e_4*\Lambda_4,
 \qquad
 e_4(1)=1,
 \qquad
 e_4(4^r)=-3\ (r\ge1).
\]

The true physical prefix is

\[
 \boxed{
 G_4(x)=\sum_{m\le x}c_4(m).
 }
 \tag{L-32411.1}
\]

For an integer parent `n=j+k`, the RH-sensitive centered-interval current is

\[
 \boxed{
 Q_4^{\rm phys}(n,j)=G_4(n)-G_4(j)-G_4(k).
 }
 \tag{L-32411.2}
\]

No carry/floor transform is applied to `c_4` in this lemma.

## 2. Exact Q-adic prefix identity

Let

\[
 \Psi_4(x)=\sum_{m\le x}\Lambda_4(m).
\]

Since `c_4=e_4*Lambda_4`, ordinary prefix summation of the finite Dirichlet
convolution gives exactly

\[
 \boxed{
 G_4(x)=\Psi_4(x)-3\sum_{r\ge1}\Psi_4(x/4^r).
 }
 \tag{L-32411.3}
\]

Only finitely many terms occur for a fixed `x`.

By `L-32404.8`,

\[
 \Psi_4(x)=\psi(x)+D_4(x),
 \qquad
 D_4(x)=(\log4)\sum_{4^m\le x}(4^m-1).
 \tag{L-32411.4}
\]

Hence

\[
 G_4(x)=H_4(x)+L_4(x),
 \tag{L-32411.5}
\]

with

\[
 H_4(x)=\psi(x)-3\sum_{r\ge1}\psi(x/4^r)
 \tag{L-32411.6}
\]

and

\[
 L_4(x)=D_4(x)-3\sum_{r\ge1}D_4(x/4^r).
 \tag{L-32411.7}
\]

## 3. The local Euler tower collapses to logarithmic size

At the atom `4^m`, the coefficient of the local part (L-32411.7) is

\[
\begin{aligned}
&(\log4)\left[(4^m-1)
 -3\sum_{a=1}^{m-1}(4^{m-a}-1)\right]\\
&\qquad=3m\log4.
\end{aligned}
\]

Therefore

\[
 \boxed{
 L_4(x)=3\log4\sum_{1\le m\le\lfloor\log_4x\rfloor}m
 =O((\log x)^2).
 }
 \tag{L-32411.8}
\]

Thus the huge positive generalized-prime atoms on the powers of four cancel
exactly under the pole-killing Euler source before any absolute value is taken.

## 4. The ordinary linear density cancels exactly

The prime number theorem gives

\[
 \psi(y)=y+o(y).
 \tag{L-32411.9}
\]

The linear contribution to (L-32411.6) vanishes because

\[
 3\sum_{r\ge1}4^{-r}=1.
 \tag{L-32411.10}
\]

For completeness, fix `R`. For every fixed `r<=R`,

\[
 \psi(x/4^r)=x/4^r+o(x).
\]

For the tail `r>R`, a classical Chebyshev bound `psi(y)<<y` gives

\[
 \sum_{r>R}\psi(x/4^r)=O(x4^{-R}).
\]

Let first `x->infinity` and then `R->infinity`. Consequently

\[
 \boxed{H_4(x)=o(x).}
 \tag{L-32411.11}
\]

Combining with (L-32411.8),

\[
 \boxed{G_4(x)=o(x).}
 \tag{L-32411.12}
\]

This uses only the classical PNT and no estimate inside the critical strip.

## 5. Uniform balanced decay of the true physical field

Fix `0<eta<1/2`. Equation (L-32411.12) implies

\[
 \boxed{
 \sup_{\eta n\le j\le(1-\eta)n}
 \frac{|Q_4^{\rm phys}(n,j)|}{n}
 \longrightarrow0.
 }
 \tag{L-32411.13}
\]

Indeed, for every `epsilon>0`, all three arguments `n,j,k` in
(L-32411.2) exceed the PNT threshold once `n` is sufficiently large, and

\[
 |Q_4^{\rm phys}(n,j)|
 \le\epsilon(n+j+k)=2\epsilon n.
\]

For the quarter-balanced cone, `L-32405` gives cofinally

\[
 \mathcal R_4(n,j)
 >\frac1{20}P_4(n,j)^2,
 \qquad
 P_4(n,j)\ge\frac n4\log2.
\]

Therefore

\[
 \boxed{
 \sup_{n/4\le j\le3n/4}
 \frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
 \longrightarrow0.
 }
 \tag{L-32411.14}
\]

Equivalently, for every `delta>0` there is `N_delta` such that

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2
 \le\delta\,\mathcal R_4(n,j)
 }
 \tag{L-32411.15}
\]

for every `n>=N_delta` and every quarter-balanced `j`.

This strictly strengthens the fixed constant in corrected `L-32407` on the
cofinal tail while leaving its rigorous finite table untouched.

## 6. Normal-Gram consequence

For any finite nonnegative row measure supported on quarter-balanced parents at
least `N_delta`, summation of (L-32411.15) gives

\[
 \boxed{
 \sum\nu(n,j)|Q_4^{\rm phys}(n,j)|^2
 \le\delta\sum\nu(n,j)\mathcal R_4(n,j).
 }
 \tag{L-32411.16}
\]

Thus the **correctly typed pole-sensitive physical current** has arbitrarily
small relative charge against the source-matched Q=4 Kummer reserve on cofinal
balanced blocks.

The result is source-complete at one row: the Q-adic generalized-prime tower is
recombined before the PNT estimate, and no extra divisor/carry transform is
inserted.

## 7. Proof boundary

Closed here, subject to review:

1. exact prefix identity for the true physical coefficient;
2. exact collapse of the local Q=4 tower to `O(log^2 x)`;
3. PNT cancellation of the remaining linear density;
4. `G_4(x)=o(x)`;
5. uniform balanced physical-current decay;
6. vanishing current-to-Selberg-reserve ratio and its finite normal-Gram form.

Not closed here:

1. the independent-frequency reflected no-double-spend assembly placing the
   reserve with the required sign;
2. the coefficient-one neutral scattering recurrence;
3. RH.
