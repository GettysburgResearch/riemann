# Joint quadratic/sextic means with unequal completion lengths

20 October 2026. **Proposed source-dependent analytic lemma.**
This is a direct paired-sieve derivation of a simultaneous conductor
average, separate from the frozen fixed-conductor proof. Independent
review is requested. The bound improves direct summation of that
fixed-conductor lemma, but Section 5 shows it is already recoverable
from a stronger supplied recursive input. The contribution is the
proof with fewer dependencies, not a new best numerical estimate or
a smaller zero-free boundary.

Dependencies are the complete reflected pair and four-profile closure
in `QUADRATIC_PAIR_ABSORPTION.md`, the number-field quadratic large sieve,
and the fixed-order sextic large-sieve upper bound of de Faveri,
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1). The argument
uses the latter's Theorem 1.1 in the squarefree row and column form

\[
 \Delta_6(H,Y)\ll(HY)^\epsilon
 \{H+Y+H^{5/6}Y^{1/3}+H^{1/3}Y^{5/6}\}.                 \tag{JQ1}
\]

The analytic large-sieve and theta inputs are imported; finite algebra
checks are not a proof of them.
The quadratic bound is its displayed (1.4), attributed there to the
number-field quadratic large sieve of Goldmakher and Louvel. The
Eisenstein primary-generator residue conventions are compared to these
ideal character families on fixed finite ray sectors; fixed row and
column phases have no effect on the positive norms.

## 1. The joint family and statement

Retain the definitions and natural zeros in (Q1)--(Q2) of the
fixed-conductor note. Here the quadratic character is the standard
primitive residue character \(\xi_S=\chi_{6,S}^3\), with the fixed
ray conventions of the source. Thus
\(\eta_0=\chi_{6,S}^3\) and \(\eta_2=\chi_{6,S}\).
Both \(r,S\) are squarefree primary ideals prime to 6, with
\((r,S)=1\). The row ranges are
\(Nr\le R\), \(H<NS\le2H\), where \(R,H\ge1\).
Fixed finite ray sectors are allowed. The angular degree is fixed
and nonzero.

Write \(\mathbf Q_j\) for the four scalar profiles and both angular
signs, with partner index \(j\in\{0,2\}\). Put

\[
 \mathcal M_j(R,H;s)=
 \sum_{\substack{Nr\le R,\ H<NS\le2H\\(r,S)=1}}^*
                    \|\mathbf Q_{r,S,j}(s)\|^2.
                                                               \tag{JQ2}
\]

Fix \(0<\delta<1/6\), and define

\[
 V=R^{6/11}H^{10/11},\quad W=R^{5/11}H^{12/11},\quad
 c_0=R^{2\delta/11}H^{-4\delta/11},\quad c_2=c_0^{-1}.
                                                               \tag{JQ3}
\]

In particular \(VW=RH^2\). Define the positive sums

\[
 \begin{split}
 F_2(R,H)={}&RH+RV^{1-2\delta}
       +RH^{5/6}V^{1/3-2\delta}
       +RH^{1/3}V^{5/6-2\delta}\\
       &+c_2RH+R^2H^2V^{-1-2\delta},\qquad
 F_0(R,H)=c_0F_2(R,H).
 \end{split}                                                   \tag{JQ4}
\]

Then the proposed estimate is

\[
 \boxed{\quad
 \mathcal M_j(R,H;1/2+\delta+it)
 \ll_{\ell,\delta,\epsilon}(RH)^\epsilon F_j(R,H)
                                  (1+|t|)^C,\quad j=0,2.
 \quad}                                                       \tag{JQ5}
\]

The exponent \(C\) is finite and independent of the moving ideals.
It can depend on the fixed angular and profile data. No uniformity in
a growing angular degree is claimed in this note.

At \(R=H=N\), throughout \(0<\delta<1/6\), the largest terms are

\[
 F_2(N,N)\asymp N^{(28-32\delta)/11},\qquad
 F_0(N,N)\asymp N^{(28-34\delta)/11}.                     \tag{JQ6}
\]

Thus on a line arbitrarily close to one-half from the right the
balanced exponent is \(28/11\), improving \(8/3\), which follows
by summing the earlier fixed-\(S\) bound over \(S\).
The exponent comparison at the limiting line is an epsilon-buffered
comparison of right-line estimates, not an assertion of pointwise
convergence of the defining series at \(s=1/2\).

## 2. Original-side bounds, including the entire cube sum

Use the same Gaussian free-split integral as in the fixed-conductor
proof. On the original side at \(\sigma=1/2+\delta\), apply the
quadratic or sextic sieve in \(S\), for each fixed \(r\).
The column multiplier
\(\widetilde g(c)\kappa(c)\overline{(c/r)_3}\alpha(c)^\ell\)
is allowed in these arbitrary-coefficient sieves, and the column
is squarefree. Removing \((r,S)=1\) only enlarges a positive row
sum. The fixed supplementary and ray phases have bounded finite
expansions.

At each fixed cube ideal \(d\), the extra factor \(\xi_S(d)\)
is a bounded row multiplier, including its zero. It can be removed
after placing the expression inside the positive \(S\) norm.
The remaining zero \((d,r)=1\) restricts the positive outer sum.
There is no new arithmetic multiplier depending on \(c,S\)
beyond the character already in the sieve, and no condition
\((c,d)=1\) is introduced.

The complete cube coefficient has modulus
\((Nd)^{-1-3\delta}\). Minkowski on its dyads converges for
\(\delta>0\); an original column power \(Y^a\), \(a\ge0\),
adds the factor \((Nd)^{-3a/2}\) to this norm estimate.
For the four relevant powers,
\(a=0,1-2\delta,1/3-2\delta,5/6-2\delta\), all are
nonnegative in the stated range. This includes every cube factor,
not only the unit cube.

Dyadic summation and the common Gaussian integral therefore give,
up to arbitrarily small powers and fixed height factors,

\[
 O_0(R,H;Y)=RH+RY^{1-2\delta},                           \tag{JQ7}
\]

\[
 O_2(R,H;Y)=RH+RY^{1-2\delta}
       +RH^{5/6}Y^{1/3-2\delta}
       +RH^{1/3}Y^{5/6-2\delta}.                        \tag{JQ8}
\]

The row term \(RH\) also covers the bounded initial column range.
The Gaussian truncation permits all longer columns with rapid decay,
instead of introducing a row-dependent sharp cutoff.

## 3. The reflected partner and the divisor rows

The exact primitive transformation in (Q6) sends \(0\leftrightarrow2\)
and leaves \(S\) unchanged. Its conductor factor is
\((Nr)^{1/2-2s}(NS)^{1-2s}\). Full signed resummation at the
primes of \(r\) has new row \(k\mid r\), still coprime to
\(S\). All four profiles and both angular signs remain in the
vector of the opposite partner.

Squaring and summing multiples of \(k\), exactly as in (Q9), gives

\[
 \mathcal M_j(R,H;1/2-\delta+it)
 \ll H^{4\delta}(1+|t|)^{8\delta}R^{4\delta+\eta}
 \sum_{Nk\le R}(Nk)^{-2\delta}
 \sum_{\substack{H<NS\le2H\\(k,S)=1}}^*
             \|\mathbf Q_{k,S,2-j}(1/2+\delta-it)\|^2.
                                                               \tag{JQ9}
\]

Every monomial of \(F_2\), as a function of \(R\), has one
of the powers

\[
 1,\quad 17/11-12\delta/11,\quad
 13/11-12\delta/11,\quad16/11-12\delta/11,\quad
 1-2\delta/11.
\]

For \(F_0\), add \(2\delta/11\) to those powers. Every one
is strictly greater than \(2\delta\) when \(0<\delta<1/6\).
Partial summation in (JQ9) consequently costs
\(R^{-2\delta}F_{2-j}(R,H)\), with constants depending only
on the fixed parameters. The reflected contribution to a free-split
mean with cutoff \(Y_j\), relative to the unshifted partner mean,
therefore has factor

\[
 R^{2\delta+\eta}H^{4\delta}Y_j^{-4\delta}
                                      (1+|t|)^{8\delta}.       \tag{JQ10}
\]

This divisor step is essential. A diagonal calculation only at
\(R=H\) would not be a closed proof, because reflection produces
smaller \(k\) while keeping the same \(S\).

## 4. Two finite suprema and contraction

Ignore small-power and height inflations for a moment. Choose
\(Y_2=V\), \(Y_0=W\). The two factors in (JQ10) are exactly
\(c_2\) and \(c_0\). Thus

\[
 O_2(V)\le F_2,\quad c_2O_0(W)\le F_2,\quad
 O_0(W)\le F_0,\quad c_0O_2(V)\le F_0.                 \tag{JQ11}
\]

The nontrivial equality in this check is

\[
 c_2 R W^{1-2\delta}
       =R^2H^2V^{-1-2\delta},                           \tag{JQ12}
\]

which uses \(VW=RH^2\). Therefore the normalized reflected
map from either partner to the other has coefficient one before
an enlargement of the cutoffs.

Now truncate both conductor ranges at arbitrary finite limits.
For each partner take its supremum over all lower row bounds,
dyadic \(S\) ranges within those limits, and real heights, divided
by
\((RH)^{\epsilon_0}F_j(R,H)(1+|t|)^C\).
The continued theta series have polynomial strip growth before
absorption, with a height degree independent of the moving ideals;
choose \(C\) sufficiently large. Each truncated supremum is
finite. The reflection preserves \(S\), decreases \(r\), and
changes only the included angular sign and partner, so both
truncations close.

Use the actual cutoffs

\[
 Y_2=C_0(RH)^\theta V(1+|t|)^2,\qquad
 Y_0=C_0(RH)^\theta W(1+|t|)^2.                          \tag{JQ13}
\]

Choose the sieve and divisor losses smaller than
\(4\delta\theta\), and then choose \(\theta\) small
enough that the increases in (JQ7)--(JQ8) fit in the final
epsilon allowance. The height factors in (JQ10) are canceled by
the displayed square of \(1+|t|\). The Gaussian convolution
preserves the polynomial height normalization, with a fixed
constant. The original-side height powers are bounded by a
fixed polynomial and are absorbed by the same chosen \(C\).

Finally choose the fixed \(C_0\) sufficiently large, after all
those constants. Each normalized reflected coefficient is at
most one-half, uniformly for \(R,H\ge1\). If the two finite
suprema are \(M_0,M_2\), they satisfy

\[
 M_0\le C_1+\tfrac12M_2,\qquad
 M_2\le C_1+\tfrac12M_0.
\]

They are bounded independently of the finite conductor cutoffs.
Letting those cutoffs tend to infinity proves (JQ5).

## 5. Source overlap and the unchanged detector obstruction

The two cutoffs balance the decreasing term
\(R^2H^2V^{-1-2\delta}\) with
\(RH^{1/3}V^{5/6-2\delta}\); their equality gives
\(V^{11/6}=RH^{5/3}\), hence (JQ3). No claim of global
optimality over all possible sieves or cutoffs is made.

The already supplied prescribed-coefficient completed means in
[rStation paper 5, Theorems 5--6](https://rstation.ai/problems/riemann_hypothesis/papers/5)
give more than the \(R=1\) special case. Its completed sum (11.1)
is the exact \(j=2\) family here, with row \(z=S\), fourth-power
label \(f=r\), and all cube factors. Fixed reciprocal phases can be
expanded on the same finite ray sectors. Undoing the normalized label
average in its (11.4) gives the central annular bound

\[
 \mathcal J_{2,\mathrm{comp}}(R,H;D)
           \ll(RHD)^\epsilon\{RH+R^2H^2/D\}.            \tag{JQ14}
\]

This bound holds for every \(D\), not merely its natural functional
equation length. Combine it with the original sextic sieve bound for
the same completed annulus. Below \(D=V\), use that sieve; above
\(V\), use (JQ14). At \(\sigma=1/2+\delta\), the square of
the dyadic weight is \(D^{-2\delta}\). Minkowski and geometric
summation give \(F_2-c_2RH\), which is at most our \(F_2\).
One quadratic free split at \(W\), followed by (JQ9), then gives
\(F_0\). Thus the exponent \(28/11\) is **already a consequence
of the supplied recursive input plus the ordinary sieves**.

The present proof does not use that recursion, its amplified inverse
moment, or (JQ14). It derives the comparable estimate directly from
the reflected pair and two elementary large-sieve original sides.
The distinction is a reduction of analytic dependencies. The displayed
comparison with \(8/3\) is only against direct summation of the
fixed-conductor lemma.

The actual detector additionally has a coherent prime-label sum with
row-dependent coefficients. This mean permits those coefficients only
after Cauchy, which loses that coherence. Even a hypothetical natural
joint count \(RH\) would only recover the inherited terminal edge,
as shown in `JOINT_CONDUCTOR_INTERFACE.md`. Since (JQ4) contains
\(RH\), the new bound does not lower that edge. The Type-III prime
problem also cannot substitute a prime-supported column for the free
theta series used in this proof. No improvement of \(B_\flat\)
or proof of RH follows from this auxiliary theorem.

## 6. A genuine free-column consumer

For \(|b(r,S)|\le1\), supported on the squarefree coprime ranges
above, consider

\[
 T_j(A,R,H)=\sum_{r,S}b(r,S)
       \sum_u\widetilde g(ur)\alpha(ur)^\ell
             \eta_{j,S}(ur)W_A(Nu/A),\qquad j=0,2.       \tag{JQ15}
\]

The free inner sum has a fixed smooth annular weight. It is not
restricted to primes, and there is no arbitrary arithmetic multiplier
in \(u\). The outer coefficients may depend jointly on \(r,S\).
The natural Gauss and character zeros retain all coprimalities.

Exact cubic multiplicativity extracts the unit outer coefficient
\(\widetilde g(r)\alpha(r)^\ell\eta_{j,S}(r)\), leaving
the squarefree series in (Q1). On \(\sigma=1/2+\delta\),
the reciprocal of its full cube factor is uniformly bounded by
absolute Euler convergence, since \(3\sigma-1/2=1+3\delta>1\).
Mellin inversion and Cauchy over the actual \((r,S)\) pairs give

\[
 |T_j(A,R,H)|\ll (ARH)^\epsilon
                   A^{1/2+\delta}(RH F_j(R,H))^{1/2}.    \tag{JQ16}
\]

The fixed height factor in (JQ5) is integrated against the rapidly
decreasing Mellin transform of \(W_A\). This is a statement about
the genuine mixed-conductor sum, with the specified smooth free
column, and does not need the detector's prime-label independence.

At \(A=R=H=N\), (JQ16) has exponents

\[
 T_0\ll N^{61/22-6\delta/11+\epsilon},\qquad
 T_2\ll N^{61/22-5\delta/11+\epsilon}.                   \tag{JQ17}
\]

Taking \(\delta\) arbitrarily close to \(1/6\), while remaining
inside the proved range, gives respectively
\(N^{59/22+\epsilon}\) and \(N^{89/33+\epsilon}\).
In the notation \(X=N^3\), these are
\(X^{59/66+\epsilon}\) and \(X^{89/99+\epsilon}\).
As with the mean, these explicit consumers can also be recovered from
the recursive source input in Section 5; no best-known novelty claim
is made for their numerical exponents.
