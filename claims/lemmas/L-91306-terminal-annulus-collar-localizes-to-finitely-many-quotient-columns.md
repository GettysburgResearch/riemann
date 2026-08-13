# L-91306 — The terminal quantization disturbance localizes to finitely many quotient columns

Claim ID: `L-91306`  
Status: **PROVED ASYMPTOTIC LOCALIZATION THEOREM; FINITE COLLAR CERTIFICATE OPEN**  
Created: 2026-08-12  
Depends on: `L-91110`, `L-91111`, `L-91303`  
RH status: **unproved**

## 1. Setting

Let the continuum endpoint density be

\[
 \lambda_X(s)=L(X/s)
\]

on the factor-54 outer window, truncated smoothly or cellwise to

\[
 K+2\le s\le X-1,
 \qquad K=c_0X+O(1).
\]

Let `C_X(m)` be the positive martingale-quantization collar of `L-91111`.
Its exact formula is a sum of two half-cell integrals involving the endpoint
state

\[
 r_T
 =\frac{2((T-1)^{-1/2}-T^{-1/2})}
        {\log(T/(T-1))}
\]

and the split point `s_T=r_T^-2`.

The terminal detail annulus is

\[
 \frac X4<q<X.
\]

There `4q>X`, so the radix-four detail equals the ordinary carry response:

\[
 \mathcal D_4v_q(C_X)=v_q(C_X).
\tag{L-91306.1}
\]

## 2. Uniform scaled collar profile away from reciprocal knots

Fix a compact interval

\[
 J\Subset(c_0,1)
\]

which avoids the finitely many reciprocal knots `1,1/2,1/3,1/4` relevant to
the terminal annulus.  Standard expansion of the weighted means gives,
uniformly for `T/X in J`,

\[
 r_T
 =T^{-1/2}+\frac14T^{-3/2}+O(T^{-5/2}),
\tag{L-91306.2}
\]

\[
 s_T
 =T-\frac12-\frac7{48T}+O(T^{-2}).
\tag{L-91306.3}
\]

Substitution in the exact formula of `L-91111`, followed by rescaling each
half-cell by its unit local coordinate, yields a piecewise `C^1` function
`c(theta)` such that

\[
 \boxed{
 C_X(m)
 =X^{-3/2}c(m/X)+O(X^{-5/2})
 }
\tag{L-91306.4}
\]

uniformly whenever `m/X in J`.  The function `c` depends only on the finite
cell formula for `L(1/theta)` and the universal endpoint-state asymptotics.

The same statement holds separately on every closed subcell of
`[1/4,1]` cut at the reciprocal knots.

## 3. Carry cancellation away from activation columns

For `X/4<q<X`, at most three multiples of `q` occur below `X-1`.  On a
subcell where the active number of multiples is fixed and every `kq/X` stays a
positive distance from a reciprocal knot, (L-91306.4) gives

\[
 C_X(kq)-C_X(kq+1)=O(X^{-5/2}).
\]

Therefore

\[
 \boxed{
 v_q(C_X)=O(X^{-5/2})
 }
\tag{L-91306.5}

uniformly away from finitely many activation columns.

On the same compact subcell the terminal target has the form

\[
 \Omega_X(q)=X^{-1/2}\omega(q/X),
\]

where `omega` is continuous and strictly positive.  Hence

\[
 \boxed{
 \frac{|v_q(C_X)|}{\Omega_X(q)}=O(X^{-2}).
 }
\tag{L-91306.6}

Thus the terminal annulus is not a macroscopic safety-factor problem.  Every
nonlocal column has two extra powers of reserve.

## 4. The top endpoint constant

The only place where the target itself vanishes at terminal scale is `q/X ->1`.
For `m=X-1`, only the upper half of the last endpoint cell contributes to the
exact collar formula.  Equations (L-91306.2)--(L-91306.3) give

\[
 \sqrt{X-1}\,[1-r_X\sqrt{X-1}]
 =\frac1{4\sqrt X}+O(X^{-3/2}).
\tag{L-91306.7}

On that half-cell the martingale weight converges to the linear hat

\[
 u\longmapsto\frac12-u,
 \qquad0\le u\le\frac12,
\]

whose integral is `1/8`.  Since `L(1)=1` and `a(s)=2/s`,

\[
 \boxed{
 C_X(X-1)
 =\frac1{16}X^{-3/2}+O(X^{-5/2}).
 }
\tag{L-91306.8}

Meanwhile

\[
 \Omega_X(X-1)
 =(X-1)^{-1/2}\log\frac X{X-1}
 =X^{-3/2}+O(X^{-5/2}).
\tag{L-91306.9}

Consequently

\[
 \boxed{
 \frac{C_X(X-1)}{\Omega_X(X-1)}
 \longrightarrow\frac1{16}.
 }
\tag{L-91306.10}

The last-column disturbance is therefore strictly subcapacity.  It is not an
asymptotic obstruction.

## 5. Finite quotient-collar localization

The active-multiple count changes only near

\[
 q=\frac Xj,
 \qquad j=1,2,3,4.
\]

The endpoint density itself changes cell formula only when one of the finitely
many arguments `kq/X` crosses a reciprocal knot.  In the terminal annulus these
are the same finite quotient locations.

For every fixed collar width `C`, all columns outside

\[
 \boxed{
 \bigcup_{j=1}^4
 \left\{q:\left|q-\frac Xj\right|\le C\right\}
 }
\tag{L-91306.11}

obey (L-91306.6), after increasing `C` once to include the support endpoint.
Inside (L-91306.11) there are only `O(C)` columns, independently of `X`, and
all collar entries are `O(X^-3/2)`.

Thus the terminal annulus reduces to a bounded-dimensional local capacity
problem repeated at four quotient interfaces.

## 6. Score scale of a local repair

The endpoint entropy increment near endpoint `T asymp X` is `O(X^-1/2)`.
Every correction in (L-91306.11) has bounded endpoint width and bounded
intensity after normalization by its local target.  Therefore any fixed
nonnegative collar repair has score charge

\[
 \boxed{O(X^{-1/2})=O(1).}
\tag{L-91306.12}

In particular, a directed finite certificate for the four local quotient
collars is compatible with the bounded-debt hypothesis H3 of `T-91101`.

## 7. Consequence for the reset programme

Combining `L-91303` and the present theorem gives:

```text
bulk finite-transfer error          relative O(X^-1);
quantization collar away from knots relative O(X^-2);
top endpoint ratio                  -> 1/16;
all terminal anomalies              four bounded-width quotient collars;
score of a finite local repair       O(1) per generation.
```

The remaining theorem is therefore a finite directed capacity certificate for
four quotient interfaces, coupled to the 33-state parity shadow and the
three-integer divisor stencil of `L-91105`.

## 8. Proof boundary

```text
endpoint-state asymptotics                     EXACT
piecewise scaled collar profile                 EXACT ASYMPTOTIC
terminal carry cancellation away from knots     EXACT ASYMPTOTIC
top endpoint ratio 1/16                         EXACT ASYMPTOTIC
localization to four quotient collars           EXACT
bounded score scale of local repair             EXACT ORDER BOUND
nonnegative divisor-faithful collar certificate OPEN
coefficient-one reset                           OPEN
Riemann Hypothesis                              UNPROVED
```
