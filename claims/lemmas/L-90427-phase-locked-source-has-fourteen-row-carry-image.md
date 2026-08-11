# L-90427 — The phase-locked factor-16 source has an exact fourteen-row carry image

Claim ID: `L-90427`  
Title: Applying the critical adjoint to the dyadic dipole produces the unique phase-locked factor-16 source and compresses its complete average-carry image to fourteen explicit rows  
Status: **PROPOSED COMPLETE EXACT FINITE-CARRY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Corrected: 2026-08-11 to distinguish full and column-one-deleted Riesz sums  
Dependencies: `L-90423`, `L-90424`, `L-90426`; elementary prefix averaging  
Scope: source and finite carry image; no sign or RH claim

## 1. Critical adjoint factorization

The phase-locked normalized source polynomial is

\[
\frac12Q_*(y)
 =(1-y)(1-y/2)(1-2y)(1-4y).
\tag{L-90427.1}
\]

Thus, with `omega_2` from `L-90426`,

\[
\boxed{
 b_*
 = (\varepsilon-2\delta_2)
   *(\varepsilon-4\delta_2)
   *\omega_2.
}
\tag{L-90427.2}
\]

The two new factors are exactly the critical-circle adjoints of `1-y` and `1-y/2`. Hence `b_*` is the source-level critical adjoint square of the dyadic dipole.

Its divisor-prefix sequence is

\[
\boxed{
\mathbf1*b_*
 =\delta_1-\frac{15}{2}\delta_2
  +\frac{35}{2}\delta_4
  -15\delta_8+4\delta_{16}.
}
\tag{L-90427.3}
\]

The corresponding prefix potential is

\[
H_*(m)=
\begin{cases}
0,&m=0,\\
1,&m=1,\\
-13/2,&2\le m\le3,\\
11,&4\le m\le7,\\
-4,&8\le m\le15,\\
0,&m\ge16.
\end{cases}
\tag{L-90427.4}
\]

Both its terminal value and its complete finite sum vanish:

\[
H_*(m)=0\ (m\ge16),
\qquad
\sum_{j=0}^{15}H_*(j)=0.
\tag{L-90427.5}
\]

## 2. Exact fourteen-row image

Use the average-carry identity

\[
Y_*(n):=\sum_{q=2}^n b_*(q)\beta_{nq}
 =H_*(n)-\frac2{n+1}\sum_{j=0}^nH_*(j).
\tag{L-90427.6}
\]

Substitution of (L-90427.4) gives

\[
\boxed{
Y_*(n)=
\begin{cases}
-17/6,&n=2,\\
-1/2,&n=3,\\
(101-11n)/(n+1),&4\le n\le7,\\
4(n-31)/(n+1),&8\le n\le15,\\
0,&n\ge16.
\end{cases}}
\tag{L-90427.7}
\]

Therefore the complete infinite source has exactly fourteen nonzero average-carry rows.

The sign pattern is

```text
rows 2,3:   negative;
rows 4--7:  positive;
rows 8--15: negative;
rows >=16:  zero.
```

This is a source-specific finite compression, not a universal bounded-rank geometry statement.

## 3. Pairing with an arbitrary carry target

Suppose a finite target `w(q)` on columns `2<=q<=X` has the triangular representation

\[
w(q)=\sum_{n=q}^X c(n)\beta_{nq}.
\tag{L-90427.8}
\]

Pairing with `b_*` and switching finite sums gives exactly

\[
\boxed{
\sum_{q=2}^X b_*(q)w(q)
 =\sum_{n=2}^{15}Y_*(n)c(n),
}
\tag{L-90427.9}
\]

for every `X>=15`.

Thus every target consumer of the phase-locked source is a fixed fourteen-row scalar. No coefficient above row fifteen enters.

## 4. Full and column-one-deleted Riesz sums

The distinction in this section is load bearing. Define

\[
\mathcal R_f^{\rm full}(X)
 =\sum_{1\le n\le X}\frac{f(n)}{\sqrt n}
   \log\frac Xn,
\tag{L-90427.10}
\]

and

\[
\mathcal R_f^{\circ}(X)
 =\sum_{2\le n\le X}\frac{f(n)}{\sqrt n}
   \log\frac Xn.
\tag{L-90427.11}
\]

For a source dilation,

\[
\boxed{
\mathcal R_{\delta_d*f}^{\rm full}(X)
 =d^{-1/2}\mathcal R_f^{\rm full}(X/d).
}
\tag{L-90427.12}
\]

Using (L-90427.2),

\[
\boxed{
\mathcal R_{b_*}^{\rm full}(X)
 =\mathcal R_{\omega_2}^{\rm full}(X)
  -3\sqrt2\,\mathcal R_{\omega_2}^{\rm full}(X/2)
  +4\mathcal R_{\omega_2}^{\rm full}(X/4).
}
\tag{L-90427.13}
\]

Both sources have coefficient one at `n=1`, so

\[
\mathcal R_f^{\rm full}(X)
 =\mathcal R_f^{\circ}(X)+\log X.
\tag{L-90427.14}
\]

Consequently the actual carry-column pairing, which deletes column one, satisfies

\[
\boxed{
\begin{aligned}
\mathcal R_{b_*}^{\circ}(X)
={}&\mathcal R_{\omega_2}^{\circ}(X)
 -3\sqrt2\,\mathcal R_{\omega_2}^{\circ}(X/2)
 +4\mathcal R_{\omega_2}^{\circ}(X/4)\\
&+(4-3\sqrt2)\log X
 +(3\sqrt2-8)\log2.
\end{aligned}}
\tag{L-90427.15}
\]

The last line is an explicit elementary gauge. It may not be omitted when translating between the finite carry charge and the full convolution identity.

## 5. Exact Möbius-adjoint coordinate and the column-one firewall

For a target `w(2),...,w(X)`, extend it by `w(1)=0` and define

\[
u_m=\sum_{k\le X/m}\mu(k)w(mk).
\tag{L-90427.16}
\]

Since `b_*=c_* *\mu` with `c_*=\mathbf1*b_*`, finite switching gives

\[
\boxed{
\sum_{q=2}^X b_*(q)w(q)
 =u_1-\frac{15}{2}u_2
  +\frac{35}{2}u_4-15u_8+4u_{16}.
}
\tag{L-90427.17}
\]

The `u_1` term is mandatory. Dropping it would silently restore the deleted column-one target value and is false in general.

## 6. Proof boundary

Closed exactly here:

1. source-level adjoint factorization;
2. finite prefix potential;
3. exact fourteen-row carry image;
4. finite target pairing;
5. full Riesz scale relation;
6. exact column-one gauge;
7. five-state Möbius-adjoint representation including `u_1`.

Open:

1. a critical bound or sign for the fourteen-row scalar;
2. the corresponding filtered bottom charge;
3. RH.
