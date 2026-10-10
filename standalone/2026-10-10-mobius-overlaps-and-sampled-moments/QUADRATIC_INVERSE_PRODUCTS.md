# Quadratic inverse products: averaging the square part before interpolation

Status: proposed proved deductions from the classical squarefree quadratic large sieve and the explicitly stated pointwise or reciprocal-L premises. The main estimate applies to every fixed product length and every nonzero Eisenstein row. It is a new component estimate for the generalized sextic-moment program, not a full sextic moment theorem or a new zero-free region.

Exact sources: Goldmakher--Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642v2, Theorem 1.1 and Corollary 1.2; the fixed primary/ray conventions and literal zero extension in PR #917, commit `6b4723042b3d250024eef45cb1924f88f28e902c`; and the reciprocal argument in PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md`, Lemma 8.1. The latter is used only under its stated common finite-order zero-free premise. No native sextic second-moment theorem is needed below.

What was actually checked: the primary quadratic-sieve statement and its squarefree-index convention, the pinned reciprocal proof, the exact square-part reduction, the shared-prime weights, and the dyadic optimization. Finite diagnostics and independent review are recorded separately in the eventual packet.

## 1. Definitions and distinct analytic premises

Let \(K=\mathbb Q(\sqrt{-3})\), with ring of integers \(\mathcal O_K\). Use the repository's primary generators for ideals and all six unit rows when summing elements. Fix a finite set \(S\) containing primes over 6 and the conductors of the fixed finite-order characters below. Write

\[
\rho_n(u)=\chi_n(u)^3=(u/n)_2.
\tag{1.1}
\]

This symbol has value zero when \((n,u)\ne1\). A principal even power still has that zero. After the fixed finite ray and unit partition, the squarefree-index quadratic Hecke-family sieve is

\[
\sum_{\substack{a\ \mathrm{squarefree}\\Na\le M}}
\left|\sum_{\substack{n\ \mathrm{squarefree}\\Nn\le L}}
 z_n\rho_n(a)\right|^2
\ll_\epsilon(ML)^\epsilon(M+L)\sum_n|z_n|^2.
\tag{QLS}
\]

Both indices avoid the fixed bad primes at the point where this theorem is applied. Bad squarefree parts of a row are separated into finitely many possibilities first. The primitive-character convention in the cited paper is not used to replace any nonunit zero by one.

Fix an ambient parameter \(D\ge2\) and a fixed \(A_0\). All varying positive norm scales and auxiliary norms are at most \(D^{A_0}\); a product of a fixed number of these has another fixed polynomial bound. Implied constants may depend on this exponent and on the fixed number of factors. For nonempty column supports, bounded scales below one are absorbed into the fixed support constants; formulas are written for \(L_i\ge1\).

For fixed compactly supported smooth tests \(W_i\), fixed finite-order \(\nu_i\), and moving exclusions \(q_i\), put

\[
B_{i,u}(L_i;q_i)
=\sum_{(n,q_iS)=1}\mu_K(n)\nu_i(n)\rho_n(u)W_i(Nn/L_i).
\tag{1.2}
\]

The smooth pointwise premise \(\mathrm{PW}_{b_i}^{\mathrm{sm}}\), with \(1/2<b_i\le1\), is

\[
|B_{i,u}(L_i;q_i)|
\ll_{\epsilon}D^\epsilon L_i^{b_i}
\tag{1.3}
\]

uniformly in every polynomially bounded nonzero row and exclusion. It is required also for the finitely many unit/bad-part twists arising below. When a test is modulated by an imaginary norm power, its bound must have the usual fixed polynomial seminorm dependence. At \(b_i=1\), counting proves this premise. For \(b_i<1\), it is an explicit arithmetic input.

A separate premise, denoted \(\mathrm R_b\), concerns reciprocal L-functions. For every fixed \(\delta,\epsilon>0\), it asserts holomorphy and

\[
|L(\sigma+it,\eta)^{-1}|
\ll_{\delta,\epsilon}
[N\mathfrak f_\eta(2+|t|)]^\epsilon,
\qquad \sigma\ge b+\delta,
\tag{1.4}
\]

uniformly in the finite-order Hecke characters needed here. At a principal pole the reciprocal is its analytic zero. Imprimitive characters and additional excluded primes are handled by their finite Euler corrections. Lemma 8.1 of the pinned PR #913 proves (1.4) under its common finite-order zero-free half-plane hypothesis. In particular, invoking that route retains the imported zero-free statement as a source-qualified assumption.

The distinction matters: this note does not infer sharp interval cancellation from a smooth-test estimate whose high seminorm constants are uncontrolled.

## 2. Uniform sharp interval control from the reciprocal premise

### Lemma 2.1

Assume \(\mathrm R_b\), with \(1/2<b<1\). For polynomially bounded finite conductor, exclusion \(q\), and \(1\le x\le D^{A_0}\),

\[
\left|\sum_{\substack{Nn\le x\\(n,qS)=1}}
\mu_K(n)\eta(n)\right|
\ll_\epsilon D^\epsilon x^b.
\tag{2.1}
\]

The same holds for any interval inside a fixed annulus of scale \(L\), with right side \(D^\epsilon L^b\). A bounded-variation weight on that annulus costs its supremum plus total variation. Multiplication by \((Nn/L)^{it}\) costs a fixed polynomial in \(1+|t|\), sufficient for the Mellin separations in the companion overlap proof.

**Proof.** The Dirichlet series of the coefficients is

\[
F(s)=L(s,\eta)^{-1}
\prod_{p\mid qS}(1-\eta(p)(Np)^{-s})^{-1},
\tag{2.2}
\]

with redundant factors omitted when their character value is zero. In any fixed half-plane \(\Re s\ge b+\delta>0\), the absolute finite correction is bounded by

\[
\prod_{p\mid qS}(1-(Np)^{-b-\delta})^{-1}
\ll_{\epsilon,\delta}(Nq)^\epsilon.
\tag{2.3}
\]

To prove the last estimate, each sufficiently large prime factor is bounded by \((Np)^\epsilon\); the finitely many smaller ones give a fixed constant. Thus \(F\) has the uniform holomorphic reciprocal bound with all exclusions retained.

Group ideals by their integer norm, writing \(F(s)=\sum_{m\ge1}a_m m^{-s}\). The number of ideals of a given norm over this quadratic field is at most the ordinary integer divisor function \(\tau(m)\): at a split prime the local count is the exponent plus one, and the inert and ramified local counts are smaller. Hence \(|a_m|\le\tau(m)\ll_\varepsilon m^\varepsilon\), uniformly in the character and mask. Replace \(x\) by \(x_0=\lfloor x\rfloor+1/2\); the partial sum is unchanged. For bounded \(x\) the claim follows directly.

Apply truncated Perron on \(c=1+1/\log(2x_0)\), at height \(T=D^A\), where \(A\) is a sufficiently large fixed constant. Because every norm is at distance at least \(1/2\) from \(x_0\), the standard Perron truncation error is bounded directly by

\[
\sum_m |a_m|(x_0/m)^c
\min\{1,(T|\log(x_0/m)|)^{-1}\}
\ll_\varepsilon x_0^{1+\varepsilon}T^{-1}\log^2(2x_0).
\tag{2.4}
\]

For completeness, on \(x_0/2<m<2x_0\) use
\(|\log(x_0/m)|\gg |m-x_0|/x_0\), the half-integer separation, and the harmonic sum over distances. Outside that interval, use absolute convergence at \(c\), which has only a fixed logarithmic cost for the ideal divisor majorant. Take \(T\ge D^{2A_0+2}\) so every displayed estimate is in the small-error regime.

Move the finite contour to \(\sigma_0=b+\delta\). There are no reciprocal poles in the rectangle, and the Perron pole at zero is not crossed. The new vertical integral is bounded by

\[
x_0^{b+\delta}[N\mathfrak f_\eta\,Nq\,(2+T)]^{\varepsilon_0}\log(2T).
\tag{2.5}
\]

The two horizontal integrals are
\(O(x_0^c[N\mathfrak f_\eta Nq(2+T)]^{\varepsilon_0}/T)\).
Choose \(\delta>0\) and then \(\varepsilon_0>0\) sufficiently small in terms of the requested ambient loss \(\epsilon\), the fixed polynomial bounds, and \(A\). Equations (2.4)--(2.5) give (2.1).

An interval is a difference of two such sums. Partial summation proves the bounded-variation statement. On a fixed positive annulus, \((Nn/L)^{it}\) has variation \(O(1+|t|)\), so no new angular-character theorem is needed. \(\square\)

For \(b=1\), all these interval statements follow from counting. Lemma 2.1 is used only when an interval-truncated inverse column is required. The smooth main theorem below requires only (1.3).

## 3. A squarefree-row bound for an entire quadratic product

### Lemma 3.1

Let \(j\ge1\) be fixed. Each \(P_{i,a}\) is a sum on squarefree columns in a fixed annulus of norm scale \(L_i\), with arbitrary bounded row-independent coefficients multiplying \(\rho_n(a)\). Arbitrary fixed exclusions in these coefficients are permitted. Put \(P=\prod_{i=1}^jL_i\). Then

\[
\sum_{\substack{a\ \mathrm{squarefree}\\Na\le M}}
\left|\prod_{i=1}^jP_{i,a}\right|^2
\ll_{j,\epsilon}D^\epsilon(MP+P^2).
\tag{3.1}
\]

**Proof.** Decompose each ordered tuple of squarefree columns into its exact incidence ideals \(c_I\), where a prime belongs to \(c_I\) precisely when it occurs in the positions \(I\). Freeze all labels with \(|I|\ge2\). Their product row character, including any even-power masks, has modulus at most one. The remaining singleton ideals are pairwise coprime, have scales

\[
Z_i=L_i\Big/\prod_{I\ni i,\ |I|\ge2}Nc_I,
\qquad
P_{\mathbf c}=\prod_i Z_i
=P\prod_{|I|\ge2}(Nc_I)^{-|I|},
\tag{3.2}
\]

and can be grouped into one squarefree product column. At that column, the tuple multiplicity is bounded by a fixed-order ideal divisor function. Its squared coefficient mass is \(O_\epsilon(D^\epsilon P_{\mathbf c})\): count the \(O(P_{\mathbf c})\) supported tuples first, and then bound their multiplicity at each product. Bounded nonempty scales below one cost only fixed support constants.

The quadratic sieve gives row norm

\[
\ll D^{\epsilon_0}
\left(M^{1/2}P_{\mathbf c}^{1/2}+P_{\mathbf c}\right).
\tag{3.3}
\]

Use Minkowski over the frozen shared labels. In the first term, a label of multiplicity \(m\) has weight \((Nc_I)^{-m/2}\). Pair incidences have a logarithmic sum; higher incidences have convergent sums. In the second term, every weight \((Nc_I)^{-m}\), \(m\ge2\), is summable. The fixed number of logarithms fits in \(D^\epsilon\). Squaring proves (3.1). Every exclusion remains in the row-independent column coefficient before the sieve, and every exterior nonunit zero remains a contraction. \(\square\)

This lemma concerns a physical product, with all its internal collisions. It does not replace that product by a squarefree-only product without accounting for the repeated primes.

## 4. The all-row product theorem

### Theorem 4.1

Assume \(\mathrm{PW}_{b_i}^{\mathrm{sm}}\) for the \(j\) factors (1.2). Put

\[
P=\prod_{i=1}^j L_i,
\qquad R=\prod_{i=1}^j L_i^{b_i}.
\]

Uniformly in every stated moving exclusion,

\[
\boxed{
\sum_{0<Nu\le H}
\left|\prod_{i=1}^jB_{i,u}(L_i;q_i)\right|^2
\ll_\epsilon D^\epsilon
\min\{HR^2,\ HP+H^{1/2}PR\}.
}
\tag{4.1}
\]

The same result holds for interval-truncated or uniformly bounded-variation column tests if the corresponding interval pointwise premise is supplied, in particular under \(\mathrm R_{b_i}\) by Lemma 2.1.

**Proof.** Decompose each nonzero row uniquely at the ideal level as

\[
u=\varepsilon v^2a,\qquad a\ \mathrm{squarefree}.
\tag{4.2}
\]

The ideal \(v\) is arbitrary and may overlap \(a\). The six unit choices and the finitely many bad squarefree parts of \(a\) are kept in fixed sectors. The literal symbol identity is

\[
\rho_n(\varepsilon v^2a)
=\rho_n(\varepsilon a)\mathbf1_{(n,v)=1}.
\tag{4.3}
\]

Thus fixing \(v\) changes the exclusion in the \(i\)-th column to \(q_i v\); it does not remove that exclusion. At \(Nv\asymp V\), the remaining squarefree row has norm at most \(H/V^2\), up to a fixed dyadic factor. There are \(O(V)\) possible \(v\). Lemma 3.1 therefore gives for this dyad

\[
\mathcal E_V
\ll D^{\epsilon_0}
\left(\frac{HP}{V}+VP^2\right).
\tag{4.4}
\]

The uniform pointwise premise and the \(O(H/V)\) actual row count give independently

\[
\mathcal E_V\ll D^{\epsilon_0}\frac{HR^2}{V}.
\tag{4.5}
\]

We apply a minimum of the two valid positive bounds on the same dyad. For nonnegative quantities,
\(\min(A+B,C)\le A+\min(B,C)\), hence

\[
\mathcal E_V
\ll D^{\epsilon_0}
\left\{\frac{HP}{V}
+\min\left(VP^2,\frac{HR^2}{V}\right)\right\}.
\tag{4.6}
\]

Sum over dyadic \(1\le V\ll\sqrt H\). The first terms form a geometric sum \(O(HP)\). The other terms switch at

\[
V_*=\frac{\sqrt H\,R}{P}.
\tag{4.7}
\]

Below \(V_*\), sum \(VP^2\); above it, sum \(HR^2/V\). Each sum is \(O(\sqrt H\,PR)\). This upper bound remains valid if the switch lies outside the actual range: use just the corresponding geometric half. Thus (4.6) gives the second entry in (4.1). The first entry is the pointwise bound over all \(O(H)\) rows. All preliminary losses can be reassigned to the prescribed \(\epsilon\). \(\square\)

### Corollary 4.2. A sharper quadratic inverse second moment

For one factor of length \(L\),

\[
\boxed{
\sum_{0<Nu\le H}|B_u(L;q)|^2
\ll_\epsilon D^\epsilon
\min\{HL^{2b},\ HL+H^{1/2}L^{1+b}\}.
}
\tag{4.8}
\]

The classical all-row bound has second term \(H^{1/2}L^2\). The new term replaces exponent 2 by \(1+b\), under the displayed pointwise premise. It reaches \(HL\) when \(H\ge L^{2b}\). At \(b=7/8\), this sufficient height is \(H\ge L^{7/4}\), rather than the classical \(L^2\).

For \(j\) identical factors, Theorem 4.1 gives every fixed quadratic moment:

\[
\sum_{0<Nu\le H}|B_u(L;q)|^{2j}
\ll_{j,\epsilon}D^\epsilon
\min\{HL^{2jb},\ HL^j+H^{1/2}L^{j(1+b)}\}.
\tag{4.9}
\]

No uniform-in-\(j\) constant is asserted. These are quadratic-character sums arising from net sextic exponent 3, not the original net-exponent-1 sextic moment.

## 5. Interface with odd common factors and its scope

In a degree-three common-gcd decomposition of the original sextic polynomial, the common factor carries

\[
\mu_K(c)^3\nu(c)^3\chi_c(u)^3
=\mu_K(c)\nu(c)^3\rho_c(u).
\tag{5.1}
\]

It therefore belongs to the quadratic inverse family. The mixed collision correction in the companion overlap note retains the disjointness between this common factor and the residual columns. Applying (4.8) with the other three columns bounded pointwise gives the tail expression

\[
D^{6b+\epsilon}
\left[HC^{1-6b}+H^{1/2}C^{1-5b}\right],
\tag{5.2}
\]

provided that companion exact correction and its specified test class are used. Formula (5.2) is only the interface here; the full polynomial-tail proof is in the companion note. With sharp common-gcd thresholds, the stronger interval premise is retained explicitly.

At \(b=7/8\), \(H=D^h\), \(1<h\le11/10\), comparison with \(HD^3\) gives

\[
\max\left\{\frac9{17},\frac{18-4h}{27}\right\}
=\frac9{17}.
\tag{5.3}
\]

Thus the refined quadratic component allows the degree-three common-factor tail to reach diagonal size at \(C\ge D^{9/17}\) under its stated premises. This is a common-factor cutoff in a sixth-moment polynomial piece; it is not a zero-free boundary.

## 6. Remaining limitation

At every moment order, the fully singleton sextic core has no such common quadratic factor. Theorem 4.1 gives no estimate for that complementary coefficient family. Likewise, a smooth pointwise premise alone is not silently promoted to a sharp interval theorem. The generalized short-row sextic moment, the signed long-dual covariance, and any improved zero-free half-plane remain open.
