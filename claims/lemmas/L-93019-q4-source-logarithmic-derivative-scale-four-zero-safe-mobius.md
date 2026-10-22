# L-93019 - The compact Q4 source is the logarithmic derivative of one scale-four zero-safe Mobius source

Claim ID: `L-93019`  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/CONVOLUTION DICTIONARY - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `T-93010` for the compact-Q4 source; elementary Dirichlet-series algebra  
Scope: exact source identities and a cross-route dictionary; no Cycle-Debt, Q4-mean, or RH estimate

## 1. The scale-four zero-safe factor

Put

\[
B_4(s)
=
\frac{1-4^{1-s}}{1-4^{-s}}
\tag{L-93019.1}
\]

and

\[
A_4(s)
=
\frac{B_4(s)}{\zeta(s)}.
\tag{L-93019.2}
\]

For \(\Re s>1\),

\[
B_4(s)
=
1-3\sum_{r\ge1}4^{-rs}.
\tag{L-93019.3}
\]

Thus \(B_4\) has Dirichlet coefficients

\[
b_4(1)=1,
\qquad
b_4(4^r)=-3\quad(r\ge1),
\qquad
b_4(n)=0\quad\text{otherwise}.
\tag{L-93019.4}
\]

Let

\[
a_4=b_4*\mu,
\tag{L-93019.5}
\]

so that

\[
A_4(s)=\sum_{n\ge1}\frac{a_4(n)}{n^s}.
\tag{L-93019.6}
\]

The factor \(B_4\) has zeros only on \(\Re s=1\) and poles only on
\(\Re s=0\). Hence it is finite and nonzero at every nontrivial zeta zero in

\[
0<\Re s<1.
\tag{L-93019.7}
\]

The source \(A_4=B_4/\zeta\) therefore retains every open-strip reciprocal-zeta
singularity.

## 2. Exact two-adic coefficients

Write

\[
n=2^e m,
\qquad m\ \text{odd}.
\tag{L-93019.8}
\]

If \(m\) is not squarefree then \(a_4(n)=0\). If \(m\) is squarefree, then

\[
\boxed{
a_4(2^e m)
=
\begin{cases}
\mu(m),&e=0,\\
-\mu(m),&e=1,\\
3(-1)^{e+1}\mu(m),&e\ge2.
\end{cases}
}
\tag{L-93019.9}
\]

Indeed,

\[
a_4(n)
=
\mu(n)
-
3\sum_{\substack{r\ge1\\4^r\mid n}}
\mu(n/4^r),
\tag{L-93019.10}
\]

and among the terms on the right at most one has two-adic exponent zero or one.

After critical normalization, the complete two-adic tower is geometrically
summable:

\[
\frac{a_4(2^e m)}{\sqrt{2^e m}}
=
O\left(2^{-e/2}\right)\frac{\mu(m)}{\sqrt m}.
\tag{L-93019.11}
\]

This is the exact scale-four filtered Mobius state naturally paired with the Q4
source.

## 3. The Q4 gauge is the derivative of the dyadic factor

Differentiate (L-93019.1). A direct calculation gives

\[
\boxed{
(1-4^{1-s})\frac{B_4'(s)}{B_4(s)}
=
3(\log4)\frac{4^{-s}}{1-4^{-s}}.
}
\tag{L-93019.12}
\]

Since

\[
\frac{A_4'}{A_4}
=
\frac{B_4'}{B_4}
-
\frac{\zeta'}{\zeta},
\tag{L-93019.13}
\]

one obtains

\[
\boxed{
(1-4^{1-s})\frac{A_4'(s)}{A_4(s)}
=
(1-4^{1-s})
\left(-\frac{\zeta'}{\zeta}(s)\right)
+
3(\log4)\frac{4^{-s}}{1-4^{-s}}.
}
\tag{L-93019.14}
\]

The right side is exactly the Dirichlet series of the compact-Q4 source
\(c_\circ\) from `T-93010`:

\[
\boxed{
\sum_{n\ge1}\frac{c_\circ(n)}{n^s}
=
(1-4^{1-s})\frac{A_4'(s)}{A_4(s)}.
}
\tag{L-93019.15}
\]

Thus the delayed four-adic gauge is not an auxiliary correction. It is exactly
the logarithmic derivative of the zero-safe scale-four factor \(B_4\).

## 4. Exact coefficientwise convolution identity

Let

\[
(a_4\log)(n)=a_4(n)\log n.
\tag{L-93019.16}
\]

Because

\[
A_4'(s)
=
-\sum_{n\ge1}\frac{(a_4\log)(n)}{n^s},
\tag{L-93019.17}
\]

multiplying (L-93019.15) by \(A_4(s)\) gives the coefficientwise identity

\[
\boxed{
c_\circ*a_4
=
-(\varepsilon-4\delta_4)*(a_4\log).
}
\tag{L-93019.18}
\]

Equivalently, for every integer \(n\ge1\),

\[
\boxed{
\sum_{d\mid n}c_\circ(d)a_4(n/d)
=
-a_4(n)\log n
+
4\mathbf1_{4\mid n}\,
a_4(n/4)\log(n/4).
}
\tag{L-93019.19}
\]

All logarithms are retained prime by prime. This is an exact arithmetic
identity, not a formal equality after numerical evaluation.

## 5. The filtered Riesz scalar

Define the critical Riesz scalar of a coefficient sequence \(a\) by

\[
\mathcal R_a(X)
=
\sum_{n\le X}
\frac{a(n)}{\sqrt n}
\log\frac Xn.
\tag{L-93019.20}
\]

Using \(a_4=b_4*\mu\) and (L-93019.4),

\[
\boxed{
\mathcal R_{a_4}(X)
=
\mathcal R_\mu(X)
-
3\sum_{r\ge1}
2^{-r}\mathcal R_\mu(X/4^r).
}
\tag{L-93019.21}
\]

The sum is finite at every endpoint. Its Mellin transform is

\[
\boxed{
\int_1^\infty
\mathcal R_{a_4}(X)X^{-z-1}\,dX
=
\frac{A_4(z+1/2)}{z^2},
}
\tag{L-93019.22}
\]

initially in the half-plane of absolute convergence.

Because \(B_4\) is nonzero at every nontrivial zeta zero, no off-line pole of
\(1/\zeta(z+1/2)\) is cancelled in (L-93019.22).

## 6. Cross-route meaning

The two PR #474 routes are therefore linked at source level:

\[
\boxed{
\begin{array}{c}
\text{scale-four zero-safe Mobius state }a_4\\
\downarrow\ \text{logarithmic derivative}\\
\text{complete compact-Q4 source }c_\circ.
\end{array}
}
\tag{L-93019.23}
\]

The Cycle-Debt side seeks a capacity-faithful transport theorem for a
reciprocal-zeta state. The Q4 side studies a positive endpoint energy of its
scale-four logarithmic derivative.

This identity suggests two legitimate cross-route attacks:

1. construct a centered carry certificate for the geometrically summable
   two-adic source \(a_4\), then transfer its logarithmic derivative through
   (L-93019.18);
2. use the scalar Q4 mean to control the filtered Riesz state through the exact
   convolution equation.

Neither transfer estimate is proved here. In particular, convolution
invertibility alone supplies no positive or bounded carry map.

## 7. Proof boundary

Established exactly:

1. the scale-four dyadic factor and its coefficients;
2. the explicit two-adic formula for \(a_4\);
3. zero safety in the open critical strip;
4. the logarithmic-derivative identity for \(c_\circ\);
5. the coefficientwise convolution equation;
6. the filtered Riesz scalar and its finite scale-four expansion.

Open:

1. a capacity-faithful transfer between the filtered Riesz state and Q4 mean;
2. an unconditional square-root/polylogarithmic bound on either side;
3. RH.
