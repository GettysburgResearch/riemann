# Principal replicas: the exact average, its invertibility, and the converse scope

**Status:** new exact average and operator estimates, and a conditional converse audit for the companion principal-capture theorem. No estimate for the arithmetic target is proved. Ordinary RH is not assumed in Sections 1–4; Section 5 states explicitly where it is assumed.

**Scope:** the restored ordinary integer Möbius detector, its literal Eisenstein-ideal sixth-power replicas, a fixed finite excluded-prime set, and polynomially growing base norms. Split prime ideals of equal rational norm remain separate ideal indices. The result narrows the target to ordinary zeta; it does not prove GRH for the full moving Hecke family.

**Exact inherited source:** PR #917, commit `6b4723042b3d250024eef45cb1924f88f28e902c`, `standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/SCALE_AVERAGED_CRITERION.md`, Sections 1–3. Its full-ball moving-mask operator is already proved. The changes proved here are the rough-annulus density, the restored zeta multiplier, and the exact fixed-endpoint versus cofinal converse. The restoration and sparse-capture interfaces are those of this packet's `EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md`; its final hash will be recorded in the packet source lock. The elementary lattice count is the same fixed-field input as in the pinned source.

## 1. The literal principal family

Let \(K=\mathbb Q(\sqrt{-3})\), and let \(Q\) be a fixed finite set of prime ideals containing all primes excluded in the restored source. Let \(W\in C_c^\infty((0,\infty))\) be fixed. Define

\[
F(D)=\sum_{n\ge1}\mu_{\mathbb Z}(n)W(n/D).
\tag{1.1}
\]

For an integral ideal \(w\) prime to \(Q\), the exact restored replica is

\[
B_w(D):=B_{w^6}(D)
=T_wF(D)
:=\sum_{\operatorname{rad}d\mid w} F(D/Nd).
\tag{1.2}
\]

Here \(d\) is an integral ideal of \(K\), with unrestricted exponents at the primes of \(w\). The shorthand \(B_w\) in this note denotes the row \(w^6\), not the row \(w\). Equation (1.2) is imported only after the companion's exact periodic filter and finite prime-ideal restoration. It is not true for an arbitrary unfiltered Hecke row. All sums in (1.2) are finite at a fixed \(D\), since \(F\) vanishes below a fixed positive scale.

The two ideals over a split rational prime can both divide \(w\). Their two geometric series then remain two factors in (1.2); no duplicate norm is erased.

Put

\[
\mathcal V_Q(Y)=\{w:(w,Q)=1,\ Y/2<Nw\le Y\},\qquad
J_Q^\circ(Y)=|\mathcal V_Q(Y)|,
\]

and define the natural positive average

\[
P_YF(D)=\frac1{J_Q^\circ(Y)}
\sum_{w\in\mathcal V_Q(Y)}B_w(D).
\tag{1.3}
\]

Statements involving this average are for \(Y\) above a fixed threshold where its denominator is positive.

## 2. The exact rough-annulus density

Let \(J_Q(x)=\#\{w:(w,Q)=1,Nw\le x\}\), extended by zero for \(x<1\). Finite inclusion–exclusion in the elementary Eisenstein ideal count gives

\[
J_Q(x)=\kappa_Qx+O_Q(x^{1/2}+1),\qquad \kappa_Q>0,
\tag{2.1}
\]

and consequently \(J_Q^\circ(Y)\asymp_QY\).

### Theorem 2.1. Exact coefficients and uniform error

Write \(R_d=N\operatorname{rad}d\). Then

\[
P_YF(D)=\sum_{(d,Q)=1}w_Y^\circ(d)F(D/Nd),
\]

\[
w_Y^\circ(d)=
\frac{J_Q(Y/R_d)-J_Q(Y/(2R_d))}
     {J_Q(Y)-J_Q(Y/2)}.
\tag{2.2}
\]

For all sufficiently large \(Y\), uniformly in every ideal \(d\) prime to \(Q\),

\[
0\le w_Y^\circ(d)\ll_Q R_d^{-1},\qquad
\left|w_Y^\circ(d)-R_d^{-1}\right|
\ll_Q\min\{R_d^{-1},Y^{-1/2}R_d^{-1/2}\}.
\tag{2.3}
\]

In particular, for \(0<\delta<1/2\),

\[
\left|w_Y^\circ(d)-R_d^{-1}\right|
\ll_{Q,\delta}Y^{-\delta}R_d^{-1+\delta}.
\tag{2.4}
\]

**Proof.** A base counted by (1.3) contributes the dilation \(d\) precisely when \(\operatorname{rad}d\mid w\). Writing \(w=\operatorname{rad}d\,v\) proves (2.2); no coprimality of \(d\) and \(v\) is imposed. If \(R_d\le Y\), apply (2.1) to the numerator and denominator. The numerator is \(\kappa_QY/(2R_d)+O_Q((Y/R_d)^{1/2}+1)\), and the denominator is \(\kappa_QY/2+O_Q(Y^{1/2}+1)\). Their ratio has error \(O_Q(Y^{-1/2}R_d^{-1/2})\); the \(Y^{-1}\) term is smaller for \(R_d\le Y\). Ideal counting also bounds the numerator by \(O_Q(Y/R_d)\), proving the first bound. If \(R_d>Y\), the numerator vanishes, and the difference is \(R_d^{-1}\), which is at most \(Y^{-1/2}R_d^{-1/2}\). Combining the two estimates and geometrically interpolating them proves (2.3)–(2.4). \(\square\)

## 3. A quantitative limiting operator which is invertible throughout \(\Re s>0\)

Define

\[
(\mathcal M_QF)(D)=\sum_{(d,Q)=1}R_d^{-1}F(D/Nd).
\tag{3.1}
\]

For \(1\le p<\infty\), \(\sigma>0\), use the causal weighted scale norm

\[
\|F\|_{p,\sigma;(0,T)}^p
=\int_0^T|F(D)|^pD^{-p\sigma}\,\frac{dD}{D}.
\tag{3.2}
\]

The same coefficient argument applies to the weighted supremum norm \(\sup_{0<D\le T}D^{-\sigma}|F(D)|\). A dilation by \(Nd\) has norm at most \((Nd)^{-\sigma}\).

### Theorem 3.1. Uniform boundedness, inverse, and finite-\(Y\) approximation

The operator \(\mathcal M_Q\) and its causal inverse are bounded in each norm (3.2), uniformly in \(T\). For every \(0<\delta<\min(\sigma,1/2)\),

\[
\|P_Y-\mathcal M_Q\|_{p,\sigma;(0,T)}
\ll_{Q,\sigma,\delta}Y^{-\delta}.
\tag{3.3}
\]

All these statements also hold in the weighted supremum norm. If \(Y=Y(D)\) is measurable and \(Y(D)\ge cD^\rho\), \(c,\rho>0\), choose \(D_0\) so large that \(Y(D)\) exceeds the threshold in Theorem 2.1 for every \(D\ge D_0\). For this restricted assertion define the moving operator's output to be zero below \(D_0\), where its finite-annulus denominator need not be available. Then, on functions extended by zero below \(D_0\),

\[
\|P_{Y(\cdot)}-\mathcal M_Q\|
\ll_{Q,\sigma,\delta,c}D_0^{-\rho\delta},
\tag{3.4}
\]

uniformly on finite causal horizons. Every dilation has \(Nd\ge1\), so both operators preserve this zero-below-\(D_0\) subspace. In particular the moving operator is invertible on a sufficiently late causal tail, with bounds independent of the upper endpoint.

**Proof.** The positive coefficient majorant supplied by (2.4) has finite weighted sum

\[
\sum_{(d,Q)=1}R_d^{-1+\delta}(Nd)^{-\sigma}
=\prod_{\mathfrak p\notin Q}
\left(1+\frac{(N\mathfrak p)^{-1+\delta-\sigma}}
                  {1-(N\mathfrak p)^{-\sigma}}\right)<\infty.
\tag{3.5}
\]

This proves (3.3), and the pointwise majorant with \(Y(D)^{-\delta}\le c^{-\delta}D_0^{-\rho\delta}\) proves (3.4). At \(q=N\mathfrak p\), set \(S_qF(D)=F(D/q)\). The local factor of \(\mathcal M_Q\) and its inverse are exactly

\[
\mathcal M_{Q,\mathfrak p}
=\frac{1-(1-q^{-1})S_q}{1-S_q},\qquad
\mathcal M_{Q,\mathfrak p}^{-1}
=1-q^{-1}\sum_{j\ge1}(1-q^{-1})^{j-1}S_q^j.
\tag{3.6}
\]

Both products converge in the coefficient norm \(\sum_d|c_d|(Nd)^{-\sigma}\), since each nonconstant local norm is \(O_\sigma(q^{-1-\sigma})\). This proves boundedness and the causal inverse, including all duplicate prime-ideal norms. Choose \(D_0\) so that the norm of \(\mathcal M_Q^{-1}(P_{Y(\cdot)}-\mathcal M_Q)\) is less than one half. The Neumann series then proves the last assertion on the subspace zero below \(D_0\). As in the pinned source, a low-scale piece with finite weighted norm is handled separately by the positive bounded dilation majorant; integrability of an unknown tail is not assumed. \(\square\)

### Corollary 3.2. The average preserves the target's Mellin singularities

The Dirichlet multiplier of (3.1) is

\[
\boxed{
m_Q(s)=\prod_{\mathfrak p\notin Q}
\frac{1-(1-(N\mathfrak p)^{-1})(N\mathfrak p)^{-s}}
     {1-(N\mathfrak p)^{-s}}.
}
\tag{3.7}
\]

It and its reciprocal are holomorphic and nonzero for \(\Re s>0\). For the integer detector (1.1),

\[
\mathcal M_{\rm Mellin}(\mathcal M_QF)(s)
=m_Q(s)\frac{\widehat W(s)}{\zeta(s)}
\qquad(\Re s>1),
\tag{3.8}
\]

with the corresponding meromorphic continuation wherever the right side is defined.

**Proof.** Absolute and locally uniform convergence follows from the \(O_\sigma(q^{-1-\sigma})\) local errors, uniformly in the imaginary part on \(\Re s\ge\sigma>0\). The denominator of each factor is nonzero there, and the numerator cannot vanish since \(|(1-q^{-1})q^{-s}|<1\). The inverse product converges in the same region. Absolute Mellin summation first in \(\Re s>1\) proves (3.8). \(\square\)

Thus the natural average is an explicitly invertible smoothing of the ordinary zeta detector. It is not a new family of independent pole-free functions. Any zero of \(\zeta\) not canceled by the fixed window remains a pole after multiplying by \(m_Q\). The variable finite-\(Y\) average is not asserted to have exactly the scalar multiplier (3.7); its correct statement is the operator approximation and causal inverse above.

## 4. Fixed-fraction capture is already enough at every real scale

This elementary version isolates the arithmetic content without a sampling adapter. Fix \(\alpha>0\), \(\gamma\in(0,1)\), \(h>0\), and \(Y(D)=D^{h/6}\). For a base \(w\), put

\[
K_\alpha(w)=\sum_{\substack{d\ne1\\\operatorname{rad}d\mid w}}(Nd)^{-\alpha}.
\tag{4.1}
\]

The exact limiting mean over the rough annulus is

\[
\lim_{Y\to\infty}\frac1{J_Q^\circ(Y)}
\sum_{w\in\mathcal V_Q(Y)}K_\alpha(w)
=\prod_{\mathfrak p\notin Q}
\left(1+\frac1{N\mathfrak p((N\mathfrak p)^\alpha-1)}\right)-1.
\tag{4.2}
\]

Equation (2.3) and the convergent positive majorant justify dominated convergence. By enlarging the fixed \(Q\), the right side is arbitrarily small. Fix \(Q\) so that the eventual mean is at most \(\gamma/8\).

### Proposition 4.1. Quantile-to-target induction

Suppose that for every sufficiently large real \(D\), at least a proportion \(\gamma\) of \(w\in\mathcal V_Q(Y(D))\) satisfy

\[
|B_w(D)|\le C_0D^\alpha.
\tag{4.3}
\]

Then \(F(D)\ll D^\alpha\).

**Proof.** Markov's inequality shows that at most \(\gamma/4\) of the bases have \(K_\alpha(w)>1/2\). Hence one can choose a base satisfying both (4.3) and \(K_\alpha(w)\le1/2\). From (1.2),

\[
F(D)=B_w(D)-\sum_{\substack{d\ne1\\\operatorname{rad}d\mid w}}F(D/Nd).
\tag{4.4}
\]

Every nonidentity ideal has norm at least two. If \(|F(x)|\le Cx^\alpha\) is known for \(x\le D/2\), then (4.4) is at most \(C_0D^\alpha+(C/2)D^\alpha\). Choose \(C\ge2C_0\) and to cover the bounded initial range, and induct on dyadic intervals. The selected base may vary with \(D\); no lower-scale moment or capture assertion with a moving excluded prime is used. \(\square\)

The companion sparse-capture theorem replaces “every real scale” by its exact fixed polylogarithmic grid, using the separately proved interpolation and the universal fixed window. That is a useful reduction in the observations required. It supplies no arithmetic proof of (4.3).

## 5. Ordinary RH supplies all polynomially bounded principal replicas

### Theorem 5.1. Converse with the correct endpoint margin

Assume ordinary RH. Fix any \(\alpha>1/2\), fixed \(h>0\), fixed smooth compact window \(W\), and any fixed finite \(Q\). Then

\[
\boxed{
\sup_{Nw\le D^{h/6},\ (w,Q)=1}|B_w(D)|\ll_{W,\alpha,h,Q}D^\alpha
\qquad(D\ge2).
}
\tag{5.1}
\]

This holds at every sufficiently large real \(D\), hence on any predetermined sampling grid. It implies every fixed-fraction capture assertion with \(\gamma\in(0,1)\), and every fixed moment bound for the positive principal-replica average with this amplitude exponent.

**Proof.** Choose \(1/2<\sigma<\alpha\). We first justify the fixed-zeta bound \(F(X)\ll_{W,\sigma}X^\sigma\), without a Hecke-family assumption. The classical summation identity
\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx
\qquad(\Re s>0)
\tag{5.1a}
\]
gives polynomial vertical growth after removing the pole: \(Z(s)=(s-1)\zeta(s)/(s+1)\) satisfies \(Z(s)\ll_a1+|s|\) on each fixed bounded real strip to the right of \(a>0\). Under RH, \(Z\) is holomorphic and nonzero on \(\Re s>1/2\), including at one. For each large height \(t\), take the analytic logarithm on a disk centered at \(2+it\), with fixed outer left edge between \(1/2\) and \(\sigma\), and an inner disk reaching \(\sigma+it\). Its center value is bounded by the absolutely convergent Euler product and the pole-removal factor. The bound on \(\Re\log Z\) is \(O_\sigma(\log(2+|t|))\). Borel–Carathéodory therefore gives \(|\log Z(\sigma+it)|=O_\sigma(\log(2+|t|))\), and hence a polynomial bound for \(1/\zeta(\sigma+it)\). Bounded heights are covered by continuity, with the reciprocal zero at one retained.

This is the fixed-zeta specialization of the analytic-log argument in PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1, FOURTH_MOMENT_ATTACK.md, Lemma 8.1; its stronger subpower conclusion is unnecessary here. Shifting the Mellin integral \(\widehat W(s)/\zeta(s)\) to \(\Re s=\sigma\) is justified by this polynomial bound and the fixed smooth test's rapid vertical decay. It gives \(F(X)\ll_{W,\sigma}X^\sigma\). The lower support cutoff and a bounded initial interval make this power bound valid for every \(X>0\). Only ordinary RH was used.

For every fixed \(\eta>0\), elementary finite-prime splitting gives

\[
\sum_{\operatorname{rad}d\mid w}(Nd)^{-\sigma}
=\prod_{\mathfrak p\mid w}(1-(N\mathfrak p)^{-\sigma})^{-1}
\ll_{\sigma,\eta}(Nw)^\eta.
\tag{5.2}
\]

Indeed each sufficiently large local factor is at most \((N\mathfrak p)^\eta\); the finitely many smaller prime ideals contribute a fixed constant. Apply (1.2), then (5.2), to obtain \(|B_w(D)|\ll D^\sigma(Nw)^\eta\le D^{\sigma+h\eta/6}\). Choose \(\eta<6(\alpha-\sigma)/h\). This proves (5.1). \(\square\)

### Corollary 5.2. Exact strength of the cofinal capture program

Use the companion's fixed universal window, whose Mellin transform is nonzero in \(\Re s>0\), and its exact forward sparse-capture theorem. Then the capture assertions for every fixed \(\alpha>1/2\) are equivalent to ordinary RH. The parameters \(h,\gamma,Q\), thresholds, grid constants and implied constants may be fixed separately for each \(\alpha\), as allowed by that theorem. The theorem is applied at one fixed \(\alpha\) before the scale tends to infinity; no uniformity as \(\alpha\downarrow1/2\) is supplied or needed for this qualitative equivalence.

**Proof.** RH implies even the all-replica statement (5.1), so it implies the required grid quantile. Conversely the companion theorem gives zeta zero-freeness in \(\Re s>\alpha\) for every \(\alpha>1/2\). The zeta functional equation then puts every nontrivial zero on the critical line. \(\square\)

At a single fixed \(\alpha\), capture implies zero-freeness in the strict half-plane \(\Re s>\alpha\). This note does **not** claim the converse at the same endpoint. A zero-free assertion only in \(\Re s>\alpha\) generally permits a bound with exponent \(\alpha+\varepsilon\); it does not provide \(CD^\alpha\) without additional boundary information. The margin in Theorem 5.1 is essential.

## 6. Consequence for the research direction

This is a narrower arithmetic target than the old all-row cofinal moment hierarchy. The old hierarchy detects every fixed sextic row twist and is equivalent to GRH for that entire family. The restored principal-replica criterion asks only about ordinary integer Möbius cancellation, and its cofinal form is equivalent to ordinary RH.

The positive average (3.8) and the quantile induction show that averaging copies does not create an independent cancellation mechanism. A successful new argument must prove that the actual restored replicas are small on the stated positive fraction of the prescribed nodes, or directly control their appropriately weighted mean. No finite numerical sample, change of replica weights, or passage to the limiting Euler multiplier proves that arithmetic assertion.
