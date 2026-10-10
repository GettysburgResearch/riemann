# Quasi-Riemann: a rational refinement and a precise height-local target

**Status: proposed research; a completed conditional corollary of imported analytic results, proved component lemmas, and explicitly open stronger estimates.**

This packet continues the [complete OpenAI source import](../2026-10-07-openai-quasi-riemann-import/README.md). It develops the request to lower the zero-free constant and to make the possible zero band narrow with height. It is not part of the accepted integrated record. RH remains unproved here.

The clearest numerical result of this pass is the following **conditional deduction from the imported analytic machinery**:

\[
\boxed{\quad
\zeta(s)\ne0\quad\text{when}\quad
\Re s>\frac{139999}{160000}=0.87499375.
\quad}
\]

The same deduction covers every Dirichlet L-function and the source's finite-order Hecke family, with principal poles allowed. The proof uses the existing moments; it adds no hypothetical fourth-moment premise. Its new adapters and parameter calculation received a scoped independent source review. The full imported analytic proof has not been independently reverified, and this new deduction has not been formalized or built in Lean.

The improvement is exactly \(1/160000\) below \(7/8\). It is modest. The height-local and higher-moment results below identify substantially stronger targets without claiming that they have been attained.

## Read the work

| Result or question | Complete account | Status |
|---|---|---|
| Why the constant can move slightly below \(7/8\) | [Geometric perturbation](GEOMETRY_PERTURBATION.md) | Complete deduction conditional on the listed imported analytic inputs; no new moment assumption |
| Why tuning the same geometry cannot produce a dramatic gain | [Exact envelope limit](GEOMETRY_ENVELOPE_LIMIT.md) | Exact algebraic obstruction for the specified sufficient envelope |
| A genuine finite detector at a chosen height, and the remaining signed sum | [Native height proof](NATIVE_HEIGHT.md) | Proved finite identities, classical mean-square consequence, local peak theorem and shrinking-strip diagonal bound |
| What height does to the imported transform, and what higher moments would imply | [Height and moment analysis](UPSTREAM_HEIGHT_AND_MOMENTS.md) | Completed-transform deduction and conditional extraction theorem; stronger moment open |
| A smaller coefficient problem sufficient for the fourth moment | [Squarefree fourth-moment reduction](FOURTH_MOMENT_REDUCTION.md) | Exact gcd decomposition, harmonic-cost reduction and all-moment diagonal count; mean-square target open |
| The actual auxiliary L-factor and exact tail-zero criteria | [Euler factorization and tail criteria](TAIL_AND_EULER.md) | Local analytic and meromorphic reductions; tail cancellation open |
| Whether a causal inverse can remove that auxiliary factor for free | [Causal auxiliary-factor calculation](CAUSAL_AUXILIARY_FACTOR.md) | Exact operator and weighted cost; stronger angular cancellation conditional |
| What was independently checked and what was not | [Review](REVIEW.md), [validation](VALIDATION.md), [provenance](PROVENANCE.json) | Scoped evidence, with source and content hashes |

## 1. The small numerical improvement is a direct-estimate improvement

The published compensated geometry has total prime-slot length \(\ell=1/6\), imbalance \(b=1/8\), and structural relations

\[
l_x=\frac{1-\ell-b}{2},\qquad
l_y=\frac{1-\ell+b}{2},\qquad
h=\frac{1+3\ell+b}{2}.
\]

Its principal signal exponent is

\[
C(s)=s+l_x/2-1+h/6=s-\frac{11}{16}
\]

when \(b=1/8\). This exponent is independent of \(\ell\). The direct bound is \(Z^{l_x/2+b/12+\epsilon}\).

Increasing \(\ell\) to \(1/6+1/40000\) therefore lowers the direct exponent by \(1/160000\), while keeping the same affine principal signal. There is a genuine issue to resolve: the published no-loss row bound for every rescaled subset no longer holds. Carrying the changed loss through the complete compensated sum repairs it.

For a subset of total rescaling length \(d\), the corrected row energy costs

\[
Z^{(5\ell-1+d)_+/4}.
\]

After Cauchy–Schwarz and all tuple/rescaling factors, its total extra exponent is

\[
f_\ell(d)=-d+\frac{(5\ell-1+d)_+}{8}.
\]

Its two slopes are \(-1\) and \(-7/8\). Consequently its maximum over \(0\le d\le\ell\) is zero for \(\ell\le1/5\). The final direct estimate survives the parameter change even though a stronger intermediate estimate does not.

The old high-side certificate has uniform margin \(49/440640\). Its derivative with respect to \(\ell\) is at most \(5/2\), so the new tuple retains the exact margin

\[
\frac{49}{440640}-\frac1{16000}
=\frac{1073}{22032000}>0.
\]

The full proof also supplies the enlarged Euler domain, every changed contour interface, fixed \(\kappa=3/4\) reuse of the existing plain moment, the same physical expression on both sides, and the nonzero principal normalizer. A check of the final exponent alone would not have sufficed.

## 2. There is an exact limit to this particular parameter strategy

For the existing balanced row count, the point

\[
x=\frac12,\qquad
\delta=\frac{49-\sqrt{921}}{48}
\]

has row exponent \(R_*=2/3\). At that point the imbalance parameter \(b\) cancels from the high exponent. Uniform strict negativity of the same sufficient envelope requires

\[
\beta_0>
\frac{1507-2\sqrt{921}}{1653}
=0.874957067\ldots .
\]

This is not a limit on the actual zeros or on other methods. It tells us that repeatedly optimizing these two parameters with the unchanged row-count estimate cannot produce a substantial reduction.

The point also identifies a concrete opportunity: the current marginal estimates allow the inverse/plain witness and maximal prime-amplitude configuration to coexist. A stronger estimate for their actual joint arithmetic source could reduce that count. Their coexistence has not been ruled out here.

## 3. The height-dependent program now has an explicit detector

Define finite Dirichlet polynomials

\[
G_Y(s)=\sum_{n\le Y}\mu(n)n^{-s},\qquad
B_Y(s)=\sum_{n\le Y}n^{-s},\qquad
R_Y(s)=G_Y(s)B_Y(s)-1.
\]

Forming the product before estimating it gives exact zero coefficients through \(Y\):

\[
R_Y(s)=\sum_{Y<n\le Y^2}e_Y(n)n^{-s},\qquad
e_Y(n)=\sum_{\substack{ab=n\\a,b\le Y}}\mu(a).
\]

This keeps every divisor collision and its sign. The proof includes a full mean-square bound

\[
\int_T^{T+H}|R_Y(\sigma+it)|^2dt
\ll_\sigma (1+\log Y)^3
\left(HY^{1-2\sigma}+Y^{4-4\sigma}\right).
\]

The stated two-term estimate holds for \(1/2<\sigma<1\).

For a hypothetical zero \(\rho=\beta+iT\), take \(Y=\lceil4(T+2)\rceil\) at positive height. Euler summation, including the pole term, shows

\[
|R_Y(\rho)+1|
\le H_Y\left(\frac{Y^{2-2\beta}}{T}+2Y^{1-2\beta}\right),
\]

where \(H_Y\) is the harmonic number. For sufficiently large \(T\) in the stated strip this is at most \(1/2\). Thus the zero forces \(|R_Y(\rho)|\ge1/2\).

Put \(\Omega=2\log Y\), \(h=1/\Omega\), and

\[
\mathcal E_Y(\sigma;T)=
\int_{T-h}^{T+h}
\left(|R_Y(\sigma+it)|^2+
\Omega^{-2}|\partial_tR_Y(\sigma+it)|^2\right)\,dt.
\]

The proved local Sobolev estimate then forces

\[
\mathcal E_Y(\beta;T)\ge\frac1{6\Omega}.
\]

The complete energy is an exact diagonal plus an off-diagonal:

\[
\mathcal E_Y=\mathcal D_Y+\mathcal O_Y.
\]

For \(a_n=e_Y(n)n^{-\sigma}\), the latter is explicitly

\[
\mathcal O_Y(\sigma;T)=
4\sum_{Y<m<n\le Y^2}
a_ma_n\left(1+\frac{\log m\log n}{\Omega^2}\right)
\cos\!\left(T\log\frac nm\right)
\frac{\sin(h\log(n/m))}{\log(n/m)}.
\]

This is the exact signed source whose additional height cancellation is needed.

### Components already reach a shrinking boundary

For any fixed \(c>2\), let

\[
\sigma_0(Y)=\frac12+c\frac{\log\log Y}{\log Y}.
\]

Uniformly for \(\sigma_0(Y)\le\sigma<1\), the zero-detection error tends to zero and

\[
\Omega\mathcal D_Y(\sigma)
\le\frac{512}{c\log2}\,
\frac{(\log Y)^{4-2c}}{\log\log Y}\longrightarrow0.
\]

Thus a sufficient new theorem would be

\[
\mathcal O_Y(\sigma;T)<\frac1{12\Omega}
\]

for every sufficiently large \(T\) and every \(\sigma\) in the target strip, once the diagonal is at most \(1/(12\Omega)\). It would contradict the local energy forced by a zero.

**That pointwise off-diagonal theorem is open.** The proved average bound allows narrow peaks. In fact, at \(Y\asymp T\) near the shrinking boundary its main term is of scale \(T^{2-o(1)}\), far above the required local threshold. A small average, Gaussian attenuation of distant poles, or a fixed-height factor in an all-scale Mellin bound does not supply the missing theorem.

The native note also extends the exact Newton reconstruction and its \(5/6\) detail-energy budget to every real height by twisting all convolution factors coherently. The changed harmonic kernel is written explicitly; no unproved transfer from the untwisted coarse-energy bound is used.

## 4. A distinct route could lower the constant much further

For the actual Möbius/sextic family \(A_u(D;W)\), suppose that

\[
\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll D^{k+\epsilon}H,\qquad H=D^{1+\theta},
\]

with all rows retained, every smooth test required by the extraction covered, and the fixed-data uniformity stated in the proof. This diagonal-size moment would give, after the exact extraction proved here,

\[
\beta_k=\frac12+\frac{5}{12k}
\]

as the limiting cancellation and zero-free exponent when arbitrarily small fixed \(\theta>0\) are allowed.

| Needed moment | Limiting exponent from this extraction | Status |
|---|---:|---|
| Second moment | \(11/12\) | Imported October 5 route |
| Fourth moment | \(17/24\approx0.708333\) | New analytic estimate required |
| Sixth moment | \(23/36\approx0.638889\) | New analytic estimate required |
| Every fixed \(2k\)-th moment | \(1/2+5/(12k)\) | Would approach the critical line; not proved |

The one-shot omitted-prime error would spoil the higher-moment gain. The exact recursion

\[
A_1(D)=B_p(D)-\nu(p)B_p(D/Np)
\]

and induction on smaller scales remove that error without putting the moving prime into the fixed datum.

The fourth moment has also been reduced to a smaller explicit coefficient problem. Separate the gcd of the two inverse factors. The remaining product column is squarefree and carries the exact balanced divisor weight

\[
\mathcal W_X(r)=
\sum_{d\mid r}W(Nd/X)W\!\left(\frac{Nr}{XNd}\right).
\]

A suitable mean square for these columns, uniform in the exterior coprimality exclusion and with the full original row range retained, implies the desired fourth moment. Summing the gcd costs only a harmonic factor. This removes the need to carry a changing cubic factor through the new closure proof, but the balanced coefficient estimate remains unproved.

The natural sextic diagonal has the expected \(D^{k+\epsilon}\) size for every fixed \(k\), including \(k\ge6\). Its size therefore does not by itself refute the proposed moment targets. The difficult off-diagonal cancellation is still present.

## 5. Connection to the Euler and causal programs

The principal correction factors exactly as

\[
H_\eta(s)=
\frac{L_K^S(6s-3,\bar\alpha^6\eta^6)}{\zeta_K^S(2)}
K_\eta(s),
\]

with \(K_\eta\) holomorphic and nonvanishing for \(\Re s>1/2\). The auxiliary character has nonzero angular type. This identifies the precise possible cancellation in the principal signal, rather than treating the correction as an unspecified obstacle.

The matching causal dilation inverse is exact on every finite horizon. Its absolute weighted norm preserves the source exponent only for \(\Re s>2/3\). An assumed angular summatory exponent \(\theta\) moves that threshold to \((3+\theta)/6\); even the conditional square-root value gives \(7/12\), not \(1/2\). A finite causal inverse and a bounded inverse on the needed analytic space are different requirements.

These local-factor issues do not obstruct the small geometric corollary near \(7/8\). They matter for substantially deeper continuation.

## 6. Evidence and remaining work

Three standard-library checkers pass **30,016 explicit predicates in each of normal and optimized Python**, with identical result output between modes. They authenticate exact local polynomial identities, the original and perturbed rational certificates, the quadratic-field envelope obstruction, finite causal inversions, and native/gcd coefficient identities with declared structural phases. They do not numerically prove an infinite moment or a zero-free theorem.

The repository contains the complete proofs, scoped independent review, checker sources and outputs. The imported manuscripts and relevant Lean closure were unchanged at the newer upstream head checked on October 10. Existing reviewed native material and the October 7 import are preserved.

The next decisive arithmetic objectives are the displayed pointwise native off-diagonal bound, and the squarefree balanced-divisor mean square sufficient for the fourth moment. A shrinking high-height band would also require a further argument handling any remaining off-line zeros before it could establish RH. The tail-zero note makes that quantifier distinction precise.
