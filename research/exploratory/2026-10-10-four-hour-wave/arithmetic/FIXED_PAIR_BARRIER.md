# An exact barrier for any fixed number of exclusion pairs

Status: **Root-reviewed analytic and source component deduction; directed
scalar brackets passed normal and optimized replay.** This is a limitation of a
specific lower-bound architecture. It gives no native negative SHARP
endpoint and no counterexample to RH.

Use the exact labels, exponent a>1, static weights w_q=q^-a, V=sum w_q,
and elementary masses e_k=sum_(|A|=k) product_(q in A)w_q. All sums converge
absolutely. Define the complete static marked mass

\[
 D_k^\infty=\sum_{|A|=k}\left(\prod_{q\in A}w_q\right)
                   \sum_{q\in A}w_q.
\]

Multiplying e_k by V splits the chosen extra label into an unused label,
counting each (k+1)-subset k+1 times, and a used label. Therefore

\[
 V e_k=(k+1)e_{k+1}+D_k^\infty.
 \tag{B-E1}
\]

All terms are positive and the total is finite, so this split is exact.
Both labelled copies of 67 remain distinct throughout.

## 1. The ideal complete-mass comparison

Retain precisely the even removal pairs k=2,4,...,2J with the static
used-label correction (E4). Even granting their full infinite static
masses and replacing every kernel by its limit one, the resulting margin is

\[
 G_J(a)=1-V+\sum_{j=1}^J\left[
 (1-V/(2j+1))e_{2j}+D_{2j}^\infty/(2j+1)\right]
       =\sum_{k=0}^{2J+1}(-1)^ke_k.
 \tag{B-E2}
\]

The equality follows directly from (B-E1). In the architecture used by
A-PA1, V<3 makes every retained even coefficient positive. Consequently
any finite selected even/marked mass gives a limiting margin <=G_J.
The selected masses converge increasingly to e_k,D_k^infinity as the
product cutoff tends to infinity. Therefore G_J is the optimal limiting
static margin for this fixed list of pairs and this removal comparison.

At each fixed a>1 the native normalized source itself satisfies

\[
 \lim_{x\to\infty}H_m(x)/T(x)^m
    =\prod_q(1-w_q)=(1-67^{-a})/\zeta(a)>0.
 \tag{B-E3}
\]

This follows from normalized kernel convergence to one and domination by
the absolutely convergent labelled product sum. Negative G_J is thus a
loss in the chosen comparison, even though the actual eventual source
has a positive limit.

## 2. Strict monotonicity and a unique boundary

For finitely many labels and weights in (0,1), G_J is the odd Bonferroni
partial sum for the probability that none of independent events with
probabilities w_q occurs. Its derivative with respect to one weight w_i is
minus the even Bonferroni partial sum of degree 2J over the remaining labels.
That even sum is at least the exact positive remaining product
product_(q!=i)(1-w_q). This standard finite Bonferroni inequality also
follows pointwise by writing the truncated inclusion-exclusion sum in
terms of the integer number of events that occurred and then averaging.
Hence G_J is strictly decreasing in each coordinate.

As a increases every coordinate q^-a decreases. The finite inequalities
pass to the infinite sums by absolute convergence. Strictness survives:
for a2>a1, first decrease the 2-label weight alone, obtaining at least

\[
 (2^{-a_1}-2^{-a_2})\prod_{q\ne2}(1-q^{-a_1})>0,
\]

and then decrease all remaining weights, which can only increase G_J.
The product is positive because sum q^-a1 converges. Thus G_J is continuous
and strictly increasing on a>1.

For fixed j>=2, W_j(a)=sum q^-ja has a finite limit as a decreases to one.
The generating identity

\[
 \sum_ke_k t^k=\exp\left[\sum_{j\ge1}(-1)^{j-1}W_jt^j/j\right]
\]

is valid near t=0 by absolute convergence, and for fixed coefficients
yields e_k=V^k/k!+O(V^(k-2)) for k>=2. Since V(a) diverges as a decreases
to one, the highest odd term of (B-E2) gives

\[
 G_J(a)=-V^{2J+1}/(2J+1)!+O(V^{2J})\longrightarrow-\infty.
 \tag{B-E4}
\]

As a tends to infinity, V tends to zero and G_J tends to one. There is
therefore a unique scalar root a_J>1. Below its corresponding power
m_J=2a_J-1, the ideal fixed-pair margin is negative. No finite product
cutoff or sharper finite moment arithmetic can make this architecture's
limiting lower margin strictly positive there.

The mark correction itself has only the lower-order growth

\[
 D_k^\infty=W_2V^{k-1}/(k-1)!+O(V^{k-2}),
\]

from (B-E1) and the generating expansion. It pays exact collision costs,
but does not cancel the fixed highest odd level as V diverges.

## 3. Directed scalar brackets

`verify_exclusion_barrier.py` applies the independently proved prime-zeta
Möbius formula and its entire omitted tail (P10), at cutoff 80 and Arb
precision 192. Newton's elementary identity supplies e_1,...,e_(2J+1).
Exact rational bisection retains strict negative/positive endpoint balls.
Normal and optimized JSON outputs are byte-identical.

The power boundaries are enclosed by

| Fixed architecture | Certified strict bracket for its ideal boundary |
| --- | --- |
| One even pair (levels 2--3) | 1.323532271997906 < m_1 < 1.323532271998134 |
| Two even pairs (through levels 4--5) | 1.155936917402701 < m_2 < 1.155936917402929 |
| Three even pairs (through levels 6--7) | 1.081059981705183 < m_3 < 1.081059981705411 |
| Positive-pair guard V<3 | 1.077289147610658 < m_V < 1.077289147610886 |

The decimal displays are enlarged from exact retained rational endpoints;
the receipts contain those endpoints and their directed sign balls.
In particular the three-pair ideal boundary is stronger than its V<3
coefficient guard. These boundaries concern this fixed architecture,
rather than the native positivity threshold. Increasing the number of
retained pairs changes the method boundary and still requires a fresh
uniform source proof; no passage to critical power is established here.
