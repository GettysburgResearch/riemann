# D-23801 — Carry packing and Möbius-curvature coordinates

Definition ID: `D-23801`  
Title: The prime ramp has an exact finite carry-packing LP whose inverse is a discrete Möbius curvature  
Status: **PROPOSED EXACT FINITE FORMULATION**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238  
Scope: finite algebra only; no RH conclusion

## 1. Carry matrix

Fix an integer `X>=2`. For `2<=q<=n<=X`, put

\[
 a_{nq}=\left\lfloor\frac nq\right\rfloor,
 \qquad
 r_{nq}=n-q a_{nq},
\]

and define

\[
 \boxed{
 \beta_{nq}
 =\frac{a_{nq}(q-1-r_{nq})}{n+1}.}
 \tag{D-23801.1}
\]

Let `B_X` be the lower-triangular matrix with rows indexed by `n` and columns
indexed by `q`:

\[
 (B_X)_{nq}=\beta_{nq}\mathbf1_{q\le n}.
 \tag{D-23801.2}
\]

Its diagonal is

\[
 \beta_{nn}=\frac{n-1}{n+1}>0,
 \tag{D-23801.3}
\]

so `B_X` is invertible over the real numbers.

For `2<=q<=X`, define the prime-ramp column

\[
 \boxed{
 w_X(q)=\frac1{\sqrt q}\log\frac Xq.}
 \tag{D-23801.4}
\]

The exact Carry Saturation coefficients are the unique vector `c_X` satisfying

\[
 B_X^T c_X=w_X.
 \tag{D-23801.5}
\]

The present route does not assume `c_X>=0`.

## 2. Positive carry packings

A **carry packing** is a vector

\[
 d=(d(2),\ldots,d(X))
 \tag{D-23801.6}
\]

such that

\[
 \boxed{
 d(n)\ge0,
 \qquad
 B_X^Td\le w_X
 }
 \tag{D-23801.7}
\]

coordinatewise. Its unused ramp is

\[
 \rho_d(q)=w_X(q)-(B_X^Td)(q)\ge0.
 \tag{D-23801.8}
\]

Thus a packing is a finite nonnegative sub-saturation of the exact triangular
inverse. The zero vector is always feasible.

## 3. Möbius transform of an arbitrary ramp

For any real column `w=(w(2),...,w(X))`, define

\[
 u_w(m)
 =\sum_{k\le X/m}\mu(k)w(mk),
 \qquad 2\le m\le X,
 \tag{D-23801.9}
\]

\[
 U_w(j)=\sum_{m=j}^X u_w(m),
 \tag{D-23801.10}
\]

and the normalized tail profile

\[
 \boxed{
 F_w(j)=\frac{U_w(j)}{j-1},
 \qquad
 F_w(X+1)=F_w(X+2)=0.}
 \tag{D-23801.11}
\]

The transform is finite and exact. It contains every Möbius sign; no estimate
has been taken.

## 4. Exact curvature factorization

Let `c` be any coefficient vector and put `w=B_X^Tc`. Then

\[
 \boxed{
 u_w(m)
 =\sum_{n=m}^X c(n)
 \left(\frac{2m}{n+1}-1\right).}
 \tag{D-23801.12}
\]

Indeed, for `n>=m`,

\[
 \sum_{k\le n/m}\mu(k)\beta_{n,mk}
 =\frac{2m}{n+1}-1.
 \tag{D-23801.13}
\]

To verify (D-23801.13), use

\[
 \beta_{nq}
 =\frac{q a_{nq}(a_{nq}+1)}{n+1}-a_{nq},
 \tag{D-23801.14}
\]

and the two divisor identities

\[
 \sum_{k\le y}\mu(k)\left\lfloor\frac yk\right\rfloor=1,
 \tag{D-23801.15}
\]

\[
 \sum_{k\le y}
 \mu(k)k
 \left\lfloor\frac yk\right\rfloor
 \left(\left\lfloor\frac yk\right\rfloor+1\right)=2.
 \tag{D-23801.16}
\]

For the second identity, expand `a(a+1)=2 sum_(r<=a) r`, put `l=kr`, and use
`sum_(k|l) mu(k)=1_(l=1)`.

Summing (D-23801.12) over `m>=j` gives

\[
 \boxed{
 F_w(j)
 =\sum_{n=j}^X
 c(n)\frac{n-j+1}{n+1}.}
 \tag{D-23801.17}
\]

Consequently

\[
 \boxed{
 c(j)
 =(j+1)\bigl[F_w(j)-2F_w(j+1)+F_w(j+2)\bigr].}
 \tag{D-23801.18}
\]

Thus exact Carry Saturation is equivalent to discrete convexity of the
Möbius-tail profile `F_(w_X)`.

## 5. Profile coordinates for every packing

For any coefficient vector `d`, define its Green profile

\[
 \boxed{
 P_d(j)
 =\sum_{n=j}^X
 d(n)\frac{n-j+1}{n+1},
 \qquad
 P_d(X+1)=P_d(X+2)=0.}
 \tag{D-23801.19}
\]

Then

\[
 \boxed{
 d(j)=(j+1)\Delta^2P_d(j),}
 \tag{D-23801.20}
\]

where

\[
 \Delta^2P(j)=P(j)-2P(j+1)+P(j+2).
\]

In particular,

```text
d>=0  iff  P_d is discretely convex with the declared terminal boundary.
```

Let

\[
 H_d(j)=F_w(j)-P_d(j).
 \tag{D-23801.21}
\]

The Möbius transform of the residual `rho_d=w-B_X^Td` is

\[
 v_d(m)
 =(m-1)H_d(m)-mH_d(m+1),
 \tag{D-23801.22}
\]

and finite Möbius inversion gives

\[
 \boxed{
 \rho_d(q)
 =\sum_{k\le X/q}v_d(qk).}
 \tag{D-23801.23}
\]

Therefore the carry-packing cone is exactly the finite profile cone

\[
 \boxed{
 \Delta^2P(j)\ge0,
 \qquad
 \sum_{k\le X/q}
 \bigl[(qk-1)(F_w(qk)-P(qk))
       -qk(F_w(qk+1)-P(qk+1))\bigr]
 \ge0.}
 \tag{D-23801.24}
\]

This is a one-dimensional convex obstacle with a finite Möbius-divisor obstacle.

## 6. Exact mass identities

For `d(j)=(j+1)Delta^2P(j)`, summation by parts gives

\[
 \boxed{
 \sum_{n=2}^X n d(n)
 =6P(2)+2\sum_{j=4}^X P(j),}
 \tag{D-23801.25}
\]

and

\[
 \boxed{
 \sum_{n=2}^X d(n)
 =3P(2)-2P(3).}
 \tag{D-23801.26}
\]

The sharp `8 sqrt(X)` packing target is therefore an area theorem for an
admissible convex profile.

## 7. Finite primal and dual

Let

\[
 G_n=\frac1{n+1}\sum_{j=0}^n\log\binom nj.
 \tag{D-23801.27}
\]

The carry-packing primal is

\[
 \boxed{
 \mathsf P_X
 =\max\left\{
 \sum_{n=2}^X d(n)G_n:
 d\ge0,\ B_X^Td\le w_X
 \right\}.}
 \tag{D-23801.28}
\]

Its exact finite LP dual is

\[
 \boxed{
 \mathsf P_X
 =\min\left\{
 \sum_{q=2}^X w_X(q)y(q):
 y\ge0,\ B_Xy\ge G
 \right\}.}
 \tag{D-23801.29}
\]

The feasible set is nonempty and bounded in the objective directions because
the diagonal of `B_X` is positive.

## 8. Proof boundary

Closed exactly in this definition:

- the carry matrix and packing cone;
- the Möbius-curvature factorization;
- the profile/residual reconstruction;
- the mass identities;
- finite LP duality.

Open:

- construction of a packing with objective `4 sqrt(X)-X^o(1)`;
- RH.
