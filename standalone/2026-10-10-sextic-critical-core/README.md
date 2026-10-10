# Coupled reflection and further sextic-moment ranges

Research pass: 10 October 2026. This packet builds on [PR #913 at its exact head](https://github.com/GettysburgResearch/riemann/tree/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent) and combines it with pinned work from [#911](https://github.com/GettysburgResearch/riemann/pull/911) and [#912](https://github.com/GettysburgResearch/riemann/pull/912).

**The full fourth moment, the boundary \(17/24\), the unbounded moment hierarchy, and RH remain open.** This pass establishes further component estimates and exact analytic reductions, with explicit dependencies and independent AI-agent proof review. It does not improve the preceding source-conditional zero-free boundary \(139999/160000\). It is proposed standalone research, with no promotion to the integrated record and no Lean verification.

The principal advance is to keep the divisor factor coupled through the theta reflection. An exact Gauss cancellation leaves a quadratic character and an angular weight. This gives stronger estimates for several actual reflected components. Reuniting their Ramanujan terms also produces an explicit joint Euler factorization, including a finite-order \(L\)-factor and its possible polar divisor.

## The target and the two different row scales

The original inverse family is

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad K=\mathbb Q(\sqrt{-3}),
\]

Here \(\nu\) is a fixed finite-order Hecke character, and \(S\) is fixed and contains its bad primes and the primes over 6. Keep the fixed primary convention and literal nonunit zeros. Implied constants may depend on these fixed choices. The desired bound is

\[
M_{2k}(D,H;W):=\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{\epsilon,k,W,\theta} H D^{k+\epsilon},
\qquad H=D^{1+\theta}.
\]

At \(k=2\), this would give the limiting boundary \(1/2+5/24=17/24\), by the previously established moment-to-zero adapter as \(\theta\downarrow0\). An unbounded sequence of fixed orders with sublinear exponent loss would approach \(1/2\). Constants may depend on each fixed order; the limit in the arithmetic scale is taken first.

In the reflection notes, the letter \(H\) instead denotes a **dual** row norm. Call it \(\mathcal H\) here. The difficult initial fourth-moment transform has \(\mathcal H\asymp D^{3-\theta}\), with balanced factor lengths \(A=B=D\). Neither arithmetic row norm is the imaginary height of a zeta zero.

## 1. A stronger coupled theta estimate

The full source scalar gives the exact identity

\[
\chi_a(k)\,C(k,a)\,a_\xi(a)
=F_0\,\Gamma(k)\,\Xi(a)\,
 \overline{\alpha(a)}^3\chi_a(k)^3.
\]

The cubic Gauss factor of the outer divisor cancels its conjugate factor inside the reflection. The angular factor \(\overline{\alpha(a)}^3\), every fixed-ray factor, and the original zero masks remain.

Expand the local Ramanujan factor as

\[
q^{-1/2}(-1+q\,\mathbf1_{p\mid nb})
=-q^{-1/2}
 +q^{1/2}\mathbf1_{p\mid n}
 +q^{1/2}\mathbf1_{p\nmid n,\ p\mid b}.
\]

Allocate the primes of \(a=efg\) to the squarefree theta index, the cube index, and the negative summand, respectively. Write \(Ne\asymp E\), \(Nf\asymp F\), \(Ng\asymp G\), so \(EFG\asymp A\), and set \(Y=\mathcal H^2EG^2/(BF)\).

| Precisely specified component | Proved mean-square upper bound, up to \(D^\epsilon\) |
| --- | --- |
| Every \(E,F,G\) allocation block, at every cusp, on squarefree dual rows | \(\mathcal H E/G+\mathcal H^2 A^2/(BF^3)\) |
| Same allocation on the stated good standard infinity-cusp face | \(\mathcal H E+Y+(EY)^{2/3}\) |
| All divisor primes assigned to the dual cube index | \(\mathcal H+\mathcal H^2/(AB)\) |
| All divisor primes assigned to the squarefree theta index, on that standard face | \(\mathcal H A+\mathcal H^2 A/B+(\mathcal H^2 A^2/B)^{2/3}\) |

All four component bounds average over squarefree dual rows.

At \(A=B=D\) and \(\mathcal H=D\), the last bound is \(D^{2+\epsilon}\), where the factorwise estimate costs \(D^{3+\epsilon}\). Its target-size range grows from \(\mathcal H\le D^{1/2}\) to \(\mathcal H\le D\). This is a genuine saving for the named component.

The negative allocation still has the term \(\mathcal H^2A^2/B\), and other cusp and row contributions remain. These bounds do not cover the initial \(\mathcal H\asymp D^{3-\theta}\) range of the complete fourth moment.

**Generalized-order corollary.** These component bounds remain valid when the outer \(a\)-coefficient is multiplied by any row-independent \(v_D(a)\) with \(|v_D(a)|\ll_\eta D^\eta\) for every \(\eta>0\) on its polynomial support. This includes fixed-order outer allocation divisor weights. To prove it, in Theorem 5.1 freeze \(e,f\) and absorb \(v_D(efg)\) into the arbitrary bounded product-column coefficient; in Theorem 6.2 freeze \(f,g\) and absorb it into the bounded \(e\)-coefficient. Rescale the preliminary epsilon losses. No derivative of \(v_D\) is taken. This corollary concerns the component estimates only: an arbitrary multiplier does not preserve the separate Euler-product identities below.

Proofs: [coupled completion](COUPLED_THETA_COMPLETION.md) and [full scalar calculation](REFLECTION_SCALAR_AUDIT.md).

## 2. Preserve interference between the Ramanujan terms

The negative summand alone has an exact two-variable representation with a reciprocal Hecke \(L\)-function of infinity type \(-3\). A theorem for finite-order twists does not automatically cover that angular character.

The stronger structural reduction holds the original squarefree theta index \(n\) fixed and sums **all** divisor and cube allocations together. With \(r=3s-\tfrac12\) and \(v=w+r-1\), it gives

\[
\mathcal F_{k,n}(w,r)=
\frac{L_S(r,\chi^+)\,L_S(v,\kappa_k)}
     {L_S(w,\chi^-)}\,
\mathcal E_{k,n}(w,v).
\]

Here \(\chi^\pm\) have infinity types \(+3\) and \(-3\); their product \(\kappa_k\) is finite order, with every moving \(k\)-Euler exclusion retained. The Euler remainder is holomorphic in

\[
\Re w>0,\qquad \Re v>\tfrac12,\qquad \Re(w+v)>1,
\]

and, away from these boundaries, is bounded uniformly in \(k\) and the imaginary parts by

\[
|\mathcal E_{k,n}(w,v)|
\ll_{\delta,\epsilon}(Nn)^{\max(0,\,1-\Re w)+\epsilon}.
\]

If the finite character is principal, its \(L(v,\kappa_k)\) factor has a possible pole at \(v=1\). The original scale factor becomes

\[
A^{v-1}\left(\frac{(Nk)^2}{cAB}\right)^t,
\]

with \(c>0\) fixed. This exposes both the polar divisor and the adverse dual-length ratio. The outer, deformed Gauss-coefficient series still needs an analytic estimate; its proved sufficient absolute-convergence region forces \(\Re v>5/2\). No critical contour shift follows from the fixed-\(n\) Euler identity alone.

Proofs: [negative-branch Dirichlet series](NEGATIVE_BRANCH_DIRICHLET_SERIES.md) and [reunited Euler product](REUNITED_RAMANUJAN_EULER_PRODUCT.md). The [primary-source comparison](PRIMARY_SOURCE_MATCH.md) identifies relevant existing theta machinery and the coefficient matching that remains to be established.

## 3. A further controlled part of every fixed higher moment

In the exact shared-prime incidence decomposition, let \(X_i\) be the remaining singleton lengths and put

\[
P=\prod_iX_i,\qquad Q=\frac{P}{\max_iX_i}.
\]

The imported second moment and an optional conductor-uniform pointwise exponent \(b>1/2\) give

\[
\|B_C(\mathbf X)\|_2^2
\ll D^\epsilon HPQ^{2b-1}.
\]

The proof uses the exact forward Euler correction, including the moving exclusion \(C\). At a prime outside \(C\), the coefficient of a nonconstant monomial is one minus its number of active axes; consequently every correction uses at least two axes. That makes the anisotropic absolute coefficient norm converge.

At \(b=1\), the pointwise input is elementary counting. Already in that case, the entire incidence portion with \(Q=D^{o(1)}\) contributes at most \(HD^{k+\epsilon}\), including interference between its configurations.

For example, at \(k=3\), the lengths \((X_1,X_2,X_3)\asymp(D,1,1)\) can have full common gcd one and \(P\asymp D>H^{1/2}\). This portion lies outside both previous controlled ranges and is now bounded. For the balanced fourth moment, the two singleton lengths agree, so this theorem does not add a new range.

Proof: [anisotropic singleton cores](ANISOTROPIC_SINGLETON_CORES.md).

## 4. Two further quantitative consequences

Amplifying the actual polynomial before applying the previous Gram theorem gives the squarefree-row bound

\[
\sum_{\substack{0<Nu\le H\\u\ \mathrm{squarefree}}}|A_u(D)|^4
\ll(DH)^\epsilon
\left(D^4+HD^{8/3}+H^{4/3}D^{20/9}\right).
\]

This improves the previous interpolation bound on that subset in a specified intermediate row range, approximately \(D^{1.2500125}<H<D^{1.583295833}\) at the inherited conditional exponent. The nonsquarefree rows and the desired near-linear range are not covered by this gain. The same note exhibits an abstract amplitude distribution showing why the collected scalar bounds alone cannot supply the missing power saving; it is not an actual Möbius counterexample.

Separately, combining #912's one fixed Mellin test with #913's positive-density rough bases removes the logarithmic shortage of prime replicas. The sufficient exceptional-tail criterion is now \(o(D^{h/6})\), in place of \(o(D^{h/6}/\log D)\). This strengthens the extraction endpoint without changing its power or providing the unproved arithmetic tail estimate.

Proofs: [high-value amplification](HIGH_VALUE_SCALAR_OBSTRUCTION.md) and [log-free replicated spikes](LOG_FREE_REPLICATED_SPIKES.md).

## 5. A concrete bridge to the repository's arithmetic positivity work

For the native SHARP source in #911, suppose \(M(x)=O(x^b)\), with \(1/2<b<1\). Uniformly for sufficiently small \(0\le\delta\le\delta_0\),

\[
H_{1+\delta}(x)
=4^{1+\delta}\frac{1-67^{-(1+\delta/2)}}{\zeta(1+\delta/2)}
 x^{(1+\delta)/2}
 +O(x^{b-1/2}).
\]

The leading coefficient is bounded below by a fixed multiple of \(\delta\). Therefore

\[
H_{1+\delta}(x)>0
\quad\hbox{for }0<\delta\le\delta_0,\quad x\ge C\delta^{-1/(1-b)}.
\]

This is a polynomial positivity horizon under the stated cancellation hypothesis. The previous elementary exponential horizon did not require that hypothesis.

Conversely, a uniform polynomial horizon \(x\ge C\delta^{-A}\), \(A\ge2\), excludes zeta zeros to the right of \(1-1/A\). If \(\Theta_\zeta\) is the supremum of their real parts, the exact infimum of admissible horizon exponents, restricted to \(A\ge2\), is

\[
\mathcal A_*=\frac1{1-\Theta_\zeta}.
\]

The identity concerns an infimum; endpoint attainment and explicit numerical threshold constants are not asserted.

| Zero boundary supplied as input | Consequence for the native positivity horizon |
| --- | --- |
| Inherited conditional \(139999/160000\) | Every \(A>160000/20001\), approximately \(7.99960002\) |
| Desired fourth-moment limit \(17/24\) | Every \(A>24/7\), approximately \(3.42857143\) |
| Desired \(2k\)-moment limit \(1/2+5/(12k)\) | Every \(A>12k/(6k-5)\), tending to \(2\) |

This identifies an exact quantitative target for combining the moment program with the native kernel. It does not independently improve the zero boundary or extend an ordinary-zeta theorem to all sextic twists.

Proof: [polynomial critical horizon](POLYNOMIAL_CRITICAL_HORIZON.md).

## Review, reproducibility and source boundaries

Read the [scoped independent review](INDEPENDENT_CRITICAL_CORE_REVIEW.md), [validation record](VALIDATION.md), [source lock](SOURCE_LOCK.json), and [file manifest](MANIFEST.json). The review identifies authorship and independent review roles separately and binds exact content hashes.

The [local checker](checks/check_local_identities.py) passes 14,224 exact integer/cyclotomic predicates, including split and inert residue fields, the two relevant local Fourier transforms, nonunit masks, and multivariate Euler coefficients. Normal and optimized Python runs agree. These finite checks do not certify an analytic estimate, automorphy, or RH.

The [adjacent source snapshots](adjacent-sources/README.md) preserve twelve exact files from #911 and #912. Earlier packets and the external source import remain unchanged. Source-conditional estimates retain the imported completed theta transformation, its cusp and weight estimates, and the imported inverse second moment as stated inputs.

The next substantive estimate must control the coupled, deformed Gauss series with its angular reciprocal, moving conductor, polar divisor and all row strata. The exact formulas here make that problem more explicit and rule out several unsupported shortcuts; they do not replace the required cancellation.
