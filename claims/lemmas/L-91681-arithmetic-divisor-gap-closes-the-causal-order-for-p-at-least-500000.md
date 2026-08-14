# L-91681 — The arithmetic divisor gap closes the causal inner order for every rough prime at least 500000

Claim ID: `L-91681`  
Status: **PROVED EXACT ANALYTIC + DIRECTED TAIL THEOREM**  
Created: 2026-08-14  
Depends on: `L-91359`; scope correction `R-91311`; exact replay `X-91681`  
RH status: **unproved**

## 1. Purpose

`L-91359` proves global monotonicity of the score-normalized component profile

\[
 \Phi_j(Y)=\frac{Q_Y(j)}{5\sqrt Y-3},
 \qquad 2\le j\le66.
\]

The same lemma closes the child-inactive sector of the causal packet.  `R-91311` correctly shows that the continuously parametrized child-active ratio need not be monotone for arbitrary nearby real arguments.

The actual arithmetic arguments are not arbitrary nearby reals.  They have the form

\[
 z=\frac yd,
 \qquad d\mid P_{61},
 \qquad d\le y<67,
\]

and distinct active divisors have a fixed logarithmic separation.  This theorem uses that arithmetic gap to close the entire unbounded rough-prime tail.

## 2. Causal ratio identity

Put

\[
 S(Y)=5\sqrt Y-3,
 \qquad r=p^{-1/2},
\]

and define the child-active causal row-per-score ratio

\[
 \mathcal R_{p,j}(z)
 =\frac{Q_{pz}(j)-rQ_z(j)}
 {S(pz)-rS(z)}.
 \tag{L-91681.1}
\]

For `1<=Y<j`, extend `Phi_j(Y)` by zero, consistently with the causal row `Q_Y(j)=0`.

Since `Q_Y=Phi_j(Y)S(Y)`, direct algebra gives

\[
 \boxed{
 \mathcal R_{p,j}(z)
 =\Phi_j(pz)
  +\theta_p(z)\,[\Phi_j(pz)-\Phi_j(z)],
 }
 \tag{L-91681.2}
\]

where

\[
 \theta_p(z)
 =\frac{rS(z)}{S(pz)-rS(z)}.
 \tag{L-91681.3}
\]

For `p>1` and `z>=1`, the denominator is positive and

\[
 \boxed{
 0\le\theta_p(z)<\frac1{p-1}.
 }
 \tag{L-91681.4}
\]

Indeed, after multiplying by `sqrt(p)`, inequality (L-91681.4) is equivalent to

\[
 (p-1)(5\sqrt z-3)
 <5\sqrt z(p-1)-3(\sqrt p-1),
\]

which reduces to `p>sqrt(p)`.

Because `Phi_j` is increasing, the correction in (L-91681.2) is nonnegative.

## 3. Uniform upper bound for the normalized row

Use the constants of `L-91359`:

\[
 c_j=\frac2{j(j-1)},
 \qquad
 a_j=\frac{j+2}{j\sqrt j},
 \qquad
 b_j=\frac1{\sqrt{j+1}},
 \tag{L-91681.5}
\]

\[
 \eta_j
 =c_j\left(1+\sum_{m<j}m^{-1/2}\right)-a_j+b_j>0,
 \tag{L-91681.6}
\]

and

\[
 K_j
 =-4c_j
 +c_j\sum_{m<j}m^{-1/2}\log m
 -a_j\log j+b_j\log(j+1).
 \tag{L-91681.7}
\]

The directed replay proves `K_j<0` for every row `2<=j<=66`.  Equation `L-91359.10` therefore gives

\[
 Q_Y(j)\le4c_j\sqrt Y
 \qquad(Y\ge j).
\]

Since `sqrt(Y)/(5sqrt(Y)-3)` decreases with `Y`,

\[
 \boxed{
 0\le\Phi_j(Y)\le
 B_j:=\frac{4c_j}{5-3/\sqrt j}
 \qquad(Y\ge1).
 }
 \tag{L-91681.8}
\]

## 4. Explicit derivative reserve

Put

\[
 \boxed{
 A_j(p)
 =5\eta_j\log p
  -22c_j-10\eta_j-5K_j.
 }
 \tag{L-91681.9}
\]

The normalized derivative numerator in `L-91359` satisfies, for every `Y>=p`,

\[
 M_j(Y)
 \ge\sqrt Y\,A_j(p).
 \tag{L-91681.10}
\]

Moreover

\[
 \frac{d\Phi_j}{d\log Y}
 =\frac{M_j(Y)}{2(5\sqrt Y-3)^2}.
\]

Using `(5sqrt(Y)-3)^2<25Y`,

\[
 \boxed{
 \frac{d\Phi_j}{d\log Y}
 \ge\frac{A_j(p)}{50\sqrt Y}
 \qquad(Y\ge p).
 }
 \tag{L-91681.11}
\]

The replay below proves `A_j(500000)>0` for all 65 rows.

## 5. The arithmetic gap

Let

\[
 d_1<d_2,
 \qquad d_1,d_2\mid P_{61},
 \qquad d_2\le y<67,
\]

and put

\[
 z_i=\frac y{d_i}.
\]

Then

\[
 z_1>z_2\ge1,
 \qquad z_1<67.
\]

Since `d_1,d_2` are distinct positive integers at most `66`,

\[
 \boxed{
 \log\frac{z_1}{z_2}
 =\log\frac{d_2}{d_1}
 \ge\delta_0:=\log\frac{66}{65}.
 }
 \tag{L-91681.12}
\]

Integrating (L-91681.11) from `pz_2` to `pz_1` and using `z_1<67` gives

\[
 \boxed{
 \Phi_j(pz_1)-\Phi_j(pz_2)
 \ge
 \frac{\delta_0A_j(p)}{50\sqrt{67p}}.
 }
 \tag{L-91681.13}
\]

## 6. Causal order on the child-active sector

From (L-91681.2), discard the nonnegative correction at `z_1` and use (L-91681.4), (L-91681.8) at `z_2`:

\[
\begin{aligned}
 \mathcal R_{p,j}(z_1)-\mathcal R_{p,j}(z_2)
 &\ge
 \Phi_j(pz_1)-\Phi_j(pz_2)\\
 &\quad-	heta_p(z_2)
 [\Phi_j(pz_2)-\Phi_j(z_2)]\\
 &>
 \frac{\delta_0A_j(p)}{50\sqrt{67p}}
 -\frac{B_j}{p-1}.
\end{aligned}
 \tag{L-91681.14}
\]

Thus one explicit scalar inequality per row suffices.

## 7. Directed exact tail gate

The companion verifier uses:

```text
exact Fraction arithmetic;
directed decimal square-root intervals;
directed positive-tail atanh intervals for logarithms;
70 decimal digits in the primitive enclosures.
```

At

\[
 P_0=500000
\]

it proves, for every `2<=j<=66`,

\[
 \boxed{
 \frac{\delta_0A_j(P_0)}{50\sqrt{67P_0}}
 -\frac{B_j}{P_0-1}>0.
 }
 \tag{L-91681.15}
\]

The smallest directed lower margin occurs at `j=66` and is greater than

\[
 6.81\times10^{-9}.
\]

More precisely, the retained outward computation reports

```text
minimum lower left side   6.951977823131507e-9
maximum upper right side  1.392008272476988e-10
minimum certified margin  6.812776995883809e-9
```

The function `A_j(p)` is increasing because `eta_j>0`, and `(p-1)/sqrt(p)` is increasing for `p>1`.  Since `A_j(P_0)>0`, multiplying (L-91681.15) by the positive monotone factors proves the same inequality for every real

\[
 p\ge500000.
\]

Consequently

\[
 \boxed{
 d_1<d_2\le y
 \Longrightarrow
 \mathcal R_{p,j}(y/d_1)
 >\mathcal R_{p,j}(y/d_2)
 }
 \tag{L-91681.16}
\]

for all `p>=500000`, all `1<=y<67`, all active `P_61` divisors and all rows `2<=j<=66`.

## 8. Cross-boundary and child-inactive sectors

If `d_1<=y<d_2`, the first causal ratio contains the nonnegative correction in (L-91681.2), while the child term at `d_2` is zero.  Since `d_1<d_2`, global monotonicity of `Phi_j` gives

\[
 \mathcal R_{p,j}(y/d_1)
 \ge\Phi_j(py/d_1)
 >\Phi_j(py/d_2),
 \tag{L-91681.17}
\]

which is the child-inactive ratio at `d_2`.

If `y<d_1<d_2`, the result is exactly `L-91359.19`.

Combining these cases with (L-91681.16), the complete divisor-ordered causal profile is strictly decreasing in `d` for every rough prime `p>=500000`.

## 9. What this removes

The continuous counterexample of `R-91311` is valid but no longer blocks the unbounded prime range.  Its bad pair uses arbitrarily close real arguments; the arithmetic source cannot realize such a pair because distinct active divisors satisfy (L-91681.12).

The remaining profile theorem is finite:

\[
 \boxed{
 67\le p<500000,
 \qquad1\le y<67,
 \qquad d\mid P_{61},
 \qquad2\le j\le66.
 }
 \tag{L-91681.18}
\]

A directed activation-cell replay can either close this corridor or emit an exact arithmetic counterexample.

## 10. Exact boundary

```text
continuous causal monotonicity                     FALSE / R-91311
arithmetic inner-divisor gap                        EXACT
causal child-active order for p>=500000             EXACT
cross-boundary order                                EXACT
global child-inactive order                         EXACT / L-91359
entire unbounded rough-prime profile tail           CLOSED
finite corridor 67<=p<500000                        OPEN / FINITE-DIRECTED
full even/odd determinant                           OPEN / FINITE-ANALYTIC
target-proportional/Lorenz packet producer          CONDITIONAL ON THOSE SIGNS
Riemann Hypothesis                                  UNPROVED
```
