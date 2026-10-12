# Independent exact primitive synthesis audit

Date: 2026-10-10 UTC. Read-only audit, all replay/oracle artifacts under `/tmp`; no checkout or Git mutation and no second continuum residual integration.

**Scoped PASS.** The complete primitive trace is rigorously below one, so the exact synthesis constant `K=1` is valid for the same fourteen completed native Galerkin tests. The reviewed Young argument therefore yields the improved exact bound

`q_1(h,h) >= (1/600000000000)*(||Pi_E h||_2^2+||G_1 h||_2^2)`,

and, by literal-kernel zero extension, `q_L(h,h) >= (1/600000000000)*||G_L h||_2^2` for every complex native L2 test and every `0<L<=1`. This controls a compact injective primitive norm, not the native L2 norm; there is no assertion at `L>1` and no RH consequence from this bounded-window result.

## Frozen files and provenance

Wave operator directory: `/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/operators`.

- `EXACT_PRIMITIVE_SYNTHESIS.md`: `1e1cd511a477cf5120b0b7ca0a9ebb36ce5b115d8c3faa063e76b6870733aac9`.
- `enclose_exact_primitive_synthesis.py`: `009ae7df8ef5acdea2be122602d8c239eb0a36ac56563bf76640469926b8a011`.
- Owner `directed_exact_synthesis_codim14_trial100.json`: `df598c783ec412941cfd13f3c07cb3054ae3ad32a613320318a5915ffcbe3551`.
- Frozen inherited extractor `enclose_primitive_norm.py`: `a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0`.
- Unchanged completed continuum residual: `9213accb90caa99e17172f620c3946ab638542eaf0523dfba89ab8f870d2016a`.
- Checkout weighted receipt bound by the owner synthesis receipt: `da0917e75a165b817c1ed7120dc17a467c88092a160f0f41da6b0b80a083b101`.
- Independently replayed fresh weighted receipt used for this review: `eab5e0bd7f683de7c185e3795be5f2e039a0d7f0f08a38a15a7249995322e4ce`.

The completed weighted acceptance and original quantitative argument were independently reviewed previously in `/tmp/review-completed-native-lower.md` (SHA256 `04eebe843815decf5f29fd11738a58c7778897b17beda168759ab15573632db9`). That review also independently checked the complete 696-panel residual coverage, source/coefficient bindings and exact rational positive-definiteness oracle. This sharpening imports that same completed acceptance, not a new integration or a source replacement.

## Complete analytic formulas

Proof lines 22–27 are correct. For general positive c, the convolution with `cosh(c*t)` has Laplace multiplier `s/(s^2-c^2)`. Multiplying by the transforms of `sin(a*t)`, `exp(+-c*t)` and `cosh(b*t)` gives respectively

`a/(a^2+c^2)*(cosh(c*t)-cos(a*t))`,

`(t/2)*exp(+-c*t)+(exp(c*t)-exp(-c*t))/(4c)`,

`b/(b^2-c^2)*sinh(b*t)-c/(b^2-c^2)*sinh(c*t)`.

At `c=1/2`, `b=3/2` these are exactly (S2). In particular the resonant `+-c` limits are both included and their signs agree with the literal convolution. The functions vanish at zero and their derivatives at zero equal those of the corresponding convolution, namely the input value at zero.

The six soft coefficients in checker lines 61–73 exactly expand these formulas in the ordered basis `exp(c*t),exp(-c*t),t*exp(c*t),t*exp(-c*t),exp(b*t),exp(-b*t)`. The sine primitive contributes equally to the first two soft exponentials and contributes minus its scale to its cosine, as in lines 55–60. There is no sign dropped in either resonant exponential or the cosh term.

The whole soft Gram and mixed cosine integrals in (S3) are correct. All native functions and coefficient balls are real, so the real bilinear calculation is the squared L2 norm. The cosine functions have strictly positive integer frequencies, giving their exact Gram `delta_nm/2`; the constant cosine is not needed. `F`, `F'`, and `F''` are the displayed entire integrals. Rates that sum to exact zero are handled by the exact `1/(p+1)` branch, including `F''(0)=1/3`. Nonzero mixed arguments contain a positive integer imaginary frequency and hence cannot encounter the removable singularity.

For complex synthesis scalars, Hilbert-space Cauchy–Schwarz still gives `||sum x_i*Gz_i||^2 <= (sum ||Gz_i||^2)*sum |x_i|^2`, so bounding the trace is sufficient; no real-only restriction enters the final conclusion.

## Native inventory and normalization

The original source basis is explicitly unnormalized `sin(n*pi*t)` in `enclose_analytic_upper.py` lines 164–172. It consists of low sines 1–11, `exp(t/2)`, `exp(-t/2)`, `cosh(3t/2)`, and high sines 12–111. The source's Gram matrix and Cholesky inverse in lines 199–201 produce the exact L2-orthonormal complement basis. Its projected trial constraints, correction solve and complete coefficient construction are in lines 203–217; in particular the high-sine coefficients are minus the correction coefficients, and the low/soft coefficient block already includes the orthogonal-projection correction.

The synthesis checker therefore correctly applies its transform to the complete raw-basis coefficient inventory rather than assuming that the raw sines are normalized or omitting the low projection. Its index map sends raw rows 0–10 to frequencies 1–11 and raw rows 14–113 to frequencies 12–111. The three intervening rows are precisely the exponentials and cosh term. All 114 raw rows, fourteen trial columns, six soft functions and 111 cosines are retained. The dimension guard and finite positive norm checks use `require` and remain active under optimized Python.

## Full receipt replay and metadata distinction

The new checker hashes the frozen extractor, then invokes its complete weighted fresh replay before consuming the same authenticated coefficient inventory. The extractor checks the residual hash, current weighted checker, all source/helper/parameter/trial guards and the full mathematical weighted receipt (`enclose_primitive_norm.py` lines 46–65). It preserves the exact reserve `epsilon=1e-11`, complete source-U matrix and full weighted residual.

Running against the saved checkout weighted receipt in the current environment fails closed at the extractor's exact semantic-equality guard. I independently compared all nonvolatile fields of that saved receipt and my fresh accepted receipt. The **sole** difference is `/fresh_source_moment_receipt/source_U_receipt/python_flint_version`: saved `0.8.0`, current `0.9.0`. Every mathematical field, matrix and coefficient-ball string is identical. No source, parameter or arithmetic acceptance guard was relaxed. I reran against the already authenticated fresh weighted `/tmp` receipt, thereby obtaining complete original-checker acceptance in both modes.

Normal and optimized synthesis receipts:

`/tmp/review-exact-primitive-synthesis-normal.json`

`/tmp/review-exact-primitive-synthesis-optimized.json`

Both exited zero and are byte-identical, SHA256 `1e6eb716fc49da8860b69950304a52b7c86cea3521f906d2149ef56e045c851e`. They enclose the synthesis trace by

`[0.51327163928409972066385135858719195985933514973386 +/- 1.00e-15]`.

Their baseline weighted hash/version fields intentionally differ from the owner's historical receipt as described above. The mathematical synthesis fields and all fourteen norm-ball strings agree with the owner's retained receipt.

## Independent whole-integral oracle

Script `/tmp/review_exact_primitive_synthesis_oracle.py` has SHA256 `1a17e760ef7762e7d372746faf69e8248d45e4c8057fbcd9f17c9c3b3b2cd713`.

It checks four rational Laplace identities symbolically with general a,c,b. It then independently builds the full 117-function primitive Gram at 384 bits:

- Soft-product moments are evaluated by the uniform entire exponential series through degree 120, with the full remainder bounded by `exp(3)*3^121/121!` on the integration interval. This avoids the owner's closed removable formulas.
- Mixed cosine moments use exact endpoint parity `cos(n*pi)=(-1)^n`, `sin(n*pi)=0`, and the real formulas `r*((-1)^n*exp(r)-1)/(r^2+(n*pi)^2)` and its derivative in r. This avoids complex exponential-integral evaluation.
- It assembles the complete linear primitive transform into a matrix and computes one Gram congruence for all fourteen trials, rather than reproducing the owner's per-trial summation organization.

All fourteen directed norm balls are positive and overlap their retained counterparts. The independent full trace is

`[0.51327163928409972066385135858612668673822436320598 +/- 5.00e-16] < 1`.

Normal and optimized oracle outputs are byte-identical:

`/tmp/review-exact-primitive-synthesis-oracle-normal.json`

`/tmp/review-exact-primitive-synthesis-oracle-optimized.json`

SHA256 `0e180f58f46e8c987e57b46a56cf29f427513e61eae75a6e7ab92b2b798445a1`.

The oracle uses the native outward Arb backend for arithmetic, independently organized analytic integrals and the authenticated exact coefficient balls. It does not rebuild the continuum source integration.

## Exact final constant and scope

The original accepted trace bound remains `M=1`; `epsilon=1/10^11`, `theta=1/200000000001`, `kappa=6/5`. With K=1, the two exact Young candidates are `1/600000000000` and `3/(5*200000000001)`. The first is strictly smaller, hence is the stated delta. This is a strict improvement over the previous coarse synthesis value without changing any continuum residual or weighted acceptance matrix.

The all-complex native L2, bounded-window conclusion follows from the already reviewed quantitative argument and literal-kernel zero extension. Injectivity of G yields strict positivity for each nonzero test. There is no uniform native L2 spectral gap, no cofinal length assertion and no RH inference.
