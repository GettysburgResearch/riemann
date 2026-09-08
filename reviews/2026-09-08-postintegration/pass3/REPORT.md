# Post-integration scientific review — pass three

**Disposition: review recommendations, not integration or blanket acceptance. RH remains unproved.**

This pass works from the published pass-one and pass-two records on PR #827, at review checkpoint `13ac26caae546c8a6481a85b2f61ecc524dbbb27`. Main was observed at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. All changes in this packet are additions to the review branch. A later integration must begin from then-current main and preserve its cumulative scientific account and contributor-facing improvements; merging this review branch wholesale would be the wrong operation.

The unit of coverage is a **source-qualified component**, not a PR title or the latest paragraph of a long-running branch. [FILES.tsv](FILES.tsv) binds this pass's inspected manuscripts to full commit and blob identities. [COVERAGE.tsv](COVERAGE.tsv) gives the cumulative packet inventory; [SOURCE_HEADS.json](SOURCE_HEADS.json) gives the watched refs. Recommendations apply to those files at those commits, not automatically to their siblings, later revisions, imported dependencies, or author checkers.

## 1. Outcome and remaining review

All **24 packets left at main-manuscript depth after the published second pass**, including its three late arrivals, received substantive mathematical reading in this pass. There are now **45 of 45 inventoried packets with main-argument coverage across the three passes**. This is a milestone in manuscript coverage, **not 45 accepted packages**. The inventory comprises fourteen research PRs and one branch-only deposit. The older divisor-cusp packet is a separately qualified preintegration dependency, not a new forty-sixth packet.

The especially useful advances are:

* sharp logarithmic-logarithmic **anchoring costs**, despite constant centered gaps, with exact root resolvents;
* a source-specific identification of the native Möbius energy with the **coherent function channel** untouched by the divisor gradient;
* a sharp **order `Y/log Y` loss** in coefficient-uniform graph-to-physical norm transfer, surviving the actual prefix and three normalization constraints;
* a classical-cancellation-based **`o(Y)` full physical residual bound**, without incorrectly claiming a fixed power saving;
* source-exact compact-annular and sparse-sign reductions, complete Green/harmonic transfers, and explicit limits on detail-only optimization;
* independent finite reconstruction of four two-jet minima, three one-jet minima, the full-source `8 -> 16` obstruction, the actual prime-box capacities, and the complete norm-transfer profile constant.

I did not find a fatal defect in the principal arguments inspected at the scopes discussed below. There are small statement/citation repairs, substantial nontrivial open estimates, and still-unreviewed supporting files and package contracts. One more focused pass should finish those source/code/auxiliary obligations and disposition any new deltas. It should not reread the same principal manuscripts indiscriminately. [RESUME.md](RESUME.md) specifies that queue.

### Which pass-two record controls

The **published** pass-two report and coverage table control. They record source-stability as reviewed, entropy feedback as still unread, and the three rational-capture minima as not replayed. An earlier locally prepared delivery differs on those points. This pass freshly reads entropy feedback and freshly reconstructs those minima; it does not retroactively attribute either execution to the published second pass.

## 2. The new graph synthesis: distinguish three different problems

### 2.1 Grounding capacity, #828 — GCP

Source: `528b33ac8d57b5a046260ee45d585cd3fe720f4c`, `standalone/2026-09-08-astra-grounding-capacity/PROOF.md`.

The setting is either the squarefree divisors of a finite primorial, or all integers supported on a **fixed finite prime alphabet with unbounded exponent depths**. The normalized harmonic measure is `1/(Zn)`; the full prime-power energy is retained. These are product reservoirs, not the cutoff `n <= N`.

The proof correctly separates the centered spectral gap from two anchoring constants. Set

\[
 b_p=1/p,\quad a_p=(1+1/p)\log p
\]

in the squarefree case, and

\[
 b_p=1/(p-1),\quad a_p=p\log p/(p-1)
\]

in the geometric case. For nonempty prime subsets `D`, put `b_D=product b_p` and `lambda_D=sum a_p`. The root-contrast Green norm and optimal anchored constant have the exact representations

\[
 G_P=\sum_{D\ne\varnothing}\frac{b_D}{\lambda_D},\qquad
 \sum_{D\ne\varnothing}\frac{b_D}{C_P\lambda_D-1}=1,
\]

with the root taken above the reciprocal centered gap. The positive root weights and strict monotonicity give existence and uniqueness. In the countable geometric reservoir, root evaluation sees only the first nonconstant eigenmode in each prime coordinate. Higher exponent modes are not numerically truncated; their root coefficients vanish. Coincident eigenvalues retain their subset multiplicities.

The centered gaps are absolute constants when prime 2 is present. Nevertheless,

\[
 G_{\rm sf}(P)=\zeta(2)^{-1}\log\log P+O(1),\qquad
 G_{\rm geo}(P)=\log\log P+O(1),\qquad
 C_P-G_P=O(1/\log\log P).
\]

The manuscript's argument uses the positive real Euler product, elementary prime bounds, and an integral of the return product. It isolates the pole at **real `s=1`**, not nontrivial zero locations. The second inverse moment stays bounded; the secular equation then yields the small `C-G` difference. No PNT or RH estimate is smuggled into the centered-to-anchored transition.

For the **specified** coupling `ell(f)=f(1)-mean(f)`, completion of squares gives

\[
 c|a|^2+2\Re(\overline a\tau\ell(f))+\mathcal E(f)\ge0
 \quad\Longleftrightarrow\quad c\ge|\tau|^2G_P.
\]

This is a usable exact Schur cost and a negative witness when it is unpaid. It does **not** prove that the missing full Weil/Xi coupling has this particular root form.

**Recommendation:** retain the spectral/anchoring statements at these exact reservoir and domain scopes, including the geometric extension and specified-coupling criterion. Do not transfer their product spectra to arbitrary divisor downsets or to integer cutoffs.

**New finite evidence:** the reviewer code sums all 63 visible nonempty subsets for each reservoir at `P=13`, using independently written directed logarithms and monotone secular bracketing. It reproduces the advertised capacity intervals. This is not a replay of the authors' package or a proof of the asymptotic by finite extrapolation.

### 2.2 Coherent-channel synthesis, #829 — CCS

Source: `f782788933dc21a0fe6a844950f5ca532eba7d86`, both `PROOF.md` and `COHERENT_SOURCE.md` in `standalone/2026-09-08-astra-coherent-channel-synthesis/`.

The squarefree Green sum, secular equation, constant centered gap, sharp anchoring asymptotic and small difference overlap with GCP. This should become **one shared mathematical extraction with both sources credited**, not two independent discoveries or two independent referee votes. CCS does not supply GCP's geometric extension merely by having the same squarefree formula.

CCS adds a rooted survival statement. For the finite chain killed at the root, the least Dirichlet eigenvalue is `1/A_P`. Its ground-state weight is `1/(1+V_P)` with the full squared-norm normalization. Therefore

\[
 (1+V_P)^{-1}e^{-t/A_P}\le S_P(t)\le e^{-t/A_P},
\]

and `V_P=O((log log P)^-2)`. The stationary root-hitting law consequently tends uniformly to the exponential law after scaling by `A_P`. Root mass is already killed at time zero. A root Poisson solution gives exact mean lifetime `G_P`. This is a statement about a specified finite arithmetic graph, **not a probabilistic model for the locations of primes**. I reconstructed the root Poisson and mean identity in a separate exact rational-rate product model.

More importantly for the RH programme, the second manuscript takes the literal Hilbert-valued vertices

\[
 v_n=\mu(n)S_{\log n}\phi,\qquad \phi(t)=e^{-t/2},
\]

and identifies

\[
 J_N=\left\|\sum_{n\le N}\frac{\mu(n)}{\sqrt n}S_{\log n}\phi\right\|^2
 =\sum_{k<N}\frac{M(k)^2}{k(k+1)}+\frac{M(N)^2}{N}.
\]

The final term is the **complete stopped-source future**, not an optional correction. Projection on the original harmonic coherent channel has squared norm `J_N/H_N`; its complement has squared norm `sum mu(n)^2-J_N/H_N`. The complete graph energy of the same field is

\[
 \mathcal E_N(v)=\zeta(2)^{-1}N\log N+O(N),
\]

with higher-power outgoing edges included. Thus a complement gap does not give the desired upper bound on `J_N`: the unknown lies in exactly the channel the gradient kills, and the known edge energy has the wrong size for a naive application anyway.

The source convolution and zero-forced lower-growth argument retain the original metric and full horizon. A subpower upper bound on `J_N` along an unbounded sequence would contradict every fixed hypothetical off-line zero. But the work identity

\[
 J_N=\sum_{n\le N}\frac{\mu(n)^2}{n}
      +2\sum_{n\le N}\frac{\mu(n)M(n-1)}n
\]

does not bound its signed second term. The reviewer checks reconstruct the pair kernel, stopped future and work formula at every integer `N <= 64`.

**Recommendation:** retain the exact coherent-source identification and complete graph-energy asymptotic, plus the rooted survival law. Their chief significance is to identify and quantify a real obstruction to combining the branches. They are not an RH conclusion.

### 2.3 Arithmetic norm transfer, #803 — ANT

Source: `db175de165a9077e709b1cb482998171ffc0c6e7`, `standalone/2026-09-08-arithmetic-norm-transfer/PROOF.md`.

This paper tests another possible adapter: the physical floor-residual norm versus the harmonic prime-power graph form in **coefficient coordinates**. It correctly retains zero coefficients at lower vertices outside the tail; deleting those vertices changes the graph.

For balanced tail coefficients in `[Y,N]`, `N <= AY`, write `R` for the complete physical floor-response energy, `S=sum |c_n|^2/n`, and `G_N` for the full divisor energy. The finite source argument gives

\[
 R\le A^2YS,\qquad G_N\ge(\log Y-\psi(A))S,
 \qquad |G_N-(\log Y)S|\le C(A)S.
\]

The explicit variation

\[
 q_Y(s)=Q_Y(s)(1-2^{1-s})^2(1-2^{-s}),\qquad
 Q_Y(s)=Y^{-1}\sum_{Y\le n<2Y}n^{1-s}
\]

has `q_Y(1)=q_Y'(1)=q_Y(0)=0`, bounded coefficients, support below `16Y`, and `S<189/4`, yet `R>=Y/24`. This proves the order **`Y/log Y`** is necessary for a coefficient-uniform comparison, as well as sufficient in fixed-ratio tails for large `Y`. Any proposed polylogarithmic adapter of this uniform kind is false. Fixed additional jet orders have analogous obstructions; a growing-jet-order assertion is not established.

Adding or subtracting this variation preserves an actual Möbius prefix and all three prescribed normalizations. The parallelogram identity forces one of the two perturbed physical energies to be large. This is not a counterexample to an estimate for the selected native completion or its minimum; it refutes the **uniform transfer shortcut**.

The positive native result should also be retained. Complete twisted partial summation, the classical unconditional Mertens estimate, and critical-line convexity give

\[
 E(p_Y^c)\ll Y\exp\{-c(\log Y)^{3/5}(\log\log Y)^{-1/5}\}=o(Y).
\]

The proof keeps the `(1+|t|)` factor and splits the full frequency integral at the inverse small parameter. It does not use a reciprocal-zeta estimate in an unknown zero-free region. This is an application of classical cancellation to the **complete physical norm**, not a new Mertens theorem or fixed-power saving. It remains compatible with every hypothetical off-line-zero exponent below one.

**Complete profile reconstruction:** the reviewer evaluated all 4,095 rational cells through `T=4096` and retained the exact tail `10000/(3T^3)`. The resulting enclosure is

\[
 1.704219450036840710\le C_*\le1.704219498543224805.
\]

It supports the author's broader printed bracket. `C_*` is the explicit variation-profile constant, not an actual zeta norm, a minimum, or the optimal leading constant of the transfer supremum.

## 3. The #803 predecessor sequence: finite range, scalar criteria and failed closing steps

The following conclusions all concern the frozen `db175...` head, at the individual files in FILES.tsv.

### HT and AN: a fixed compact-annular criterion

The annular filter is fixed before introducing a hypothetical zero. It annihilates the complete safe-prime tail and deterministic exponential terms, while its zeros lie outside the sensitive strip. All prime powers survive in the remaining finite annular source. At square scale `m^2`, the paper defines

\[
 D_m=\frac{1}{192m^3}\sum_n a_m(n)\Lambda(n)-\frac{45m}{128}+\frac14,
\]

with the two nonnegative rational branches of `a_m(n)` on `(m^2/4,m^2]` and `(m^2,4m^2]`. The fixed-source Landau argument gives the stated equivalence between eventual nonnegative square samples, the full-window criterion and RH. Under RH the chosen offset gives a strictly positive margin. Neither this conditional margin nor the legality of the filter establishes the arithmetic lower bound.

The height-transfer paper uses the published verification of all zeta zeros through height `3*10^12` and a complete counting/tail estimate. It obtains positive lower bounds on a **continuum of endpoints**, including the stated `X <= 10^22` range. This is an imported finite-height theorem combined with an analytic tail bound, not a direct scan of primes or a new zero computation.

The reviewer independently enclosed the scalar `C_0`, the `Rbar(H)` tail comparison, and the endpoint inequalities used with concavity to cover the interval. The reconstructed bound is `Rbar(3*10^12)<37/(25*10^12)`. Additional exact/directed tests compute the actual prime-power `D_m` for `2 <= m <= 32`. These are separately declared scopes. The prime-square limiting contribution `49/288` and the resulting changed prime-only baseline must not be dropped when extracting the optional prime-only formulation.

**Recommendation:** retain the complete source-specific criterion and source-qualified finite-range theorem, with the external height and all-height counting input explicit. No all-scale sign is inferred.

### PC, SS and FM: what sparse failure counting really buys

The curvature and interpolation arguments reconstruct the continuous scalar from its prescribed samples with controlled error. The later sparse-sign bootstrap improves the earlier failure-count target: for the specified sample powers `r=1,2` and fixed threshold, **any fixed power saving in the count of negative failures** would suffice for RH. It uses the amplitude bound and meromorphic transform of the **same source**. A generic sparse sequence is not enough.

Under failure of RH, the paper gets lower logarithmic counting exponent one without assuming the rightmost zero edge is attained. A positive-density conclusion requires the separately stated attained-edge/almost-periodic hypotheses. Do not replace the first conclusion by a positive proportion in the unattained case.

The fixed-moment attempt is correctly a negative result about the attempted method. Raw fixed moments already have nontrivial critical-line oscillation and the pertinent diagonal has positive-power size; obtaining a power-saving failure count cannot be justified by the proposed raw-moment bound. This does not refute the sparse-sign criterion, its actual arithmetic input, or RH.

**Recommendation:** keep the sharper sparse-sign criterion, the predecessor interpolation lemmas, and the failed moment mechanism. The missing power saving stays an open node, not an accepted graph edge.

### ES: why a finite prefix and classical-scale accuracy are insufficient

The modified positive Euler-product model preserves the stated finite prime prefix, source-tail scalar and PNT-shaped behavior, while inserting exceptional zeros into a **different infinite source**. The exact infinite arithmetic identities and functional equation are not all preserved. This is a useful stability countermodel, not an off-line zero of zeta. Its scope should be stated next to any synthesis using it.

### MC and CR: contour permission is not a bound; normalization can make an objective rigid

The balanced Möbius contour has zeta in the numerator, so the critical-line contour shift does not assume RH. The square is a signed analytic square, not an absolute square. Complete high-frequency estimates are provided; the low-frequency signed integral is still the hard term. Prefix matching and bounded logarithmic coefficient mass do not imply a source-independent absolute majorant.

The completion-rigidity paper computes the residue dependence on the actual jets. With the prescribed prefix, balance and derivative normalization, the resulting annular functional is unchanged by the allowed completion. Optimizing that constant functional cannot improve the arithmetic sign. With relaxed jets, its displayed dependence is rank one; it does not become a positive-definite closing objective. I reconstructed the triple-jet Laurent coefficients as exact rational identities.

**Recommendation:** preserve these as source/normalization identities and explicit failed-optimization diagnoses. A legal critical-line contour or a positive coefficient Gram does not pay the arithmetic constant term.

## 4. Residual minima: full tails, exact feasible classes, independent numbers

### PR and RN: physical norm and two jets

The full residual is

\[
 E(p)=\int_1^\infty\left|1-\sum_n a_n\lfloor x/n\rfloor\right|^2\frac{dx}{x^2}.
\]

For every finite balanced polynomial the error is positive somewhere beyond its exact initial horizon. This proves positivity of each finite-support minimum once finite-dimensional coercivity is supplied; it does **not** prove a positive infimum over all supports.

The derivative-normalizing binary correction is a bounded idempotent projection with squared norm `1/log 2`, not a contraction. It preserves the target construction up to a controlled support enlargement. It cannot force the still-unknown minimum to be small.

RN reconstructs the exact integer-cell Gram, with the essential constant term `E=-1+a^TGa` on the two-jet affine class. Finite differences and divisor inversion give the tangent-space lower bound

\[
 v^*Gv\ge\frac{\|v\|^2}{4\lfloor N/Y\rfloor^2N(N+1)}.
\]

For `N=2Y` the resulting conditioning is polynomial in orthonormal tangent coordinates. This is a genuine finite optimization tool, not an estimate of distance to the affine target.

### Four complete two-jet minima independently reconstructed

`gram_checks.py` constructs each pair's own periodic fractional-part Gram and an Euler--Maclaurin enclosure of its **entire remaining tail**. No common period of all indices and no numerical special-function oracle is used. Rational midpoint KKT produces a trial; exact symbolic endpoint formulas enforce both actual logarithmic constraints. Merely seeing zero inside a constraint interval would not suffice. A certified stationarity residual and the proved tangent-space floor give a lower bound on the true minimum.

| Prefix cutoff Y | Support N | Reviewer enclosure of the full two-jet minimum |
|---:|---:|---|
| 2 | 4 | `[0.072123117281951579, 0.072123117281951580]` |
| 4 | 8 | `[0.026111243144081930, 0.026111243144081931]` |
| 8 | 16 | `[0.023695806559291602, 0.023695806559291603]` |
| 16 | 32 | `[0.022118909935520037, 0.022118909935520038]` |

These enclosures lie inside the published printed brackets. They are new reviewer-produced evidence for those brackets, not automatic canonical promotion of tighter endpoints. The prefix changes with `Y`; the four classes are not a nested sequence with a fixed prefix. No asymptotic conclusion follows from the displayed decrease.

### RC: three one-jet minima also reconstructed, with a citation repair

The published pass-two record retained the uniform rational tail-comparison theorem but left these three minima unreplayed. This pass freshly solves KKT systems in **all free coordinates** using exact common-denominator integer cells and gcd covariance for the complete period mean. It reconstructs

| Y | N | H | Full minimum enclosure; p(1)=0 only |
|---:|---:|---:|---|
| 2 | 8 | 4096 | `[0.025607338825, 0.025616531671]` |
| 3 | 12 | 4096 | `[0.021620272026, 0.021647203122]` |
| 4 | 16 | 4096 | `[0.019070164807, 0.019120804411]` |

These are **not** RN's derivative-normalized classes. Their tight endpoints come from separately minimizing the lower and upper forms in **equation (18)**. Section 8's attribution to the central form and relative estimate (8) alone should be corrected. The general approximation theorem is not refuted; the claimed numerical brackets reproduce with the stronger displayed comparison actually needed.

**Recommendation:** lift the numerical hold for these exact seven bounded minimum statements, subject to the recorded proof/primitive contracts. Do not treat this as a run of either author's full package or as growing-support subpower control.

## 5. The full #805 sequence: detail, full energy and exact source must stay separate

### DO and BG: the real finite obstruction to the detail shortcut

The initial dilation dictionary, bounded leakage identities and full coupled block formula retain all source coordinates. The odd-detail problem is explicitly solved, with a favorable asymptotic and uniform detail gain. Its optimum is **not** the full residual optimum.

Using a separately reconstructed full Gram, I obtained:

\[
 \delta_8\in[0.024244525306522673,0.024244525306522674],
\]
\[
 \delta_{16}\in[0.017936267020202549,0.017936267020202550],
\]

and the advertised negative dilation leakage. Lifting the optimal detail and then choosing the best old coarse correction gives

\[
 U_8\in[0.025491663369613566,0.025491663369613567]>\delta_8.
\]

Thus this particular detail-driven lift is worse than the old full optimum. The actual full coefficient at nonsquarefree index 9 is nonzero, approximately `-0.105967221798838`. This is a finite-optimality fact, not a proof that index 9 is necessary for asymptotic target approximation.

The finite-support dual for an omitted squarefree index is reconstructed directly. In particular omitting 5 gives the stated `1/52` separating bound. Sharing Mellin zero constraints does not identify two closed spans. The special overlapping dual at index 2 must be handled without double-counting.

### GT and BL: legitimate norm transfers, unknown exponents

The operator-valued Dirichlet convolutions genuinely retain the full source and metric. Growth statements still contain the unknown zero edge; they do not evaluate it as one half. The use of the quoted Balazard--Saias lemma retains its zero-free-half-plane hypothesis. The case with no available half-plane strictly between the zero edge and one is treated separately, not inserted into a theorem requiring such a half-plane.

The squarefree target-density statement is distinct from ambient density and finite optimality. The damped approximation converse is conditional on RH; an undamped strong-convergence assertion is not supplied.

The balanced-lift rational optimizer has explicit native coefficient approximation and a finite initial horizon. Its full norm includes the central unresolved range even when the early error and far tail vanish. Near-optimal detail and local agreement do not control that middle energy.

**Small wording repair:** where BL's explanatory prose says that the "full norm" has `Omega(sqrt(M))` growth, the displayed result concerns the **squared norm/energy**. The corresponding unsquared lower growth is `Omega(M^(1/4))`. Do not double the exponent in extraction.

### GE and TE: exact Green and harmonic representations, not endpoint cancellation

The finite balanced odd source has an exact Green energy with all cotangent charges and cross terms. Finite ordered breakpoints give the Brownian-min kernel and its tridiagonal inverse. Improved native coefficient bounds and a polylogarithmic complement estimate are retained. The shrinking endpoint remains the unknown energy region.

TE's harmonic replacement proves

\[
 \sqrt{E[\lambda]}\le\sqrt{\mathcal H[\lambda]}+4B[\lambda],\qquad
 \sqrt{\mathcal H[\lambda]}\le\sqrt{2E[\lambda]}+2B[\lambda].
\]

This pays the complete far tail, not just a compact trigonometric interval. For rational coefficients the entire harmonic energy is a quadratic polynomial in `log 2` with rational coefficients. A family with subpower `B` has equivalent subpower full/harmonic energy, but neither bound is proved by the comparison.

TE then deliberately changes to a terminal-balanced Möbius family. Its exact horizon, nonsquarefree terminal correction, and transform of `Q(x)=M_o(x)-xm_o(x)` give a prescribed fourth-power-grid criterion. An arbitrary selected subsequence is not covered by that sampling argument, and the scalar criterion does not apply to the earlier different optimizer merely by sharing notation. A balanced source with zero first harmonic interval but positive full energy is an explicit control.

**Small wording repair:** for a general support bound `M`, the formula for the "first interval" must mean the specified interval `(0,1/M)`, or `M` must be the relevant active mesh cutoff. If `M` is only a loose bound, the actual first mesh cell can be longer. This does not invalidate the full harmonic comparison or the stated terminal-grid criterion.

### BH and CL: exact main-term cancellation and a still-open signed integral

The balanced hyperbola/Newton hierarchy is coefficientwise finite. Its identity at the closed support endpoint is valid because the smoothing weight vanishes there; the coefficient itself need not match at that endpoint. Balance annihilates the complete pole main term before a norm is taken.

The compact continuum remainder operator has norm at most `1/8`, but the corresponding **unweighted sampled matrix** has linearly growing norm. Explicit bounded balanced sources give either sign with quadratic size. I reconstructed their rational formulas. Consequently a small continuum kernel and a small diagonal do not yield a near-linear estimate for the actual discrete vector.

The actual identity `B_Y=Q(Y^2)-2Q(Y)` gives the source-pinned grid criterion. CL legally shifts its zeta-numerator contour to the critical line, with `P_Y(s)^2`, not `|P_Y(s)|^2`. The complete high-frequency tail is `O(Y)` at the prescribed cutoff; the finite signed integral remains uncontrolled at the required scale. The classical unconditional improvement is weaker than every requisite fixed power saving. Either **fixed** one-sided near-linear estimate would suffice; choosing the favorable sign separately at every sample would not.

**Recommendation:** retain the exact source identities, complete transfers, lower-growth and no-go results; keep the full residual gain, prescribed-grid bound, and low-frequency estimate open. These packets are not eight independent approaches to be multiplied together.

## 6. The #804 cutoff/work sequence and #811 entropy feedback

### DC: source input versus realized output

The cutoff construction matches the stated higher-degree target before its exact horizon and retains the entire stopped future. Its target is neither the unit exponential used in IE nor the older ramp trial. Zero multiplicity is retained in the Laguerre obstruction.

The complete Gram-floor calculation gives an explicit rank-dependent lower bound. It is not a rank-uniform floor. Damping changes the generator; multiplying coefficients by a damping factor is not automatically a contraction on the old generated space. The missing commutator or domain adapter cannot be discarded.

### MW: exact signed input work and critical resonance

The Lyapunov matrix identity gives the full four-state energy, including the future contribution. Its actual finite work at cutoff three is strictly positive; the reviewer reconstructed the rational Lyapunov solution, all four positive pivots, and a directed value above `1/20`. This refutes the attempted source-blind diagonal domination at its literal scope.

A classically existing critical-line zero forces logarithmic input-energy growth. Thus a uniformly bounded subsequence of this **input** energy is not an admissible completion target even under RH. A linear upper input bound would impose additional simplicity/residue-summability conditions. These statements do not obstruct a bounded **output** or a different realization strategy. The source's larger numerical campaign has not been replayed here.

### EF: exact nonlinear feedback accounting, open arithmetic upper work

At the unchanged ordinary-prime source and physical Cauchy measure, the log-cosh argument gives, for every real `X >= 2`,

\[
 |2E(X)-W(X)|<8+24\log(1+\log X).
\]

The proof correctly uses the pre-jump source at each prime, includes every power of that prime at its birth, and controls the complete higher-power and nonlinear jump remainders. The initial frequency tail and mean are explicitly paid. An elementary prime-harmonic estimate suffices for this identity; no RH input is hidden in it.

The associated saturated kernel is positive semidefinite, but the feedback is a signed off-diagonal correlation with a subtraction. Positivity therefore supplies no decay estimate. The identity yields a lower bound on `W`; the required subpower **upper** bound is still open. The endpoint transfer in the sibling paper and this work balance are compatible tools, not independent upper estimates.

**Recommendation:** retain the all-cutoff accounting identity with its exact source and measure. Do not turn a bounded feedback function, a positive kernel, or a nonnegative convex remainder into the missing arithmetic estimate.

## 7. Corrections, imports and evidence boundaries

### Corrections for the eventual extraction

1. **RC numerical attribution:** use separately minimized equation (18), not equation (8) alone, for the three tight one-jet brackets.
2. **BL exponent wording:** distinguish norm from squared norm in the `Omega(sqrt(M))` energy statement.
3. **TE interval wording:** identify `(0,1/M)` explicitly when `M` is an arbitrary upper support bound.
4. Carry forward pass two's **eleven**, not ten, prime bases in the `N=32` divisor inverse.

These are component repairs, not a claim that the intended principal theorems are false. Any materially strengthened statement, newly combined adapter, or tighter canonical numerical endpoint still needs its own approval; this review does not install it.

### External analytic inputs checked at their needed scopes

The classical Mertens estimate was checked against Lee--Leong, arXiv `2208.06141v4`; only the qualitative Vinogradov--Korobov-shaped bound is consumed. The critical-line convexity consequence was checked against DLMF 25.9's approximate functional equation. The published Platt--Trudgian height `3*10^12` is an imported zero-verification theorem, not a new computation. Baez-Duarte `math/0202141v2` was inspected, including the quoted Balazard--Saias lemma and the conditional identification before the limiting approximation. The original Balazard--Saias proof was not independently reread.

These are source checks, not a comprehensive originality/literature audit. Standard finite spectral, Hilbert, Mellin, partial-summation and positivity arguments are not claimed as newly discovered general mechanisms.

### What the new code does and does not establish

All new mathematical computations are reviewer-written and use standard-library integers, rational arithmetic and outward interval bounds. **No author numerical producer or package test suite was executed in this pass.** The new finite computations use the mathematics of the sources but independently implement the stated reconstruction. That independence of computation does not certify a distinct non-author referee identity: the project's agents share an account and naming conventions.

The complete finite statements actually reconstructed are enumerated in [VALIDATION.md](VALIDATION.md) and their receipts. Finite checks do not prove an analytic infinite passage. In particular no new full-checkout validation, Lean/comparator/axiom audit, native Windows run, remote CI result, actual high-zero computation, large Möbius/prime-discrepancy campaign, or full historical/discussion census is claimed.

The two important certificate replays in the **published second pass**—unit-window positivity and the entropy trial—retain their own code and assurance boundaries. They are not counted as fresh runs here. The completed finite minima and anchoring constants here do not discharge their respective unbounded arithmetic targets.

## 8. Integration readiness after one final targeted pass

The principal-paper queue is cleared at the frozen inventory. The remaining pass should inspect the supporting source/synthesis/attempt files, reconcile any revised heads, and either clear or explicitly exclude each author package/certificate not yet covered. Highest-priority numerical leftovers are the fixed-horizon ordinary-input realization and older ramp/compact-source trials, square-grid prime-energy prefixes, and any finite Green/capture assertions selected for publication beyond the reviewer reconstructions already supplied.

For each packet, finish with one of: exact proof component ready for extraction; exact numerical component supported by a declared reconstruction; exploratory source retained without acceptance; or a specific hold with named missing file/input. No reviewer needs to solve the still-open RH-strength estimate to dispose of the packet honestly.

The eventual cumulative account should explain the new positive results and their exact scope, not headline review counts. In particular it should retain both the improved unit-window sign and the arithmetic graph bounds, while displaying why neither the coherent channel nor the graph-to-physical comparison is automatically paid. **Integration preparation, final review of that branch, and merge remain later user-authorized stages.**
