# Current statements and proof routes

This is an editorial reading guide to retained mathematics, not a new theorem packet. Statements below keep the hypotheses of the cited results and incorporate their recorded corrections. The proof routes explain existing arguments; they do not certify an unreviewed combination of them. Earlier source reviews remain inherited. A numerical or external-source assumption is stated where it matters.

[Results and significance](../../RESULTS.md) · [approaches](../../PROGRAMMES.md) · [next tasks](../../OPEN_CUTS.md) · [full research index](../RESULTS_INDEX.md).

## Source-qualified extensions in this integration candidate

The earlier statements below remain part of the cumulative account. The following thematic pages add the selected reviewed work without changing the published baseline before this branch receives its own integration review.

| Topic | Current statement, proof route and evidence |
|---|---|
| Whole-function unit-window positivity and the arithmetic graph | [Operators, anchoring and the retained coherent channel](native_sources/OPERATORS.md) |
| Native arithmetic minima, annular criteria and balanced lifts | [Full residuals and their exact remaining estimates](native_sources/RESIDUALS.md) |
| Ordinary causal inputs and the actual intrinsic floor | [Source domains, realization and entropy](native_sources/CAUSAL.md) |
| Critical prime discrepancy and summable local detail | [Complete prime energy and square-grid localization](native_sources/PRIME_ENERGY.md) |
| All-rank tensor/symmetric-power intersections | [Rational spectral classification and its exception](native_sources/STRUCTURES.md) |

The [resident proof library](native_sources/SOURCE_INDEX.md) links every selected packet to its original manuscript. The [evidence guide](native_sources/EVIDENCE.md) distinguishes complete numerical reconstructions from archival programs. These are current formulations of reviewed components, not approval of a new composition or a claim that any open RH-strength upper bound has been proved.

## Conventions

$\mu$ denotes the Möbius function, $\sigma$ the sum-of-divisors function, and $\gamma$ Euler's constant. For a real function, $F_-=\max\{-F,0\}$. A bound called **subpower** means: for every $\epsilon>0$ there are $C_\epsilon$ and a threshold such that the quantity is at most $C_\epsilon X^\epsilon$ thereafter. Constants need not be uniform in $\epsilon$.

The completed function $\xi(s)$ is the **entire continuation** of $s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2$, with $\xi(0)=\xi(1)=1/2$. Write $E(z)=\xi(1/2+z)$ when using horizontal coordinates, and $\Xi(t)=\xi(1/2+it)$ when discussing real zeros. These are different coordinates. Finite logarithmic-derivative evaluations require certified nonzero denominators.

<a id="robin"></a>
## 1. Robin: canonical completeness and a corrected finite envelope

**Retained scope:** the finite barrier and canonical reduction are reviewed results; the global interpretation uses Robin's classical equivalence, not a new proof of that equivalence.

Let $I(n)=\sigma(n)/n$. The exact finite maxima are $I(5040)=403/105$ on $1\le n\le5040$ and $I(5460)=224/65$ on $5041\le n\le5582$, each uniquely. Directed bounds prove

$$e^\gamma\log\log5041>224/65,\qquad e^\gamma\log\log5582<403/105<e^\gamma\log\log5583.$$

Thus there is no Robin violation in $5041\le n\le5582$. For $n=\prod q_i^{a_i}$, sort the exponent multiset as $b_1\ge\cdots\ge b_k\ge1$ and put $\mathcal H(n)=\prod_{i=1}^k p_i^{b_i}$, where $p_i$ are the first $k$ primes. Then $\mathcal H(n)\le n$ and $I(\mathcal H(n))\ge I(n)$. Every hypothetical violation at $n>5040$ maps to a violation at $\mathcal H(n)>5040$.

**Proof route.** Exchanging inverted exponents decreases the integer and increases its abundancy; replacing primes by smaller consecutive primes has the same effect. The finite barrier ensures $n\ge5583$. Were $\mathcal H(n)\le5040$, the first maximum would contradict the strict threshold at 5583. Monotonicity of $\log\log$ finishes the reduction. This proves completeness, not finiteness, of the canonical search domain.

### Bounded-tail envelope with all cap and feasibility hypotheses

Fix a canonical prefix of value $P$, abundancy $I_P$, and last exponent $A\ge1$. Let $q_1<\cdots<q_n$ be its next consecutive primes. Fix an integer bound $B$ and put

$$M=\lfloor B/P\rfloor,\quad R=\prod_iq_i,\quad M_0=\lfloor M/R\rfloor.$$

**Dispose of $R>M$ as an empty subtree first.** Otherwise choose certified nonincreasing caps $A\ge c_1\ge\cdots\ge c_n\ge1$ that dominate every admissible completion exponent $b_i$. The weaker choice $c_i=A$ is valid. Define $n_r=\#\{i:c_i\ge r\}$ for $2\le r\le A$ and

$$Q_\ell=\prod_{i\le\ell}q_i,\qquad G_{r,\ell}=\prod_{i\le\ell}\frac{q_i^{r+1}-1}{q_i(q_i^r-1)}.$$

For integers $a\ge0,d\ge1$, set $W_{r,\ell}=G_{r,\ell}^d/Q_\ell^a$, $V_{A+1}(j)=1$, and

$$V_r(j)=\max_{0\le\ell\le\min(j,n_r)}W_{r,\ell}V_{r+1}(\ell).$$

Put $V=V_2(n)$ for $A\ge2$, and $V=1$ for $A=1$. Every admissible completion satisfies

$$I\!\left(P\prod_iq_i^{b_i}\right)^d\le (I_PI(R))^dM_0^aV.$$

**Proof route.** Encode the completion by nested lengths $\ell_r=\#\{i:b_i\ge r\}$. Its optional cost is $\prod_rQ_{\ell_r}\le M_0$, while its abundancy increment is $\prod_rG_{r,\ell_r}$. Backward maximization bounds the quotient of the $d$th power of the increment by the $a$th power of the cost. All quantities in this envelope are rational. No unsupported definition of $n_r$, empty-budget convention or new large traversal range is being used.

**Proof/evidence:** [resident foundations, sections 1–5](robin/finite-robin-foundations.md); [cap/feasibility correction, section R6](../../reviews/D/REPAIRS.md). **Open:** the unbounded canonical tail.

<a id="sharp"></a>
## 2. SHARP: every real power at least two

Define

$$\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),\qquad T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},$$

$$\mathfrak H^{[m]}(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n)^m.$$

**Current theorem:** $\mathfrak H^{[m]}(x)>0$ for every real $x\ge1$ and real $m\ge2$.

**Proof route.** Expand on the finite active subsets of a prime-label set with one label for each prime and an additional label at 67. For an active removal of a label of prime $q$, the weight ratio is less than $q^{-(m+1)/2}$. The complete label sum is bounded by

$$S_2=\sum_{q\ \mathrm{prime}}q^{-3/2}+67^{-3/2}<1.$$

Double counting gives $kM_k\le S_2M_{k-1}$ for the nonnegative level masses. Hence each even/odd pair has nonnegative difference, and the first has strictly positive difference. **Do not use a strict inequality between two empty levels.** This correction preserves the strict final theorem.

**Proof/evidence:** [exact source statement and Euler proof](https://github.com/GettysburgResearch/riemann/blob/fa081e81044a81e76f48cb9878a659d749e98427/claims/lemmas/L-99613-every-sharp-boundary-power-at-least-two-is-globally-positive.md); [scope correction in the component ledger](../../reviews/D/CLAIMS.tsv); [descent and source manifest](sharp_native/README.md).

**Open:** $m=1$. The distributional identities connecting the quadratic object to the critical detector do not bound its weighted downward variation. At the critical exponent the corresponding prime-harmonic summation is not the subunit summation above.

<a id="mellin"></a>
## 3. A fixed Mellin detector and the arithmetic premise

Use $\mathcal MF(s)=\int_1^\infty F(x)x^{-s-1}\,dx$. Fix the real arithmetic detector $F$ before making any implication. Require local integrability, initial absolute convergence, and a correctly normalized meromorphic continuation whose multiplier does not cancel any right-half-strip reciprocal-zeta pole. In the fixed-row examples this is an exact reciprocal-zeta identity, not equality to a positive surrogate. The continuation must be holomorphic near each positive real $s$; exceptional total-function values must agree with the analytic continuation.

For this source, the still-open arithmetic premise is

$$N_F(Y)=\int_1^YF_-(x)\,\frac{dx}{x}=O_\epsilon(Y^\epsilon)\quad\text{for every }\epsilon>0.$$

**Retained conditional conclusion:** the fixed, noncancelling consumer with this premise excludes zeta zeros with real part greater than $1/2$; the usual zero symmetries then give RH. The statement is an implication, not an unconditional detector estimate.

**Proof route.** On a compact subset of $\Re s>0$, choose $\epsilon$ smaller than its minimum real part. Dyadic summation controls the negative-part Mellin integral and all fixed derivatives. For an eventually nonnegative tail with finite abscissa $c$, an analytic extension through $c$ would let the positive Taylor series sum its Laplace moments at an exponent left of $c$, contradicting the abscissa. Apply this tail Landau theorem after splitting positive and negative parts. An abscissa of minus infinity means an entire transform and is handled separately. Noncancellation then contradicts a reciprocal-zeta pole.

The fixed rows 2 and 3 and the fixed 5:3 scalar have reviewed noncancellation algebra. The analytic input is not supplied by a varying row selected after introducing a hypothetical zero. For genuine poles use nonextendibility of a punctured germ; mere nonanalyticity of an arbitrarily assigned total-function value is weaker.

### Corrected excursion estimate

Let $f(u)=F(e^u)$ be locally absolutely continuous. On $[0,\log Y]$, let $\mathcal I_Y$ contain only negative components whose **two endpoint values are zero and which meet neither outer boundary**. Put

$$L(Y)=\sum_{I\in\mathcal I_Y}|I|,\qquad V(Y)=\sum_{I\in\mathcal I_Y}\int_I|f'(u)|^2du.$$

Let $B_\partial(Y)$ be all negative mass in components meeting either outer boundary, counting a component meeting both once. With finite interior energy, the current bound is

$$N_F(Y)\le\pi^{-1}L(Y)^{3/2}V(Y)^{1/2}+B_\partial(Y).$$

Apply Dirichlet Poincare and Cauchy–Schwarz on each interior component, sum the squared lengths appropriately, and add the boundary integrals without approximation. Since $L(Y)\le\log Y$, a subpower estimate on $V(Y)+B_\partial(Y)$ suffices. **That source-specific estimate is not proved by this inequality.** Nor is subpower logarithmic length a separate difficult premise.

**Proof/evidence:** [fixed consumers](mellin_landau/README.md); [complete analytic proof, M1–M8](../../reviews/C/pass4-math-completion/proofs/MELLIN_ANALYTIC_GAPS.md); [both-boundary correction, R7](../../reviews/D/REPAIRS.md). The proposed Lean analytic implementations have not become proved instances merely by being restated here.

<a id="wavelet"></a>
## 4. Compact wavelets: distinct energies and one source

For the fixed compact kernel $K_0$ supported on $[1,8]$, let $a=X/8$, $d_n=\mu(n)n^{-1/2}K_0(X/n)$, $G(X)=\sum_nd_n$, and $S_X(v)=\sum_{n\ge v}d_n$. Finite summation gives, for $\tau>0$,

$$\sum_{m,n}d_m\overline{d_n}\min(m,n)^{2\tau}
=a^{2\tau}|G(X)|^2+2\tau\int_a^X|S_X(v)|^2v^{2\tau-1}\,dv.$$

In particular the Cauchy–Poisson energy has $a^2|G|^2$ as its boundary term. The older quantity with $|G|^2$ is a **different energy**. The literal older criterion retains a separate suffix-field/Mellin proof; it is not justified by the false equality of the two expressions.

**Proof route.** Expand $\min(m,n)^{2\tau}$ as its value at $a$ plus an integral, then interchange finite sums. For the older criterion, fixed suffix test functions separate the reciprocal-zeta poles. For the corrected spectral-abscissa theorem, the actual half-plane Hardy norm, reciprocal-zeta growth, phase integrability and source uniqueness must be supplied; a finite boundary integral alone is insufficient. With $\Theta$ the supremum of real parts of nontrivial zeta zeros, its abscissa $\Theta+1/2$ is an **infimum**, not an assertion of convergence at the endpoint.

The minimal causal dyadic annihilator $(I-\sqrt2S_2)(I-S_2)^2$, where $S_2h(X)=h(X/2)$, gives ratio-eight compactification. The Abel–Mertens frame and same-$K_1$ largest-prime/Vaughan translation retain their fixed kernels and endpoint conventions. The translation error is integrable in $dX/X$; swapping $K_0$ and $K_1$ is not licensed.

**Proof/evidence:** [wavelet source manifest](wavelet_xd/README.md); [energy and suffix-field proof, R4](../../reviews/D/REPAIRS.md); [Hardy/abscissa completion, R15](../../reviews/D-final/REPAIRS.md). **Open:** the full signed critical estimate after recombining carriers, not a separate unsigned component bound.

<a id="q4"></a>
## 5. Q4 and compatible estimates: what the repairs permit

The exact Fourier/Haar/Jordan and annular decompositions retain their source, measure and endpoint conventions. The terminal annular core is formed using a **disjoint partition including the small-variable sector**; the contribution bounded by $O(H\log^2(2X))$ must be charged to the remainder. A sign-free divisor indicator does not make the remaining product of real kernels positive.

For any finite Dirichlet polynomial $P(t)=\sum_{1\le m\le X}c_mm^{-it}$ with complex coefficients, $X\ge1$ and $T>0$, the repaired mean-value argument yields

$$\int_{-T}^T|P(t)|^2dt\le(2T+14X)\sum_m|c_m|^2.$$

**Proof route.** The nodes $\log m$ are $1/X$-separated. Compare their signed reciprocal-difference form with the continuous Hilbert transform, control the averaging error, and apply the bound to two oppositely modulated coefficient vectors. Taking absolute values of $1/(m-n)$ first loses the cancellation. This analytic $O(X)$ bound is not the open subpower arithmetic estimate.

**Filter scope.** A fixed causal filter preserves the subpower criterion only in its declared endpoint space, with bounded initial data and genuinely subpower forward/inverse coefficient mass. Independently bounding each frozen-order inverse does not bound a varying-row inverse. The latter requires its own coherent prefix control or a bound for the actual varying-row operator.

**Combining bounds.** Regional Schur estimates for a growing partition require constants uniform over all active regions, or a direct subpower bound on the sum of the square-root products of row and column masses. A fixed finite partition is a different scope. A supplied common transfer must remain the same on both sides of a matched-transfer identity. Finite Farkas duality does not construct a feasible native source allocation.

For $Az=b$, $Gz\ge0$, $z\ge0$, the correct obstruction is $A^Tu-G^Tv\ge0$, $v\ge0$, $b^Tu<0$. Rational certificates are guaranteed for rational data, not arbitrary real coefficients. A different primal convention, $Gz\le c$, has a different dual sign; the corrections are not interchangeable.

**Proof/evidence:** [Q4 sources](q4/README.md); [partition and signed mean-value proofs, R17–R19](../../reviews/D-pass3/PROOFS_AND_REPAIRS.md); [regional uniformity, R9](../../reviews/D/REPAIRS.md); [Farkas repairs, R11–R12](../../reviews/D-final/REPAIRS.md); [half-divisor sources](vaughan_half_divisor/README.md). **Open:** the literal signed near-collision/annular estimate and any still-unproved change of measure. SACF is retained as sufficient; the later UOSACF has the stated converse. They are not interchangeable labels.

<a id="xi"></a>
## 6. Xi: distinguish the finite witnesses from low-order safe-axis positivity

### RH-necessary tests at a general height

At zero-free evaluation points define $R_T(x)=\Re(\xi'/\xi)(1/2+x+iT)$ and $J_T(u)=\sqrt u\,R_T(\sqrt u)$ for $x,u>0$. Under RH and the source-qualified canonical-product/resolvent interface,

$$J_T(u)=\sum_\gamma\frac{u}{u+(T-\gamma)^2}.$$

Ordinates are counted with multiplicity. Absolute convergence of the derived series justifies finite secants and minors. For distinct positive nodes,

$$(-1)^{n-1}[u_0,\ldots,u_n]J_T
=\sum_\gamma\frac{(T-\gamma)^2}{\prod_{j=0}^n(u_j+(T-\gamma)^2)}\ge0\quad(n\ge1).$$

A strict directed opposite sign contradicts RH. Off-line pole geometry gives an open finite witness basin if RH fails; it does not produce an actual violating Riemann-data packet.

**Proof route.** Compute the divided difference of $u/(u+a)$ and sum. Cross-Loewner minors follow from Cauchy–Binet and Cauchy determinants. Barycentric localizers retain their exact vector and primitive-error amplification. A matched-pole annihilator needs **at least two distinct admissible nodes**, nonzero denominators and every remaining background-zero contribution; its modeled pair is not the full sign.

[Full finite statements, proof and source interface](xi/derivative-free-pick-loewner.md) · [annihilator correction, R5](../../reviews/D/REPAIRS.md).

### Current conditional entire-source theorem through order three

If $\Lambda(s)=\Lambda_0(s)-1/s-1/(1-s)$ with entire $\Lambda_0$, the correct normalization is

$$\xi_{\rm ent}(s)=\tfrac12+\tfrac12s(s-1)\Lambda_0(s).$$

It agrees with the usual product off $0,1$ and takes value $1/2$ at both. The raw totalized product at these points does not define the intended entire function.

For the conditional source theorem, assume an even real entire $E$ of order less than two with $E(0)\ne0$ has **exactly** the following zeros, with analytic multiplicities: a selected critical pair $\pm i\gamma_0$ of multiplicity $m_0\ge1$, all other distinct critical pairs $\pm i\gamma_j$ with $\gamma_j>0$, and right-upper off-line representatives $a_i+ib_i$ with their symmetry orbits. All recorded multiplicities are positive integers. Allow empty, finite or countable lists of other-critical and off-line locations; require completeness, no duplicate locations and no double use of the selected reserve. For some $H\ge1024$, require

$$0<\gamma_0\le H/2,\quad 0<a_i<1/2,\quad b_i>H,\qquad
\sum_jm_j/\gamma_j^2<\infty,\quad\sum_im_i/b_i^2\le2(\log H+1)/H.$$

With $R(t)=2/(t+\gamma_0^2)$, $c_i=b_i^2-a_i^2$, $B_i=2a_ib_i$ and $q_i(t)=4m_i(t+c_i)/((t+c_i)^2+B_i^2)$, put

$$p(t)=m_0R(t)+\sum_j\frac{2m_j}{t+\gamma_j^2}+\sum_iq_i(t).$$

The current conditional conclusion is that $p(t)=E'(\sqrt t)/(\sqrt t E(\sqrt t))$ for $t>0$ and that

$$K_{ij}=\frac{x_ip(x_i^2)+x_jp(x_j^2)}{x_i+x_j}$$

is PSD for every positive-node packet of size at most three, including repeated evaluation nodes.

**Proof route.** Genus-zero factorization after writing $E(z)=G(z^2)$ and locally uniform differentiated sums identify the entire source. For $d_i=c_i-\gamma_0^2$ and $\kappa_i=B_i^2/d_i^2$, allocate $\epsilon_i=2m_i\kappa_i/(1-\kappa_i)$ of $R$ to each off-line block. The shares are constant in $t$, and their sum is at most $297/512$. The paid blocks have nonnegative $ff''-2(f')^2$; positive-sum closure and $C^2$ convergence give reciprocal concavity of $p$. Direct differentiation gives concavity of $tp$. The exact three-node determinant factors into their two second divided differences with a nonnegative prefactor. A strictly positive two-node pivot completes the PSD argument. Repeated nodes are handled by coefficient-summing congruence, not by an unproved confluent-derivative claim.

For actual xi, the published finite-height information, existence of a low reserve, all-height counting bound, entire growth and complete zero identification remain named source inputs. The earlier safe-domain paper result retains its recorded scope; the expanded all-positive-node statement here remains conditional on this source contract. Neither asserts order four or higher.

**Proof/evidence:** [complete normalization, source and prefix proof](../../reviews/C/pass4-math-completion/proofs/XI_SOURCE_REPAIR.md); [earlier low-order source family](xi_pick/README.md). **Formal boundary:** the old Lean input is empty because of the removable-value defect; its injective Nat-to-off-line enumeration independently forces infinitely many off-line orbits. The repaired paper theorem is not a compiled construction of an inhabited Lean input.

<a id="operators"></a>
## 7. Operators, cardinal capture and heat

### Effective forms in the energy completion

The retained finite-window reduction concerns the **specified full arithmetic kernel**, not an arbitrary positive discretization. On its constrained finite-codimension subspace $V$, the Hermitian form $q$ is positive and the coupling functionals $q(\cdot,e_i)$ of the finite complementary basis are bounded in the $q$ norm. Let $g_i$ be their Riesz vectors in the energy completion and define

$$S_{ij}=q(e_i,e_j)-q(g_i,g_j).$$

Completing the square gives full-window positivity iff $S\succeq0$, and equality of negative indices. The $g_i$ need not lie in the original $L^2$ space; an unrestricted nullity equality is not claimed.

**Proof route.** Prove source-specific energy continuity before invoking Riesz representation, then complete the square in that energy space. The actual coupling uses one integrable kernel derivative, with gamma singularity and prime-power cusps retained. The full-tail constrained coercivity and coupling proofs specify the spaces and normalizations.

For those spaces, exact trial corrections give the full residual-Gram enclosure

$$U-3R\preceq S_L\preceq U.$$

For the specifically defined $L=1$, $X=3$, $K=101$ subspace, the stronger lower bound is $U-(15/8)R$. Here $U$ and $R$ are the source-defined trial and residual matrices, including every cross term—not entrywise error magnitudes. Their definitions and continuum constraints are in the linked full proof. Finite Galerkin effective matrices approach $S_L$ **from above**. Neither their positivity nor sampled positive lower estimates certifies the continuum sign.

[Complete source, space and residual definitions](../../reviews/C/pass4-math-completion/proofs/OPERATOR_AUDIT.md) · [earlier finite operator components](../RESULTS_INDEX.md#inherited-source-results). **Current selected advance:** the [unit-window positive-extension theorem](native_sources/OPERATORS.md) now supplies a source-qualified whole-function sign at length at most one, with its [complete Fourier-tail evidence](native_sources/EVIDENCE.md#unit-window). The [logarithmic-core continuation](native_sources/OPERATORS.md) also gives converging two-sided Schur enclosures for each fixed window, without a length-uniform convergence rate. **Open:** the sign on the required unbounded family of complete windows. Neither the unit-window result nor a positive Galerkin upper section supplies that family. The [strong-residual statement for unbounded operators](native_sources/OPERATORS.md#strong-schur) separately retains its operator-domain hypothesis.

### Other retained operator results and their domains

**Birman–Schwinger:** the threshold kernel correspondence is with eigenvalue 1 in the **point spectrum**. Spectrum alone needs an additional compactness/isolation hypothesis. Keep the closed form domain and coupling hypotheses in the source theorem. [Current correction and maps, R2](../../reviews/D/REPAIRS.md).

**Cardinal capture:** the multiplicity-aware construction uses the complete zero background, smooth compact approximation and the specified Gaussian-confined range. The packet/support may adapt to the target and required accuracy. This supports that capture theorem, not every predetermined fixed-grid hierarchy and not the arithmetic lower floor. [Full reconstruction, R16](../../reviews/D-pass3/PROOFS_AND_REPAIRS.md).

**High carriers and safe sources:** the inherited unnormalized Fourier convention requires the leading Fredholm coefficient $2\pi\mu(T)$ unless the entire form is rescaled; here $\mu(T)=[\Re\psi(1/4+iT/2)-\log\pi]/(2\pi)$ is the gamma density, not the Möbius function, and $\psi=\Gamma'/\Gamma$. Fixed-degree high-carrier positivity remains a blindness result, not an RH test. For a finite positive jump measure and a measurable unitary family $D_t$, define $Lf=\int(D_tf-f)\,d\nu(t)$; the correct identity is $-\Re\langle f,Lf\rangle=\frac12\int\|f-D_tf\|^2d\nu(t)$. Positive source atoms can nevertheless give negative elementary Wick diagonals; the signed $D^*D-U^*U-V^*V$ decomposition must be retained. [Normalization/dissipation proofs](../../reviews/D-final/REPAIRS.md) · [safe-source proof and negative prime atom](../../reviews/D-pass4/PROOFS_AND_REPAIRS.md).

**Heat and Brownian results:** retain the stated broad-kernel, fixed-resolution exterior and large-center First-Hermite positivity regions with their epsilon dependence and complete explicit-formula inputs. The remaining First-Hermite criterion is on the whole complementary domain, including bounded centers with arbitrarily large heat parameter. Fixed-compact Brownian Taylor/remainder and simple-root displacement results do not imply growing-height positivity or nonsimple-root formulas. [Heat source statements](heat_hermite/README.md) · [full-domain correction, R10](../../reviews/D/REPAIRS.md) · [fixed-compact reconstruction, R27](../../reviews/D-pass4/PROOFS_AND_REPAIRS.md).

<a id="p61"></a>
## 8. Fixed-$P_{61}$ bias with replacement evidence

Let $P$ be the product of primes through 61 and define

$$q(n)=6-6\mathbf1_{n=1}+9\mathbf1_{n=2}-3\mathbf1_{n=4},\quad
H_x(n)=\max\{0,\min(\log4,\log(x/n))\},$$

$$A(x)=\sum_nq(n)H_x(n)/\sqrt n,\quad
F(x)=\sum_{d\mid P}\mu(d)A(x/d)/\sqrt d,\quad M(x)=\sum_{d\mid P}A(x/d)/\sqrt d.$$

**Current theorem:** $0\le F\le M$ for $1\le x<67$ and $M/42\le F\le M/8$ for every real $x\ge67$. At $x\ge67$, these quantities are strictly positive. The $1/40$ lower factor is not retained.

**Proof route and assurance.** Exact divisor coefficients give finite prefix formulas. Between integer activation/saturation knots, the observations are affine in $\log x$, so endpoint bounds cover the whole finite region. A source-specific ramp remainder gives $A(y)=12\sqrt y+C_0+E(y)$ with the required uniform error bound. Compact error is controlled across activations by a Lipschitz estimate. On each divisor-activation slab the tail lower bound is affine in $\sqrt x$; both endpoints and the final unbounded slab are checked.

The retained replacement certificate uses directed MPFR primitives followed by integer interval operations, together with the named analytic ramp theorem. Its primitive/library/runtime contract is part of the evidence. The old printed singleton for $C_0$ does not enclose the true constant and is not accepted evidence, even though the repaired theorem survives.

[Complete statement, analytic dependencies and replacement producer, R25](../../reviews/D-pass4/PROOFS_AND_REPAIRS.md) · [evidence entry points](../../COMPUTATIONS.md). **Open:** uniform growing-$P$ control, the rough completion and the critical dynamic Bellman block. None follows merely from an all-real theorem for this fixed $P$.

<a id="causal"></a>
## 9. Causal Euler/Dickman correction: the line-one scope

The retained component concerns the source and correction defined in the [horizon-faithful completion proof](https://github.com/GettysburgResearch/riemann/blob/cdf2f15965decbd35afbbd09a16c89cb3e215737/standalone/2026-09-05-three-route-assault/pass7-dickman-completion/PROOF.md). With $L=\log X$, its finite Euler product is corrected by

$$C_X(s)=e^\gamma(s-1)L\exp[-\operatorname{Ein}((s-1)L)],$$

where $\operatorname{Ein}(z)=\int_0^z(1-e^{-w})\,dw/w$ is entire. The causal realization is $I-k_{X,a}*$ with $k_{X,a}(x)=L^{-1}e^{(1-a)x}(-\rho'(x/L))$, supported on $x\ge L$, and $\rho$ the classical Dickman function. It leaves the source's exact initial horizon unchanged.

**Retained result:** under the proof's quantitative classical PNT/Mertens inputs, the complete corrected logarithmic-source norm satisfies

$$\|\check F_{X,1}-F_1\|_2\ll\exp(-c\sqrt{\log X})$$

for some positive $c$, with all frequencies included. The source $F_a$, finite-product source $F_{X,a}$, removed-prime convention and norm are those of the linked proof; no alternate cutoff is substituted. Constants are not numerically certified.

**Proof route:** exact signed regrouping, classical Dickman/Buchstab transforms, the horizon-preserving convolution and the source's full-frequency estimates. The $a=1$ correction is bounded by two but is not a contraction. The stronger corrected-product half-plane problem remains open. This page does not promote its proposed conclusion-facing adapter, other branch layers, or a bound for separately estimated factors below one.

[Component review and analytic boundaries](../../reviews/B/REPORT.md) · [next problem](../../OPEN_CUTS.md#causal).

<a id="seven-point"></a>
## 10. Seven-point continuum pressure, not a scalar-only zeta theorem

For

$$K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2t)\cos(2\pi xt)\,dt,\quad K(0)=\sqrt2\sin(1/\sqrt2),\quad w(x)=(K(x)/K(0))^2,$$

the retained certificate establishes, for **every** $g_1,\ldots,g_6\ge0$,

$$\frac1{3000}\sum_{i=1}^6g_i+
\sum_{s=1}^6\frac2{7-s}\sum_{i=1}^{7-s}w(g_i+\cdots+g_{i+s-1})\ge\frac{19}{5000}.$$

**Proof route:** the linear term handles $\sum g_i\ge57/5$. A complete closed-box cover handles the rest by interval kernel bounds or certified Hessian/tangent bounds. Every remaining box must be covered; sampled positivity is not used as continuum proof. The arithmetic contract combines outward dyadic primitives with explicitly widened binary64 aggregation, not an assertion of exclusively rational execution.

The later 269/280-block deductions require their separate trace normalization, bounded-separation, mean-square and tail inputs. The corrected 269 scalar lies between $0.673008527927779$ and $0.673008527927780$. Its scalar correctness and the continuum certificate do not alone establish a new zeta proportion. The invalid original wrapper remains superseded evidence, not repaired by association.

[Complete inequality, cover argument and arithmetic contract](../../reviews/A/supplement/REPORT.md#S01) · [scalar-wrapper audit and correction](../../reviews/C/pass3/RECORD_ARITHMETIC.md) · [evidence guide](../../COMPUTATIONS.md).

<a id="families"></a>
## 11. Families and generalized structures: exact components, qualified transfers

**Literal Euler restoration.** For a prime $\ell$, set $b(n)=\mu(n)\mathbf1_{\ell\nmid n}$. The coefficient identity

$$b(n)-\mathbf1_{\ell\mid n}b(n/\ell)=\mu(n)$$

follows by the three $\ell$-valuation cases. It restores the principal coefficient source at the **linear** level. It cannot be inserted into separately squared pieces. Nonvanishing of the finite Euler factors does not establish nonvanishing of the complete Mellin numerator; the compact mother multiplier still needs its source theorem.

**Witt identity.** With

$$\gamma_m=\frac1m\sum_{d\mid m}\mu(d)2^{-m/d},$$

the identity $1-x/2=\prod_{m\ge1}(1-x^m)^{\gamma_m}$ holds as a formal power series, proved by logarithms and divisor inversion. Each coefficient uses finitely many factors. The reviewed function-field coefficient bound uses additional normal convergence and Weil-root input at **fixed field and conductor**, separating the possible principal quadratic resonance. It is not uniform over arbitrary stopped shells or growing conductors.

**Filtered-complex convention.** In the reviewed finite perturbation setting, retain the contraction and side conditions of the source, $dh+hd=1-ip$, and nilpotence of the relevant filtration-raising perturbation. The transferred correction is $p\delta(1+h\delta)^{-1}i$. The inverse is the corresponding finite geometric series. Higher-page differentials also involve lower-component zigzags; they are not automatically the literal higher components alone. The degree-six Euler relation and lower-bound modules retain the exact Chow-table and nonformality premises; they are not full computed characters.

**Recurrence and source-quotient scope.** Generic numerator-degree/alternant statements retain their genericity and nonvanishing assumptions. The torsion-entry calculation is not universal persistence across boundary exceptions. Source quotients and selected-minor identities do not automatically supply a common uniform inverse or the relative precision of an unbounded native Poincare ladder. Exact local-factor identities do not identify motives or create a number-field Euler product.

**Proof routes and evidence:** [family identities, finite measures, recurrence/cofactor proofs and corrected transfer arguments](../../reviews/B/REPORT.md); [component-by-component conditions and omissions](../../reviews/B/CLAIMS.tsv). These are retained exact or conditional components, not acceptance of every atlas builder, Chow witness, graph census or numerical Epstein contour. [Family tasks](../../OPEN_CUTS.md#family-transfer) identify the missing arithmetic and evidence work.

## Continue by topic

The [extended index](../RESULTS_INDEX.md) also preserves the carry-hinge, four-band, native allocation, earlier terminal-prime/screw and source-qualified finite operator results. Their inclusion is inherited at the listed scope, not evidence that they were all re-proved in the latest audit. [Useful failed approaches](../../REFUTATIONS.md) explain why several tempting extensions are invalid. Exact source freezes, review dispositions and execution histories live in [integration/audit records](../../integration/README.md).
