# L-105220 — A positive three-height Poisson localizer with value-only boundary formulas

Claim ID: `L-105220`  
Status: **PROPOSED EXACT FINITE-POLYNOMIAL THEOREM; independent review pending**  
Created: 2026-08-23  
Depends on: `L-105200`; PR #723 `L-105101--L-105102` for comparison  
RH status: **not assumed**

## 1. Positive multipole localizer

Fix a real centre `a` and define

\[
\boxed{
\Omega_a(z)=
\frac{36}{
\bigl((z-a)^2+1\bigr)
\bigl((z-a)^2+4\bigr)
\bigl((z-a)^2+9\bigr)
}.
}
\tag{L-105220.1}
\]

For real `x`,

\[
\Omega_a(x)>0,
\qquad
\Omega_a(x)\ll (1+|x-a|)^{-6}.
\]

The exact partial-fraction decomposition is

\[
\boxed{
\Omega_a(z)
=
\frac{3/2}{(z-a)^2+1}
-\frac{12/5}{(z-a)^2+4}
+\frac{9/10}{(z-a)^2+9}.
}
\tag{L-105220.2}
\]

Thus the only poles of the localizer are the six simple safe points

\[
a\pm i,\qquad a\pm2i,\qquad a\pm3i.
\]

Its real-axis mass is

\[
\boxed{
\int_{\mathbb R}\Omega_a(x)\,dx
=
\pi\left(\frac32-\frac65+\frac3{10}\right)
=
\frac{3\pi}{5}.
}
\tag{L-105220.3}
\]

## 2. Value-only boundary functional

For a rational function `R` with real coefficients and growth
`R(z)=O(z^4)` at infinity, define

\[
\boxed{
\mathfrak P_a[R]
=
-\frac32\Im R(a+i)
+\frac65\Im R(a+2i)
-\frac3{10}\Im R(a+3i).
}
\tag{L-105220.4}
\]

Suppose `R` is holomorphic at `a+/-i`, `a+/-2i`, and `a+/-3i`; suppose its
finite poles `w` are simple or conjugate paired, and write
`r_w=Res_(z=w)R(z)`. Since `Omega_a R=O(z^-2)` or better, the residue at
infinity vanishes. The residue of the `h`th partial-fraction term at `a+ih`
is `c_h/(2ih)`, with

\[
(c_1,c_2,c_3)=\left(\frac32,-\frac{12}{5},\frac9{10}\right).
\]

Schwarz pairing at `a-ih` and the residue theorem give

\[
\boxed{
\sum_w\Omega_a(w)r_w
=
\mathfrak P_a[R].
}
\tag{L-105220.5}
\]

Unlike `L-105200`, this boundary functional uses no derivatives of `R` at the
safe points.

## 3. Critical count and residue moments

Let `p` be a real polynomial. Assume every zero `c` of `p'` is simple and
`p(c)!=0`, every zero `d` of `p''` is simple, and none of the six safe points
is a zero of `p'p''`. Put

\[
\rho_c=\frac{p(c)}{p''(c)},
\qquad
\tau_d=\frac{p(d)^2}{p'(d)p'''(d)}.
\]

Apply (L-105220.5) successively to

\[
R_0=\frac{p''}{p'},
\qquad
R_1=\frac p{p'},
\qquad
R_2=\frac{p^2}{p'p''}.
\]

One obtains the exact common-weight identities

\[
\boxed{
\sum_{p'(c)=0}\Omega_a(c)
=
\mathfrak P_a\!\left[\frac{p''}{p'}\right],
}
\tag{L-105220.6}
\]

\[
\boxed{
\sum_{p'(c)=0}\Omega_a(c)\rho_c
=
\mathfrak P_a\!\left[\frac p{p'}\right],
}
\tag{L-105220.7}
\]

and

\[
\boxed{
\sum_{p'(c)=0}\Omega_a(c)\rho_c^2
+
\sum_{p''(d)=0}\Omega_a(d)\tau_d
=
\mathfrak P_a\!\left[\frac{p^2}{p'p''}\right].
}
\tag{L-105220.8}
\]

All sums are algebraic. Nonreal events are included with their conjugates.

## 4. Exact finite Bézout removal

Under the hypotheses of `L-105201`, let `A_p` be the canonical polynomial
satisfying

\[
A_pp'\equiv p^2\pmod{p''},
\]

and put

\[
\widetilde Q_p
=
\frac{p^2-A_pp'}{p'p''}.
\]

Its only finite poles are the zeros of `p'`, with residue `rho_c^2`.
Consequently

\[
\boxed{
\sum_{p'(c)=0}\Omega_a(c)\rho_c^2
=
\mathfrak P_a[\widetilde Q_p].
}
\tag{L-105220.9}
\]

Thus the finite Bézout correction and the positive localizer commute exactly.

## 5. Scope

The theorem is finite and exact. It does not construct the entire-Xi Bézout
interpolant, justify a cofinal canonical-product passage, or remove the
nonreal-critical correction. Its advance is geometric: the three moments are
measured by one positive weight using only six **values** of the relevant
ratios, rather than second derivatives of those ratios at two boundary points.
