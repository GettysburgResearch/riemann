# L-105221 — Quadratic residue-defect duality and additive descent

Claim ID: `L-105221`  
Status: **PROVED EXACT, FINITE REGULAR-WINDOW THEOREM**  
Depends on: exact real reverse Rolle; L-104523; L-105101  
RH status: not assumed

Let \(F_k=F_0^{(k)}\) on a regular real interval \(I\), with every real zero
of \(F_k\) simple and no common zero of \(F_k,F_{k+1}\). At a real zero
\(c\) of \(F_k\), put
\[
\rho_{k,c}=\frac{F_{k-1}(c)}{F_{k+1}(c)}.
\]
For any \(\lambda_k\ge0\), define the square defect
\[
\boxed{
\mathcal D_k(\lambda_k)
=\sum_{F_k(c)=0,\ c\in I}(1+\lambda_k\rho_{k,c})^2.
}
\tag{1}
\]

If \(E_k\) is the number of wrong extrema of \(F_{k-1}\), then
\[
\boxed{E_k\le \mathcal D_k(\lambda_k).}
\tag{2}
\]
Indeed, every wrong extremum has \(\rho_{k,c}>0\), and therefore
\((1+\lambda_k\rho_{k,c})^2\ge1\).

Consequently, for every derivative block \(1\le k\le K\),
\[
\boxed{
R_0\ge R_K-2\sum_{k=1}^K\mathcal D_k(\lambda_k)-K.
}
\tag{3}
\]
This follows by summing the exact one-step bound
\(R_{k-1}\ge R_k-2E_k-1\).

## Moment duality

Put
\[
M_{1,k}=-\sum_c\rho_{k,c},
\qquad
M_{2,k}=\sum_c\rho_{k,c}^2.
\]
Then
\[
\boxed{
\mathcal D_k(\lambda)
=R_k-2\lambda M_{1,k}+\lambda^2M_{2,k}.
}
\tag{4}
\]
Hence
\[
\boxed{
\min_{\lambda\ge0}\mathcal D_k(\lambda)
=R_k-\frac{(M_{1,k})_+^2}{M_{2,k}},
}
\tag{5}
\]
with the usual zero convention when \(M_{2,k}=0\). Thus the coherence ratio
is exactly the optimized quadratic square defect, not an additional
hypothesis.

## Canonical contour form and its debt

On a regular rectangle \(\Omega_{T,\eta}\), define
\[
P_k=\frac{F_{k-1}}{F_k},
\qquad
Q_k=\frac{F_{k-1}^2}{F_kF_{k+1}}.
\]
Let \(C_{1,k}\) and \(C_{2,k}\) be the algebraic first- and squared-residue
sums over nonreal \(F_k\)-zeros in the rectangle, and let \(D_{2,k}\) be the
adjacent-derivative debt over \(F_{k+1}\)-zeros from L-105101. Then
\[
\boxed{
\mathcal D_k(\lambda)
=R_k+\frac1{2\pi i}\int_{\partial\Omega}
(2\lambda P_k+\lambda^2Q_k)\,dz
-2\lambda C_{1,k}-\lambda^2(C_{2,k}+D_{2,k}).
}
\tag{6}
\]
This is an additive, ratio-free contour target. L-105222 removes the
adjacent-derivative debt by a finite-window interpolation.
