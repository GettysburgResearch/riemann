# L-96301 — Rows two and three collapse to one positive-base scalar with a completely factored zero-safe numerator

Claim ID: `L-96301`  
Status: **PROVED EXACT FINITE AND MELLIN ALGEBRA**  
Created: 2026-08-17  
Depends on: the fixed-row formulas of PR #542; compatible with the two-row audit of PR #546  
RH status: **not assumed**

## 1. The two canonical rows

For the canonical component spline, the base coefficients are

\[
q_2(2)=3,\quad q_2(3)=0,\quad q_2(m)=1\ (m\ge4),
\]

and

\[
q_3(3)=2,\quad q_3(4)=-\frac23,\quad
q_3(m)=\frac13\ (m\ge5).
\]

Define the single scalar row

\[
\boxed{
\mathcal R_X=5c_X(2)+3c_X(3).
}
\tag{L-96301.1}
\]

Its unsieved base dictionary is

\[
q_*(m)=5q_2(m)+3q_3(m),
\]

hence

\[
\boxed{
q_*(2)=15,\qquad q_*(3)=6,\qquad q_*(4)=3,
\qquad q_*(m)=6\ (m\ge5).
}
\tag{L-96301.2}
\]

Every base coefficient is strictly positive. The negative shoulder of row three disappears before the Möbius sieve is applied.

## 2. Exact Mellin numerator

Put

\[
a=2^{-z},\qquad b=3^{-z}.
\]

The fixed-row numerators are

\[
P_2(z)=2a-1-b,
\]

and

\[
3P_3(z)=5b-a-1-3a^2.
\]

Therefore

\[
\boxed{
5P_2(z)+3P_3(z)
=-3(a-1)(a-2).
}
\tag{L-96301.3}
\]

If `0<Re(z)<1`, then

\[
\frac12<|2^{-z}|<1,
\]

so neither factor in (L-96301.3) can vanish. This is stronger than merely showing that rows two and three have no common open-strip zero: the complete consumer is one scalar.

## 3. Exact transform

The zeta coefficient of the combined row is

\[
5C_2+3C_3=5+1=6.
\]

Consequently, with `z=s+1/2`,

\[
\boxed{
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac6{s^2}
-
\frac{3(1-2^{-z})(2-2^{-z})}
{s^2\zeta(z)}.
}
\tag{L-96301.4}
\]

Every hypothetical off-line zero survives in this one transform.

## 4. Integer reduction

Between consecutive integer activation knots, every active logarithmic ramp is affine in `log X`. Hence `mathcal R_X` is affine in `log X` on each open cell. Positivity at both cell endpoints implies positivity throughout the cell.

Thus the producer may be stated on integers without losing the real-endpoint Landau conclusion.
