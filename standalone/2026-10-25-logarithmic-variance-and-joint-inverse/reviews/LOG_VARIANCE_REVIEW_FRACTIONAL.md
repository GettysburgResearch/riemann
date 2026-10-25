# Independent analytic review: logarithmic-variance selector

Date: 25 October 2026.
Reviewer: `/root/fractional_global`, independent of the author of the reviewed theorem.

## Reviewed object and verdict

Reviewed file:

`third-pass/root/LOGARITHMIC_VARIANCE_SELECTOR.md`

Reviewed SHA256:

`e7910ca304881bf384c1b1a3781eb486b2c803446a313e3475242a7d871265c3`

**Verdict: the two analytic implications are supported by the supplied proofs, with the stated imported source dependencies. No mathematical blocker found at this hash.** This approves the conditional component, not the existence of the selector family and not an unconditional RH result or a new zero-free region.

The reviewed statements are:

1. Exact legal full-matrix resolvents at `N_a = ceil(4a log a)`, whose signed real-zero variance is at most `a/(10 log a)` for every sufficiently large integer `a`, have shifts tending to zero and imply RH.
2. An eventual uniform lower bound for the exact even finite compressions on that same integer schedule implies RH.

The source-specific all-scale variance inequality is not proved. The cosine-power example establishes compatibility with the function space, not the resolvent equation. Nothing in this review changes those boundaries.

## What was independently inspected

I read the entire reviewed file, the companion `SIGNED_GAUSSIAN_SELECTOR.md`, the full browsable source proof in PR #1017 at `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, and the theta-source note at PR #1021's cited source identity. I also opened the primary articles and checked the actual statement and matrix-class requirements of Connes--van Suijlekom, Theorem 5.6, and the full Weil form in Connes--Consani--Moscovici, equation (3.19).

Primary sources inspected:

- Connes--van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, [arXiv:2511.23257v1](https://arxiv.org/html/2511.23257v1), Sections 4--5, especially equation (11), Remark 4.3, and Theorem 5.6.
- Connes--Consani--Moscovici, *Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1), equation (3.19).

The review consists of analytic checks, source-scope checks, and file hashing. No numerical eigenvalue, finite variance sample, directed-arithmetic certificate, or asymptotic fit was used.

## 1. Full legality and the real-zero input

The new explicit rank-one paragraph correctly reduces the resolvent to the imported finite theorem. If `A=T_a-kappa_a I>0` and `c=<1,A^{-1}1>^{-1}`, then

\[
 A-c|1\rangle\langle1|\ge0,
 \qquad
 \ker(A-c|1\rangle\langle1|)=\mathbb C A^{-1}1.
\]

This follows from Cauchy--Schwarz in the `A` inner product, with equality precisely in that line. The kernel is even and real. The identity shift and the constant convolution kernel preserve the distribution-matrix class used by Theorem 5.6. Translation from the centered interval to the primary source's interval only rephases the Fourier basis by `(-1)^n`; it preserves this even-kernel conclusion and the real-zero conclusion for the transform.

The full minimum, including the odd block, is essential to this step. The reviewed theorem uses that minimum. It does not substitute even-only legality or generic positive-definite matrix reasoning.

## 2. Compulsory zeros and the polynomial variation bound

The paired Hadamard product is justified for these normalized even entire functions of exponential type. Pairing the opposite real zeros cancels the genus-one exponentials. The remaining zero-free factor is `exp(A+Bz)`; normalization and evenness make it one. In particular,

\[
 V=2\sum_j t_j^{-2}\ge0.
\]

Fourier orthogonality gives exact zeros at every `m*pi/a` with `|m|>N`. Removing one copy of each compulsory pair leaves a locally convergent paired product with reciprocal-square sum `(V-V_tail)/2`. This does not assume that the compulsory zeros are simple; any extra multiplicity stays in the remaining product.

Inside the first compulsory zero, the tail product is positive and satisfies

\[
 P_{a,N}(t)\le e^{-V_{\rm tail}t^2/2},
 \qquad
 |H(t)|\le e^{(V-V_{\rm tail})t^2/2}.
\]

Thus the coefficient `V-2 V_tail` in equation (7), rather than `V-V_tail`, is correct. The integral estimate

\[
 \sum_{m>N}m^{-2}\ge\frac1{N+1}
\]

makes condition (8) sufficient to bound every retained Fourier sample by one. The exact trigonometric coefficients are `F(n*pi/a)/(2a)`, so the displayed `L^1` bound `2N+1` follows without a physical sign hypothesis.

The ceiling estimate in (10) is also correct. The limiting constants are `2/5` and `4/pi^2`, with a strict favorable gap. The cosine-power gamma formula and its variance are consistent with the same normalization. Its variance is about `(5/pi^2) M_a`, so the target lies above the compulsory-zero floor; this does not establish that a legal resolvent attains it.

## 3. Signed overlap and growing-Gaussian uniformity

The bounds in (13) follow directly by estimating and expanding the paired product. For real `t`, both `F_a(t)` and the theta transform `X(t)` are real. Since `|X(t)|<=1` and `X(t)>=1-V_X t^2/2`, the lower bound used in (14) is valid even when `F_a` or `X` is negative. Its Gaussian integration gives exactly

\[
 \frac{2-\sqrt2-V_X/(4M)}{2\sqrt{\pi M}}.
\]

The assumption `M>=V_X` gives the stated positive constant times `M^{-1/2}`. Thus this is an actual positive source overlap for a possibly signed `f_a`.

The growing smoothing parameter does not create a hidden exponential constant in (15). With fixed `d_0<d_1<1/4`, the Gaussian derivative is bounded by a slightly weaker Gaussian uniformly for `M>=1`. Completing the square leaves a factor `exp(C_1 y^2/M)`, bounded under integration by the single fixed theta moment with `M=1`. This verifies the claimed uniformity.

For the stated schedule,

\[
 \frac{a^2}{M}=10a\log a,
 \qquad
 \frac{M\pi^2N_a^2}{a^2}
 \ge\frac{4\pi^2}{25}\frac{a^2}{M}.
\]

The second exponent is strictly larger than `d_0 a^2/M`. Gaussian tail sums with one derivative introduce only fixed powers of `a`; the periodization copies are uniformly summable because `a^2/M` tends to infinity. The zero Fourier coefficient before endpoint subtraction is exactly the total mass one, so the normalizing mass tends to one after subtraction.

The broad comparator remains a source null function. Young's inequality gives its `L^2` norm squared at most `C/a` uniformly in `M`, because the Gaussian-smoothed theta density has mass one. Its boundary clearance is `a/2`, explaining the factor `1/4` in the comparator's physical exponent. These constants cannot simply be imported from a fixed-`M` argument, but the reviewed proof supplies the necessary uniform estimates.

## 4. Endpoint correction and the complete source

An even trigonometric polynomial has derivative zero at both endpoints. Subtracting its common endpoint value therefore makes its zero extension `C^1`. These functions belong to the full interval operator domain: their Fourier decay is enough for the logarithmic multiplier in `L^2`, and the other fixed-interval terms are bounded. The use of `q_a(f,v_a)=<f,A_a v_a>` is consequently legitimate even when the first argument is only in the form domain.

The weighted global error (17) follows both inside and outside the interval. Outside, the maximum of `-d_0 x^2/M+2|x|` is at the boundary eventually because `a/M=10 log a`. The corresponding statement for the broad comparator uses `-d_0(|x|-a/2)^2/M+2|x|` and has the same property.

The complete residual lemma retains every term of the actual source. The local archimedean bracket is `O(Bt)`, canceling its `1/t` kernel; the distant part is integrable. The pole term costs at most `C B exp(|x|/2)`. Each prime term is bounded using

\[
 e^{-2|x\pm\log n|}\le e^{2|x|}n^{-2},
 \qquad
 \sum_{n\ge2}(\log n)n^{-5/2}<\infty.
\]

In particular, no replacement by a finite zero census or an unsigned prime approximation occurs. The full-line null identities may be convolved with the Gaussian and with the compact broadening kernel: for each fixed parameter their absolute source integrals converge, so the exact cancellation is legitimate. The growing-parameter estimates are then obtained separately from (15)--(18).

The principal residual rates are polynomial factors times

\[
 e^{-(49/20)a\log a+4a}
 \quad\hbox{and}\quad
 e^{-(49/80)a\log a+4a}.
\]

They remain negligible after multiplication by `2N_a+1`, by `a`, or by `sqrt(M)`. This confirms both lines of (21) and the final smallness assertions in (22).

## 5. The legal-shift comparison

The mass-constrained minimum in (23) has value exactly `c_a`; expansion around `f_a` has zero cross term for every mass-zero perturbation. Pairing the finite equation with the mass-one `v_a` therefore gives (24) with the stated sign.

For negative shifts, the overlap is at least `c_*/(2 sqrt(M))`, whereas the broad comparator costs `C/a` in squared norm. The first term dominates because `sqrt(M)/a` tends to zero. Multiplying the residual inequality by `sqrt(M)` proves that the negative shifts tend to zero. For nonnegative shifts, mass one gives the lower norm bound `||w_a||_2^2>=1/(2a)`; legality and its Rayleigh quotient give (26). If its Rayleigh quotient were negative, this case could not occur, so there is no sign reversal in that division.

It follows that the full finite minima, and hence the even minima, are eventually bounded below by a fixed constant. No continuum lower bound is inferred from a finite minimum.

## 6. Fixed double-exponential test and finite consumer

The fixed choice `G(z)=exp(1-cosh(z/10))` is nonvanishing. Shifting the inverse Fourier contour by `+/-12i` is legitimate: throughout the strip used to close the contour, `cos(Im(z)/10)` stays positive. The shifted integrals with any fixed polynomial weight are finite. Thus all fixed derivatives of `g` have the asserted `exp(-12|x|)` decay.

For `a=ceil(t)`, both translates have boundary clearance at least `a/2`. Their physical approximation errors are `O(exp(-6a))`; multiplying by the residual weight gives `O(exp(-4a))`. The Fourier tail starts beyond a frequency satisfying

\[
 e^{\pi N_a/(10a)}\ge a^{2\pi/5}.
\]

Since `2*pi/5>1`, its double-exponential bound beats the fixed exponential growth of the full-source residual. The repaired equation (31) correctly **adds** the physical and Fourier errors. After multiplication by `exp(2a)` in (32), the two errors still tend to zero. The `L^1` and `L^2` bounds are uniform in the translated center.

The zero-side formula has the correct square, `G(z_rho)^2`, for the real even test, rather than an absolute square. Indeed its transform is `2G(z)cos(zt/2)`; expansion and the symmetry `z_rho -> -z_rho` give (33). On the unconditional critical strip, the coefficients decay doubly exponentially in `|gamma|`, so the zero count justifies the stated convergence and Laplace interchange. The compact-test explicit formula extends to this test by the source and transform decay estimates.

The Laplace argument is sound. Adding a constant makes `C_g(t)` nonnegative under the hypothesized uniform finite lower bound. Its convergence abscissa is finite above, since `|C_g(t)|<=C exp(t/2)`. A positive finite abscissa would be a real singularity by the elementary nonnegative-Laplace argument, but the normally convergent meromorphic expression has no positive real pole. Hence the integral is holomorphic in `Re(w)>0`. A zero with `beta>1/2` produces there a pole of residue `m_rho G(z_rho)^2`, which cannot vanish or cancel against a different zero. This proves the finite consumer as stated.

## 7. Repairs and approval boundary

An earlier draft, SHA256 `709c47151291ed2ae88de811e9bb6571fcdf757cf95fcb8ee4e801c08d13484e`, omitted the plus sign between the two bounds in (31). A product of those errors would not be justified. The reviewed hash repairs that issue and adds the explicit finite rank-one reduction. Neither earlier bytes nor any subsequent changed file are approved by this hash-bound review.

The accepted contribution is a new conditional analytic criterion at a coupled mode/variance schedule, together with its finite spectral consumer. The unresolved condition concerns the actual exact full-matrix resolvents for every sufficiently large integer scale. This review supplies no estimate proving that condition, no monotonicity in the legal shift, and no finite-to-infinite extrapolation.
