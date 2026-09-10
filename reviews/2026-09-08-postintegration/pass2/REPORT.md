# Post-integration review — pass 2

**Review recommendations only. RH remains unproved. No integration branch or main change is authorized by this packet.** This continues draft PR #827 while retaining pass one unchanged. The source commits in [SOURCE_HEADS.json](SOURCE_HEADS.json), exact file blobs/read boundaries in [FILES.tsv](FILES.tsv), and [coverage table](COVERAGE.tsv) govern every recommendation below. A branch head is a retrieval anchor, not blanket review of its contents or ancestry.

## Verdict and coverage

The two numerical holds prioritized in pass one can now be narrowed substantially: the **complete length-one coefficient certificate** and the **intrinsic-entropy trial with its entire tail** both reproduce in normal and optimized Python after source-byte authentication. Their paper interfaces were reconstructed separately. I recommend their stated component conclusions for later integration, not an all-window sign or zero intrinsic defect.

This pass also reconstructs the main arguments for uniform rational residual capture, two complementary divisor-graph bounds, finite realization/conditioning, actual-source feedback failure, and the source-faithful prime-discrepancy chain. No fatal mathematical defect was demonstrated in these inspected main arguments. This is not clearance of every supporting file, numerical package, inherited adapter, or research PR.

Twelve packets received main-proof attention in this pass: WP, IE, RC, ADG, DPG, DC10, FR, FC, ST, OEC, EPD and PDS. WP and IE deepen prior paper reviews. Nine advance packets previously triaged. Thus **21 of the original 42 packets have main-proof-level coverage across the two passes, with 21 still at triage depth**. This denominator measures reading depth, not accepted theorems or fully audited packages. DC10 is an additional **preintegration held dependency**, not a new postintegration packet. Only the opening source/index sections of its HH5 ancestor were examined.

A new PR #828 was discovered during the pass at `528b33ac8d57b5a046260ee45d585cd3fe720f4c`. Its description and successor comments were read for inventory, not its proof or checker. It is explicitly queued. Existing watched research heads did not drift between the opening and recorded recheck, except that #803's pass-one late head is now the anchor of the selective new review. The observations are not a global atomic freeze.

## 1. Full length-one positivity: the numerical hold is now supported by replay

**WP, PR #803 at `31a35a90b0b924dc98a2c89c463fb59577f45a4e`.** The relevant paper is `standalone/2026-09-06-logarithmic-core/window-one-positivity/PROOF.md`, blob `644392c4a59edff697851fe526b8da5de96492cf`.

The source is the actual damped Hardy/Weil kernel

$$T(t,u)=\frac32 e^{-3(t+u)/4}W(t-u),$$

including its gamma term, the prime-2 cusp on the unit difference interval, and the complete arithmetic constant $P_2=-\zeta'(2)/\zeta(2)$. It is not a raw prime cutoff or a fitted matrix. The constructed four-periodic positive extension agrees with the necessary residual kernel on $[-1,1]$; positive cosine atoms are added back. No claim of agreement on larger difference intervals is used.

I checked the finite Fourier integrations, endpoint/spline derivative jumps, real digamma representation, directed primitive formulas, and the separation between the 256 rational spline phases and the nonperiodic prime phase. The latter is bounded independently; it is not incorrectly reduced modulo 256. The tail proof uses a positive partial gamma sum as a lower bound, with the entire remaining analytic error paid. The NIST digamma asymptotic remainder convention is consistent with the terminated Bernoulli series and sector factor used in the consumed code.

The exact published input, interval core and verifier were authenticated before execution. All **2,049 initial coefficients**, all **256 phase residues**, and the analytic all-index tail test passed in both Python modes. The complete output is byte-identical to the published result blob `a94e20c9cbdb16e29fc95d5a95d6be9e660de2e5`. The least finite scaled coefficient occurs at mode 149 and exceeds $2^{-35}$; the tail lower bound exceeds $2/5$. See [the reconstructed output](evidence/window-one.json).

The Fourier-series deduction then applies to every complex $L^2$ test supported on an interval of length at most one, not just sampled vectors. In the undamped variable $h$, it gives the source's $H^{-1}$-type lower bound with constant $3\delta/4$, $\delta=2^{-35}$. It is **not a uniform positive $L^2$ eigenvalue gap**. The resulting lower bound for the specified length-one effective Schur matrix uses the same undamped form and the source's basis Gram matrices; it does not mix damped and undamped normalization.

**Recommendation:** retain the fixed-length all-functions theorem and its exact certificate/proof interface. This changes the earlier “actual length-one sign not certified by this review” recommendation at these bytes. It does not settle an unbounded family of windows. The arithmetic implementation was reused and inspected, not replaced by a second independent special-function backend. Original package-wide tests, witness optimization and full-repository validation were not run.

## 2. Intrinsic entropy: a complete trial bound, not a vanishing defect

**IE, PR #819 at `c4fb013692c51d6b26b8a3c33200615af764da82`.** Main proof blob `afb721d6eddae8eb4fe861091f9747394bd7c708`.

For the literal factorial source, the Cayley image is $A(w)=w\zeta(1/(1-w))$, with $A(0)=1$. Its factorization $A=BO$ retains any off-line Blaschke factor. The proof's exclusion of a singular factor uses actual boundary continuation and the positive-real behavior at the exceptional boundary point; it does not assume outerness. The classical logarithmic defect is

$$J=\frac1{2\pi}\int_{\mathbb R}\frac{\log|\zeta(1/2+it)|}{t^2+1/4}\,dt\ge0.$$

The unit exponential target maps to 1, so its intrinsic squared error is $\delta=1-e^{-2J}$. The ramp target maps to $1-w$ and can suppress that error cubically. The exact ramp formula, Schwarz–Pick sensitivity bounds, the second logarithmic moment, and the strip-qualified nonnegative refinement survive reconstruction. Neither the moment formula nor the decreasing finite Toeplitz determinant-ratio entropy sets $J$ to zero. The quantitative rate corollary still inherits HC1's pass-one source-specific review boundary.

I inspected `check.py`, the full certificate function, and its consumed 160-bit integer-interval paths, then executed **the certificate function**, not the entire package CLI/test suite. The degree-six rational trial integrates all 2,047 integer cells through $x=2048$. Its smooth future state and primitive periodic-Bernoulli remainder retain the **entire** infinite tail. In particular, the bound on the integrated remainder follows by writing it as $\partial_t\epsilon(e^t)-\epsilon(e^t)$ with $|\epsilon(x)|\le1/(6x)$; a pointwise remainder is not integrated as if it decayed by itself.

Both modes reproduce

$$0.047034408869<\|p(R)d-e^{-t/2}\|_2^2<0.051343069499<13/250,$$

hence

$$0\le J\le-\tfrac12\log(237/250)<27/1000.$$

The complete tail upper contribution is below $0.004308660629$. [The output](evidence/intrinsic-entropy.json) retains its integer interval endpoints. A positive lower endpoint for this **trial error is not a lower bound for the optimal error or for $J$**. This experiment is not the old prefix-matched ramp experiment or a compact-input realization certificate.

**Recommendation:** retain the complete trial upper bound and the exact target/entropy identities, crediting the classical Balazard–Saias–Yor/Hardy mechanisms. Do not advertise a competitive zero-free-height bound, $J=0$, or closure of growing-horizon control. The reused interval core is explicitly not an independent arithmetic implementation.

## 3. Rational residual capture: the tail can be controlled before optimization

**RC, PR #803 at the same frozen head.** `standalone/2026-09-08-rational-residual-capture/PROOF.md`, blob `e7b0dfd9db3a114962ed610c9b19900df135b58b`.

The finite balanced source is

$$u(x)=b-\sum_{n\le N}a_n\lfloor x/n\rfloor,\quad \sum a_n/n=0,\quad E=\int_1^\infty |u(x)|^2x^{-2}dx.$$

The complete period mean $V$ includes the mean-square term $|b+\sum a_n/2|^2$, plus the Jordan-totient gcd-covariance form. CRT gives the covariance, while rational-frequency separation and a harmonic-row estimate give a uniform interval discrepancy. Abel summation yields

$$|E-Q_H-V/H|\le C_NV/[H(H+1)],\quad C_N=N^2(1+2\lceil\log_2N\rceil).$$

The step $V\le4C_NE$ is what makes the ensuing relative comparison uniform over **all coefficients**, including optimizers with large coefficients. With $\widehat E_H=Q_H+V/H$, the relative error is at most $4C_N^2/[H(H+1)]$. Choosing $H=2C_N\lceil\sqrt N\rceil$ makes it less than $1/N$ at physical cutoff $O(N^{5/2}\log N)$.

The finite-dimensional coercivity/uniqueness argument and the minimum sandwich follow at a **fixed, nonempty affine class**. The rational matrix does not make an extra logarithmic derivative constraint rational. The source's three advertised finite minimum brackets use only balance, not that derivative-normalized class; I have **not replayed those three minimizations**.

The centering correction at $H,2H,4H$ preserves the two safe jets and old prefix at a controlled full-norm cost, but permits growing support. It does not equate minima at the same support. The bounded rational two-block completion controls the complete far tail; it does not control the earlier energy at subpower scale.

The independent review code reconstructs CRT covariances, complete small periods, interval discrepancy controls, centering algebra and native-prefix countercontrols. In particular $Q_H$ alone can be zero while $E>0$. Finite tests support the exact formulas; the all-support/infinite-tail theorem still rests on the paper argument.

**Recommendation:** retain the uniform full-form comparison and its fixed-support optimization consequence. This is a useful removal of an optimization/tail interchange obstacle, not a proof that the minima tend to zero or grow subpower with the prefix.

## 4. Divisor graphs: two compatible gains, one uncontrolled coherent channel

**ADG #825 at `e4a486d3fd4009e3722e9e93f35710b834fbd195`; DPG #826 at `3a82b80da82edbcd65d4538418a3d51d6030f058`.** Their main proof blobs are `d87d275f53b68472e29dce777de3f786566184fc` and `3e598e27e6b258d2fbd1a77740543ae99e191c3f`.

Both use the complete prime-power energy on a finite divisor-closed support,

$$\mathcal E_S(f)=\sum_{jp^k\in S}\frac{\log p}{jp^k}|f(jp^k)-f(j)|^2.$$

Least-prime **full-power** removal gives a genuine tree inside this graph. Divisor closure is indispensable: $S=\{1,6\}$ is a countercontrol, not an admissible connected support. Descendants of an edge involve strictly smaller primes; their harmonic mass is paid by the original $\log p$ conductance. The elementary finite Euler-product estimates do not assume PNT, RH, or independence of physical prime phases.

ADG proves the anchored inequality with

$$\kappa(P)=48[1+\log(16\log P)],$$

uniform in cardinality, exponent depth and support shape on primes at most $P$. The centered inequality follows. The tunable path weight is the load-bearing improvement over an unweighted path-length bound. Infinite reservoirs are allowed only on a **fixed finite prime alphabet** with the stated closed form/conservative-domain construction.

DPG proves the complementary bound $24r_S$, $r_S=\max\omega(n)$, an explicit decoder, complete one-prime spectra and rectangular tensor spectra. On $\{1,p,\ldots,p^m\}$ the nonzero eigenvalues are

$$\log p\left[j+\sum_{\ell=1}^{m-j+1}p^{-\ell}\right],\quad 1\le j\le m.$$

The weighted step eigenvectors and their orthogonality were reconstructed exactly. A rectangular spectrum is **not** the spectrum of the cutoff $n\le N$. The fixed-finite-prime infinite construction is not an unrenormalized all-prime operator. The singleton support must be handled without dividing by $r_S=0$.

The residual/Schur applications are valid in the original metric: for $A\succeq\gamma I$, trial $Y$, $R=B-AY$ and $V=Y^*B+B^*Y-Y^*AY$,

$$H_0-V-\gamma^{-1}R^*R\preceq H_0-B^*A^{-1}B\preceq H_0-V.$$

Positive upper sections alone are still insufficient. The harmonic ground channel remains; for Hilbert-valued vertices it contains an **entire common function**, not a single scalar. Neither paper identifies the full gamma/continuum/mean coupling with this graph or bounds the actual prime-discrepancy energy by it.

### Independent actual finite inverse

For the ADG $N=32$ example I reconstructed every stiffness contribution in its rational harmonic-mean-zero coordinates. All **65 prime-power edges and eleven prime bases** are included. The PR description's phrase “ten prime bases” is a minor prose error, not a missing edge in the reconstructed matrix; correct it before publishing the integrated summary.

The review implementation uses its own reduced positive-atanh logarithms, 112-bit rational endpoints, Loewner inverse order and exact LDL solves. It does **not** use the author's approximate solution, rational trial, interval backend, or precomputed matrix. It proves the rational minorant $K_- -M/384\succ0$ and encloses the actual inverse quadratic by

$$0.744480619465733367\le b^TK^{-1}b\le0.744480619465733368.$$

There are 93 positive exact pivots across the three 31-dimensional factorizations, with exact linear-system residual checks. This is separate reviewer-produced finite evidence corroborating the original bracket, not an automatically accepted stronger canonical statement, a computation of a zeta value, or a proof of the infinite gap theorem. See [reviewer output](evidence/independent.json).

### The older cusp predecessor

DC10 in #790 at `6b309554bf1e2f83a83325cd54038f5a0b9b0014` was committed **September 5**, and is already named in the preserved review census. It is a held preintegration dependency, not newly pushed September-8 research. I reconstructed its prime-power square, logarithmic cusp bound and all-$N$ positivity on the specific windows of width $2^{-20}N^{-2}$, imposing a separate damped mean-zero condition in each window.

The regular cross interaction, exact divisibility cusps, complete $P_2$ tail and source invariant budget remain necessary. Only the relevant opening HH5 source/index sections were reread. Unrestricted window means and their coupling are not controlled; at most $N$ negative directions is not zero. The total support measure tends to zero, so these windows are not a cofinal capture hierarchy. ADG/DPG improve the same graph complement without eliminating these restrictions.

## 5. Realization and conditioning: useful theorems and an actual feedback obstruction

**FR/FC in #812 at `2d683186cb3dd4f304159d8176215ceae8ac59fb`; ST in #814 at `dc7babb830cb696810fb68bd74f6a33459f5f921`.**

FR's ordinary-box approximation treats the discontinuities of the actual factorial source, including the leading translation modulus $s\log(1/s)+O(s)$. The coefficient and truncation allowances preserve complete future filter tails. Its finite-Gram floor is for a fixed rank, not a uniform all-rank inverse. Its fixed-horizon **numerical** improvement remains on hold here: inspecting the analytic realization argument and replaying IE's different trial does not rerun FR's ideal/compact trial certificate.

FC and ST improve actual-source finite conditioning to explicit rational floors of order $\exp[-O(\log^2(K+2))]$, using alternative constants. Their Jensen/Harnack arguments remove a small exceptional set around **possible zeros** rather than exclude those zeros. Polynomial mass bounds on the complement give the Gram floor. The resulting source cutoff is quasipolynomial in rank; the large constants are not a practical bit-complexity claim. The two proofs describe the same order of conditioning, not two independent routes around the intrinsic obstruction.

ST separately proves quantitative inverse-input blow-up at a critical-line boundary zero of order $m$: if the approximation error is $\varepsilon$ and the target does not vanish there, then $\|v\|\ge c\varepsilon^{-(2m-1)}$. Exact $L^2$ input attainment is impossible. Rational models show sharpness for the general class. This constrains input cost, **not** closure of the range or subexponential growing-horizon output error.

FC exposes a more concrete failed composition. For its fixed ideal trial, the second feedback iterate has a nonzero atom, with coefficient $-17689/100000000$, so it is not locally $L^2$. More generally, in the stated ordinary compact piecewise-regular input class, the actual relative response is unbounded on the critical boundary. Safe-line Dirichlet coefficients at all but finitely many primes survive, and finite Bessel sums force divergence; no RH assumption is used. Repeating one controller then has superexponential norm cost, interpreting a non-$L^2$ iterate as infinite cost.

This is an **actual-source obstruction to fixed-controller repetition**, not merely a synthetic example. It does not refute the original fixed-horizon correction or controllers re-chosen as the horizon grows. The excellent-conditioning example $A(w)=1-2w$ remains a separate synthetic explanation of why convergence to the intrinsic floor does not evaluate that floor.

## 6. The prime-discrepancy chain: remove an analytic loss without deleting arithmetic work

**OEC, EPD and PDS in #811 at `946dedfa3f6ec2d74f3f0f00f9ca511abf9652d7`.** The PR description still advertises an earlier head; the frozen file blobs, not that prose checkpoint, control this review. The entropy-feedback sibling and auxiliary attempt/Abel notes were not read in full.

Keep the ordinary-prime completion $A_X$, **all powers of every included prime base**, and the physical measure $d\mu(y)=dy/[\pi(1+y^2)]$. Its finite-cutoff cost $E(X)=\int\log^+|A_X(1/2+iy)|d\mu$ is not IE's limiting logarithmic defect $J$.

OEC proves an entropy-to-smoothed-logarithmic-derivative bound with a strictly positive inward shift. The derivative has a literal signed causal prime/continuum measure. Convolving with the actual factorial source gives an admissible output matching a fixed target before $\log X$. At a hypothetical off-line zero of multiplicity $m$, the lower jets vanish; the normalized Laguerre test gives the correct factorial constant without an artificial power of $\log X$. This supplies power-growth obstructions and conditional criteria, not an upper estimate.

EPD removes the inward shift by a **different argument**, not substitution of zero into a divergent constant. The first-prime part has positive frequencies between $\log2$ and $\log X$. A compact, one-sided smooth multiplier reconstructs its analytic derivative from its real part; the infinite higher-power frequencies are paid separately. I reconstructed the Fourier factors, weighted convolution inequality and the three polynomial pieces giving

$$\|m_\Lambda-m_\Lambda''\|_2^2=\frac{1142}{315}\Lambda^3+\frac{768}{35}\Lambda+\frac{463514}{1215}+\frac{624}{5\Lambda}<576\Lambda^3.$$

Consequently a zero with depth $\delta=\beta-1/2>0$ forces the **full-depth** lower bound $E(X)\ge\kappa_\rho X^\delta/(288\Lambda^{3/2})-8\sqrt\Lambda$, $\Lambda=\max(1,\log X)$, with multiplicities retained. This is a genuine analytic endpoint improvement; its missing arithmetic upper bound remains open.

PDS supplies a complementary uniformly bounded error: the complete higher-prime-power term has $L^2(\mu)$ norm below 14, with explicit prime-base tail bound, even though it diverges at the single frequency zero. Therefore $|2E(X)-\|\Re C_X\|_{L^1(\mu)}|<32$. Elementary Chebyshev estimates suffice for that statement; the optional sharp tail asymptotic imports ordinary PNT separately.

### Reconciliation of the two complete-square formulas

The EPD suffix energy $Q(X)$ and PDS filtered-past energy $I(X)$ satisfy

$$Q(X)=\|\Re C_X\|_{L^2(\mu)}^2=I(X)+c_X^2/2.$$

Here $c_X$ is the common safe-value discrepancy. This follows directly from the two papers' finite-measure Cauchy-kernel identities; independent rational atomic controls check both decompositions. The forward version's stopped-state tail $R(X)^2/(2X^2)$ and the backward version's initial constant term are compulsory. These are **two representations of the same complete physical norm**, not two independent arithmetic bounds. They do not identify that norm with the harmonic divisor graph or the floor-residual period form.

Both retain the classical RH-conditional upper scale $Q,I=O((1+\log X)^3)$ and $E=O((1+\log X)^{3/2})$. Unconditional PNT still leaves positive-power growth allowances. The entire signed prime/prime, prime/continuum and continuum/continuum interactions remain in the square. No independent-prime replacement, local reset or diagonal-only estimate proves the missing bound.

## 7. Evidence, independence and next action

The newly written reviewer checker imports no author code and passes **3,024 bounded exact reconstruction assertions** in both modes, with identical JSON. This includes the independent actual inverse, exact prime-power eigenvectors, rational residual controls and polynomial/Fourier normalization checks. Separately, **213 pinned-subset primitive/parser/hash contracts** pass. These counts have different purposes and are not combined into a theorem count.

The two certificate calculations also pass in both modes. Only five author files are compiled/consumed by the new replay wrapper; each is authenticated first and rechecked afterward. The wrapper and recorded results are reproducible from the exact source commits. This is methodological independent checking and, for the $N=32$ inverse, a separate arithmetic implementation. It is **not an assertion that the same agent/account name proves non-author referee independence**. That question remains distinct from the mathematical and execution evidence.

No complete checkout, Lean build, remote CI result, full author-package rejection suite, all-history audit, or exhaustive source-branch review is claimed. [REPLAY.md](REPLAY.md) lists what ran. [RESUME.md](RESUME.md) gives exact delta instructions and the remaining queue. Do not merge this review PR as a substitute for a later curated integration decision.
