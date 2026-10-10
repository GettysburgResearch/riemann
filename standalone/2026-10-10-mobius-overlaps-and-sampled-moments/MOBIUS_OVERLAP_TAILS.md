# Signed residuals and two oscillating incidence axes

Status: proposed component theorems for the actual inverse Möbius/sextic polynomial. The fourth-moment common-factor cutoff and the cubic-axis triangle sector below are deductions from explicitly stated pointwise cancellation and classical character large sieves. At pointwise exponent one the hypotheses are elementary, but the new numerical improvements use exponent 7/8 as a separate, source-qualified premise. No full generalized short-row moment theorem or new zero-free half-plane is asserted.

Scope: every fixed polynomial degree over the Eisenstein field, all nonzero element rows, literal nonunit zeros, fixed finite-order character data, and fixed smooth original column tests. The common-factor theorem permits a sharp arithmetic gcd threshold. The Hermitian theorem concerns complete smooth incidence blocks. These are different objects, and neither is replaced by a sum of absolute individual tuple contributions.

What is new: a forward local correction allows Möbius cancellation in every residual column while leaving one common factor oscillatory; a separate mixed-sign correction allows positive even-incidence cubic factors, or whole groups of them, to serve as either of the two row-averaged axes. Grouping the three cubic pair variables on each side reaches a new zero-excess double-triangle range with no triple or higher overlap.

What was actually done: exact formal local-factor calculations, weighted absolute-convergence proofs, finite-test Mellin separation, and exact rational cutoff calculations. No numerical experiment with L-functions or sieve constants was used. The all-row character sieves are inherited from pinned sources. The quadratic refinement used in Section 5.2 is separately authored and explicitly identified.

Smallest remaining gap: the long fully singleton sextic incidence core, and its signed averaged-conductor counterpart. The present arguments do not estimate that core beyond the existing norm bounds.

## 1. Fixed data and the analytic hypotheses

Let \(K=\mathbb Q(\sqrt{-3})\). Use the repository's multiplicative primary ideal generators. Let \(S\) contain the primes over 6 and the ramification of the fixed finite-order datum \(\nu\). For a squarefree ideal \(n\) prime to \(S\), let
\[
\chi_n(u)=(u/n)_6,\qquad
\eta_u(n)=\nu(n)\chi_n(u).
\tag{1.1}
\]
Every symbol is zero on a nonunit. Extend \(\eta_u\) completely multiplicatively to all ideals prime to \(S\). The value at the unit ideal is one.

For fixed smooth tests \(W_i\) supported on positive compact intervals, write
\[
A_{i,u}(D_i)=
\sum_{(n,S)=1}\mu_K(n)\eta_u(n)W_i(Nn/D_i).
\tag{1.2}
\]
All row norms in Sections 2--5 mean \(\ell^2(0<Nu\le H)\), with all six element-unit sectors included. Put \(D_*=2+\max_iD_i\), and fix a polynomial range \(1\le H\le D_*^{A_0}\). The number of factors, \(A_0\), and every support interval are fixed. All auxiliary norms below have a fixed polynomial bound in \(D_*\). Constants may depend on these fixed data and on a displayed positive loss.

### The pointwise premise

For \(1/2<b\le1\), the hypothesis \(\mathrm{PW}_b^{\rm sm}\) is
\[
\left|\sum_{(n,qS)=1}\mu_K(n)\lambda(n)
       \chi_n(u)^{[e]}V(Nn/Y)\right|
\ll_\epsilon D_*^\epsilon Y^b\|V\|_{C^J},
\tag{1.3}
\]
uniformly for all relevant nonempty smaller scales \(Y\ll D_*\), every \(0<Nu\le O(H)\), polynomially bounded exclusions \(q\), and the fixed finite collection of odd powers \(e\) and finite-order data \(\lambda\) that is being used. Here \([e]\) denotes the literal power, using conjugates for negative \(e\), with zeros retained. The fixed seminorm order \(J\) and its constant are independent of the moving scale, row, and exclusion.

Sections 3--5.1 need (1.3) only for \(e=1,\lambda=\nu,q=1\); its uniform finite-seminorm form is still essential. Section 6 needs it for the odd incidence powers used there and for moving exclusions. At \(b=1\), elementary ideal counting supplies all these assertions. At \(b<1\), they are analytic hypotheses, not arbitrary-coefficient large-sieve consequences.

The optional native inverse second moment, denoted \(\mathrm{NM2}\), is
\[
\sum_{0<Nu\le O(H)}
\left|\sum_{(n,qS)=1}\mu(n)\lambda(n)
          \chi_n(u)^{[e]}V(Nn/Y)\right|^2
\ll_\epsilon D_*^\epsilon HY\|V\|_{C^{J_2}}^2
\tag{1.4}
\]
for the stated smaller scales and exclusions and \(e\equiv1,5\pmod6\). This is a separate optional input; no theorem below applies (1.4) to arbitrary coefficients or to cubic positive coefficients. It is used only in the optional comparison with the earlier selector. The two new numerical main examples do not need \(\mathrm{NM2}\).

These premise types, including finite test seminorms and their moving-mask adapters, are stated in PR #921, HERMITIAN_INCIDENCE.md, Section 1, at commit

    4e6d4aa57ae4cb04d76b2b31279ac367951b469a.

That note derives the optional exponent \(b<1\) only through the common finite-order zero-free premise and the uniform reciprocal argument imported from PR #913. A fixed-row bound with an uncontrolled conductor constant does not suffice here.

### Sharp inverse tests are a distinct premise

When an inverse quadratic axis has a sharp norm interval, we will explicitly use the reciprocal hypothesis \(\mathrm R_b\):
\[
L(s,\lambda)^{-1}\text{ is holomorphic and }\quad
|L(\sigma+it,\lambda)^{-1}|
\ll_{\delta,\epsilon}
[N\mathfrak f_\lambda(2+|t|)]^\epsilon,
\quad \sigma\ge b+\delta,
\tag{1.5}
\]
uniformly for the relevant finite-order characters, with finite Euler exclusions retained. At a principal pole the reciprocal has its analytic zero. Lemma 2.1 of the companion QUADRATIC_INVERSE_PRODUCTS.md proves that (1.5) gives sharp interval inverse sums with bound \(D_*^\epsilon Y^b\), by truncated Perron at half-integer norm cutoffs and partial summation. We do not infer this sharp-test assertion from (1.3) alone.

The numeric uses of \(b=7/8\) below always retain the corresponding premise. They do not independently establish the imported 7/8 zero-free claim.

## 2. The all-row oscillatory inputs

For squarefree columns, arbitrary row-independent coefficients \(z_n\), and \(Nn\ll L\), the pinned all-row inputs can be written as
\[
\sum_{0<Nu\le H}
\left|\sum_nz_n\chi_n(u)^{[m]}\right|^2
\ll_\epsilon(HL)^\epsilon K_r(H,L)\sum_n|z_n|^2,
\quad r=\frac6{\gcd(m,6)},
\tag{2.1}
\]
where
\[
K_r(H,L)=
\begin{cases}
H+H^{1/r}L+(HL)^{2/3},&r=3,6,\\
H+H^{1/2}L,&r=2,\\
HL,&r=1.
\end{cases}
\tag{2.2}
\]
The order-one case means the literal mask \(\mathbf1_{(n,u)=1}\) and is elementary counting. A fixed finite-order column twist and an arbitrary fixed column exclusion are part of \(z_n\), so the constants do not depend on that exclusion.

The order-six assertion is PR #913, REFINED_ALL_ROW_SIEVE.md, Theorem 3.4, at commit

    6498d6cc2eded03159c7332b25fd224ad07f89c1.

The order-three and order-two assertions, and their precise nonunit-zero conventions, are proved in PR #917, OSCILLATING_OVERLAPS.md, Sections 2--3, at commit

    6b4723042b3d250024eef45cb1924f88f28e902c.

The cubic proof writes \(u=\varepsilon v^3ab^2\), with \(a,b\) squarefree and coprime, freezes \(v\) and the smaller of \(a,b\), and retains the complete mask \(\mathbf1_{(n,v)=1}\). On a dyad, with
\[
P=V^3AB^2,\qquad F=VAB,\qquad M=\max(A,B),
\]
the squarefree cubic sieve gives
\[
F+\frac{FL}{M}+\frac{FL^{2/3}}{M^{1/3}}.
\]
The exact inequalities
\[
F\le P,\quad
(F/M)^3/P=A^2B/M^3\le1,\quad
(F/M^{1/3})^3/P^2=A/(MV^3B)\le1
\]
give \(H+H^{1/3}L+(HL)^{2/3}\). The quadratic proof uses \(u=\varepsilon v^2a\), with squarefree \(a\), and again retains \(\mathbf1_{(n,v)=1}\). Its two terms sum as \(H\sum_v(Nv)^{-2}\) and \(L\,\#\{Nv\ll\sqrt H\}\). Finite bad-prime parts and all unit sectors are retained as fixed partitions. Thus neither input silently replaces an imprimitive zero by one.

For
\[
C_u^{[m]}(L;V)=
\sum_{(c,S)=1}\mu(c)^m\eta_u(c)^m V(Nc/L),
\tag{2.3}
\]
any bounded test on a fixed positive annulus gives
\[
\|C^{[m]}(L;V)\|_2^2
\ll_\epsilon D_*^\epsilon K_r(H,L)L\,\|V\|_\infty^2.
\tag{2.4}
\]
For even \(m\), the coefficient is \(\mu^2\), not \(\mu\). This positive coefficient still has a nontrivial cubic phase when \(m\equiv2,4\pmod6\).

## 3. An exact correction for one designated incidence ideal

Expand \(\prod_{i=1}^kA_{i,u}(D_i)\). Fix \(I\subseteq[k]\), \(m=|I|\ge2\). Let \(q_I\) be the product of primes occurring in precisely the original positions in \(I\), and let \(F_{I,\ge C}\) be the exact polynomial portion with \(Nq_I\ge C\). It is a signed polynomial in the row \(u\), before taking any row norm.

Write \(c=q_I\), and set \(n_i=ca_i\) for \(i\in I\), \(n_j=a_j\) for \(j\notin I\). The \(a_i\) are squarefree. A prime of \(c\) occurs in none of the residual \(a_i\). At a prime not in \(c\), the residual incidence set can be every subset of \([k]\) except exactly \(I\). Other residual overlaps are allowed. In particular, when \(I=[k]\) the residual condition is a common gcd of one, not pairwise coprimality.

Put
\[
\varepsilon_m=(-1)^m,\qquad
R(\mathbf z)=\prod_{i=1}^k(1-z_i),\qquad
Z_I=\prod_{i\in I}z_i.
\]
Using \(z_0\) for the \(c\) coordinate, the required local series is
\[
\mathcal F_{I,p}(\mathbf z)
=R(\mathbf z)-\varepsilon_m Z_I+\varepsilon_m z_0.
\tag{3.1}
\]
The independent \(c\)-axis and residual inverse factors have local series
\[
(1+\varepsilon_m z_0)R(\mathbf z).
\]
Define the forward correction
\[
E_{I,p}(\mathbf z)
=\frac{R-\varepsilon_m Z_I+\varepsilon_m z_0}
       {(1+\varepsilon_m z_0)R}.
\tag{3.2}
\]
All factors at \(p\in S\) are one. This is an identity of formal power series with constant term one. It does not require dividing by a character value. Its row-independent coefficients will be denoted \(e_I(d_0,\ldots,d_k)\).

The nonconstant part has the useful form
\[
E_{I,p}-1
=\frac{\varepsilon_m\{z_0(1-R)-Z_I\}}
       {(1+\varepsilon_m z_0)R}.
\tag{3.3}
\]
Thus every nonconstant numerator term either uses \(c\) and a residual axis, or uses all \(m\) residual axes of \(I\). There are no unsupported one-axis error terms.

### Lemma 3.1: the weighted correction is absolutely summable

If \(\alpha>0\), \(b>0\), \(\alpha+b>1\), and \(mb>1\), then
\[
\sum_{\mathbf d}|e_I(\mathbf d)|
(Nd_0)^{-\alpha}\prod_{i=1}^k(Nd_i)^{-b}<\infty.
\tag{3.4}
\]
Its constant depends only on the fixed data and exponents.

**Proof.** At \(q=Np\), put \(t_0=q^{-\alpha}\), \(t_i=q^{-b}\). Expanding the denominator of (3.3) geometrically in absolute value bounds its nonconstant coefficient mass by
\[
\frac{t_0\{\prod_i(1+t_i)-1\}+\prod_{i\in I}t_i}
     {(1-t_0)\prod_i(1-t_i)}
\ll_{\alpha,b,k}q^{-(\alpha+b)}+q^{-mb}.
\tag{3.5}
\]
Both prime-ideal sums converge under the stated strict inequalities. Every fixed small-prime denominator is nonzero because all \(t_i<1\). Their finite product is a fixed constant. No additional small primes are removed, and no denominator \(1-k/\sqrt{Np}\) is introduced. Multiplication of the local absolute majorants proves (3.4). \(\square\)

Insert the row characters by setting
\[
z_0=\eta_u(p)^m x_0,\qquad z_i=\eta_u(p)x_i.
\]
The exterior character multiplier in the global convolution is
\[
\eta_u(d_0)^m\prod_{i=1}^k\eta_u(d_i),
\tag{3.6}
\]
of modulus at most one. If \(u\) is a nonunit at \(p\), every nonconstant local monomial involving \(p\) vanishes on both sides. This includes the case \(6\mid m\): the \(c\)-axis has the correct principal mask, not an everywhere-one value.

Consequently the sum with the exact eligibility in (3.1) and separated tests is identically
\[
\sum_{\mathbf d}e_I(\mathbf d)
\eta_u(d_0)^m\prod_i\eta_u(d_i)\,
C_u^{[m]}(L/Nd_0;V_0)
\prod_i A_u(X_i/Nd_i;V_i).
\tag{3.7}
\]
Here and below \(A_u(Y;V)\) denotes the sum in (1.2) with test \(V\). Equation (3.7) is a finite identity on compact support: every contributing \(Nd_0\ll L\) and \(Nd_i\ll X_i\). Intermediate correction indices may have prime powers; this is ordinary formal convolution, and cancellation restores the prescribed squarefree original coordinates.

### Ordinary subset gcd

For the ordinary gcd of the factors in \(I\), outside residual factors may share primes with \(c\). The required local series is
\[
\left\{\prod_{i\in I}(1-z_i)-\varepsilon_mZ_I
              +\varepsilon_m z_0\right\}
\prod_{j\notin I}(1-z_j).
\tag{3.8}
\]
Thus the correction (3.2) uses only the \(m\) residual coordinates inside \(I\); the outside inverse factors remain independent. The same weighted bound and subsequent theorem apply. For \(I=[k]\), the designated incidence and the full ordinary gcd coincide.

## 4. A sharp designated-factor tail with signed residuals

Put \(\mathcal P=\prod_{i=1}^kD_i\). Assume \(\mathrm{PW}_b^{\rm sm}\), with \(1/2<b\le1\), for the residual factors.

### Theorem 4.1

For \(r=6/\gcd(m,6)\in\{3,6\}\),
\[
\boxed{
\|F_{I,\ge C}\|_2^2
\ll_\epsilon D_*^\epsilon\mathcal P^{2b}
\left[
 HC^{1-2mb}
 +H^{1/r}C^{2-2mb}
 +H^{2/3}C^{5/3-2mb}
\right].
}
\tag{4.1}
\]
For \(r=2\),
\[
\boxed{
\|F_{I,\ge C}\|_2^2
\ll_\epsilon D_*^\epsilon\mathcal P^{2b}
\left[HC^{1-2mb}+H^{1/2}C^{2-2mb}\right].
}
\tag{4.2}
\]
For \(r=1\),
\[
\boxed{
\|F_{I,\ge C}\|_2^2
\ll_\epsilon D_*^\epsilon H\mathcal P^{2b}C^{2-2mb}.
}
\tag{4.3}
\]
All three assertions allow the sharp threshold \(Nq_I\ge C\), and the ordinary subset-gcd variant from (3.8). The threshold is at least one. A proposed nonempty range must also meet \(C\ll\min_{i\in I}D_i\); beyond the actual support the polynomial is zero.

**Proof.** First restrict \(Nc\) to \(L\le Nc<2L\). Put
\[
X_i=D_i/L\quad(i\in I),\qquad X_i=D_i\quad(i\notin I).
\tag{4.4}
\]
For \(i\in I\), write \(t=Nc/L\), \(y_i=Na_i/X_i\), so the original weight is \(W_i(ty_i)\). Choose a fixed smooth cutoff \(\rho_i\) that is one on every possible \(y_i\) when \(1\le t<2\) and \(W_i(ty_i)\ne0\). Mellin inversion on the imaginary axis gives
\[
W_i(ty_i)=\frac1{2\pi}\int_{\mathbb R}
\widehat W_i(is_i)t^{-is_i}y_i^{-is_i}\rho_i(y_i)\,ds_i
\tag{4.5}
\]
on the dyad. The insertion of \(\rho_i\) is an equality on the original support. Outside factors can keep their original tests. The resulting \(c\)-test is
\[
V_0(t)=\mathbf1_{[1,2)}(t)t^{-i\sum_{i\in I}s_i}.
\tag{4.6}
\]
It is bounded by one; the classical sieve (2.4) accepts it. We have not Mellin-inverted the sharp indicator. Each residual test \(V_i(y)=\rho_i(y)y^{-is_i}\) has a fixed \(C^J\) norm bounded polynomially in \(1+|s_i|\). The transforms of the original smooth \(W_i\) decrease faster than every fixed power, so all resulting seminorm costs are integrable.

Apply the exact identity (3.7) before row Cauchy or absolute coefficient summation. On each independent product, bound all \(k\) residual inverse factors by (1.3), and use (2.4) on \(C^{[m]}\). Since
\[
\prod_iX_i^b=\mathcal P^bL^{-mb},
\]
the \(r=3,6\) dyadic row norm is
\[
\ll_\epsilon D_*^\epsilon\mathcal P^b
\left[
H^{1/2}L^{1/2-mb}
+H^{1/(2r)}L^{1-mb}
+H^{1/3}L^{5/6-mb}
\right].
\tag{4.7}
\]
To justify summing the correction, the three respective \(d_0\) weights are \(\alpha=1/2,1,5/6\); every residual weight is \(b\). Lemma 3.1 applies to each because \(b>1/2\) and \(mb>1\). The exterior factor (3.6) remains a contraction. Scales below the fixed support cutoff vanish; every remaining scale below one lies in a fixed compact positive interval, where the displayed power bounds differ from counting by fixed constants only.

For \(r=2\), omit the third term of (4.7) and use \(H^{1/4}\) in the second. For \(r=1\), counting gives just \(H^{1/2}\mathcal P^bL^{1-mb}\), with correction weight \(\alpha=1\).

Partition the sharp tail into \(L=2^jC\), \(j\ge0\). Every exponent of \(L\) in the row-norm estimates is strictly negative, because \(mb>1\). Minkowski and geometric summation therefore replace \(L\) by \(C\) in (4.7) and its companions. Squaring, with a fixed finite-term inequality, proves (4.1)--(4.3). All polynomial and finite-seminorm losses may start with a smaller epsilon and be reassigned to the displayed one. The mask and eligibility identities held before every estimate. \(\square\)

At \(b=1\) this recovers the designated-factor theorem in PR #917. For \(b<1\), it uses cancellation in all residual inverse factors, including those that retain ordinary collisions. Treating those residual factors as positive tuple counts would lose this gain.

### Explicit target criterion

The natural diagonal target is \(H\mathcal P\). Put \(Q=\mathcal P^{2b-1}\). For \(r=3,6\), (4.1) reaches this target if
\[
C\ge
\max\left\{
1,\,
Q^{1/(2mb-1)},\,
\left(\frac{Q}{H^{1-1/r}}\right)^{1/(2mb-2)},\,
\left(\frac{Q^3}{H}\right)^{1/(6mb-5)}
\right\}.
\tag{4.8}
\]
For \(r=2\), omit the last entry and set \(1-1/r=1/2\). For \(r=1\), the criterion is \(C\ge\max\{1,Q^{1/(2mb-2)}\}\). These are sufficient conditions for the specified exact polynomial tail, not for its complement.

## 5. Concrete common-factor improvements

### 5.1. The sharp fourth-moment polynomial tail

Let \(k=m=2\), \(D_1=D_2=D\), \(H=D^h\), and let \(T_{\ge C}\) be the exact portion of \(A_u(D)^2\) with \(N\gcd(n_1,n_2)\ge C\). Theorem 4.1 gives
\[
\boxed{
\|T_{\ge C}\|_2^2
\ll_\epsilon D^{4b+\epsilon}
\left[
 HC^{1-4b}
 +H^{1/3}C^{2-4b}
 +H^{2/3}C^{5/3-4b}
\right].
}
\tag{5.1}
\]
At \(b=7/8\), the three cutoff exponents against \(HD^2\) are
\[
\frac35,\qquad 1-\frac{4h}{9},\qquad \frac{9-2h}{11}.
\tag{5.2}
\]
For \(1<h\le11/10\), the third is the largest: its difference from \(3/5\) is nonnegative for \(h\le6/5\), and its difference from \(1-4h/9\) is \((26h-18)/99>0\). Hence
\[
\boxed{
\|T_{\ge D^{(9-2h)/11}}\|_2^2\ll_\epsilon HD^{2+\epsilon},
\qquad 1<h\le11/10,
}
\tag{5.3}
\]
under \(\mathrm{PW}_{7/8}^{\rm sm}\). In the source notation \(h=1+\theta\), the cutoff exponent is \((7-2\theta)/11\).

PR #917's unconditional pointwise-counting argument uses \((6-h)/7\). The exact decrease here is
\[
\frac{6-h}{7}-\frac{9-2h}{11}
=\frac{3(1+h)}{77}>0.
\tag{5.4}
\]
For example \(h=21/20\) gives \(69/110\), compared with \(99/140\). This improves a whole exact one-sided polynomial tail and so may be used in a valid decomposition \(A^2=T_{\ge C}+T_{<C}\). It does not estimate the remaining small-gcd polynomial, or its signed completed covariance.

### 5.2. The quadratic degree-three common factor

For \(k=m=3\), the common factor has coefficient
\[
\mu(c)^3\nu(c)^3\chi_c(u)^3
=\mu(c)\nu(c)^3\chi_c(u)^3.
\tag{5.5}
\]
It is an inverse quadratic sum. The classical version (4.2) gives
\[
\|G_{\ge C}^{(3)}\|_2^2
\ll_\epsilon D^{6b+\epsilon}
\left[HC^{1-6b}+H^{1/2}C^{2-6b}\right].
\tag{5.6}
\]
At \(b=7/8\), its cutoff against \(HD^3\) is
\[
\max\left\{\frac9{17},\frac{9-2h}{13}\right\}.
\tag{5.7}
\]
For \(h=21/20\), this is \(69/130\).

The companion QUADRATIC_INVERSE_PRODUCTS.md, titled Quadratic inverse products: averaging the square part before interpolation, proves the refined input
\[
\|C^{[3]}(L;V)\|_2^2
\ll_\epsilon D_*^\epsilon
\left[HL+H^{1/2}L^{1+b}\right]
\tag{Q-refined}
\]
for smooth tests from its uniform quadratic pointwise premise. It also proves it for interval-truncated bounded-variation tests under \(\mathrm R_b\). The author is the root agent; the version checked for this application has SHA256

    7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696.

Its precise statement is Corollary 4.2, equation (4.8); its sharp-test adapter is Lemma 2.1. The proof writes \(u=\varepsilon v^2a\), retains the exclusion by \(v\), and on \(Nv\asymp V\) takes the minimum of \((H/V)L+VL^2\) and \((H/V)L^{2b}\). The switch is \(V_*=\sqrt H L^{b-1}\). No square part of a row is discarded.

Under \(\mathrm R_b\), use (Q-refined) on the sharp dyadic test (4.6) in the proof of Theorem 4.1. Its variation is \(O(1+|\sum s_i|)\), so it fits the same Mellin integral. The new \(d_0\) weight is \(\alpha=(1+b)/2\), which satisfies \(\alpha+b>1\). This proves
\[
\boxed{
\|G_{\ge C}^{(3)}\|_2^2
\ll_\epsilon D^{6b+\epsilon}
\left[HC^{1-6b}+H^{1/2}C^{1-5b}\right].
}
\tag{5.8}
\]
Here \(\mathrm R_b\) must cover the residual sextic inverse family and the quadratic datum \(\nu^3\), with the finite exclusions used by the companion square-part proof. Alternatively one can state those smooth and interval pointwise premises separately.

At \(b=7/8\), comparison with \(HD^3\) gives
\[
\max\left\{\frac9{17},\frac{18-4h}{27}\right\}
=\frac9{17}
\qquad(1<h\le11/10).
\tag{5.9}
\]
The equality holds already for \(h\ge63/68\). Thus the sharp one-sided degree-three common-factor tail reaches the sixth-moment diagonal target at \(C\ge D^{9/17}\), under the explicit reciprocal premise. This cutoff is not a new zero-free boundary. A theorem only for smooth pointwise tests is insufficient to justify the sharp common-factor use of (Q-refined).

## 6. Two row-averaged incidence axes, including positive cubic axes

Now expand a Hermitian moment with \(2k\) original positions. Let \(\sigma_i=1\) in the \(k\) unbarred positions and \(\sigma_i=-1\) in the \(k\) barred positions. The original fixed smooth column tests may differ. For each nonempty incidence set \(I\), put
\[
m_I=|I|,\qquad e_I=\sum_{i\in I}\sigma_i.
\]
The incidence ideals \(q_I\) are squarefree and pairwise coprime. Their literal local coefficient is
\[
\mu(q_I)^{m_I}\,\nu(q_I)^{e_I}\,
\chi_{q_I}(u)^{[e_I]}.
\tag{6.1}
\]
When \(e_I=0\), the last factor means \(\mathbf1_{(q_I,u)=1}\). For nonzero negative \(e_I\) use conjugates. All incidences have positive multiplicity, so no principal power removes their nonunit zeros.

Consider a complete smooth incidence block \(Nq_I\asymp Q_I\), with compatible scales \(Q_I\ge1\), and a row weight \(\varpi(u)\) of bounded absolute value supported on \(0<Nu\le O(H)\). A scale one may also be fixed to the exact unit ideal. Let \(S_{\mathbf Q}\) denote the resulting signed tuple-row sum, retaining the original coupled tests. A complete block here means the entire sum at those scales; it does not permit arbitrary further tuple-dependent cuts after the estimate.

Write
\[
p_I=\begin{cases}b,&m_I\text{ odd},\\1,&m_I\text{ even},\end{cases}
\qquad
\mathcal B=\prod_IQ_I^{p_I}.
\tag{6.2}
\]
Odd axes have inverse coefficients \(\mu\); even axes have coefficients \(\mu^2\). Suppose the corresponding inverse odd axes satisfy \(\mathrm{PW}_b^{\rm sm}\), with all finite twists and moving masks specified in Section 1.

### Available square-mean costs

For an axis \(I\), let \(\mathcal Q_I(H,Q_I)\) denote a normalized row \(L^2\) cost, so that its independent polynomial has squared row norm \(\ll D^\epsilon H\mathcal Q_I^2\), uniformly under moving column exclusions. The following choices are valid:

| Axis | Valid normalized cost \(\mathcal Q_I(H,Q)\) | Input |
| --- | --- | --- |
| Odd, \(e_I\equiv1,5\pmod6\) | \(Q^{1/2}\) | Optional \(\mathrm{NM2}\) |
| Odd, \(e_I\equiv3\pmod6\) | \(\{Q+H^{-1/2}Q^2\}^{1/2}\) | Classical quadratic sieve |
| Odd, \(e_I\equiv3\pmod6\) | \(\{Q+H^{-1/2}Q^{1+b}\}^{1/2}\) | Smooth (Q-refined) |
| Even, \(e_I\equiv2,4\pmod6\) | \(\{Q+H^{-2/3}Q^2+H^{-1/3}Q^{5/3}\}^{1/2}\) | Classical cubic sieve |
| Nonprincipal sextic | \(\{Q+H^{-5/6}Q^2+H^{-1/3}Q^{5/3}\}^{1/2}\) | Classical sextic sieve |
| Principal mask, \(e_I\equiv0\pmod6\) | \(Q\) | Counting |

An odd axis also has the pointwise cost \(Q^b\). One may select any applicable cost, or their minimum, provided its analytic premise is retained. The tests in this section are smooth, so the optional refined quadratic row does not itself require the sharp-test upgrade \(\mathrm R_b\).

Define its score by
\[
\mathcal S_I=\frac{Q_I^{p_I}}{\mathcal Q_I(H,Q_I)}.
\tag{6.3}
\]
The score measures the saving when that axis is averaged in row \(L^2\) instead of counted or bounded pointwise.

### Lemma 6.1: mixed positive and inverse coefficients have the same correction majorant

Freeze all even incidence variables except any even variables chosen as the two averaged axes. Let \(C\) be the product of these frozen ideals. Retain all odd variables and the selected even ones as free axes. Write \(s_j=(-1)^{m_j}\) for each free axis; its independent local series is \(1+s_jz_j\). Pairwise disjointness of the free variables requires the local numerator \(1+\sum_js_jz_j\). Thus the forward correction is
\[
E_{C,p}(\mathbf z)=
\begin{cases}
\displaystyle\frac{1+\sum_js_jz_j}{\prod_j(1+s_jz_j)},&p\nmid CS,\\[6pt]
\displaystyle\frac1{\prod_j(1+s_jz_j)},&p\mid C,\ p\notin S,\\
1,&p\in S.
\end{cases}
\tag{6.4}
\]
The substitution \(w_j=-s_jz_j\) turns the first expression into \((1-\sum_jw_j)/\prod_j(1-w_j)\). Therefore a nonconstant monomial supported on \(J\) has absolute coefficient \(|1-|J||\); outside the mask, every one-axis term vanishes. At a mask prime every coefficient has absolute value one. These statements include prime powers in the correction.

If every \(\alpha_j\ge1/2\), then, on any polynomially bounded finite support,
\[
\sum_{\rm contributing\ \mathbf d}|e_C(\mathbf d)|
\prod_j(Nd_j)^{-\alpha_j}\ll_\epsilon D^\epsilon,
\qquad NC\le D^{O_k(1)}.
\tag{6.5}
\]
Indeed at weights \(1/2+\delta\) or larger the unmasked nonconstant local mass is
\[
\sum_{|J|\ge2}(|J|-1)\prod_{j\in J}
\frac{(Np)^{-\alpha_j-\delta}}{1-(Np)^{-\alpha_j-\delta}}
=O((Np)^{-1-2\delta}).
\]
Its prime-ideal product converges. The mask-prime product is
\[
\prod_{p\mid C}\prod_j(1-(Np)^{-\alpha_j-\delta})^{-1}
\ll_\eta(NC)^\eta.
\]
Returning to the critical finite-support weights costs \(D^{O_k(\delta)}\), which can be absorbed with \(\eta\) in the chosen epsilon. All fixed small-prime factors are finite; none is removed. The resulting finite convolution has exterior factors \(\prod_j\xi_{j,u}(d_j)\) of modulus at most one, where \(\xi_{j,u}\) is the literal character in (6.1). At a nonunit all corresponding nonconstant terms still vanish. \(\square\)

### Theorem 6.2: a two-axis selector

For any two distinct free axes \(J,L\) with applicable costs from the table,
\[
\boxed{
|S_{\mathbf Q}|
\ll_\epsilon
HD^\epsilon
\frac{\mathcal B}{\mathcal S_J\mathcal S_L}.
}
\tag{6.6}
\]
Here all original factor scales are \(\asymp D\), and \(H\) has a fixed polynomial relation to \(D\). The row estimate is uniform in the frozen masks. One may minimize the right side over the available pair of axes and costs.

**Proof.** Freeze the indicated other even variables. Their number is
\[
O_k\!\left(\prod_{\substack{I\ {\rm even}\\I\ne J,L}}Q_I\right),
\]
and their row factors have modulus at most one. The requirement that the frozen ideals themselves be pairwise coprime may be retained, or their positive counting majorant may be enlarged.

Mellin-invert the \(2k\) original smooth factor tests before any row estimate. For an incidence variable \(q_I\), the resulting imaginary norm exponent is \(\tau_I=\sum_{i\in I}t_i\), and its smooth dyadic test is \(\psi_I(Nq_I/Q_I)(Nq_I/Q_I)^{-i\tau_I}\). Fixed compact support and finite test seminorms give a polynomial in the Mellin frequencies, integrable against the rapidly decreasing original transforms. Thus the coupled weights are exactly separated without discarding any original coefficient.

Apply the finite convolution from Lemma 6.1 to the remaining pairwise-coprime free variables, with the frozen mask \(C\). On each independent product use row Cauchy on \(J,L\), and the uniform pointwise bounds on all remaining odd axes. The selected pair costs
\[
H\,\mathcal Q_J(H,Q_J/Nd_J)
\mathcal Q_L(H,Q_L/Nd_L).
\]
For every cost in the table, expand a square root of a sum into the sum of square roots of its finitely many monomials. The column exponents in these monomials are at least \(1/2\): they are \(1/2,1,5/6\), or \((1+b)/2\). All other free weights equal \(b>1/2\). Lemma 6.1 therefore sums the correction with loss \(D^\epsilon\). Recombining the finite square-root terms changes the bound only by a fixed constant. If one uses a minimum of applicable costs, choose that valid branch at the original scales before applying this argument.

Every shifted scale is smaller. Empty scales vanish, and bounded scales below one are absorbed uniformly. Summing the frozen variables and integrating the Mellin frequencies yields exactly (6.6). No arbitrary arithmetic coefficients enter \(\mathrm{NM2}\) or the pointwise hypothesis; they have been removed by the explicit finite correction. The classical selected even axes do permit arbitrary bounded coefficients. \(\square\)

For comparison with the earlier incidence normalization, put
\[
L_1=\prod_{|I|=1}Q_I,\qquad
\Gamma=\prod_{|I|\ge3}Q_I^{|I|-2}.
\tag{6.7}
\]
Compatibility with the \(2k\) original tests gives \(\prod_IQ_I^{|I|}\asymp D^{2k}\). Consequently
\[
\prod_IQ_I\asymp D^k\sqrt{L_1/\Gamma},
\]
and (6.6) is equivalently
\[
\boxed{
|S_{\mathbf Q}|
\ll_\epsilon HD^{k+\epsilon}
\sqrt{\frac{L_1}{\Gamma}}\,
\frac{\prod_{I\ {\rm odd}}Q_I^{b-1}}
     {\mathcal S_J\mathcal S_L}.
}
\tag{6.8}
\]
If the two selected axes are eligible odd inverse axes with native cost \(Q^{1/2}\), this recovers the two-axis bound of PR #921. The new possibilities include either or both axes having even multiplicity and positive cubic coefficients.

Because \(k\) is fixed, there are only a fixed power of \(\log D\) smooth dyadic scale blocks. Therefore a specified collection of complete blocks on which the normalized right side of (6.8) is at most \(D^\lambda\) has total signed contribution \(O_\epsilon(HD^{k+\lambda+\epsilon})\). This uses the triangle inequality between whole blocks. It does not use monotonicity of an internal signed tuple sum under deletion of arbitrary tuples.

### Lemma 6.3: an entire physical cubic product

Let \(j\ge1\) be fixed, and let
\[
P_{i,u}=\sum_{\substack{n\ {\rm squarefree}\\Nn\asymp Y_i}}
z_{i,n}\chi_n(u)^{[e]},
\qquad |z_{i,n}|\le1,\qquad e\equiv2\text{ or }4\pmod6.
\]
The same residue class \(e\) is used in all factors; arbitrary fixed twists, tests, and exclusions may be included in the coefficients. Put \(P=\prod_{i=1}^jY_i\). Then
\[
\boxed{
\sum_{0<Nu\le H}\left|\prod_{i=1}^jP_{i,u}\right|^2
\ll_\epsilon D^\epsilon
\left[HP+H^{1/3}P^2+H^{2/3}P^{5/3}\right].
}
\tag{6.9}
\]
All \(Y_i\) and \(H\) lie in fixed polynomial ranges in \(D\); nonempty bounded scales below one are harmless.

**Proof.** Decompose every ordered tuple of squarefree columns into exact shared-prime incidence ideals. Freeze all shared labels of multiplicity \(m\ge2\). The exterior row factors, including the principal masks when \(3\mid m\), have modulus at most one. The remaining pairwise-coprime singleton columns have product scale
\[
P_{\mathbf c}=P\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\]
Because their row powers are all \(e\), they combine into the same cubic character at one squarefree product column. The squared coefficient mass at that column is
\(O_\epsilon(D^\epsilon P_{\mathbf c})\): first count the \(O(P_{\mathbf c})\) supported ordered tuples, then use the fixed-order ideal divisor bound for the number representing a given product. All exclusions stay in that coefficient.

The all-row cubic sieve (2.1) gives the row norm
\[
\ll D^\epsilon\left[
H^{1/2}P_{\mathbf c}^{1/2}
+H^{1/6}P_{\mathbf c}
+H^{1/3}P_{\mathbf c}^{5/6}\right].
\]
Minkowski over shared labels assigns a multiplicity-\(m\) label the respective weights \(m/2,m,5m/6\). Only the first term with \(m=2\) is critical; its finite ideal sum is logarithmic. The other weights exceed one and sum absolutely. Their fixed number of logarithms is \(D^\epsilon\). Squaring proves (6.9). This proof accounts for every collision of the independent product; it does not pretend the product columns were squarefree without decomposition. \(\square\)

Define
\[
\mathcal R_3(H,P)
=\{P+H^{-2/3}P^2+H^{-1/3}P^{5/3}\}^{1/2}.
\tag{6.10}
\]
Let \(\mathcal J,\mathcal L\) be disjoint nonempty groups of even incidence axes. Within each group the net row exponents are all congruent to 2, or all congruent to 4, modulo 6; the two groups may have different congruence classes. Put \(P_{\mathcal J}=\prod_{I\in\mathcal J}Q_I\), and similarly \(P_{\mathcal L}\). Freeze all other even variables, and retain every odd variable.

### Corollary 6.4: two grouped cubic axes

In the hypotheses of Theorem 6.2,
\[
\boxed{
|S_{\mathbf Q}|
\ll_\epsilon HD^\epsilon\mathcal B\,
\frac{\mathcal R_3(H,P_{\mathcal J})}{P_{\mathcal J}}\,
\frac{\mathcal R_3(H,P_{\mathcal L})}{P_{\mathcal L}}.
}
\tag{6.11}
\]

**Proof.** Apply the same exact correction (6.4) with all axes in both groups free. On the independent product, row Cauchy is now between the two entire cubic products. Lemma 6.3 supplies their row \(L^2\) bounds. Other odd variables retain their pointwise bounds. Each monomial in either group row norm assigns every axis in that group one of the weights \(1/2,1,5/6\). Lemma 6.1 was proved for arbitrarily many critical weights at or above \(1/2\), with the number of axes fixed. It therefore sums this correction too, including all cross-group eligibility conditions. The frozen-variable counts and the Mellin integrals are exactly those in Theorem 6.2. This yields (6.11). \(\square\)

One can in particular place every even net-exponent-2 incidence axis in one group and every even net-exponent-4 axis in the other, when both groups are nonempty. Their coefficients may be positive \(\mu^2\); no inverse second-moment estimate is applied to them.

## 7. A new diagonal-size double-triangle sector

### Corollary 7.1

Take the sixth moment, with unbarred positions \(1,2,3\) and barred positions \(4,5,6\). Let
\[
q_{12},q_{13},q_{23},q_{45},q_{46},q_{56}\asymp R=D^r,
\tag{7.1}
\]
and require every other repeated incidence ideal to be one. The six singleton scales are
\[
X=D/R^2.
\tag{7.2}
\]
Assume the original fixed tests have compatible nonempty support at these scales, and apply smooth dyadic incidence tests to the six pair variables and singletons. If \(1<h\le11/10\), \(H=D^h\), and \(0\le r\le1/2\), then under \(\mathrm{PW}_b^{\rm sm}\),
\[
\boxed{
|S_R|
\ll_\epsilon HD^\epsilon R^5X^{6b}
=HD^{6b+\epsilon}R^{5-12b}.
}
\tag{7.3}
\]

**Proof.** Every displayed pair variable has multiplicity two and net exponent \(2\) or \(-2\). Its coefficient is positive \(\mu^2\), and its character is cubic. As \(R\le D^{1/2}\le H^{1/2}\), each such axis has normalized cubic cost \(R^{1/2}\): both \(R/H^{2/3}\) and \((R^2/H)^{1/3}\) are bounded. Select any two of these pair axes in Theorem 6.2. The four frozen pair variables cost \(R^4\); row Cauchy on the two selected axes costs \(HR\); the six odd singleton variables cost \(X^{6b}\). Lemma 6.1 retains all cross exclusions and pairwise disjointness. This proves (7.3). \(\square\)

The diagonal target \(HD^3\) is attained when
\[
r\ge r_{\rm cubic}(b):=\frac{6b-3}{12b-5}.
\tag{7.4}
\]
For every \(b>1/2\), the denominator is positive and \(0<r_{\rm cubic}(b)<1/2\), so the stated scale range is consistent. At \(b=7/8\),
\[
\boxed{r\ge\frac9{22}.}
\tag{7.5}
\]
The original columns may have smooth tests different from each other; this is a complete signed incidence-sector estimate rather than a positivity argument.

### Corollary 7.2: grouping both whole triangles gives a stronger bound

For the same compatible blocks, under \(\mathrm{PW}_b^{\rm sm}\),
\[
\boxed{
|S_R|\ll_\epsilon
HD^\epsilon X^{6b}
\left[R^3+H^{-2/3}R^6+H^{-1/3}R^5\right].
}
\tag{7.6}
\]
Choose \(\mathcal J=\{12,13,23\}\), with row exponent 2, and
\(\mathcal L=\{45,46,56\}\), with row exponent \(-2\equiv4\pmod6\).
Both product scales are \(R^3\). Substitution in (6.11), with
\(\mathcal B=R^6X^{6b}\), proves (7.6). In particular the internal shared-prime expansion in Lemma 6.3 occurs only in the independent products of the correction; the original six incidence ideals remain exactly pairwise coprime.

At \(b=7/8\), the three cutoff exponents against \(HD^3\) are
\[
\frac3{10},\qquad
\frac12-\frac{4h}{27},\qquad
\frac{27-4h}{66}.
\tag{7.7}
\]
For \(1<h\le11/10\) the first is smaller than both others, and the last two cross at \(h=27/26\). Thus the diagonal-size range begins at
\[
\boxed{
r\ge r_{\rm grouped}(h):=
\begin{cases}
\displaystyle\frac12-\frac{4h}{27},&1<h\le27/26,\\[4pt]
\displaystyle\frac{27-4h}{66},&27/26\le h\le11/10.
\end{cases}}
\tag{7.8}
\]
For \(h=21/20\), this is
\[
\boxed{r\ge\frac{19}{55}.}
\tag{7.9}
\]
These are upper bounds on the absolute value of the complete signed Hermitian sector. They are not bounds for the full sixth-moment polynomial norm or for a sum of absolute values of individual tuples.

### Strict comparison with the pinned earlier selectors

For this precise configuration, PR #921 freezes all six even pair ideals and can select only two singleton inverse axes. Its bound is
\[
H R^6 X^{1+4b}.
\tag{7.10}
\]
At \(b=7/8\), this equals \(HD^{9/2}R^{-3}\), reaching \(HD^3\) only at \(r\ge1/2\).

PR #923's one-sided subset-product selector applies on either triangle with three singleton lengths \(X\). Its zero-excess condition, for \(X=D^{1-2r}\) with \(r<1/2\), requires using all three singleton axes in the classical product estimate. Every proper subset leaves the positive exponent \((2b-1)\) on an omitted growing singleton scale. The full-subset cost is
\[
1+\frac{X^3}{H^{5/6}}+
\left(\frac{X^6}{H}\right)^{1/3},
\tag{7.11}
\]
so it has zero power loss exactly when
\[
3(1-2r)\le h/2,\qquad
r\ge\frac12-\frac h{12}.
\tag{7.12}
\]
This gives the same threshold for the signed double-triangle block by row Cauchy between the two one-sided polynomials; their frozen pair counts are already included in the normalization \(R^6X^3=D^3\).

At \(h=21/20\), (7.12) is \(r\ge33/80\). The elementary two-individual-axis range starts at \(9/22\), a strict decrease
\[
\frac{33}{80}-\frac9{22}=\frac3{880}>0.
\tag{7.13}
\]
The grouped version improves further:
\[
\frac{33}{80}-\frac{19}{55}=\frac{59}{880}>0.
\tag{7.14}
\]
It is a strict extension of the earlier zero-excess range throughout \(1<h\le11/10\). Indeed the previous threshold \(\tfrac12-h/12\) exceeds the second entry of (7.7) by \(7h/108>0\), the third by \(1/11-h/44>0\), and the first by \(1/5-h/12>0\) in that interval. These comparisons concern the matched double-triangle configuration, not every sector treated by the source.

This block has no triple or higher incidence ideal, so \(\Gamma=1\). Each one-sided triple has ordinary common gcd one. There is also no cross-side shared prime. It is therefore absent from all nontrivial one-sided common-triple tails and from the global Hermitian common-gcd tail.

In the pinned averaged-conductor notation, \(g_1\) is the product of the six singleton ideals and \(g_2\) the product of the six nonprincipal double ideals. Thus
\[
Ng_1\asymp X^6,\qquad Ng_2\asymp R^6,\qquad
Ng_1\sqrt{Ng_2}\asymp D^{6-9r}.
\tag{7.15}
\]
For \(r<1/2\) and a growing compatible block, \(g_1\ne1\); throughout \(r\le1/2\), \(6-9r\ge3/2>h\). Hence these nontrivial blocks lie on the large-conductor side of the surviving signed sector. The estimate uses cancellation after summing the complete incidence block, rather than the absolute accounting estimate for each tuple.

### Corollary 7.3: embedding in every higher fixed moment

For any fixed \(k\ge3\), place the two triangles on three unbarred and three barred positions. For each of the remaining \(k-3\) unbarred positions, match it with one barred position and require their sole repeated ideal to have norm \(\asymp D\); all other repeated ideals are one. Their remaining singleton scales are bounded. Provided the original tests have nonempty compatible support, these matched cross pairs cost \(O(D^{k-3})\) choices and contribute only literal principal masks to the six active inverse axes.

Theorem 6.2, with those additional masks retained, gives
\[
|S_R^{(k)}|
\ll_\epsilon HD^{k-3+6b+\epsilon}R^{5-12b}.
\tag{7.16}
\]
Corollary 6.4 gives the stronger bound
\[
|S_R^{(k)}|
\ll_\epsilon HD^{k-3+\epsilon}X^{6b}
\left[R^3+H^{-2/3}R^6+H^{-1/3}R^5\right].
\tag{7.17}
\]
Thus the same \(r\ge r_{\rm grouped}(h)\) condition at \(b=7/8\) reaches \(HD^k\) for this specified portion of every fixed \(2k\)-th moment; at \(h=21/20\) it is \(r\ge19/55\). This is a restricted incidence family at each order; it is not coverage of the full moment or of every low-gcd configuration.

## 8. What the improvements do not settle

The fourth-moment theorem decreases a sharp one-sided gcd cutoff from \((6-h)/7\) to \((9-2h)/11\) under the explicit pointwise premise. The double-triangle theorem treats a new low-multiplicity signed sector through two groups of positive cubic axes. Neither theorem changes the fully singleton incidence block, where every repeated ideal is the unit ideal.

On that fully singleton block, the present two-axis architecture has only inverse singleton axes. If it uses two native second moments and pointwise exponent \(b\) on the other \(2k-2\) factors, it gives
\[
H D^{1+2b(k-1)+\epsilon}
=HD^{k+(2b-1)(k-1)+\epsilon}.
\tag{8.1}
\]
At \(b=7/8\), the excess is \(3(k-1)/4\), linear in \(k\). Grouping subsets using the earlier arbitrary-coefficient product sieve does not alter this conclusion merely by adding the new repeated-variable axes, because those axes are absent. This is a limitation of the specified norm estimates; it is not an impossibility theorem for signed arithmetic cancellation in that family.

A full result approaching the generalized diagonal moment hierarchy still needs a new estimate for the surviving signed long-conductor average or for a sufficiently comprehensive collection of those long singleton blocks. No such estimate is assumed implicitly in Sections 3--7.

## 9. Pinned files and provenance

The six source files retrieved for this attack were materialized at their actual repository paths, with byte lengths, Git blob IDs, commit pins, and SHA256 values recorded in the separate source manifest attack3_moment_sources.json. They were not edited.

The load-bearing source identities are:

| Pinned source | Commit | File SHA256 |
| --- | --- | --- |
| PR #923, SUBSET_PRODUCT_INCIDENCE.md | 1a1152008706f7e24fa1efe4990588f8f99c5d8d | 9d62a79c0074c7506d273ff7203807e4efd054bfdf0b85baddf340304da4f3de |
| PR #923, CROSS_SIDE_SEPARATION_SECTOR.md | 1a1152008706f7e24fa1efe4990588f8f99c5d8d | 299b8cc4f981bd1bdfe1c3c8ac4b0d4eea23eec77c4e87b4ac46ff6ee0dcb263 |
| PR #921, HERMITIAN_INCIDENCE.md | 4e6d4aa57ae4cb04d76b2b31279ac367951b469a | 5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9 |
| PR #915, ANISOTROPIC_SINGLETON_CORES.md | 9959364671f89b86f3992ec5ed5e19f804eb607b | 4854a01c2767a1dc4d7c67c490e5502bcad8935bce3089ba5f37adb1e6d02ea8 |
| PR #917, OSCILLATING_OVERLAPS.md | 6b4723042b3d250024eef45cb1924f88f28e902c | 271f4f71bda533810ee49f6498f4ffbc42c3f0cb37c59151f9f703e715f58397 |

The external squarefree character sieves, their fixed ray/unit conventions, and the distinction between classical and imported inverse inputs remain exactly as identified in Sections 1--2. The independent quadratic component and its checked local content hash are identified in Section 5.2. These pins establish which statements are being composed; they do not certify the truth of a source-qualified analytic premise.
