# R-105270 — A holomorphic safe-line carrier cancels on the closed residue contour

Claim ID: `R-105270`  
Status: **PROVED EXACT; BINDING CORRECTION TO T-105250/T-105260**  
Created: 2026-08-24  
RH status: unproved

Let \(\Omega\) be a bounded domain with piecewise smooth boundary.  Let
\(h,\phi_1,\ldots,\phi_d\) be holomorphic in a neighbourhood of
\(\overline\Omega\).  Then Cauchy's theorem gives, entry by entry,

\[
\boxed{
-\frac1{2\pi i}\int_{\partial\Omega}
 h(z)\phi_i(z)\phi_j(z)\,dz=0.
}
\tag{1}
\]

The statement remains true after multiplying every observation by any
holomorphic source-fixed taper \(w\), because \(h(w\phi_i)(w\phi_j)\) is still
holomorphic.

## Safe-line decomposition firewall

Suppose a boundary calculation decomposes the zero matrix in (1) as

\[
0=M_h+E_h,
\tag{2}
\]

where \(M_h\) is the contribution assigned to selected safe-line pieces and
\(E_h\) is everything else.  Then

\[
\boxed{E_h=-M_h.}
\tag{3}
\]

In particular, if the safe-line calculation represents a constant carrier as
a positive Gram \(M_h=G\succ0\), then in the \(G\)-normalization

\[
G^{-1/2}E_hG^{-1/2}=-I
\]

and

\[
\boxed{
\operatorname{tr}
\bigl((G^{-1/2}E_hG^{-1/2})_-\bigr)=d.
}
\tag{4}
\]

Thus the complementary contour cannot have normalized negative trace
\(<1/20\), \(<647/19980\), or even \(o(d)\) in the pure-carrier fixture.

## Consequences for the polynomial Wick model

The degree-zero term in

\[
\frac{P_K(x)^2}{1-x}
=1+\sum_{m\ge K+1}q_{K,m}x^m
\]

is a holomorphic frozen carrier.  It is useful for safe-line algebra but is
not a conclusion-facing positive direction of the closed critical-residue
form.  Any actual/model transfer theorem that counts this `1` as a positive
identity block must also retain its exact cancellation in the complementary
contour.

Accordingly:

1. `T-105250` remains valid as an exact source/model hierarchy and as a
   conditional implication, but its proposed asymptotically lossless transfer
   cannot be justified by declaring the carrier closure negligible;
2. `T-105260`'s `EDGEFLUX105260` is false for the natural decomposition that
   leaves the safe-line identity carrier in the anchor;
3. an analytic endpoint taper cannot repair the problem, because (1) holds
   after tapering;
4. a viable ninety-percent argument must use a carrier owned by a pole,
   Cauchy index, non-holomorphic boundary jump, or another conclusion-facing
   source—not a holomorphic frozen constant.

This refutation does not affect the exact Toeplitz--Hankel polarization formulas
or the carrier-free Hankel energy bound of L-105260/L-105261.
