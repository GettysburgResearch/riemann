# The exact multi-place $L$-function identity

Status: **PROVED** for every odd prime power `q`, every set of distinct
rational places, and every squarefree degree. The packet unifies the earlier
one-, two-, and three-place coefficient calculations; it proves no zero
theorem, memberwise sign law, or RH implication.

## Start here

Let `q` be odd, let $a_1,\ldots,a_m$ be distinct elements of
$\mathbf F_q$, and extend the quadratic character by $\chi(0)=0$. For a
monic polynomial $F$, put

\[
 \psi_{\mathbf a}(F)=\prod_{i=1}^m\chi(F(a_i)).
\tag{1}
\]

Write $\mathcal H_n(q)$ for the monic squarefree polynomials of degree
`n`. Then

\[
\boxed{
 \sum_{n\geq0}\ \sum_{D\in\mathcal H_n(q)}
 \psi_{\mathbf a}(D)u^n
 =L(u,\psi_{\mathbf a}){1-qu^2\over(1-u^2)^m}.}
\tag{2}
\]

In particular,

\[
\boxed{
 \sum_{D\in\mathcal H_n(q)}\prod_{i=1}^m\chi(D(a_i))
 =[u^n]L(u,\psi_{\mathbf a}){1-qu^2\over(1-u^2)^m}.}
\tag{3}
\]

The curve convention is essential. Define

\[
 f_{\mathbf a}(z)=\prod_{i=1}^m(a_i-z)
 =(-1)^m\prod_{i=1}^m(z-a_i),
 \qquad C_{\mathbf a}:y^2=f_{\mathbf a}(z),
\tag{4}
\]

using the smooth projective completion, and write its zeta numerator as

\[
 Z(C_{\mathbf a},u)
 ={P_{\mathbf a}(u)\over(1-u)(1-qu)}.
\tag{5}
\]

Then the finite-place Dirichlet polynomial in (2) is

\[
\boxed{
 L(u,\psi_{\mathbf a})=
 \begin{cases}
 P_{\mathbf a}(u),&m\text{ odd},\\
 (1-u)P_{\mathbf a}(u),&m\text{ even}.
 \end{cases}}
\tag{6}
\]

For odd `m`, the monic polynomial $\prod_i(z-a_i)$ is exactly
$-f_{\mathbf a}$. If `-1` is nonsquare, that replacement is the nontrivial
quadratic twist; if `-1` is square, the two models are already
$\mathbf F_q$-isomorphic. Equation (4), rather than a silently monic model,
is the convention that makes
$\psi_{\mathbf a}(T-z)=\chi(f_{\mathbf a}(z))$ exactly.

## 1. Proof of the squarefree identity

Multiplicativity and squarefree Euler factorization give

\[
\begin{aligned}
 \sum_{D\ {\rm monic\ squarefree}}\psi_{\mathbf a}(D)u^{\deg D}
 &=\prod_P\left(1+\psi_{\mathbf a}(P)u^{\deg P}\right)\\
 &={L(u,\psi_{\mathbf a})\over
          L(u^2,\psi_{\mathbf a}^2)}.
\end{aligned}
\tag{7}
\]

The square $\psi_{\mathbf a}^2$ is the indicator that a polynomial is
coprime to the `m` conductor factors $T-a_i$. Therefore

\[
 L(u^2,\psi_{\mathbf a}^2)
 =\prod_{P\nmid\prod_i(T-a_i)}(1-u^{2\deg P})^{-1}
 ={(1-u^2)^m\over1-qu^2}.
\tag{8}
\]

Substituting (8) into (7) proves (2)--(3).

The quotient in (7) is standard: it appears explicitly as equation (9.7) in
the preprint version, equation (10-4) in the published version, of
Keating--Rudnick, *Squarefree polynomials and Möbius values in short
intervals and arithmetic progressions*
([arXiv:1504.03444](https://arxiv.org/abs/1504.03444)). The contribution of
this packet is the evaluation-character adapter, its exact infinity/twist
convention, and the bounded degree-five specializations, not a novelty claim
for the Euler quotient.

For completeness, (6) is the infinity-factor bookkeeping for the quadratic
cover (4). If `m` is odd, infinity is ramified, contributes no Artin Euler
factor, and the finite Dirichlet polynomial is $P_{\mathbf a}$. If `m` is
even, the leading coefficient of $f_{\mathbf a}$ is `1`, so infinity
splits. The global Artin factor at infinity is $(1-u)^{-1}$; deleting it
from the finite Dirichlet product gives $(1-u)P_{\mathbf a}(u)$.

This also explains the point-count convention. The completion of (4) has
one rational point above infinity for odd `m` and two for even `m`. Thus,
with

\[
 t_{\mathbf a}=q+1-\#C_{\mathbf a}(\mathbf F_q),
\tag{9}
\]

we have

\[
 t_{\mathbf a}=
 \begin{cases}
 -\sum_z\chi(f_{\mathbf a}(z)),&m\text{ odd},\\
 -1-\sum_z\chi(f_{\mathbf a}(z)),&m\text{ even}.
 \end{cases}
\tag{10}
\]

The extra `-1` in the even row is not optional: it is the same split-infinity
factor seen in (6).

## 2. Degree-five specializations

The even coefficient kernel in (2) is

\[
 [u^{2k}]{1-qu^2\over(1-u^2)^m}
 =\binom{m+k-1}{k}-q\binom{m+k-2}{k-1}
 \quad(k\geq1).
\tag{11}
\]

If

\[
 L(u,\psi_{\mathbf a})=\sum_{j\geq0}\ell_j u^j,\qquad
 B_{m,0}=1,\qquad
 B_{m,k}=\binom{m+k-1}{k}-q\binom{m+k-2}{k-1}\quad(k\geq1),
\]

then every degree has the finite coefficient formula

\[
\boxed{
 S_{n,m}:=\sum_{D\in\mathcal H_n(q)}\psi_{\mathbf a}(D)
 =\sum_{\substack{0\leq j\leq n\\n-j\ {\rm even}}}
 \ell_j B_{m,(n-j)/2}.}
\tag{12}
\]

In degree five this reduces to the particularly useful identity

\[
\boxed{
 S_{5,m}=
 \left(\binom{m+1}{2}-qm\right)\ell_1
 +(m-q)\ell_3+\ell_5.}
\tag{13}
\]

Set $t=t_{\mathbf a}$. For `n=5` and `1 <= m <= 5`, (13) becomes

\[
\boxed{
\begin{array}{c|c|c}
 m&P_{\mathbf a}(u)&
 \displaystyle\sum_{D\in\mathcal H_5(q)}\prod_{i=1}^m\chi(D(a_i))\\ \hline
 1&1&0\\
 2&1&2q-3\\
 3&1-tu+qu^2&3(q-2)t\\
 4&1-tu+qu^2&q^2-10+(4q-10)t\\
 5&1-tu+bu^2-qtu^3+q^2u^4&(q^2-15)t.
\end{array}}
\tag{14}
\]

Several features that looked separate in the smaller packets are therefore
one coefficient extraction:

* the one-place mean vanishes;
* the two-place coefficient is $2q-3$;
* the three-place elliptic channel is $3(q-2)t$;
* four places retain both a universal term and an elliptic trace term;
* five places expose only the genus-two Frobenius trace at degree five: the
  middle coefficient `b` cancels exactly.

The last cancellation is a coefficient identity, not evidence that the full
genus-two local factor is determined by its trace.

## 3. Connected joint cumulants

There is an exact connected-correlation corollary. Draw $D$ uniformly from
$\mathcal H_5(q)$ and put $X_i=\chi(D(a_i))$. For a set $I$ of distinct
labels, let

\[
 \kappa_I=
 \sum_{\pi\in\Pi(I)}
 (-1)^{|\pi|-1}(|\pi|-1)!
 \prod_{B\in\pi}\mathbb E\!\left[\prod_{i\in B}X_i\right].
\tag{15}
\]

Write

\[
 N=q^4(q-1),\qquad C=2q-3,\qquad
 t_I=q+1-\#C_I(\mathbf F_q),\qquad
 C_I:y^2=\prod_{i\in I}(a_i-z),
\tag{16}
\]

with the same twist and infinity convention as (4)--(10). Because every
one-place mean vanishes, partitions containing a singleton make no
contribution. Equations (12)--(14) therefore give

\[
\boxed{
\begin{array}{c|c}
 |I|&\kappa_I\\ \hline
 2&\displaystyle {C\over N}\\[4pt]
 3&\displaystyle {3(q-2)t_I\over N}\\[4pt]
 4&\displaystyle {q^2-10+(4q-10)t_I\over N}
                 -{3C^2\over N^2}.
\end{array}}
\tag{17}
\]

For a five-element place set $A$, the only proper centered partition profile
is $2+3$. The ten pair/triple partitions are indexed bijectively by the ten
three-subsets $B\subset A$, so

\[
\boxed{
 \kappa_A=
 { (q^2-15)t_A\over N}
 -{3C(q-2)\over N^2}
  \sum_{\substack{B\subset A\\|B|=3}}t_B.}
\tag{18}
\]

The ten elliptic traces $t_B$ generally differ from one another. In
particular, their sum must not be replaced by $10t_A$, or by any other
automatic multiple of the five-place genus-two trace. Formula (18) is a
connected five-place identity, but it retains the separate geometry of all
ten triple subconfigurations.

### Hasse envelopes

A triple requires `q >= 3`. Four distinct rational places require
`q >= 4`, hence `q >= 5` in the present odd-characteristic setting, and five
places require `q >= 5`. For `q >= 5`, the relevant Hasse bounds are

\[
 |t_I|\leq2\sqrt q\quad(|I|=3,4),\qquad
 |t_A|\leq4\sqrt q\quad(|A|=5),\qquad
 \sum_{\substack{B\subset A\\|B|=3}}|t_B|\leq20\sqrt q.
\tag{19}
\]

They make the connected scales rigorous and uniform in the marked places:

\[
 \kappa_2={2q-3\over q^4(q-1)}
 =2q^{-4}-{1\over q^4(q-1)}
 =2q^{-4}+O(q^{-5}),
\tag{20}
\]

\[
 |\kappa_I|
 \leq {6(q-2)\sqrt q\over N}
 ={6(q-2)\over q-1}q^{-7/2}
 \qquad(|I|=3),
\tag{21}
\]

and, for `|I|=4`,

\[
 \left|\kappa_I-{q^2-10\over N}\right|
 \leq {2(4q-10)\sqrt q\over N}+{3C^2\over N^2}.
\tag{22}
\]

Consequently,

\[
 \kappa_I={q^2-10\over N}+O(q^{-7/2})+O(q^{-8})
 =q^{-3}+O(q^{-7/2})\qquad(|I|=4).
\tag{23}
\]

Finally, (18) and all ten genus-one Hasse bounds give

\[
 |\kappa_A|
 \leq {4(q^2-15)\sqrt q\over N}
      +{60C(q-2)\sqrt q\over N^2}
 =O(q^{-5/2}).
\tag{24}
\]

The second term in (24), which is precisely the pair/triple complement
correction, is `O(q^-15/2)`. Thus the genus-two trace supplies the largest
available Hasse envelope, while the ten elliptic subconfiguration traces
remain exactly present at a much smaller scale. These are envelope bounds,
not claims that either scale is attained for every configuration.

The producer verifies the centered partition skeletons directly: one full
block at orders two and three; a full block minus the three pair-pair
partitions at order four; and a full block minus the ten pair-triple
partitions at order five. It enumerates only the 52 set partitions of five
labels. This is finite combinatorial replay, not another finite-field
enumeration.

## 4. Tiny convention control

The producer makes one pass through the $5^5=3,125$ monic quintics over
$\mathbf F_5$. It reuses that pass for the prefixes of the ordered place
list `(0,1,2,3,4)` and checks all five rows of (14). It also computes each
auxiliary trace directly, adding one point at infinity for odd prefixes and
two for even prefixes.

The enforced bounds are 3,125 candidate polynomials, 15,625 possible family
place evaluations, 25 auxiliary affine evaluations, formal series degree
five, and no extension-field enumeration. This direct row checks signs,
twists, and infinity factors; the all-field proof is (7)--(8), not the
$\mathbf F_5$ enumeration.

```text
python -B research/l-families/atlas/function_field/quadratic_family_multiplace_l_function_identity.py --check
python -O -B research/l-families/atlas/function_field/quadratic_family_multiplace_l_function_identity.py --check
python -m pytest -q tests/test_quadratic_family_multiplace_l_function_identity.py
python -O -m pytest -q tests/test_quadratic_family_multiplace_l_function_identity.py
```

The auxiliary curve is the quadratic cover representing the finite
Dirichlet character. Nothing here promotes a local coincidence to a motive
or compatible system for an individual member, supplies a principal-member
amplifier, or proves RH/GRH. No external novelty claim is made.
