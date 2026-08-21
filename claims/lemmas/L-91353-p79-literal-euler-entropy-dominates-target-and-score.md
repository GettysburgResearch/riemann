# L-91353 — The literal `P_79` Euler-row entropy uniformly dominates both target and declared score

Claim ID: `L-91353`  
Status: **PROVED EXACT/DIRECTED RAW-ROW SCORE THEOREM — FINITE-FRONTIER ASSEMBLY STILL OPEN**  
Created: 2026-08-13  
Frozen main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Depends on: `L-91352`; the exact Euler identities of `L-91351`; exact/directed replay `X-91311`  
RH status: **unproved**

## 1. Target, score and literal entropy

Put

\[
 P=P_{79},
 \qquad
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d,
 \qquad
 B_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}{\sqrt d}.
\]

For `a=4` or `a=5`, define

\[
 \boxed{
 W_{a,P}(x)=a\sqrt x\,A_P(x)-3B_P(x).
 }
 \tag{L-91353.1}
\]

Thus `W_(4,P)` is the SHARP target and `W_(5,P)` is the declared endpoint source score.

Let `mathcal E_P` be the literal component-row entropy of `L-91352`:

\[
 \mathcal E_P(x)
 =\sum_{n\le x}\frac{\lambda_P(n)}{\sqrt n}\log\frac xn,
 \qquad
 \lambda_P(n)\ge0.
 \tag{L-91353.2}
\]

Set

\[
 \boxed{F_a(x)=\mathcal E_P(x)-W_{a,P}(x).}
 \tag{L-91353.3}
\]

## 2. Global finite Euler corridors

The exact activation scan in `X-91311` streams all

\[
 2^{22}=4,194,304
\]

divisors of `P` and proves

\[
 \boxed{
 A_P(x)<\frac15\qquad(x\ge83),
 }
 \tag{L-91353.4}
\]

with exact maximum at the activation `x=221`.  The same scan proves

\[
 \boxed{|A_P(x)|\le1,\qquad |B_P(x)|<\frac32\qquad(x\ge1).}
 \tag{L-91353.5}
\]

The `B_P` inequalities use fixed-denominator outward square-root enclosures and are checked at every activation state.

## 3. Exact finite-cell bound through `10,000`

On one integer cell

\[
 N\le x<N+1,
\]
write `u=sqrt(x)`.  The active coefficients in (L-91353.2) and (L-91353.1) are fixed, so

\[
 F_a(x)=2C_N\log u-D_N-aA_Nu+3B_N,
 \tag{L-91353.6}
\]

where `C_N>=0`.  Therefore

\[
 \frac{d^2}{du^2}F_a(x)=-\frac{2C_N}{u^2}\le0.
 \tag{L-91353.7}
\]

The minimum on each closed cell is attained at one of its two endpoints.  Activation jumps require both the left and right endpoint states; the checker evaluates both with exact atanh logarithm intervals and rational square-root intervals.

For every real

\[
 83\le x\le10000
\]

it proves

\[
 \boxed{F_4(x)>18,\qquad F_5(x)>18.}
 \tag{L-91353.8}
\]

Both minima occur at the right-hand state `x=83`.  The directed margins above `18` are respectively larger than

\[
 0.907123129000,
 \qquad
 1.026180268819.
 \tag{L-91353.9}
\]

## 4. An elementary prime lower bound

Let

\[
 \theta(t)=\sum_{q\le t\atop q\text{ prime}}\log q.
\]

The finite directed prime scan proves, with the real-cell endpoint convention,

\[
 \boxed{
 \theta(t)-\theta(79)>\frac t2
 \qquad(179\le t<10000).
 }
 \tag{L-91353.10}
\]

For `t>=10000`, put `n=floor(t/2)`.  The central binomial coefficient divides the least-common-multiple prime-power budget, hence

\[
 \psi(t)
 \ge\log\binom{2n}{n}
 \ge2n\log2-\log(2n+1)
 \ge(t-2)\log2-\log(t+1).
 \tag{L-91353.11}
\]

Also

\[
 \psi(t)-\theta(t)
 =\sum_{m=2}^{\lfloor\log_2t\rfloor}\theta(t^{1/m})
 \le\frac12\sqrt t\log t
 +\frac{t^{1/3}(\log t)^2}{3\log2}.
 \tag{L-91353.12}
\]

After division by `t`, every adverse term in (L-91353.11)--(L-91353.12) decreases for `t>=10000`.  The exact rational logarithm enclosures retained by the checker give at the left endpoint

\[
 \frac{\theta(t)-\theta(79)}t
 >
 \frac{27503}{50000}
 >\frac12.
 \tag{L-91353.13}
\]

Together, (L-91353.10) and (L-91353.13) prove

\[
 \boxed{
 \theta(t)-\theta(79)>\frac t2
 \qquad(t\ge179).
 }
 \tag{L-91353.14}
\]

No prime number theorem is imported.

## 5. Analytic tail for the component entropy

For a prime `q>79`, the positive coefficient formula of `L-91352` gives

\[
 \lambda_P(q)=\log q.
\]

Hence `mathcal E_P(x)` dominates its prime subsource.  With

\[
 f_x(t)=t^{-1/2}\log(x/t),
\]

Stieltjes summation and (L-91353.14) give, for `x>=10000`,

\[
\begin{aligned}
 \mathcal E_P(x)
 &\ge-\int_{179}^{x}
  [\theta(t)-\theta(79)]f_x'(t)\,dt\\
 &>2\sqrt x
 -\frac{\sqrt{179}}2\log\frac{x}{179}
 -2\sqrt{179}.
\end{aligned}
\tag{L-91353.15}

By (L-91353.4)--(L-91353.5), for `a<=5`,

\[
 W_{a,P}(x)<\sqrt x+\frac92.
 \tag{L-91353.16}
\]

Therefore

\[
 F_a(x)
 >\sqrt x
 -\frac{\sqrt{179}}2\log\frac{x}{179}
 -2\sqrt{179}-\frac92.
 \tag{L-91353.17}
\]

The right side is increasing for `x>=10000`.  Since

\[
 \sqrt{179}<14,
 \qquad
 \frac{10000}{179}<56,
 \qquad
 \log56<\frac{403}{100},
\]

its value at `10,000` is larger than

\[
 100-7\frac{403}{100}-28-\frac92
 =\frac{3929}{100}>18.
 \tag{L-91353.18}
\]

Combining Sections 3 and 5 yields the global bound

\[
 \boxed{
 F_4(x)>18,
 \qquad
 F_5(x)>18
 \qquad(x\ge83).
 }
 \tag{L-91353.19}
\]

## 6. Compact child upper bound

Because every coefficient `lambda_P(n)` is nonnegative, `mathcal E_P(x)` is increasing.  The directed finite evaluation gives

\[
 \mathcal E_P(83)<21.
 \tag{L-91353.20}
\]

For `1<=y<83`, equations (L-91353.5) and `sqrt(y)<10` give

\[
 |W_{a,P}(y)|<5\cdot10+\frac92.
\]

Consequently

\[
 \boxed{
 F_a(y)<76
 \qquad(1\le y<83,\ a\in\{4,5\}).
 }
 \tag{L-91353.21}
\]

## 7. Uniform one-prime physical-score surplus

Let `p>=83`, `r=p^-1/2`, and `1<=y<83`.  By exact linearity,

\[
\begin{aligned}
 &\mathcal E_P(py)-r\mathcal E_P(y)
 -\big[W_{a,P}(py)-rW_{a,P}(y)\big]\\
 &\qquad=F_a(py)-rF_a(y).
\end{aligned}
\tag{L-91353.22}

Since `r<1/9`, (L-91353.19) and (L-91353.21) imply

\[
 \boxed{
 F_a(py)-rF_a(y)
 >18-\frac{76}{9}
 =\frac{86}{9}>0.
 }
 \tag{L-91353.23}
\]

Thus the literal entropy of the direct Euler residual dominates both ledgers uniformly:

\[
 \boxed{
 \mathcal E_{P;p}(py)
 >\mathfrak T_{P;p}(py)+\frac{86}{9},
 }
 \tag{L-91353.24}
\]

\[
 \boxed{
 \mathcal E_{P;p}(py)
 >\mathfrak S_{P;p}(py)+\frac{86}{9}.
 }
 \tag{L-91353.25}
\]

This replaces the false scalar surplus of `R-91310` by a stronger true statement about the actual row entropy.

## 8. Exact remaining interface

The present theorem is a raw-row entropy theorem.  `T-91304` separates inherited rows from noninherited current-generation frontier rows and then applies finite endpoint conversion, collar assembly and one quantization.

To turn (L-91353.24) into the loss recurrence, one must still prove that this source-bound finite-frontier assembly retains the literal entropy in (L-91353.2), or loses at most one absolute bounded amount after all least-prime branches have been summed.  It is not enough to cite positivity of the raw row or the declared source score.

The corrected first open theorem is therefore:

> **Finite-frontier entropy preservation.**  Under the exact decomposition used by `T-91304`, the one-use current-generation packing represents at least the literal residual entropy `mathcal E_(P;p)(py)` minus an absolute homogeneous debt, with no branchwise duplication.

```text
literal residual entropy > target                  PROVED UNIFORMLY
literal residual entropy > declared score          PROVED UNIFORMLY
false scalar source surplus                         NOT USED
finite-frontier/collar entropy preservation         OPEN / RH-BEARING
one-use homogeneous debt accounting                 OPEN / RH-BEARING
corrected T-91304 recurrence                        OPEN
Riemann Hypothesis                                  UNPROVEN
```
