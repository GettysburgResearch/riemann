# The exact prime-amplified fourth-power small-core component

24 October 2026. New research note, separate from the frozen fourth-pass
packet. Status: proposed source-dependent component, submitted for
independent review. This note keeps the actual prime product through the
root-number representation. It proves no new M2 capacity or numerical
zero-free boundary.

## 1. Inputs and the physical squarefree row family

Use the primary-ideal conventions and finite reciprocity partitions of
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, the quasi-Riemann
source `arithmetic_lane/ope26a_source.tex`, especially `old-eq:1.2`,
`old-eq:2.1d`, and the selected-prime discussion. The exact source SHA256
is `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
For the cubic norm, use `NATURAL_PRESENTATION_TWIST_EXTENSION.md` at
the fourth-pass mathematical commit
`GettysburgResearch/riemann@8c88fd23300bba093ce2f78295c4e27dbd60147d`,
SHA256 `fda494d598fa01a5f6c652b9bf503bad2fc95f4fe1a3af7e594b41b43ce6775f`.
Its all-finite-character hypothesis \(\mathrm{ZF}_\beta\) remains
an assumption here. No later enlargement of its conductor range is used.

The original row \(u\) is squarefree, good, primary, and has
\(Nu\asymp U\). Write \(\psi_u^*\) for the primitive
inducing character and \(\psi_u^0\) for its original presentation,
including all fixed omitted primes. Away from those fixed primes it
is \(\nu(n)\chi_{6,u}(n)\), after a fixed reciprocity
partition, with \(\nu\) in a fixed finite ray family. The
primitive character is nonprincipal, finite order, and has trivial
infinite type and conductor norm \(Q_u=c_\nu Nu\). Bounded
unit/principal rows are excluded before reflection. This is the squarefree part of
the physical family, not an assertion about every sixth-power-free row
or the source's complete moving-twist M2 induction.
For the literal reflection normalization put
\(C_u=3Q_u/(2\pi)^2\), as in the source's `old-eq:2.1d`.

Write the actual selected prime product as
\[
 \mathcal Q_u=\prod_{i=1}^j
   P_i^{-1/2}\sum_{p\text{ prime}}
       a_i(p)\psi_u^0(p)W_i(Np/P_i),
 \qquad L=\prod_i P_i.
 \tag{1}
\]
The slot count is fixed; the underlying prime supports are pairwise
disjoint; all zeros and original fixed exclusions are retained.
The coefficients are the fixed finite-ray combinations in the source,
independent of \(u\) and of the other selected primes. Norm heights
are kept in the smooth profiles. Parameters are common to a row sum.

For the root-number identity, the frozen fourth-power note proves
\[
 \overline{\varepsilon_u}^{\,2}
   =\mu(u)\overline{\gamma_2(u)}\,\theta(u),
 \tag{2}
\]
where \(\theta\) has fixed angular and finite-ray data. The
common norm twist at a nonzero central height can also be included.
This is the orientation matching the whole conjugate of the structured
cubic moment.

The same root coefficient occurs for the actual plain witnesses.
First let \(S_u(N;W)\) denote the primitive centrally normalized
full smooth sum of \(\psi_u^*\). For these primitive sums,
reflect each of the two conjugate factors in
\(|S_u(N_1;W_1)S_u(N_2;W_2)|^2\). The source's exact primitive
reflection gives
\[
 \overline{\varepsilon_u}^{\,2}
 S_u(N_1;W_1)S_u(N_2;W_2)
 S_u(C_u/N_1;W_1^\vee)S_u(C_u/N_2;W_2^\vee).
 \tag{3}
\]
Here \(W_i^\vee\) is the reflected profile of the conjugate
original profile. The product (3) equals the original positive product;
it is not an inequality. The product of its four principal norm scales
is \(C_u^2\asymp U^2\).

For the actual fixed-puncture sums, use the source's natural reflection
before asserting (3). On a fixed ray sector let \(R_0\) be the
fixed radical of the redundant omitted primes. The exact formula is
\[
 S_u^0(N;W)=\varepsilon_u
 \sum_{\substack{e\mid R_0\\\operatorname{rad}f\mid R_0}}
 \frac{\mu(e)\psi_u^*(e)\overline{\psi_u^*(f)}}
      {\sqrt{Ne\,Nf}}
 S_{\overline{\psi_u^0}}
       \left(\frac{C_uNe}{N\,Nf};W^\sharp\right).
 \tag{3a}
\]
Apply its conjugate version to each conjugate plain factor. The
reflected characters then have the same natural presentation
\(\psi_u^0\) as the two original factors. The \(e\)'s have
bounded fixed norm; the \(f\)'s lower the reflected scales.
The coefficient mass in (3a) is absolutely summable, since \(R_0\)
is fixed and each geometric series is weighted by \((Nf)^{-1/2}\).
The phases at these fixed primes range over a fixed finite ray family
as functions of \(u\), so they enter \(\theta\) in (2).
They are not arbitrary row coefficients. A fixed sufficiently large
polynomial cutoff on \(Nf\) has an arbitrarily small tail by
Rankin's bound with any exponent below one half; the source's rapid
profile decay also covers reflected scales below the first nonempty
annulus. The proof below is uniform in the retained scales. Its
component bounds can therefore be summed with this absolute coefficient
mass. Upper scales differ from \(C_u^2\) only by a fixed factor,
and all original fixed column and prime zeros remain present.

The central fourth-power AFE gives the analogous
signed expression with coefficient \(d_4(n)\) and total norm length
\(Q_u^2\), with the fixed field factor absorbed in its AFE profile,
as proved in the frozen fourth-power note.
If its primitive Dirichlet series includes a fixed omitted prime,
extract that prime's powers first; their coefficient mass is bounded
by \(\sum_{j\ge0}(j+1)^3(Np)^{-j/2}<\infty\).
The resulting phases are in the same fixed finite ray family and the
remaining variable \(n\) is good.

Common Mellin separation of the conductor-dependent profiles is taken
before the row sum. On an original four-variable product dyad
\(Nn\asymp X\), the coefficient has a fixed divisor bound times
\(X^{-1/2}\). For the reflected plain products, lower annuli
add a coefficient of size at most one to this bound. Upper annuli have
arbitrary decay. Thus the model below applies to both actual sources.

## 2. Every prime coincidence and square-core overlap

Expand \(|\mathcal Q_u|^2\). For a fixed coincidence pattern,
let \(D\) be the product of primes chosen identically on the two
sides, and let \(P,Q\) be the two unmatched products. The ideals
\(D,P,Q\) are pairwise coprime and squarefree. The row phase is
\[
 1_{(u,D)=1}\chi_{6,u}(P)\overline{\chi_{6,u}(Q)}.
 \tag{4}
\]
Fixed ray factors are in the row-independent coefficients. The
normalization is still \(L^{-1}\), including coincident slots.

Write \(n=t h^2\), with \(t\) squarefree. Split
\[
 P=ac,\qquad Q=bd,\qquad t=sab,
 \qquad (s,PQ)=1.
 \tag{5}
\]
Thus \(a=(t,P)\) and \(b=(t,Q)\). The ideals
\(a,b,c,d\) are pairwise coprime. There is no requirement that
\(h\) be coprime to any of them. Define
\[
 v=scd,\qquad k=ad^2h.
 \tag{6}
\]
Then \(v\) is squarefree, and the following identity includes
all natural zeros:
\[
 \boxed{
 1_{(u,D)=1}\chi_{6,u}(th^2)
       \chi_{6,u}(P)\overline{\chi_{6,u}(Q)}
 =1_{(u,Db)=1}\chi_{6,u}(v)\chi_{3,u}(k).
 }
 \tag{7}
\]
At a prime of \(a\), the exponent is two and is carried by
the cubic row \(k\). At a prime of \(b\), the exponent
cancels on units but its zero remains in the mask. At primes of
\(c,d\), the exponents are respectively one and five; the latter
is one in \(v\) plus four in \(k^2\). This checks (7)
locally even when a prime also divides \(h\) or \(u\).

The common natural twist in the \(u\) column therefore has full
good radical
\[
 R=\operatorname{rad}(vDb).
 \tag{8}
\]
Primes of \(a\) need not be included separately: their natural
zero is already present in the live cubic row \(k\). A redundant
prime of \(b\) is included even though its unit phase canceled.
This is the precise allocation that avoids charging every prime as
an additional conductor twist.

Let the norm scales of \(D,b,d,v,k\) be respectively
\(D_0,S,E,T,A\). Each pattern fixes the prime-slot subsets, so
\[
 L\asymp D_0SE,\qquad
 A\asymp\frac{\sqrt X\,E^3}{\sqrt T},\qquad
 NR\ll T D_0S\asymp TL/E.
 \tag{9}
\]
The middle identity follows exactly from
\(nPQ^5=b^6vk^2\). All displayed comparability constants depend
only on the fixed slot count and annular supports.

## 3. The coefficient energy retains the prime normalization

After (7), collect the coefficients of each \((v,D,b,k)\),
including the original normalization \((L\sqrt X)^{-1}\).
Call them \(c_{v,D,b}(k)\). Common Mellin parameters are fixed
at this stage. The coefficients are independent of \(u\).
Their squared mass is
\[
 \sum_{v,D,b,k}|c_{v,D,b}(k)|^2
 \ll (UXL)^\epsilon
       \frac{D_0S\,T A}{E^2XL^2}.
 \tag{10}
\]

Here is the counting proof, including the sparsity used in (10).
For fixed \(v,D,b\), both \(c\) and \(d\) divide
\(v\), so their possible assignments have fixed divisor
multiplicity. For such an assignment, \(k=ad^2h\). If
\(Na\asymp A_0\), counting \(a\) and \(h\) gives
\(O(A_0)O(A/(A_0E^2))=O(A/E^2)\), up to small powers.
A nonempty bounded annulus has the same bound after enlarging its
fixed constant; a genuinely empty subunit annulus contributes nothing.
For a fixed output \(k\), the possible \(a\)'s divide
\(k\), again with fixed divisor multiplicity. The original four
plain factors or \(d_4\) coefficient add another fixed divisor
power. There are at most \(O(D_0ST)\) choices for
\((D,b,v)\). Dividing the resulting count by \(XL^2\)
proves (10). No free count of unmatched negative primes is paid:
their remaining product \(d\) must divide \(v\).

Let \(J_R(A,U)\) be the normalized cubic norm of the whole
conjugate natural-presentation theorem, with the column twist
specified by (7)--(8). Cauchy over \((v,D,b,k)\), followed by
that theorem for each fixed \((v,D,b)\), gives the general
component bound
\[
 \boxed{
 |\mathcal C_{X,T}|\ll(UXL)^\epsilon
    \frac{U^{1/2}T A^{1/2}}{X^{1/2}E^2}
    \sup_{v,D,b}J_R(A,U)^{1/2}.
 }
 \tag{11}
\]
The factor \(U^{1/2}\) restores the unnormalized root-number
column. In simplifying (11), \(L\asymp D_0SE\) cancels
all apparent factors from counting the prime pairs. The normalized
moment is applied only after fixing its whole natural presentation.
It is not applied with a different coefficient twist at each live
cubic row.

## 4. A below-volume bound for the combined small cores

Shrink the positive saving in the natural theorem to a fixed
\(0<\eta<1/12\). For \(A\le U\), its rectangular
bound gives \(J_R(A,U)\ll A^{1/3}U^{1-2\eta}\), up to
small powers, provided
\[
 TL/E\le\{U/(U/A)^{1/3}\}^{2/3}.
 \tag{12}
\]
In the parameters (9), a sufficient form of (12) is
\[
 T\le U^{2/5}X^{1/10}E^{3/2}L^{-9/10}
 \tag{13}
\]
with a fixed strict exponent margin. Substitution in (11) yields
\[
 \boxed{
 |\mathcal C_{X,T}|
 \ll(UXL)^\epsilon U^{1-\eta}X^{-1/6}T^{2/3}.
 }
 \tag{14}
\]
Thus the useful bound has no positive power of the total prime scale.
The core in (14) is the **combined** squarefree core \(v\),
not the original squarefree core \(t\).

For completeness, when \(A\ge U\), require
\(TL/E\le U^{2/3}\) and use the original full moment in
(11). Its volume term is
\[
 U^{1/2}T^{1/2}E.
 \tag{15}
\]
Its other term is
\[
 U^{5/6-\eta/2}X^{-1/12-\eta/4}
       E^{1/2-3\eta/2}T^{7/12+\eta/4}.
 \tag{16}
\]
The condition \(A\ge U\) implies
\(T\ll XE^6/U^2\). At the upper endpoint, (15)--(16)
are at most
\[
 U^{-1/2}X^{1/2}E^4,
 \qquad U^{-1/3-\eta}X^{1/2}E^4,
 \tag{17}
\]
respectively. Their exponents in \(T\) are positive.

Fix \(\delta>0\) and suppose
\[
 L\le U^{1/12-\delta}.
 \tag{18}
\]
For \(X\le U^2\), retain all components satisfying
\[
 T\le X^{1/4}U^{3\eta/4}.
 \tag{19}
\]
Take \(\eta\) smaller if necessary. In the branch \(A\le U\),
the conductor condition holds with a fixed margin: after substituting
(19) in (12), it suffices that
\[
 L\,X^{1/6}U^{5\eta/6}\le U^{4/9},
\]
which follows from (18), \(X\le U^2\), and
\(1/12+5\eta/6<1/9\). Equation (14) is then at most
\(U^{1-\eta/2+\epsilon}\). In the branch \(A\ge U\),
\(NR\ll LE^5\le L^6<U^{1/2}\), and (17) is at most
\(U^{5/6-4\delta}+U^{1-\eta-4\delta}\), up to small powers.

There are finitely many prime-membership patterns and logarithmically
many dyads. Consequently the sum of all components (19) is bounded
by \(U^{1-\eta/3}\), after shrinking the saving and choosing
the subsidiary losses. The same conclusion includes the standard
upper-profile tails: retain \(X\le U^{2+\zeta}\) for
\(\zeta\) sufficiently small compared with \(\eta,\delta\),
then use arbitrary fixed decay outside. Formula (17) costs only
\(U^{\zeta/2}\) in the retained enlargement.

For fixed bounded norm heights this completes the component estimate.
A positive height range \(U^{\tau_0}\) is also allowed after
the finite profile and tail orders are fixed: choose \(\tau_0\)
so their polynomial height loss is below the reserved saving, the
fourth-power/paired-reflection enlargement fits \(U^\zeta\),
and the common cubic-column heights fit the natural adapter. This is
the same order of choices as the frozen unamplified fourth-power note.
No arbitrary row-dependent height or class mask is inserted into (11).

## 5. Relation to the M2 capacity edge and the remaining sum

For two copies of a plain witness of length \(U^m\), the
source's present prime capacity is \(2m+6\kappa z\le1\),
where \(L=U^z\). Whenever \(m\ge1/3\) and
\(\kappa>2/3\), this implies
\[
 z\le\frac1{18\kappa}<\frac1{12}.
\]
Thus (18) has a fixed margin in that range. The actual selected
prime product can be kept in the controlled component without the
pointwise charge \(L^{2\beta-1}\).

This does not yet improve the capacity. The remaining signed sum is
exactly the same expansion with
\[
 Nv>X^{1/4}U^{3\eta/4},
\]
all prime-slot coefficients, the mask \((u,Db)=1\), and the
phase
\[
 \mu(u)\overline{\gamma_2(u)}\theta(u)
    1_{(u,Db)=1}\chi_{6,u}(v)\chi_{3,u}(k).
 \tag{20}
\]
Its coefficient retains the sparse factorization conditions in
(5)--(6). In a disjoint prime pattern with \(n\) itself
squarefree and prime to \(PQ\), the combined core is
\(v=nPQ\), of norm \(\asymp X(L/D_0)^2\). Such
configurations are not excluded by trivial common supports. At
\(X\asymp U^2\), they lie far outside (19). The source's
capacity-limiting common-support-free edge supplies no condition
forcing them into the controlled range.

The complete original moment remains positive, but these reflected
core components are signed. Its original pair diagonal has not been
removed or replaced by a positive small-core contribution. A bound for
the selected small-core sum cannot by itself bound the whole moment or
a detected class. A complete application still requires a new estimate
for (20), and the non-squarefree part of the physical row family must
also be accounted for. The present result identifies a component with
the actual prime correlations intact; it does not claim those missing
steps.
