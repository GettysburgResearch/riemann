# L-105240 — Positive companion line-energy decomposition

Claim ID: `L-105240`  
Status: **PROVED EXACT, FINITE TOOTHED-CONTOUR IDENTITY**  
Depends on: L-105230

Fix one derivative level and write
\[
p=F_k,
\qquad
E=F_{k+1}+i\delta F_k,
\qquad
H=F_{k+1}+\lambda F_{k-1},
\]
where `delta>0` and `lambda>=0`.  Define
\[
\boxed{
\mathscr T(z)=\frac{H(z)^2}{F_k(z)E(z)}.
}
\tag{1}
\]
At a simple real zero `c` of `F_k`,
\[
\boxed{
\operatorname{Res}_{z=c}\mathscr T
=(1+\lambda\rho_{k,c})^2.
}
\tag{2}
\]
At a simple zero `zeta` of `E`,
\[
\boxed{
\sigma_{k,\lambda,\delta}(\zeta)
=
\frac{H(\zeta)^2}{F_k(\zeta)E'(\zeta)}.
}
\tag{3}
\]
There are no other poles.

Let `Gamma_(T,eta,epsilon)` be the positively oriented boundary of the lower
rectangle `[-T,T] x [-eta,0]`, with a small upper semicircular bump around
each real `F_k` zero in `(-T,T)`.  Assume the collar contains no nonreal
`F_k` zero and no pole on its boundary.  Let `P_k` be the sum of the companion
residues (3) inside the collar, and let `O_k` be the normalized integral over
the bottom and two vertical sides:
\[
O_k=\frac1{2\pi i}\int_{\Gamma_{\rm bottom+sides}}\mathscr T(z)\,dz.
\]

On the real axis away from the poles,
\[
\boxed{
-\Im\mathscr T(x)
=
\delta\,
\frac{[F_{k+1}(x)+\lambda F_{k-1}(x)]^2}
{F_{k+1}(x)^2+\delta^2F_k(x)^2}
\ge0.
}
\tag{4}
\]
Each upper semicircle contributes one half of its real residue.  Taking the
radius to zero in the residue theorem therefore gives
\[
\boxed{
\mathcal D_k(\lambda)
=
\frac{\delta}{\pi}\int_{-T}^{T}
\frac{[F_{k+1}(x)+\lambda F_{k-1}(x)]^2}
{F_{k+1}(x)^2+\delta^2F_k(x)^2}
\,dx
+2\Re O_k-2\Re P_k,
}
\tag{5}
\]
where
\[
\mathcal D_k(\lambda)
=\sum_{F_k(c)=0,\ c\in(-T,T)}(1+\lambda\rho_{k,c})^2.
\]

Consequently
\[
\boxed{
\mathcal D_k(\lambda)
\le
\mathcal E_k(\lambda,\delta)
+2(\Re O_k)_+
+2(-\Re P_k)_+,
}
\tag{6}
\]
with the first term in (5) denoted by `mathcal E_k`.

The identity is local and exact.  Passage to growing Xi windows requires
regular-height, multiplicity, and collar-exhaustion ledgers.
