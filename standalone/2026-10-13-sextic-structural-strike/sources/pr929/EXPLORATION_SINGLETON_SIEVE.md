# Exploration: averaging singleton conductors and the cost of balancing their signs

**Status:** research exploration, not an additional promoted theorem or
an enlargement of the reviewed packet's signed remainder. The large-sieve
input and the exponent algebra are explicit below. A coarse version of
this approach gives no new diagonal-size region: its necessary condition
is exactly an older classical-completion condition. A more informative
profile retains the two singleton sign sizes; the feasible example at
the end identifies an avenue for a separate uniform-adapter review.
Neither calculation proves the full generalized moment or RH.

The source considered is Alexandre de Faveri,
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
Theorem 1.1 with order six. This is a different input from Proposition
8.1 used in [CUBIC_CONDUCTOR_AVERAGE.md](CUBIC_CONDUCTOR_AVERAGE.md).
The discussion below does not independently certify the external
theorem. The exact moment kernel, principal mask, and positive tuple
assignment count are those in Sections 3--4 of the companion note.

## 1. The one-label sixth-order mean suggested by the AFE

The order-six large sieve has the form
\[
\Theta_6(X,Q)\ll_\epsilon(XQ)^\epsilon
\left[X+Q+X^{5/6}Q^{1/3}+X^{1/3}Q^{5/6}\right].
\tag{1.1}
\]
Both ideal indices in this norm are sixth-power-free; a squarefree
outer index is an allowed further restriction by positivity.
All fixed family data, including the bad set and ray classes, must
remain fixed as the conductor varies.

Suppose a primitive background character has good conductor norm
\(R\), disjoint from a squarefree varying label \(a\sim X\).
The conductor of its product with the sixth-order family character
has norm comparable to \(RX\). The same uniform approximate-functional-
equation construction as in the companion note consequently suggests
a common length \(Q\ll(RX)^{1/2+\epsilon}\), with polynomial
dependence on vertical height suppressed here.

For this source the relevant unrestricted-index reduction is
\[
n=sqr^6,\qquad s\mid S^\infty,\quad q,r\in I(S),\quad
q\ \text{sixth-power-free}.
\tag{1.2}
\]
It is unique and imposes no condition \((q,r)=1\).
On a positive Mellin line, weighted Cauchy--Schwarz uses
\[
\sum_{s\mid S^\infty}\sum_r(N(sr^6))^{-1/2-\delta}
<\infty.
\tag{1.3}
\]
The \(r\)-sum is bounded by \(\zeta_K(3+6\delta)\).
As before, the actual primitive product values must be used at the
fixed bad primes. The square-norm of the remaining \(q\)-coefficient
on a dyadic block is \(O_\delta(1)\).

Substituting \(Q=(RX)^{1/2}\) in (1.1), and dividing by the number
of outer labels, gives the exact candidate second-mean ratio
\[
1+(R/X)^{1/2}+R^{1/6}+R^{5/12}X^{-1/4}.
\tag{1.4}
\]
In particular,
\[
\begin{aligned}
X^{-1}X^{5/6}(RX)^{1/6}&=R^{1/6},\\
X^{-1}X^{1/3}(RX)^{5/12}&=R^{5/12}X^{-1/4}.
\end{aligned}
\]
The associated first-mean bound has the four factors
\[
1,\qquad (R/X)^{1/4},\qquad R^{1/12},\qquad
R^{5/24}X^{-1/8}.
\tag{1.5}
\]
This step uses Cauchy--Schwarz over \(a\); it is an average of
absolute values of \(L\), without signed Möbius cancellation.

To promote this calculation, the sixth-order family must also be
matched explicitly to the physical singleton symbols with the
fixed finite ray and unit correction, just as Lemma 3.1 did for
the cubic double-prime family. A constant allowed to depend
arbitrarily on the moving background would not suffice. The
uniformity and the primitive bad-prime convention are therefore
part of the prospective deduction, not optional notation.

## 2. The singleton signs and the exact profile algebra

Separate the ideal singleton product into its two actual signs:
\[
g_1=a_+a_-,\qquad
a_+=\prod_{r_p=1,s_p=0}p,\qquad
a_-=\prod_{r_p=0,s_p=1}p.
\tag{2.1}
\]
These are squarefree and coprime. On a dyadic block write
\[
\max(Na_+,Na_-)\sim X,\qquad
\min(Na_+,Na_-)\sim Y,\qquad X\ge Y,\qquad XY\asymp L,
\]
and let \(Ng_2\sim G\). If the larger singleton label has the
negative sign, conjugate the \(L\)-function before applying the
one-label mean. Absolute values are preserved.

Freeze the smaller singleton label and every nonsingleton
conductor, including their residual exponents. The background
conductor in (1.4) is then
\[
R\asymp YG\prod_{m\ge3}Ng_m.
\tag{2.2}
\]
The principal-mask count supplies
\[
D^{k+\epsilon}(XY)^{-1/2}G^{-1}
\prod_{m\ge3}(Ng_m)^{-m/2}.
\tag{2.3}
\]
The first mean over the larger singleton, followed by the
positive sum over the smaller singleton, contributes \(XY\)
times (1.5). Summing the \(g_2\)-block contributes its \(G\)
possibilities, which cancels \(G^{-1}\) in (2.3).
Every higher-multiplicity sum converges: its positive conductor
exponent is one of \(0,1/4,1/12,5/24\), and even at \(m=3\)
the total exponent is strictly less than \(-1\).

Thus the profile delivered by this route is
\[
\boxed{
D^{k+\epsilon}H^{1/2}(XY)^{1/2}
\left[
1+(YG/X)^{1/4}+(YG)^{1/12}
+(YG)^{5/24}X^{-1/8}
\right].
}
\tag{2.4}
\]
The factors \(D^{k+\epsilon}\) and \(H^{1/2}\) here come from
the exact tuple count and the Mellin identity, respectively.
Arbitrary additional tuple selectors would be allowed by this
positive accounting, if the uniform family adapter is separately
reviewed and the estimate is promoted.

## 3. Why the coarse \(L,G\) consequence gives no new controlled region

Forgetting the sign sizes and only using \(Y\le\sqrt L\le X\)
replaces (2.4), up to fixed factors, by
\[
D^{k+\epsilon}H^{1/2}
\left[L^{1/2}G^{1/4}+L^{13/24}G^{5/24}\right].
\tag{3.1}
\]
Here the constant term is absorbed by the first term because
\(G\ge1\), and the term containing \(G^{1/12}\) is absorbed
by the second term.

To make (3.1) at most \(HD^{k+\epsilon}\), both conditions are
required:
\[
L^2G\le H^2,\qquad L^{13}G^5\le H^{12}.
\tag{3.2}
\]
But the first is exactly
\[
L\sqrt G\le H,
\tag{3.3}
\]
the earlier classical-completion diagonal region in PR #925.
Consequently (3.2) is contained in a previously controlled
region. It is incorrect to advertise it as a new diagonal-size
sector simply because it extends the isolated cubic-average
condition \(L\le H^{2/3}\).

For example, at \(G=1\) the apparent threshold
\(L\le H^{12/13}\) is weaker than the older threshold
\(L\le H\). Comparing only with the newest companion result
would conceal this no-gain conclusion.

This also explains why the coarse calculation cannot settle
the large-singleton remainder. Its apparent improvement in
the power of \(L\) carries another term which reinstates the
old completion obstruction. Every term of the large-sieve
bound must be retained before testing a target region.

## 4. A prospective sign-asymmetric profile worth reviewing separately

The loss in Section 3 occurred when \(Y/X\) was replaced by
one. This is avoidable for a specified asymmetric sign block.
In particular, if \(YG\le X\), the second term in the bracket
of (2.4) is at most one, and the fourth is at most the third:
\[
\frac{(YG)^{5/24}X^{-1/8}}{(YG)^{1/12}}
=(YG/X)^{1/8}\le1.
\]
The remaining profile is
\[
D^{k+\epsilon}H^{1/2}(XY)^{1/2}(YG)^{1/12},
\qquad
YG\le X,\qquad (XY)^6YG\le H^6.
\tag{4.1}
\]
Its second condition need not imply (3.3), because it uses
the actual smaller singleton sign label.

A feasible fourth-tuple pattern is
\[
(n_1,n_2;m_1,m_2)
=(ce a_1,\;cf_0 a_2;\;de,\;df_0),
\tag{4.2}
\]
with all six named labels supported on distinct good split
rational primes. Choose norm exponents
\[
Nc\asymp D^{1/10},\qquad
Nd,Ne,Nf_0\asymp D^{1/2},\qquad
Na_1,Na_2\asymp D^{2/5}.
\tag{4.3}
\]
Every original column has scale \(D\). The singleton labels
occur only on the positive side, so
\[
X=D^{4/5},\qquad Y=1,\qquad G=D^{3/5},
\qquad Nq_0=D.
\tag{4.4}
\]
These are feasible scale comparisons, not lower bounds for
arithmetic sums.

At \(h=21/20\), the four terms in (2.4) have respective
excesses over \(HD^2\)
\[
-\frac18,\qquad-\frac7{40},\qquad
-\frac3{40},\qquad-\frac1{10}.
\tag{4.5}
\]
The earlier completion excess is \(1/20>0\).
The middle term of the companion cubic anisotropic bound
has excess \(1/24>0\), since the two actual cubic labels
have exponents \(1/10\) and \(1/2\).
Thus this profile is not dismissed by the coarse no-gain
calculation in Section 3.

The appropriate next step is to review the full uniform
sixth-order adapter and compare the resulting positive
accounting with all stated older pointwise branches.
No claim is made here that it improves every existing
complete signed-block estimate. The main reviewed
remainder in this packet is unchanged by this exploration.
