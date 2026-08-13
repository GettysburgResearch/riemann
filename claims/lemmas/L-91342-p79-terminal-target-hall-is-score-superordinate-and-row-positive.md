# L-91342 — The `P_79` terminal window has a no-upward target Hall projection which is score-superordinate and row-positive

Claim ID: `L-91342`  
Status: **PROPOSED COMPLETE EXACT TERMINAL-PROJECTION THEOREM — DIRECTED CERTIFICATE PROVIDED**  
Created: 2026-08-12  
Depends on: `L-91112.25--26`, `L-91340/L-91341`; elementary Ferrers-Hall transport  
RH status: **unproved**

## 1. Why the target, not the score, is the right transport currency

Let

\[
 P_{79}=\prod_{p\le79}p.
\]

On the terminal range

\[
 1\le x<83,
\]

all squarefree integers which can occur have prime factors at most `79`.  Thus
this is exactly the finite `P_79` source window; the next possible rough prime is
`83`.

For squarefree `n<=x`, put

\[
 \boxed{
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
 }
\tag{L-91342.1}
\]

These are respectively the SHARP-target and endpoint-score source atoms.
Both are strictly positive on their support.

Define

\[
 \boxed{
 q_x(n)=\frac{W_\Psi(x,n)}{W_S(x,n)}.
 }
\tag{L-91342.2}
\]

Writing `t=sqrt(x/n)>=1`,

\[
 q_x(n)=\frac{4t-3}{5t-3},
 \qquad
 \frac d{dt}q_x(n)=\frac3{(5t-3)^2}>0.
\]

Consequently

\[
 \boxed{
 e\le o\Longrightarrow q_x(e)\ge q_x(o).
 }
\tag{L-91342.3}
\]

A smaller even source therefore supplies at least as much target per unit score
as a larger odd source.

## 2. Directed target-Hall margin through the next rough prime

For an active odd squarefree threshold `t<83`, define

\[
 \mathcal H_{\Psi,t}(x)
 =\sum_{\substack{e\le t\\\mu(e)=1}}W_\Psi(x,e)
  -\sum_{\substack{o\le t\\\mu(o)=-1}}W_\Psi(x,o).
\tag{L-91342.4}
\]

On a fixed threshold this is

\[
 \mathcal H_{\Psi,t}(x)
 =4A_t\sqrt x-3B_t,
\]

where

\[
 A_t=\sum_{n\le t}\frac{\mu(n)}n,
 \qquad
 B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

Hence its minimum on `t<=x<83` occurs at `x=t` if `A_t>=0`, and at the
right limit `x->83-` if `A_t<0`.

The directed checker `X-91122` verifies all twenty-seven active odd thresholds
using exact `Fraction` arithmetic and rational square-root enclosures.  It proves

\[
 \boxed{
 \mathcal H_{\Psi,t}(x)>\frac7{100}
 \qquad(1\le x<83)
 }
\tag{L-91342.5}
\]

for every active odd threshold.  The least directed margin occurs at `t=13` and
`x->83-`; its lower endpoint is larger than

\[
 0.07307554067.
\]

Therefore the nested-neighborhood Hall theorem gives a positive transport, in
**target-mass units**,

\[
 \boxed{
 \pi_x:O_\Psi^x\longrightarrow E_\Psi^x,
 \qquad e\le o,
 }
\tag{L-91342.6}
\]

which uses every odd target demand and no more than the even target capacities.

## 3. Target-exact positive residual measure

Let `t_(o,e)>=0` be any transport in (L-91342.6).  Thus

\[
 \sum_e t_{o,e}=W_\Psi(x,o)
\]

for every odd source, and

\[
 \sum_o t_{o,e}\le W_\Psi(x,e)
\]

for every even source.  Define the residual target mass

\[
 r_e=W_\Psi(x,e)-\sum_ot_{o,e}\ge0
\]

and the positive coefficient measure

\[
 \boxed{
 \nu_x(e)=\frac{r_e}{W_\Psi(x,e)}\ge0.
 }
\tag{L-91342.7}
\]

Then the signed finite target is represented exactly:

\[
 \boxed{
 \sum_e\nu_x(e)W_\Psi(x,e)
 =\sum_{\mu(e)=1}W_\Psi(x,e)
  -\sum_{\mu(o)=-1}W_\Psi(x,o).
 }
\tag{L-91342.8}
\]

No target capacity is discarded or duplicated.

## 4. The same representation has at least the signed endpoint score

Since score per target unit is `1/q_x(n)`, the score of the residual positive
measure minus the signed score equals

\[
 \begin{aligned}
 &\sum_e\nu_x(e)W_S(x,e)
 -\left[
   \sum_{\mu(e)=1}W_S(x,e)
   -\sum_{\mu(o)=-1}W_S(x,o)
  \right]\\
 &\qquad=
 \sum_{o,e}t_{o,e}
 \left[\frac1{q_x(o)}-\frac1{q_x(e)}\right].
 \end{aligned}
\]

By `e<=o` and (L-91342.3), every summand is nonnegative.  Therefore

\[
 \boxed{
 \sum_e\nu_x(e)W_S(x,e)
 \ge
 \sum_{\mu(e)=1}W_S(x,e)
 -\sum_{\mu(o)=-1}W_S(x,o).
 }
\tag{L-91342.9}
\]

The terminal projection is target-exact and **score-superordinate**.  This is the
correct orientation for the signed score-loss consumer.

## 5. Target-normalized component rows are increasing through `83`

Retain the exact positive component row

\[
 Q_Y(j)
 =(j+1)\Delta^2\left[\frac{S_Y(j)}{j-1}\right]\ge0.
\]

On an activation cell `N<=Y<N+1`, write

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N},
 \qquad C_{j,N}>0.
\]

For

\[
 \mathcal Q_j^\Psi(Y)
 =\frac{Q_Y(j)}{4\sqrt Y-3},
\]

direct differentiation gives a numerator

\[
 M_{4,3}(Y)
 =4\sqrt Y[2C_{j,N}-Q_Y(j)]-6C_{j,N}.
\tag{L-91342.10}
\]

Moreover

\[
 M_{4,3}'(Y)
 =-\frac{2Q_Y(j)}{\sqrt Y}\le0,
\]

so the minimum on each cell is at the right endpoint.

The checker `X-91122` evaluates all

\[
 3321
\]

cells `2<=j<=N<=82`.  Directed square-root and logarithm intervals prove

\[
 \boxed{
 M_{4,3}(Y)>\frac16
 \qquad(1<Y<83).
 }
\tag{L-91342.11}

The least lower endpoint is larger than `0.1810531355`, at row `j=81`, cell
`N=82`.  Hence

\[
 \boxed{
 \frac{Q_Y(j)}{4\sqrt Y-3}
 \text{ is strictly increasing on }1<Y<83.
 }
\tag{L-91342.12}

## 6. Exact finite-row lift

For a source `k`,

\[
 k^{-1/2}Q_{x/k}(j)
 =W_\Psi(x,k)
  \frac{Q_{x/k}(j)}{4\sqrt{x/k}-3}.
\tag{L-91342.13}
\]

Apply the target-mass transport of Section 2.  Since `e<=o`, one has
`x/e>=x/o`; by (L-91342.12),

\[
 \boxed{
 \begin{aligned}
 c_x(j)={}&
 \sum_{o,e}t_{o,e}
 \left[
  \frac{Q_{x/e}(j)}{4\sqrt{x/e}-3}
  -\frac{Q_{x/o}(j)}{4\sqrt{x/o}-3}
 \right]\\
 &+\sum_er_e
  \frac{Q_{x/e}(j)}{4\sqrt{x/e}-3}
 \ge0.
 \end{aligned}
 }
\tag{L-91342.14}
\]

Thus the same positive object is simultaneously:

```text
target-exact;
score-superordinate;
coefficientwise nonnegative in every exact finite row;
source-faithful before ordinary/radix-four carry evaluation.
```

## 7. Reset meaning

After absorbing primes through `79`, every unprocessed rough prime is at least
`83`.  A branch with no active rough prime has local ratio below `83`, so the
complete terminal source is covered by this theorem.  No upward parity edge,
scalar tensorization, fractional finite-column evaluation, or signed endpoint
inverse is required at the leaf.

The theorem does not by itself construct the nonterminal rough source
partition.  It closes the terminal projection needed by such a partition.

## 8. Proof boundary

```text
P_79 target-Hall margin >7/100                   DIRECTED EXACT
target-mass no-upward transport                    EXACT
positive residual target representation            EXACT
score superordination                               EXACT
target-normalized component monotonicity to 83      DIRECTED EXACT
exact finite-row positivity                         EXACT
terminal source-to-row projection                   CLOSED
nonterminal rough source disintegration             SEPARATE / OPEN
Riemann Hypothesis                                  UNPROVEN
```