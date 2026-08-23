# L-105221 — Moving-centre Xi safe-line carriers have coherence defect two logarithmic orders below the main scale

Claim ID: `L-105221`  
Status: **PROPOSED UNCONDITIONAL FIXED-ORDER SAFE-LINE ASYMPTOTIC; independent review pending**  
Created: 2026-08-23  
Depends on: `L-105220`; the functional equation and standard right-half-plane asymptotics for `xi`  
RH status: **not assumed**

Let

\[
\Xi(z)=\xi\!\left(\frac12+iz\right),
\qquad
F_j(z)=\Xi^{(j)}(z).
\]

Fix an integer `k>=1`. For a real centre `a`, define the three safe
right-half-plane points

\[
s_h(a)=\frac12+h-ia,
\qquad h=1,2,3.
\tag{L-105221.1}
\]

Put

\[
d_1=\frac32,\qquad
d_2=-\frac65,\qquad
d_3=\frac3{10},
\qquad
D=\sum_{h=1}^3d_h=\frac35.
\tag{L-105221.2}
\]

## 1. Functional-equation dictionary

At `z=a+ih`, the functional equation gives

\[
F_j(a+ih)=(-i)^j\xi^{(j)}(s_h(a)).
\tag{L-105221.3}
\]

Define

\[
U_{k,h}=\frac{\xi^{(k+1)}}{\xi^{(k)}}(s_h),
\qquad
S_{k,h}=\frac{\xi^{(k-1)}}{\xi^{(k)}}(s_h),
\]

\[
V_{k,h}=
\frac{\xi^{(k-1)}(s_h)^2}
{\xi^{(k)}(s_h)\xi^{(k+1)}(s_h)}.
\tag{L-105221.4}
\]

Then

\[
\frac{F_{k+1}}{F_k}(a+ih)=-iU_{k,h},
\qquad
\frac{F_{k-1}}{F_k}(a+ih)=iS_{k,h},
\]

\[
\frac{F_{k-1}^2}{F_kF_{k+1}}(a+ih)=-iV_{k,h}.
\tag{L-105221.5}
\]

The value-only boundary carriers are therefore

\[
\boxed{
\mathcal N_k(a)=\sum_{h=1}^3d_h\Re U_{k,h},
}
\tag{L-105221.6}
\]

\[
\boxed{
\mathcal A_k(a)=\sum_{h=1}^3d_h\Re S_{k,h},
}
\tag{L-105221.7}
\]

and

\[
\boxed{
\mathcal B_k(a)=\sum_{h=1}^3d_h\Re V_{k,h}.
}
\tag{L-105221.8}
\]

For a finite polynomial approximation these are, respectively, the complete
localized critical count, the negative first-residue carrier, and the raw
second-residue carrier including the adjacent-derivative debt.

## 2. Fixed-order safe-line expansion

Put

\[
\ell(a)=\frac12\log\frac{2+|a|}{2\pi}.
\tag{L-105221.9}
\]

On each of the fixed lines `Re(s)=3/2,5/2,7/2`, Stirling's formula and absolute
convergence of the zeta Euler product give

\[
L_h(a):=\frac{\xi'}{\xi}(s_h(a))
=
\ell(a)+q_h(a),
\qquad
q_h(a)=O(1),
\tag{L-105221.10}
\]

and every fixed derivative of `L_h` is `O_j(1)`.

The complete Bell-polynomial formula for `xi^(j)/xi` shows first that
`xi^(k)(s_h)` and `xi^(k+1)(s_h)` are nonzero for all sufficiently large
`|a|`; it then gives, uniformly in `h=1,2,3` for fixed `k`,

\[
U_{k,h}
=
L_h+k\frac{L_h'}{L_h}+O_k(\ell^{-2}),
\tag{L-105221.11}
\]

\[
S_{k,h}
=
L_h^{-1}-(k-1)\frac{L_h'}{L_h^3}
+O_k(\ell^{-4}),
\tag{L-105221.12}
\]

and

\[
V_{k,h}
=
L_h^{-3}+(2-3k)\frac{L_h'}{L_h^5}
+O_k(\ell^{-6}).
\tag{L-105221.13}
\]

Let

\[
Q(a)=\sum_hd_h\Re q_h(a).
\]

Expanding in powers of `ell^-1` yields

\[
\boxed{
\mathcal N_k
=
D\ell+Q+O_k(\ell^{-1}),
}
\tag{L-105221.14}
\]

\[
\boxed{
\mathcal A_k
=
D\ell^{-1}-Q\ell^{-2}+O_k(\ell^{-3}),
}
\tag{L-105221.15}
\]

and

\[
\boxed{
\mathcal B_k
=
D\ell^{-3}-3Q\ell^{-4}+O_k(\ell^{-5}).
}
\tag{L-105221.16}
\]

In particular all three carriers are positive for sufficiently large `|a|`.

## 3. Coherence cancellation

The coefficients of `ell^-2` and `ell^-3` cancel identically in

\[
\mathcal D_k(a)
=
\mathcal N_k(a)\mathcal B_k(a)-\mathcal A_k(a)^2.
\]

Hence

\[
\boxed{
\mathcal D_k(a)=O_k(\ell(a)^{-4}).
}
\tag{L-105221.17}
\]

Since

\[
\mathcal N_k\mathcal B_k
=
D^2\ell^{-2}(1+O_k(\ell^{-1})),
\]

one obtains

\[
\boxed{
\frac{\mathcal A_k(a)^2}
{\mathcal N_k(a)\mathcal B_k(a)}
=
1+O_k(\ell(a)^{-2}).
}
\tag{L-105221.18}
\]

The `L_h'` contributions cancel from the first nonzero formal defect
coefficient. If

\[
Q_2(a)=\sum_hd_h\Re(q_h(a)^2),
\]

then the purely algebraic leading term is

\[
\boxed{
\mathcal D_k(a)
=
4\bigl(DQ_2-Q^2\bigr)\ell^{-4}
+O_k(\ell^{-5}),
}
\tag{L-105221.19}
\]

provided the displayed bounded coefficient functions are expanded one order
further.

The improvement over the triple-pole localizer is structural: no boundary
derivatives of the ratios are taken, and the common first-order perturbation
cancels automatically between count, mean, and second moment.

## 4. Scope

Equations (L-105221.17)--(L-105221.18) concern the **complete boundary
carriers**. They do not identify them with the real-critical moments. The
nonreal-critical corrections and the adjacent-derivative/Bézout correction are
load bearing and are isolated exactly in `L-105222`. No RH conclusion follows
from the safe-line asymptotic alone.
