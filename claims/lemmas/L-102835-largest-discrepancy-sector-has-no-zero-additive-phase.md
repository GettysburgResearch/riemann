# L-102835 — A largest-discrepancy sector is exactly a nonzero additive-phase packet

Claim ID: `L-102835`  
Status: **PROVED EXACT DISPERSION IDENTITY**  
Created: 2026-08-24  
Depends on: `L-102831`; `L-102834`  
RH status: **not assumed**

Work in the hard sector of distinct physical owner primes, after the joint
occurrence of the two labelled `67` copies has been placed in the closed
repeated-prime diagonal. Let

\[
N=pq\,a^2,
\qquad
M=rs\,b^2
\]

have different semiprime squareclasses, and let `ell` be their largest
discrepancy prime as in `L-102834`. Orient the pair so that `ell` belongs to
`{p,q}`.

Because every core prime is smaller than the second owner and every larger
owner parity agrees, one has

\[
\ell\mid N,
\qquad
\ell\nmid M.
\tag{L-102835.1}

For

\[
e_\ell(x)=\exp(2\pi i x/\ell),
\]

the prime Ramanujan identity gives

\[
\sum_{h=0}^{\ell-1}e_\ell(h(N-M))=0.
\]

Since the `h=0` term is one,

\[
\boxed{
1=-\sum_{h=1}^{\ell-1}e_\ell(h(N-M)).
}
\tag{L-102835.2}

Thus every cross-squareclass Gram coefficient in the `ell` sector is exactly a
sum of **nonzero** additive phases. The zero phase, which contains the
source-blind carrier, is absent before Cauchy or a large-sieve estimate is
applied.

If `A_ell` denotes the field on the side divisible by `ell` and
`B_{ell,h}` is the non-`ell` field twisted by `e_ell(-hM)`, then

\[
\boxed{
\mathcal C_\ell
=-\sum_{h=1}^{\ell-1}
\langle A_\ell,B_{\ell,h}\rangle.
}
\tag{L-102835.3}

The identity is coefficient-exact, keeps all owner and source-region labels,
and commutes with the fixed ratio-eight outer observation.

## Scope

Equation (L-102835.3) is an exact dispersion normal form. It does not bound the
nonzero phase packet. `L-102836` supplies the uniform square-core phase energy
for each fixed non-`ell` squareclass; coherent cross-owner summation remains
arithmetic.