# L-20812 — Finite Euler Riccati strip flow

Claim ID: `L-20812`  
Title: The shifted-prefix energy is a positive local Euler flow minus one explicit first-omitted-power defect  
Status: `PROPOSED — COMPLETE FINITE EULER-FACTOR AND STRIP-FLOW IDENTITIES`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Dependencies: `L-20811`; `T-20803`; finite geometric sums  
Scope: proof-facing decomposition of the shrinking-strip criterion  
Related counterexample candidates: none

## 1. Local truncated Euler factor

Fix a base prime `p`, an integer `K>=1`, and an offset `u>=0`. Put

\[
 a=\log p,
 \qquad s={1\over2}+u,
 \qquad r=p^{-s}\in(0,1).
 \tag{L-20812.1}
\]

Define the truncated local logarithmic-derivative and its first `s`-derivative
moment by

\[
 \boxed{
 P_{p,K}(u)=a\sum_{k=1}^K r^k,}
 \tag{L-20812.2}
\]

and

\[
 \boxed{
 Q_{p,K}(u)=a^2\sum_{k=1}^K k r^k
 =-\partial_uP_{p,K}(u).}
 \tag{L-20812.3}
\]

The finite geometric sums satisfy the exact Riccati identity

\[
 \boxed{
 Q_{p,K}(u)
 =P_{p,K}(u)^2+aP_{p,K}(u)-E_{p,K}(u),}
 \tag{L-20812.4}
\]

where the cutoff defect is

\[
 \boxed{
 E_{p,K}(u)
 =a^2r^{K+1}
  \sum_{m=0}^{K-1}(K-m)r^m
 \ge0.}
 \tag{L-20812.5}
\]

Equivalently,

\[
 E_{p,K}(u)
 =a^2{r^{K+1}\over(1-r)^2}
  [K-(K+1)r+r^{K+1}].
 \tag{L-20812.6}
\]

### Proof

Let

\[
 S_K=\sum_{k=1}^Kr^k,
 \qquad T_K=\sum_{k=1}^Kkr^k.
\]

Direct summation gives

\[
 S_K+S_K^2-T_K
 ={r^{K+1}\over(1-r)^2}
 [K-(K+1)r+r^{K+1}].
 \tag{L-20812.7}
\]

The bracket factors as

\[
 K-(K+1)r+r^{K+1}
 =(1-r)^2\sum_{m=0}^{K-1}(K-m)r^m,
 \tag{L-20812.8}
\]

so it is positive. Multiplication by `a^2` proves
(L-20812.4)--(L-20812.6). QED.

The elementary bounds

\[
 \boxed{
 a^2K r^{K+1}
 \le E_{p,K}(u)
 \le {a^2K r^{K+1}\over1-r}}
 \tag{L-20812.9}
\]

show that the complete failure of the local Riccati equality is concentrated at
the first omitted power `p^(K+1)`.

## 2. Infinite local factor

Letting `K` tend to infinity gives

\[
 P_{p,\infty}(u)={a r\over1-r}
 ={\log p\over p^{1/2+u}-1},
 \tag{L-20812.10}
\]

and the defect vanishes. Therefore the complete local Euler factor obeys the
exact positive Riccati equation

\[
 \boxed{
 -\partial_uP_{p,\infty}
 =P_{p,\infty}^2+aP_{p,\infty}.}
 \tag{L-20812.11}
\]

Completing a finite prefix to full Euler factors is thus not an innocent upper
or lower approximation: it deletes precisely the positive quantity
`E_(p,K)` from the derivative moment.

## 3. Global finite prefix

At a prime-power cutoff `X=q_j`, put

\[
 K_p(X)=\max\{k:p^k\le X\}.
 \tag{L-20812.12}
\]

Define the positive shifted prefix

\[
 \boxed{
 \mathcal P_j(u)
 =\sum_{q\le X}{\Lambda(q)\over q^{1/2+u}}
 =\sum_{p\le X}P_{p,K_p(X)}(u).}
 \tag{L-20812.13}
\]

Then

\[
 \mathcal P_j(0)=P_j
 \tag{L-20812.14}
\]

and

\[
 \boxed{
 -\mathcal P_j'(u)
 =\sum_{p\le X}
  \left[
   P_{p,K_p}(u)^2
   +(\log p)P_{p,K_p}(u)
   -E_{p,K_p}(u)
  \right].}
 \tag{L-20812.15}
\]

Every term in the first two channels is nonnegative. The entire negative channel
is the explicit, source-bound first-omitted-power defect.

At `u=0`, (L-20812.15) gives the exact finite moment decomposition

\[
 \boxed{
 Q_j
 =\sum_{p\le X}
   [P_{p,K_p}(0)^2+(\log p)P_{p,K_p}(0)]
  -\sum_{p\le X}E_{p,K_p}(0).}
 \tag{L-20812.16}
\]

This is a finite same-prime Selberg/Riccati energy with no double enumeration of
prime powers.

## 4. Exact shrinking-strip flow

For `omega>0`, define

\[
 \mathcal L_j(\omega)
 ={P_j\over\omega}
 \log{P_j\over\mathcal P_j(\omega)}.
 \tag{L-20812.17}
\]

Since `-partial_u log mathcal P= -mathcal P'/mathcal P`, integration of
(L-20812.15) gives

\[
 \boxed{
\begin{aligned}
 \mathcal L_j(\omega)
 ={P_j\over\omega}\int_0^\omega
 {1\over\mathcal P_j(u)}
 \sum_{p\le X}
 \bigl[&P_{p,K_p}(u)^2\\
       &+(\log p)P_{p,K_p}(u)\\
       &-E_{p,K_p}(u)\bigr]du.
\end{aligned}}
 \tag{L-20812.18}
\]

This is the proof-facing form of `T-20803`:

```text
positive local collision energy
+ positive logarithmic drift
- explicit finite-power cutoff defect
- explicit archimedean Fenchel barrier.
```

No zero ordinate, matrix, Schur complement, or oscillatory phase occurs in the
identity.

## 5. Exact completion target

Combining (L-20812.18) with `T-20803`, it is enough to prove cofinally

\[
 \boxed{
 \mathcal L_j(P_j^{-2})
 \ge A_+^*(P_j)
     -{(\log(q_j/2))^2\over8P_j}.}
 \tag{L-20812.19}
\]

A positive proof may therefore proceed by showing that, after the complete
prime/pole/gamma centering in `A_+^*`, the integrated positive local channels in
(L-20812.18) dominate the cutoff defect.

The cutoff term is especially concrete:

- it is positive before subtraction;
- it is attached to the first omitted power of each base prime;
- it vanishes for a completed local Euler factor;
- it has the explicit bounds (L-20812.9);
- it can be grouped by the integer layer `K_p(X)` without any prime-pair
  expansion.

This is a more rigid target than estimating the full von Mangoldt staircase by
a phase-blind PNT remainder.

## 6. Scope correction

Two tempting shortcuts are invalid:

1. **Prime-only:** deleting all `K_p>=2` rows removes a load-bearing entropy and
   Riccati correction.
2. **Completed Euler factors:** replacing finite `K_p` by infinity deletes the
   entire negative channel `sum E_(p,K_p)` and can create a large false reserve.

A correct proof may use completed factors only if it reintroduces the exact
cutoff defect from (L-20812.5).

## 7. Proof boundary

- The finite local Riccati formula, global moment identity, and strip integral
  are exact.
- The decomposition isolates one explicit negative channel but does not yet
  dominate it.
- A coarse sum of the upper bounds in (L-20812.9) loses the constant-scale RH
  margin; cancellation-preserving block or convolution structure is still
  required.
- No RH proof is claimed.