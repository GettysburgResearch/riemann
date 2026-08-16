# L-20211 — Exact optimal endpoint Fejer family and its autocorrelations

Claim ID: `L-20211`  
Title: The sharp half-knot extremizer has closed spectral, ramp, and terminal-autocorrelation formulas  
Status: **PROPOSED — COMPLETE ELEMENTARY PROOF**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-20208`; `L-20209`  
Scope: the canonical growing positive filter for the bulk-transport attack

## 1. Alternating-sine factor

For an integer `N>=2`, put

\[
 \alpha_N={\pi\over N+1}
\]

and define

\[
\boxed{
 q_j^{(N)}=(-1)^j\sin((j+1)\alpha_N),
 \qquad0\le j<N.}
\]

Let

\[
 Q_N(z)=\sum_{j=0}^{N-1}q_j^{(N)}z^j,
 \qquad
 A_N(z)=(1-z)Q_N(z),
\]

and

\[
 P_N(x)=|A_N(e^{ix})|^2.
\]

Then `P_N` is nonzero, real, even, and nonnegative.

The finite sine generating function gives

\[
\boxed{
 Q_N(z)
 =\sin\alpha_N\,
 {1+(-z)^{N+1}\over
  1+2z\cos\alpha_N+z^2}.}
\]

The apparent poles at `z=-e^(+-i alpha_N)` cancel against the numerator, so the
right side is exactly the polynomial `Q_N`.

## 2. Exact norm and sharp half-knot value

The discrete sine orthogonality identity gives

\[
\boxed{
 \|q^{(N)}\|_2^2={N+1\over2}.}
\]

The vector is the top eigenvector of the Dirichlet difference matrix `D^*D`,
with eigenvalue

\[
 4\cos^2\!\left({\alpha_N\over2}\right).
\]

Therefore its ramp satisfies, for `0<=s<=1`,

\[
\boxed{
 {L_N(s)\over L_N(0)}
 =1-2s\cos^2\!\left({\alpha_N\over2}\right),}
\]

and in particular

\[
\boxed{
 {L_N(1/2)\over L_N(0)}
 =\sin^2\!\left({\alpha_N\over2}\right).}
\]

This attains the sharp inequality of `L-20208`.

## 3. Complete autocorrelation formula

For `0<=m<N`, define

\[
 d_m^{(N)}
 =\sum_{j=0}^{N-m-1}q_{j+m}^{(N)}q_j^{(N)},
 \qquad d_N^{(N)}=0.
\]

Product-to-sum and the finite cosine progression give

\[
\boxed{
 d_m^{(N)}
 ={(-1)^m\over2}
 \left[
  (N-m)\cos(m\alpha_N)
  +{\sin((m+1)\alpha_N)\over\sin\alpha_N}
 \right].}
\]

### Proof

After removing the factor `(-1)^m`,

\[
\begin{aligned}
 \sum_{j=1}^{N-m}
 \sin(j\alpha_N)\sin((j+m)\alpha_N)
 ={}&{N-m\over2}\cos(m\alpha_N)\\
 &-{1\over2}
 \sum_{j=1}^{N-m}
 \cos((2j+m)\alpha_N).
\end{aligned}
\]

The final cosine progression is centered at

\[
 (N+1)\alpha_N=\pi
\]

and equals

\[
 -{\sin((N-m)\alpha_N)\over\sin\alpha_N}
 =-{\sin((m+1)\alpha_N)\over\sin\alpha_N}.
\]

This proves the formula.

By `L-20209`, the full prime ramp is its linear interpolation:

\[
\boxed{
 L_N(m+\theta)
 =2\left[(1-\theta)d_m^{(N)}+
          \theta d_{m+1}^{(N)}\right].}
\]

## 4. Terminal flatness

For a fixed integer `ell>=1`, put `m=N-ell`. The exact formula becomes

\[
\boxed{
 d_{N-\ell}^{(N)}
 ={(-1)^{N-\ell}\over2}
 \left[
  -\ell\cos((\ell+1)\alpha_N)
  +{\sin(\ell\alpha_N)\over\sin\alpha_N}
 \right].}
\]

Taylor expansion at `alpha_N=0` gives

\[
\boxed{
 d_{N-\ell}^{(N)}
 =(-1)^{N-\ell}
 {\ell(\ell+1)(\ell+2)\over6}
 \alpha_N^2
 +O_\ell(\alpha_N^4).}
\]

Thus every fixed terminal lag is `O_ell(N^-2)`, on the same scale as the sharp
half-knot debt.

For example,

\[
 d_{N-1}^{(N)}=(-1)^{N-1}\sin^2\alpha_N.
\]

## 5. Low-lag oscillation

For each fixed `m` as `N->infinity`,

\[
\boxed{
 {d_m^{(N)}\over d_0^{(N)}}
 =(-1)^m+O_m(N^{-2}).}
\]

The optimal first-cell filter therefore pays for its small half-knot debt by a
strong alternating low-lag autocorrelation pattern. It is not automatically
optimal for the complete prime deposition ledger.

This fact is load-bearing for the next search: candidate filters must be ranked
by the **full centered prime/pole quadratic**, not by the half-knot ratio alone.

## 6. Proof-facing use

The family supplies an exact baseline with:

- optimal `O(N^-2)` first-prime debt;
- explicit autocorrelations at every lag;
- explicit `O(N^-2)` terminal flatness;
- no numerical eigensolve or rational repair.

The remaining theorem is to show that a centered prime-bulk/Selberg transport
pays the positive part of its alternating autocorrelation ledger, or to replace
it by a different growing family with a better full-ledger ratio while retaining
the pole-descent completeness gate.
