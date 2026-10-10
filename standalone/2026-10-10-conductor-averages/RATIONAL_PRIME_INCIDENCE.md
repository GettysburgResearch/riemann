# Rational-prime incidence: conjugate and inert links in every even moment

**Status:** proposed proved component estimates for the actual inverse sextic
moments. The rational-prime count, enlarged radical sector, and classical
completed-character branch are native deductions from elementary counting and
the previously proved smooth Poisson bound. The additional subconvex branches
use the explicitly pinned published inputs of PR #925. Every bound concerns
actual tuple contributions, allows arbitrary bounded coefficient phases, and
retains all principal masks. The generalized moment and remaining signed
covariance are not proved.

**What is new.** Earlier incidence arguments count prime ideals independently.
Above a split rational prime, the two conjugate prime ideals have the same
rational norm parameter; an inert prime ideal has norm equal to the square of
its rational prime. Counting those parameters only once gives additional
power savings. The entire sector where the product of column norms is
squarefull is already of diagonal size, even when every pair of column ideals
is coprime. A stronger radical criterion and four-parameter bounds are proved
below. Section 7 gives a fourth-moment family outside the pointwise conductor
regions of PR #925 and the new classical region, but inside the new
subconvex region. Section 8 combines rational counting with this packet's
separate cubic-conductor average and proves a further strict gain.

**Exact sources and dependencies.**

1. PR #914, commit
   0cc0428fedbbfc340044c7451b3d392c1da9a103,
   [CONDUCTOR_SECTORS.md](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md),
   Sections 2--4: literal residual character, smooth row test, and masked
   Poisson bound. Sections 5--8 supply the earlier prime-ideal incidence
   argument for comparison. Section 9 already proves the Möbius parity
   identity; that identity is not a new result here.
2. PR #925, frozen mathematical source
   5ad900ff27d34f1a8f94d28e19c47a3b37de6e39,
   [SIGNED_CONDUCTOR_PROGRESS.md](https://github.com/GettysburgResearch/riemann/blob/5ad900ff27d34f1a8f94d28e19c47a3b37de6e39/standalone/2026-10-10-joint-divisor-covariance/SIGNED_CONDUCTOR_PROGRESS.md),
   Sections 1--2: the all-element-row adapter to Wu's subconvex bound and
   Söhne's divisor bound in its explicitly quoted form. Those external
   analytic inputs are not reproved here.
3. PR #919, commit
   9b04a887e171b3104a66cf57296ce5b0b2920d78,
   [SMALL_GCD_CONDUCTOR_REDUCTION.md](https://github.com/GettysburgResearch/riemann/blob/9b04a887e171b3104a66cf57296ce5b0b2920d78/standalone/2026-10-10-averaged-conductor-frontier/SMALL_GCD_CONDUCTOR_REDUCTION.md),
   supplies the existing fourth-moment signed remainder, used only for
   Section 8's consequence.
4. PR #924, commit
   725b2d25ab47e57500049d93985560098c7ef3fa,
   [CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md](https://github.com/GettysburgResearch/riemann/blob/725b2d25ab47e57500049d93985560098c7ef3fa/standalone/2026-10-10-sextic-moving-labels/CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md),
   is a comparison source for ordinary cross-gcd conditions. Its native
   second-moment hypothesis is not used in this note.
5. The companion [CUBIC_CONDUCTOR_AVERAGE.md](CUBIC_CONDUCTOR_AVERAGE.md),
   specifically its fixed-background bound (4.6), is an additional
   source-dependent input only to Section 8 here. That companion derives
   its estimate from Proposition 8.1 of
   [de Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1)
   with the moving-conductor dependence displayed. Sections 1--7
   of the present note do not depend on that input.
6. PR #926, commit
   086bf0560c0c2679a1fe41418f583d2c5ca743c3,
   [MOBIUS_OVERLAP_TAILS.md](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/MOBIUS_OVERLAP_TAILS.md),
   Sections 5.1 and 6.2, is a comparison source for the separately
   conditional cutoff in Section 7 and the distinct signed two-axis
   bounds discussed after Section 8's example.

Coefficient phases are not averaged or replaced by random signs. The gain
is an arithmetic count combined, where specified, with cancellation already
proved for each complete residual-character row sum.
The strict comparisons below concern the displayed positive absolute
accounting bounds. They are not claims to dominate every contemporary
signed-sector estimate for specially structured Möbius coefficients.

## 1. Exact tuple and rational-prime data

Work over \(K=\mathbb Q(\sqrt{-3})\), with its fixed primary generators,
fixed bad-prime set \(S\), and literal zero-extended sextic symbols
\(\chi_n(u)\). The primes over \(2\) and \(3\) belong to \(S\).
Fix \(k\ge1\), \(B\ge1\), \(D\ge2\), \(H\ge1\), and coefficients
\[
|a_n|\le1,\qquad a_n=0
\quad\hbox{unless }n\hbox{ is squarefree},\ (n,S)=1,\ Nn\le BD.
\tag{1.1}
\]
The inverse coefficients \(\mu_K(n)\nu(n)W(Nn/D)\) are included after
one fixed rescaling of \(W\).

For a Hermitian tuple
\[
\mathbf t=(n_1,\ldots,n_k;m_1,\ldots,m_k),\qquad
c(\mathbf t)=\prod_i a_{n_i}\prod_i\overline{a_{m_i}},
\]
put
\[
\mathscr N(\mathbf t)=\prod_iNn_i\prod_iNm_i\le(BD)^{2k}.
\tag{1.2}
\]
This is an ordinary positive integer. At a prime ideal \(\mathfrak p\),
write \(r_{\mathfrak p},s_{\mathfrak p}\) for its two multiplicities,
\(m_{\mathfrak p}=r_{\mathfrak p}+s_{\mathfrak p}\), and
\(e_{\mathfrak p}=r_{\mathfrak p}-s_{\mathfrak p}\pmod6\). The exact
primitive residual conductor and principal mask are
\[
f=\prod_{e_{\mathfrak p}\ne0}\mathfrak p,\qquad
q_0=\prod_{\substack{m_{\mathfrak p}>0\\e_{\mathfrak p}=0}}\mathfrak p.
\tag{1.3}
\]
The full row character is, also at nonunits,
\[
\psi_{\mathbf t}(u)\mathbf1_{(u,q_0)=1}.
\tag{1.4}
\]
If \(f\ne1\), \(\psi_{\mathbf t}\) is primitive and nonprincipal modulo
\(f\). Fix the same type of nonnegative compact smooth radial test
\(\Phi\) as in the sources and put
\[
S_{\mathbf t}^{\Phi}(H)
=\sum_{u\in\mathcal O_K}\Phi(u/\sqrt H)
 \psi_{\mathbf t}(u)\mathbf1_{(u,q_0)=1}.
\tag{1.5}
\]
The zero row is included with the original convention; it is zero for
the nonprincipal tuples below. Every nonzero element row is retained.

For each rational prime \(p\mid\mathscr N(\mathbf t)\), define
\[
\ell_p=v_p(\mathscr N(\mathbf t)),\qquad
j_p=v_p(Nf)\in\{0,1,2\}.
\tag{1.6}
\]
The value \(\ell_p\) is an occurrence count weighted by residue degree.
It need not equal the number of prime-ideal occurrences.

### The two splitting cases

If \(p\equiv1\pmod3\), write
\(p\mathcal O_K=\mathfrak p\overline{\mathfrak p}\). Then
\[
\ell_p=m_{\mathfrak p}+m_{\overline{\mathfrak p}},\qquad
j_p=\mathbf1_{e_{\mathfrak p}\ne0}
    +\mathbf1_{e_{\overline{\mathfrak p}}\ne0}.
\tag{1.7}
\]
Both local incidence patterns may be nonempty, and they may share
column positions. No coprimality between conjugate column factors is
assumed.

If \(p\equiv2\pmod3\), the ideal \(p\mathcal O_K\) is prime of norm
\(p^2\), and
\[
\ell_p=2m_{p\mathcal O_K},\qquad
j_p=2\mathbf1_{e_{p\mathcal O_K}\ne0}.
\tag{1.8}
\]
One inert prime ideal in one column therefore has
\((\ell_p,j_p)=(2,2)\), not \((1,1)\).

In both cases \(1\le\ell_p\le4k\). If \(j_p=0\), then
\(\ell_p\ge2\); a single split-prime occurrence cannot be principal.
The low-occurrence nonprincipal types are exactly:

| Type \((\ell,j)\) | Source of the rational prime |
|---|---|
| \((1,1)\) | One split prime ideal in one column |
| \((2,1)\) | One split prime ideal twice on the same Hermitian side |
| \((2,2)\) | Both conjugate split prime ideals once each, or one inert prime ideal once |
| \((3,2)\) | A split prime with both conjugate local characters nonprincipal and three occurrences in total |

For \((3,2)\), the two ideal multiplicities are \(1\) and \(2\);
the double occurrences are on one side. The inert case has even
\(\ell\) and cannot produce this type.

For \(j=1,2\), put
\[
r_{\ell,j}=\prod_{p:(\ell_p,j_p)=(\ell,j)}p,\qquad
r_0=\prod_{p:j_p=0}p.
\tag{1.9}
\]
These are pairwise coprime squarefree ordinary integers. Empty products
are one. The four exceptional labels used below are
\[
\lambda=r_{1,1},\qquad g=r_{2,1},\qquad
t=r_{2,2},\qquad z=r_{3,2}.
\tag{1.10}
\]
In particular,
\[
Nf=\prod_{\ell,j}r_{\ell,j}^{\,j}.
\tag{1.11}
\]
The label \(t\) records one rational parameter for a pair of conjugate
prime ideals or for a degree-two prime ideal. Treating it as two
independent norm parameters would lose the saving below.

## 2. A native radical count, including all squarefull norm products

Let
\[
\rho(\mathbf t)=\operatorname{rad}_{\mathbb Z}\mathscr N(\mathbf t)
=\prod_{p\mid\mathscr N(\mathbf t)}p.
\tag{2.1}
\]

### Theorem 2.1. Small rational radical

For every \(R\ge1\),
\[
\#\{\mathbf t:\rho(\mathbf t)\le R\}
\ll_{k,B,\epsilon}D^\epsilon R.
\tag{2.2}
\]
Consequently the entire region \(\rho(\mathbf t)\le(BD)^k\) has
positive absolute accounting
\[
\boxed{
\sum_{\rho(\mathbf t)\le(BD)^k}|c(\mathbf t)|
 |S_{\mathbf t}^{\Phi}(H)|
\ll_{k,B,S,\Phi,\epsilon}HD^{k+\epsilon}.
}
\tag{2.3}
\]
The same bound holds with the sharp nonzero row cutoff. No analytic
character estimate is used.

**Proof.** Fix a squarefree integer \(\rho\). A split rational prime
has two prime ideals. Each has an incidence subset of the \(2k\)
column positions, including the empty subset. Thus at most
\(2^{4k}\) joint choices are possible; omit the joint empty choice.
An inert prime has only \(2^{2k}-1\) nonempty choices. These choices
determine the tuple of ideals uniquely. Their number is at most
\[
C_k^{\omega(\rho)}\ll_{k,\eta}\rho^\eta
\ll_{k,B,\epsilon}D^\epsilon,
\tag{2.4}
\]
after choosing \(\eta\) sufficiently small, since every supported tuple
has \(\rho\le\mathscr N\le(BD)^{2k}\).
For the elementary small-power bound, \(C_k\le p^\eta\) at every
sufficiently large prime, and the finite remaining set contributes a
constant. There are at most \(R\) positive integers \(\rho\le R\).
Discarding squarefreeness and individual column constraints only
enlarges this count. This proves (2.2).

The smooth sum has \(|S_{\mathbf t}^{\Phi}(H)|\ll_\Phi H\), by
planar lattice counting and \(H\ge1\); the sharp sum has the same
bound. Multiply (2.2), with \(R=(BD)^k\), by this estimate and
\(|c|\le1\). This proves (2.3). \(\square\)

### Corollary 2.2. Every squarefull total norm product

If every rational prime dividing \(\mathscr N(\mathbf t)\) has
\(\ell_p\ge2\), then the tuple belongs to the region (2.3).
Hence the complete squarefull-total-norm sector is
\[
\boxed{O_{k,B,S,\Phi,\epsilon}(HD^{k+\epsilon})}
\tag{2.5}
\]
with either smooth or sharp rows.

Indeed \(\rho^2\le\mathscr N\le(BD)^{2k}\). This condition permits
prime ideals occurring just once: a conjugate pair or an inert prime
ideal already contributes two powers of its rational prime. The stronger
criterion (2.3) also permits rational singletons when other incidences
sufficiently reduce the radical.

## 3. Fixed rational-type count and complete row inputs

### Lemma 3.1. Fixed nonprincipal rational labels

For any fixed collection of pairwise coprime \(r_{\ell,j}\), \(j=1,2\),
the compatible tuple count satisfies
\[
\boxed{
\#\{\text{compatible tuples}\}
\ll_{k,B,\epsilon}
D^{k+\epsilon}\prod_{\ell,j}r_{\ell,j}^{-\ell/2}.
}
\tag{3.1}
\]
If
\[
Z=(BD)^k\prod_{\ell,j}r_{\ell,j}^{-\ell/2}<1,
\tag{3.2}
\]
there are no compatible tuples.

**Proof.** Every rational prime in \(r_0\) has total norm occurrence
at least two. Therefore
\[
r_0^2\prod_{\ell,j}r_{\ell,j}^{\,\ell}
\le\mathscr N(\mathbf t)\le(BD)^{2k},
\qquad r_0\le Z.
\tag{3.3}
\]
There are at most \(Z\) possible positive integers \(r_0\) when
\(Z\ge1\). For every choice, the finite local assignments in (2.4)
bound all allocations, including actual multiplicities at the
principal primes, by \(D^\epsilon\). This proves (3.1).
No second sum over the two conjugate prime ideals is introduced.
The exclusions by \(S\) and individual factor supports are only
discarded in this positive count. \(\square\)

We use the following exact masked row estimates. For all tuples,
\[
|S_{\mathbf t}^{\Phi}(H)|\ll H.
\tag{3.4}
\]
For \(f\ne1\), the smooth Poisson bound of PR #914 gives
\[
|S_{\mathbf t}^{\Phi}(H)|
\ll_\Phi d_K(q_0)(Nf)^{1/2}.
\tag{3.5}
\]
Its proof first expands the literal principal mask over \(d\mid q_0\)
and applies the primitive Gauss-sum Poisson identity at scale \(H/Nd\).
That identity is valid even below unit scale. The factor \(d_K(q_0)\)
is at most \(D^\epsilon\), with losses reassigned using (1.2).

For the additional branches put
\[
\beta=\frac{103}{512}.
\tag{3.6}
\]
PR #925's adapter to Wu and Blomer--Brumley gives
\[
|S_{\mathbf t}^{\Phi}(H)|
\ll_{\Phi,\epsilon}
H^{1/2}(Nf\,Nq_0)^\epsilon(Nf)^\beta,\qquad f\ne1.
\tag{3.7}
\]
The same source, using Söhne's theorem in the precise form quoted
there, proves
\[
|S_{\mathbf t}^{\Phi}(H)|
\ll_{\Phi,\epsilon}
H^{1/2}(Nf\,Nq_0)^\epsilon(Nf\,P(f))^{1/6},
\tag{3.8}
\]
where \(P(f)=\max_{\mathfrak p\mid f}N\mathfrak p\).
Here \(P(f)\) is a prime-ideal norm: at an inert prime it is
\(p^2\), not \(p\). If \(f\) has a divisor \(d\) with
\[
C_1^{-1}(Nf)^{1/3}\le Nd\le C_1(Nf)^{1/3}
\tag{3.9}
\]
for a fixed \(C_1\ge1\), the factor \(P(f)^{1/6}\) in (3.8) can
be omitted. Restriction (3.9) is imposed before using that bound.

For clarity about normalization, the subconvex adapter first projects
the complete radial row sum onto the unit-trivial characters. A
unit-nontrivial residual character gives zero. Otherwise there are
exactly six element generators per ideal, the residual character is
a nonprincipal primitive finite-order Hecke character, and the mask
is its exact finite Euler polynomial. Mellin inversion shifts only
the \(L\)-function to \(1/2\), never its reciprocal. Thus no zero-free
assumption or native Möbius second moment enters (3.7)--(3.8).
All adapter details and external source limits are those of PR #925.

## 4. Four rational-type branches at every fixed order

For \(L,G,T,U\ge1\), define
\[
\mathcal R^\Phi_{L,G,T,U}
=\sum_{\substack{
 \mathbf t:f\ne1,\ L\le\lambda<2L,\ G\le g<2G\\
 T\le t<2T,\ U\le z<2U}}
 |c(\mathbf t)|\,|S_{\mathbf t}^{\Phi}(H)|.
\tag{4.1}
\]
Every other rational type and every principal mask is summed.
An arbitrary extra tuple selector is permitted throughout the
following estimates, since (4.1) is positive accounting.

### Theorem 4.1. Rational incidence bounds

Uniformly for all these blocks,
\[
\boxed{
\mathcal R^\Phi_{L,G,T,U}
\ll D^{k+\epsilon}
\min\left\{
 H\sqrt{L/U},\
 L\sqrt G\,T\sqrt U,\
 H^{1/2}L^{359/512}G^{103/512}
             T^{103/256}U^{-25/256}
\right\}.
}
\tag{4.2}
\]
Only the final branch uses the published subconvex input. The first
branch also holds with sharp rows, and with principal tuples included.

On the subfamily \(P(f)\le Y\),
\[
\boxed{
\mathcal R^\Phi_{L,G,T,U;P\le Y}
\ll D^{k+\epsilon}
H^{1/2}Y^{1/6}L^{2/3}G^{1/6}T^{1/3}U^{-1/6}.
}
\tag{4.3}
\]
On the balanced-divisor subfamily (3.9), the same bound holds without
\(Y^{1/6}\), with the constant allowed to depend on \(C_1\).

**Proof.** A row estimate of the form
\(H^\tau(Nf)^\gamma D^\epsilon\), combined with (3.1) and (1.11),
leaves the fixed-label weight
\[
D^{k+\epsilon}H^\tau
\prod_{\ell,j}r_{\ell,j}^{\,j\gamma-\ell/2}.
\tag{4.4}
\]
All preliminary losses can be chosen in terms of the requested final
\(\epsilon\), since \(NfNq_0\le(BD)^{2k}\), and the finite number
of local types depends only on \(k\).

For a positive integer \(v\) in \(V\le v<2V\), ordinary counting gives
\[
\sum_{V\le v<2V}v^\alpha\ll_\alpha V^{1+\alpha}.
\tag{4.5}
\]
Enlarging from the allowed squarefree integers with their prescribed
splitting types to all positive integers is legitimate here. The
four retained block powers are consequently:

| Rational type | General power | \(\gamma=0\) | \(\gamma=1/2\) | \(\gamma=\beta\) |
|---|---:|---:|---:|---:|
| \((1,1)\), \(L\) | \(1/2+\gamma\) | \(1/2\) | \(1\) | \(359/512\) |
| \((2,1)\), \(G\) | \(\gamma\) | \(0\) | \(1/2\) | \(103/512\) |
| \((2,2)\), \(T\) | \(2\gamma\) | \(0\) | \(1\) | \(103/256\) |
| \((3,2)\), \(U\) | \(2\gamma-1/2\) | \(-1/2\) | \(1/2\) | \(-25/256\) |

For \(\gamma=0\), all other nonprincipal types have \(\ell\ge3\),
so their integer sums in (4.4) converge absolutely. Apply (3.4),
with \(\tau=1\), to obtain the first branch.

For \(\gamma=1/2\), the only other borderline types are \((3,1)\)
and \((4,2)\), with fixed-label exponent \(-1\). Each contributes
\(O_k(\log(2D))\) up to its physical cutoff from (1.2).
Every other nonprincipal type has exponent strictly less than \(-1\).
Thus (3.5) and (4.5) give the second branch after absorbing these
two logarithms. The potentially growing \((3,2)\) block has been
retained explicitly as \(U^{1/2}\).

For \(\gamma=\beta=103/512<1/4\), every type other than the first
three has \(\ell\ge3\), and
\[
j\beta-\ell/2\le2\beta-3/2
=-\frac{281}{256}<-1.
\tag{4.6}
\]
All omitted sums are absolutely convergent. Retaining the fourth
block gives its additional factor \(U^{2\beta-1/2}\).
Use (3.7) and \(\tau=1/2\) to prove the third branch.

Finally use (3.8), with \(\gamma=1/6\), retaining the restriction
\(P(f)\le Y\). The same calculation gives the four powers
\(2/3,1/6,1/3,-1/6\), proving (4.3). Under (3.9), use the
stated bound without \(P(f)^{1/6}\). Every mask and conductor
restriction was imposed before the positive majorant was enlarged.
The separate valid bounds apply to the same quantity, so their
minimum is valid. \(\square\)

### Corollary 4.2. Three labels suffice for the subconvex gain

If \(z\) is also summed, then
\[
\boxed{
\mathcal R^\Phi_{L,G,T}
\ll D^{k+\epsilon}
\min\left\{
 H\sqrt L,\
 H^{1/2}L^{359/512}G^{103/512}T^{103/256}
\right\}.
}
\tag{4.7}
\]
The prime-factor branch becomes
\[
\mathcal R^\Phi_{L,G,T;P\le Y}
\ll D^{k+\epsilon}
H^{1/2}Y^{1/6}L^{2/3}G^{1/6}T^{1/3},
\tag{4.8}
\]
and the balanced-divisor branch again omits \(Y^{1/6}\).

**Proof.** Sum the corresponding branches of (4.2)--(4.3) over
dyadic \(U\ge1\). Their exponents \(-1/2,-25/256,-1/6\) are
strictly negative, so the geometric sums converge. The classical
completion branch has positive \(U\)-exponent and is deliberately
not asserted in this three-label form. \(\square\)

## 5. Additional complete diagonal-size regions

All quantities here are actual tuple labels from (1.10).
The new classical region is
\[
\boxed{\lambda\sqrt g\,t\sqrt z\le H,\qquad f\ne1.}
\tag{5.1}
\]
The new subconvex region is
\[
\boxed{
\lambda^{359/256}g^{103/256}
t^{103/128}z^{-25/128}\le H,\qquad f\ne1.
}
\tag{5.2}
\]
Both have positive absolute accounting \(O(HD^{k+\epsilon})\).
Partition the four labels into dyadic blocks and use the corresponding
branch of (4.2). In (5.2), the negative exponent of \(z\) is treated
using its upper endpoint when determining whether a block meets
the region. Within a block this changes the bound by at most a fixed
factor. There are \(O_k((\log(2D))^4)\) nonempty blocks; absorb
the logarithms in \(\epsilon\).

The first branch also controls \(\lambda\le z\), although this
is already contained in Theorem 2.1's radical region:
\[
\mathscr N=\rho^2\lambda^{-1}
\prod_{\ell_p\ge3}p^{\ell_p-2}\ge\rho^2 z/\lambda.
\tag{5.3}
\]
This explains why the radical theorem was stated separately.

From (4.3), the additional region
\[
\boxed{
P(f)\lambda^4g\,t^2/z\le H^3,\qquad f\ne1
}
\tag{5.4}
\]
is controlled at the same diagonal size. Partition the actual
largest prime-ideal norm \(P(f)\) into dyadic blocks as well.
On the balanced-divisor subfamily (3.9), one can omit \(P(f)\):
\[
\boxed{\lambda^4g\,t^2/z\le H^3.}
\tag{5.5}
\]
All denominator labels are positive integers. If desired, the
three-label versions set aside the favorable \(z\)-factor by
applying (4.7)--(4.8).

These positive accounting estimates survive any additional restrictions,
including the original two small-gcd conditions, far-cross-separation
conditions, or arbitrary bounded coefficient phases. They can be united
with the previous controlled regions by counting each tuple once.
No monotonicity of an isolated signed sum is assumed.

## 6. A new all-order sector with pairwise coprime column ideals

Choose distinct split rational primes \(p_1,\ldots,p_k\asymp D\)
and one prime ideal \(\mathfrak p_i\) above each. Set
\[
(n_1,\ldots,n_k;m_1,\ldots,m_k)
=(\mathfrak p_1,\ldots,\mathfrak p_k;
  \overline{\mathfrak p_1},\ldots,\overline{\mathfrak p_k}).
\tag{6.1}
\]
All \(2k\) ideals are pairwise coprime. Every prime ideal is an
ideal singleton, so in the old notation
\[
Ng_1\asymp D^{2k},\qquad g_2=1,\qquad Nf\asymp D^{2k}.
\tag{6.2}
\]
Yet
\[
\mathscr N=(p_1\cdots p_k)^2,\qquad
\rho=p_1\cdots p_k\asymp D^k,\qquad \lambda=1.
\tag{6.3}
\]
Theorem 2.1, or the squarefull corollary with fixed support constants
retained, controls the whole squarefull-total-norm collection
containing these tuples by \(HD^{k+\epsilon}\). It does not
require the specified pairing (6.1) to be fixed beforehand.

At \(H=D^h\), \(1<h\le11/10\), the old completion criterion has
exponent \(2k>h\), and the old Wu criterion has exponent
\((359/256)2k>h\). Even the optional old balanced-divisor
criterion has exponent \(8k>3h\). Thus these tuples lie outside
those earlier criteria; all their ordinary within-side and cross
gcds are one.

The example is feasible for every fixed \(k\), and its residual
character is nonprincipal. Choosing all split primes in the fixed
class \(p\equiv1\pmod{36}\) also makes their local sextic characters
trivial on the six units. This choice is optional: unit-nontrivial
tuples already have zero complete radial kernel. No assertion that
these thin collections dominate the full moment is made.

## 7. A strict gain beyond PR #925 and the new classical branch

This example has rational singletons and lies outside the small-rational-
radical region. The subconvex branch together with the new rational
count is necessary for its displayed saving.

Take split prime ideals
\[
c,d,e,f_0,t_1,t_2,x_1,x_2,y_1,y_2
\]
over distinct rational primes, with no further conjugate identifications.
Use \(\overline{t_1},\overline{t_2}\) in the opposite columns and set
\[
\begin{aligned}
n_1&=c e t_1x_1,&n_2&=c f_0t_2x_2,\\
m_1&=d e\overline{t_1}y_1,&
m_2&=d f_0\overline{t_2}y_2.
\end{aligned}
\tag{7.1}
\]
All columns are squarefree. Take norm scales
\[
\begin{gathered}
Nc,Nd\asymp D^{7/10},\qquad
Ne,Nf_0\asymp D^{1/5},\\
Nt_1,Nt_2\asymp D^{1/50},\qquad
Nx_i,Ny_i\asymp D^{2/25}.
\end{gathered}
\tag{7.2}
\]
Each column has exponent
\[
\frac7{10}+\frac15+\frac1{50}+\frac2{25}=1.
\tag{7.3}
\]
Fixed relative intervals and fixed support constants can be inserted
in each comparison. Distinct split primes in those intervals give
realizations; a fixed \(1\pmod{36}\) restriction is again available
if unit-trivial residual characters are desired.

The two repeated same-side ideals are \(c,d\), the principal-mask
ideals are \(e,f_0\), and all other prime ideals are singletons.
Thus the old ideal-incidence labels and actual conductor have
\[
Ng_1\asymp D^{2/5},\qquad
Ng_2\asymp D^{7/5},\qquad
Nq_0\asymp D^{2/5},\qquad
Nf\asymp D^{9/5}.
\tag{7.4}
\]
The new rational labels instead satisfy
\[
\lambda\asymp D^{8/25},\qquad
g\asymp D^{7/5},\qquad
t\asymp D^{1/25},\qquad z=1.
\tag{7.5}
\]
The two conjugate pairs cost only the rational-prime product
\(Nt_1Nt_2\), of exponent \(1/25\), rather than two independent
ideal parameters. Moreover
\[
\rho(\mathbf t)\asymp D^{54/25}>D^2,
\tag{7.6}
\]
so the native radical bound (2.3) alone does not control this family
at diagonal size.

Take \(h=21/20\), \(H=D^h\). Both within-side gcds have exponent
\(7/10<99/140=(6-h)/7\); the margin is \(1/140\).
The matched ordinary cross gcds are \(e,f_0\), of exponent \(1/5\),
and the other two cross gcds are one. All ordinary cross separation
costs therefore have exponent at least \(4/5\). These tuples remain
inside the old small-gcd, far-cross-separation region for any chosen
subpower cross threshold.

The comparison of positive accounting bounds, normalized by \(HD^2\), is:

| Bound | Excess exponent |
|---|---:|
| Old ideal-incidence completion | \(1/20\) |
| Old ideal-incidence Wu branch | \(19/512\) |
| New rational-incidence completion | \(1/100\) |
| New rational-incidence Wu branch | \(-37/12800\) |

The final calculation is exactly
\[
\begin{aligned}
-\frac12\frac{21}{20}
&+\frac{359}{512}\frac8{25}
+\frac{103}{512}\frac75
+\frac{103}{256}\frac1{25}
=-\frac{37}{12800}.
\end{aligned}
\tag{7.7}
\]
Therefore the complete incidence collection with the restrictions
just stated satisfies
\[
\boxed{
\mathcal R^\Phi\ll HD^{\,2-37/12800+\epsilon}.
}
\tag{7.8}
\]
The proof bounds the whole corresponding block of (4.2); the additional
fixed incidence restrictions only decrease its positive accounting.

For a complete comparison with PR #925, its largest-prime criterion
also fails: \(c,d\) are each single prime ideals of norm
\(\asymp D^{7/10}\), so its left exponent is
\[
\frac7{10}+4\frac25+\frac75=\frac{37}{10}
>3h=\frac{63}{20}.
\tag{7.9}
\]
Its balanced-divisor alternative cannot be invoked. Every divisor
of \(f\) either contains \(c\) or \(d\), in which case its norm is
\(\gg D^{7/10}\), or avoids both, in which case its norm is
\(\ll D^{2/5}\). But \((Nf)^{1/3}\asymp D^{3/5}\).
These fixed positive exponent gaps exclude a divisor satisfying
(3.9) for any fixed comparison constant \(C_1\), once \(D\) is
sufficiently large. This uses that \(c,d\) were explicitly chosen
as prime ideals, not merely squarefree products.

The new prime-factor criterion (5.4) also fails: its exponent
excess over \(3h\) is \(31/100>0\). Thus (7.8) is a strict
gain from the general subconvex branch with rational incidence,
not an instance of the old balanced-divisor or prime-factor examples.

These are comparisons of valid upper bounds for feasible collections.
They are not lower bounds for the old estimates or measurements
of the true signed contribution.

The comparison is with the specified pointwise conductor branches of
PR #925. Under the separate uniform pointwise premise
\(\mathrm{PW}_{7/8}^{\rm sm}\), PR #926 lowers the common-gcd tail
cutoff at this height to \(D^{69/110}\), which also removes the
present \(D^{7/10}\) common factors through its norm decomposition.
No novelty claim against that additionally conditional route is made.
The bounds here allow arbitrary bounded coefficient phases and do not
use that pointwise inverse premise. The cubic-conductor average of
the current packet also controls this example; the next section gives
a strict gain from combining that average with the rational count.

## 8. Combining the cubic average with rational singleton counting

This section alone uses the companion
[CUBIC_CONDUCTOR_AVERAGE.md](CUBIC_CONDUCTOR_AVERAGE.md). Its
uniform mean over the cubic double-prime labels gives, before summing
the remaining ideals, the bound
\[
D^{k+\epsilon}H^{1/2}
(Ng_1)^{-1/4}\prod_{m\ge3}(Ng_m)^{-m/2+1/4}.
\tag{8.1}
\]
Here \(g_1,g_m\) are the original prime-ideal incidence labels.
This is the companion's equation (4.6), after its entire sum over
the cubic labels and its uniformly retained principal-mask count.
It is uniform in every frozen residual character. In particular,
this use does not assert that de Faveri's fixed-twist Theorem 1.2
has an unstated uniform constant.

### New labels depending only on the singleton ideal

For the squarefree ideal \(g_1\), define ordinary squarefree integers
\[
\begin{aligned}
v(g_1)&=\prod_{\substack{p\ {\rm split}\\
 \text{exactly one prime ideal above }p\text{ divides }g_1}}p,\\
w(g_1)&=\prod_{\substack{p\ {\rm split,\ both\ primes\ divide}\ g_1\\
 \text{or }p\ {\rm inert,\ its\ prime\ ideal\ divides}\ g_1}}p.
\end{aligned}
\tag{8.2}
\]
Then
\[
Ng_1=v(g_1)w(g_1)^2,\qquad (v(g_1),w(g_1))=1.
\tag{8.3}
\]
These labels concern \(g_1\) alone. They are different from
\(\lambda,t\), which classify occurrences in the entire tuple.
For example, a conjugate prime outside \(g_1\) may raise the full
tuple occurrence without changing its singleton label \(v\).

### Theorem 8.1. An averaged rational-singleton branch

For \(V,W\ge1\), sum all nonprincipal tuple contributions with
\(V\le v(g_1)<2V\) and \(W\le w(g_1)<2W\), retaining the complete
smooth row kernel. Then
\[
\boxed{
\mathcal Q^\Phi_{V,W}
\ll_{k,B,S,\Phi,\epsilon}
D^{k+\epsilon}H^{1/2}V^{3/4}W^{1/2}.
}
\tag{8.4}
\]
Consequently the complete nonprincipal region
\[
\boxed{v(g_1)^3w(g_1)^2\le H^2}
\tag{8.5}
\]
has positive absolute accounting \(O(HD^{k+\epsilon})\).
This includes the companion's region \(Ng_1\le H^{2/3}\);
the latter is equivalently \(v(g_1)^3w(g_1)^6\le H^2\).

**Proof.** For fixed ordinary integers \(v,w\), at most
\(2^{\omega(v)}\) ideals \(g_1\) satisfy (8.2). At each split
prime of \(v\) choose which one of its two prime ideals occurs.
At a split prime of \(w\), both occur; at an inert prime of \(w\),
its one degree-two prime occurs. Thus the number of choices is
at most \(D^\epsilon\), with preliminary losses reassigned.

Using (8.3), the weighted singleton sum in (8.1) is at most
\[
\begin{aligned}
\sum_{\substack{g_1:\ v(g_1)\sim V\\w(g_1)\sim W}}
(Ng_1)^{-1/4}
&\ll D^\epsilon
\sum_{v\sim V}v^{-1/4}\sum_{w\sim W}w^{-1/2}\\
&\ll D^\epsilon V^{3/4}W^{1/2}.
\end{aligned}
\tag{8.6}
\]
The ideal sums for every \(m\ge3\) in (8.1) converge absolutely,
already with exponent \(-5/4\) at \(m=3\). There is no requirement
that the rational prime supports of different \(g_m\) be disjoint:
those remaining restrictions are only discarded in this positive
majorant. In particular, the varying cubic labels have already
been averaged before this singleton count, and no relation between
them and the frozen background is silently imposed or removed
inside the conductor mean. This proves (8.4).

Partitioning \(v,w\) into their \(O_k(\log^2(2D))\) nonempty
dyadic blocks proves (8.5). Every block meeting that inequality
has the cost in (8.4) at most a fixed multiple of \(HD^{k+\epsilon}\).
Absorb logarithms in the positive loss. \(\square\)

### A strict gain from the composition

Use the same ideal pattern (7.1), but now choose exponents
\[
\begin{gathered}
Nc,Nd\asymp D^{1/2},\qquad
Ne,Nf_0\asymp D^{3/10},\\
Nt_1,Nt_2\asymp D^{1/20},\qquad
Nx_i,Ny_i\asymp D^{3/20}.
\end{gathered}
\tag{8.7}
\]
All underlying rational primes are again different apart from the
two prescribed conjugate pairs. Each column still has scale \(D\).
At \(H=D^{21/20}\), one has
\[
Ng_1\asymp D^{4/5},\quad Ng_2\asymp D,\quad
v(g_1)\asymp D^{3/5},\quad w(g_1)\asymp D^{1/10}.
\tag{8.8}
\]
The companion's unrefined bound has excess
\(-21/40+(3/4)(4/5)=3/40>0\) over \(HD^2\).
The new composed bound instead gives
\[
\boxed{\mathcal Q^\Phi\ll HD^{2-1/40+\epsilon}},
\qquad
-\frac{21}{40}+\frac34\frac35+\frac12\frac1{10}
=-\frac1{40}.
\tag{8.9}
\]
The separate rational classical branch of Section 4 has excess
\(3/5+1/2+1/10-21/20=3/20>0\). Its Wu branch has excess
\(351/2560>0\), and even its optional balanced-divisor criterion
has left exponent \(4(3/5)+1+2(1/10)=18/5>63/20=3h\).
The rational radical has exponent \(23/10>2\), so the native
radical theorem alone is insufficient too.

Both common-gcd exponents are now \(1/2\), below both
\(99/140\) and PR #926's separately conditional \(69/110\)
cutoffs. The matched cross separation exponent is \(7/10\),
and the other cross pairs are coprime. These comparisons establish
a strict gain beyond the specified separate branches, with no
claim of optimality against every other possible norm argument.

In particular, PR #926's Theorem 6.2 gives signed bounds for
complete smooth incidence blocks by averaging two even cubic axes,
and at pointwise exponent one it already controls some geometric
patterns outside the earlier pointwise conductor criteria.
Those are distinct from the positive quantity bounded here:
\(\sum_{\mathbf t}|c(\mathbf t)|\,|S_{\mathbf t}^{\Phi}(H)|\).
The present estimates permit arbitrary bounded column phases and
arbitrary additional tuple selectors, including the prescribed
conjugate identifications. No unsigned restriction principle is
inferred from the signed two-axis theorem, and no broader
all-source novelty claim is made.

## 9. Exact effect on the signed remainder, and what remains open

Let \(\mathcal C_{\mathbb Q}\) be the literal union of the rational
radical region (2.3), regions (5.1)--(5.2), and the permitted
prime-factor and balanced-divisor regions (5.4)--(5.5).
Each has positive absolute accounting \(O(HD^{k+\epsilon})\);
their union therefore does too. It can be united with all previously
valid controlled regions, counting each tuple once. When the additional
cubic conductor input is used, the composed region (8.5) can also be
included with the same conclusion.

The selection is invariant under interchanging the two Hermitian
sides: \(\ell_p\), \(j_p\), the rational radical, and conductor
divisor criteria are unchanged. If \(\mathcal W_k(D,H)\) is the
literal signed contribution of the complement in the full smooth
\(2k\)-moment, then
\[
\mathcal M_{2k}^{\Phi}(D,H)
=\mathcal W_k(D,H)+O(HD^{k+\epsilon}),\qquad
\mathcal W_k(D,H)\in\mathbb R,\qquad
\mathcal W_k(D,H)\ge-O(HD^{k+\epsilon}).
\tag{9.1}
\]
Only the established controlled union is subtracted in (9.1).

For the fourth-moment remainder \(\mathcal V_h(D)\) of PR #925,
intersect \(\mathcal C_{\mathbb Q}\) with its actual existing
small-gcd remainder and subtract that signed portion. Its absolute
value is \(O(D^{h+2+\epsilon})\) by the same positive accounting.
Thus the refined remainder \(\widetilde{\mathcal V}_h\) still obeys
\[
M_4(D,D^h)\le K_{\epsilon,h}D^{h+2+\epsilon}
+2\widetilde{\mathcal V}_h(D),\qquad
\widetilde{\mathcal V}_h(D)\ge-K_{\epsilon,h}D^{h+2+\epsilon}.
\tag{9.2}
\]
The old sufficient signed dyadic-scale upper bound remains sufficient
with \(\widetilde{\mathcal V}_h\) in place of \(\mathcal V_h\).
That average has not been bounded here.

Surviving tuples include \(2k\) top-scale split prime-ideal factors
whose underlying rational primes are all different. There
\[
\lambda\asymp D^{2k},\qquad g=t=z=1,\qquad
\rho\asymp D^{2k}.
\tag{9.3}
\]
None of the new bounds reaches \(HD^{k+\epsilon}\) for
\(H=D^{1+\vartheta}\), arbitrarily small fixed \(\vartheta>0\),
in the intended higher-moment range. The Möbius parity sign
already identified in PR #914 does not cancel inside a fixed
residual character class by itself. New control of its signed
average over these independent rational-prime configurations
is still required.

The advance is a rigorously enlarged arithmetic domain and strict
power savings, including (7.8), for actual complete moment sectors.
It does not prove the full fourth moment, the boundary \(17/24\),
an unbounded hierarchy of diagonal moments, or RH.

## 10. Review and finite-validation boundary

Load-bearing finite statements are the split/inert formulas
(1.7)--(1.8), fixed-type support inequality (3.3), block exponent
table, and rational exponents and divisor gap in Section 7.
Section 8 adds the exact singleton factorization and the
\(V^{3/4}W^{1/2}\) weighted count. They admit independent finite
exact checks. Those checks do not
authenticate the external subconvex theorems, replace the
convergence arguments in Section 4, or prove the remaining
signed average.

The smallest new analytic inference whose failure would invalidate
the block theorem is (3.1): the principal rational radical must
have at most \(Z\) possible values, and the two split local
assignments must cost only a fixed number of choices per rational
prime. The proof gives both explicitly. No new estimate for a
reciprocal \(L\)-function is an unstated premise.
