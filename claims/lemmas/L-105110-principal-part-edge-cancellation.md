# L-105110 — Exterior principal-part edge cancellation

Claim ID: L-105110

Status: **PROPOSED EXACT FINITE-EDGE THEOREM**

Created: 2026-08-23

Depends on: L-105103; L-105105; L-105107; L-105109

RH status: **unproved**

## 1. The straight-edge kernel

Let

\[
E=\{z_0+ut:-A\le t\le B\},
\qquad |u|=1,
\tag{L-105110.1}
\]

be oriented in the direction of increasing \(t\), where \(A,B>0\).
For \(\delta>0\), \(\sigma\in\{-1,1\}\), put

\[
p_{\delta}=z_0+i\sigma u\delta.
\tag{L-105110.2}
\]

Direct integration gives

\[
\boxed{
\begin{aligned}
J_{\sigma}(A,B;\delta)
&:=\int_E\frac{dz}{z-p_\delta}\\
&=\frac12\log\frac{B^2+\delta^2}{A^2+\delta^2}
+i\sigma\left[
\arctan\frac B\delta+\arctan\frac A\delta
\right].
\end{aligned}
}
\tag{L-105110.3}
\]

The corresponding absolute integral is

\[
\boxed{
\int_E\frac{|dz|}{|z-p_\delta|}
=\operatorname{arsinh}\frac A\delta
+\operatorname{arsinh}\frac B\delta.
}
\tag{L-105110.4}
\]

Thus normal approach of a simple pole makes the absolute integral diverge,
while the oriented integral stays bounded whenever its tangential projection
stays uniformly inside the edge.  More precisely, if

\[
0<\kappa\le A,B\le\ell,
\tag{L-105110.5}
\]

then

\[
\boxed{
|J_\sigma(A,B;\delta)|
\le \pi+\log\frac\ell\kappa,
}
\tag{L-105110.6}
\]

independently of \(\delta\).  In the centered case \(A=B=a\),

\[
J_\sigma(a,a;\delta)
=2i\sigma\arctan(a/\delta),
\qquad |J_\sigma|<\pi.
\tag{L-105110.7}
\]

The endpoint condition is load bearing.  If the pole projects to the initial
endpoint, then

\[
\boxed{
J_\sigma(0,B;\delta)
=\frac12\log\frac{B^2+\delta^2}{\delta^2}
+i\sigma\arctan\frac B\delta,
}
\tag{L-105110.8}
\]

whose real part diverges as \(\delta\downarrow0\).  A corner event therefore
requires either a two-edge paired calculation or a separate corner margin.

## 2. A finite principal-part certificate

Let \(H_\nu\) be meromorphic in a two-sided neighborhood of the open edge
\(E\), and suppose its exterior simple poles that approach \(E\) have the
finite decomposition

\[
H_\nu(z)=R_\nu(z)
+\sum_{j=1}^{m_\nu}\frac{r_{\nu,j}}{z-p_{\nu,j}}.
\tag{L-105110.9}
\]

Assume:

1. every normal projection of \(p_{\nu,j}\) lies on the open edge and its
   two tangential endpoint distances lie in \([\kappa,\ell]\);
2. the weighted residue ledger is uniformly summable,
   \(\sum_j|r_{\nu,j}|\le C_{\rm pp}\);
3. the pole-subtracted remainder obeys
   \(\int_E|R_\nu(z)|\,|dz|\le C_{\rm rem}\).

Then (L-105110.3) and the triangle inequality give the collar-independent
oriented-edge estimate

\[
\boxed{
\left|\int_EH_\nu(z)\,dz\right|
\le
C_{\rm rem}
+\left(\pi+\log\frac\ell\kappa\right)C_{\rm pp}.
}
\tag{L-105110.10}
\]

The estimate deliberately pays the remainder in \(L^1\), but it does not pay
the singular principal parts in boundary supremum or absolute-integral norm.
It remains valid as their normal collar distances tend to zero.

For a weighted first quotient, a simple exterior zero \(p\) of \(F'\), with
\(F(p)F''(p)\ne0\), contributes

\[
r_{1,p}=\frac{W_1(p)}{\mathscr L_F'(p)}.
\tag{L-105110.11}
\]

For a weighted second quotient, the same event contributes

\[
r_{2,p}
=\frac{W_2(p)}{\mathscr L_F'(p)\mathscr A_F(p)}
=\frac{W_2(p)}{\mathscr L_F'(p)^2},
\tag{L-105110.12}
\]

while a simple exterior zero \(q\) of \(F''\), with
\(F(q)F'(q)F'''(q)\ne0\), contributes

\[
r_{2,q}
=\frac{W_2(q)}{\mathscr L_F(q)\mathscr A_F'(q)}.
\tag{L-105110.13}
\]

Here \(\mathscr L_F=F'/F\) and \(\mathscr A_F=F''/F\).  Applying
(L-105110.10) therefore requires meromorphic continuation of the *weighted*
quotient across the open edge, completeness of its exterior principal-part
list, corner separation, a weighted-residue \(\ell^1\) bound, and an
\(L^1\) estimate for what remains after subtraction.

Multiple or common exterior events require their full confluent principal
parts and coefficient bounds.  They are not covered by the simple-pole
statement (L-105110.10).

## 3. Both quotient suprema can diverge while the edges stay bounded

For

\[
0<a\le\frac12,
\qquad
0<\delta\le\frac12,
\tag{L-105110.14}
\]

define the real zero-free entire function

\[
F_\delta(z)=\exp(z^2/2-\delta z),
\qquad w=z-\delta.
\tag{L-105110.15}
\]

Then

\[
\mathscr L_\delta=w,
\qquad
\mathscr A_\delta=w^2+1,
\tag{L-105110.16}
\]

and hence

\[
\boxed{
h_{1,\delta}=\frac1w,
\qquad
h_{2,\delta}=\frac1{w(w^2+1)}
=\frac1w-\frac{w}{w^2+1}.
}
\tag{L-105110.17}
\]

On the upward edge

\[
E_a=\{iy:-a\le y\le a\},
\tag{L-105110.18}
\]

one obtains exactly

\[
\boxed{
I_{1}(a,\delta)
:=\int_{E_a}h_{1,\delta}(z)\,dz
=-2i\arctan(a/\delta),
}
\tag{L-105110.19}
\]

and, because \(1+\delta^2-a^2>0\),

\[
\boxed{
\begin{aligned}
I_{2}(a,\delta)
&:=\int_{E_a}h_{2,\delta}(z)\,dz\\
&=-2i\arctan(a/\delta)
+i\arctan\frac{2a\delta}{1+\delta^2-a^2}.
\end{aligned}
}
\tag{L-105110.20}
\]

For fixed \(a>0\), both converge to \(-i\pi\) as
\(\delta\downarrow0\), and in particular remain uniformly bounded.  In
contrast,

\[
|h_{1,\delta}(0)|=\frac1\delta,
\qquad
|h_{2,\delta}(0)|=\frac1{\delta(1+\delta^2)},
\tag{L-105110.21}
\]

and

\[
\int_{E_a}|h_{1,\delta}|\,|dz|
=2\operatorname{arsinh}(a/\delta).
\tag{L-105110.22}
\]

On the stated parameter box,
\(\Re(1+w^2)=1+\delta^2-y^2\ge3/4\) and
\(|1+w^2|\le3/2\).  Direct algebra therefore gives

\[
\frac23|h_{1,\delta}|
\le |h_{2,\delta}|
\le\frac43|h_{1,\delta}|.
\tag{L-105110.23}
\]

Thus both absolute edge integrals diverge for fixed \(a\), while both
oriented integrals stay bounded.  If the edge is cut at the projected event,
however,

\[
\int_0^{ia}h_{1,\delta}(z)\,dz
=\frac12\log\frac{a^2+\delta^2}{\delta^2}
-i\arctan(a/\delta),
\tag{L-105110.24}
\]

so the one-sided piece diverges.  Symmetric cancellation is not a bound for
arbitrary edge partitions.

The pole \(\delta\) is exterior to a left-hand rectangle whose right edge is
\(E_a\).  That rectangle has an empty interior pole manifest, so the unit
weight in (L-105110.19)--(L-105110.20) is a fixed test weight, **not** the
L-105107 optimum for an empty interpolation problem (which is zero).

## 4. Stable manifest data do not control the remainder

The certificate (L-105110.10) is not automatic.  For every integer \(N\ge1\)
let

\[
\boxed{
F_N(z)=
\exp\!\left(\frac{1-e^{-Nz^2}}{2N}\right).
}
\tag{L-105110.25}
\]

This function is real, even, entire, and zero-free, with

\[
\mathscr L_N(z)=ze^{-Nz^2},
\qquad
\frac{F_N}{F_N'}(z)=\frac{e^{Nz^2}}z.
\tag{L-105110.26}
\]

Consequently \(F_N'\) has exactly the one simple zero \(0\) in the entire
plane.  The complete first-quotient manifest in every window containing zero
is the same simple target, its residue is one, and its boundary-optimal
selector is

\[
W_{1,N,*}=1,
\qquad \tau_{1,N}=1.
\tag{L-105110.27}
\]

Set

\[
\eta_N=\frac1{8N},
\qquad
\Omega_N=\{z:|\Re z|<1,\ |\Im z|<\eta_N\},
\tag{L-105110.28}
\]

and orient the right edge

\[
E_N=\{1+iy:-\eta_N\le y\le\eta_N\}
\tag{L-105110.29}
\]

upward.  Its integral is purely positive imaginary, and

\[
\begin{aligned}
\Im\int_{E_N}\frac{F_N}{F_N'}\,dz
={}&2e^N\int_0^{\eta_N}e^{-Ny^2}
\frac{\cos(2Ny)+y\sin(2Ny)}{1+y^2}\,dy\\
\ge{}&\frac{16}{65N}e^{N-1/64}\cos(1/4)
>\frac{e^N}{5N}.
\end{aligned}
\tag{L-105110.30}
\]

The last strict bound uses only
\(\cos(1/4)\ge31/32\) and
\(e^{-1/64}\ge63/64\).  Since \(e^N\ge N^3/6\),

\[
\boxed{
\left|\int_{E_N}\frac{F_N}{F_N'}\,dz\right|
>\frac{N^2}{30}.
}
\tag{L-105110.31}
\]

Nevertheless the full contour identity remains

\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega_N}
\frac{F_N}{F_N'}\,dz=1.
}
\tag{L-105110.32}
\]

There is no exterior critical point to subtract: the pole-subtracted
remainder is the whole edge carrier, and its individual oriented integral is
unbounded.  The other three edges cancel the growing right-edge contribution
in the full contour sum.

## 5. Boundary of the result

The theorem supplies a finite sufficient certificate for cancellation of
exterior simple-event principal parts and proves that the remaining
holomorphic edge term is independent, load-bearing data.  It does not
supply:

- meromorphic continuation of Xi selectors and quotients across changing
  rectangle edges;
- a complete Xi exterior-event or confluent principal-part manifest;
- cofinal weighted exterior-residue bounds or corner separation;
- an estimate for the pole-subtracted Xi remainder;
- a second-quotient analogue of the family (L-105110.25);
- cofinal Green–Gram control, strict jet coherence, RCMV104530, or RH.

The family (L-105110.25) varies with \(N\), has infinite order, and uses
shrinking-height finite windows.  It is not an Xi-class or fixed-function
cofinal model.  It refutes only the inference that parity, a stable complete
manifest, fixed target data, and bounded optimal selectors automatically
control each oriented edge.

No novelty is claimed for integration of the Cauchy kernel, elementary
partial fractions, or the residue theorem.  The contribution is their exact
placement in the L-105109 cancellation fork and the separation of the
exterior-event principal-part debt from the pole-subtracted remainder debt.

The closest programme antecedents are L-104512/L-104521/L-104523 in draft PR
#720, which identify phase and contour quantities without closing these
weighted oriented edges; PR #720 L-104519, which controls a different
Hermite--Biehler log-derivative-difference edge under an ordered far-right
exhaustion; R-105106, which requires retention of a holomorphic remainder;
and L/T-105109, which leave phase-sensitive cancellation open.
