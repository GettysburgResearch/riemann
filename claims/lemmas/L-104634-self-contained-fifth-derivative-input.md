# L-104634 — A self-contained exact fifth-derivative input above 98 percent

Claim ID: `L-104634`  
Status: **PROVED UNCONDITIONALLY FROM THE RECONSTRUCTED CONREY FUNCTIONAL**  
Created: 2026-08-27  
Depends on: `L-104602`, exact verifier `X-104620`  
RH status: **not assumed**

Use the reconstructed Conrey functional of `L-104602` with

\[
m=5,\qquad R=1,\qquad \phi(x)=1-x.
\]

Then

\[
q_5(x)=(1-x)(1-2x)^5
\]

is admissible:

\[
\phi(0)=1,\qquad \phi'(x)=\phi'(1-x),\qquad \phi(1)=0.
\]

The exact rational interval engine of `X-104620`, with the additional target
defect `1/50`, proves

\[
\mathcal F_5(1,1-x)<e^{1/50}.
\]

Therefore Conrey's reconstructed theorem gives

\[
\boxed{\alpha_5>{49\over50}=0.98.}
\tag{L-104634.1}
\]

No optimized decimal coefficient from Conrey's published table is used. The
stronger classical value `alpha_5>0.9970` remains available, but
(L-104634.1) is a fully transparent source-locked fallback for the
fifth-endpoint programme.

## Height consequence

All zeros of the fixed fifth derivative lie in the centered strip
`|Im z|<=1/2`. Conjugation pairs the nonreal zeros. Hence on regular dyadic
windows,

\[
\boxed{
\mathfrak h_+(\Xi^{(5)};T,2T)
\le {1\over4}(N_5-R_5)
\le\left({1\over200}+o(1)\right)N(T,2T).
}
\tag{L-104634.2}
\]

Together with the Selberg/Rouché parent-companion passage of `L-106591`, the
complete fifth-endpoint denominator height is at most
`(1/200+o(1))N`.
