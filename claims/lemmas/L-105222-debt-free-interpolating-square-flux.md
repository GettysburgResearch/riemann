# L-105222 — Debt-free interpolating square flux

Claim ID: `L-105222`  
Status: **PROVED EXACT, FINITE-WINDOW MEROMORPHIC IDENTITY**  
Depends on: finite polynomial interpolation; residue theorem  
RH status: not assumed

Let \(F_k=F_0^{(k)}\), and let \(\Omega\) be a bounded rectangle such that:

1. every zero of \(F_k\) in \(\overline\Omega\) is simple;
2. \(F_k\) has no zero on \(\partial\Omega\);
3. \(F_{k+1}(c)\ne0\) at every zero \(c\) of \(F_k\) in \(\Omega\).

The zero set inside \(\Omega\) is finite. Therefore there is a polynomial
\(U_{k,\Omega}\) satisfying
\[
\boxed{
U_{k,\Omega}(c)
=\frac{F_{k-1}(c)}{F_{k+1}(c)}
}
\tag{1}
\]
for every \(F_k\)-zero \(c\) in \(\Omega\).

For \(\lambda\ge0\), define
\[
\boxed{
\mathscr G_{k,\lambda,\Omega}(z)
=\frac{F_{k+1}(z)}{F_k(z)}
\bigl(1+\lambda U_{k,\Omega}(z)\bigr)^2.
}
\tag{2}
\]
This meromorphic function has no pole at a zero of \(F_{k+1}\). Its only
poles in \(\Omega\) are the zeros of \(F_k\), and at such a zero \(c\),
\[
\operatorname{Res}_{z=c}\mathscr G_{k,\lambda,\Omega}
=(1+\lambda\rho_{k,c})^2.
\tag{3}
\]
Consequently
\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega}
\mathscr G_{k,\lambda,\Omega}(z)\,dz
=
\sum_{F_k(c)=0,\ c\in\Omega}
(1+\lambda\rho_{k,c})^2.
}
\tag{4}
\]

If the rectangle and zero data are invariant under conjugation and
\(z\mapsto-z\), and the derivative chain has definite parity, the interpolant
may be chosen with real coefficients and even parity. Then
\(\mathscr G(-z)=-\mathscr G(z)\), and
\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega_{T,\eta}}\mathscr G\,dz
=\frac2\pi\left[
\int_0^\eta\Re\mathscr G(T+iy)\,dy
-
\int_0^T\Im\mathscr G(x+i\eta)\,dx
\right].
}
\tag{5}
\]

Thus the adjacent-derivative debt in the canonical local observable
\(F_{k-1}^2/(F_kF_{k+1})\) is not structurally necessary at a fixed finite
window. It can be exchanged exactly for the boundary growth of one
source-matched interpolation polynomial.
