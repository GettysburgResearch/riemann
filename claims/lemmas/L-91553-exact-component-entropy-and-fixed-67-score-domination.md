# L-91553 — The exact component entropy dominates every fixed-67 inherited score difference

Claim ID: `L-91553`  
Status: **PROVED EXACT SCORE-REALIZATION REPAIR; NATIVE ROOT NORMALIZATION STILL REQUIRES AUDIT**  
Created: 2026-08-13  
Depends on: `L-24501`; `R-91552`; `L-91540/L-91547`; directed replay `X-91553`  
RH status: **unproved**

## 1. Exact row entropy

For the positive component row `Q_Y` define

\[
 \boxed{
 \mathcal E(Y)
 =\sum_{n\ge2}Q_Y(n)G_n
 =\sum_{q=2}^{\lfloor Y\rfloor}
   \frac{\log q}{\sqrt q}\log\frac Yq.
 }
 \tag{L-91553.1}
\]

The first equality is the literal entropy score; the second is
`R-91552.4`, obtained from `L-24501.4` by two exact summations.

The function is continuous on `[1,infinity)`: when `Y` crosses an integer `q`,
the entering term has factor `log(Y/q)=0`.

Put

\[
 A(Y)=\sum_{2\le q\le Y}\frac{\log q}{\sqrt q}.
 \tag{L-91553.2}
\]

On every open arithmetic cell,

\[
 \boxed{
 \partial_{\log Y}\mathcal E(Y)=A(Y).
 }
 \tag{L-91553.3}
\]

## 2. Large-parent score is already favorable

The directed base evaluation gives

\[
 \boxed{
 \mathcal E(67)-(5\sqrt{67}-3)
 >3.2764>0.
 }
 \tag{L-91553.4}
\]

For every integer `N>=67`, the function

\[
 f(t)=\frac{\log t}{\sqrt t}
\]

is decreasing on `[8,infinity)`, and hence

\[
\begin{aligned}
 A(N)
 &\ge\sum_{q=8}^{N}f(q)\\
 &\ge\int_8^{N+1}f(t)dt\\
 &=2\sqrt{N+1}[\log(N+1)-2]
   -2\sqrt8(\log8-2).
\end{aligned}
\tag{L-91553.5}
\]

For `N+1>=68`, use

\[
 \log(N+1)>4,
 \qquad
 \log8<3,
 \qquad
 \sqrt{N+1}>8
\]

to obtain

\[
 \boxed{
 A(N)>\frac52\sqrt{N+1}.
 }
 \tag{L-91553.6}
\]

Therefore `mathcal E(Y)-5sqrt(Y)+3` is increasing on every cell above `67`.
By continuity and (L-91553.4),

\[
 \boxed{
 \mathcal E(Y)>5\sqrt Y-3
 \qquad(Y\ge67).
 }
 \tag{L-91553.7}
\]

Thus the large parent component row has **more**, not less, literal entropy
than the native declared endpoint-score profile.

## 3. Fixed-67 difference theorem

Define

\[
 \mathcal D_{67}(Y)
 =\mathcal E(Y)-\mathcal E(Y/67)
  -5\left(\sqrt Y-\sqrt{Y/67}\right).
 \tag{L-91553.8}
\]

The directed base evaluation gives

\[
 \boxed{
 \mathcal D_{67}(67)>3.2764.
 }
 \tag{L-91553.9}
\]

On a cell `N<=Y<N+1`,

\[
 \partial_{\log Y}\mathcal D_{67}(Y)
 =A(N)-A(\lfloor N/67\rfloor)
 -\frac52\left(\sqrt Y-\sqrt{Y/67}\right).
 \tag{L-91553.10}
\]

This derivative decreases inside the cell.  The exact directed checker verifies
at every right endpoint for `67<=N<536` that

\[
 \boxed{
 A(N)-A(\lfloor N/67\rfloor)
 -\frac52\left(
   \sqrt{N+1}-\sqrt{(N+1)/67}
  \right)
 >22.17.
 }
 \tag{L-91553.11}
\]

For `Y>=536`, every integer in `(Y/4,Y]` also lies in `(Y/67,Y]`.  There are at
least `3Y/4-1` such integers, and each contributes at least
`log(Y/4)/sqrt(Y)`.  Hence

\[
\begin{aligned}
 A(Y)-A(Y/67)
 &\ge\left(\frac{3Y}{4}-1\right)
       \frac{\log(Y/4)}{\sqrt Y}\\
 &>\frac83\sqrt Y\\
 &>\frac52\left(
       \sqrt Y-\sqrt{Y/67}
      \right).
\end{aligned}
\tag{L-91553.12}
\]

Indeed `3/4-1/Y>2/3`, `log(Y/4)>4`, and the final right side is `<(5/2)sqrt(Y)`.
Thus the derivative is positive for every `Y>=536` as well.

Combining continuity, (L-91553.9), (L-91553.11) and
(L-91553.12),

\[
 \boxed{
 \mathcal E(Y)-\mathcal E(Y/67)
 \ge5\left(
  \sqrt Y-\sqrt{Y/67}
 \right)
 \qquad(Y\ge67).
 }
 \tag{L-91553.13}
\]

## 4. Every live branch score lies below the universal slope five

After division by the positive row coefficient, every declared survival or
hazard score has the affine form

\[
 S_\tau(Y)=a_\tau\sqrt Y-b_\tau
 \tag{L-91553.14}
\]

with

\[
 0<a_\tau<5.
 \tag{L-91553.15}
\]

For example,

\[
 \frac{S_s}{(1-r)(r+3)}
 =\frac{r+1}{r+3}(5\sqrt Y-3),
 \tag{L-91553.16}
\]

and

\[
 \frac{S_h}{r(r+2)}
 =\frac{(4r+1)\sqrt Y-(2r+1)}{r+2}.
 \tag{L-91553.17}
\]

The constants cancel under a fixed endpoint difference.  Therefore
(L-91553.13) implies

\[
 \boxed{
 \mathcal E(Y)-\mathcal E(Y/67)
 \ge S_\tau(Y)-S_\tau(Y/67)
 \qquad(Y\ge67)
 }
 \tag{L-91553.18}
\]

for both target-Hall branch types, and also for the native slope-five score.

## 5. Correct score interpretation of the fixed split

Take a positive source atom with quotient `Y>=67`.  The current-generation row
in the deterministic split is the coefficientwise positive difference

\[
 Q_Y-Q_{Y/67}.
 \tag{L-91553.19}
\]

Its literal entropy score is

\[
 \mathcal E(Y)-\mathcal E(Y/67).
 \tag{L-91553.20}
\]

Equation (L-91553.18) proves that this actual physical row realizes at least the
entire declared current-generation score difference.  Consequently replacing
the child component row by an arbitrary feasible child packing creates no
extra local score debt:

\[
 \boxed{
 \text{parent loss inherited from this atom}
 \le\text{child declared-score loss}.
 }
 \tag{L-91553.21}
\]

The fixed affine lift is separately score-noncontracting by `L-91549`, so the
same inequality holds in parent physical coordinates.

## 6. Frontier below 67

For `1<=Y<67` there is no contracted child.  The exact entropy row is
nonnegative, while every live paired type obeys

\[
 0\le S_\tau(Y)\le2T_\tau(Y).
 \tag{L-91553.22}
\]

Hence the positive score-realization debt of the bounded frontier satisfies

\[
 \boxed{
 [S_\tau(Y)-\mathcal E_\tau(Y)]_+
 \le2T_\tau(Y).
 }
 \tag{L-91553.23}
\]

After target normalization, the complete frontier debt is at most `2`.  Hall
row bonuses are coefficientwise nonnegative and contribute additional favorable
entropy.

## 7. What is repaired and what remains

`R-91552` refutes exact equality between declared source score and component
entropy.  The correct mechanism is stronger where inheritance occurs:

```text
large parent quotient Y>=67:
    actual current-row entropy >= declared score difference;
small quotient Y<67:
    no child, bounded finite-frontier debt.
```

Thus the fixed-67 **local** score recurrence can be repaired without the false
identity.

What remains to audit is global normalization: the target-normalized frontier
bound must be inserted into the literal unnormalized native loss recurrence
with the exact root packet amplitude.  This lemma does not assert that the root
target mass is `O(1)`.

```text
exact component entropy formula                    EXACT
source score = component entropy                    FALSE / R-91552
large-parent entropy domination                     PROVED
fixed-67 score-difference domination                PROVED
bounded normalized frontier debt                    PROVED
local inherited loss coefficient one                REPAIRED
native root-amplitude normalization                  OPEN / LOAD BEARING
Riemann Hypothesis                                   UNPROVEN
```
