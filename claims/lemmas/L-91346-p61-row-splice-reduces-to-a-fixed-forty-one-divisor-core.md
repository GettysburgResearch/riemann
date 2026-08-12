# L-91346 — The `P_61` one-prime row splice reduces to a fixed forty-one-divisor core

Claim ID: `L-91346`  
Status: **PROVED EXACT GLOBAL PROFILE / FINITE-CORE REDUCTION — CORE SIGN OPEN**  
Created: 2026-08-12  
Depends on: `L-91344`, `L-91345`  
RH status: **unproved**

## 1. Global component profile

Retain the positive component row

\[
 Q_Y(j)=A_j\ell_Y(j)+B_j\ell_Y(j+1)
       +C_j\sum_{m\ge j+2}\ell_Y(m),
\tag{L-91346.1}
\]

where

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=-\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\tag{L-91346.2}
\]

Put

\[
 \boxed{
 q_j(Y)=\frac{Q_Y(j)}{\sqrt Y},
 }
\tag{L-91346.3}
\]

with `q_j(Y)=0` for `Y<j`.

### Theorem 1.1

For every

\[
 2\le j\le66,
\]

the function `q_j` is continuous and strictly increasing on `[j,infinity)`.

## 2. Proof of global monotonicity

On one activation cell

\[
 N\le Y<N+1,
\]

write

\[
 Q_Y(j)=\Gamma_{j,N}\log Y-D_{j,N},
\qquad
 \Gamma_{j,N}>0.
\tag{L-91346.4}
\]

Direct differentiation gives

\[
 \boxed{
 q_j'(Y)
 =\frac{2\Gamma_{j,N}-Q_Y(j)}{2Y^{3/2}}.
 }
\tag{L-91346.5}
\]

It remains to prove

\[
 E_j(Y):=2\Gamma_{j,N}-Q_Y(j)>0.
\tag{L-91346.6}
\]

The first cell `j<=Y<j+1` is immediate, because only the positive `j` atom is
active and `log((j+1)/j)<2`.

For the next cell put

\[
 \alpha_j=\frac{A_j}{\sqrt j}+\frac{B_j}{\sqrt{j+1}},
 \qquad
 \beta_j=\frac{A_j\log j}{\sqrt j}
          +\frac{B_j\log(j+1)}{\sqrt{j+1}}.
\tag{L-91346.7}
\]

Then on `j+1<=Y<j+2`,

\[
 E_j(Y)=\alpha_j(2-\log Y)+\beta_j.
\]

This decreases on the cell.  The directed companion checker proves

\[
 \boxed{
 E_j((j+2)^-)>\frac7{1000}
 \qquad(2\le j\le66).
 }
\tag{L-91346.8}
\]

Now suppose `N>=j+2`.  The function

\[
 t\longmapsto t^{-1/2}\left[2-\log(Y/t)\right]
\]

is increasing on `1<=t<=Y`, because its derivative is

\[
 \frac{\log(Y/t)}{2t^{3/2}}\ge0.
\]

Therefore

\[
\begin{aligned}
 \sum_{m=j+2}^{N}\frac{2-\log(Y/m)}{\sqrt m}
 &\ge
 \int_{j+1}^{N}t^{-1/2}[2-\log(Y/t)]\,dt\\
 &=2\sqrt N\log(N/Y)
   -2\sqrt{j+1}\log((j+1)/Y).
\end{aligned}
\tag{L-91346.9}

Define

\[
 \kappa_j=2C_j\sqrt{j+1}-\alpha_j.
\tag{L-91346.10}
\]

An exact simplification gives

\[
 \boxed{
 \kappa_j
 =\frac{(j+1)[j+2-\sqrt{j(j+1)}]}
 {j(j-1)\sqrt{j+1}}>0.
 }
\tag{L-91346.11}
\]

Using `Y<N+1` in (L-91346.9) yields

\[
 E_j(Y)\ge \mathcal L_j(N),
\tag{L-91346.12}
\]

where

\[
\boxed{
\begin{aligned}
 \mathcal L_j(N)={}&2\alpha_j+\beta_j
 +\kappa_j\log(N+1)\\
 &-2C_j\sqrt{j+1}\log(j+1)
 +2C_j\sqrt N\log\frac N{N+1}.
\end{aligned}}
\tag{L-91346.13}
\]

The function

\[
 N\longmapsto \sqrt N\log\frac N{N+1}
\]

is increasing for `N>1`, since

\[
 \frac d{dN}
 \left(\sqrt N\log\frac N{N+1}\right)
 >-\frac1{2N^{3/2}}+rac1{\sqrt N(N+1)}
 =\frac{N-1}{2N^{3/2}(N+1)}>0.
\tag{L-91346.14}
\]

Together with `kappa_j>0`, this proves that `mathcal L_j(N)` is increasing in
`N`.  The checker proves

\[
 \boxed{
 \mathcal L_j(j+2)>\frac7{1000}
 \qquad(2\le j\le66).
 }
\tag{L-91346.15}

Equations (L-91346.5)--(L-91346.15) prove Theorem 1.1 on the entire unbounded
half-line.  This removes the previous factor-54-window restriction for the
profile `Q_Y(j)/sqrt(Y)` in precisely the inherited row range needed below.

## 3. Rewrite the one-prime row in `1/d` coordinates

Let

\[
 P'=P_{61}p,
 \qquad p\ge67\text{ prime},
 \qquad x=py,
 \qquad j\le y<67.
\]

The exact splice is

\[
 \mathscr R^{61}_{p,y}(j)
 =\mathcal Q_{P',x}(j).
\tag{L-91346.16}
\]

Using (L-91346.3),

\[
\boxed{
 \frac{\mathscr R^{61}_{p,y}(j)}{\sqrt x}
 =\sum_{\substack{d\mid P'\\d\le x/j}}
   \frac{\mu(d)}d\,q_j(x/d).
 }
\tag{L-91346.17}
\]

Since `x/j>=p>=67`, the active divisor list always reaches the uniform positive
prefix region.

## 4. Uniform positive divisor prefixes from `67` onward

For real `t>=1`, put

\[
 A_{P'}(t)
 =\sum_{\substack{d\mid P'\\d\le t}}\frac{\mu(d)}d.
\tag{L-91346.18}
\]

Retain from `L-91345` the exact constants

\[
 m_{61}
 =\frac{55036345385124606673}{3351096610268770599522},
\]

and

\[
 \boxed{
 \delta_{61}
 =m_{61}-\frac1{67}
 =\frac{336338530534578047569}
 {224523472888007630167974}>0.
 }
\tag{L-91346.19}
\]

If `67<=t<p`, then

\[
 A_{P'}(t)=A_{61}(t)\ge m_{61}>\delta_{61}.
\]

If `t>=p`, then

\[
 A_{P'}(t)
 =A_{61}(t)-\frac1pA_{61}(t/p)
 \ge m_{61}-\frac1{67}
 =\delta_{61},
\]

because `A_61<=1`.  Hence

\[
 \boxed{
 A_{P'}(t)\ge\delta_{61}
 \qquad(t\ge67).
 }
\tag{L-91346.20}
\]

The exact prefix at `66` is also larger than `delta_61`.

## 5. Forty-one-divisor Abel reduction

Let

\[
 1=d_1<d_2<\cdots<d_{41}=66
\tag{L-91346.21}
\]

be all divisors of `P_61` below `67`, and put

\[
 B_i=\sum_{r=1}^{i}\frac{\mu(d_r)}{d_r}.
\tag{L-91346.22}
\]

Sort all active divisors of `P'` as `e_1<...<e_M`.  The first forty-one are
exactly the `d_i`.  Set

\[
 f_i=q_j(x/e_i).
\]

By Theorem 1.1, `f_i` is nonincreasing.  Abel summation gives

\[
 \sum_{i=1}^{M}\frac{\mu(e_i)}{e_i}f_i
 =A_{P'}(e_M)f_M
  +\sum_{i=1}^{M-1}A_{P'}(e_i)(f_i-f_{i+1}).
\tag{L-91346.23}
\]

Every prefix from `e_41=66` onward is at least `delta_61`.  Therefore the whole
unbounded tail satisfies

\[
 A_{P'}(e_M)f_M
 +\sum_{i=41}^{M-1}A_{P'}(e_i)(f_i-f_{i+1})
 \ge\delta_{61}f_{41}.
\tag{L-91346.24}
\]

Combining (L-91346.17), (L-91346.23) and (L-91346.24) yields the exact global
lower bound

\[
\boxed{
 \frac{\mathscr R^{61}_{p,y}(j)}{\sqrt{py}}
 \ge \mathcal C_j(py),
 }
\tag{L-91346.25}
\]

where the fixed core is

\[
\boxed{
 \mathcal C_j(X)
 =\sum_{i=1}^{40}B_i
   \left[q_j(X/d_i)-q_j(X/d_{i+1})\right]
  +\delta_{61}q_j(X/66).
 }
\tag{L-91346.26}
\]

The right side contains no prime parameter, no large divisor of `P_61`, and no
rough-lattice tail.

## 6. Exact remaining theorem

The complete preferred row gate is reduced to only

\[
\boxed{
 \mathcal C_j(X)\ge0
 \qquad
 (2\le j\le66,\ X\ge67j).
 }
\tag{L-91346.27}
\]

Thus the prior infinite-parametric problem

```text
p>=67 prime;
1<=y<67;
2<=j<=y;
all P_61 divisors;
all rough-lattice activations
```

has collapsed to sixty-five explicit one-variable inequalities built from the
fixed forty-one divisors below `67`.

The limit is strictly positive:

\[
 \lim_{X\to\infty}\mathcal C_j(X)
 =4C_j\delta_{61}>0,
\tag{L-91346.28}
\]

because `q_j(Y)` tends to `4C_j`.  What remains is to exclude a finite-height
dip of one of the functions `mathcal C_j`.

## 7. Verification boundary

The companion checker authenticates:

```text
global q_j monotonicity constants for j=2,...,66;
the exact P_61 divisor-prefix corridor;
the exact value of delta_61;
the list of all forty-one divisors below 67;
the Abel-core coefficient dictionary.
```

It does not certify (L-91346.27).

```text
global profile q_j increasing                      PROVED
uniform P_61 p-prefix positivity from 67 onward    EXACT
infinite rough tail contribution                    NONNEGATIVE
P_61 one-prime row -> forty-one-divisor core        EXACT
forty-one-divisor core sign                         OPEN / EXPLICIT
ordinary/radix-four physical splice                 OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
