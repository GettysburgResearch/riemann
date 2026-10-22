# L-26201 — Exact dyadic opposite-parity contraction of the carry kernel

Claim ID: `L-26201`  
Title: One source-specific dyadic Euler factor turns the Möbius-adjoint carry row into a compact positive/negative dipole  
Status: **PROPOSED EXACT FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: PR #244 `L-23704`; PR #236 fixed-ratio shell transfer; elementary Dirichlet convolution  
Scope: exact source recombination; no reflected reserve or RH conclusion

## 1. Carry kernel and its Möbius adjoint

For integers `2<=q<=n`, put

\[
 \beta_{nq}
 =
 \frac{\lfloor n/q\rfloor\,
       (q-1-(n\bmod q))}
      {n+1}.
\tag{L-26201.1}
\]

For `2<=m<=n`, the exact Möbius contraction is

\[
 \boxed{
 \sum_{k\le n/m}\mu(k)\beta_{n,mk}
 =
 \frac{2m-n-1}{n+1}.}
\tag{L-26201.2}
\]

This is the affine row collapse proved independently in PR #244.  It follows
directly from the floor form of `beta` and

\[
 \sum_{k\le y}\mu(k)\lfloor y/k\rfloor=1.
\]

The generic Brion and bounded-rank proposals attempted to find cancellation
after expanding many Möbius variables.  Here the cancellation is inserted at
the arithmetic-source level before any geometry is introduced.

## 2. The minimal dyadic opposite-parity source

Define

\[
 \boxed{
 \omega_2(n)
 =
 \mu(n)
 -\frac32\,{\bf1}_{2\mid n}\mu(n/2)
 +\frac12\,{\bf1}_{4\mid n}\mu(n/4).}
\tag{L-26201.3}
\]

Its Dirichlet series is

\[
 \boxed{
 \Omega_2(s)
 =
 \sum_{n\ge1}\frac{\omega_2(n)}{n^s}
 =
 \frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.}
\tag{L-26201.4}
\]

The additional factor `1-2^(-s-1)` has zeros only on `Re(s)=-1`; it cannot
cancel a zeta zero in `Re(s)>1/2`.  Thus this finite Euler modification retains
the same rightmost-zero obstruction as the dyadic Mertens shell.

Writing `n=2^nu m` with `m` odd,

\[
 \boxed{
 \omega_2(2^\nu m)
 =
 \mu(m)
 \begin{cases}
  1,&\nu=0,\\
  -5/2,&\nu=1,\\
  2,&\nu=2,\\
  -1/2,&\nu=3,\\
  0,&\nu\ge4.
 \end{cases}}
\tag{L-26201.5}
\]

The four layers are an exact opposite-parity family.  In particular, the
same-sign odd Möbius cube is never declared to vanish by a generic line cone:
it is paired with three actual `2`-adic siblings carrying the displayed signs.

## 3. Exact compact carry dipole

Contract the carry row against the complete source (L-26201.3):

\[
 \Gamma_2(n,m)
 =
 \sum_{k\le n/m}\omega_2(k)\beta_{n,mk}.
\tag{L-26201.6}
\]

Using (L-26201.2) at `m`, `2m`, and `4m` gives

\[
 \Gamma_2(n,m)
 =
 K(n,m)-\frac32K(n,2m)+\frac12K(n,4m),
\tag{L-26201.7}
\]

where `K(n,a)=0` for `a>n`.  Therefore

\[
 \boxed{
 \Gamma_2(n,m)=
 \begin{cases}
  0,&n<m,\\[1mm]
  \dfrac{2m-n-1}{n+1},
     &m\le n<2m,\\[3mm]
  \dfrac{n+1-8m}{2(n+1)},
     &2m\le n<4m,\\[3mm]
  0,&n\ge4m.
 \end{cases}}
\tag{L-26201.8}
\]

The first active band is nonnegative and the second is strictly negative:

\[
 \Gamma_2(n,m)\ge0
 \quad(m\le n<2m),
\tag{L-26201.9}
\]

\[
 \Gamma_2(n,m)<0
 \quad(2m\le n<4m).
\tag{L-26201.10}
\]

The entire affine tail beyond `4m` cancels exactly.  This is not a rank
assertion and it is not automatic polyhedral line cancellation.  It is an
explicit source identity between opposite-parity Möbius families.

The polynomial behind the cancellation is

\[
 (1-X)(1-X/2)=1-\frac32X+\frac12X^2.
\tag{L-26201.11}
\]

Its roots `1` and `2` annihilate the two affine modes in (L-26201.2).  The
coefficient signs in (L-26201.3) are forced by this two-moment requirement.

## 4. Stable transfer from the dyadic Mertens shell

Let

\[
 b_2(n)=\mu(n)-{\bf1}_{2\mid n}\mu(n/2)
\tag{L-26201.12}
\]

be the dyadic shell coefficient, and write

\[
 B_2(x)=\sum_{n\le x}b_2(n),
 \qquad
 W_2(x)=\sum_{n\le x}\omega_2(n).
\]

Then

\[
 \boxed{
 W_2(x)=B_2(x)-\frac12 B_2(x/2),}
\tag{L-26201.13}
\]

with the floor convention in every summatory function.  Pointwise finite
geometric inversion gives

\[
 \boxed{
 B_2(x)
 =
 \sum_{j\ge0}2^{-j}W_2(x/2^j).}
\tag{L-26201.14}
\]

Thus the two shell functions have the same polynomial growth exponent.  In
logarithmic normalized coordinates,

\[
 Q_B(t)=e^{-t/2}B_2(e^t),
 \qquad
 Q_W(t)=e^{-t/2}W_2(e^t),
\]

one has

\[
 \boxed{
 Q_W
 =
 \left(I-2^{-3/2}\tau_{\log2}\right)Q_B,}
\tag{L-26201.15}
\]

and the inverse filter has absolutely summable positive coefficients.  Hence
the unit-block energy of `Q_W` is subexponential if and only if the unit-block
energy of `Q_B` is subexponential.  By the fixed-ratio shell criterion of
PRs #234/#236, either condition implies RH.

The gain is structural rather than logical: `omega_2` is an RH-equivalent
source whose carry image is the compact dipole (L-26201.8).

## 5. Exact packet interface

If `c(n)` is any finite carry coefficient vector and

\[
 u_m=\sum_{n=m}^X c(n)\frac{2m-n-1}{n+1},
\tag{L-26201.16}
\]

then the opposite-parity transform obeys

\[
 \boxed{
 u_m-\frac32u_{2m}+\frac12u_{4m}
 =
 \sum_{m\le n<4m}c(n)\Gamma_2(n,m),}
\tag{L-26201.17}
\]

where terms with index above `X` are zero.  Every transformed row is therefore
a coupled inner/outer dyadic band, not an unbounded-rank tuple face.

A proof may still fail because the positive and negative bands need a
source-specific reserve.  Equation (L-26201.17) only supplies the exact place
where that reserve must act.

## 6. Proof boundary

Closed exactly:

- the four `2`-adic source layers;
- the safe Euler-factor identity;
- the compact positive/negative carry dipole;
- the stable transfer to the dyadic Mertens shell;
- the factor-four local packet equation.

Open:

- a positivity-preserving defect-to-slack recombination of the two dipole bands;
- a coupled reflected normal-Gram estimate for this exact source;
- the dyadic shell energy bound;
- RH.
