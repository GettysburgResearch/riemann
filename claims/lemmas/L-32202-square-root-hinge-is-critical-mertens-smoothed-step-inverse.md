# L-32202 — The square-root hinge is a critical Mertens-smoothed step inverse

Claim ID: `L-32202`
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**
Created: 2026-08-08
Dependencies: the carry matrix and its Mobius adjoint identity `D-23801/L-23803`
Scope: exact finite decomposition and proof firewall; no positivity theorem

## 1. Step targets

For an endpoint `N>=2`, define

\[
e_N(q)=\mathbf 1_{2\le q\le N}.
\]

Let `s_N(j)` be the unique carry coefficient satisfying

\[
e_N(q)=\sum_{j=q}^{N}s_N(j)\beta_{jq}.
\tag{L-32202.1}
\]

Embedding this target into any larger endpoint does not change its inverse:
all coefficients above `N` are forced to zero by triangularity.

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\]

The exact Mobius coordinate of the step target is

\[
u_m=M(\lfloor N/m\rfloor).
\tag{L-32202.2}
\]

Substitution in the exact carry-adjoint inverse gives

\[
\boxed{
 s_N(j)=
 \frac{
 (j+1)\left[
 jM(\lfloor N/j\rfloor)
 -(j-2)M(\lfloor N/(j+1)\rfloor)
 \right]
 +2\sum_{m=j+2}^{N}M(\lfloor N/m\rfloor)
 }{j(j-1)}.}
\tag{L-32202.3}
\]

Thus a constant step already carries an explicit Mertens channel.  The values
`s_N(j)` need not be nonnegative.

## 2. Exact hinge mixture

For `T>=3` put

\[
h_T(q)=
\begin{cases}
q^{-1/2}-T^{-1/2},&2\le q\le T,\\
0,&q>T.
\end{cases}
\tag{L-32202.4}
\]

Let

\[
\delta_N=N^{-1/2}-(N+1)^{-1/2}>0.
\tag{L-32202.5}
\]

The finite telescope is

\[
\boxed{
h_T(q)=\sum_{N=2}^{T-1}\delta_N e_N(q).}
\tag{L-32202.6}
\]

By linearity and uniqueness of the triangular inverse, the exact hinge
coefficient is therefore

\[
\boxed{
 c_T(j)=\sum_{N=j}^{T-1}\delta_N s_N(j).}
\tag{L-32202.7}
\]

This is a positive square-root smoothing of an oscillatory Mertens step inverse.
It explains both the exceptional numerical stability of the hinge and why a
finite positivity scan cannot be promoted to a theorem.

## 3. Endpoint update

Equivalently,

\[
h_{T+1}=h_T+\delta_Te_T
\]

on the common columns, and hence

\[
\boxed{
 c_{T+1}(j)=c_T(j)+\delta_Ts_T(j),
 \qquad2\le j\le T.}
\tag{L-32202.8}
\]

Because `s_T(j)` has genuine sign changes, hinge positivity is not monotone in
the endpoint by a coefficientwise argument.  Any proposed endpoint induction
must control the complete signed term in (L-32202.8).

## 4. Continuum Mellin firewall

The scaled carry kernel has Mellin symbol

\[
I(p)=\frac{p-2}{p(p-1)}\zeta(p-1).
\]

For the normalized hinge target

\[
g(t)=t^{-1/2}-1,
\qquad0<t\le1,
\]

one has

\[
\int_0^1g(t)t^{z-1}dt
=\frac1{2z(z-1/2)}.
\]

Writing `p=z+1`, the formal inverse Mellin transform has

\[
\boxed{
F_h(p)=
\frac{p}{2(p-2)(p-3/2)\zeta(p-1)}.}
\tag{L-32202.9}
\]

Its first mass is

\[
\boxed{F_h(2)=2.}
\tag{L-32202.10}
\]

The reciprocal-zeta factor is therefore present already in a single
square-root hinge.  Full hinge positivity is not a generic matrix-positivity or
smoothness lemma; it is legitimately RH-sensitive.

## 5. Proof boundary

Closed exactly:

- the Mertens formula for the step inverse;
- the positive step-mixture representation of a hinge;
- the exact endpoint update;
- the reciprocal-zeta continuum firewall and mass two.

Open:

- the sign of the complete sum (L-32202.7) for arbitrary `T,j`;
- Critical Hinge Saturation;
- RH.
