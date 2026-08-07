# R-20805 — Carry saturation is not formal positivity

Refutation ID: `R-20805`  
Title: The positive carry ledger does not make its triangular inverse positive; the inverse contains a Möbius and reciprocal-zeta channel  
Status: `PROPOSED — EXACT FINITE ADJOINT FACTORIZATION AND MELLIN SCOPE CORRECTION`  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: `L-20815`; `L-20816`  
Scope: prevent the open carry-saturation hinge from being silently promoted

## 1. The tempting but invalid inference

The matrix

\[
 B_{q,n}=\beta_{nq},
 \qquad2\le q\le n\le X,
 \tag{R-20805.1}
\]

is upper triangular and entrywise nonnegative, with positive diagonal. This does
**not** imply that the solution of

\[
 B^Tc=w_X
 \tag{R-20805.2}
\]

is nonnegative. Inverses of positive triangular matrices generally have mixed
signs.

Therefore the numerical observation

\[
 c_X(n)\ge0
\]

must be proved for the particular weight `w_X`; it is not a consequence of
`beta_(nq)>=0`.

## 2. Exact adjoint factorization

Let

\[
 w_q=w_X(q).
\]

Define the finite multiples-Möbius transform

\[
 \boxed{
 u_m=\sum_{k\le X/m}\mu(k)w_{mk}.}
 \tag{R-20805.3}
\]

It is characterized by

\[
 w_q=\sum_{k\le X/q}u_{kq}.
 \tag{R-20805.4}
\]

Put

\[
 z_m=u_m-u_{m+1},
 \qquad u_{X+1}=0,
 \tag{R-20805.5}
\]

and

\[
 \boxed{
 C_j={j u_j+\sum_{m=j+1}^Xu_m\over j(j-1)}.}
 \tag{R-20805.6}
\]

Then the unique triangular solution is

\[
 \boxed{
 c_X(j)=(j+1)(C_j-C_{j+1}).}
 \tag{R-20805.7}
\]

### Derivation

For a vector `y_q`, define

\[
 a_m=\sum_{q\mid m}y_q,
 \qquad
 Y_n=\sum_{m\le n}a_m.
 \tag{R-20805.8}
\]

The carry operator factors as

\[
 (By)_n
 =Y_n-{2\over n+1}\sum_{j=0}^nY_j.
 \tag{R-20805.9}
\]

Taking finite adjoints gives, successively:

1. multiples Möbius inversion, producing `u`;
2. a backward difference, producing `z`;
3. inversion of the averaging adjoint, producing (R-20805.6)--(R-20805.7).

Every identity is finite. The first stage already contains the Möbius function,
so coefficient positivity is a genuine arithmetic statement.

For the target weight,

\[
 \boxed{
 u_m={1\over\sqrt m}
 \sum_{k\le X/m}{\mu(k)\over\sqrt k}
 \log{X/m\over k}.}
 \tag{R-20805.10}
\]

The `u_m` and their first differences have both signs in actual computations;
positivity appears only after the final nonlocal averaging inversion.

## 3. Exact signed dual sequence

There is one signed sequence `y_q` satisfying

\[
 \sum_{q=2}^n\beta_{nq}y_q={n\over2}
 \qquad(n\ge2).
 \tag{R-20805.11}
\]

Let

\[
 Y(n)=\sum_{q=2}^ny_q\left\lfloor{n\over q}\right\rfloor.
 \tag{R-20805.12}
\]

Solving the averaging recurrence gives

\[
 \boxed{
 Y(n)=nH_{n-1}+{n\over2}
 \qquad(n\ge2).}
 \tag{R-20805.13}
\]

With `Y(1)=0`, define `a_n=Y(n)-Y(n-1)`. Then

\[
 a_2=3,
 \qquad
 a_n=H_{n-1}+{3\over2}\quad(n\ge3),
 \tag{R-20805.14}
\]

and Möbius inversion yields

\[
 \boxed{
 y_n=\sum_{d\mid n}\mu(n/d)a_d.}
 \tag{R-20805.15}
\]

The sequence is signed; for example

\[
 y_2=3,
 \quad y_3=3,
 \quad y_4={1\over3},
 \quad y_6=-{133\over60}.
 \tag{R-20805.16}
\]

Whenever (L-20816.3) is saturated,

\[
 \boxed{
 {1\over2}\sum_{n=2}^Xn c_X(n)
 =\sum_{q=2}^Xy_qw_X(q).}
 \tag{R-20805.17}
\]

Thus the exact leading carry mass also has a signed reciprocal-zeta coordinate.
The elementary dual minorant in `L-20816` avoids estimating this signed sequence
directly, but only after `c_X>=0` is known.

## 4. Dirichlet-series audit

Let

\[
 \mathcal A(s)
 =3\,2^{-s}
 +\sum_{n\ge3}
 \left(H_{n-1}+{3\over2}\right)n^{-s}.
 \tag{R-20805.18}
\]

For `Re(s)>1`, (R-20805.15) gives

\[
 \boxed{
 \sum_{n\ge2}{y_n\over n^s}
 ={\mathcal A(s)\over\zeta(s)}.}
 \tag{R-20805.19}
\]

The numerator has the double-pole growth expected from `H_n`, while division by
`zeta` leaves the main simple pole at `s=1` and introduces the nontrivial-zero
channel. A sharp direct estimate of the signed dual Riesz sum is therefore not a
free consequence of Stirling's formula.

## 5. Continuum critical profile

The continuum carry kernel has Mellin transform

\[
 \widehat K(s)={s-1\over s(s+1)}\zeta(s).
 \tag{R-20805.20}
\]

After the critical scaling `q=Xe^{-t}`, the formal limiting inverse profile has
Laplace transform

\[
 \boxed{
 \Phi(z)
 ={(z+1/2)(z+3/2)
  \over z^2(z-1/2)\zeta(z+1/2)}.}
 \tag{R-20805.21}
\]

The normalization at `z=1/2` gives

\[
 \Phi(1/2)=8,
 \tag{R-20805.22}
\]

which is exactly the coefficient `4 sqrt(X)` after the factor `1/2` in the
carry objective. But (R-20805.21) also makes clear that global positivity or
variation diminution of the inverse profile interacts with the nontrivial
zeros of zeta.

## 6. Scope correction

The following inference is rejected:

```text
positive carry entries
+ positive target weights
=> positive saturation coefficients
=> RH.
```

Only the first two premises are automatic. The coefficient positivity theorem
is the load-bearing new assertion.

This does not refute the carry route. It makes it unusually sharp: one finite,
explicit, independently checkable triangular positivity theorem is now the
entire arithmetic frontier.

## 7. Proof boundary

- The finite adjoint factorization, signed dual, and Dirichlet/Mellin formulas
  are exact.
- They explain why finite positivity through a large cutoff is evidence, not a
  proof.
- They do not prove that a negative coefficient eventually occurs.
- They do not disprove the carry-saturation conjecture.
- `T-20805` is valid only after this exact positivity hinge is independently
  proved.