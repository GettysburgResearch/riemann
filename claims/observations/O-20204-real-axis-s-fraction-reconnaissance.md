# O-20204 — Real-axis Haar Stieltjes continued-fraction reconnaissance

Claim ID: `O-20204`  
Title: The first twelve empirical Stieltjes S-fraction coefficients at `y0=2` are positive  
Status: **EMPIRICAL / NON-DIRECTED**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: proposed `T-20202`; `O-20203` moment jet  
Scope: all-order factorization scheduling only

Using the 140-decimal Taylor jet of

\[
 \mathcal L_2(y)
 ={2\over y^2}
 \left[
  2{\xi'\over\xi}(1/2+y)
  -{\xi'\over\xi}(1/2+y/2)
 \right]
\]

at `y0=2`, I formed

\[
 \mu_k=(-1)^k\mathcal L_2^{(k)}(2)
\]

through order `24` and reconstructed the first twelve Stieltjes S-fraction
coefficients from the two Hankel determinant families:

\[
 a_{2n-1}
 ={\Delta_n^{(1)}\Delta_{n-1}^{(0)}
   \over
   \Delta_n^{(0)}\Delta_{n-1}^{(1)}},
\]

\[
 a_{2n}
 ={\Delta_{n+1}^{(0)}\Delta_{n-1}^{(1)}
   \over
   \Delta_n^{(1)}\Delta_n^{(0)}}.
\]

All twelve computed coefficients were positive in ordinary high precision.

This is not a certificate:

- the moments were not directed balls;
- determinants at increasing order are ill-conditioned;
- finite positivity does not imply an infinite Stieltjes fraction;
- no closed recurrence or positive production matrix has been proved.

The useful signal is that the proposed real-axis route is numerically consistent
with a positive continued fraction well beyond the first scalar derivatives.
The next proof-facing task is to derive the coefficients from the Euler/gamma
structure by a positive recurrence, not to extend the decimal ladder alone.
