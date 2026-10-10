# A pruned coupled theta mean square, including all three cusps

Status: proposed source-conditional analytic deductions. This note proves an improved estimate for the literal completed two-axis family over squarefree dual rows. It does not prove the fourth moment, the boundary 17/24, an all-row version of this two-axis estimate, or a moving-conductor A2 adapter. No numerical evidence or Lean build is used.

The first gain uses exact cancellation before taking norms. A further gain uses the literal Möbius coefficient in the remaining negative allocation and a convergent operator for its moving coprimality condition. The latter gain is not an arbitrary-divisor-coefficient theorem.

## 1. Exact inputs, object and quantifiers

The following source interfaces are retained as inputs, with their original analytic scope.

1. OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`: the completed theta reflection, its full scalar, fixed-ray uniformity, and transformed-weight bounds. The local file is in the October 7 upstream import. Relevant labels are `eq:reflection`, `eq:theta-local-factors`, `lem:reflection-uniformity`, `eq:theta-support`, `eq:theta-weight-decay`, and `eq:cusp-fourier-coefficients`/`eq:conjugate-cusp-coefficients` (lines 3090–3144).
2. PR #915, `9959364671f89b86f3992ec5ed5e19f804eb607b`, `COUPLED_THETA_COMPLETION.md`, Sections 1–3 and Lemma 6.1: exact coupled reflection, Ramanujan allocation, and the quadratic–cubic sieve with its moving row mask.
3. PR #920, `2edc467ef4dea4aa685219ac6a558a158b88768d`, `RAMANUJAN_SUPPORT_PRUNING.md`, Sections 3 and 5, and its proved `ALL_CUSP_REFLECTION.md` adapter: complete projected groups vanish uniformly when the negative allocation has norm greater than a fixed multiple of the square root of the original theta length.
4. For the stronger result only, the same PR's `HIGHER_ANGULAR_SECOND_MOMENT.md`, Theorem 6.2: conductor-uniform reciprocal control in real part greater than 11/12 for infinity type -3 and arbitrary finite character/masks. That theorem itself retains the imported canonical theorem and theta argument as inputs.
5. The explicit cusp coefficients in Dunn–Radziwiłł, *Bias in cubic Gauss sums*, arXiv:2109.07463v3, equations (5.7), (5.13), (5.14), pp. 16–18: https://arxiv.org/pdf/2109.07463. Only these coefficient formulas are needed for the all-cusp extension below; no RH-dependent estimate elsewhere in that paper is used.

Work over the Eisenstein integers with the source primary-generator convention. Write \(\alpha(a)=a/|a|\), \(\chi_a(k)=(k/a)_6\), with literal nonunit zeros, and
\[
a_\xi(a)=\overline{\alpha(a)}\gamma_2(a)\xi(a).
\]
Fix a finite bad set \(S\) containing the primes above 6, a fixed ray character \(\xi\), and two smooth norm weights \(W_1,W_2\) supported in fixed compact subintervals of \((0,\infty)\). Original indices \(a,k\) are good primary; \(a,k\) are squarefree. Reflected theta indices are **not** required to avoid \(S\).

Let \(T(B;k,a)\) be exactly the source theta completion with finite twist \(\xi(n)\chi_n(k)\chi_n(a)^4\) and weight \(W_2\). Define
\[
\mathcal C_{A,B}(k)=A^{-1/2}\sum_a^*
 a_\xi(a)\chi_a(k)W_1(Na/A)T(B;k,a).                    \tag{1.1}
\]
The star on a row sum means squarefree primary rows outside \(S\). In particular every conclusion below has the row sum \(\sum_{H\le Nk<2H}^{*}\). It is not the unrestricted row sum from an initial Möbius moment.

Assume \(A,B,H\ge1\) and all scales are bounded by a fixed power of an auxiliary \(D\ge2\). Constants in \(D^\epsilon\) may depend on that power, \(\epsilon\), the fixed data, and finitely many weight seminorms. An additional original mask \(\mathbf1_{(a,h)=1}\) is allowed in the stronger theorem if \(Nh\) is also polynomially bounded; it is retained in every Euler product and coefficient vector.

## 2. The cubic Gauss structure survives at every source cusp

The imported normalization is
\[
t_0(\ell)=\tau(\ell),\quad
t_-(\ell)=\omega^2\tau_1(\omega^2\ell)\breve e(\ell),\quad
t_+(\ell)=\omega\tau_2(\omega\ell)\breve e(\ell),\qquad
d_\sigma(\ell)=\overline{t_\sigma(-\ell)}.                \tag{2.1}
\]
The primary coefficient formulas express each nonzero coefficient at
\(\ell=u\lambda^mnb^3\), \(n\) squarefree, as the same normalized cubic Gauss coefficient in \(n\), multiplied by \(\sqrt{Nb}\), a fixed supplementary ray factor and a scalar of size \(O(3^{m/6})\). The extra cusps have \(m=-4\); the infinity cusp has its two permitted towers. Conjugation in (2.1) is the same conjugation as on the standard face, so the normalized coefficient is \(\gamma_2(n)\), with the source orientation, at all three cusps. The Gauss numerator changes only among a fixed list of units and powers of \(\lambda\). Thus this is more information than the absolute theta coefficient bound.

In particular, after writing \(n=e n'\), its variable two-axis factor is
\[
\gamma_2(en')=\gamma_2(e)\gamma_2(n')\chi_{n'}(e)^4.
                                                               \tag{2.2}
\]
Supplementary factors separate multiplicatively. Any additive phase in (2.1), after fixing the cube index and ramified valuation, has fixed bad denominator. A finite residue split therefore separates it into bounded coefficients on \(e\) and \(n'\). The number of classes is uniformly bounded: the negative ramified valuations have a fixed lower bound, and positive valuations introduce no new denominator. The same applies to the source's finite fixed-ray branches.

This argument retains all bad-prime factors. Split the squarefree \(S\)-part of \(n'\) first; there are finitely many possibilities. Its Gauss and character factors go into bounded row or column multipliers. Split the \(S\setminus\{\mathfrak p\mid3\}\)-part of the primary cube index as \(b_S\), retaining arbitrary powers. The cube index is prime to \(\lambda\); the arbitrary ramified valuation is already carried by \(m\). Its eventual weight has the summable mass
\[
\sum_{b_S\ (S\setminus\{\mathfrak p\mid3\})\text{-smooth}}\frac1{Nb_S}
=\prod_{\mathfrak p\in S,\,\mathfrak p\nmid3}
 (1-(N\mathfrak p)^{-1})^{-1}<\infty.                    \tag{2.3}
\]
The ramified coefficient divided by \(\sqrt{N\ell}\) contributes \(O(3^{-m/3})\), \(m\ge-4\), which is also summable. Its effect on the effective squarefree length is a factor \(3^{-m}(Nb_S)^{-3}\); its bounded lowest valuations can be absorbed into fixed constants. These facts justify using the same quadratic–cubic coefficient structure at all cusps without deleting dual primes in \(S\).

## 3. Prune complete groups before allocating or taking norms

For \(a\) squarefree the exact Ramanujan identity is
\[
\prod_{p\mid a}(-1+Np\mathbf1_{p\mid nb})
 =\sum_{dg=a}\mu(g)Nd\,\mathbf1_{d\mid nb}.             \tag{3.1}
\]
PR #920's all-cusp support theorem concerns the entire completed frequency sum for each fixed \((d,g)\). It gives zero when
\[
Ng>C_S\sqrt B.                                         \tag{3.2}
\]
Its constant is uniform in the original row and all good arithmetic labels. The complete sum includes the cube index, every ramified valuation, and every positive allocation. Nothing here asserts vanishing of an individual frequency or dyadic piece.

Choose a fixed smooth cutoff equal to one on \([0,1]\) and zero on \([2,\infty)\), and insert it at \(Ng/(C_S\sqrt B)\) into (3.1). This leaves the completed sum exactly unchanged: only complete groups already equal to zero are altered. **Only now** expand
\[
\mathbf1_{d\mid nb}
=\sum_{ef=d}\mathbf1_{e\mid n}\mathbf1_{f\mid b}
                       \mathbf1_{(f,n)=1},
\]
write \(n=en'\), \(b=fb'\), and introduce norm dyads. The surviving dyadic scales obey
\[
EFG\asymp A,\qquad G\ll T:=\min(A,\sqrt B),             \tag{3.3}
\]
where fixed support constants are absorbed. The smooth cutoff has uniform logarithmic derivatives on each dyad. This order of operations retains the exact cancellation needed for (3.3).

The source scalar cancellation and the normalizations from PR #915 give, up to fixed factors and common smooth norm kernels,
\[
\frac{1}{\sqrt A}
\frac{\mu(g)}{\sqrt{Nf\,Ng}\sqrt{Nn'}\,Nb'}
\times\text{bounded separate arithmetic factors}
\times\chi_k(gn'b')^3\mathbf1_{(k,ef)=1}
\times\chi_{n'}(e)^4.                                  \tag{3.4}
\]
The angular factor on \(g\) is \(\overline{\alpha(g)}^3\); its remaining finite multiplier is a fixed ray character. The conditions \((g,ef)=1\) remain. There is **no** condition \((g,n'b')=1\).

On the dyad \(Nb'\asymp C\), and after the fixed bad-prime splits, the squarefree reflected length is bounded by a constant times
\[
U\asymp \frac{Y}{3^m (Nb_S)^3 C^3},\qquad
Y:=\frac{H^2 E G^2}{BF}.                                \tag{3.5}
\]
Use the imported bounds on every logarithmic derivative of the transformed weight to separate its norm variables before applying any sieve. A smooth dyadic partition makes the Mellin coefficients bounded by a common integrable majorant, with rapid tails when the ratio in (3.5) leaves the effective range. Arithmetic Gauss, angular and character factors are coefficients; no arithmetic factor is differentiated.

## 4. A whole-family gain using the known two-sieve estimate

For reference the precise PR #915 quadratic–cubic lemma is
\[
Q_k(E,U)=\frac1{\sqrt{EU}}\sum_{e,n}^*
u_e v_n\mathbf1_{(k,e)=1}\chi_k(n)^3\chi_n(e)^4,
\]
\[
\sum_k^*|Q_k(E,U)|^2\ll (HEU)^\epsilon F(E,U,H),\quad
F(E,U,H):=\frac{H+U}{U}[E+U+(EU)^{2/3}],                 \tag{4.1}
\]
for bounded separate coefficient vectors, including fixed additional exclusions. This is obtained by expanding the row mask over its common divisor, applying the quadratic sieve and then the cubic sieve. Its common-divisor costs are the six convergent or logarithmic sums with powers \(3,2,8/3,2,1,5/3\). Thus the row mask has not been dropped as if independent of the column.

The all-cusp coefficient adapter of Section 2 permits (4.1) on every branch of (3.4). Freeze \(f,g,b'\). The actual squared prefactor relative to (4.1) is \(E/(AFG)\). Minkowski over the \(O(FG)\) labels \(f,g\) costs \((FG)^2\), and \(EFG\asymp A\) cancels this prefactor. The cube weight has mass \(\sum_{Nb'\asymp C}(Nb')^{-1}=O(1)\) on each dyad. Equations (2.3) and (3.5) make all ramified and bad-prime tails summable.

For \(1\le U\ll Y\), expansion of (4.1) gives
\[
F=H+U+HE/U+E+HE^{2/3}U^{-1/3}+E^{2/3}U^{2/3}
\ll HE+Y+(EY)^{2/3}.                                  \tag{4.2}
\]
If \(Y<1\), no sieve at subunit length is needed: nonzero frequencies have a rapidly decreasing transformed tail, bounded by the same expression. Dyadic sums and the finitely many branches cost at most \(D^\epsilon\). Therefore every surviving allocation block satisfies
\[
\sum_k^*|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon[HE+Y+(EY)^{2/3}].                        \tag{4.3}
\]

### Theorem 4.1: completed family after exact pruning

With the fixed data and source inputs of Section 1,
\[
\boxed{\sum_{k\asymp H}^*|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon\left[
HA+\frac{H^2A}{B}\,T+
\left(\frac{H^2A^2}{B}\right)^{2/3}\right],\quad
T=\min(A,\sqrt B).}                                    \tag{4.4}
\]
The same bound holds with any row-independent coefficient \(v(a)\) bounded by \(D^\epsilon\) for every \(\epsilon>0\) on the allowed support.

**Proof.** Insert the cutoff before the allocations as in Section 3. In (4.3), use \(E\ll A/(FG)\), obtaining
\[
HE\ll HA,\quad
Y\ll H^2AG/(BF^2)\ll H^2AT/B,\quad
EY\ll H^2A^2/(BF^3)\ll H^2A^2/B.
\]
Minkowski over the logarithmically many norm blocks proves (4.4). An outer \(v(a)\) preserves the exact zero of each complete group; after freezing \(f,g\), it is the bounded coefficient \(v(efg)\) in the \(e\)-vector in (4.1). No multiplicativity of \(v\) is used here. QED.

For \(A=B=D\) this reads
\[
\boxed{\sum_{k\asymp H}^*|\mathcal C_{D,D}(k)|^2
\ll D^\epsilon[HD+H^2D^{1/2}+H^{4/3}D^{2/3}].}          \tag{4.5}
\]
It is \(O(D^{2+\epsilon})\) for \(1\le H\le D^{3/4}\). This estimate is for the whole completed family, including all three cusps, rather than one positive allocation.

## 5. A convergent operator for the negative allocation's exclusion

Here the literal Möbius coefficient gives a second gain. The relevant imprimitive character is
\[
\chi_{k,f,h}(g)=\eta(g)\overline{\alpha(g)}^3\chi_k(g)^3
                  \mathbf1_{(g,fhS)=1},                 \tag{5.1}
\]
where \(\eta\) belongs to a fixed finite set of ray characters. Finite residue restrictions on \(g\) are expanded into that fixed set. Its finite modulus has polynomial norm in the allowed scales and \(Nh\). Input 4 gives, for every fixed \(\sigma>11/12\),
\[
|L(\sigma+it,\chi_{k,f,h})^{-1}|
\ll D^\epsilon(2+|t|)^\epsilon.                          \tag{5.2}
\]
The literal zero masks at \(k,f,h,S\) are part of this L-function. Infinity type -3 is essential: a theorem only for finite-order characters would not imply (5.2).

### Lemma 5.1: the moving e-exclusion is bounded in the two-sieve norm

Fix \(s=\sigma+it\), \(\sigma>1/2\). In (4.1), multiply the summand with index \(e\) by
\[
M_k(e;s)=\prod_{p\mid e}(1-\chi_{k,f,h}(p)(Np)^{-s})^{-1}.
                                                               \tag{5.3}
\]
Then the resulting row vector has norm at most a constant depending on \(\sigma\), times \((HEU)^\epsilon F(E,U,H)^{1/2}\), uniformly in \(t\) and the moving labels. Separate bounded e/n coefficient vectors and the original row mask are retained.

**Proof.** Expand the finite Euler product, absolutely, as
\[
M_k(e;s)=\sum_{\operatorname{rad}(d)\mid e}
           \chi_{k,f,h}(d)(Nd)^{-s}.                    \tag{5.4}
\]
For a fixed \(d\), put \(r=\operatorname{rad}(d)\) and write \(e=r e'\). The index \(e'\) is squarefree and coprime to \(r\). All scalar factors depending on \(r,d\) and the row have modulus at most one. The factor \(\chi_n(r)^4\) belongs to the n-vector; the mask \((k,r)=1\) is a fixed row restriction; the original moving mask \((k,e')=1\) remains. Thus the fixed-d row vector is bounded by (4.1) at e-length \(E/Nr\), multiplied by the normalization ratio \((Nr)^{-1/2}\). Since \(F\) is increasing in its first argument, its norm is at most
\[
(HEU)^\epsilon (Nr)^{-1/2}F(E,U,H)^{1/2}.
\]
Bounded nonempty scales are absorbed in a fixed annulus; if \(r\) exceeds the e-support the term is zero. Minkowski is now justified by the convergent product
\[
\sum_d (Nd)^{-\sigma}(N\operatorname{rad}d)^{-1/2}
=\prod_p\left(1+
 \frac{(Np)^{-\sigma-1/2}}{1-(Np)^{-\sigma}}\right)<\infty.
                                                               \tag{5.5}
\]
The convergence condition is precisely \(\sigma+1/2>1\). This proves the lemma. QED.

This proof does not estimate (5.3) by an uncontrolled growing row-dependent coefficient inside the cubic sieve. It resolves the coefficient as a sum of operators, each with an explicit summable norm loss.

## 6. Use the Möbius g-sum before the row norm

After the common Mellin separation in Section 3, the g-sum is a compact smooth dyadic sum with the literal coefficient \(\mu(g)\chi_{k,f,h}(g)\), together with \((g,e)=1\). Its Mellin Dirichlet series, initially in real part greater than one, is exactly
\[
\sum_{(g,e)=1}\frac{\mu(g)\chi_{k,f,h}(g)}{(Ng)^s}
 =L(s,\chi_{k,f,h})^{-1}M_k(e;s).                       \tag{6.1}
\]
The factor \((Ng)^{-1/2}\) in (3.4) is absorbed into the smooth dyadic profile with its explicit scale \(G^{-1/2}\). Smooth oscillatory factors from the other norm variables are separated first. Their Mellin parameters simply translate the g variable's imaginary part, and are controlled by the common rapid majorant.

Move the g-Mellin contour to fixed \(\sigma\in(11/12,1)\). There are no poles: (5.2) is holomorphic on a slightly larger half-plane, and each factor of (5.3) is nonzero for real part greater than zero. Horizontal integrals vanish by rapid Mellin decay and the polynomial/subpower vertical bound. Formula (5.2) is a row scalar, while Lemma 5.1 handles the remaining dependence on e. Thus, in the norm calculation of Section 4, the count of \(O(G)\) g-labels is replaced by
\[
O(D^\epsilon G^\sigma)
\]
with the same normalized two-sieve bound. The f-labels still cost \(O(F)\) by Minkowski. This is legitimate before Cauchy: all norm kernels have already been separated, and the common Mellin majorant is integrable after multiplying by the subpower losses. The exact support cutoff is one of these smooth profiles.

Consequently the old squared prefactor \(E/(AFG)\) is multiplied by \(F^2G^{2\sigma}\), not \((FG)^2\). Since \(EFG\asymp A\), the surviving factor is \(G^{2\sigma-2}\). This proves
\[
\boxed{\sum_k^*|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon G^{2\sigma-2}
            [HE+Y+(EY)^{2/3}].}                         \tag{6.2}
\]
All original masks involving g and k remain in (5.1); g is still permitted to share primes with the reflected squarefree and cube indices. An extra \((a,h)=1\) only adds e/f restrictions and the base exclusion in (5.1), so (6.2) is uniform for that mask.

### Theorem 6.1: angularly improved pruned completion

For each fixed \(11/12<\sigma<1\), under all four analytic inputs of Section 1,
\[
\boxed{\sum_{k\asymp H}^*|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon\left[
HA+\frac{H^2A}{B}T^{2\sigma-1}
 +\left(\frac{H^2A^2}{B}\right)^{2/3}\right].}            \tag{6.3}
\]
The bound is uniform with an additional original mask \((a,h)=1\) of polynomially bounded norm.

**Proof.** Apply exact pruning and (6.2). The first term is at most \(HA\) because \(G\ge1\) and \(2\sigma-2<0\). Substituting \(E\asymp A/(FG)\), the second term is at most \(H^2 A G^{2\sigma-1}/B\), maximized at \(G\ll T\), since \(2\sigma-1>0\). The third is at most \((H^2A^2/B)^{2/3}\), because its additional factors are \(F^{-2}G^{2\sigma-2}\le1\). Sum the norm blocks and finite branches. QED.

At balanced lengths, choose \(\sigma-11/12\) sufficiently small in terms of the final \(\epsilon\). This gives the endpoint-exponent notation
\[
\boxed{\sum_{k\asymp H}^*|\mathcal C_{D,D}(k)|^2
\ll D^\epsilon[HD+H^2D^{5/12}+H^{4/3}D^{2/3}].}          \tag{6.4}
\]
No estimate on the line \(\sigma=11/12\) is asserted. For every final epsilon the proof first chooses a fixed positive margin and absorbs its loss. In particular (6.4) is \(O(D^{2+\epsilon})\) for
\[
\boxed{1\le H\le D^{19/24}.}                            \tag{6.5}
\]

For general lengths the corresponding diagonal-size range, with fixed margins absorbed into epsilon, is
\[
H\le\min\{B,\ B T^{-5/12},\ B^{5/4}A^{-1/4}\},
\qquad T=\min(A,\sqrt B).                              \tag{6.6}
\]
The first constraint is redundant when \(T\ge1\), but records the separate \(HA\) term. Theorem 4.1 instead has \(B T^{-1/2}\) in the middle constraint.

The literal coefficient qualification matters. A general multiplier \(v(efg)\), even divisor bounded and independent of the row, destroys (6.1). Theorem 4.1 tolerates it; Theorem 6.1 does not assert that extension. Products of fixed smooth norm factors and original coprimality masks have been treated explicitly and are permitted.

## 7. What this gains, and the precise remaining adapter

Theorems 4.1 and 6.1 improve the completed theta estimate by combining exact support pruning with arithmetic structure before taking norms. The 19/24 in (6.5) is a **dual-row range exponent for a completed family**. It is not a zero-free boundary and is unrelated to proving the target zeta boundary 17/24.

For comparison, grouping the raw balanced squarefree Gauss polynomial into its length-AB column and using the ordinary cubic/sextic large sieve gives, with its normalized divisor-bounded coefficients,
\[
H+AB+(HAB)^{2/3}.
\]
The same envelope holds for the completion itself: expand its physical cube index as in PR #918 Corollary 3.3, use the squarefree-row sieve for each shortened column, and sum the weights \(1/Nb\). The H term costs only a logarithm, and the AB and cross terms have convergent cube sums. On squarefree dual rows this elementary envelope already reaches \(O(AB D^\epsilon)\) at balanced lengths through \(H\le D\).

Consequently (6.5) is an improvement of the reflected estimate and its subdiagonal size, not an extension of the largest AB-threshold already supplied by the elementary sieve. For example, at \(A=B=D\), \(H=D^{1/2}\), (6.4) gives \(O(D^{3/2+\epsilon})\); the elementary envelope and the old whole-reflection estimate both give only \(O(D^{2+\epsilon})\). At \(H=D^{3/4}\), the new angular bound is \(O(D^{23/12+\epsilon})\), versus \(O(D^{2+\epsilon})\) from the elementary envelope and from (4.5). These are actual mean-square savings for the specified completed object. They should not be converted into a raw-polynomial or Möbius-moment range merely by substituting a dual-length formula.

The exact cube inversion from PR #918 permits masks \((a,h)=1\) and a coefficient \(1/Nh\), which are compatible with Section 6. Its A2/cube children have
\[
A'=\frac{A}{Nc\,(Nd)^2(Ne)^2},\qquad
B'=\frac{B}{(Nc)^2Nd\,(Ne)^2(Nh)^3},                    \tag{7.1}
\]
at the same row height. The admissible range (6.6) is not invariant under these shortenings: nonempty children with \(B'\asymp1\) require bounded H already from \(H\le B'\). Even the child with all four labels equal to one retains the original restriction. Thus the positive weights in the exact composition do not supply an all-child estimate from (6.6).

Moreover the moving A2 conductor labels \(q,f\) alter the local reflection and phases; this note has proved no uniform adapter for those labels. It also has only squarefree dual rows. The unrestricted sixth-power-copy rows cannot be discarded. The source's all-row decomposition \(k=u_0 s v^2\) changes the auxiliary theta twist to one involving \(a v^2\). Applying the source's one-axis argument to this two-axis family would require a separate uniform treatment of its local factors, full scalar, and norm costs; that adapter has not been proved here. A full fourth-moment claim would require a proved all-row, moving-conductor uncompletion/covariance theorem; none is inferred here.

The largest actual new statement is (6.3), conditional on the pinned source analytic framework and its angular extension. The weaker (4.4) uses no angular zero-free input and admits arbitrary fixed-order outer divisor weights. Both preserve every reflected cusp, every source zero, and the complete-group order of cancellation.
