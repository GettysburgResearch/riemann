# L-90427 — The phase-locked factor-16 source has an exact fourteen-row carry image

Claim ID: `L-90427`  
Title: Applying the critical adjoint to the dyadic dipole produces the unique phase-locked factor-16 source and compresses its complete average-carry image to fourteen explicit rows  
Status: **PROPOSED COMPLETE EXACT FINITE-CARRY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
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

Suppose a finite target `w(q)` has the triangular representation

\[
w(q)=\sum_{n=q}^X c(n)\beta_{nq}.
\tag{L-90427.8}
\]

Pairing with `b_*` and switching finite sums gives exactly

\[
\boxed{
\sum_{q\le X}b_*(q)w(q)
 =\sum_{n=2}^{15}Y_*(n)c(n),
}
\tag{L-90427.9}
\]

for every `X>=15`.

Thus every target consumer of the phase-locked source is a fixed fourteen-row scalar. No coefficient above row fifteen enters.

## 4. Relation to the two-row dipole

Let

\[
\mathcal R_f(X)
 =\sum_{n\le X}\frac{f(n)}{\sqrt n}
   \log\frac Xn.
\tag{L-90427.10}
\]

For a source dilation,

\[
\mathcal R_{\delta_d*f}(X)
 =d^{-1/2}\mathcal R_f(X/d).
\tag{L-90427.11}
\]

Using (L-90427.2),

\[
\boxed{
\mathcal R_{b_*}(X)
 =\mathcal R_{\omega_2}(X)
  -3\sqrt2\,\mathcal R_{\omega_2}(X/2)
  +4\mathcal R_{\omega_2}(X/4).
}
\tag{L-90427.12}
\]

Thus the fourteen-row source is not independent of the two-row bottom charge: it is its exact critically adjointed three-scale filter.

## 5. Proof boundary

Closed exactly here:

1. source-level adjoint factorization;
2. finite prefix potential;
3. exact fourteen-row carry image;
4. finite target pairing;
5. exact scale relation to the two-row dipole.

Open:

1. a critical bound or sign for the fourteen-row scalar;
2. the corresponding two-row filtered bound;
3. RH.
