# L-105115 - Common safe-rectangle projection and restricted averaging

Claim ID: L-105115

Status: **PROPOSED EXACT FINITE GEOMETRIC LEMMA; XI INPUT OPEN**

Created: 2026-08-23

Depends on: L-105113 for the shell-average interface and L-105114 for a
possible analytic source of the finite disk family

RH status: **unproved**

## 1. Supporting-line certificate

Let

\[
D_j=\overline D(x_j+iy_j,r_j),\qquad r_j>0,\qquad
S=\sum_{j=1}^N r_j,
\]

be a finite family of closed positive-radius disks.  Let

\[
0\le T_0<T_1,\qquad 0\le\eta_0<\eta_1,
\]

write

\[
I_T=(T_0,T_1),\quad I_\eta=(\eta_0,\eta_1),\quad
\Delta_T=T_1-T_0,\quad\Delta_\eta=\eta_1-\eta_0,
\]

and set

\[
\Omega_{T,\eta}=\{z:|\Re z|<T,\ |\Im z|<\eta\}.
\]

Define the bad supporting-line parameters

\[
B_T=\bigcup_{j=1}^N
\left([|x_j|-r_j,|x_j|+r_j]\cap I_T\right),
\tag{L-105115.1}
\]

\[
B_\eta=\bigcup_{j=1}^N
\left([|y_j|-r_j,|y_j|+r_j]\cap I_\eta\right),
\tag{L-105115.2}
\]

where the intersections are relative to the open parameter intervals, and
let \(G_T=I_T\setminus B_T\), \(G_\eta=I_\eta\setminus B_\eta\).

For \(T\ge0\),

\[
\min\{|T-x_j|,|-T-x_j|\}=|T-|x_j||.
\tag{L-105115.3}
\]

Thus one of the two full vertical lines \(\Re z=\pm T\) meets \(D_j\)
if and only if \(T\in[|x_j|-r_j,|x_j|+r_j]\).  The horizontal statement
is identical.  Consequently, every

\[
(T,\eta)\in G_T\times G_\eta
\tag{L-105115.4}
\]

satisfies

\[
\partial\Omega_{T,\eta}\cap\bigcup_{j=1}^N D_j=\varnothing.
\tag{L-105115.5}
\]

This is an exact characterization of the coordinatewise *full supporting-
line certificate*.  It is only a sufficient product subset of all safe
rectangle parameters: a full supporting line can meet a disk beyond the
finite side segment even when the actual rectangle boundary is safe.

## 2. Exact measure gate and the sharp \(2S\) relaxation

The sets \(B_T,B_\eta\) are finite unions of relatively closed intervals.
Their complements are relatively open.  Hence the certified safe product
is nonempty if and only if it has positive measure, equivalently

\[
|B_T|<\Delta_T,\qquad |B_\eta|<\Delta_\eta.
\tag{L-105115.6}
\]

Writing

\[
g_T=\Delta_T-|B_T|,\qquad
g_\eta=\Delta_\eta-|B_\eta|,
\tag{L-105115.7}
\]

one has

\[
|G_T\times G_\eta|=g_Tg_\eta.
\tag{L-105115.8}
\]

Every interval in (L-105115.1) or (L-105115.2) has length at most \(2r_j\),
so subadditivity gives

\[
|B_T|\le2S,\qquad |B_\eta|\le2S.
\tag{L-105115.9}
\]

Therefore the clean radius-only gate is the strict pair

\[
\boxed{\Delta_T>2S,\qquad\Delta_\eta>2S.}
\tag{L-105115.10}
\]

Both the factor two and strictness are sharp when only \(S\) is known.  If
\(\Delta_T\le2S\), one disk of radius \(S\), centered at
\(((T_0+T_1)/2,0)\), meets the right supporting line for every
\(T\in I_T\).  The horizontal analogue proves the same statement for
\(I_\eta\).  This is coordinatewise worst-case sharpness, not a claim that
one disk must saturate both coordinate gates simultaneously.

## 3. Restricted Tonelli selection

Let \(q:I_T\times I_\eta\to[0,\infty]\) be measurable and integrable, and
put

\[
Q=\int_{I_T\times I_\eta}q(T,\eta)\,d\eta\,dT.
\]

If (L-105115.6) holds, then averaging \(q\) over the positive-measure safe
product gives a pair \((T_*,\eta_*)\in G_T\times G_\eta\), outside any
separately declared null exceptional set, such that

\[
q(T_*,\eta_*)\le\frac{Q}{g_Tg_\eta}.
\tag{L-105115.11}
\]

Relative to the unrestricted mean, the exact parameter-normalization factor is

\[
\kappa=\frac{\Delta_T\Delta_\eta}{g_Tg_\eta}.
\tag{L-105115.12}
\]

Under (L-105115.10), (L-105115.9) further gives

\[
\kappa\le
\frac{\Delta_T\Delta_\eta}
{(\Delta_T-2S)(\Delta_\eta-2S)}.
\tag{L-105115.13}
\]

This is a crude total-radius relaxation; overlapping projections can make
the exact loss in (L-105115.12) much smaller.

The full-shell integrability hypothesis is load bearing for the comparison
with the unrestricted mean.  Uncancelled raw quotients can be undefined or
nonintegrable on unsafe shells.  In that case one may average a separately
integrable cost only over \(G_T\times G_\eta\), using its restricted
integral; one may not import the unrestricted L-105113 budget or the factor
\(\kappa\) without a removable continuation or an independent full-shell
integrability proof.

## 4. Raw quotient transfer

Assume that \(F\) is holomorphic in a neighborhood of
\(\overline\Omega_{T_1,\eta_1}\) and that, on this closed outer rectangle
outside the disks,

\[
|F|\le M_0,\qquad |F'|\ge a_1>0,\qquad |F''|\ge a_2>0.
\tag{L-105115.14}
\]

For every certified safe boundary \(E=\partial\Omega_{T,\eta}\),

\[
\left\|\frac F{F'}\right\|_E\le\frac{M_0}{a_1},
\qquad
\left\|\frac{F^2}{F'F''}\right\|_E
\le\frac{M_0^2}{a_1a_2}.
\tag{L-105115.15}
\]

Zeros of \(F\) on \(E\) are harmless: the denominators are nonzero and the
raw quotients vanish.  Rewriting through \(F'/F\) or \(F''/F\) would lose
this advantage.

For continuous weights \(W_1,W_2\), define

\[
I_j(E)=\int_E|W_j|\,|dz|,\qquad b_j(E)=\|W_j\|_E.
\]

Since \({\rm len}(E)=4(T+\eta)\),

\[
\int_E\left|W_1\frac F{F'}\right|\,|dz|
\le\frac{M_0}{a_1}I_1(E)
\le4(T+\eta)\frac{M_0}{a_1}b_1(E),
\tag{L-105115.16}
\]

\[
\int_E\left|W_2\frac{F^2}{F'F''}\right|\,|dz|
\le\frac{M_0^2}{a_1a_2}I_2(E)
\le4(T+\eta)\frac{M_0^2}{a_1a_2}b_2(E).
\tag{L-105115.17}
\]

The fixed-carrier hypothesis is load bearing when these costs are inserted
into L-105113.  L-105107 guarantees constant-boundary-modulus equality only
on the boundary of the exact selector domain; it does not imply equality on
an intermediate boundary.  Rebuilding the selector for each parameter pair
does not preserve the fixed-carrier Tonelli argument.

## 5. Boundary of the result

L-105114 can supply a finite disk family and the pointwise lower bounds
needed in (L-105115.14), but this lemma does not authenticate those inputs
for Xi at cofinal scale.  It does not prove that \(2S\) fits inside a
prescribed Xi shell, that the actual quotient-pole manifests are complete,
or that reciprocal margins, projection loss, edge length, and selector
conditioning are absorbable.  It proves no signed lower bound, RCMV104530,
or RH.
