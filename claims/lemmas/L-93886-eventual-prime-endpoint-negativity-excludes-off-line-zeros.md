# L-93886 — Eventual prime-endpoint negativity excludes every off-line zero

Claim ID: `L-93886`  
Status: **PROPOSED COMPLETE ONE-WAY MELLIN–LANDAU THEOREM**  
Depends on: elementary prime-zeta Möbius inversion; Landau's theorem  
RH status: **conclusion of this claim**

## 1. Mellin transform

For

\[
A(X)=\sum_{p\le X}(\log p)r_X(p),
\]

put

\[
\widehat A(z)=\int_1^\infty A(X)X^{-z-1}\,dX.
\]

The integral converges initially for `Re z>1/2`. Put `s=z+1/2`.

For

\[
P_1(s)=\sum_p\frac{\log p}{p^s}
\]

and the exact adjacent kernel symbol `D`, direct termwise integration gives

\[
\boxed{
\widehat A(z)
=
\frac1{z^2}
\left[
\frac{D(s-1)}s-P_1(s)
\right].
}
\tag{L-93886.1}
\]

## 2. Prime-zeta inversion

For `Re s>1`,

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{m\ge1}P_1(ms).
\]

Möbius inversion gives

\[
\boxed{
P_1(s)
=
\sum_{m\ge1}\mu(m)
\left(-\frac{\zeta'}{\zeta}\right)(ms).
}
\tag{L-93886.2}
\]

This continues `P_1` meromorphically.

## 3. Pole created by an off-line zero

Let `rho` be a zero of multiplicity `m_rho` with `Re rho>1/2`. At

\[
z_\rho=\rho-\frac12
\]

only the `m=1` term in (L-93886.2) has a singularity at `s=rho`.
The adjacent-kernel term is analytic there. Therefore

\[
\boxed{
\operatorname*{Res}_{z=z_\rho}\widehat A(z)
=
\frac{m_\rho}{(\rho-1/2)^2}\ne0.
}
\tag{L-93886.3}
\]

The pole cannot be cancelled by a scaled zero.

## 4. No positive real singularity

For real `s>1/2`, `zeta(s)` has no zeros:

- `zeta(s)>0` for `s>1`;
- `zeta(s)<0` for `0<s<1`, from the alternating eta representation.

All `m>=2` terms in (L-93886.2) are regular for `s>1/2`. At `s=1`, the pole of
`P_1(s)` cancels exactly with the pole in `D(s-1)/s`; the Laurent principal
parts agree by the adjacent-kernel identity.

Consequently the right side of (L-93886.1) is analytic at every positive real
`z`.

## 5. Landau argument

Assume `A(X)<0` for all `X>=X_0`. Put

\[
f(t)=-A(e^t).
\]

Then `f(t)>=0` eventually and has finite exponential order. Its Laplace
transform is `-\widehat A(z)`.

Landau's theorem says that if the real abscissa of convergence `sigma_c` is
finite, then `z=sigma_c` is a singularity. Since the meromorphic continuation
has no positive real singularity, `sigma_c<=0`.

Hence the Laplace integral itself converges absolutely and defines a
holomorphic function throughout `Re z>0`. By identity continuation it equals
the right side of (L-93886.1) there.

An off-line zero with `Re rho>1/2` would create the genuine pole (L-93886.3) in
that half-plane, a contradiction.

Therefore

\[
\zeta(s)\ne0\qquad(\Re s>1/2).
\]

The functional equation reflects zeros about `Re s=1/2`, so every nontrivial
zero lies on the critical line:

\[
\boxed{\mathrm{RH}.}
\tag{L-93886.4}
\]

## 6. Scope

Only the implication

\[
A(X)<0\text{ eventually}\Longrightarrow\mathrm{RH}
\]

is used. No contour shift under RH and no converse estimate is imported.
