# L-105324 — Local root temperature changes by an exact weighted winding flux

Claim ID: `L-105324`  
Status: **PROPOSED EXACT ENTIRE-FUNCTION IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105323`; parent entire-window residue flux `L-105204`  
RH status: **not assumed**

## 1. Window root moments

Let `F` be entire and let `Omega` be a bounded positively oriented Jordan
domain such that neither `F` nor `F'` vanishes on `partial Omega`. Zeros are
counted with multiplicity. Put

\[
N_F={1\over2\pi i}\int_{\partial\Omega}{F'(z)\over F(z)}\,dz
\tag{L-105324.1}
\]

and, for `k=1,2`,

\[
S_k(F;\Omega)
={1\over2\pi i}\int_{\partial\Omega}
 z^k{F'(z)\over F(z)}\,dz
=
\sum_{\substack{F(\rho)=0\\\rho\in\Omega}}\rho^k.
\tag{L-105324.2}
\]

When `N_F>=2`, define the local centered root temperature

\[
\boxed{
\mathcal T_\Omega(F)
={N_FS_2(F;\Omega)-S_1(F;\Omega)^2
 \over N_F^2(N_F-1)}.
}
\tag{L-105324.3}
\]

Equivalently, if

\[
\bar\rho_\Omega={S_1(F;\Omega)\over N_F},
\]

then

\[
\mathcal T_\Omega(F)
={1\over N_F(N_F-1)}
\sum_{F(\rho)=0,\ \rho\in\Omega}
(\rho-\bar\rho_\Omega)^2.
\tag{L-105324.4}
\]

For a polynomial and a domain containing every zero, this is exactly the
finite invariant `mathcal T(p)` of `L-105323`.

## 2. Weighted logarithmic-derivative flux

Let

\[
L_F(z)={F'(z)\over F(z)}.
\]

The divisor of `L_F` is the zero divisor of `F'` minus the zero divisor of
`F`. Define

\[
\boxed{
\Delta_k(F;\Omega)
={1\over2\pi i}
\int_{\partial\Omega}
 z^k{L_F'(z)\over L_F(z)}\,dz,
\qquad k=0,1,2.
}
\tag{L-105324.5}
\]

The identity

\[
{L_F'\over L_F}
={F''\over F'}-{F'\over F}
\]

gives, without any simplicity assumption,

\[
\boxed{
\begin{aligned}
N_{F'}&=N_F+\Delta_0,\\
S_1(F';\Omega)&=S_1(F;\Omega)+\Delta_1,\\
S_2(F';\Omega)&=S_2(F;\Omega)+\Delta_2.
\end{aligned}
}
\tag{L-105324.6}
\]

Thus `Delta_0` is the ordinary derivative-versus-parent winding charge, while
`Delta_1` and `Delta_2` are its first and second spatial moments.

## 3. Exact localized temperature transport

Write

\[
N=N_F,
\qquad
S_1=S_1(F;\Omega),
\qquad
S_2=S_2(F;\Omega),
\qquad
M=N+\Delta_0.
\]

Assume `N,M>=2`. Substitution of (L-105324.6) into (L-105324.3) gives

\[
\boxed{
\begin{aligned}
\mathcal T_\Omega(F')-\mathcal T_\Omega(F)
={}&
{M(S_2+\Delta_2)-(S_1+\Delta_1)^2
 \over M^2(M-1)}\\
&-
{NS_2-S_1^2\over N^2(N-1)}.
\end{aligned}
}
\tag{L-105324.7}
\]

This is the exact height-localized replacement for the global derivative
invariance of `L-105323`. Every failure of local temperature conservation is
carried by the three explicit boundary fluxes `Delta_0,Delta_1,Delta_2`.

No exterior zero sum is hidden in an error term: it is encoded by the
logarithmic-derivative winding on `partial Omega`.

## 4. Symmetric Xi rectangles

Suppose `Omega` is invariant under `z -> -z` and `F` has definite parity.
Then both the parent and derivative zero multisets in `Omega` are symmetric,
so

\[
S_1(F;\Omega)=0,
\qquad
\Delta_1(F;\Omega)=0.
\]

Equation (L-105324.7) simplifies to

\[
\boxed{
\mathcal T_\Omega(F')-\mathcal T_\Omega(F)
=
{S_2+\Delta_2\over M(M-1)}
-
{S_2\over N(N-1)}.
}
\tag{L-105324.8}
\]

Thus the local derivative-temperature defect in a symmetric Xi rectangle is a
two-input object:

```text
ordinary zero-count / winding flux Delta_0;
second-moment winding flux Delta_2.
```

The first spatial flux vanishes identically by parity.

## 5. Global polynomial recovery

Let `F=p` be a polynomial of degree `n`, and let `Omega` contain every zero of
`p` and `p'`. Then

\[
N=n,
\qquad M=n-1,
\qquad\Delta_0=-1.
\]

The coefficient identity for the derivative roots gives

\[
\Delta_1=-{S_1\over n},
\qquad
\Delta_2=-{2\over n}S_2+{S_1^2\over n^2}
\]

in uncentered coordinates. Inserting these values into (L-105324.7) gives

\[
\boxed{
\mathcal T_\Omega(p')=\mathcal T_\Omega(p).
}
\]

This recovers `L-105323` as the zero-leakage global case. For centered or
parity-symmetric `p`, the fluxes reduce to

\[
\Delta_1=0,
\qquad
\Delta_2=-{2\over n}S_2.
\]

## 6. Exact bridge to the first critical-residue flux

Assume now that the critical points of `F` in `Omega` are simple and that
`F'` has no boundary zero. The parent entire-window theorem defines

\[
B_{1,F}(\Omega)
={1\over2\pi i}
\int_{\partial\Omega}{F(z)\over F'(z)}\,dz
=
\sum_{F'(c)=0,\ c\in\Omega}{F(c)\over F''(c)}.
\tag{L-105324.9}
\]

Define the local carrier-leakage functional

\[
\boxed{
\mathcal E_\Omega(F)
=-{N_F\over N_F-1}B_{1,F}(\Omega)
-\mathcal T_\Omega(F).
}
\tag{L-105324.10}
\]

For a polynomial window containing the complete root and critical sets,
`mathcal E=0` by `L-104524` and `L-105323`. In a finite entire-function window,
`mathcal E` is an explicit boundary functional: both terms on the right of
(L-105324.10) are contour integrals on the same boundary.

If `C_(1,F)` denotes the nonreal-critical correction of the parent window
identity, the real first residue moment is exactly

\[
\boxed{
M_{1,F}(\Omega)
={N_F-1\over N_F}
\left[\mathcal T_\Omega(F)+\mathcal E_\Omega(F)\right]
+C_{1,F}(\Omega).
}
\tag{L-105324.11}
\]

This separates the first-moment input into:

```text
local root temperature;
carrier leakage through the boundary;
nonreal critical-point correction.
```

## 7. Xi consequence and new target

Apply the theorem to

\[
F=\Xi^{(j)}
\]

on a regular parity-symmetric rectangle. The ordinary Levinson winding term is
`Delta_0`; the new weighted companion is `Delta_2`. Therefore the finite
residue-temperature invariant and the complex reverse-Rolle boundary ledger
are two moments of the **same logarithmic-derivative flux**.

A sufficient continuation is:

```text
WTL105324:
  the cumulative second-moment winding leakage and carrier leakage across the
  first O(T log T) derivative levels are subunit after the exact Delta_0
  transport is included.
```

Together with the normalized curvature-variance budget of `T-105323`, this
implies `CRDB105200` and hence RH. `WTL105324` remains open.

## 8. Scope

This theorem is an exact contour identity, not a bound. The local temperature
may be complex when the window contains nonreal roots. It does not show that
`Delta_2` or `mathcal E` has a favorable sign. It does not justify exchanging
canonical-product and height limits. It supplies the missing exact interface
between the finite derivative invariant and the Xi boundary/winding programme;
RH remains unproved.
