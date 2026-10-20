# Unequal cutoffs for the conductor-averaged quadratic/sextic pair

20 October 2026. Status: proposed source-dependent lemma, with an
explicit polynomial angular cost. For each fixed nonzero angular
order, the row-scale estimate of rStation paper 5 v3 is stronger.
The interest here is a proof from two operator sieves and the closed
theta reflection, without its inverse-moment recursion.

Use the pair in ../mixed/QUADRATIC_PAIR_ABSORPTION.md with r=1:
S is squarefree and prime to 6, \(\xi_S=(\cdot/S)_2\),
\(\eta_0=\xi_S\), and \(\eta_2=\xi_S(\cdot/S)_3^2\).
These are the quadratic and positive sextic channels, respectively.
Every character retains its nonunit zero. The completion remains
the quadratic-twisted cube factor, and all four ramified profiles
and both angular signs are included.

The primary operator inputs are Goldmakher--Louvel,
arXiv:1112.1642v2, Theorem 1.1/Corollary 1.2, and de Faveri,
arXiv:2610.04045v1, Theorem 1.1 with n=6.
The native-character bridge is recorded in
../global/QUADRATIC_LARGE_SIEVE_SOURCE_AUDIT.md, SHA256
91e0650760dd908b06984e6c806297508e70712695cdabbdde069e7c4b0aa863.
Their operator factors are, respectively,

\[
 H+Y,\qquad H+Y+H^{5/6}Y^{1/3}+H^{1/3}Y^{5/6},
\tag{A1}
\]

up to an arbitrarily small power and on their actual squarefree
supports. Our coefficients in the column are allowed arbitrary
complex sequences by these inputs. The family of row characters
is the stated residue-symbol family; no unrelated character may
be selected independently for each conductor.

## 1. The explicit mean

Fix \(0<\delta<1/6\), let \(\sigma=1/2+\delta\), and put
\(L=1+|\ell|+|t|\). Sum over \(NS\asymp H\), excluding S=1.
For \(\ell\ne0\), the two completed squared means satisfy

\[
 \mathcal A_2(H,\ell,t)\ll_{\delta,\epsilon}
       H^{\mu(\delta)+\epsilon}L^{2-4\delta+\epsilon},
\qquad
 \mathcal A_0(H,\ell,t)\ll_{\delta,\epsilon}
       H^{\nu(\delta)+\epsilon}L^{2-4\delta+\epsilon},
\tag{A2}
\]

where

\[
 \mu(\delta)=
 \begin{cases}
 9/8-7\delta/4,&0<\delta\le1/18,\\
 1+\dfrac{2\delta(1-12\delta)}{1+6\delta},
                 &1/18\le\delta\le1/12,\\
 1,&1/12\le\delta<1/6,
 \end{cases}
 \qquad
 \nu(\delta)=\max\{1,9/8-9\delta/4\}.
\tag{A3}
\]

The same proof includes \(\ell=0\) if the separate
../global/GUARDED_SPHERICAL_MEAN.md is used: every S here is a
nonunit primitive quadratic conductor, so its two odd local
characters kill both constant terms. No S=1 spherical claim is made.

## 2. Coupling the two free splits

The original integral in the two Gaussian free-split identities,
at length Y, has squared mean bounded by

\[
 O_0(Y)=H+Y^{1-2\delta},
\quad
 O_2(Y)=H+Y^{1-2\delta}
   +H^{5/6}Y^{1/3-2\delta}
   +H^{1/3}Y^{5/6-2\delta},
\tag{A4}
\]

up to \((HY)^\eta\). To check completion, fix a cube ideal d
before using (A1); its row factor \(\xi_S(d)\) has modulus at most
one and keeps its zeros. Minkowski then produces convergent d
sums with exponents \(-1-3\delta,-5/2,-3/2,-9/4\), respectively.
No independent coprimality condition between the squarefree and
cube indices is inserted.

The complete reflection exchanges channels 0 and 2. Its absolute
factor on the left line is \(H^{2\delta}L^{4\delta}\).
There is no moving cubic r and hence no Ramanujan divisor sum.
The shifted squared mean therefore has coefficient

\[
                   Y^{-4\delta}H^{4\delta}L^{8\delta}.
\tag{A5}
\]

Choose the sextic and quadratic cutoffs

\[
 Y_2=C H^b L^2,\qquad Y_0=C H^{2-b}L^2.
\tag{A6}
\]

The product of the two coefficients in (A5) is \(C^{-8\delta}\).
The exponents in (A3) and the choice of b below satisfy
\(\mu-\nu=4\delta(1-b)\). Thus, after normalizing the two
suprema by their respective H powers and the same L power,
both cross coefficients are \(C^{-4\delta}\), up to fixed
constants. Choose C sufficiently large to make both less than
one quarter.

Use finite conductor and angular cutoffs and all real heights.
The preliminary uniform right-line absolute bound, exact reflected
left-line bound, and Gaussian three-lines argument in
ANGULAR_UNIFORMITY.md make both normalized suprema finite before
absorption. Reflection keeps S and reverses ell, so the finite
cutoffs close. Arbitrarily small sieve losses are absorbed into
the final epsilon powers; the largest angular exponent from
(A4) is \(2-4\delta\). Letting the cutoffs increase proves (A2).
At ell=0 the finitely many bounded gamma arguments are handled
as in that note, using a preliminary left line \(-\eta\),
\(0<\eta<1/6\).

Equivalently, eliminating the quadratic mean gives the sextic
H-exponent as the maximum of the six affine functions

\[
 1,\quad b(1-2\delta),\quad
 5/6+b(1/3-2\delta),\quad
 1/3+b(5/6-2\delta),\quad
 1+4\delta(1-b),\quad 2-b(1+2\delta).
\tag{A7}
\]

The extra factor \(L^2\) in both cutoffs is essential for a
uniform angular statement; keeping Y independent of ell would
leave an uncontrolled cross coefficient.

## 3. Exact optimization of this envelope

For \(0<\delta\le1/18\), the third and sixth functions in (A7)
have opposite slopes and meet at b=7/8, giving
\(9/8-7\delta/4\). The other four are no larger there.
Their maximum is a lower bound for the whole envelope, proving
optimality within (A7), not just a sampled-grid optimum.

For \(1/18\le\delta\le1/12\), the third and fifth functions meet
at

\[
                  b=\frac{1+24\delta}{2+12\delta},
\tag{A8}
\]

which lies in [7/8,1]. Their value is the middle expression
in (A3). The sixth function is no larger precisely from the
left endpoint onward. For b at most one, the fourth function
is no larger than the third, and the second is at most one.
Again the two active functions give a matching lower bound.

For \(\delta\ge1/12\), b=1 makes every function at most one,
and the first function proves optimality. Subtracting
\(4\delta(1-b)\) gives the quadratic exponent in (A3).
Thus both bounds in (A2) are obtained by the same pair of
cutoffs, including their shared boundary points.

## 4. Comparison and limits

rStation paper 5 v3, Theorem 5 and (11.5), gives the completed
sextic H bound at all lengths for a fixed nonzero angular order.
Its Theorem 6 gives the quadratic partner, including the three
reflected cusp families and complete cube tails. The four fixed
ramified characters here fit its allowed finite ray character.
A fixed excluded prime can be reopened by finitely many squarefree
choices and a convergent cube geometric sum on this right line.
Summing dyads with the factor \(D^{-\delta}\) therefore gives
\(H^{1+\epsilon}\) for this pair at every fixed nonzero ell.

That result explicitly does not assert uniformity in growing ell
and excludes angular order zero. We do not claim that (A2)
improves its fixed-nonzero-angular conductor exponent. The present
proof records a polynomial angular cost using fewer analytic
inputs, and permits the separately guarded spherical extension.
It supplies no estimate for an additive prime-divisor mark and
no improved numerical zero-free boundary.
