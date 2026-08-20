# L-100720 — The critical cubic is an exact hinge mixture with one compact collar

Claim ID: `L-100720`  
Status: **PROVED EXACT KERNEL/SOURCE IDENTITY**  
Created: 2026-08-21  
Base: PR #691 at `be9a4168fa0df971a2fc63176f07ce3beee6c3d4`  
RH status: **not assumed**

Let the centered critical cubic kernel of PR #676 be

\[
\Psi(y)=64\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\]

Write `t=sqrt(y)` and put `h_s(t)=(t-s)_+`. Then

\[
\boxed{
\Psi(t^2)=384\int_0^1 h_s(t)(1-s)\,ds.
}
\tag{L-100720.1}
\]

Indeed, for `0<t<=1`,

\[
6\int_0^t(t-s)(1-s)ds=3t^2-t^3,
\]

while for `t>=1`,

\[
6\int_0^1(t-s)(1-s)ds=3t-1.
\]

The same identity has the carrier/collar form

\[
\boxed{
\Psi(t^2)=192t-64+64(1-t)_+^3.
}
\tag{L-100720.2}
\]

## Double-owner interval

Fix two endpoint primes `p<q` and a finite set `P` of interior primes strictly
between them.  On functions of `t`, let

\[
(V_a f)(t)=f(t/\sqrt a),
\qquad
\Delta_a=I-V_a,
\]

and put

\[
E_{\mathcal P}=\prod_{\ell\in\mathcal P}
 (I-\ell^{-1/2}V_\ell).
\]

The literal double-owner cubic entry is

\[
H_{p,q;\mathcal P}(t)
=\Delta_p\Delta_qE_{\mathcal P}\Psi(t^2).
\tag{L-100720.3}
\]

The linear carrier in (L-100720.2) is an eigenfunction of every scale shift.
Therefore

\[
\boxed{
M_{p,q;\mathcal P}(t)
=192t(1-p^{-1/2})(1-q^{-1/2})
 \prod_{\ell\in\mathcal P}(1-\ell^{-1})
\ge0
}
\tag{L-100720.4}
\]

and

\[
\boxed{
\widetilde H_{p,q;\mathcal P}(t)
:=H_{p,q;\mathcal P}(t)-M_{p,q;\mathcal P}(t)
=64\Delta_p\Delta_qE_{\mathcal P}(1-t)_+^3.
}
\tag{L-100720.5}
\]

The constant `-64` is killed by the two endpoint differences.  Thus the
centered interval entry is exactly one compact cubic spline; it is not merely
bounded by an unspecified activation error.

If

\[
D_{\mathcal P}=\prod_{\ell\in\mathcal P}\ell,
\]

then

\[
\widetilde H_{p,q;\mathcal P}(t)
=\widetilde H'_{p,q;\mathcal P}(t)
=\widetilde H''_{p,q;\mathcal P}(t)=0
\qquad(t\ge\sqrt{pqD_{\mathcal P}}).
\tag{L-100720.6}
\]

At the other endpoint,

\[
H_{p,q;\mathcal P}(0)=H'_{p,q;\mathcal P}(0)=0,
\]

and

\[
\boxed{
\frac12H''_{p,q;\mathcal P}(0)
=192(1-p^{-1})(1-q^{-1})
 \prod_{\ell\in\mathcal P}(1-\ell^{-3/2})>0.
}
\tag{L-100720.7}
\]

Equations (L-100720.5)--(L-100720.7) give exact left and right boundary data
for the final partial-activation collar.  No deep carrier, constant mode, or
fully active Euler product remains inside the centered packet.
