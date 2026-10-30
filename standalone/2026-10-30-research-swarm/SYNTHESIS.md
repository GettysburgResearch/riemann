# Synthesis and next mathematical targets

Status: **EXPLORATORY SYNTHESIS**, 2026-10-30. The proofs and limitations are in the linked lane reports. This file does not promote any lane to a proof of RH or a new zero-free boundary.

## 1. Main constructive lead: an arithmetic detector with its actual main term removed

For all characters modulo q, including the imprimitive Euler factors, set

$$
D_q(s)=\sum_{\chi\bmod q}\frac{L_q'}{L_q}(s,\chi),
\qquad T_Q(s)=\frac1{Q-1}\sum_{q=2}^{Q}D_q(s).
$$

Character orthogonality gives the exact source

$$D_q(s)=-\varphi(q)\sum_{n\equiv1\pmod q}\Lambda(n)n^{-s},\qquad \Re s>1.$$

Every nontrivial zeta zero is a pole of each D_q with positive integer residue. Averaging does not dilute its principal-character contribution: it remains at least its zeta multiplicity. This is the useful feature of the construction. A reciprocal product can have an uncontrolled residue size; the logarithmic derivative has a residue fixed by multiplicity. The [parent arithmetic report](arithmetic/report.md) proves this and gives exact conductor accounting.

The natural cumulative source is

$$\Psi_Q(x)=\frac1{Q-1}\sum_{q=2}^{Q}\varphi(q)\psi(x;q,1).$$

The naive cutoff model, averaging (x−q)_+, is wrong by order Q already when x is a fixed multiple of Q. Divisor switching identifies the missing deterministic contribution. Define

$$
A=\prod_p\left(1-\frac1{p(p-1)}\right),\qquad
C(k)=A\prod_{p\mid k}\frac{p^2-1}{p^2-p-1}.
$$

The independently reviewed fixed-scale limit is

$$
\frac{\Psi_Q(uQ)}Q\longrightarrow
P(u)=\frac12\left[u^2-\sum_{k<u}C(k)\left(\frac{u^2}{k^2}-1\right)\right].
$$

It is uniform for u in each fixed compact interval. The weighted-prime lemma behind C(k) uses classical fixed-progression PNT and Brun–Titchmarsh. The Artin constant is an unconditional average here, not an invocation of the primitive-root conjecture. The [profile report](arithmetic/progression_profile.md) supplies a self-contained derivation and the bounds justifying the divisor truncation.

For 1<u<2, P(u)=((1−A)u²+A)/2. At u=1+A its difference from the naive limit u−1/2 is −A²(1+A)/2. Thus the correction addresses a proved main-term error, not merely a better numerical fit.

Its Mellin transform is explicit. Put

$$
\mathcal C(s)=A\zeta(s)\prod_p\left(1+\frac{p^{1-s}}{p^2-p-1}\right),
\qquad
C_Q^*(s)=\frac{Q^{1-s}\mathcal C(s)-Q^{-1}}{2-s}.
$$

The auxiliary product converges absolutely in Re(s)>0. The two identities Res_1 C=1 and C(2)=1 cancel the known pole of T_Q at 1 and the apparent singularity at 2. No reciprocal-zeta factor is introduced. Therefore

$$R_Q^*(s)=T_Q(s)+C_Q^*(s)$$

is regular at 1 and retains every positive zero residue. Its exact source, initially in Re(s)>1, is

$$
R_Q^*(s)=-s\int_1^\infty
\left[\Psi_Q(x)-QP(x/Q)+\frac1{2Q}\right]x^{-s-1}\,dx.
$$

### The precise open gate

For a suitable contour enclosing a domain U inside Re(s)>0 and excluding 1, the compensator has zero contour integral, while the argument principle gives

$$
\frac1{2\pi i}\oint_{\partial U}R_Q^*(s)\,ds
=N_\zeta(U)+\sum_{d=2}^{Q}\frac{\lfloor Q/d\rfloor}{Q-1}N_d^*(U)
\ge N_\zeta(U).
$$

Here N_d^* counts the zeros of the primitive conductor-d family, with multiplicity; endpoints and boundaries must avoid poles. A bound strictly below one would exclude a zeta zero in U. No such bound is proved in this packet.

There are two reasons the fixed-scale theorem is insufficient. First, an o(Q) source error on a fixed-ratio block gives only o(Q^(1−sigma)) after Mellin weighting; this need not vanish for sigma<1. Second, it does not control the unbounded x/Q tail. Analytic continuation of the integral cannot be assumed from a limit proved in its absolute convergence half-plane. Family zero-density estimates also cannot discard the N_zeta term, whose coefficient is exactly one.

The priority is to estimate this corrected error with all endpoint and growing-ratio ranges retained. A successful estimate would exploit arithmetic beyond the classical main term. The explicit correction makes that obligation sharper, but does not pay it.

The [continuation note](arithmetic/normality_gate.md) gives a rigorous sufficient package for an alternative route: bounded total positive residue mass, a locally bounded holomorphic regular part after subtracting every pole in a disk, and a bounded unweighted Blaschke budget. Pole-clearing then permits a holomorphic subsequence argument and a positive-residue contradiction. None of these bounds is asserted for the target strip. Explicit examples show why pole counts do not control the regular part, and why bounded weighted pole mass does not prevent many small-residue poles from destroying continuation. Moreover, forcing the detector to zero would exclude every fixed-conductor Dirichlet zero in the disk; it is a stronger target than the original zeta-only contour threshold below one.

## 2. Factor removal: a local inequality with a global obstruction

Let p be the normalized reciprocal-xi density, so its bilateral Laplace transform is Xi(0)/Xi(s). Removing a real-zero pair at ±a acts on a density through

$$\mathcal D_a f=f-a^{-2}f''.$$

If f is even, positive and log-concave, with logarithmic tail slope −a, this operation preserves nonnegativity. Iteration requires more. With h=\mathcal D_a f>0, exact differentiation gives

$$
-(\log h)''=
\frac{(a^2f'-f''')^2-(a^2f-f'')(a^2f''-f'''')}
{(a^2f-f'')^2}.
$$

The numerator is a concrete fourth-order sign to control from the actual reciprocal-xi source. This is more useful as a research target than simply restating an all-minors positivity criterion. It still requires a proof for every removal and every real x.

The [positivity report](positivity/report.md) derives a finite closure result from Suvrit Sra's author-site v2 of 29 October 2026. Under its finite-verification inputs, deleting all verified real-zero factors through U/8 leaves a positive analytic strictly log-concave density. At U=3×10^12 that is deletion through 3.75×10^11. This is an extension of a cited mechanism, not a new zero verification.

A [second derivation](positivity/NEAR_CUTOFF_REMOVAL.md) sharpens the finite statement: for 10^6<=U<=3×10^12, deletion through V<=U−70 preserves an entire positive strictly log-concave density. At the supplied verified height, V may therefore reach 2,999,999,999,930. The proof constructs a positive bilateral Lévy residual directly, retains two zero factors with an explicit gap, and bounds every needed exponential tilt. It does not assume the one-sided residual clock remains positive, and does not invoke Sra's retained-zero theorem outside its stated range. The more general retained-gap criterion explains how the buffer grows like log(U) for other large verified heights. This is still a finite source-qualified corollary, not a continuation beyond the verification boundary.

An exact countermodel shows why shape and approximation alone cannot supply an infinite induction. Start with

$$h(x)=\frac{e^{-|x|}}{10}(4-\cos|x|+3\sin|x|),
\qquad \mathcal Lh(s)=\frac4{(1-s^2)(s^4+4)}.$$

Convolving h with a sufficiently broad Laplace density gives strict log-concavity and an arbitrarily small total-variation distance from a PF-infinity density. Removing the broad Laplace factor recovers h, which is not log-concave; the next removal becomes negative. The report also constructs an analytic smoothing with an entire order-one reciprocal while retaining the failure. The model does not claim the actual xi arithmetic, Sra's full PF_256 hypothesis, or all of xi's spectral data.

Thus the next viable attack is a source-specific invariant forcing the displayed fourth-order numerator to remain nonnegative after successive removals. A generic theorem based only on the properties in the countermodel is false. A cofinal positivity theorem would reach RH by the nonnegative-power-series boundary argument; the cofinal statement is exactly what has not been proved.

The [Gaussian posterior note](positivity/GAUSSIAN_POSTERIOR.md) supplies an alternative exact coordinate system for this invariant. If U=1/(4S) is the inverse variance of the reciprocal-xi Gaussian clock, then minus log-curvature is 2 E_x(U)−4x² Var_x(U). The removal expression is an explicit polynomial in the first four posterior moments. Ordinary moment positivity gives lower variance bounds, while this target needs an upper bound. The note also shows that the apparent posterior reweighting changes sign; a positive one-sided clock cannot be assumed after the bilateral near-cutoff construction.

## 3. Dynamics: the integration constant contains missing information

The [dynamics report](dynamics/report.md) studies

$$G_C(w)=C+2\sqrt w\sinh\sqrt w-2\cosh\sqrt w+2.$$

It is entire of order one half, has positive Taylor coefficients, and G_C'=cosh(sqrt(w)) has only negative real zeros. Every further derivative lies in the Laguerre–Pólya class. Yet for pi−2<C<5pi−2, G_C has exactly one nonreal conjugate pair. In the even order-one variable this is one off-axis quartet.

The construction can move that quartet arbitrarily high and arbitrarily close to the line, prescribe any finite list of lower real zeros, and retain real-rootedness of all sufficiently high derivatives. It therefore exposes a specific failure of downward reconstruction from high derivatives. Its finite exponential type and missing xi source are explicitly excluded from the comparison.

For a derivative whose critical points are real, reconstructing a real-rooted antiderivative requires the integration constant to lie in the intersection of the critical-value intervals. The packet derives this exact gate and an explicit Jensen-degree threshold. For the rational choice C=6/5, exact Sturm arithmetic finds all real roots through degree 17, but only 16 real roots at degree 18. The asymptotic model detection degree grows like T²/(4 delta²), so a high, narrow defect can evade extensive finite testing.

The polynomial heat model also gives an exact density-assisted collision time a²/(4m+2). This is a forward-flow statement; it supplies no reverse inference that the unsmoothed source began with real zeros.

The useful next target is the actual xi integration constant at every relevant critical-value gate, derived from its arithmetic or theta representation. Repeating high-shift hyperbolicity checks does not settle that missing information.

## 4. Heat trace: retain the method, withdraw the frontier claim

The root calculation proves a uniform saddle estimate for all high derivative orders at small positive time, and a finite all-time range using a retained verified zero. Three independent reviews found no blocking defect under its stated inputs.

However, the pinned Polson–Sokolov book source already asserts the same signs over a much larger range. The [current heat-trace status](heat_trace/README.md) records the exact theorem and normalization comparison. This appendix is retained for its independent argument, not promoted as a new result frontier.

A separate analytic countermodel in the [dynamics heat review](dynamics/REVIEW_HEAT_TRACE.md), f(t)=1/t+e^(−t)cos(t), has every alternating derivative positive on a short interval, and both f and −f' positive at all positive times, but fails a later derivative sign. It makes the local/global quantifier gap explicit.

## 5. Research decision

The arithmetic correction is the first follow-up target because it removes a concrete, proved obstruction in the proposed main term while preserving the zero signal. The factor-removal inequality is a second independent target with a clear source-specific hypothesis to attack. The dynamics packet is an obstruction and a diagnostic: any descent argument must exhibit the integration-constant information its countermodel lacks.

The evidence does not justify a new zero-free endpoint, a global positivity claim, or a statement that these mechanisms are unprecedented. It does justify a reviewable set of formulas, proofs, failed shortcuts, and exact next estimates, with independent checks and reproducible finite experiments.
