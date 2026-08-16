# O-20203 — Real-axis Haar Stieltjes reconnaissance at `y0=2`

Claim ID: `O-20203`  
Title: The first twelve two-sided Stieltjes Hankel levels are positive in ordinary high precision  
Status: **EMPIRICAL / NON-DIRECTED**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: proposed `T-20202`  
Scope: scheduling evidence for the real-axis all-order route

For

\[
 \mathcal L_2(y)
 ={2\over y^2}
 \left[
  2{\xi'\over\xi}\left({1\over2}+y\right)
  -{\xi'\over\xi}\left({1\over2}+{y\over2}\right)
 \right]
\]

and

\[
 \mu_k=(-1)^k\mathcal L_2^{(k)}(2),
\]

I evaluated the Taylor jet through order `24` at 140 decimal working digits
using the explicit completed-xi logarithmic derivative at the ordinary real
points `3/2` and `5/2`.

For every `n=0,...,11`, both moment matrices

\[
 H_n^{(0)}=(\mu_{i+j})_{0\le i,j\le n},
 \qquad
 H_n^{(1)}=(\mu_{i+j+1})_{0\le i,j\le n}
\]

had positive ordinary high-precision LDL pivots.

This is reconnaissance only:

- no ball or directed interval arithmetic was used;
- numerical differentiation/Taylor assembly is not an all-order theorem;
- twelve positive levels do not imply complete monotonicity or RH.

The useful conclusion is strategic. The first likely obstruction is not at a
tiny Hankel order. The proof attack should seek a structural continued fraction,
Jacobi production matrix, or positive-measure representation rather than merely
extending the finite numerical ladder.

The exact CSV generated in-session is retained separately as a downloadable
conversation artifact; it has not been promoted to a proof object in the
repository.
