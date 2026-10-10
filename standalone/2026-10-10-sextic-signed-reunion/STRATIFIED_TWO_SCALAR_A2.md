# Sixth-power stratification with both inverse scalar savings

**Status: proposed source-qualified component theorem.** The normalized raw
two-axis Gauss family and its complete arithmetic A2 correction both satisfy
the six-term estimate below. At the angular exponent 11/12, unit moving
labels and physical row height H equal to the square root of D, this gives
energy at most D to the power 89/55 plus epsilon. The signed native fourth
moment and the generalized moment hierarchy remain open.

This note combines the second scalar cancellation in this packet with the
sixth-power row stratification introduced in the adjacent PR #924. The full
A2 sum uses a new length-dependent cutoff chosen for the two-scalar powers.
It retains the precise original column exclusions and their overlaps.

## 1. Exact sources, objects, and premises

The mathematical dependencies are:

* [HYBRID_CUBE_INVERSE.md](HYBRID_CUBE_INVERSE.md), SHA-256
  d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a:
  the physical cube inverse, two scalar block factorization, smooth
  separation, and exact long-inverse regrouping.
* [MOVING_COLUMN_MASKS.md](MOVING_COLUMN_MASKS.md), SHA-256
  068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee:
  the local factorization with costs 1, J, K, including every physical row
  valuation and the moving exclusion in both scalar coefficients.
* [A2_MOVING_MEAN_SQUARE.md](A2_MOVING_MEAN_SQUARE.md), SHA-256
  6eed5695c672dab92620763f8df5b63f60dc416754367ed541cb854bf06854ba:
  the exact normalized A2 projection, child labels and tests.
* PR #924 at commit 725b2d25ab47e57500049d93985560098c7ef3fa,
  folder standalone/2026-10-10-sextic-moving-labels:
  SIXTH_POWER_STRATIFIED_INVERSE.md, Git blob
  004dd4a8de2237661235a9da460b3caab432ef53, SHA-256
  f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9;
  and ANISOTROPIC_A2_NORM_TRANSFER.md, Git blob
  1e4e8a9b70fb15ee42bc41abbcdc3b217e07f215, SHA-256
  e671b8b1c8717ed494b3db0ba39fb4c0de374aef56f774bf9a7ca68e01b277cf.
  These supply the adjacent stratification and positive-cutoff idea.
* PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1,
  REFINED_ALL_ROW_SIEVE.md, SHA-256
  6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8:
  the exact valuation blocks of the classical row sieve.
* PR #914, commit 0cc0428fedbbfc340044c7451b3d392c1da9a103,
  A2_COMPLETION.md, SHA-256
  d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad:
  the underlying five-label arithmetic A2 coefficient.

All theta, cusp and classical upper-sieve inputs of those notes remain
explicit premises. Fix \(1/2<\beta\le1\). Both actual angular scalar sums
in the cube inverse must satisfy the uniform exponent-beta estimate in
HYBRID_CUBE_INVERSE.md (1.2), with its fixed finite smooth seminorm and
moving-exclusion range. Counting supplies beta=1. The notation beta=11/12
uses the same imported angular/canonical premise and positive epsilon
margin as that proof. This note does not prove that upstream premise anew.
No native inverse moment of order greater than two, or arbitrary-coefficient
analogue of a structured theta estimate, is assumed.

Work over the Eisenstein field with the fixed source bad-prime set S,
primary generators and finite ray datum xi. Every residue symbol has its
literal zero on nonunits. Write
\[
\lambda(n)=\overline{\alpha(n)}\xi(n),\qquad
a_\xi(n)=\lambda(n)\gamma_2(n).
\]
For squarefree original labels \(q_0,f\), possibly overlapping, define
\[
P_{q_0}(A,B;k,f)=\frac1{\sqrt{AB}}
\sum_{\substack{an\ {\rm squarefree}\\(an,Sq_0)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
W_1(Na/A)W_2(Nn/B).
\tag{1.1}
\]
Let
\[
F=Nf,\quad Q=N(q_0/(q_0,f)),\quad
J=FQ,\quad K=F^{2/3}Q^{1/3}\le J^{2/3}.
\tag{1.2}
\]
The replacement of the exclusion by \(q_0/(q_0,f)\) is exact because the
f twist already supplies its nonunit zeros.

The reference D is at least two. The physical scales, row heights and
labels are bounded by a fixed power of D. Tests have fixed compact positive
norm support and a fixed finite smooth seminorm. A nonempty physical scale
below one has a fixed positive lower bound from the upper endpoint of its
test support. Replacing such a scale by one and rescaling the test has
uniformly bounded normalization and seminorm costs. An empty child is zero.
The free cutoff R may be any positive real; it is not a physical scale.
All row sums include all six units, repeated prime powers and allowed
bad-prime factors.

## 2. The sieve on sixth-power-free rows

For arbitrary coefficients on squarefree columns of norm at most L,
the classical valuation-block argument gives
\[
\sum_{\substack{0<Nk\le U\\k\ {\rm sixth\text{-}power\text{-}free}}}
\left|\sum_n z_n\chi_n(k)\right|^2
\ll (UL)^\epsilon
[U+L+(UL)^{2/3}]\sum_n|z_n|^2.
\tag{2.1}
\]
Sixth-power-free means that each valuation is at most five. It does not
mean squarefree and does not exclude the unit rows.

Here is the precise reduction from the pinned classical input. In a
valuation block let \(A_j\) be the norms of its five disjoint squarefree
labels, \(P_0=\prod_{j=1}^5 A_j\), \(M=\max_j A_j\), and
\(P=\prod_{j=1}^5 A_j^j\le U\). The two classical alternatives from PR #913
are, up to the stated small power,
\[
P_0+P_0L/M+P_0L^{2/3}/M^{1/3},
\qquad L+P_0^2.
\]
We have \(P_0\le U\), \(P_0^2/M\le U\), and
\(P_0/M^{1/3}\le U^{2/3}\). For the last two inequalities, take logarithms:
the only positive coefficient in the excess over the required weighted
sum is that of \(\log A_1\), and it is absorbed by \(\log M\). Hence
\[
\min(P_0L/M,P_0^2)
\le (P_0L/M)^{2/3}(P_0^2)^{1/3}
\le (UL)^{2/3}.
\]
Taking the better alternative, then summing the finitely many unit/bad-ray
classes and logarithmically many valuation blocks, proves (2.1).
Fixed row-independent column masks and twists are allowed in \(z_n\).
The ordinary primitive-character alternative in the named source already
retains those zeros; no contraction of a structured completed norm is used.

## 3. A two-scalar raw bound for every positive cutoff

Put
\[
p=\frac52-\beta.
\tag{3.1}
\]

### Theorem 3.1

For the literal family (1.1), for either prescribed orientation of A and B,
and every \(R>0\),
\[
\boxed{\begin{aligned}
\sum_{k\asymp H}|P_{q_0}(A,B;k,f)|^2
\ll D^\epsilon\big[&
HA+JH^2AB^{\beta-3/2}R^p
+KH^{4/3}A^{4/3}B^{-2/3}R^{2\beta}\\
&+H+ABR^{-3}+(HAB)^{2/3}R^{-2}\big].
\end{aligned}}
\tag{3.2}
\]
No assertion \(A\le B\) is needed in this oriented, possibly weaker bound.

#### 3.1. Smooth truncation and exact caps

Fix a smooth function omega between zero and one, equal to one on
\([0,1/2]\) and zero on \([1,\infty)\). This is a fixed dilation of the
cutoff used in the frozen hybrid proof. Multiplying each physical inverse
coefficient h by \(\omega(Nh/r)\) defines an exact short part at any
positive cutoff r. The complementary multiplier defines the long part.
If \(r\le1\), the short part is exactly empty.

Choose a fixed constant C, depending only on the test support, so that
every nonempty inverse index h and regrouped cube index d has norm at most
\(CB^{1/3}\). Enlarge C so this bound is at least one for every nonempty
original rectangle. At a cutoff \(r=2CB^{1/3}\) the multiplier is one on
the entire inverse support and the long part is exactly empty.

On each nonempty smooth h dyad \(Nh\asymp Z\), the factor
\(\omega((Z/r)(Nh/Z))\) has uniformly bounded rescaled derivatives.
Its nonempty support forces \(Z/r\) to be bounded. The common-divisor
shifts used to separate the two actual scalar sums preserve this ratio.
Thus the scalar seminorm constants do not acquire powers of r or 1/r.
If r is too small for a nonempty dyad, no scalar estimate is applied there.

#### 3.2. Why the short estimate permits either axis orientation

The frozen hybrid states its rectangular corollary after ordering the
axes for the best bound. Its proof also yields the displayed weaker
oriented estimate without ordering. At arbitrary positive A,B, its
physical block constraints and middle energy monomial are
\[
E F_1 G\asymp A,\quad Nh\asymp Z,\quad G^2Z^3\ll B,
\qquad
\frac{J U^2A}{BF_1^2}G^{2\beta-1}Z^{2\beta+1}.
\]
Here \(F_1\) is a positive allocation scale, not the auxiliary norm F.
Using \(G\ll\sqrt B Z^{-3/2}\) bounds this monomial by
\[
J U^2 A B^{\beta-3/2}Z^{5/2-\beta}.
\]
This inequality is valid whether A is smaller or larger than B; using an
upper bound for G that is larger than its outer support remains valid.
The other two block monomials are bounded by
\[
UA,\qquad K U^{4/3}A^{4/3}B^{-2/3}Z^{2\beta}.
\]
These follow from \(G^{2\beta-3}Z^{2\beta-2}\ll1\) and
\(G^{2\beta-2}\ll1\), with fixed constants on bounded nonempty scales.

The exact common-divisor norm weights for the two scalar cancellations
remain \(d_1^{-\beta-1/2}d_2^{-\beta-1/2}\ell^{-2\beta}\) in ideal norms.
Their sums converge for beta greater than one half. The remaining
positive factor may meet ell, as required by the exact identity.
The moving-mask local proof supplies J and K before the scalars are
estimated. Its excluded primes enter both scalars solely with their
proved masks and phases. No new inverse-index coefficient is put into
an arbitrary theta vector.

Summing the smooth blocks therefore gives
\[
\|S_r\|_{2,U}^2\ll D^\epsilon[
UA+JU^2AB^{\beta-3/2}r^p
+KU^{4/3}A^{4/3}B^{-2/3}r^{2\beta}]
\tag{3.3}
\]
for every positive r up to the physical cap. It is also a valid
nonnegative upper bound when its short part is empty.

#### 3.3. Partition the actual rows before estimating the long part

Every nonzero row has a unique representation
\[
k=\varepsilon v^6k_0,
\tag{3.4}
\]
where epsilon is a unit, v is an ideal, and \(k_0\) is sixth-power-free.
There is no condition \((v,k_0)=1\). Division of each valuation by six
gives existence and uniqueness in the fixed generator convention.

For fixed v, \(\chi_n(v^6)=\mathbf1_{(n,v)=1}\). Thus (3.4) inserts
the additional physical exclusion \({\rm rad}(v)\), including on the
cube index and inverse coefficient. After removing primes already
excluded by f or S, denote the effective label by \(q_v\). With V=Nv,
\[
Q_v\le QV,\quad J_v\le JV,\quad K_v\le KV^{1/3},
\qquad U_v\ll H/V^6.
\tag{3.5}
\]
Only \(V\ll H^{1/6}\) contribute. Nonempty annuli just below unit
height can be bounded at height one, a fixed multiple of \(H/V^6\).
The six unit twists remain in the declared finite ray family.

On this exact stratum choose
\[
r_v=\min(2CB^{1/3},RV).
\tag{3.6}
\]
Apply (3.3) to its short part, allowing all rows in that positive
norm. This is a legitimate enlargement of the sixth-power-free
row subset, with its fixed v mask retained.

For the long part expand the physical cube index b and put d=hb.
The coefficient is exactly
\[
c_{r_v}(d)=\sum_{h\mid d}\mu(h)[1-\omega(Nh/r_v)].
\tag{3.7}
\]
It vanishes if \(Nd\le r_v/2\), and its size is at most a fixed-order
divisor bound. Its raw child has inner scale \(B/(Nd)^3\), prefactor
1/Nd, the original masks on every physical factor, and the outer
mask \((a,d)=1\). The inner squarefree column may meet d. The ideal
d may have powers, and no condition \((h,b)=1\) is imposed.

Group the child's squarefree product an. Its normalized squared
coefficient mass is \(D^\epsilon\), by ideal counting and divisor
counting, uniformly in the fixed masks and twists. Apply (2.1) to
the actual \(k_0\) rows. This gives the child energy
\[
D^\epsilon[U_v+AB/(Nd)^3+(U_vAB)^{2/3}/(Nd)^2].
\]
The exterior d character is a contraction for each fixed d, with its
zero still present. Taking square roots, multiplying by 1/Nd and
summing d by Minkowski proves
\[
\|L_{r_v}\|_2^2\ll D^\epsilon[
U_v+ABr_v^{-3}+(U_vAB)^{2/3}r_v^{-2}].
\tag{3.8}
\]
The harmonic first sum ends at the physical support. The other two
ideal tails have powers \(-5/2\) and \(-2\). Their estimates by
\(r_v^{-3/2}\) and \(r_v^{-1}\) remain valid for \(0<r_v<1\), because
the corresponding sums starting at norm one are bounded. The fixed
factor one half in the support threshold changes only constants.
Capped strata have zero long contribution and are omitted from (3.8).

Finally, the physical v strata are disjoint, so their energies add.
For the short part use \(r_v\le RV\); for every uncapped long part
use \(r_v=RV\). The six powers of V are respectively
\[
-6,\quad -11+p=-17/2-\beta,\quad -23/3+2\beta,
\qquad -6,\quad -3,\quad -6.
\tag{3.9}
\]
All are strictly below minus one. Their ideal sums converge.
All source small-power losses are assigned a smaller preliminary
epsilon before summation. The squared triangle inequality then
proves (3.2), including both r-small and r-capped cases. QED.

## 4. The complete A2 correction has the same six terms

Let \(\mathscr Q_{q_0,f}(D,D;k)\) be the full normalized arithmetic A2
polynomial of the cited A2 note, with its fixed Gauss orientation.
Its local support has five disjoint squarefree labels
\[
n_1=a c d^2 e^2,\qquad n_2=b c^2 d e^2.
\tag{4.1}
\]
Write \(x=Nc,\ y=Nd,\ z=Ne\). The exact forward projection is
\[
\mathscr Q_{q_0,f}(D,D;k)
=\sum_{c,d,e}\frac{\omega_{c,d,e}(k,f)}{xyz^{3/2}}\,
P_{q_t}(A_t,B_t;k,f_t),\qquad |\omega_{c,d,e}(k,f)|\le1,
\tag{4.2}
\]
where the correction primes avoid \(Sq_0f\) and
\[
A_t=Dx^{-1}y^{-2}z^{-2},\quad
B_t=Dx^{-2}y^{-1}z^{-2},\quad
q_t=q_0cde,\quad f_t=fe.
\tag{4.3}
\]
For example the source phase is
\(\lambda(cde)^3a_\xi(e)\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f)^4\);
every one of its nonunit zeros is retained before using its modulus.
The normalization is exactly
\(\sqrt{N(cde)}\sqrt{A_tB_t/D^2}=1/(xyz^{3/2})\).

The effective child labels satisfy the exact identities
\[
J_t=Jxyz,\qquad K_t=K(xy)^{1/3}z^{2/3}.
\tag{4.4}
\]
The overlap at e is counted once. It would be incorrect to replace
these identities by a conductor-independent column contraction.

Choose
\[
\boxed{\tau=\frac{3-2\beta}{5-2\beta},\qquad
R_t=R(B_t/D)^\tau.}
\tag{4.5}
\]
Here \(1/3\le\tau<1/2\), and \(p\tau=(3-2\beta)/2\).
The cutoff may be below one. Theorem 3.1 applies to the actual ordered
outer/inner scales \(A_t,B_t\) without a size ordering, as proved in
Section 3.2. Within that theorem the child uses its own capped
stratum cutoff \(\min(2CB_t^{1/3},R_tNv)\).

Let \(m_j\) be the six parent monomials in (3.2) with A=B=D.
Take the square root of the corresponding child term and multiply
by \(1/(xyz^{3/2})\). Its remaining norm powers are:

| Parent term | x exponent | y exponent | z exponent |
|---|---:|---:|---:|
| \(HD\) | \(-3/2\) | \(-2\) | \(-5/2\) |
| \(JH^2D^{\beta-1/2}R^p\) | \(-1\) | \(-3/2\) | \(-2\) |
| \(KH^{4/3}D^{2/3}R^{2\beta}\) | \(-5/6-2\beta\tau\) | \(-11/6-\beta\tau\) | \(-11/6-2\beta\tau\) |
| \(H\) | \(-1\) | \(-1\) | \(-3/2\) |
| \(D^2R^{-3}\) | \(-5/2+3\tau\) | \(-5/2+3\tau/2\) | \(-7/2+3\tau\) |
| \(H^{2/3}D^{4/3}R^{-2}\) | \(-2+2\tau\) | \(-2+\tau\) | \(-17/6+2\tau\) |

For the critical second row, the child energy exponents before
the exterior normalization are
\[
3-2\beta-2p\tau=0,\quad
1/2-\beta-p\tau=-1,\quad
2-2\beta-2p\tau=-1.
\]
This proves the displayed norm row exactly.

Every table entry is at most minus one. Outside the explicitly
harmonic entries it is strictly smaller. For the third row,
\(\beta>1/2\) and \(\tau\ge1/3\) already imply
\(2\beta\tau>1/3\), so its x exponent is smaller than minus one.
For the last two rows the assertion follows from \(\tau<1/2\).
The constants may depend on the fixed distance of beta from one half.

All correction ideals have polynomial norm on nonempty support.
Their positive norm sums therefore converge, apart from the indicated
harmonic sums, which cost at most a fixed power of \(\log(2D)\).
Drop the correction coprimalities only in these positive upper sums.
Minkowski applied to the exact finite projection (4.2), followed by
the six-term square-root inequality, proves the following theorem.

### Theorem 4.1. Full A2 transfer

For every \(R>0\),
\[
\boxed{\begin{aligned}
\sum_{k\asymp H}|\mathscr Q_{q_0,f}(D,D;k)|^2
\ll D^\epsilon\big[&
HD+JH^2D^{\beta-1/2}R^{5/2-\beta}
+KH^{4/3}D^{2/3}R^{2\beta}\\
&+H+D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}\big].
\end{aligned}}
\tag{4.6}
\]
The raw balanced family satisfies the identical envelope.
All correction labels and all nonzero row classes are present.
There is no independent cutoff on \(N(cde)\) and no residual positive
power of that cutoff in the bound. This conclusion uses the combined
weights in the table, rather than summing an unscaled child inequality.

## 5. Exact optimization and the strict new exponent

Let E denote either balanced energy in Theorem 4.1. Suppose
\[
JH^2\le D^{5/2-\beta}=D^p.
\tag{5.1}
\]
Define the two balancing cutoffs
\[
R_2=D^{p/(p+3)}H^{-2/(p+3)}J^{-1/(p+3)},\qquad
R_3=D^{4/[3(2\beta+3)]}H^{-4/[3(2\beta+3)]}
K^{-1/(2\beta+3)},\qquad R=\min(R_2,R_3).
\tag{5.2}
\]
The second short term balances \(D^2R^{-3}\) at \(R_2\);
the third balances it at \(R_3\). Both are increasing in R.

Condition (5.1) gives \(R_2\ge1\). Since \(K\le J^{2/3}\),
\[
KH^{4/3}\le (JH^2)^{2/3}\le D^{2p/3}\le D^{4/3},
\]
so \(R_3\ge1\). Also \(R_3\le D^{1/3}\), because
beta is greater than one half and H,K are at least one.
Consequently the chosen R lies in \([1,D^{1/3}]\).
The other cutoff \(R_2\) need not separately be below \(D^{1/3}\);
only the minimum is needed. Every A2 child still uses (4.5), which
can be less than one.

At the chosen R both increasing terms are bounded by
\(E_* =D^2R^{-3}\). Furthermore (5.1) implies \(H\le D\).
The branch \(D^2R_3^{-3}\) is at least HD, since its ratio to HD is
\[
(D/H)^{(2\beta-1)/(2\beta+3)}K^{3/(2\beta+3)}\ge1.
\]
The remaining mixed tail divided by \(E_*\) is
\[
H^{2/3}D^{-2/3}R
\le (H/D)^{\,2/3-4/[3(2\beta+3)]}K^{-1/(2\beta+3)}
\le1.
\]
The H term is harmless as well. Thus
\[
\boxed{
E\ll D^\epsilon\max\left\{
D^{(4\beta+2)/(2\beta+3)}
H^{4/(2\beta+3)}K^{3/(2\beta+3)},
\quad
D^{(6-p)/(p+3)}H^{6/(p+3)}J^{3/(p+3)}
\right\}.}
\tag{5.3}
\]
It is at most \(D^{2+\epsilon}\) throughout (5.1), also directly
because \(E_*=D^2R^{-3}\le D^2\).

At the source-qualified value beta=11/12 this becomes
\[
\boxed{
E\ll D^\epsilon
\max\left\{
D^{34/29}H^{24/29}K^{18/29},
D^{53/55}H^{72/55}J^{36/55}
\right\},
\qquad JH^2\le D^{19/12}.}
\tag{5.4}
\]
The cutoffs are
\[
R_2=D^{19/55}H^{-24/55}J^{-12/55},\qquad
R_3=D^{8/29}H^{-8/29}K^{-6/29}.
\tag{5.5}
\]
Both the raw family and its complete A2 correction satisfy this bound.

### Corollary 5.1

At \(q_0=f=1\), \(H=D^{1/2}\), the choice \(R=D^{7/55}\) gives
\[
\boxed{
\sum_{k\asymp D^{1/2}}|P_1(D,D;k,1)|^2
\ll D^{89/55+\epsilon},\qquad
\sum_{k\asymp D^{1/2}}|\mathscr Q_{1,1}(D,D;k)|^2
\ll D^{89/55+\epsilon}.}
\tag{5.6}
\]
At this same choice of R, the six exponents in the boxed envelope are
\[
3/2,\quad 89/55,\quad 47/30,\quad
1/2,\quad 89/55,\quad 233/165.
\tag{5.7}
\]
The largest is 89/55. This direct evaluation also verifies the balance
without relying on a numerical optimizer.

The adjacent PR #924 gives 31/19 for these same positive objects and
this height under its one-scalar angular premise. The improvement is
\[
\frac{31}{19}-\frac{89}{55}=\frac{14}{1045}>0.
\tag{5.8}
\]
Here the extra input use is precisely the already stated cancellation
in the second actual inverse scalar, not a new higher native moment.
The earlier unstratified two-scalar raw value 1087/660 improves by
19/660; its full A2 counterpart 2399/1428 is also superseded by (5.6).
At the counting scalar value beta=1, the two-scalar powers coincide
with the one-scalar powers and (5.3) reduces to the existing
\(\max(D^{6/5}H^{4/5}K^{3/5},D H^{4/3}J^{2/3})\) bound.
Thus no strict counting-exponent improvement is claimed.

At unit moving labels the sufficient positive-energy range remains
\[
H\le D^{19/24}.
\tag{5.9}
\]
This is a physical row-height range for normalized Gauss/A2 energies.
It is not a zeta zero-free boundary. The general moving-label version
is \(H\le D^{19/24}J^{-1/2}\), with \(H\ge1\).

## 6. Profiles, cutoff choices, and the retained boundary

Fixed smooth compactly supported two-variable tests are covered by
Mellin separation with one-variable cutoffs on their physical supports.
Their transforms have enough integrable polynomial moments to absorb
the finite scalar seminorm losses. This does not insert an arbitrary
arithmetic coefficient into the short structured bound.

Sharp row balls follow by using the same parent R on all inward annuli.
All six row exponents, namely 1, 2, 4/3, 1, 0 and 2/3, are nonnegative;
the row-independent term costs only a logarithmic number of nonempty
annuli. For a fixed Schwartz row profile, keep A,B,q0,f,R and all
arithmetic child choices fixed on outward annuli, and enlarge only the
common reference parameter to retain the polynomial ceilings.
The largest row power is two, so a fixed sufficiently rapid decay
absorbs both this growth and the preliminary small-power loss.
This uses the unoptimized six-term envelope on those annuli; it does
not assume that the feasibility range (5.1) remains valid as H grows.
The optimized consequences follow by choosing the parent R once.

The exponent tau in (4.5) is one explicit successful coordinatewise
summation choice. It is not asserted to be the only possible cutoff.
For example the cube-root choice in PR #924 no longer has separately
summable x powers after the new second scalar saving: its corresponding
x exponent is -17/18 at beta=11/12. That rules out the naive independent
three-coordinate summation of that table. It does not rule out an
ordered or coupled summation of the correction scales.

The positivity of the energies is used only after the exact masks,
row partition and A2 projection have been written. The estimates still
do not control the signed centered first-Poisson covariance with its
original row-dependent kernel, independent A2 corrections on both sides,
and equality subtraction at reconstructed product columns. In the
leading fourth-moment block its dual height is about \(D^{3-\theta}\),
outside (5.9) in the intended original range. The exact signed reunion
and the small-w audits elsewhere in this packet identify that
remaining native problem. No full fourth moment, cofinal generalized
moment hierarchy, attainment of 17/24, or RH conclusion follows from
the present two positive-energy theorems.
