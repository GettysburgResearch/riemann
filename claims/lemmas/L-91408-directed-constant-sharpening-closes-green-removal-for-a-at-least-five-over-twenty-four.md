# L-91408 — Directed constant sharpening closes Green removal for `a>=5/24`

Claim ID: `L-91408`  
Status: **PROVED UNCONDITIONAL RANGE SHARPENING**  
Created: 2026-08-12  
Depends on: `L-91407`  
RH status: **unproved**

## 1. Statement

The final Green-removal density of PR #396 satisfies

\[
 \boxed{
 B_a(t)>0
 \qquad
 \left(a\ge\frac5{24},\ t\ge0\right).
 }
 \tag{L-91408.1}
\]

Consequently its unresolved arithmetic range is confined to

\[
 \boxed{0<a<\frac5{24}.}
 \tag{L-91408.2}
\]

## 2. Scalar gate from the ballistic proof

`L-91407` reduces the first-crossing contradiction to positivity of

\[
 D_a(c)
 =-c+\kappa ac\delta
  +\frac{2a^2}{c}(1-c^2\delta^2),
 \tag{L-91408.3}
\]

where

\[
 c=\zeta(1+2a)^{-1},
 \qquad
 \delta=1-\log2,
 \qquad
 \kappa=\sqrt{275/14}.
\]

For `a<=1/2`, this expression decreases in `c`. The elementary zeta bound

\[
 c\le\frac{2a}{1+a}
\]

therefore gives

\[
 D_a(c)
 \ge\frac{a}{1+a}P(a),
 \tag{L-91408.4}
\]

with

\[
 P(a)
 =(1-4\delta^2)a^2
 +(2+2\kappa\delta)a-1.
 \tag{L-91408.5}
\]

The polynomial is strictly increasing on the positive half-line.

## 3. Directed rational constants

Use

\[
 \boxed{
 \frac{6931}{10000}<\log2<\frac{6932}{10000}.
 }
 \tag{L-91408.6}
\]

These bounds follow, for example, from the positive atanh expansion

\[
 \log2
 =2\sum_{j\ge0}\frac{1}{(2j+1)3^{2j+1}}
\]

with a geometric tail enclosure. Thus

\[
 \frac{3068}{10000}<\delta<\frac{3069}{10000}.
 \tag{L-91408.7}
\]

Also

\[
 \boxed{\kappa>\frac{443}{100}}
 \tag{L-91408.8}
\]

because

\[
 \left(\frac{443}{100}\right)^2
 =\frac{196249}{10000}
 <\frac{275}{14}.
\]

At `a=5/24`, equations (L-91408.7)--(L-91408.8) give the directed lower bound

\[
\begin{aligned}
 P(5/24)
 &>
 \frac{25}{576}
 \left[1-4\left(\frac{3069}{10000}\right)^2\right]\\
 &\quad+
 \frac5{24}
 \left[2+2\left(\frac{443}{100}\right)
              \left(\frac{3068}{10000}\right)\right]
 -1\\
 &>\frac1{100}>0.
\end{aligned}
 \tag{L-91408.9}
\]

Since `P` is increasing,

\[
 P(a)>0
 \qquad(a\ge5/24).
\]

This proves `D_a(c)>0` throughout `5/24<=a<=1/2`. The inherited terminal theorem covers `a>=1/2`, completing the proof.

## 4. Significance

The threshold improvement is not numerical reconnaissance. It follows from:

```text
one exact ballistic invariant;
one exact Harris–FKG one-Green floor;
one elementary zeta integral bound;
three directed rational constants.
```

A further improvement requires only sharper input to the one-variable gate `P(a)>0` or a better uniform lower corridor for `E_{2a,0}`. No new continuous density analysis is required.

```text
Green density for a>=5/24          PROVED
remaining interval 0<a<5/24       OPEN
small-a cofinal positivity         INHERITED NON-EFFECTIVE
compact middle certification       OPEN / FINITE-ANALYTIC
completed critical intertwiner     OPEN / RH-BEARING
Riemann Hypothesis                 UNPROVED
```
