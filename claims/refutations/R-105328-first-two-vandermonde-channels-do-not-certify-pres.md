# R-105328 — The first two critical Vandermonde channels do not certify the pointwise residue gate

Claim ID: `R-105328`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105328`; parent `R-105202--R-105203`  
RH status: **not assumed**

## 1. Exact quartic separator

Put

\[
p(x)=x^4-2x^2-1.
\tag{R-105328.1}
\]

Then

\[
p'(x)=4x(x-1)(x+1),
\]

so the critical points are `-1,0,1`. Their derivative-ratio residues are

\[
\boxed{
(\rho_{-1},\rho_0,\rho_1)
=(-1/4,\ 1/4,\ -1/4).
}
\tag{R-105328.2}
\]

The middle critical point is a wrong extremum. Nevertheless, for the critical
sign Hankel matrix

\[
\mathsf P_{rs}=\sum_c(-\rho_c)c^{r+s},
\qquad0\le r,s\le2,
\]

the first two leading determinants are positive:

\[
\boxed{
D_1^{\rm crit}=1/4>0,
\qquad
D_2^{\rm crit}=1/8>0.
}
\tag{R-105328.3}
\]

The complete determinant detects the defect:

\[
\boxed{
D_3^{\rm crit}=-1/16<0.
}
\tag{R-105328.4}
\]

Equivalently, the cardinal polynomial

\[
q(x)=1-x^2
\]

isolates the middle critical point and gives

\[
q^T\mathsf Pq=-1/4.
\tag{R-105328.5}
\]

## 2. Consequence

The scalar first residue moment and the first exterior-square/Vandermonde
minor can both have the favorable sign while one literal positive critical
residue remains. Thus

```text
D_1^crit > 0 and D_2^crit > 0
    do not imply
PRES105220.
```

No bounded initial segment of the determinant hierarchy may be promoted to the
complete pointwise sign gate without new Xi-specific structure. This is the
critical-residue counterpart of the parent four-point Loewner separator.

## 3. Sharpness against the coherence firewall

The earlier five-real-root polynomial

\[
p(x)=x^5/5-7x^3-10x^2+8/5
\]

has all residues negative while violating the subunit coherence condition by
a large exact margin. Its **complete** critical Hankel hierarchy is strictly
positive. Hence the new full hierarchy is sharp on the simple real-critical
stratum, while both scalar coherence and bounded-order determinant shortcuts
are overstrong or insufficient in different directions.

## 4. Scope

This is an elementary polynomial separator, not a counterexample built from
Xi. It proves that the complete hierarchy—or a genuinely source-specific
replacement—is load bearing.
