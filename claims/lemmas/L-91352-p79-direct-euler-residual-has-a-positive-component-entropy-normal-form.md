# L-91352 — The direct `P_79` Euler residual has an exact positive component-entropy normal form

Claim ID: `L-91352`  
Status: **PROVED EXACT POSITIVE ENTROPY IDENTITY — GLOBAL TARGET DOMINATION STILL OPEN**  
Created: 2026-08-13  
Frozen main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Depends on: the exact component entropy identity of `R-91552`; `L-91344`; `R-91310`; replay `X-91310`  
RH status: **unproved**

## 1. Literal component-row entropy

For `Y>=1`, the literal average-binomial entropy of the positive component row is

\[
 \mathcal E(Y)
 =\sum_{q=2}^{\lfloor Y\rfloor}
  \frac{\log q}{\sqrt q}\log\frac Yq.
 \tag{L-91352.1}
\]

For the finite Euler block `P=P_79`, define its linear Euler transform

\[
 \boxed{
 \mathcal E_P(x)
 =\sum_{\substack{d\mid P\\d\le x/2}}
  \frac{\mu(d)}{\sqrt d}\,\mathcal E(x/d).
 }
 \tag{L-91352.2}
\]

This is the literal entropy functional applied to the exact Euler component row `D_P(x)`.

## 2. Positive coefficient collapse

Interchange the finite divisor sum with the integer entropy sum and write `n=dq`.  Then

\[
 \boxed{
 \mathcal E_P(x)
 =\sum_{n\le x}
  \frac{\lambda_P(n)}{\sqrt n}\log\frac xn,
 }
 \tag{L-91352.3}
\]

where

\[
 \boxed{
 \lambda_P(n)
 =\sum_{d\mid(n,P)}\mu(d)\log\frac nd.
 }
 \tag{L-91352.4}
\]

Let

\[
 g=\operatorname{rad}(n,P)
 =\prod_{q\mid(n,P)}q.
\]

The coefficient has the exact classification

\[
 \boxed{
 \lambda_P(n)=
 \begin{cases}
  \log n,&g=1,\\
  \log q,&g=q\text{ is prime},\\
  0,&\omega(g)\ge2.
 \end{cases}
 }
 \tag{L-91352.5}
\]

Indeed,

\[
 \lambda_P(n)
 =\log n\sum_{d\mid g}\mu(d)
  -\sum_{d\mid g}\mu(d)\log d.
\]

For `g=1` this is `log n`; for `g=q` it is `log q`; and for at least two distinct prime factors both the product and its first logarithmic derivative vanish at the origin.  In particular,

\[
 \boxed{\lambda_P(n)\ge0\quad(n\ge1).}
 \tag{L-91352.6}
\]

Thus a signed Möbius Euler transform of the component entropy collapses to one coefficientwise positive arithmetic source.

## 3. Positive one-prime residual

Let `p>=83` be prime, `p` not divide `P`, put `r=p^{-1/2}`, and let `y>=1`.  Define

\[
 \mathcal E_{P;p}(py)
 =\mathcal E_P(py)-r\mathcal E_P(y).
 \tag{L-91352.7}
\]

Using (L-91352.3), split at `n=y`.  One obtains the exact identity

\[
\boxed{
\begin{aligned}
 \mathcal E_{P;p}(py)
 ={}&\sum_{n\le y}
 \frac{\lambda_P(n)}{\sqrt n}
 \left[
  \log p+(1-r)\log\frac yn
 \right]\\
 &+\sum_{y<n\le py}
 \frac{\lambda_P(n)}{\sqrt n}
 \log\frac{py}{n}.
\end{aligned}}
\tag{L-91352.8}
\]

Every summand is nonnegative.  Since `py>=83`, the `n=2` coefficient is active and `lambda_P(2)=log 2`; hence the residual is strictly positive:

\[
 \boxed{
 \mathcal E_{P;p}(py)>0
 \qquad(p\ge83,\ y\ge1).
 }
 \tag{L-91352.9}
\]

This positivity is exact and does not use a Hall transport, a source-score label, or cancellation between rows.

## 4. The first scalar counterexample is physically overpaid

At the counterexample of `R-91310`, namely `p=83` and `y=1`, (L-91352.8) gives

\[
 \mathcal E_{P;83}(83)
 \ge
 \frac{\log2}{\sqrt2}\log\frac{83}{2}.
 \tag{L-91352.10}
\]

The exact rational atanh truncations and square-root enclosures in `X-91310` prove

\[
 \frac{\log2}{\sqrt2}\log\frac{83}{2}
 >1.825,
 \tag{L-91352.11}
\]

whereas the complete residual target satisfies

\[
 \mathfrak T_{P;83}(83)<1.813.
 \tag{L-91352.12}
\]

Consequently

\[
 \boxed{
 \mathcal E_{P;83}(83)
 >\mathfrak T_{P;83}(83)
 >\mathfrak S_{P;83}(83).
 }
 \tag{L-91352.13}
\]

Thus the exact scalar failure in `R-91310` does not produce a physical entropy deficit at the same point.  It instead proves that the direct-row route must use its literal component entropy rather than the declared source score.

## 5. Corrected all-parameter target

Put

\[
 F_P(x)=\mathcal E_P(x)-\mathfrak S_P(x).
 \tag{L-91352.14}
\]

Then the exact physical-score discrepancy of one splice is

\[
 \boxed{
 \mathcal E_{P;p}(py)-\mathfrak S_{P;p}(py)
 =F_P(py)-p^{-1/2}F_P(y).
 }
 \tag{L-91352.15}
\]

Therefore either of the following would repair the score interface of `T-91304`:

1. the sharp physical domination
   \[
   \mathcal E_{P;p}(py)\ge\mathfrak T_{P;p}(py)
   \qquad(p\ge83,\ 1\le y<83);
   \tag{L-91352.16}
   \]
2. or a uniform bound on the positive deficit
   \[
   \sup_{p\ge83,\ 1\le y<83}
   [\mathfrak T_{P;p}(py)-\mathcal E_{P;p}(py)]_+<\infty,
   \tag{L-91352.17}
   \]
   together with exact one-use branch accounting.

Equation (L-91352.15) reduces the comparison to one scalar function `F_P` and a fixed compact child corridor.  Its logarithmic derivative away from activation points is

\[
 \frac{d}{d\log x}F_P(x)
 =C_P(x)-\frac52\sqrt x\,A_P(x),
 \tag{L-91352.18}
\]

where

\[
 C_P(x)=\sum_{n\le x}\frac{\lambda_P(n)}{\sqrt n}\ge0.
\]

The exact prefix scan in `X-91310` proves the useful global corridor

\[
 \boxed{
 A_P(x)<\frac15\qquad(x\ge83),
 }
 \tag{L-91352.19}
\]

with maximum at the activation `x=221`.  Hence a sufficient continuous-cell inequality is

\[
 C_P(x)>\frac12\sqrt x.
 \tag{L-91352.20}
\]

This has now become a positive counting problem for the explicit coefficients (L-91352.5), rather than a signed Möbius problem.  Activation jumps and the finite frontier must still be included before promoting a global recurrence.

## 6. Boundary

```text
literal component entropy formula                 EXACT
positive lambda_P coefficient classification       EXACT
positive one-prime entropy residual                EXACT
first-cell entropy exceeds target                  DIRECTED/EXACT
source score exceeds target on first cell          FALSE / R-91310
global physical target domination                  OPEN
finite-frontier score preservation                 OPEN / MUST BE SOURCE BOUND
corrected factor-54 recurrence                      OPEN
Riemann Hypothesis                                 UNPROVEN
```
