# L-105230 — Companion-corona square-flux identity

Claim ID: `L-105230`  
Status: **PROVED EXACT, FINITE-WINDOW MEROMORPHIC IDENTITY**  
RH status: not assumed

Let `F_j=F_0^(j)` and fix `k>=1`, `lambda>=0`, `delta>0`.  Put
\[
G_{k,\delta}=F_{k+1}+i\delta F_k
\]
and define
\[
\boxed{
\mathscr S_{k,\lambda,\delta}
=
\frac{F_{k+1}}{F_k}
+2\lambda\frac{F_{k-1}}{F_k}
+\lambda^2
\frac{F_{k-1}^2}{F_kG_{k,\delta}}.
}
\tag{1}
\]
Let `Omega` be a bounded domain with piecewise smooth boundary such that:

1. `F_k` and `G_(k,delta)` have no zero on the boundary;
2. every zero of either function in `Omega` is simple;
3. `F_k` and `F_(k+1)` have no common zero in `Omega`.

At a zero `c` of `F_k`, define
\[
\rho_{k,c}=\frac{F_{k-1}(c)}{F_{k+1}(c)}.
\]
Then
\[
\boxed{
\operatorname{Res}_{z=c}\mathscr S_{k,\lambda,\delta}
=(1+\lambda\rho_{k,c})^2.
}
\tag{2}
\]
Indeed, the three terms in (1) have residues `1`, `2 lambda rho`, and
`lambda^2 rho^2`, because `G_(k,delta)(c)=F_(k+1)(c)`.

At a zero `zeta` of `G_(k,delta)`, the only pole is the final term and
\[
\boxed{
\pi_{k,\lambda,\delta}(\zeta)
=
\lambda^2
\frac{F_{k-1}(\zeta)^2}
{F_k(\zeta)G_{k,\delta}'(\zeta)}.
}
\tag{3}
\]
Since at such a zero `F_(k+1)=-i delta F_k`, this may also be written
\[
\pi_{k,\lambda,\delta}(\zeta)
=
\lambda^2
\frac{F_{k-1}(\zeta)^2}
{F_k(\zeta)[F_{k+2}(\zeta)+\delta^2F_k(\zeta)]}.
\tag{4}
\]
There are no adjacent-derivative poles at zeros of `F_(k+1)`.

The residue theorem therefore gives the exact identity
\[
\boxed{
\sum_{F_k(c)=0,\ c\in\Omega}(1+\lambda\rho_{k,c})^2
=
\frac1{2\pi i}\int_{\partial\Omega}\mathscr S_{k,\lambda,\delta}(z)\,dz
-
\sum_{G_{k,\delta}(\zeta)=0,\ \zeta\in\Omega}
\pi_{k,\lambda,\delta}(\zeta).
}
\tag{5}
\]

Unlike L-105222, (1) is a fixed source-matched field.  No polynomial
interpolation, Vandermonde inverse, or growing interpolation degree occurs.
