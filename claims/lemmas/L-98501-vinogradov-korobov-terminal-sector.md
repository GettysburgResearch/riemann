# L-98501 — Vinogradov–Korobov prime discrepancy closes a moving subpower terminal sector

Claim ID: `L-98501`  
Status: **UNCONDITIONAL EFFECTIVE ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98500`; the classical Vinogradov–Korobov prime number theorem  
RH status: **not assumed**

The prime number theorem with Vinogradov–Korobov error implies effective
constants \(c,C>0\) such that, for \(L=\log z\) sufficiently large,
\[
\boxed{
\Delta_z(u)
\le
C\exp\!\left[
-cL^{3/5}(\log L)^{-1/5}
\right]
}
\tag{L-98501.1}
\]
uniformly in \(u\ge1\). Also
\[
\sum_{p\ge z}\frac1{p^2}\ll\frac1{z\log z}.
\tag{L-98501.2}
\]

The elementary Dickman lower bound
\[
\boxed{
\rho(u)\ge
(2u+2)^{-\,2u-2}
}
\tag{L-98501.3}
\]
follows by iterating
\[
u\rho(u)=\int_{u-1}^{u}\rho(t)\,dt
\]
over half-unit subintervals.

Let \(b\) satisfy `L-98500`. There is an effective constant \(C_b\) such that
\[
\boxed{
2(u+1)\log(2u+2)+4\log(2u+2)
\le
\frac c2L^{3/5}(\log L)^{-1/5}
}
\tag{L-98501.4}
\]
and \(L\ge C_b\log(2u+2)\) imply
\[
\boxed{\mathcal F_b(Y,z)>0.}
\tag{L-98501.5}
\]

Indeed (L-98501.4) makes the discrete error in (L-98500.5) at most one quarter
of \(a\rho(u)\). Equation (L-98500.13) pays the signed boundary term by another
quarter. The exponentially small endpoint term and (L-98501.2) are absorbed
after increasing the effective threshold.

## Endpoint-only corollary

Put \(T=\log Y\). There is an effective constant \(C_0\), depending only on the
fixed annular base, such that
\[
\boxed{
\log z
\ge
C_0T^{5/8}(\log T)^{3/4}
\quad\Longrightarrow\quad
\mathcal F_b(Y,z)>0
}
\tag{L-98501.6}
\]
for all sufficiently large \(Y\).

To verify the exponents, set
\[
L=C_0T^{5/8}(\log T)^{3/4},
\qquad
u=\frac TL.
\]
Then
\[
u\log(2u)
\ll
C_0^{-1}T^{3/8}(\log T)^{1/4},
\]
whereas
\[
L^{3/5}(\log L)^{-1/5}
\gg
C_0^{3/5}T^{3/8}(\log T)^{1/4}.
\]
A sufficiently large effective \(C_0\) gives (L-98501.4).

For the complete \(P_{61}\) annular \(5{:}3\) base of PR #576, all hypotheses
of `L-98500` follow from its finite hinge formula and the retained
Euler–Maclaurin expansion. Therefore
\[
\boxed{
p_0\ge
\exp\!\left[
C_0(\log Y)^{5/8}(\log\log Y)^{3/4}
\right]
\Longrightarrow
\mathcal F_{p_0}(Y)>0.
}
\tag{L-98501.7}
\]

This is a canonical-orientation theorem. An odd incoming rough history still
reverses signed observation.
