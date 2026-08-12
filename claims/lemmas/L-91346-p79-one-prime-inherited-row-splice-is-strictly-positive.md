# L-91346 — The `P_79` one-prime inherited-row splice is strictly positive

Claim ID: `L-91346`  
Status: **PROPOSED COMPLETE EXACT/DIRECTED ROW THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91344`, `L-91345`; directed replay `X-91125`  
RH status: **unproved**

## 1. Statement

Let

\[
 P_{79}=\prod_{q\le79}q,
\]

and, for real `z`, use causal zero extension below one and put

\[
 \mathcal G(z)
 =\sum_{\substack{d\mid P_{79}\\d\le z}}
  \frac{\mu(d)}{\sqrt d}\log\frac zd,
\tag{L-91346.1}
\]

\[
 \mathcal R(x)
 =\sum_{\substack{k\le x\\(k,P_{79})=1}}
  \frac1{\sqrt k}\log\frac xk.
\tag{L-91346.2}
\]

For a prime `p>=83`, write `r=p^-1/2` and define

\[
 F_p(z)=\mathcal G(pz)-r\mathcal G(z),
\tag{L-91346.3}
\]

\[
 D_p(y)=\mathcal R(py)-r\mathcal R(y).
\tag{L-91346.4}
\]

The exact Green decomposition of `L-91344` gives, for every inherited row

\[
 2\le j\le y<83,
\]

the one-prime splice

\[
\boxed{
\begin{aligned}
 \mathscr R_{p,y}(j)={}&
 \frac2{j(j-1)}D_p(y)\\
 &-\frac2{j(j-1)}
  \sum_{m=1}^{j-1}\frac1{\sqrt m}F_p(y/m)\\
 &+\frac{j+2}{j\sqrt j}F_p(y/j)
 -\frac1{\sqrt{j+1}}F_p(y/(j+1)).
\end{aligned}}
\tag{L-91346.5}
\]

Then

\[
\boxed{
 \mathscr R_{p,y}(j)>0
 \qquad
 (p\ge83\text{ prime},\ 2\le j\le y<83).
}
\tag{L-91346.6}
\]

More explicitly, the proof gives

\[
 \boxed{
 j^{3/2}\mathscr R_{83,y}(j)
 >\frac{38381}{90000},
 }
\tag{L-91346.7}
\]

and, for every prime `p>=89`,

\[
 \boxed{
 j^{3/2}\mathscr R_{p,y}(j)
 >\frac{18779}{1417500}.
 }
\tag{L-91346.8}
\]

Thus the inherited-row part of the `P_79` one-prime arithmetic splice is
closed with a fixed positive margin.

## 2. A finite boundary-functional lemma

Multiply the boundary part of (L-91346.5) by `j^(3/2)`. It becomes

\[
 \mathfrak B_j[f]
 =\sum_{m=1}^{j+1}w_{j,m}f(y/m),
\tag{L-91346.9}
\]

with

\[
 w_{j,m}=-\frac{2\sqrt j}{(j-1)\sqrt m}
 \quad(1\le m<j),
\tag{L-91346.10}
\]

\[
 w_{j,j}=j+2,
 \qquad
 w_{j,j+1}=-\frac{j^{3/2}}{\sqrt{j+1}}.
\tag{L-91346.11}
\]

Let

\[
 S_j=\sum_{m=1}^{j+1}w_{j,m}.
\]

For one support point `a_j`, subtract `S_j delta_(log a_j)` from the signed
measure

\[
 \sum_mw_{j,m}\delta_{\log m}.
\]

The result has total mass zero. Its one-dimensional Kantorovich--Rubinstein norm
is the integral of the absolute cumulative signed mass.

The directed finite replay chooses

\[
 a_j=
 \begin{cases}
 1,&2\le j\le18,\\
 2,&19\le j\le39,\\
 3,&40\le j\le62,\\
 4,&63\le j\le82,
 \end{cases}
\]

and proves

\[
 \boxed{|S_j|<\frac{61}{50}}
\tag{L-91346.12}
\]

and

\[
 \boxed{
 \left\|
  \sum_mw_{j,m}\delta_{\log m}
  -S_j\delta_{\log a_j}
 \right\|_{KR}
 <\frac{387}{100}
 }
\tag{L-91346.13}
\]

for every `2<=j<=82`.

Consequently, if `f` is bounded by `M` and is `L`-Lipschitz as a function of
`log z`, then

\[
\boxed{
 |\mathfrak B_j[f]|
 <\frac{61}{50}M+\frac{387}{100}L.
}
\tag{L-91346.14}
\]

The maxima in the replay occur at `j=82`; the directed upper endpoints are
approximately

\[
 1.2150313677,
 \qquad
 3.8653634563.
\]

## 3. The compact prime `p=83`

The activation points of `F_83` on

\[
 \frac23\le z\le83
\]

are exactly the rational points `d/83` and `d` coming from divisors of `P_79`.
Between adjacent activation points, `F_83` is affine in `log z`. Its logarithmic
derivative is the corresponding difference of two finite prefix sums.

The directed certificate checks every activation endpoint and proves

\[
 \boxed{
 |F_{83}(z)|<\frac{141}{100},
 \qquad
 \operatorname{Lip}_{\log}F_{83}<\frac{147}{100}.
 }
\tag{L-91346.15}

For the Green bulk it proves

\[
 \boxed{
 D_{83}(y)>\frac{387}{100}\sqrt y
 \qquad(1\le y<83).
 }
\tag{L-91346.16}

To justify the finite endpoint reduction in (L-91346.16), observe that on one
activation cell

\[
 D_{83}(y)=A\log y+B
\]

with `A>0`. Therefore

\[
 \frac{D_{83}(y)}{\sqrt y}
 =e^{-u/2}(Au+B),
 \qquad u=\log y,
\]

has at most one interior critical point, and that point is a maximum. Its cell
minimum is attained at an endpoint.

Now `y>=j`, so the normalized positive bulk satisfies

\[
\begin{aligned}
 j^{3/2}\frac2{j(j-1)}D_{83}(y)
 &=\frac{2\sqrt j}{j-1}D_{83}(y)\\
 &>\frac{774}{100}\frac{j}{j-1}\\
 &\ge\frac{774}{100}\frac{82}{81}.
\end{aligned}
\tag{L-91346.17}
\]

Equations (L-91346.14)--(L-91346.15) bound the adverse boundary by

\[
 \frac{61}{50}\frac{141}{100}
 +\frac{387}{100}\frac{147}{100}.
\]

The exact difference is

\[
 \frac{774}{100}\frac{82}{81}
 -\frac{61}{50}\frac{141}{100}
 -\frac{387}{100}\frac{147}{100}
 =\boxed{\frac{38381}{90000}}>0.
\tag{L-91346.18}
\]

This proves (L-91346.7).

## 4. Global finite-block corridors

Put

\[
 \beta_{79}
 =\prod_{q\le79}(1-q^{-1/2}),
\]

and

\[
 M(z)=\sum_{\substack{d\mid P_{79}\\d\le z}}
       \frac{\mu(d)}{\sqrt d}.
\tag{L-91346.19}
\]

For `z>=1`, define the centered activation spline

\[
 E(z)=\mathcal G(z)-\beta_{79}\log z.
\tag{L-91346.20}
\]

A directed scan of all

\[
 2^{22}=4,194,304
\]

activation states proves

\[
 \boxed{
 0<\beta_{79}<\frac1{700},
 \qquad
 |M(z)|<\frac{36}{25},
 \qquad
 |E(z)|<\frac{269}{200}.
 }
\tag{L-91346.21}
\]

The observed directed maxima are approximately

\[
 \max|M|=1.4292396712,
 \qquad
 \max|E|=1.3350166017.
\]

These are finite statements about the fixed Boolean block, not estimates on an
unbounded Möbius sum.

## 5. Uniform spline bounds for every `p>=89`

Let `p>=89`, `r=p^-1/2`, and `2/3<=z<=83`. Since

\[
 r<\frac8{75},
\tag{L-91346.22}
\]

(L-91346.21) gives

\[
 \boxed{
 |F_p(z)|
 <\frac32+\frac{\log p}{700}.
 }
\tag{L-91346.23}

Indeed, for `z>=1`,

\[
 F_p(z)
 =\beta_{79}[\log p+(1-r)\log z]
  +E(pz)-rE(z),
\]

and

\[
 \left(1+\frac8{75}\right)\frac{269}{200}
 +\frac{\log83}{700}
 <\frac32,
\]

where `log 83<9/2` is sufficient. For `z<1`, the `rE(z)` term is absent and the
same bound is easier.

The logarithmic derivative is either `M(pz)` or `M(pz)-rM(z)`, according as
`z<1` or `z>=1`. Hence

\[
 \boxed{
 \operatorname{Lip}_{\log}F_p<\frac85.
 }
\tag{L-91346.24}

## 6. Uniform Green-bulk bounds for every `p>=89`

The function

\[
 D_p(y)=\mathcal R(py)-p^{-1/2}\mathcal R(y)
\]

is increasing in `p`: the first term increases with its endpoint and the
coefficient subtracted from the nonnegative second term decreases.

The directed activation-cell certificate at `p=89` proves

\[
 \boxed{
 D_{89}(y)>4\sqrt y
 \qquad(1\le y<83).
 }
\tag{L-91346.25}

Thus (L-91346.25) holds for every `p>=89`.

There is also the elementary lower bound

\[
 \boxed{D_p(y)\ge\log p.}
\tag{L-91346.26}

The `k=1` summand contributes

\[
 \log p+(1-p^{-1/2})\log y\ge\log p,
\]

and every remaining paired or newly activated rough-lattice summand is
nonnegative.

It follows that the normalized positive bulk is at least

\[
 \boxed{
 \max\left(
  \frac{656}{81},
  \frac29\log p
 \right).
 }
\tag{L-91346.27}

The first term uses `j<=82`; the second uses

\[
 \frac{\sqrt j}{j-1}>\frac19
 \qquad(2\le j\le82).
\]

## 7. Bulk dominates the boundary for every `p>=89`

Equations (L-91346.14), (L-91346.23), and (L-91346.24) give

\[
\begin{aligned}
 j^{3/2}|\text{boundary}|
 &<\frac{61}{50}
   \left(\frac32+\frac{\log p}{700}\right)
   +\frac{387}{100}\frac85\\
 &=\frac{4011}{500}
   +\frac{61}{35000}\log p.
\end{aligned}
\tag{L-91346.28}
\]

The two bulk bounds in (L-91346.27) meet at

\[
 \log p=\frac{328}{9}.
\]

At that crossing the exact margin is

\[
\begin{aligned}
 \frac{656}{81}
 -\frac{4011}{500}
 -\frac{61}{35000}\frac{328}{9}
 =\boxed{\frac{18779}{1417500}}>0.
\end{aligned}
\tag{L-91346.29}

Below the crossing, the fixed bulk bound applies and the adverse boundary is
increasing in `log p`. Above it, the logarithmic bulk applies and its slope

\[
 \frac29
\]

is strictly larger than

\[
 \frac{61}{35000}.
\]

Therefore (L-91346.29) is the global minimum of the analytic comparison. This
proves (L-91346.8), and hence the theorem.

## 8. Consequence for the factor-54 route

The open `P_79` one-prime splice had three logically distinct parts:

```text
scalar SHARP-target sign;
scalar endpoint-score sign and surplus;
all inherited exact finite-row signs.
```

`L-91345` closes the large-prefix target Hall theorem and isolates a bounded
low-prefix correction. The present theorem closes the complete inherited-row
sign for every rough prime, with no finite search over `p`.

The first remaining gate is therefore purely the bounded low-prefix target
transport from `L-91345`:

> for the finitely many thresholds `t<4096`, realize the certified
> displacement-eight Hall matching by positive endpoint/interval packets while
> retaining target exactness and score superordination.

The row packet itself can no longer furnish a counterexample.

## 9. Verification

Replay:

```bash
python3 experiments/X-91125-p79-one-prime-row-splice/verify.py
```

Retained verdict:

```text
PASS_P79_ONE_PRIME_ROW_SPLICE
```

The checker uses exact integer square-root enclosures, fixed-denominator directed
interval arithmetic, correctly rounded standard-library decimal logarithms with
thirty guard digits and an additional outward enlargement, and exact rational
comparison of the final margins.

## 10. Proof boundary

```text
finite boundary-functional geometry              DIRECTED EXACT
p=83 compact spline/Lipschitz/bulk gates          DIRECTED EXACT
global P_79 beta/prefix/centered-spline corridors DIRECTED EXACT
p=89 bulk gate and p-monotonicity                 EXACT/DIRECTED
all p>=83 inherited-row positivity               PROPOSED COMPLETE
large-prefix one-prime Hall transport             AVAILABLE / L-91345
bounded low-prefix upward correction              OPEN / FINITE
Riemann Hypothesis                                UNPROVEN
```
