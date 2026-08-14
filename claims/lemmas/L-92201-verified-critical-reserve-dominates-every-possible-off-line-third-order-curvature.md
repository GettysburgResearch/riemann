# L-92201 — The verified critical reserve dominates every possible off-line third-order curvature

Claim ID: `L-92201`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-92200`; Platt–Trudgian verified height; Trudgian local-count lock  
RH status: **unproved**

## 1. External constants

Use the source lock

\[
 H=3{,}000{,}175{,}332{,}800.
\]

Every zeta zero with positive ordinate at most `H` is simple and on the
critical line.  Every possible off-line zero therefore has ordinate
`b>H`.

The Riemann–von Mangoldt formula gives a verified simple critical zero

\[
 \rho_0=\frac12+i\gamma_0,
 \qquad
 0<\gamma_0\le H/2.
\]

In the squared-pole expansion of `L-92200` it supplies the real parameter

\[
 r_0=\gamma_0^2\le H^2/4
\]

of weight

\[
 w_0=2.
\]

The local multiplicity lock is

\[
 N(B+2)-N(B-2)\le2\log(B+3)
 \qquad(B\ge H).
\]

Consequently the total squared-pole weight in this interval is at most

\[
 \boxed{W_B\le4\log(B+3).}
 \tag{L-92201.1}
\]

## 2. Geometry of a possible off-line pole

Let one squared-pole parameter arising from a possible off-line zero be

\[
 s=c+id,
 \qquad
 c=b^2-a^2,
 \qquad
 d=2ab,
 \qquad
 0<|a|<\frac12,
 \qquad
 b>H.
\]

Then

\[
 c\ge b^2-\frac14,
 \qquad
 |d|\le b.
 \tag{L-92201.2}
\]

For `t>1/4` put

\[
 A=t+c,
 \qquad
 A_0=t+r_0,
 \qquad
 C=c-r_0.
\]

Because `r_0<=H^2/4` and `b>=H`,

\[
 \boxed{
 A\ge A_0,
 \qquad
 C\ge\frac23b^2.
 }
 \tag{L-92201.3}
\]

## 3. Positive coupling to the verified anchor

The unordered pair contribution of `s` and `r_0` to the curvature in
`L-92200` is

\[
 2w_0w_s
 \Re\frac{(s-r_0)^2}
 {(t+s)^3(t+r_0)^3}.
\]

The phase of the numerator relative to `C^2` is at most

\[
 2\arctan\frac{|d|}{C}
 \le2\arctan\frac{3}{2b},
\]

and the phase introduced by `(t+s)^(-3)` is at most

\[
 3\arctan\frac{|d|}{A}
 \le3\arctan\frac2b.
\]

At `b>=H` their sum is far below `pi/2`; the modulus correction is also
smaller than `10^{-20}`.  The deliberately coarse bound

\[
 \boxed{
 \Re\frac{(s-r_0)^2}{(t+s)^3}
 \ge\frac12\frac{C^2}{A^3}
 }
 \tag{L-92201.4}
\]

therefore holds with enormous margin.

Using `w_0=2`, (L-92201.3), and `A_0<=A`, the positive anchor contribution is
at least

\[
\boxed{
 P_s(t)
 \ge\frac89\,w_s\frac{b^4}{A^6}.
 }
\tag{L-92201.5}
\]

## 4. Separated heights are automatically positive

Consider two squared-pole parameters `s_i,s_j`, with associated positive
ordinates `b_i,b_j`.  If

\[
 |b_i-b_j|\ge2,
\]

then

\[
 |\Re(s_i-s_j)|
 \ge2(b_i+b_j)-\frac14,
 \qquad
 |\Im(s_i-s_j)|\le b_i+b_j.
\]

Thus the argument of `(s_i-s_j)^2` has absolute value below
`2 arctan(0.501)`.  The total denominator rotation is below `6/H` whenever a
nonreal pole is present.  Their sum is less than `pi/2`, so

\[
\boxed{
 \Re\frac{(s_i-s_j)^2}
 {(t+s_i)^3(t+s_j)^3}\ge0
 \qquad(|b_i-b_j|\ge2).
 }
\tag{L-92201.6}

Therefore a negative pair interaction can occur only inside one four-unit
height neighbourhood.

## 5. Crude bound for every local negative interaction

Fix a nonreal pole `s_i` with ordinate `B=b_i`.  If
`|b_j-B|<2`, then

\[
 |s_i-s_j|^2\le30B^2.
\]

Moreover

\[
 |t+s_i|\ge A_i,
 \qquad
 |t+s_j|\ge A_i/2
\]

because `B>=H`.  Hence

\[
 \left|
 \frac{(s_i-s_j)^2}
 {(t+s_i)^3(t+s_j)^3}
 \right|
 \le240\frac{B^2}{A_i^6}.
\]

After including the factor two from the unordered pair and summing all local
squared-pole weights using (L-92201.1), the full possibly negative row attached
to `s_i` is bounded by

\[
\boxed{
 N_i(t)
 \le1920\,w_i
 \frac{B^2\log(B+3)}{A_i^6}.
 }
\tag{L-92201.7
}

This row sum deliberately double-counts a negative pair of two nonreal poles;
that only strengthens the domination below.

## 6. Anchor domination

For every `B>=H`,

\[
 \boxed{
 B^2>2160\log(B+3).
 }
 \tag{L-92201.8}

At the verified endpoint the ratio of the two sides exceeds
`10^20`, and it increases thereafter.

Combining (L-92201.5)--(L-92201.8),

\[
 \boxed{P_{s_i}(t)>N_i(t)}
 \qquad(t>1/4)
\]

for every possible nonreal squared pole.

All real-real interactions are nonnegative.  Every separated interaction is
nonnegative by (L-92201.6).  Every remaining local negative interaction is
charged to one or two nonreal rows and is dominated by the corresponding
positive coupling to the single verified critical anchor.

Therefore the complete pairwise curvature satisfies

\[
\boxed{
 p(t)p''(t)-2p'(t)^2>0
 \qquad(t>1/4).
 }
\tag{L-92201.9}

The strict sign also follows independently from the existence of at least two
distinct verified real squared poles.

## 7. Consequence

The safe Xi impedance

\[
 Z(t)=\frac1{p(t)}
\]

is strictly concave on the complete safe axis:

\[
 \boxed{Z''(t)<0\qquad(t>1/4).}
\]

This closes the hard scalar curvature left open on PR #445, subject to
independent review of the grouped product, the angle bounds, and the external
source locks.

## 8. Review joints

1. the exact correspondence between zero multiplicities and squared-pole
   weights;
2. the local weight bound `W_B<=4 log(B+3)`;
3. the argument estimate in (L-92201.4);
4. the sign localization in (L-92201.6);
5. double-counting conventions in (L-92201.7);
6. passage from finite height truncations to the normally convergent full
   curvature sum.

## 9. Exact boundary

```text
verified critical anchor                         EXTERNAL RIGOROUS INPUT
explicit local multiplicity bound                EXTERNAL + ELEMENTARY
separated-height pair positivity                 PROPOSED COMPLETE
local negative-row bound                         PROPOSED COMPLETE
verified-anchor domination                       PROPOSED COMPLETE
safe Xi reciprocal curvature                     PROPOSED UNCONDITIONAL
all-order complete Bernstein property             OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
