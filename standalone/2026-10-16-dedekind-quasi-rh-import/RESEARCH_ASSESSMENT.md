# Assessment: what to import, what it could unlock, and what still needs proof

**Status:** external result at its reported scope; source-based analysis and proposed research programme. The new elementary normalization is proved separately in [RENORMALIZED_CERTIFICATE.md](RENORMALIZED_CERTIFICATE.md). Its required signed estimate remains open. This report does not promote an external claim or a research draft into the repository's integrated record.

This is based on the versioned landing metadata and the pinned author-maintained Lean source, not on a successfully downloaded manuscript. [SOURCE_MAP.md](SOURCE_MAP.md) states the exact reading and version limits.

## 1. What the work says and why it matters

The reported theorem is

\[
 \zeta_K(s)\ne0\quad\text{for every number field }K,
 \quad\Re s>31/32,\quad s\ne1.
\]

The associated corollary covers every finite-order Hecke character over every number field, including s=1 for nonprincipal characters. In the formal statement the continuation is tied to Mathlib's arithmetic Dedekind zeta function on Re(s)>1; the Hecke function is tied to its actual ideal Dirichlet series. The exception at one is a pole convention, not a discarded potential zero. See the copied [entrypoints](upstream/DedekindZetaZeroFree/Main.lean) and [Hecke corollary](upstream/DedekindZetaZeroFree/HeckeCorollary.lean).

For orientation, Dedekind zeta replaces positive integers by nonzero integral ideals:

\[
 \zeta_K(s)=\sum_{\mathfrak a\ne0}(N\mathfrak a)^{-s}
 \quad(\Re s>1).
\]

At K=Q it is the ordinary Riemann zeta function. A fixed zero-free vertical half-plane is qualitatively stronger than a boundary that drifts toward one with height or conductor. Nevertheless 31/32=0.96875 is still far from the critical line 1/2. It is numerically weaker than 7/8 or 11/12 **in the settings where those earlier imported statements apply**. The benefit is not that a worse decimal improves an existing special-case result. It is a common statement over arbitrary fields and finite-order Hecke characters, together with reusable formal arithmetic and automorphic machinery.

This distinction is important for our dependency ledger. A special-field 7/8 estimate with additional premises and a general-field 31/32 theorem are different objects. Preserve the stronger bound wherever its exact source supports it; use the general theorem where field or character coverage was missing. Do not silently turn the finite-order corollary into an angular Hecke bound.

## 2. The visible mechanism

The landing record explicitly follows the primitive-roots strategy and identifies the Kazhdan--Patterson metaplectic development as the difficult extension to general number fields. Its references include the earlier OpenAI quasi-Riemann manuscripts. The formal source makes the following architecture visible.

**A field-general arithmetic environment.** The theorem lifts K to K(zeta_12), a totally complex abelian extension containing the required roots of unity. S-arithmetic data retain prime ideals, excluded places, generators after class-group treatment, local phases, and archimedean shapes. This avoids pretending that every number field behaves like the class-number-one Eisenstein lattice. The final [Dedekind entrypoint](upstream/DedekindZetaZeroFree/Nonvanishing/Mellin/Quantitative/DedekindZetaNonvanishing.lean) descends the same zero-free half-plane back to K.

**An actual theta/period source.** The inspected `RankOneExpansion` entrypoint constructs its certified source through trace/Haar transport, smooth Laurent germs, detected periods, exterior coefficients, residue profiles, a joint absolute-rearrangement step, and signed unfolding. These are calls into a large formal development, not independently reproved facts in this report. Their importance for us is the existence of a source with the exact normalizations needed by the analytic comparison.

**A reflected second moment.** For the selected `forwardB` coefficients, compact row-shape support, and norm height at most C Z^m, the visible `GeneralSupportMoment` theorem gives

\[
 \sum_{r\in\mathcal R}|B_r(Z)|^2
 \ll Z^{2m-1+\epsilon},\qquad m>1.
\]

Here **m is a row-height exponent, not a moment order**. This is a second moment of a specified transformed family. It is not the desired native 2k-th moment for arbitrary k, not an arbitrary-coefficient large sieve, and not a theorem over an uncontrolled unit/shape range.

**A nonvanishing Mellin certificate.** The source constructs a flat-at-zero function g and its Mellin transform T with

\[
 L^S(s)T(s)=e^{(s-5/6)^2}H(s).
\]

The identity is first proved on Re(s)=2 with converse Mellin inversion. A growth estimate makes T holomorphic farther left. If the numerator is holomorphic and nonzero there, a target zero is impossible. This is the productive conceptual point: the proof turns a bound for an actual arithmetic/automorphic probe into a contradiction at a putative zero. It does not depend on an unproved positivity assertion for all our native tuples.

## 3. Exact numerical bookkeeping: two errors and a numerator gate

At the pinned parameters, the copied [Scales.lean](upstream/DedekindZetaZeroFree/Moments/Probes/Poisson/Scales.lean) has

\[
 x=67/100,\quad y=151/400,\quad m=x+y=419/400.
\]

The row second moment has exponent 2m-1=219/200. The additive coefficient square energy contributes Z^(-y), and Cauchy gives the reflected exponent

\[
 r=\frac{2m-1-y}{2}=287/800.
\]

The copied [Growth.lean](upstream/DedekindZetaZeroFree/Nonvanishing/Mellin/Quantitative/Growth.lean) combines

\[
 |I(Z)|\ll Z^{287/800+\epsilon},\qquad
 |I(Z)-c_0 f(Z)|\ll Z^{717/2000},\qquad c_0\ne0.
\]

Since g(Z)=Z^(61/100)f(Z),

\[
 \beta=61/100+\max(287/800,717/2000)=31/32.
\]

**Exact consequence for this fixed calculation:** replacing only the reflected exponent by a smaller r' gives the envelope

\[
 61/100+\max(r',717/2000).
\]

Its best possible value, leaving the comparison estimate unchanged, is **1937/2000**, a gain of just **1/4000**. This is a statement about the displayed upper-bound calculation, not a lower bound for the true arithmetic object or a proof that other parameters cannot do better. The all-scale parameter optimization and all comparison contours were not reconstructed here.

With normalization 61/100 held fixed, reaching 1/2 by separately bounding those two terms would require both exponents at most -11/100, up to arbitrary positive losses. Alternatively, one must redesign the scales or exploit cancellation **between** I and its comparison residual before taking absolute values.

There is also a separate source gate: the inspected unmodified H product is proved holomorphic and nonzero for Re(s)>2/3, by a majorant containing q^(3-6 Re(s)). Even hypothetical perfect growth estimates do not authorize reusing that product below its established domain. The normalization below addresses this numerator issue explicitly, without claiming to solve the growth problem.

## 4. A concrete new deduction: a critical-half-plane numerator and its exact cost

The actual local correction is

\[
 C_p(s)=\frac{(1-r^2)(1-(1-r)A-rB)}{(1-B)(1-A)},
 \quad r=q^{-1},\ A=a_pq^{-s},\ B=b_pq^{3-6s}.
\]

Do not estimate its bare sixth-power Euler denominator separately. Multiply it out first:

\[
 \widetilde C_p=(1-B)C_p
 =(1-r^2)\left(1+\frac{r(A-B)}{1-A}\right).
\]

[The normalization note](RENORMALIZED_CERTIFICATE.md) proves that the reunited product is holomorphic and nonzero on **Re(s)>1/2**, uniformly bounded above and away from zero on each smaller half-plane with bounds exp(plus or minus C_delta [F:Q]). Its local error is now q^(-2)+q^(-1-sigma)+q^(2-6sigma). The extra q^(-1) is the actual reason the convergence threshold moves; saying merely that an Euler series starts in high degree would miss it.

The corresponding operation on the source is not free. It is the explicit signed sixth-power dilation

\[
 \widetilde g(Z)=\sum_{(\mathfrak d,S)=1}
 \mu_F(\mathfrak d)b(\mathfrak d)(N\mathfrak d)^3
 g\!\left(Z/(N\mathfrak d)^6\right).
\]

The source's known growth and flatness make this well-defined and preserve its available 31/32 exponent. The new identity has a nonzero numerator throughout the desired open half-plane. Therefore the **precise open target**

\[
 \widetilde g(Z)\ll_\epsilon Z^{1/2+\epsilon}
\]

would yield full zero exclusion for the target, followed by the same descent. That implication is proved in the companion note, conditional on the imported actual-source inputs.

The absolute-value cost sum_d (Nd)^(3-6alpha) converges only for alpha>2/3. Thus the operation exposes, rather than pays, the required signed cancellation. This is neither a hidden use of the desired RH bound nor a claimed improvement of 31/32. It is a source-faithful target with the numerator obstacle removed. The old cube-completion/cube-inverse work makes this particularly natural to test in our project.

## 5. Best combinations with our existing work

### First priority: a signed period, not another unrestricted positive moment

Use the renormalized probe above as the candidate analytic consumer. The existing [#946](https://github.com/GettysburgResearch/riemann/pull/946) structure is

\[
 M_4=G+I_2-D_2,\qquad G\ll HD^{2+\epsilon},\quad D_2\ge0.
\]

The missing inequality is I_2<=D_2+O(HD^(2+epsilon)). Its signed injection preserves the actual prime-removed cofactor; its compensation must not be thrown away. The new source's signed-unfolding and residue-profile machinery is a plausible way to realize such a joint functional as an automorphic period.

**Required adapter, not assumed:** construct a polarized source for the actual U,V pair, retain the same excluded primes and row measure, and identify its signed period with the wanted combination, including the normalization. The source's `forwardB` second-moment theorem does not automatically apply to U cubed times conjugate V, to a high tensor power, or to the six-dilation sum. Prove the coefficient-family membership and common-height shortened-scale estimates before using its bound. A formal identity with no better estimate would be a useful diagnostic, not a completed moment argument.

The most informative first test is at order four with a fixed smooth test and the trivial twist. Check the local identities at split, conjugate, and inert primes, including zeros, before attempting the growing family. Then establish a **net power saving for the complete signed functional**, not a favorable estimate for one removed face.

### Second priority: combine with conductor-window localization before taking norms

[#944](https://github.com/GettysburgResearch/riemann/pull/944) retains active conductor C and neutral radical R, with exact mask sum

\[
 K_{C,R}(H)=\sum_{d\mid R}\mu(d)\chi_C(d)S_{\chi_C}(H/Nd).
\]

The surviving neutral-divisor window is already localized; [#942](https://github.com/GettysburgResearch/riemann/pull/942) kills low radicals under its particular band-limited Schwartz weight; [#940](https://github.com/GettysburgResearch/riemann/pull/940) bounds the smooth-singleton sector.

A serious composition would transfer the source's actual period coefficients into the **remaining** window and estimate the signed sum jointly. This may reduce the analytic object enough to use the field-general source machinery without first proving the whole native hierarchy. But C>H and R=1 still leave d=1: the completely separated singleton core survives. Any claimed result should display its cost on that case. Band-limited identities include the entire Schwartz tail and cannot be transplanted to a selected sharp-row sum by positivity.

### Third priority: use field generality to repair coverage, not to weaken good exponents

The new finite-order theorem can supply a common safe analytic region for fields and ray-character families not covered by the earlier special construction. For example, after the precisely stated small-prime gate in the earlier determinant work, a fixed finite-ray determinant source is a finite product of inverse Hecke functions times a convergent correction. Accepting those two named inputs gives a holomorphic domain above 31/32 for that completed source. This elementary closure statement does not improve the critical line or provide a moving-conductor estimate.

The missing quantitative interface is explicit: bounds for reciprocals, derivatives, and Sobolev/profile constants as field degree, discriminant, conductor, and archimedean type vary. An identical zero-free exponent for all fields is not itself a uniform bound for these constants. In particular the infinite-order angular +/-3 factors in some earlier packets are not covered simply by the word “Hecke.”

[#947](https://github.com/GettysburgResearch/riemann/pull/947) is a further warning: its large finite cross-degree cancellation came from a few coherent physical rows. A rank-one theta construction and a rank-one physical row Gram are **different objects**. Their names do not supply an identification. The coherent native value remains in the problem even after its large degree trace is understood.

## 6. More radical route: a cofinal family of nonvanishing period certificates

The generalized native moment hierarchy is one sufficient route, not a logical requirement imposed by RH. The imported proof suggests a different programme: for each fixed small eta>0, construct an actual signed period with

\[
 L^S(s)T_\eta(s)=N_\eta(s),
\]

where T_eta is holomorphic and N_eta is nonzero on Re(s)>1/2+eta. A single zero to the right of 1/2 would contradict one of these identities. The new normalized numerator gives a candidate starting point; it does not construct the missing holomorphic T_eta.

A variable-cover or higher-rank metaplectic construction could be worthwhile if it changes the scale losses or the signed period enough to produce such certificates. The concrete success criterion is an improving half-plane, together with a nonzero source and numerator. Merely making the representation larger, tensoring a second moment, or passing to a field containing more roots of unity does not meet it. Each cover/order may be fixed before the asymptotic scale grows; any proposed cofinal argument still needs every required analytic bound at that order.

This is high-variance research, not an asserted extension of the paper. Its attraction is that the formal source provides a detailed arithmetic-to-Mellin pipeline in which one can replace a quantified estimate without losing track of the target zeta function.

## 7. Three shortcuts that do not give a full proof

**Repeated base change.** In an abelian extension E/K, the usual factorization expresses zeta_E as zeta_K times nonprincipal Hecke factors, holomorphic away from the principal pole. A zero of zeta_K persists at the **same s**. Descent transfers a beta half-plane unchanged; repeating a beta=31/32 theorem does not make beta approach 1/2. Field variation helps only if an auxiliary construction genuinely improves its analytic bound or supplies additional cancellation.

**Pointwise bound plus the old second moment.** Even granting the required uniform pointwise estimate |A_u(D)|<=D^(beta+epsilon) and M2<=HD^(1+epsilon), the immediate higher-moment bound is

\[
 M_{2k}\ll H D^{1+2\beta(k-1)+\epsilon}
 =HD^{k+(k-1)(2\beta-1)+\epsilon}.
\]

At beta=31/32, the excess is (15/16)(k-1), linear in k. The inherited extraction consequently approaches beta, not 1/2, when the row cost is sublinear. The new general theorem alone does not establish even the uniform pointwise premise used in this calculation.

**Invertible Euler compensation or uncontrolled randomization.** [#945](https://github.com/GettysburgResearch/riemann/pull/945) preserves the unknown native constant mode; its invertible correction cannot erase a genuine target pole. [#941](https://github.com/GettysburgResearch/riemann/pull/941) rules out the indicated uniform prime-freezing continuation. Our new sixth-dilation normalization respects both warnings: its better numerator has an explicit unsolved signed-transform estimate, with no free critical absolute norm.

## 8. Recommended next pass and verdict

First reproduce the pinned formal build and compare the true arithmetic target and transitive axiom footprint. Separately obtain both manuscript versions and reconcile their exact statements with the pinned code. Neither task is claimed completed here.

For mathematics, work on the normalized six-dilation probe rather than another generic estimate for already-controlled sectors. Start by expressing the full signed operation inside the source's theta/Poisson construction, retaining the comparison residual before absolute values. Attempt its order-four polarized interface with #946 and #944. Freeze the exact input identity and record the resulting exponent on the separated singleton core. If the result is merely the existing bound or reintroduces the 2/3 absolute-sum cost, reject that adapter as a power-saving mechanism and move to the cofinal period construction.

**Assessment:** important infrastructure and genuine new scope if the reported theorem and formal development survive verification; not a numerical shortcut from our existing Riemann bounds to RH. The tangible addition in this import is a concrete critical-half-plane numerator normalization and an exact signed sum whose estimate would complete the corresponding zero-exclusion route. That estimate is still open.
