# L-91348 — The `P_61` one-prime Euler row has a uniform literal entropy surplus

Claim ID: `L-91348`  
Status: **PROVED EXACT/DIRECTED LITERAL-ENTROPY THEOREM — FULL PHYSICAL ROW TYPING REMAINS SEPARATE**  
Created: 2026-08-13  
Frozen parent: PR #432 at `5831eae7081ad71a4cc44f45a911426c3d4fcbf6`  
Depends on: `R-91552`, `L-91342`, `L-91345`, `L-91347`; companion replay `X-91127`  
RH status: **unproved**

## 1. Exact component entropy and finite Euler transform

For real `Y>=1`, let

\[
 \mathcal E(Y)
 =\sum_{2\le q\le Y}
   \frac{\log q}{\sqrt q}\log\frac Yq
 \tag{L-91348.1}
\]

be the literal average-binomial entropy of the positive component row `Q_Y`, as
proved in `R-91552/L-91553`.

Put

\[
 P=P_{61}=\prod_{q\le61}q
\]

and define the signed finite-Euler entropy

\[
 \boxed{
 \mathcal E_P(X)
 =\sum_{\substack{d\mid P\\d\le X}}
   \frac{\mu(d)}{\sqrt d}\mathcal E(X/d).
 }
 \tag{L-91348.2}
\]

By linearity this is exactly the literal entropy of the signed finite-Euler
component row, whether or not one has yet supplied a positive physical typing
of every row coordinate.

## 2. Sieve collapse to a nonnegative arithmetic density

Define

\[
 \boxed{
 \lambda_P(n)
 =\sum_{d\mid(n,P)}\mu(d)\log\frac nd.
 }
 \tag{L-91348.3}
\]

Writing `n=dq` and exchanging finite sums in (L-91348.2) gives

\[
\boxed{
 \mathcal E_P(X)
 =\sum_{n\le X}
   \frac{\lambda_P(n)}{\sqrt n}
   \log\frac Xn.
}
\tag{L-91348.4}
\]

The coefficient has an elementary closed form.  Let `omega_P(n)` be the number
of distinct primes dividing both `n` and `P`.  Then

\[
\boxed{
 \lambda_P(n)=
 \begin{cases}
  \log n,&\omega_P(n)=0,\\
  \log q,&(n,P)\text{ has the single prime divisor }q,\\
  0,&\omega_P(n)\ge2.
 \end{cases}}
\tag{L-91348.5}
\]

Indeed, when at least two small primes occur, both
`sum_(d|g)mu(d)` and `sum_(d|g)mu(d)log d` vanish.  Consequently

\[
 \boxed{\lambda_P(n)\ge0.}
 \tag{L-91348.6}
\]

In particular `mathcal E_P` is continuous and nondecreasing, and on every open
integer cell

\[
 \boxed{
 \partial_{\log X}\mathcal E_P(X)
 =L_P(X)
 :=\sum_{n\le X}\frac{\lambda_P(n)}{\sqrt n}.
 }
 \tag{L-91348.7}

This is the positive arithmetic density hidden behind the signed Euler row.

## 3. Declared `P_61` score

Let

\[
 a_0(X)=\sum_{\substack{d\mid P\\d\le X}}\frac{\mu(d)}d,
 \qquad
 b_0(X)=\sum_{\substack{d\mid P\\d\le X}}\frac{\mu(d)}{\sqrt d}.
 \tag{L-91348.8}
\]

The declared endpoint score of the finite block is

\[
 \boxed{
 \mathcal S_P(X)
 =\sum_{\substack{d\mid P\\d\le X}}
  \mu(d)\left(\frac{5\sqrt X}{d}-\frac3{\sqrt d}\right)
 =5\sqrt X\,a_0(X)-3b_0(X).
 }
 \tag{L-91348.9}

For a new rough prime `p>=67`, put `r=p^(-1/2)` and `X=py`, where
`1<=y<67`.  The exact one-prime entropy and declared score are

\[
 \boxed{
 \mathcal E_{P;p}(py)
 =\mathcal E_P(py)-r\mathcal E_P(y),
 }
 \tag{L-91348.10}
\]

\[
 \boxed{
 \mathcal S_{P;p}(py)
 =\mathcal S_P(py)-r\mathcal S_P(y)
 =3F_{5/3;p}^{(61)}(py).
 }
 \tag{L-91348.11}

Thus (L-91348.11) is exactly the score packet of `L-91345`, but
(L-91348.10) is its **literal finite-row entropy**, not the refuted affine
source-score identification.

## 4. A universal half-unit summation estimate

Put

\[
 A(t)=\sum_{2\le n\le t}\frac{\log n}{\sqrt n},
 \qquad
 F_0(t)=2\sqrt t(\log t-2)+4.
 \tag{L-91348.12}
\]

Then

\[
 \boxed{|A(t)-F_0(t)|<\frac12\qquad(t\ge1).}
 \tag{L-91348.13}
\]

For `1<=t<9` this is a directed finite check.  For `t in [N,N+1)` with
`N>=8`, the function `f(t)=log(t)/sqrt(t)` is decreasing.  The left endpoint
errors

\[
 e_N=A(N)-F_0(N)
\]

decrease because

\[
 e_{N+1}-e_N
 =f(N+1)-\int_N^{N+1}f(u)du\le0,
\]

whereas the right-limit errors

\[
 r_N=A(N)-F_0(N+1)
\]

increase because

\[
 r_{N+1}-r_N
 =f(N+1)-\int_{N+1}^{N+2}f(u)du\ge0.
\]

The directed base values satisfy `e_8<1/2` and `r_8>-1/2`, proving
(L-91348.13).

## 5. Uniform positivity of the score derivative gap

Define

\[
 a_1(X)=\sum_{\substack{d\mid P\\d\le X}}
         \frac{\mu(d)\log d}{d}.
 \tag{L-91348.14}
\]

Substituting (L-91348.13) into the divisor expansion of `L_P` gives

\[
\boxed{
 L_P(X)
 =2\sqrt X\big[(\log X-2)a_0(X)-a_1(X)\big]
  +4b_0(X)+\varepsilon_X,
}
\tag{L-91348.15}
\]

with

\[
 \boxed{
 |\varepsilon_X|
 <\frac12
  \sum_{\substack{d\mid P\\d\le X}}\frac1{\sqrt d}.
 }
 \tag{L-91348.16}
\]

Let

\[
 \mathfrak B_P(X)
 =L_P(X)-\frac52\sqrt X\,a_0(X).
 \tag{L-91348.17}
\]

The directed merge of all `2^18` divisor states proves, for every `X>=67`,

\[
 a_0(X)>\frac1{61},
 \qquad
 a_1(X)<-\frac9{100},
 \qquad
 b_0(X)>-1,
 \tag{L-91348.18}
\]

and

\[
 \sum_{d\mid P}\frac1{\sqrt d}<60.
 \tag{L-91348.19}
\]

Therefore

\[
 \mathfrak B_P(X)
 >2\sqrt X\left[
   \frac{\log X-13/4}{61}+\frac9{100}
  \right]-34.
 \tag{L-91348.20}
\]

For `X>=15000`, use `sqrt(X)>122` and `log X>48/5`; the right side is at least

\[
 2\cdot122\left[
  \frac{48/5-13/4}{61}+\frac9{100}
 \right]-34
 =\frac{334}{25}>13.
 \tag{L-91348.21}
\]

The directed checker verifies every remaining arithmetic cell
`67<=X<15000` and obtains

\[
 \boxed{
 \mathfrak B_P(X)>13
 \qquad(X\ge67).
 }
 \tag{L-91348.22}

The least directed lower endpoint is greater than

\[
 13.2068410308
\]

on the cell whose left endpoint is `69`.

## 6. Global parent entropy surplus

Put

\[
 \mathcal D_P(X)=\mathcal E_P(X)-\mathcal S_P(X).
 \tag{L-91348.23}
\]

On every open cell,

\[
 \partial_{\log X}\mathcal D_P(X)=\mathfrak B_P(X).
 \tag{L-91348.24}
\]

At a divisor activation `d|P`, the entropy is continuous, while the score jumps
by `2mu(d)/sqrt(d)`.  Since `b_0` jumps by `mu(d)/sqrt(d)`, the combination

\[
 \mathcal D_P(X)+2b_0(X)
\]

is continuous.  Hence, globally for `X>=67`,

\[
 \mathcal D_P(X)+2b_0(X)
 =\mathcal D_P(67)+2b_0(67)
  +\int_{67}^{X}\mathfrak B_P(t)\frac{dt}{t}.
 \tag{L-91348.25}
\]

The directed certificate gives

\[
 \mathcal D_P(67)>15,
 \qquad
 b_0(67)>-\frac{14}{25},
 \qquad
 b_0(X)<\frac{27}{20}.
 \tag{L-91348.26}

Using (L-91348.22) only for positivity of the integral,

\[
\boxed{
 \mathcal D_P(X)
 >15-\frac{28}{25}-\frac{27}{10}
 =\frac{559}{50}
 \qquad(X\ge67).
}
\tag{L-91348.27}

## 7. Bounded terminal child

Equation (L-91348.6) makes `mathcal E_P` nondecreasing, and the directed base
certificate gives

\[
 \mathcal E_P(67)<18.
 \tag{L-91348.28}
\]

The terminal `P_61` theorem inherited from `L-91342` gives

\[
 \mathcal S_P(y)>0
 \qquad(1\le y<67).
 \tag{L-91348.29}
\]

Therefore

\[
 \boxed{
 \mathcal D_P(y)<18
 \qquad(1\le y<67).
 }
 \tag{L-91348.30}

## 8. Uniform literal one-prime score surplus

By (L-91348.10)--(L-91348.11),

\[
 \mathcal E_{P;p}(py)-\mathcal S_{P;p}(py)
 =\mathcal D_P(py)-p^{-1/2}\mathcal D_P(y).
 \tag{L-91348.31}
\]

Since `p>=67` gives `p^(-1/2)<1/8`, equations
(L-91348.27) and (L-91348.30) yield

\[
\boxed{
 \mathcal E_{P;p}(py)-\mathcal S_{P;p}(py)
 >\frac{559}{50}-\frac{18}{8}
 =\frac{893}{100}>0
}
\tag{L-91348.32}
\]

for every

\[
 \boxed{
 p\ge67,\qquad1\le y<67.
 }
\]

Thus the exact one-prime `P_61` Euler row carries at least `8.93` units of
**literal average-binomial entropy surplus** over its declared endpoint score.
No target-normalized debt estimate and no affine source-score identification is
used.

## 9. Consequence and exact boundary

Together with the resident scalar theorem `L-91345` and the inherited-row
positivity theorem `L-91347`, the preferred one-prime packet now has:

```text
SHARP target                              strictly positive;
declared endpoint score                   strictly positive;
literal finite-Euler row entropy           > declared score + 8.93;
every inherited exact row                 strictly positive.
```

This removes the literal score interface from the remaining `P_61` splice.
What is not yet proved is coefficientwise positivity/physical realization of
the complete current-generation row outside the inherited sector, together
with one-use ordinary/radix-four capacity accounting.  The entropy theorem does
not infer those geometric facts from a scalar score.

```text
sieved entropy density lambda_P                    EXACT / NONNEGATIVE
finite-Euler literal entropy formula               EXACT
uniform derivative gap B_P>13                      DIRECTED + ANALYTIC
parent entropy-score gap >559/50                   EXACT
one-prime literal entropy surplus >893/100         EXACT
inherited-row positivity                           L-91347
complete current-row positivity                    OPEN
ordinary/radix-four one-use physical realization  OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
