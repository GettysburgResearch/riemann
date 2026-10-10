# Mixed integer replications of cubic pair polynomials

Status: a further component theorem for the actual finite-order inverse
family. It improves the explicit sixth-moment triangle exponent from
119/160 to 863/1200 under precisely the same pointwise and native second
moment premises. It uses no native moment above order two. No full sixth
moment, generalized diagonal hierarchy, or zero-free conclusion is claimed.

This is an addendum to HIGHER_CUBIC_POOLS.md. Its exact mathematical
dependency is the frozen file pass2_higher_balanced_cubic_pools.md,
SHA-256 622cf846a961aed28ac0363f91766045f328c99700931621f123c17347c6bc23.
In particular it uses that file's Lemma 2.1, mixed forward correction
(3.3)-(3.4), and exact one-sided incidence definitions (4.1)-(4.7).
The source file is not modified by this addendum.

The underlying all-row cubic input is PR #917, commit
6b4723042b3d250024eef45cb1924f88f28e902c,
standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/OSCILLATING_OVERLAPS.md,
Git blob aa3137869abcee4b380bb0b621e56e93e2072d71, Theorem 2.1.
Its primary squarefree input is Blomer, Goldmakher and Louvel,
L-functions with n-th order twists, arXiv:1112.1650v1, Theorem 1.3.
The extension to all element rows and its literal cube masks are reproved
in Section 2 of HIGHER_CUBIC_POOLS.md.

The finite-order pointwise and native second moment premises remain
those stated separately in Section 1 of HIGHER_CUBIC_POOLS.md, with the
source pins there. In particular the beta=7/8 example below is conditional
on the stated uniform reciprocal/zero-free premise, and on the separately
inherited native second moment at the stated row height.

## 1. Data and the physical cubic norm

Write beta for the pointwise exponent, with 1/2<beta<=1, and put

\[
a=2\beta-1.
\tag{1.1}
\]

All moment orders, replication degrees, test functions, finite character
data, and polynomial conductor exponents in this note are fixed
independently of D. Every character has its literal nonunit zero. Every
row norm is over all nonzero Eisenstein elements u with Nu<=H, including
all units and all repeated prime powers. A moving excluded column ideal
has polynomial norm in D and is retained exactly.

The native inverse factors satisfy, in the precise domains stated in the
parent file,

\[
\|A(Y;V)\|_\infty\ll D^\epsilon Y^\beta\|V\|_{C^{J_\beta}},
\qquad
\|A(Y;V)\|_{2,H}^2\ll D^\epsilon HY\|V\|_{C^J}^2.
\tag{1.2}
\]

The second bound is a native coefficient estimate, not an arbitrary
coefficient sieve. Both are required at every nonempty smaller scale.
The first is ideal counting when beta=1; its stronger specializations
are explicitly additional premises.

Let s>=1 be fixed. For j=1,...,s let U_j be a physical cubic polynomial

\[
U_j(u)=
\sum_{\substack{n\ {\rm squarefree}\\(n,S)=1}}
\lambda_j(n)\chi_n(u)^2\,V_j(Nn/R_j),
\tag{1.3}
\]

with fixed finite-order coefficient data of modulus at most one,
R_j a nonempty polynomial scale, and V_j a bounded compactly supported
test. The actual pair polynomial has
lambda_j(n)=nu(n)^2 and the squarefree coefficient mu(n)^2.
Arbitrary fixed row-independent moving masks may be included in the
classical column coefficients. Hard dyadic endpoints on these positive
squarefree cubic factors are allowed. Conjugating every row power from
two to four gives the same assertions.

The word physical means literal multiplication of the finite sums in
(1.3). Independent factors may share primes after the exact original
coprimality has been removed by the forward correction. Such collisions
are not discarded.

For every fixed nonnegative integer vector e=(e_1,...,e_s) with positive
total degree and

\[
P_e(u)=\prod_{j=1}^s U_j(u)^{e_j},
\qquad
M_e=\prod_{j=1}^s R_j^{e_j},
\tag{1.4}
\]

Lemma 2.1 of the parent file gives

\[
\boxed{
\|P_e\|_{2,H}^2
\ll D^\epsilon
\left[HM_e+H^{1/3}M_e^2+H^{2/3}M_e^{5/3}\right].
}
\tag{1.5}
\]

The degree in (1.4) counts actual integer copies of the physical
polynomials. To recall why (1.5) is available, incidence-decompose all
these squarefree copies, freeze their repeated-prime ideals, and group
the residual disjoint singleton product into one squarefree column.
Its squared coefficient mass is bounded by its product scale times
D^epsilon, by fixed-order divisor counting. Apply the all-row cubic
sieve to that column. After taking square roots, the three product-scale
weights are 1/2, 1, and 5/6. Summing the repeated ideals costs only pair
harmonic logarithms in the first term; the higher-incidence sums converge.
This proves (1.5) with every collision, row mask, and row class present.
It invokes no native higher inverse moment.

Define

\[
\rho(H,M)=M^{-1}+H^{-2/3}+H^{-1/3}M^{-1/3}.
\tag{1.6}
\]

Thus the right side of (1.5) is D^epsilon H M_e^2 rho(H,M_e).

## 2. A mixed-replication Holder inequality

Choose fixed nonnegative integers m_1,...,m_s with

\[
d=\sum_{j=1}^s m_j\ge s.
\tag{2.1}
\]

Use cyclic indices modulo s. For t=0,...,s-1 put

\[
P_t(u)=\prod_{j=1}^sU_j(u)^{m_{j+t}},
\qquad
M_t=\prod_{j=1}^sR_j^{m_{j+t}},
\qquad
U(u)=\prod_{j=1}^sU_j(u),\quad R=\prod_{j=1}^sR_j.
\tag{2.2}
\]

Then the following identities are literal, including at zero values:

\[
\prod_{t=0}^{s-1}P_t=U^d,\qquad
\prod_{t=0}^{s-1}M_t=R^d.
\tag{2.3}
\]

### Lemma 2.1. A rational moment from integer physical products

\[
\boxed{
\|U\|_{2d/s,H}
\le\prod_{t=0}^{s-1}\|P_t\|_{2,H}^{1/d}.
}
\tag{2.4}
\]

Consequently

\[
\boxed{
\|U\|_{2d/s,H}^2
\ll D^\epsilon H^{s/d}R^2
\prod_{t=0}^{s-1}\rho(H,M_t)^{1/d}.
}
\tag{2.5}
\]

**Proof.** Equation (2.3) gives
|U|^(2d/s)=product_t |P_t|^(2/s).
Apply Holder with s equal exponents to this finite nonnegative row sum,
then take the power s/(2d):

\[
\left(\sum_u|U(u)|^{2d/s}\right)^{s/(2d)}
\le
\prod_t\left(\sum_u|P_t(u)|^2\right)^{1/(2d)}.
\]

This is (2.4). Apply (1.5) to each integer product and use the second
identity in (2.3). The constants depend on the fixed degree d, never on
a degree growing with D. QED.

If all pair scales equal R_0, then M_t=R_0^d=R^(d/s) for every t.
In this special case (2.5) has exactly the shape

\[
\|U\|_{2q,H}^2
\ll D^\epsilon H^{1/q}R^2
\rho_q(H,R)^{1/q},
\qquad q=d/s,
\tag{2.6}
\]

where rho_q(H,R)=R^(-q)+H^(-2/3)+H^(-1/3)R^(-q/3).
Thus rational q on the fixed d/s grid is available for equal scales.
The proof of the general unequal-scale formula (2.5) comes first;
equal original scales are never imposed on shifted correction scales.

## 3. Exact incidence theorem with unequal pair scales

Fix k>=2 and retain the full one-sided incidence portion from
HIGHER_CUBIC_POOLS.md. There are s=k(k-1)/2 pair axes, in any fixed order.
Freeze precisely the higher incidence ideals c_I, |I|>=3, and put

\[
T=\prod_{|I|\ge3}(Nc_I)^{|I|},\quad
M_i^{\rm high}=\prod_{\substack{I\ni i\\|I|\ge3}}c_I.
\tag{3.1}
\]

Choose complete hard dyads R_j on the pair axes. Set

\[
R=\prod_{j=1}^sR_j,\qquad
X_i=\frac{D}{NM_i^{\rm high}
 \prod_{\text{pair }j\ni i}R_j},\qquad
X=\prod_{i=1}^kX_i.
\tag{3.2}
\]

As before,

\[
R^2XT=D^k.
\tag{3.3}
\]

Let F_(c,R) be the exact complete incidence portion. The singleton
coefficients are mu times nu times the sextic row character, while
the pair coefficients are mu squared times nu squared times the
cubic row character. All the varying axes remain mutually coprime,
and they avoid the frozen higher-prime product and every explicitly
specified moving exclusion.

### Theorem 3.1. Mixed-replication incidence estimate

Let m and d be fixed as in (2.1), and define the unequal scales M_t
by (2.2). For any native singleton axis i,

\[
\boxed{
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll D^\epsilon H D^k T^{-1}
X^a X_i^{-a(1-s/d)}
\prod_{t=0}^{s-1}\rho(H,M_t)^{1/d}.
}
\tag{3.4}
\]

When d>s this uses exactly the two premises (1.2) and the classical
cubic input. When d=s, the chosen native factor is in L-infinity and
the native second moment is unnecessary. Every statement remains at
the source's allowed physical row height and every permitted smaller
column scale. The best chosen axis in (3.4) has the largest X_i.

**Proof before the correction.** If d>s, set

\[
p=\frac{2d}{d-s}.
\tag{3.5}
\]

Native interpolation between L2 and the pointwise bound gives

\[
\|A_i(Y)\|_{p,H}
\ll D^\epsilon
H^{(d-s)/(2d)}
Y^{1/2+as/(2d)}.
\tag{3.6}
\]

Indeed 2/p=(d-s)/d, and the Y exponent is
(2/p)/2+beta(1-2/p)=1/2+as/(2d).
The reciprocal exponents in Holder are

\[
\frac1p+\frac{s}{2d}=\frac12.
\tag{3.7}
\]

Bound all other singleton factors by their pointwise estimates and use
(2.4) for the physical cubic product. At d=s interpret p as infinity;
the same formulas and exponent identity remain valid.

**Coupled tests.** Mellin-separate the original fixed W_i exactly as
in the parent file. Each singleton retains a fixed smooth cutoff
on its forced compact support, with finite seminorm growing only
polynomially in the Mellin frequencies. Each pair has a bounded
hard dyadic test, which needs no derivatives in (1.5). All copies
in P_t are copies of these actual separated tests. Rapid Mellin
decay integrates every fixed seminorm loss.

**Exact varying coprimality.** Use the mixed forward correction on
all singleton and pair axes before applying the preceding norm bound.
At a prime outside the moving exclusion its local quotient is

\[
\frac{1+\sum_j \sigma_j z_j}{\prod_j(1+\sigma_j z_j)},
\qquad
\sigma_j=-1\text{ on singletons},\quad
\sigma_j=+1\text{ on pairs}.
\tag{3.8}
\]

At an excluded prime only the inverse denominator remains.
A monomial supported on I has coefficient
(1-|I|) product_j (-sigma_j)^(e_j).
There are no one-axis terms outside the exclusion. Its finite-horizon
absolute coefficient sum is D^epsilon at every vector of weights
at least 1/2, as proved in the parent file. The literal row phases
remain attached to the correction monomials and are zero at
nonunits.

Fix one correction vector. The singleton scales become
X_l/Nd_l and the pair scales become R_j/Nd_j. These shortened pair
scales can be unequal even when all original R_j agree. Apply the
unequal formula (2.4) at these actual shortened scales.

Expand each of the s cubic norm bounds into its three monomial terms.
There are only 3^s choices. Write alpha_t in {1/2,1,5/6} for the
product-scale exponent in the t-th cubic norm term. The weight of the
j-th pair correction ideal is then exactly

\[
w_j=\frac1d\sum_{t=0}^{s-1}m_{j+t}\alpha_t
\ge\frac1{2d}\sum_t m_{j+t}=\frac12.
\tag{3.9}
\]

The selected singleton has weight 1/2+as/(2d), and all other
singletons have weight beta. Therefore every term is eligible for
the same exact mixed correction estimate. Moving exclusions have
polynomial norm, every nonempty shortened scale is covered by the
declared inputs, and the finite number of choices is absorbed into
the constant. The correction can thus be summed before squaring,
by Minkowski, with only D^epsilon loss.

Undoing the finite expansion returns the unshifted product of cubic
brackets. The native height exponent (d-s)/(2d) and the total cubic
height exponent s/(2d) sum to 1/2. At the squared level the result is

\[
D^\epsilon H\,X^{2\beta}R^2
 X_i^{-a(1-s/d)}
\prod_t\rho(H,M_t)^{1/d}.
\tag{3.10}
\]

Finally substitute X^(2 beta)R^2=D^k T^(-1)X^a using (3.3).
This proves (3.4), including the unequal shifts, every variable
coprimality condition, and every nonzero row. QED.

## 4. The strict sixth-moment improvement

Take k=3, no triple incidence ideal, and all three pair dyads of
scale D^r up to fixed constants. Thus

\[
s=3,\quad T=1,\quad
X_1\asymp X_2\asymp X_3\asymp D^{1-2r},
\quad R\asymp D^{3r}.
\tag{4.1}
\]

Choose

\[
(m_1,m_2,m_3)=(1,2,2),\qquad d=5,\qquad q=d/s=5/3.
\tag{4.2}
\]

The three integer products are

\[
P_1=U_1U_2^2U_3^2,\qquad
P_2=U_1^2U_2U_3^2,\qquad
P_3=U_1^2U_2^2U_3.
\tag{4.3}
\]

Each is a genuine five-factor physical cubic product. Their product
is (U_1U_2U_3)^5, so the selected native singleton uses L5 and the
pair product uses L^(10/3). The three remaining norm estimates are
ordinary L2 instances of the classical physical cubic lemma.

Now specialize to the example from PR #923 and the parent file:

\[
H=D^{21/20},\qquad
\beta=7/8,\quad a=3/4,\qquad
r=5/24,\quad X_i\asymp D^{7/12},\quad X\asymp D^{7/4}.
\tag{4.4}
\]

All three M_t have scale D^(25/24). The exponents in their common
rho bracket are

\[
-\frac{25}{24},\qquad -\frac7{10},\qquad
-\frac7{20}-\frac{25}{72}=-\frac{251}{360}.
\tag{4.5}
\]

The last term is largest, by 1/360 over the middle term. Consequently
(3.4) gives the exact excess calculation

\[
\frac{21}{16}-\frac{7}{40}-\frac{251}{600}
=\frac{863}{1200}.
\tag{4.6}
\]

### Corollary 4.1. A stronger complete triangle estimate

Under the same two explicitly stated native premises as the
119/160 estimate in HIGHER_CUBIC_POOLS.md,

\[
\boxed{
\|F_\triangle\|_{2,H}^2
\ll_\epsilon
H D^{3+863/1200+\epsilon}.
}
\tag{4.7}
\]

The difference from the previous exponent is

\[
\frac{119}{160}-\frac{863}{1200}=\frac{59}{2400}>0.
\tag{4.8}
\]

The improvement over PR #923's 623/720 triangle excess is

\[
\frac{623}{720}-\frac{863}{1200}=\frac{263}{1800}>0.
\tag{4.9}
\]

This is an estimate for the full one-sided triangle portion and its
entire squared row norm, including every overlap between the two
Hermitian copies. It is not a sixth native inverse moment premise.
The surviving excess 863/1200 is positive, so (4.7) is not the full
diagonal-size sixth moment.

## 5. Why scalar interpolation missed this gain

For a fixed full product U=product U_j, interpolation between its
integer L^(2n) and L^(2n+2) bounds alone does not improve the best
complete endpoint hybrid cost. In reciprocal exponent 1/q, both
the cubic norm interpolation and the selected native interpolation
are affine. The resulting squared cost is a geometric mean of the
two complete endpoint costs and is at least their minimum.

The argument above uses three different five-factor monomials before
Holder is applied. They are not integer powers of the full U. That
additional collection of available classical norms is what provides
q=5/3.

A direct formal substitution of a general real q into the integer
rho_q theorem would be unsupported. In (4.4), that formal formula is
minimized at q=42/25 and would give excess 23/32, but the interpolation
argument alone does not establish that value. The proved excess is

\[
\frac{863}{1200}-\frac{23}{32}=\frac1{2400}
\tag{5.1}
\]

above the formal value.

One can also locate the exact power-exponent optimum of direct
monomial Holder bounds at this triangle. Suppose the ingredients
are the physical cubic L2 estimates (1.5) for any fixed integer
monomials, cubic pointwise counting if desired, and interpolation
of the native second moments with (1.2). No other analytic input
or row partition is allowed in this comparison.

For a degree n integer monomial, equal pair scales make its rho
exponent depend only on n:

\[
\delta_n=
\max\left\{-\frac{5n}{24},-\frac7{10},
 -\frac7{20}-\frac{5n}{72}\right\}.
\tag{5.2}
\]

The algebraic cost associated with total replication n is

\[
E_n=\frac78+\frac3n\left(\frac7{16}+\delta_n\right).
\tag{5.3}
\]

For n=1,2 these are algebraic terms in a mixed Holder allocation,
not standalone claims using an inadmissible native exponent.
Explicitly,

\[
E_n=
\begin{cases}
\displaystyle\frac14+\frac{21}{16n},&n=1,2,\\[2mm]
\displaystyle\frac23+\frac{21}{80n},&n=3,4,5,\\[2mm]
\displaystyle\frac78-\frac{63}{80n},&n\ge6.
\end{cases}
\tag{5.4}
\]

The minimum over all positive integers is E_5=863/1200.

To justify this comparison, let t_e>=0 be the exponents of monomial
norm factors in a Holder bound. Each pair variable requires
sum_e t_e e_j=1, or at most one if its remainder is bounded by its
pointwise count. Thus sum_e t_e |e|<=3. The available native
interpolation saving uses the remaining Holder budget and, because
all three singleton scales are equal, depends only on
sum_e t_e. The resulting excess is the convex combination

\[
\sum_e\frac{t_e|e|}{3}E_{|e|}
+\left(1-\sum_e\frac{t_e|e|}{3}\right)\frac78.
\tag{5.5}
\]

A degree-zero row factor only adds a nonnegative loss and may be
omitted. Equation (5.5) proves that no direct bound in this stated
monomial Holder class improves E_5. It does not rule out a new
analytic treatment, a different incidence organization, or a row
partition with additional information.

## 6. General-order and Hermitian uses

For any fixed s and d>=s, choose a fixed integer vector of total d.
The cyclic construction gives the rational grid q=d/s when the
s pair scales agree. Balanced entries floor(d/s) and ceil(d/s)
are one convenient choice; the proof permits any fixed entries.
For unequal scales the product of the s separate rho(H,M_t)
factors in (3.4) is the applicable bound.

The new costs can be added to the parent's complete-portion selector.
Choose a finite set of replication vectors independently of D.
Select complete incidence portions for which the minimum of their
old costs and the new costs is at most L_0. Summing their norms gives

\[
\|G_{L_0}\|_{2,H}^2
\ll D^\epsilon H D^k L_0.
\tag{6.1}
\]

Indeed pair dyads have only a fixed logarithmic multiplicity, and
the frozen higher ideals contribute the convergent exterior sum
product_{m=3}^k zeta_K(m/2)^(binom(k,m)) through T^(-1/2).
The selector is constant on each complete portion and never deletes
native terms inside a signed inverse polynomial.

There is also a direct Hermitian version. In the notation and exact
signed incidence decomposition of Proposition 7.1 of the parent
file, choose two native-eligible odd axes J and L. Choose a group
of s even axes whose row exponents are all two modulo six, or all
four modulo six. Denote their scale product by R and form their
M_t as in (2.2). Every other odd axis has pointwise exponent beta,
and every other even axis is bounded by counting. Then

\[
\boxed{
|\mathcal S_{\mathbf Q}|
\ll D^\epsilon H
Q_J^{1/2}Q_L^{1/2+as/(2d)}
R\prod_t\rho(H,M_t)^{1/(2d)}
\prod_{\substack{I\ {\rm odd}\\I\ne J,L}}Q_I^\beta
\prod_{\substack{I\ {\rm even}\\I\ {\rm outside\ group}}}Q_I.
}
\tag{6.2}
\]

Use the native L2 norm on J, native Lp on L with p=2d/(d-s),
and (2.4) on the cubic group. Their reciprocal exponents add to one.
The same weights (3.9), the exact mixed correction, and the coupled
test argument prove the formula. Relative to the parent's two-native
bound, the new factor is

\[
\left[Q_L^{as}\prod_t\rho(H,M_t)\right]^{1/(2d)}.
\tag{6.3}
\]

This version does not mix opposite cubic orientations inside one
physical product, and it does not assert a third full native L2
saving.

## 7. Schwartz rows and remaining scope

For a fixed Schwartz row weight, use the same annular reference-scale
adapter as Section 8 of the parent file. At H_j=2^j H, use the source
uniform inputs at the enlarged reference scale, keeping the original
column scales, incidence dyads, selectors, and moving exclusions fixed.

In the squared monomial expansion of the proof, the height exponent is

\[
1-\frac{s}{d}+\frac1d\sum_t\tau_t,\qquad
\tau_t\in\{1,1/3,2/3\}.
\tag{7.1}
\]

It is at most one. The subpower reference loss and every row annulus
are therefore absorbed by a fixed Schwartz decay power. This proves
the same bounds for the fixed weighted norm and retains every
nonzero element row.

The all-singleton balanced core still has R_j=1 and M_t=1. Since
rho(H,1)>=1, the new cost is at least
X^a X_i^(-a(1-s/d)), and the original full native second-moment
option X^a X_i^(-a) is no worse there. Thus the present advance
strictly strengthens a genuine higher-overlap sector and the
corresponding general selector. It does not close the balanced
all-singleton core or the full moment hypothesis.

