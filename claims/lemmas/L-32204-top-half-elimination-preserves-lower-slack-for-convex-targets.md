# L-32204 — Top-half elimination preserves lower slack for convex targets

Claim ID: `L-32204`  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-09  
Dependencies: `L-32201`; exact carry matrix `L-23801`  
Scope: exact finite carry algebra; no RH conclusion

## 1. Statement

Fix an endpoint `T>=4` and put

\[
N=\lfloor T/2\rfloor.
\]

Let `h(2),...,h(T)` satisfy

\[
h(T)=0,
\qquad
\Delta_m:=h(m)-h(m+1)\ge0,
\qquad
\Delta_m\ge\Delta_{m+1}.
\tag{L-32204.1}
\]

Thus `h` is nonnegative, decreasing and discretely convex.

Use the unique top-half coefficients `c(n)`, `N<n<=T`, solving

\[
h(q)=\sum_{n=q}^{T}c(n)\beta_{nq}
\qquad(N<q\le T).
\tag{L-32204.2}
\]

By `L-32201`, all these coefficients are nonnegative. Define the unused lower target

\[
r(q)=h(q)-\sum_{n=N+1}^{T}c(n)\beta_{nq},
\qquad2\le q\le N.
\tag{L-32204.3}
\]

Then

\[
\boxed{r(q)\ge0\qquad(2\le q\le N).}
\tag{L-32204.4}
\]

Consequently the exact top-half inverse is a genuine nonnegative carry packing: it saturates every column above `T/2` and never overfills a lower column.

## 2. Step decomposition

For `m<T` let

\[
e_m(q)=\mathbf 1_{q\le m}.
\]

Equation (L-32204.1) gives the positive decomposition

\[
 h=\sum_{m=2}^{T-1}\Delta_m e_m.
\tag{L-32204.5}
\]

If `m<=N`, `e_m` has no top-half coordinate and is untouched by (L-32204.2).
It remains to understand one step with `N<m<T`.

For such an `m`, direct substitution in the top-half inversion of `L-32201` gives

\[
 c_n^{(m)}=
 \begin{cases}
 \dfrac{2m}{n(n-1)},&N<n<m,\\[2mm]
 1+\dfrac{2}{m-1}=\dfrac{m+1}{m-1},&n=m,\\[2mm]
 0,&n>m.
 \end{cases}
\tag{L-32204.6}
\]

All entries are positive.

## 3. Exact lower load of one top step

Put

\[
 A_x(q)=\sum_{j=0}^{x}\left\lfloor\frac jq\right\rfloor.
\tag{L-32204.7}
\]

The floor-sum form of the carry matrix gives the exact telescoping identity

\[
\boxed{
\frac{\beta_{nq}}{n(n-1)}
=
\frac{A_n(q)}{n(n+1)}
-
\frac{A_{n-1}(q)}{(n-1)n}.}
\tag{L-32204.8}
\]

Combining (L-32204.6), (L-32204.8), and

\[
\beta_{mq}=\left\lfloor\frac mq\right\rfloor
-\frac{2A_m(q)}{m+1},
\]

the top-half realization of `e_m` has lower-column load

\[
\boxed{
L_m(q)=\left\lfloor\frac mq\right\rfloor
-\frac{2mA_N(q)}{N(N+1)}.}
\tag{L-32204.9}
\]

Hence its lower residual is

\[
\boxed{
k_m(q)=1-L_m(q)
=1-\left\lfloor\frac mq\right\rfloor
+\frac{2mA_N(q)}{N(N+1)}.}
\tag{L-32204.10}
\]

Individual `k_m(q)` need not be nonnegative. The useful invariant is its cumulative sum in the step endpoint.

## 4. Floor-prefix positivity

For

\[
N<M\le2N
\]

define

\[
K_{N,q}(M)=\sum_{m=N+1}^{M}k_m(q).
\]

Then

\[
\boxed{
K_{N,q}(M)
=M-N-A_M(q)
+\frac{M(M+1)}{N(N+1)}A_N(q)\ge0.}
\tag{L-32204.11}
\]

### Proof of the inequality

Write

\[
N=aq+r,
\qquad
M=(a+b)q+s,
\qquad0\le r,s<q.
\]

The exact floor sum is

\[
A_N(q)=\frac{qa(a-1)}2+a(r+1)
\tag{L-32204.12}
\]

and analogously for `A_M`.

After multiplication by `2N(N+1)`, the numerator of (L-32204.11) is a quadratic polynomial in `b` whose `b^2` coefficient is

\[
-q\,[a q(q-1)+r(r+1)]\le0.
\tag{L-32204.13}
\]

Thus, for fixed `a,q,r,s`, its minimum on the allowed integer interval for `b` occurs at one of the two endpoints.

The endpoint conditions coming from `0<M-N<=N` are exactly

```text
lower endpoint:
  b=0  if s>r;
  b=1  if s<=r;

upper endpoint:
  b=a-1 if s>2r;
  b=a   if 2r-q < s <=2r;
  b=a+1 if s<=2r-q.
```

Each endpoint is reduced to a polynomial with nonnegative integer coefficients by the following nonnegative substitutions:

```text
A: b=0,   s>r:
   a=A+1, s=r+1+u, q=r+u+2+w.

B: b=1,   s<=r:
   a=A+1, r=s+v,   q=s+v+1+w.

C: b=a-1, s>2r:
   a=A+2, b=A+1,
   s=2r+1+u, q=2r+u+2+w.
   (The exceptional a=1 endpoint is case A.)

D: b=a,   2r-q<s<=2r:
   use u=2r-s and q=u+1+w;
   split w<=u and w>=u and translate the remaining bounded residue
   coordinate to its corresponding endpoint.  In both subcases the numerator
   is a polynomial with nonnegative integer coefficients.

E: b=a+1, s<=2r-q:
   write r=q-1-v, s=q-2-2v-u, then q=u+2v+2+w;
   the resulting numerator has nonnegative integer coefficients.
```

No inequality involving a floor remains after these substitutions.  The exact symbolic coefficient check is included in `X-32202-floor-prefix`; it constructs (L-32204.12)--(L-32204.13) from integer polynomial arithmetic and verifies every endpoint certificate coefficientwise.  This is an all-parameter algebraic certificate, not an enumeration over bounded `N`.

For illustration, case A factors as

\[
2N(N+1)K=(u+1)P_A(A,r,u,w)
\]

with `P_A` having forty nonnegative integer monomials.  Case B has fifty nonnegative monomials.  The remaining endpoint certificates are checked in the same exact coefficient ring.

This proves (L-32204.11).

## 5. Abel recombination of the convex step weights

For fixed `q<=N`, equations (L-32204.5) and (L-32204.10) give

\[
r(q)=\sum_{m=q}^{N}\Delta_m
     +\sum_{m=N+1}^{T-1}\Delta_m k_m(q).
\tag{L-32204.14}
\]

Since `T-1<=2N`, all prefix sums in the second term are nonnegative by (L-32204.11). Finite summation by parts gives

\[
\begin{aligned}
\sum_{m=N+1}^{T-1}\Delta_m k_m(q)
={}&\Delta_{T-1}K_{N,q}(T-1)\\
&+\sum_{M=N+1}^{T-2}
  (\Delta_M-\Delta_{M+1})K_{N,q}(M)
\ge0.
\end{aligned}
\tag{L-32204.15}
\]

The first term in (L-32204.14) is also nonnegative. Therefore `r(q)>=0`, proving (L-32204.4).

## 6. Critical hinge consequence

For

\[
h_T(q)=q^{-1/2}-T^{-1/2},
\]

one has

\[
\Delta_m=m^{-1/2}-(m+1)^{-1/2}>0
\]

and these differences decrease with `m` because `x^{-1/2}` is convex. Hence `L-32204` applies exactly.

The critical hinge can therefore be saturated positively on its whole top half while leaving a nonnegative residual supported at the strict half scale.

## 7. Proof boundary

Closed here:

1. exact top-step inverse;
2. exact lower-column load of every top step;
3. all-parameter floor-prefix positivity;
4. positive Abel recombination for every decreasing discretely convex target;
5. nonnegative strict-half-scale residual for every critical square-root hinge.

Not proved here:

1. that the exported residual remains in a cone allowing indefinite repetition;
2. full Critical Hinge Saturation;
3. RH.
