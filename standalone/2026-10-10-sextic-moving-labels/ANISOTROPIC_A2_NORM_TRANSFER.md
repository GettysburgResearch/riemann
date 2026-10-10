# The full A2 correction sum inherits the improved raw norm

**Status:** proposed source-conditional theorem. The full arithmetic A2 completion, including all five local incidence labels and every nonzero element row, satisfies the same balanced positive-norm estimate as the improved raw two-axis polynomial. The proof uses an anisotropic version of the sixth-power-stratified inverse, with a cube cutoff scaled separately to each A2 child. This closes the unsigned correction sum at the displayed scale and label costs. It does not estimate the centered signed first-Poisson comparison or prove the original fourth moment.

**Exact dependencies.**

- PR #914, commit **0cc0428fedbbfc340044c7451b3d392c1da9a103**, *standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md*, Theorem 4.1: the exact five-label A2 coefficient and forward projection.
- PR #918, commit **cfa102748b26f840ccc4b963a660711424db0ec3**, *standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md*: the normalized A2 weights, physical mixed completion and masked cube inverse.
- This packet's *MIXED_LABEL_COMPLETION.md*, Theorem 2.1 and Lemma 7.1: the all-row completed estimate with the precise costs \(1,FQ,F^{2/3}Q^{1/3}\), outer-mask uniformity, and exact inverse/tail identities.
- This packet's *SIXTH_POWER_STRATIFIED_INVERSE.md*, Sections 2–5: the sixth-power-free row sieve, disjoint sixth-power row decomposition, and exact six-term optimization. Its source sieve is PR #913, commit **6498d6cc2eded03159c7332b25fd224ad07f89c1**, *REFINED_ALL_ROW_SIEVE.md*.

The fixed theta, cusp, sieve and angular assumptions attached to those theorems are retained. The scalar exponent \(\beta=1\) needs only counting in the scalar step; the exponent notation \(\beta=11/12\) uses the named source-conditional angular input with the fixed positive-margin convention. No new endpoint reciprocal bound is asserted.

## 1. Normalizations and scope

Use the Eisenstein field, fixed multiplicative generator convention, fixed finite bad set \(S\), finite ray character \(\xi\), and compact smooth positive-norm weights \(W_1,W_2\) from the companion mixed theorem. Every residue symbol retains its zero on nonunits. Set

\[
\lambda(a)=\overline{\alpha(a)}\xi(a),\qquad
a_\xi(a)=\lambda(a)\gamma_2(a).
\]

For squarefree \(q,f\) outside \(S\), possibly overlapping, and a polynomially bounded outer mask \(r\), the normalized raw polynomial is

\[
\mathscr P_{q,r}(A,B;k,f)
=\frac1{\sqrt{AB}}
\sum_{\substack{an\ {\rm squarefree}\\(an,qS)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
\mathbf1_{(a,r)=1}
W_1(Na/A)W_2(Nn/B).
\tag{1.1}
\]

The inner \(n\) may overlap \(r\). Write \(q_*=q/(q,f)\), \(Q=Nq_*\), \(F=Nf\). All displayed scales and labels are bounded by a fixed power of \(D\ge2\), except that the free inverse cutoff may be any positive real number. No analytic constant depends on that cutoff. The effective physical inverse support is bounded by the original scales.

An empty rectangle contributes zero. Nonempty rectangles below unit scale satisfy fixed support-dependent positive lower bounds: if the supports of \(W_i\) have upper endpoints \(b_i\), then \(A\ge1/b_1\) and \(B\ge1/b_2\). Such bounded nonempty scales are covered by replacing the scale by one and rescaling the fixed weight. The rescaling factors and the finite set of required seminorms are uniformly bounded on the resulting fixed compact interval. This convention is used explicitly for A2 children.

## 2. An anisotropic inverse estimate for every positive cutoff

Fix \(1/2<\beta\le1\), and put

\[
\kappa=\frac92-3\beta>0.
\tag{2.1}
\]

### Theorem 2.1. Anisotropic raw estimate

For every \(R>0\),

\[
\boxed{
\begin{aligned}
\sum_{k\asymp H}|\mathscr P_{q,r}(A,B;k,f)|^2
\ll_\epsilon D^\epsilon\bigg[
&HA+FQH^2A B^{\beta-3/2}R^\kappa\\
&+F^{2/3}Q^{1/3}H^{4/3}A^{4/3}B^{-2/3}R^2\\
&+H+ABR^{-3}+(HAB)^{2/3}R^{-2}
\bigg].
\end{aligned}
}
\tag{2.2}
\]

The row sum includes every nonzero element row in the annulus. The estimate is uniform in the stated masks and auxiliary overlaps. In particular, it does not require \(R\ge1\), \(A=B\), or a positive conductor gap.

### Proof

Write each original row uniquely as

\[
k=u\,v^6k_0,
\tag{2.3}
\]

where \(k_0\) is sixth-power-free and may share primes with \(v\). For fixed \(v\), the exact zero convention inserts the good-prime mask \(\operatorname{rad}(v)\) on every physical factor of the mixed completion. After removing the exclusions already imposed by \(f\), the new effective exclusion has norm

\[
Q_v\le QNv,\qquad H_v\ll H/(Nv)^6.
\tag{2.4}
\]

The variable \(k_0\) is averaged at physical height \(H_v\), not at the height of a newly enlarged row parameter. The fixed unit is included in the finite ray family. Bad-prime factors of \(v\) require no additional exclusion because all physical columns already avoid \(S\).

Choose a fixed \(K\ge1\) so that every nonempty inverse or physical cube index has norm at most \(K B^{1/3}\). It can also be chosen so that this cap is at least one whenever the original rectangle is nonempty. On the stratum \(v\), use the exact inverse cutoff

\[
R_v=\min(K B^{1/3},R\,Nv).
\tag{2.5}
\]

If \(R_v<1\), the short inverse is empty. If \(R_v=K B^{1/3}\), the long inverse is empty. These are exact finite-support assertions.

For the nonempty short part, apply the companion completed theorem at inner scale \(B_t=B/(Nt)^3\), retaining the inverse's outer mask \(rt\). Its middle factor satisfies

\[
B_t^{-1}\min(A,\sqrt{B_t})^{2\beta-1}
\le B_t^{\beta-3/2}
=B^{\beta-3/2}(Nt)^\kappa.
\tag{2.6}
\]

Fixed support constants cover the bounded nonempty \(B_t<1\) cases. Minkowski in the exact inverse coefficient \(1/Nt\), with its row phase used as a contraction after fixing \(t\), gives

\[
\|\mathcal S_v\|_2^2
\ll D^\epsilon\left[
H_v A
+FQ_vH_v^2 A B^{\beta-3/2}R_v^\kappa
+F^{2/3}Q_v^{1/3}H_v^{4/3}A^{4/3}B^{-2/3}R_v^2
\right].
\tag{2.7}
\]

The norm-level ideal sums are harmonic for the first term, bounded by \(R_v^{\kappa/2}\) for the second, and bounded by \(R_v\) for the third. The first logarithm is at most a fixed multiple of \(\log(2D)\) because of the physical cap. If \(R_v<1\), its short part is zero and (2.7) still supplies a valid nonnegative upper bound.

For the long part, use the exact regrouping

\[
d=t b,\qquad
c_{R_v}(d)=\sum_{\substack{t\mid d\\Nt>R_v}}\mu_K(t).
\tag{2.8}
\]

Its normalized raw child is \(\mathscr P_{q_v,rd}(A,B/(Nd)^3;k_0,f)\). The coefficient keeps \((d,q_vfS)=1\), and its exterior phase has modulus at most one. The ideal \(d\) need not be squarefree, \(t,b\) need not be coprime, and the inner raw squarefree factor may overlap \(d\).

For each fixed \(d\), the sixth-power-free row sieve gives the normalized bound

\[
D^\epsilon\left[
H_v+\frac{AB}{(Nd)^3}
+\frac{(H_vAB)^{2/3}}{(Nd)^2}
\right].
\tag{2.9}
\]

The row-independent \(q_v,f,r,d\) factors remain in its divisor-bounded coefficient vector. Its squared coefficient mass is \(D^\epsilon\) after normalization. The external \(\chi_d(k_0)^3\) is a norm contraction for each fixed \(d\).

Minkowski with the coefficient \(1/Nd\) and the convergent ideal tails yields

\[
\|\mathcal L_v\|_2^2
\ll D^\epsilon\left[
H_v+ABR_v^{-3}
+(H_vAB)^{2/3}R_v^{-2}
\right]
\tag{2.10}
\]

on the uncapped strata. This remains true when \(R_v<1\): the sums over all nonzero ideals are bounded, whereas \(R_v^{-3/2}\) and \(R_v^{-1}\) are at least one. Thus the inequalities

\[
\sum_{Nd>R_v}(Nd)^{-5/2}\ll R_v^{-3/2},
\qquad
\sum_{Nd>R_v}(Nd)^{-2}\ll R_v^{-1}
\tag{2.11}
\]

are valid for every \(R_v>0\). The harmonic first sum is truncated at the physical support. Capped strata have exactly zero long contribution.

The physical row classes indexed by \(v\) are disjoint. Sum their energies, using \(R_v\le R Nv\) in (2.7) and the exact equality \(R_v=R Nv\) on the uncapped strata in (2.10). The powers of \(Nv\) in the three short terms are

\[
-6,\qquad -12+1+\kappa=-13/2-3\beta,\qquad -17/3.
\tag{2.12}
\]

The three long terms have powers \(-6,-3,-6\). Every exponent is less than \(-1\), so the ideal sums converge. The permissible reference scales remain polynomially bounded because only \(Nv\ll H^{1/6}\) contribute. Assign sufficiently small preliminary epsilon losses before summation. This proves (2.2). \(\square\)

The extension to \(R<1\) is essential below: the correct cutoff of a small A2 child can be less than one even when the parent cutoff is large. Replacing it by one in all monomials would lose the scale cancellation used in the next section.

## 3. The exact normalized A2 projection

Let \(\mathfrak a_\xi(n_1,n_2)\) be the normalized full A2 coefficient in PR #914, with the fixed Gauss orientation. Its support has the unique five-label representation

\[
n_1=a c d^2 e^2,\qquad
n_2=b c^2 d e^2,
\tag{3.1}
\]

where \(a,b,c,d,e\) are pairwise-coprime squarefree ideals outside \(S\). On that support, with \(C=cde\),

\[
\mathfrak a_\xi(n_1,n_2)
=\sqrt{NC}\,\lambda(C)^3a_\xi(abe).
\tag{3.2}
\]

The phases in (3.2) are those of the globally twisted A2 coefficient. This is not an ordinary Euler-product approximation.

For squarefree starting labels \(q_0,f_0\), define the normalized full polynomial

\[
\mathscr Q_{q_0,f_0}(A,B;k)
=\frac1{\sqrt{AB}}
\sum_{\substack{n_1,n_2\\(n_1n_2,q_0S)=1}}
\mathfrak a_\xi(n_1,n_2)
\chi_{n_1n_2}(k)\chi_{n_1n_2}(f_0)^4
W_1(Nn_1/A)W_2(Nn_2/B).
\tag{3.3}
\]

The symbols on nonsquarefree indices use their multiplicative extension, including zeros.

For each disjoint squarefree correction triple \((c,d,e)\), with \((C,q_0f_0S)=1\), put

\[
A_t=\frac{A}{Nc\,(Nd)^2(Ne)^2},\qquad
B_t=\frac{B}{(Nc)^2Nd\,(Ne)^2},
\tag{3.4}
\]

\[
q_t=q_0 C,\qquad f_t=e f_0.
\tag{3.5}
\]

Both children are squarefree labels. They overlap at \(e\), together with any inherited overlap between \(q_0\) and \(f_0\). The exact source forward identity, after normalization, is

\[
\boxed{
\mathscr Q_{q_0,f_0}(A,B;k)
=\sum_t
\frac{\omega_t(k,f_0)}
     {Nc\,Nd\,(Ne)^{3/2}}
\mathscr P_{q_t,1}(A_t,B_t;k,f_t),
}
\tag{3.6}
\]

where

\[
\omega_t(k,f_0)
=\lambda(C)^3a_\xi(e)
\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f_0)^4,
\qquad |\omega_t(k,f_0)|\le1.
\tag{3.7}
\]

For clarity, the normalized coefficient follows from

\[
\sqrt{NC}\sqrt{\frac{A_tB_t}{AB}}
=\frac1{Nc\,Nd\,(Ne)^{3/2}}.
\tag{3.8}
\]

The source's exact CRT identity puts the extra \(e\) factor into the auxiliary \(ef_0\); its character zeros impose the displayed exclusion at \(C f_0\). Formula (3.6) remains valid on every row sharing primes with its labels. Every sum is finite on physical support.

Set

\[
F=Nf_0,\qquad Q=N\bigl(q_0/(q_0,f_0)\bigr).
\tag{3.9}
\]

Since the correction primes avoid \(q_0f_0\),

\[
Nf_t=F\,Ne,\qquad
N\bigl(q_t/(q_t,f_t)\bigr)=Q\,Nc\,Nd.
\tag{3.10}
\]

This exact overlap reduction is needed in the subsequent exponents.

## 4. Scale the inverse cutoff with the corrected second axis

We now specialize the parent to \(A=B=D\), retaining arbitrary polynomially bounded \(q_0,f_0\). For each child use

\[
\boxed{
R_t=R(B_t/D)^{1/3}.
}
\tag{4.1}
\]

This is a positive number, allowed to be less than one. Write

\[
u=Nc,\qquad v=Nd,\qquad w=Ne.
\]

Then

\[
A_t=D u^{-1}v^{-2}w^{-2},\quad
B_t=D u^{-2}v^{-1}w^{-2},\quad
R_t=R u^{-2/3}v^{-1/3}w^{-2/3},
\tag{4.2}
\]

and the normalizing weight in (3.6) is \(u^{-1}v^{-1}w^{-3/2}\).

Each child is bounded by Theorem 2.1 at \(A_t,B_t,R_t\), with the exact label norms (3.10). For a nonempty child, \(A_t\) and \(B_t\) have the fixed positive lower bounds stated in Section 1. All its remaining parameters are polynomially bounded in the common reference \(D\). Inside that theorem its own sixth-power-row cutoffs are

\[
\min(K B_t^{1/3},R_t\,Nz),
\tag{4.3}
\]

where \(z\) is its fixed sixth-power row factor. This is the same capped construction as (2.5), with \(R_t<1\) covered by the exact empty-short-part case. No common positive lower cutoff is imposed on all children.

### The six norm exponents

Let the parent energy monomials be

\[
\begin{aligned}
m_1&=HD,\\
m_2&=FQH^2D^{\beta-1/2}R^\kappa,\\
m_3&=F^{2/3}Q^{1/3}H^{4/3}D^{2/3}R^2,\\
m_4&=H,\\
m_5&=D^2R^{-3},\\
m_6&=(HD^2)^{2/3}R^{-2}.
\end{aligned}
\tag{4.4}
\]

After taking the square root of the corresponding child energy term and multiplying by \(u^{-1}v^{-1}w^{-3/2}\), its bound is \(\sqrt{m_j}\) times the following powers:

| Parent term | Power of \(u\) | Power of \(v\) | Power of \(w\) |
|---|---:|---:|---:|
| \(m_1\) | \(-3/2\) | \(-2\) | \(-5/2\) |
| \(m_2\) | \(-1\) | \(-3/2\) | \(-2\) |
| \(m_3\) | \(-3/2\) | \(-13/6\) | \(-5/2\) |
| \(m_4\) | \(-1\) | \(-1\) | \(-3/2\) |
| \(m_5\) | \(-3/2\) | \(-2\) | \(-5/2\) |
| \(m_6\) | \(-4/3\) | \(-5/3\) | \(-13/6\) |

These are norm-level powers, not squared-energy powers.

For example, the child middle energy term is

\[
(Fw)(Quv)H^2
\left(Du^{-1}v^{-2}w^{-2}\right)
\left(Du^{-2}v^{-1}w^{-2}\right)^{\beta-3/2}
\left(Ru^{-2/3}v^{-1/3}w^{-2/3}\right)^\kappa.
\]

Since \(\kappa=9/2-3\beta\), this simplifies exactly to

\[
m_2\,v^{-1}w^{-1}.
\tag{4.5}
\]

Its \(u\)-power cancels before the normalizing weight. The third child term similarly simplifies to

\[
m_3\,u^{-1}v^{-7/3}w^{-2},
\tag{4.6}
\]

and its \(A_tB_t R_t^{-3}\) tail is

\[
m_5\,u^{-1}v^{-2}w^{-2}.
\tag{4.7}
\]

These computations explain why scaling the cutoff by the second-axis cube length is effective. A single cutoff independent of \(B_t\) would not give the table.

## 5. The full correction sum is bounded

### Theorem 5.1. Full A2 positive norm

For every \(R>0\), with the stated source-qualified hypotheses,

\[
\boxed{
\begin{aligned}
\sum_{k\asymp H}|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^\epsilon\bigg[
&HD+FQH^2D^{\beta-1/2}R^{9/2-3\beta}\\
&+F^{2/3}Q^{1/3}H^{4/3}D^{2/3}R^2\\
&+H+D^2R^{-3}+(HD^2)^{2/3}R^{-2}
\bigg].
\end{aligned}
}
\tag{5.1}
\]

It includes the entire A2 arithmetic polynomial of (3.3), every correction label, every nonzero element row, and every overlap of the original labels.

**Proof.** Apply Minkowski to the exact finite projection (3.6). Each \(\omega_t(k,f_0)\) is a contraction in the positive row norm for fixed \(t\). Theorem 2.1 and
\(\sqrt{x_1+\cdots+x_6}\le\sqrt{x_1}+\cdots+\sqrt{x_6}\)
reduce the correction sum to the six rows of the table.

For each nonempty correction term, \(u,v,w\ll D\) after fixed support constants; this weaker bound is sufficient. Drop the pairwise-coprimality and moving-exclusion restrictions only in these positive upper sums. An ideal sum with power strictly below \(-1\) converges. A power equal to \(-1\) costs \(O(\log(2D))\).

The table therefore gives bounded sums except for the single harmonic \(u\) sum in \(m_2\), and the two harmonic \(u,v\) sums in \(m_4\). Thus every coefficient sum is \(O((\log(2D))^2)\). Squaring the final norm bound, and choosing smaller preliminary epsilon losses, absorbs these factors into \(D^\epsilon\). This proves (5.1). \(\square\)

The proof does not replace the corrected scales by the parent scales. It uses the actual child labels and the exact cutoff (4.1); the harmonic conclusions follow from their combined exponents.

## 6. Optimized consequences

The right side of (5.1) is exactly the same six-term envelope optimized in the companion stratified inverse theorem. Consequently, if

\[
H^2FQ\le D^{(5-2\beta)/2},
\tag{6.1}
\]

we may choose

\[
R=\min\left\{
D^{4/15}H^{-4/15}F^{-2/15}Q^{-1/15},
\ D^{1/3}(H^2FQ)^{-2/(3(5-2\beta))}
\right\}.
\tag{6.2}
\]

Both parent cutoffs lie in \([1,D^{1/3}]\) under (6.1); their A2 children are still allowed to be below one. The same exact optimization gives

\[
\boxed{
\sum_{k\asymp H}|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^\epsilon
\max\left\{
D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
\ DH^{4/(5-2\beta)}(FQ)^{2/(5-2\beta)}
\right\}.
}
\tag{6.3}
\]

The bound is \(O(D^{2+\epsilon})\) throughout (6.1).

For the source-conditional angular exponent \(\beta=11/12\),

\[
\boxed{
\sum_{k\asymp H}|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^\epsilon
\max\left\{
D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
\ DH^{24/19}(FQ)^{12/19}
\right\},
\quad H^2FQ\le D^{19/12}.
}
\tag{6.4}
\]

In particular, with \(q_0=f_0=1\),

\[
\boxed{
\sum_{k\asymp H}|\mathscr Q_{1,1}(D,D;k)|^2
\ll_\epsilon
\begin{cases}
D^{6/5+\epsilon}H^{4/5},&1\le H\le D^{19/44},\\
D^{1+\epsilon}H^{24/19},&D^{19/44}\le H\le D^{19/24}.
\end{cases}
}
\tag{6.5}
\]

Thus the **full normalized A2 polynomial**, not merely its squarefree face or a subset of correction labels, satisfies

\[
\boxed{
\sum_{k\asymp D^{1/2}}|\mathscr Q_{1,1}(D,D;k)|^2
\ll_\epsilon D^{31/19+\epsilon}.
}
\tag{6.6}
\]

The normalization is \(\mathscr Q(D,D)=Q_{\rm unnormalized}(D,D)/D\). The number \(19/24\) in (6.5) is an arithmetic row-height exponent. It is not the target zero-free boundary \(17/24\).

With moving labels at \(H=D^{1/2}\), the second term in (6.4) dominates and gives

\[
\sum_{k\asymp D^{1/2}}
|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^{31/19+\epsilon}(FQ)^{12/19},
\qquad FQ\le D^{7/12}.
\tag{6.7}
\]

Without the angular reciprocal input, \(\beta=1\) instead gives

\[
\sum_{k\asymp H}|\mathscr Q_{q_0,f_0}(D,D;k)|^2
\ll_\epsilon D^\epsilon
\max\left\{
D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
\ DH^{4/3}(FQ)^{2/3}
\right\},
\quad H^2FQ\le D^{3/2}.
\tag{6.8}
\]

For unit labels, its exponent at \(H=D^{1/2}\) is \(5/3\). It retains the classical theta and large-sieve foundations, with counting in the scalar step.

## 7. What remains after the unsigned A2 closure

The moving inner exclusion, single auxiliary twist, outer inverse mask, all repeated-prime rows, and full A2 correction sum have now been handled for the specified positive norm. In particular, merely summing A2 correction labels is no longer an unproved step in this estimate.

The actual first-Poisson comparison still has two independently corrected columns, an original row-dependent bilinear kernel, a strict product-column off-diagonal restriction, and a signed auxiliary sum. The positive norm here neither subtracts its diagonal nor controls cancellation in that signed expression. Nor does the gained range cover the adverse initial dual height near \(D^{3-\vartheta}\).

The original Möbius fourth moment, the \(17/24\) extraction, a new zeta zero-free boundary and a cofinal moment hierarchy therefore remain open. This theorem supplies a complete unsigned A2 estimate for the explicit physical family and states the remaining signed and scale interfaces separately.
