# L-105204 — Entire-window first critical-residue flux

Claim ID: `L-105204`  
Status: **PROVED EXACT ENTIRE-FUNCTION IDENTITY**  
Created: 2026-08-23  
Depends on: PR #723 `L-105101` for the common rectangle conventions  
RH status: **not assumed**

## 1. Exact rectangle identity

Let `F` be entire, real on the real axis, and let

\[
\Omega_{T,\eta}
=\{z:|\Re z|<T,\ |\Im z|<\eta\}
\]

be oriented counterclockwise. Assume every zero `c` of `F'` in the closed
rectangle is simple and `F'` has no zero on the boundary. Put

\[
P_F(z)={F(z)\over F'(z)}.
\tag{L-105204.1}
\]

At a zero `c` of `F'`,

\[
\operatorname{Res}_{z=c}P_F(z)
={F(c)\over F''(c)}
=:\rho_c.
\tag{L-105204.2}
\]

If `F(c)=0`, the singularity is removable and the displayed residue is zero.
There are no other poles. Therefore

\[
\boxed{
B_{1,F}(T,\eta)
:={1\over2\pi i}
\int_{\partial\Omega_{T,\eta}}P_F(z)\,dz
=
\sum_{\substack{F'(c)=0\\c\in\Omega_{T,\eta}}}\rho_c.
}
\tag{L-105204.3}
\]

This is the first-moment companion of the second-residue identity
`L-105101.8`.

## 2. Real/nonreal split

Define

\[
M_{1,F}(T)
=-\sum_{\substack{-T<c<T\\c\in\mathbb R,\ F'(c)=0}}
{F(c)\over F''(c)}
\tag{L-105204.4}
\]

and the algebraic nonreal correction

\[
C_{1,F}(T,\eta)
=
\sum_{\substack{F'(c)=0,\ c\in\Omega_{T,\eta}\\c\notin\mathbb R}}
\rho_c.
\tag{L-105204.5}
\]

Conjugate pairing makes `C_(1,F)` real. Splitting (L-105204.3) gives

\[
\boxed{
M_{1,F}(T)
=-B_{1,F}(T,\eta)+C_{1,F}(T,\eta).
}
\tag{L-105204.6}
\]

If the rectangle contains no nonreal zero of `F'`, then the first residue
moment is exactly minus one boundary flux.

## 3. Four-edge formula

Schwarz reflection gives

\[
\boxed{
\begin{aligned}
B_{1,F}(T,\eta)
={}&-{1\over\pi}
\int_{-T}^{T}\Im P_F(x+i\eta)\,dx\\
&+{1\over2\pi}
\int_{-\eta}^{\eta}
\left[P_F(T+iy)-P_F(-T+iy)\right]dy.
\end{aligned}
}
\tag{L-105204.7}
\]

If `F` has definite parity, then `P_F` is odd. Hence

\[
\boxed{
B_{1,F}(T,\eta)
={2\over\pi}
\left[
\int_0^\eta\Re P_F(T+iy)\,dy
-
\int_0^T\Im P_F(x+i\eta)\,dx
\right].
}
\tag{L-105204.8}
\]

The signs agree with the counterclockwise orientation used in `L-105101`.

## 4. Two-flux coherence identity

Under the simultaneous regularity hypotheses of `L-105101`, put

\[
B_{2,F}(T,\eta)
={1\over2\pi i}
\int_{\partial\Omega_{T,\eta}}
{F(z)^2\over F'(z)F''(z)}\,dz.
\]

Let `C_(2,F)` and `D_F` be the nonreal squared-residue correction and the
`F''`-zero debt of `L-105101`. Then

\[
M_{2,F}(T)=B_{2,F}-C_{2,F}-D_F.
\]

If `R_F(T)` is the number of real zeros of `F'` in the interval, the exact
residue coherence is therefore

\[
\boxed{
\mathfrak C_F(T)
=
{\bigl(-B_{1,F}+C_{1,F}\bigr)_+^2
\over
R_F(T)\bigl(B_{2,F}-C_{2,F}-D_F\bigr)}.
}
\tag{L-105204.9}
\]

This formula uses two explicit contour fluxes and three explicit correction
ledgers. It contains no unknown parent real-zero count.

## 5. Xi derivative specialization

For `F=Xi^(m)`, equations (L-105204.4) and (L-105204.9) are precisely the first
moment and coherence statistic used in `RCMV104530`, with index shifted by one.
The positive Fourier saddle evaluates the two fluxes and the adjacent debt in
the high derivative tail in `L-105205`.

## 6. Scope

The identity supplies no bound on a boundary flux or correction. Multiple
critical points require confluent residues. A height-uniform choice of `eta`
is not asserted. The theorem is an exact finite-window coordinate, not a proof
of residue coherence or RH.
