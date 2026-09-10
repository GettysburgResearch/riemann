# Causal arithmetic sources, realization and intrinsic entropy

[Guide](README.md) · [Proof library](SOURCE_INDEX.md) · [Evidence](EVIDENCE.md)

**Status:** reviewed component selections in an integration candidate. All domain, target and norm distinctions below are part of their scope. They do not repair the separate historical Lean input by editorial restatement; see [formal status](../../../FORMAL_STATUS.md).

## 1. Positive source results and the critical-domain distinction

The generalized-Jordan source has an all-time Green-density positivity theorem at every positive scale for $\kappa\ge2$, with sharp universal threshold 2. It also supplies the literal prime-deletion margin

$$s^2\sum_p\frac{\log p}{p^s(p-1)}-\frac1{\zeta(1+s)}>\frac{13s^3}{1800},\qquad0<s\le1.$$

The complete contacts, atoms and density yield positive kernels in the stated safe Laplace domain. This extends a restricted positivity region; it is not an extension of that measure to a critical contour where its exponential continuation is undefined. See the [all-scale proof](../../../standalone/2026-09-06-astra-sharp-jordan-green/PROOF.md) and [real-axis margin](../../../standalone/2026-09-06-astra-sharp-jordan-green/REAL_AXIS.md).

For the causal critical construction the actual source is

$$d(t)=e^{-t/2}\bigl[\lfloor e^t\rfloor(1-t)+\log(\lfloor e^t\rfloor!)\bigr],\qquad t\ge0,$$

with $\|d\|_1\le6$, $\|d\|_2^2\le5$, and

$$D(z)=\frac{(z-1/2)\zeta(z+1/2)}{(z+1/2)^2},\quad D(1/2)=1\text{ by analytic removal}.$$

Its unitary disk image is $A(w)=w\zeta(1/(1-w))$, $A(0)=1$. The closed causal-translation/all-pass source space is the corresponding $BH^2$, where the possible Blaschke factor retains every shifted right-of-line zeta zero with multiplicity. The source argument excludes a singular inner factor, **not** these possible zeros.

**Proof route.** Finite floor/factorial identities give the original Laplace transform; exact functional-equation and Hardy source arguments identify the admissible source space. Safe-axis kernel positivity must not replace this source-domain theorem. Read [literal input/output construction](../../../standalone/2026-09-06-astra-critical-source-map/CONSTRUCTION.md) and [domain and approximation](../../../standalone/2026-09-06-astra-critical-source-map/DOMAIN_AND_APPROXIMATION.md).

## 2. Quantitative approximation reaches the actual floor

Finite all-pass Grams are invertible with explicit lower bounds. Source-specific analyticity improves one bound to a quasipolynomial inverse allowance. The fractional-Sobolev capture theorem gives a quantitative rate toward projection onto the **actual** $BH^2$ space, and a growing-horizon excess-error schedule with uninstantiated constants. Finite ordinary input realization can then approximate the specified finite output, paying its coefficient and truncation costs.

The identity

$$\|(I-P_K)q\|^2=\|(I-P_{BH^2})q\|^2+\|(I-P_K)P_{BH^2}q\|^2$$

separates intrinsic error from finite-synthesis error. Neither good conditioning nor rapid decay of the second term makes the first vanish. A boundary zero can force approximate inverse **input** norms to diverge even when target approximation in the closure is possible.

See [stability and inverse-input cost](../../../standalone/2026-09-07-astra-source-stability/PROOF.md), [capture with its target hypotheses](../../../standalone/2026-09-07-astra-quantitative-capture/PROOF.md), and [ordinary realization](../../../standalone/2026-09-07-astra-future-realization/PROOF.md). The proof routes retain the inner factor, complete output tails and the distinction between operator and form domains. Their constants are not a practical large-rank computation claim.

<a id="entropy"></a>
## 3. The intrinsic floor is a classical logarithmic defect

For the unit target $e^{-t/2}$, whose disk image is 1, set

$$J=\frac1{2\pi}\int_{\mathbb R}\frac{\log|\zeta(1/2+it)|}{t^2+1/4}\,dt.$$

The source-qualified factorization gives exactly

$$\delta=\operatorname{dist}(1,BH^2)^2=1-e^{-2J},\qquad
J=\sum_{\Re\rho>1/2}m_\rho\log\left|\frac\rho{\rho-1}\right|\ge0.$$

Thus $J=0$ is RH-equivalent. The argument is the credited Balazard–Saias–Yor/Hardy mechanism, not a newly evaluated constant. Finite Toeplitz determinant ratios converge monotonically to $J$; the reviewed rate corollary retains the capture theorem's hypotheses and converges **to $J$**, not automatically to zero.

For the old ramp target $te^{-t/2}$, with disk image $1-w$ and squared norm 2, the horizon-zero intrinsic error $C_0$ satisfies $\delta^3/4\le C_0\le4\delta$. The cubic attenuation explains why a small ramp error cannot be treated as the same experiment as a small unit-target defect.

A fixed degree-six actual-source trial, with its entire tail retained, gives

$$.047034408869<\|p(R)d-e^{-t/2}\|_2^2<.051343069499,\qquad0\le J<.027.$$

The trial's positive lower endpoint is not a positive lower bound for the optimum or $J$. See [complete identities, target sensitivity and certificate](../../../standalone/2026-09-08-astra-intrinsic-entropy/PROOF.md) and [its evidence contract](EVIDENCE.md#entropy).

## 4. Fixed-horizon constructions genuinely use ordinary inputs

The compact-domain construction supplies explicit ordinary compact inverse inputs and eight full output-error calculations through cutoff $N=128$, including complete infinite tails. At $N=64$ its squared ramp error divided by the target's squared norm is below $1/19000$. These are prescribed trials, not optimized minima. The strict increases at $16\to32$ and $64\to128$ remain part of the result.

A different future-realization experiment at $T=\log2$ reduces full squared ramp error from above $0.3$ to below $0.001$, a greater-than-300-fold reduction. The bound survives replacement of the ideal correction by an ordinary compact $L^2$ input; the certificate includes every half-cell and the complete future. It is a **fixed-horizon** result, not the growing-horizon estimate needed for closure.

Read [compact-domain proof](../../../standalone/2026-09-06-astra-compact-domain-completion/PROOF.md), [future-realization proof](../../../standalone/2026-09-07-astra-future-realization/PROOF.md) and [numerical scope](../../../standalone/2026-09-07-astra-future-realization/NUMERICS.md). The separate [pole-neutral cutoff construction](../../../standalone/2026-09-06-astra-domain-cutoff/CONSTRUCTION.md) has its own higher-degree zero-safe target and future interpolation cost; its numbers cannot substitute for these ramp or unit-target trials.

<a id="work"></a>
## 5. Complete stopped-input work and boundary resonance

For the fixed cubic filter

$$\phi(t)=e^{-t}(1-5t/2+7t^2/8-t^3/16),\qquad
h_N(t)=\sum_{n\le N}\frac{\mu(n)}{\sqrt n}\phi(t-\log n)\mathbf1_{t\ge\log n},$$

write $J_N=\|h_N\|_2^2$. A four-state realization gives the exact identity

$$J_N=H(\log N)+x_N^*Qx_N=D_N+W_N,\qquad
D_N=\frac{385}{2048}\sum_{n\le N}\frac{\mu(n)^2}{n}.$$

The positive storage term is the full stable future after the last included input. It is not future Möbius events. The signed work is positive already at $N=3$, refuting universal diagonal domination at the actual source. A classically existing critical-line zero forces at least logarithmic inverse-input energy growth; multiplicity-sensitive lower bounds retain their stronger powers. This does not force the factorial-source **output** to diverge.

The selected complete run through 65,536 events gives

$$.721<J_{65536}<.723,\quad .718<H(\log65536)<.720,\quad .002<x_N^*Qx_N<.003.$$

It has both an authenticated author-producer replay and a different full reconstruction by direct polynomial-square integration on all interevent intervals and the stable future. Neither calculation proves the required cofinal signed-work upper bound. This filter differs from [the simple coherent-channel filter](OPERATORS.md#coherent-source).

See [exact work law](../../../standalone/2026-09-06-astra-mobius-work-resonance/WORK_IDENTITY.md), [boundary resonance](../../../standalone/2026-09-06-astra-mobius-work-resonance/RESONANCE.md), and [complete numerical evidence](EVIDENCE.md#work).

<a id="receipt-repair"></a>
**Current receipt contract (R06).** The original producer's `json.loads(...) == result` path accepts duplicate keys and some Boolean/float aliases. This is not evidence that its numerical bounds are wrong. For selected acceptance use the preserved [strict source-pinned replay wrapper](../../../reviews/2026-09-08-postintegration/pass4/replay.py), not a claim that the author's old CLI is type-strict. The wrapper checks the exact consumed source bytes and typed receipts before fresh full reconstruction. Original source and [parser-probe evidence](../../../reviews/2026-09-08-postintegration/pass4/evidence/mw-original-parser.json) are preserved separately.

## 6. Useful failed mechanisms and the next estimate

Nearby positive sources can agree on any fixed horizon and finitely many exact safe coefficients while acquiring additional inner zeros. Their generated projections can converge strongly on each fixed test but stay distance one apart in operator norm. The construction changes the infinite arithmetic source; it does not exhibit an off-line zeta zero. See [late-tail perturbations](../../../standalone/2026-09-08-astra-late-tail-zero-insertion/PROOF.md).

Likewise, nearby damping may enlarge a source domain, the simplest corresponding output rule need not be contractive, and a fixed controller can fail on iteration. The [damping analysis](../../../standalone/2026-09-06-astra-domain-cutoff/TAIL_AND_DAMPING.md) and [fixed-controller obstruction](../../../standalone/2026-09-07-astra-feedback-and-conditioning/PROOF.md) retain the stated source and controller classes. They do not rule out horizon-dependent controllers or unbounded-input approximation.

**Useful next task:** establish an upper estimate for the actual intrinsic defect or growing-horizon output error, using the unmodified infinite arithmetic identity. Another finite conditioning improvement, without target alignment, does not supply that estimate.
