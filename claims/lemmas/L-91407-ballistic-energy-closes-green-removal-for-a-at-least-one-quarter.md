# L-91407 — Ballistic energy closes the Green-removal density for every `a>=1/4`

Claim ID: `L-91407`  
Status: **PROVED UNCONDITIONAL RANGE EXTENSION**  
Created: 2026-08-12  
Depends on: `L-91406`; weighted Harris–FKG positivity from PR #396  
RH status: **unproved**

## 1. Statement

For

\[
 a\ge\frac14,
 \qquad
 s=2a,
 \qquad
 c=\zeta(1+s)^{-1},
\]

the exact final Green-removal density

\[
 B_a(t)
 =-c+\kappa aE_{s,0}(t)+4a^2E_{s,1}(t),
 \qquad
 \kappa=\sqrt{275/14},
\]

satisfies

\[
 \boxed{B_a(t)>0\qquad(t\ge0).}
 \tag{L-91407.1}
\]

Thus the compact Cauchy/Jordan arithmetic obstruction is confined to

\[
 \boxed{0<a<\frac14.}
 \tag{L-91407.2}
\]

This improves the previous elementary terminal threshold `a>=1/3`.

## 2. A uniform one-Green floor

Let `t` lie in the cell

\[
 \log N\le t<\log(N+1).
\]

Weighted Harris–FKG gives

\[
 \sum_{n\le N}\frac{F_s(n)}n
 >cH_N.
\]

Hence

\[
 E_{s,0}(t)>c[H_N-\log(N+1)].
\]

The sequence

\[
 H_N-\log(N+1)
\]

is strictly increasing because

\[
 \frac1{N+1}-\log\left(1+\frac1{N+1}\right)>0.
\]

Its first value is

\[
 \delta:=1-\log2.
\]

Therefore

\[
 \boxed{E_{s,0}(t)>c\delta\qquad(t\ge0).}
 \tag{L-91407.3}
\]

## 3. First-crossing reduction

Assume, for contradiction, that `B_a` becomes nonpositive. Since

\[
 B_a(0+)=-c+\kappa a>0
\]

and every arithmetic knot produces a positive jump, the first zero occurs during a free-flight interval and has

\[
 B_a'(t_*)\le0.
\]

By (L-91407.3),

\[
 B_a'(t_*)
 =4a^2E_{s,0}(t_*)-\kappa ac
 \ge-ac(\kappa-4a\delta).
\]

Thus

\[
 |B_a'(t_*)|
 \le ac(\kappa-4a\delta).
 \tag{L-91407.4}
\]

The monotone ballistic energy of `L-91406` gives

\[
 B_a(t_*)+\frac{B_a'(t_*)^2}{8a^2c}
 \ge
 \mathscr K_0,
\]

where

\[
 \mathscr K_0
 =-c+\kappa a
 +\frac{(4a^2-\kappa ac)^2}{8a^2c}.
\]

At the first zero, equations (L-91407.4) and the preceding inequality imply

\[
 0\ge
 \mathscr K_0-rac c8(\kappa-4a\delta)^2.
\]

A direct simplification gives

\[
 \boxed{
 \mathscr K_0-rac c8(\kappa-4a\delta)^2
 =-c+\kappa ac\delta
  +\frac{2a^2}{c}(1-c^2\delta^2).
 }
 \tag{L-91407.5}
\]

It remains to prove that the right side is positive.

## 4. Elementary zeta bound

For every `s>0`, convexity of `x^(-1-s)` on each unit interval gives

\[
 \int_1^\infty x^{-1-s}dx
 \le\frac12+\sum_{n=2}^\infty n^{-1-s}.
\]

Therefore

\[
 \zeta(1+s)\ge\frac1s+\frac12.
\]

With `s=2a`,

\[
 \boxed{
 c\le\frac{2a}{1+a}.
 }
 \tag{L-91407.6}
\]

Put

\[
 D_a(c)
 =-c+\kappa ac\delta
  +\frac{2a^2}{c}(1-c^2\delta^2).
\]

On `1/4<=a<=1/2`,

\[
 -1+\kappa a\delta-2a^2\delta^2<0,
\]

because `kappa<9/2` and `delta<1/3`. Hence `D_a(c)` is strictly decreasing in `c`. By (L-91407.6),

\[
 D_a(c)
 \ge D_a\left(\frac{2a}{1+a}\right)
 =\frac{a}{1+a}P(a),
 \tag{L-91407.7}
\]

where

\[
 P(a)
 =(1-4\delta^2)a^2+(2+2\kappa\delta)a-1.
\]

The polynomial is strictly increasing for `a>0`. At `a=1/4`,

\[
 P(1/4)
 =\frac{\kappa\delta}{2}
  -\frac{\delta^2}{4}
  -\frac7{16}.
\]

Use the elementary bounds

\[
 \kappa>4,
 \qquad
 \frac3{10}<\delta<\frac13.
\]

They give

\[
 P(1/4)
 >\frac35-\frac1{36}-\frac7{16}
 =\frac{97}{720}>0.
 \tag{L-91407.8}
\]

Thus `D_a(c)>0` for every `1/4<=a<=1/2`, contradicting the first-zero inequality.

For `a>=1/2`, positivity was already proved in PR #396; alternatively the same first-crossing argument may be combined with its terminal zeta bound. This proves (L-91407.1).

## 5. Consequence

The complete final arithmetic boundary density is now unconditional on three regions:

```text
all t when a>=1/4;                 CLOSED HERE
all sufficiently small a>0;       INHERITED FROM PR #396
first logarithmic cell and tail;  INHERITED FOR EVERY a
```

The only unresolved set is a compact middle strip contained in

\[
 0<a<\frac14.
\]

The proof uses the coupled contact/one-Green/two-Green dynamics rather than estimating the two Green orders independently. It therefore survives the one-sided-FKG firewall of `R-91401`.

```text
uniform E_0 floor c(1-log2)       EXACT
first-crossing slope orientation   EXACT
ballistic-energy contradiction     EXACT
Green density for a>=1/4           PROVED
remaining compact small-a strip    OPEN
completed critical intertwiner      OPEN / RH-BEARING
Riemann Hypothesis                  UNPROVED
```
