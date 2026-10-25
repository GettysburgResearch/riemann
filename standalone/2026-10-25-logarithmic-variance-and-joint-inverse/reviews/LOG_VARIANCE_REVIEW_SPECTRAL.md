# Independent review of the logarithmic-variance selector extension

Reviewer: `/root/spectral_floor`.
Date: 25 October 2026.
Reviewed object: `third-pass/root/LOGARITHMIC_VARIANCE_SELECTOR.md`.
Exact reviewed file SHA256: `e7910ca304881bf384c1b1a3781eb486b2c803446a313e3475242a7d871265c3`.
Disposition: **PASS as a proposed conditional analytic component, relative to the explicitly pinned complete-source, theta-null, and finite real-zero inputs. No actual all-scale selector bound or new zero-free region is certified.**

This reviewer authored the companion fixed-variance note, but did not author the compulsory-tail improvement or the logarithmic-cutoff extension reviewed here. The review checks the extension and its composition with that companion argument. It is a file-hash review, not a claim that an as-yet-uncreated integration commit has received independent review.

## 1. Scope of the result actually checked

The principal statement concerns the exact full trigonometric compression of the complete Weil form, with

\[
N_a=\lceil4a\log a\rceil,\qquad
M_a=\frac{a}{10\log a},\qquad
\kappa_a<\min\operatorname{spec}(T_a)
\]

for every sufficiently large integer \(a\). The full minimum includes both parity blocks. The additional hypothesis is the signed second-moment bound \(-F_a''(0)\le M_a\) for the normalized actual resolvent to the constant forcing. The conclusion is \(\kappa_a\to0\), followed by RH through a separately proved finite-matrix consumer.

The proof never substitutes a finite minimum for a continuum lower bound. It does not assume physical nonnegativity of the selected density, convergence of its transform to Xi, or positivity of a numerical quadrature matrix. Its unproved hypothesis remains explicitly source-dependent and cofinal.

## 2. Finite real zeros and their compulsory subset

The added source-reduction paragraph was checked. For
\(A=T_a-\kappa_a I>0\) and
\(c=\langle1,A^{-1}1\rangle^{-1}\), Cauchy--Schwarz in the \(A\) norm proves
\(A-c|1\rangle\langle1|\ge0\), and equality holds precisely on the span of \(A^{-1}1\). Reflection invariance makes this kernel even. The identity shift is a delta convolution, while the rank-one subtraction is a constant convolution kernel. They retain the distribution-matrix class required by the imported Connes--van Suijlekom Theorem 5.6, as already authenticated in pinned PR #1017. Full-block legality is retained in this argument.

Fourier orthogonality forces the zeros \(m\pi/a\) for every integer \(|m|>N_a\). The paired Hadamard factorization is valid because the transform is an even, normalized entire function of exponential type with only real zeros. Removing one copy of each compulsory pair gives a remaining product of variance \(V-V_{\rm tail}\ge0\), with no additional Gaussian exponential factor: each original transform has order at most one, and evenness eliminates its possible linear exponential factor.

On \(|t|<(N+1)\pi/a\), the compulsory product is positive and has logarithm at most \(-V_{\rm tail}t^2/2\). Multiplying its estimate by that for the remaining product gives the correct coefficient

\[
\frac{V-2V_{\rm tail}}2,
\]

not \((V-V_{\rm tail})/2\). The factor of two is the useful gain. The condition
\(V\le4a^2/[\pi^2(N+1)]\) therefore bounds every retained Fourier sample by one. It is used only at retained samples, within the stated interval, not beyond the compulsory product's first zero. The resulting \(L^1\) bound is exactly \(2N+1\).

For the stated schedule,

\[
\frac{M_a(N_a+1)}{a^2}
\le\frac25+\frac1{5a\log a}<\frac4{\pi^2}
\]

eventually. For example, the last inequality follows once
\(a\log a>\pi^2/[2(10-\pi^2)]\). The strict limiting margin is positive.

The normalized cosine power has transform
\(\Gamma(N+1)^2/[\Gamma(N+1+az/\pi)\Gamma(N+1-az/\pi)]\), hence exactly the compulsory product. Its variance is at most
\((5/\pi^2)M_a<M_a\). This authenticates structural compatibility, while the text correctly avoids calling it a source resolvent. In particular this schedule is not ruled out by the compulsory-zero variance floor.

## 3. Uniform Gaussian overlap and complete residuals

The signed overlap bound was recomputed. From the paired product,
\(|F(t)-1|\le e^{Mt^2/2}-1\). For the actual positive theta density,
\(|X(t)|\le1\) and \(X(t)\ge1-V_Xt^2/2\). Integration against \(e^{-Mt^2}\) gives

\[
\langle f,\phi*G_M\rangle
\ge\frac{2-\sqrt2-V_X/(4M)}{2\sqrt{\pi M}}
\ge\frac{7/4-\sqrt2}{2\sqrt{\pi M}}>0
\]

when \(M\ge\max(1,V_X)\). This condition holds eventually for \(M=M_a\). No inference of physical positivity from real Fourier zeros is made.

The constants in the physical Gaussian tail estimate are uniform for \(M\ge1\). Completing the square gives the factor \(e^{C y^2/M}\), which is bounded by \(e^{C y^2}\) and is theta-integrable. The fixed exponent gap below \(1/(4M)\) absorbs the first Gaussian derivative with a uniform constant. This avoids hiding an exponentially growing moment constant in the moving-smoothing argument.

At the stated cutoff, the Fourier Gaussian exponent is at least
\((4\pi^2/25)a^2/M\), strictly larger than the chosen physical exponent \((49/200)a^2/M\). Periodization, endpoint-value subtraction, and normalization therefore have the displayed errors, up to fixed polynomial factors. The normalizing mass is one minus twice the half-width times the exponentially small endpoint value. The even trigonometric derivative already vanishes at the endpoints; subtraction makes the value vanish too. The zero extension is \(C^1\) and is in the actual logarithmic operator domain.

The outside weighted envelope requires the maximum of
\(-d_0x^2/M+2|x|\) on \(|x|\ge a\) to occur at the boundary. This is valid here because \(a/M=10\log a\to\infty\). The same check for the broad comparator uses its shifted Gaussian distance \(|x|-a/2\), and holds for the same reason.

The complete residual lemma is correct term by term. Its prime estimate uses the absolutely convergent series \(\sum(\log n)n^{-5/2}\), including every prime power; its archimedean singularity is canceled by the \(C^1\) bracket; its pole term is retained. No variable \(M\) enters its constant. Hence the polynomial bound \(\|f_a\|_1\le2N_a+1\) makes the tight residual pairing negligible relative to \(M^{-1/2}\). The broad comparator has \(L^2\) norm squared \(O(1/a)\), and its residual beats both required factors \(a\) and \(\sqrt M\).

## 4. Variational step

The exact finite equation and the mass-one minimum follow from positive definiteness of \(T_a-\kappa_a\). The negative-shift argument has bracket

\[
\frac{c_*}{2\sqrt M}-\frac Ca
\ge\frac{c_*}{4\sqrt M}>0
\]

eventually, because \(\sqrt M/a\to0\). Both error terms vanish after multiplication by \(\sqrt M\), proving convergence of the negative shifts to zero. For nonnegative shifts, mass one gives \(\|w_a\|_2^2\ge1/(2a)\), and the broad Rayleigh bound proves their convergence to zero. The even finite minimum is consequently uniformly bounded below. This is the only spectral input passed to the next section.

## 5. The logarithmic-grid zero detector

The fixed entire function
\(G(z)=\exp(1-\cosh(z/10))\) never vanishes. Its restriction to the lines \(\Im z=\pm12\), multiplied by any fixed polynomial, is integrable because \(\cos(6/5)>0\). The contour shift proving
\(|g^{(j)}(x)|\le C_j e^{-12|x|}\) is therefore valid, including the vanishing vertical closing segments. Its inverse Fourier transform is real and even; its possible physical sign changes are harmless.

With \(a=\lceil t\rceil\), the two centers \(\pm t/2\) have distance at least \(a/2\) from the boundary. Physical copies and the omitted tails cost \(O(e^{-6a})\). At \(N_a=\lceil4a\log a\rceil\), the Fourier tail costs
\(a^C\exp(-\tfrac14a^{2\pi/5})\). The inequality \(2\pi/5>1\) makes it smaller than every fixed exponential. After the weighted-envelope factor \(e^{2a}\), the residual bound is

\[
B_{a,t}\le Ce^{-4a}+Ca^C e^{2a-a^{2\pi/5}/4}.
\]

The sum is essential. The initially reviewed draft omitted its plus sign; the author repaired it before the exact hash recorded above. The complete form error is \(O(B_{a,t}e^{2a})=o(1)\). This transfers the uniform finite lower bound to the whole-line two-bump correlation for every real \(t\), avoiding an integer-sampling or aliasing inference.

On the unconditional zero strip,
\(|G(z_\rho)|\le\exp(1-\cos(1/20)\cosh(\gamma/10))\). Thus the zero series and the meromorphic Laplace series converge normally in precisely the regions stated. The compact explicit formula extends to this test: smooth cutoffs preserve uniform rapidly decreasing Fourier bounds on \(|\Im z|\le1/2\), while the physical exponential tails dominate the full source's growth.

The one-sided lower bound makes \(C_g(t)+C'\) nonnegative. Landau's real-abscissa argument then places its Laplace convergence abscissa at most zero, since the continued transform has no positive real pole. Every hypothetical zero to the right of the critical line supplies a distinct pole with nonzero residue \(m_\rho G(z_\rho)^2\). Multiplicities cannot cancel it. This proves the conditional consumer as written.

## 6. Boundaries of the review

No all-scale variance estimate for the actual source resolvents was found or inferred during this review. Neither the cosine-power witness, the complete-source null competitors, nor a finite numerical matrix calculation supplies it. The imported finite real-zero theorem and theta source facts remain explicit dependencies; their entire upstream frameworks have not been independently re-proved here.

The reviewed result is a substantive weakening of a sufficient selector hypothesis and a smaller cofinal cutoff. It is not an unconditional lower spectral bound or a newly established zero-free region. The companion prime-discrepancy lower estimate is a separate actual source estimate and does not discharge this selector hypothesis.
