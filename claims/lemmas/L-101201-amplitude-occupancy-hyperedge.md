# L-101201 — Complementary amplitude and occupancy exponents give subpower negative mass

Claim ID: `L-101201`  
Status: **PROVED EXACT DYADIC AND-GATE**  
Created: 2026-08-21

Let \(I_L=[2^L,2^{L+1})\), \(E_L=\{X\in I_L:F(X)<0\}\), and suppose \(F_-(X)\le A_L(X)\mathbf1_{E_L}(X)\). If, for some \(\theta\ge0\) and \(\eta(L)=o(L)\),

\[
\int_{I_L}A_L(X)^2\frac{dX}{X}\le2^{\theta L+\eta(L)},
\qquad
\int_{E_L}\frac{dX}{X}\le2^{-\theta L+\eta(L)},
\]

then Cauchy–Schwarz gives

\[
\boxed{
\int_{I_L}F_-(X)\frac{dX}{X}\le2^{\eta(L)}=2^{o(L)}.
}
\]

Neither antecedent need be subpower. The positive and negative exponents cancel only after composition.
