# R-106610 — A positive even Fourier source does not control fifth-residue signs

Claim ID: `R-106610`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-26  
Depends on: `L-106610--L-106611`  
RH status: **not assumed**

Fix \(c>1\) and put

\[
F(t)=c+\cos t.
\]

This is the Fourier transform of the positive even finite measure

\[
c\,\delta_0+\frac12\delta_{1}+\frac12\delta_{-1}.
\]

Nevertheless \(F\) has no real zero. Its fifth derivative and sixth derivative
are

\[
Q(t)=F^{(5)}(t)=-\sin t,
\qquad
Q'(t)=F^{(6)}(t)=-\cos t.
\]

At the ordered real \(Q\)-zeros \(c_j=j\pi\),

\[
\rho_j
=
\frac{F(c_j)}{Q'(c_j)}
=
\begin{cases}
-(c+1),&j\ \mathrm{even},\\
c-1,&j\ \mathrm{odd}.
\end{cases}
\tag{R-106610.1}
\]

The residue signs alternate at every edge, while the parent has no real zero.
The projective edge charge is exactly

\[
\boxed{
\frac{(\rho_{j+1}-\rho_j)^2}
     {\rho_j^2+\rho_{j+1}^2}
=
\frac{2c^2}{c^2+1}>1
}
\tag{R-106610.2}
\]

on every interval.

The endpoint Wronskian is

\[
\mathcal L_5(t)=1+c\cos t,
\]

which also alternates sign on the \(Q\)-zero lattice. Its Fourier transform is
again a positive even measure.

Therefore none of the following implications is valid in the ambient positive
source class:

```text
positive Fourier source for F;
positive Fourier source for the fifth Wronskian;
complete real-rootedness of F^(5);
arbitrarily thin off-real parent zero strip;
-> fifth-residue coherence or parent real zeros.
```

The Xi theorem must use the continuous theta source, the exact contour
corrections, source anti-carrier information, or an equivalent Xi-specific
mechanism. This firewall is also the discrete form of `R-106600`.
