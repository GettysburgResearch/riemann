# L-97703 - Exact logarithmic prime ownership of the C4MBI67 Möbius boundary

Claim ID: `L-97703`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-18  
Depends on: `L-97702`  
RH status: **not assumed**

Let `kappa_X` be the four-band hinge kernel from `L-97702`.  For every
squarefree `n>1`,

\[
\boxed{
\mu(n)\log n=-\sum_{p\mid n}\mu(n/p)\log p.
}
\tag{L-97703.1}
\]

This is immediate because `mu(n/p)=-mu(n)` and
`sum_(p|n) log p=log n`.

Multiplying (L-97703.1) by
`kappa_X(n)/(sqrt(n) log n)`, summing, and writing `n=pm` gives

\[
\boxed{
\sum_{n>1}\frac{\mu(n)}{\sqrt n}\kappa_X(n)
=-\sum_{p\le X}\frac{\log p}{\sqrt p}
 \sum_{\substack{m\le X/p\\p\nmid m}}
 \frac{\mu(m)}{\sqrt m}
 \frac{\kappa_X(pm)}{\log(pm)}.
}
\tag{L-97703.2}
\]

The upper limits may be omitted if `kappa_X` is extended by zero.

## Exact ownership

For a fixed squarefree product `n>1`, the coefficient assigned through owner
prime `p|n` is

\[
\frac{\log p}{\log n}.
\]

These coefficients are nonnegative and sum to one.  Therefore every original
Möbius source atom is spent exactly once across all of its prime owners; no
factorization is duplicated and no unrestricted reservoir is introduced.

Define the bilinear owner functional

\[
\mathfrak B_X=
\sum_{p\le X}\frac{\log p}{\sqrt p}
 \sum_{\substack{m\le X/p\\p\nmid m}}
 \frac{\mu(m)}{\sqrt m}
 \frac{\kappa_X(pm)}{\log(pm)}.
\tag{L-97703.3}
\]

Then `L-97702` becomes

\[
\boxed{
\mathcal A_X=6H_X(1)+\kappa_X(1)-\mathfrak B_X.
}
\tag{L-97703.4}
\]

Consequently

\[
\boxed{
\mathcal A_X\ge0
\iff
\mathfrak B_X\le6H_X(1)+\kappa_X(1).
}
\tag{L-97703.5}
\]

For `X>=16`, all three unit hinges are saturated and

\[
6H_X(1)+\kappa_X(1)
=
\left(\frac9{\sqrt2}-\frac32\right)\log4
=
\frac{9\sqrt2-3}{2}\log4.
\tag{L-97703.6}
\]

Thus the remaining sign may be written either as the four-band Mertens
boundary `C4MBI67` or as the exact prime-versus-Möbius owner inequality
(L-97703.5).  No bound for either side is asserted here.
