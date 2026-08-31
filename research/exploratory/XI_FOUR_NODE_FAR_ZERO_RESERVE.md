# A far-zero reserve for the two four-node xi factors

Status: proposed analytic theorem; preregistered before its finite controls.
Scope: the literal completed Riemann xi function, ordinary real safe-axis
nodes only, with imported published partial-RH and explicit zero-count
theorems. This is not an all-order positivity theorem or a proof of RH.

Authoring parent: `e5e43625b157ecc5f602532e16a1197679594824` (SP).
The repaired order-three input is the resident canonical xi/Pick packet
at `8f01064df805624c045877655893c324a220975d`.

## 1. Claim, dependencies and preregistered checks

Write

\[
 Y(x)=\xi_R(1/2+x),\quad F(x)=Y'(x)/Y(x),\quad
 p(t)=F(\sqrt t)/\sqrt t,\qquad t>1/4.
\]

The proposed conclusion is that both p and t p have strictly positive
Schwarzian derivative on this entire interval. Consequently, for every
four distinct real numbers x_i>1/2,

\[
 H_{ij}=\frac{F(x_i)+F(x_j)}{x_i+x_j}                 \tag{FR1}
\]

is positive definite. Repeated nodes give PSD, not positive definiteness.
The same strict conclusion for one, two or three distinct nodes follows
by extending the set to four. No derivative/confluent matrix is asserted.

Imported analytic inputs are:

1. The classical even Hadamard product for completed xi, its functional
   equation and reality symmetry, and that nontrivial zeros lie in the
   open critical strip. Multiplicities are retained throughout.
2. Platt--Trudgian's published verification of RH up to height
   H=3,000,000,000,000. Only reality of the corresponding squared poles
   is used, not simplicity. The author personally inspected the rendered
   Theorem 1 page of arXiv:2004.09765; its stated bound is slightly higher.
   The original zero-verification computation is not rerun here.
3. Rosser's explicit zero-count estimate, in Faber--Kadiri's Theorem 1.5,
   personally inspected on rendered page 3. Their corrigendum was also
   read; it retains the same zero-count constants. The original 1941
   Rosser article is not claimed to have been personally inspected.
4. The repaired canonical theorem that all order-at-most-three matrices
   FR1 are PSD. No historical strict-anchor assertion is imported.
5. SP16--17's four-node determinant identity, including its normalization.

The new work is the uniform complex-pole pair budget and the disjoint
far-edge allocation, for BOTH p and t p, followed by a self-contained
Schwarzian-to-four-point argument. Numerical positivity at sampled xi
nodes is not used.

Before controls, the finite design is fixed as follows. Use exact rational
complex arithmetic only, with no new xi evaluations or zero survey:

- all q=0,1 pair-dispersion identities for six fixed conjugation-invariant
  pole multisets, at t=1/4,1,10,100;
- exact bounds on every rational constant in sections 3--6;
- shared-anchor and multiplicity allocation controls on three fixed
  directed height graphs, including an intentionally invalid reverse
  edge control;
- four-point determinant/divided-difference controls for two-, three-
  and four-atom real Stieltjes models on three fixed quadruples;
- a nonreal conjugate-pair negative-dispersion control, retained as a
  failure when no far reserve is supplied.

The companion producer must freshly rebuild the complete finite design,
with strict type/cap/source/artifact seals. It does not machine-prove the
infinite analytic argument or revalidate the imported published census.

## 2. Squared poles, convergence and the dispersion identity

For each DISTINCT nontrivial zero in the upper half-plane, write its
real offset and height as a_i,b_i, where |a_i|<1/2 and b_i>0, and its
positive integer multiplicity as m_i. Set

\[
 s_i=b_i^2-a_i^2+2ia_i b_i,\qquad w_i=2m_i.
\]

The sign of the imaginary part selects the reflected upper zero; the
whole indexed collection is conjugation invariant. There is one index
for each distinct upper zero, not one index per quartet. The even
Hadamard product, with its constant fixed at x=0, gives

\[
 p(t)=\sum_i\frac{w_i}{t+s_i}.                       \tag{FR2}
\]

Every nonreal s_i has b_i>H. A real s_i is b_i^2>0; a nonreal one has
Re s_i=b_i^2-a_i^2>0. Since |s_i|=b_i^2+a_i^2 and N(T)=O(T log T),
sum_i w_i/|s_i| is finite. Thus FR2 and every derivative used below
converge absolutely and locally uniformly on t>0. Multiplication by t
and termwise differentiation are legitimate. No genus correction or
linear term is missing: the paired product is even and xi has order one.

For q=0 use f=p and r_i=w_i; for q=1 use f=t p and r_i=w_i s_i.
Define S_k=sum_i r_i/(t+s_i)^k, k=2,3,4. For q=0,
(f',f'',f''')=(-S_2,2S_3,-6S_4), and for q=1 these three signs reverse.
It follows that

\[
 2f'f'''-3(f'')^2
 =12\sum_{i<j}w_iw_j\operatorname{Re}
 \frac{(s_i s_j)^q(s_i-s_j)^2}
 {(t+s_i)^4(t+s_j)^4}.                              \tag{FR3}
\]

To justify both the algebra and the infinite rearrangement, each
sum_i |r_i|/|t+s_i|^k is finite. Also
|s_i-s_j|^2 <= 2(|t+s_i|^2+|t+s_j|^2), so the absolute double series
is bounded by products of these convergent sums. The ordered identity
has coefficient 6; passing to unordered pairs gives 12. Its total is
real by conjugation invariance, which permits termwise real parts.

Neither derivative vanishes. For p, every real pole contributes a
negative derivative, and a conjugate pair has Re (t+s)^(-2)>0 because
|arg s| <= 4/(3H). Hence p'<0. For t p, a conjugate pair contributes
Re s/(t+s)^2>0: arg(t+s) lies between 0 and arg s, so the absolute
phase of s/(t+s)^2 is at most |arg s|<pi/2. Thus (t p)'>0.

## 3. Quantitative zero counts, including endpoints

Let N(T) count upper zeros with multiplicities. The imported estimate is

\[
 |N(T)-L(T)|\le .137\log T+.443\log\log T+1.588,
 \quad L(T)=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right)+\frac78.
                                                               \tag{FR4}
\]

We invoke this estimate only for T>=H; no estimate below T>=2000 is
required.  For T>=2000,
the right side is less than 2 log T. This weakening follows from
log log T <= log T and 1.588<log T. If a counting convention assigns a
midpoint at a zero, take left/right limits from nonzero heights; the
continuous bound holds for both and supplies the inclusive convention.

For B>=H, differentiating L and using pi>2 gives

\[
 W_B:=\sum_{|b_j-B|<2}w_j
 \le 2\{N(B+2)-N(B-2)\}<16\log(B+3).                \tag{FR5}
\]

Indeed the main-term difference is at most (2/pi)log(B+2), and the two
error terms total at most 4log(B+2); twice this is <10log(B+3).
All zeros at any repeated height and their full multiplicities are counted.

There is at least one upper zero, not necessarily critical, with

\[
                    2B<b_j\le 3B.                  \tag{FR6}
\]

For B>=H, pi<4 and B>=48 give

\[
 L(3B)-L(2B)\ge\frac B8\log(B/4)
 \ge\frac B{16}\log(3B),
\]

whereas the two errors total at most 4log(3B). The resulting count
difference is positive since B>64. This is the only anchor-existence
input. Riemann--von Mangoldt alone does NOT produce a critical-line
anchor; a proposed proof requiring such an anchor would have an unpaid
gap. The present phase argument deliberately permits complex anchors.

## 4. Only height-near pairs can be negative

Call the individual summand, including 12 w_i w_j, in FR3 C_ij(t,q).
Real-real pairs are nonnegative. Suppose at least one pole is nonreal,
and order heights B=b_i<C=b_j with C-B>=2. Put U=B+C>H. Then

\[
 |\operatorname{Re}(s_j-s_i)|\ge 2U-1/4,
 \qquad |\operatorname{Im}(s_j-s_i)|\le U.
\]

Thus the phase of (s_i-s_j)^2, modulo 2pi, has absolute value at most
2 arctan(3/5)<6/5. (U/(2U-1/4)<=3/5 for U>=1.) Each nonreal pole
has |arg s|<=4/(3H), and |arg(t+s)|<=|arg s|; real poles have phase
zero even if their height is small. All weight/denominator phases add
at most 40/(3H)<1/10. The total phase is therefore less than 13/10,
which is less than pi/2 since pi>3. Hence C_ij(t,q)>0.

Every negative pair therefore has |b_i-b_j|<2 and at least one nonreal
endpoint. This statement is uniform for t>1/4 and both q, not merely
an asymptotic statement at fixed t.

## 5. A complete local negative-row budget

Fix a nonreal i and put B=b_i>H and A=t+B^2. If |b_j-B|<2 then,
using B>=5 and |a|<=1/2,

\[
 |t+s_i|\ge\tfrac34 A,\quad |t+s_j|\ge\tfrac3{16}A,
 \quad |s_i-s_j|^2\le32B^2,\quad |s_i s_j|\le6B^4.    \tag{FR7}
\]

For example, b_j>=B/2, Re s_j>=3b_j^2/4; the real difference is at
most 4B+17/4<=5B and the imaginary difference at most 2B+2<=5B/2.
The modulus formula |s|=b^2+a^2 gives the last bound. Consequently the
sum of ABSOLUTE values in this whole local row is bounded by

\[
 N_i(t,q):=2^{28}w_i\frac{B^{4q+2}\log(B+3)}{A^8}.   \tag{FR8}
\]

Indeed the exact sufficient coefficient is
12*32*6^q*(64/9)^4*16, which is less than 2^28 for q=0,1.
This deliberately includes local positive pairs and may charge a
negative nonreal--nonreal pair twice. Overcounting negative cost is safe.
There is no assumption that the off-line zeros are simple or separated.

## 6. A positive far edge, even when both poles are complex

For this i choose any index j(i) furnished by FR6, so C=b_j lies in
(2B,3B]. Then

\[
 |s_i s_j|\ge2B^4,\quad |s_i-s_j|^2\ge7B^4,
 \quad |t+s_i|\le2A,\quad |t+s_j|\le12A.             \tag{FR9}
\]

Here Re s_i>=3B^2/4, Re s_j>=15B^2/4, and
Re(s_j-s_i)>=3B^2-1/4>=11B^2/4. For the upper bounds use
|s_i|<=B^2+1/4 and |s_j|<=9B^2+1/4.

The sum of absolute pole phases is at most 2/B. The difference phase
obeys

\[
 |\arg(s_j-s_i)|\le
 \frac{B+C}{(C-B)(B+C)-1/4}\le\frac4{3B}.
\]

Thus the total phase of the fraction in FR3 is at most
2/B+8/B+8/(3B)=38/(3B)<13/B<1. Its real part is more than half its
modulus, since cos(theta)>=1-theta^2/2 for |theta|<1. As w_j>=2,

\[
 C_{i,j(i)}(t,q)\ge P_i(t,q):=
 2^{-12}w_i\frac{B^{4q+4}}{A^8}.                    \tag{FR10}
\]

The exact sufficient coefficient is 84*2^q/24^4, which exceeds 2^-12.
Most importantly,

\[
 P_i(t,q)>N_i(t,q),\qquad
 B^2>2^{40}\log(B+3),\quad B>=H.                    \tag{FR11}
\]

The function B^2/log(B+3) is increasing for B>=1: its derivative has
the sign of 2log(B+3)-B/(B+3)>0. At H, log(H+3)<64 because
H+3<2^64 and log 2<1, and the integer inequality H^2>2^46 supplies
FR11. No floating-point logarithm or sampled asymptotic is used.

## 7. Disjoint unordered edges and the infinite sum

Enumerate the distinct upper zeros once. For each nonreal index choose,
for definiteness, the first available j(i) in FR6. The selected UNORDERED
pairs {i,j(i)} are all distinct. Equality for two different lower indices
would force the reverse assignment j(i)=k, j(k)=i, which is impossible
because each chosen upper height is more than twice the lower one.
Many lower indices may share one upper anchor. That is harmless: the
terms {i,j} and {k,j} are different terms of FR3, with their exact
weights w_i w_j and w_k w_j. No single pair or scalar reserve is reused.

Every selected edge is positive by section 6 and has height gap >H,
so it never belongs to the local negative rows. Every negative edge
has a nonreal endpoint by section 4 and is paid for by at least one
row in section 5. Hence the total negative magnitude is at most
sum_nonreal_i N_i, while distinct selected positive edges contribute
at least sum_nonreal_i P_i. All of these series converge; this follows
either from FR3's absolute convergence for actual edge sums or directly
from N(T)=O(TlogT) for the explicit bounds. Partition the full absolutely
convergent series, or first compensate a finite set of negative rows
with ALL their selected anchors and then pass to the limit. Do not
truncate anchors at the same height as their lower rows.

If any nonreal pole exists, FR11 makes FR3 strictly positive. If none
exists, every summand is nonnegative and two distinct positive real
poles give a strictly positive summand. There are infinitely many
distinct zeros by FR4 and discreteness, so such two poles exist.
Therefore

\[
 S f=\frac{f'''}{f'}-\frac32\left(\frac{f''}{f'}\right)^2>0
 \quad\hbox{for }f=p,\ tp,\quad t>1/4.               \tag{FR12}
\]

This use of an expanding far reserve is different from spending a
single fixed critical orbit against an entire tail. A critical-anchor
variant is explicitly not justified by FR4 and is not used here.

## 8. Positive Schwarzian gives the exact four-point signs

We prove the needed real-variable lemma rather than infer separated
node signs from an infinitesimal determinant without a bridge.

Let f be C^3 on an interval, f' nowhere zero, and Sf>0. For four ordered
points t_1<t_2<t_3<t_4 define

\[
 A_f=\det[1,t_i,f(t_i),t_i f(t_i)]_{i=1}^4.
\]

It cannot vanish. Otherwise a nonzero relation
a+b t_i+(c+d t_i)f(t_i)=0 produces a real fractional-linear interpolant
M(t)=-(a+bt)/(c+dt). Its denominator cannot vanish at a node: if it did,
both affine terms would vanish there, making f constant at the other
three nodes, contrary to strict monotonicity. The interpolant is
nondegenerate for the same reason. Replace f by -f if necessary, which
changes neither Sf nor A_f, so f is increasing.

M must have positive orientation. With negative orientation it decreases
on each side of its single pole, and at least two of the four nodes lie
on the same side. With positive orientation a pole between the first
and last nodes makes every value on its left greater than every value
on its right; this again contradicts the ordered interpolated values.
Thus M is increasing without a pole on [t_1,t_4]. Its inverse is defined
on [f(t_1),f(t_4)], so g=M^(-1) composed with f is increasing on this
interval, fixes all four t_i, and Sg=Sf>0.

Put v=1/sqrt(g'). Direct differentiation gives v''=-(Sg)v/2<0.
The mean-value theorem gives one point in each of the three consecutive
gaps with g'=1, hence three ordered points where v=1. This contradicts
strict concavity. Therefore A_f is nonzero on the connected domain of
ordered quadruples. Its sign follows by bringing the four nodes to a
common point:

\[
 \frac{A_f}{\prod_{i<j}(t_j-t_i)}\longrightarrow
 \frac{(f'')^2}{4}-\frac{f'f'''}6
 =-\frac{(f')^2 Sf}{6}<0.                            \tag{FR13}
\]

The limit is the standard Taylor divided-difference limit and uses only
C^3 regularity. Thus A_f<0 for every ordered quadruple.

Apply this lemma to p and t p, whose derivative signs and Schwarzians
were established above. SP16 gives, with t_i=x_i^2,

\[
 \det H=
 \frac{\det[1,t_i,p(t_i),t_i p(t_i)]\,
       \det[1,t_i,t_i p(t_i),t_i^2p(t_i)]}
      {\prod_{i<j}(x_i+x_j)^2}>0.                    \tag{FR14}
\]

Every proper principal minor is nonnegative by the repaired canonical
order-three theorem. The principal-minor characterization of PSD and
the positive determinant therefore give positive definiteness. Any
set of fewer than four distinct safe nodes can be extended to four,
so its matrix is a positive-definite principal submatrix. Repeated
nodes are obtained by duplication or continuity and yield only PSD.

## 9. Scope, novelty and proof/computation boundary

This is an all-safe-node theorem at a FIXED order, not finite sampled
positivity, a uniform bound in matrix size, or progress through every
order. It neither proves source A_Phi PSD nor closability of SP's
prime-core operator. Those remain RH-equivalent all-order conditions.
No physical capture, generalized L-family, or native-decoder conclusion
is drawn. The existing order-three repairs remain explicit dependencies.

The imported numerical theorem is a published proof-qualified zero
verification, not an unbounded-tail survey inferred from new finite
data. The new tail argument is analytic and pays all possible off-line
zeros, including multiplicities, using only their strip locations and
the explicit total counting law. The finite controls are regression and
arithmetic checks, not a replacement for sections 2--8 or the imported
theorems. External novelty has not been established.

Primary sources: [Platt--Trudgian](https://arxiv.org/abs/2004.09765),
[Faber--Kadiri, Theorem 1.5](https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Sept2013.pdf),
and their [corrigendum](https://www.cs.uleth.ca/~kadiri/articles/New-Bounds-for-Psi-Math-Comp-Faber-Corrigendum-Nov2017.pdf).
The companion manifest records the exact inspected PDF byte hashes,
but its offline producer does not download or independently authenticate
the mathematical content of those external publications.
