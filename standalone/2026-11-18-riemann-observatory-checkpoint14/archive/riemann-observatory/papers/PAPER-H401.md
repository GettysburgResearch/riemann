# PAPER-H401 — Hadamard1896: boundary nonvanishing and smoothed PNT

**Identity.** Jacques Hadamard, *Sur la distribution des zéros de la fonction ζ(s) et ses conséquences arithmétiques*, Bulletin de la Société Mathématique de France24(1896),199–220. DOI https://doi.org/10.24033/bsmf.545 . Original publisher scan: https://www.numdam.org/article/BSMF_1896__24__199_1.pdf . Local `sources/history_round4/hadamard1896.pdf`, SHA-256 `7620c7875b938e804fe11b81c465c76dd92debd0b90be4d8dffa06276da0c2ba`,23PDFpages including the Numdam cover and all22article pages. The printed199 footnote states the fundamental results were communicated to the Académie des Sciences on22June1896. Access2026-11-17.

**Scope.** All22original French pages199–220 substantively read, including the final note on de la Vallée Poussin. Selected original formula images199,202,211–213,216,218,220 visually checked against noisy OCR. Whole-work Level1. Local Level2 reconstructions: boundary nonvanishing mechanism, the precise role of μ>1 smoothing, and μ=2 monotone unsmoothing; no complete independent audit of the genus estimates, selected horizontal-contour bounds, all Hurwitz/Lipschitz character formulas or the entire22-page proof. Root independently checked the modern sufficient boundary lemma and the qualitative unsmoothing. No paper-wide Level3 claim; no exhaustive erratum search.

## Exact results and historical boundary

**§§1–5,199–203:** ζ(1+it) is nonzero for every real `t!=0`. At s=1 there is the known simple pole. This closes the boundary issue left open by the Euler product in Riemann's memoir. Hadamard describes Stieltjes's purported RH demonstration as unpublished; this archive credits neither Stieltjes nor Hadamard with a proof of RH. In §11,210, Hadamard explicitly emphasizes that zeros could still approach the boundary indefinitely.

The source proof compares the prime sums `sum p^-σ`, `sum p^-σ cos(t logp)` and `sum p^-σ cos(2t logp)`. A hypothetical boundary zero would force almost all weighted prime mass into phases near odd multiples of π; doubling those phases then forces an inadmissible singularity at `1+2it`. In §5,202, he identifies the reusable hypotheses: **positive coefficients in a convergent exponential Dirichlet expansion of log f**, plus continuation to the boundary with a single simple pole. This positivity concerns the logarithm's arithmetic-frequency expansion. It is a different hypothesis from positivity of a physical-space Laplace kernel and gives boundary nonvanishing, not RH. A precise modern sufficient formulation and proof appear in the scoped audit.

**§§6–10,203–209:** analogous analytic properties and boundary nonvanishing for Dirichlet L-functions. The inputs include periodic Hurwitz-type series, a contour continuation with its power branch, Lipschitz/Hurwitz functional relations, character orthogonality, and Dirichlet's nonvanishing at1. The logarithm of the product over all characters has nonnegative Dirichlet coefficients, and that product has only the principal simple pole. This supplies `L(1+it,chi)!=0` for every character and nonzero real t, together with the separately used nonprincipal value at1. Functional-equation symmetry belongs to the primitive completed object; imprimitive Euler factors may add zeros on Re s=0 and must be retained separately rather than turned into a generalized-RH claim.

**§§12–17,211–217:** for `a>1`, `μ>1`,

\[
 \psi_\mu(x)=-\frac1{2\pi i}
 \int_{a-i\infty}^{a+i\infty}
 \frac{\zeta'(s)}{\zeta(s)}\frac{x^s}{s^\mu}\,ds
 =\frac1{\Gamma(\mu)}\sum_{p^k<x}
 \log p\,[\log(x/p^k)]^{\mu-1}
 \sim x.
\]

The branch is the one positive for positive real s; when fractional μ is used the source's contour has a cut along the negative imaginary direction. The integer μ=2 suffices for the final conclusion and needs no fractional-power branch. For μ>1 the prime-power weights vanish at equality, making the smoothed function continuous at prime powers. The unsmoothed μ=1 endpoint requires separate Perron half-value conventions and is not interchangeable with this absolutely convergent integral.

The decisive parameter condition is `μ>1`: the zero-count/genus information makes `sum_rho |rho|^-μ` converge. Choose a finite collection of zeros leaving an arbitrarily small reciprocal-power tail. Boundary nonvanishing lets a fixed contour pass left of that finite collection; those finitely many terms are o(x), while the whole remaining zero tail is at most εx. The selection of finitely many zeros depends on ε and precedes the limit x→infinity. No uniform zero-free region is assumed or proved. Horizontal contour pieces require separate avoidance and growth estimates, supplied in §§14–16; those fine estimates are not all independently certified here.

**§18,217–218:** discard higher prime powers, take μ=2, and remove smoothing by monotonicity. If `theta(x)=sum_(p<=x)logp` and `A(x)=sum_(p<x)logp log(x/p)`, then `A~x` and `A(y)-A(x)=integral_x^y theta(t)dt/t`. Fixed multiplicative increments bound theta above and below; taking x→infinity first and then the increment to zero gives `theta(x)~x`. Partial summation gives the equivalent usual prime number theorem `pi(x)~x/logx`. No assertion of a quantitative error follows from this qualitative argument.

**§19,218–219:** for each fixed positive integer k and reduced residue class m modulo k,

\[
 \sum_{p\le x,\ p\equiv m\ (k)}\log p\sim\frac{x}{\varphi(k)},
\]

and hence the corresponding prime count is asymptotic to `x/(phi(k)logx)`. There is no claimed uniformity in growing k. The paper asks what quantitative error information may be recovered from the full family of smoothed relations; the scoped audit records an elementary quantitative unsmoothing bound and its generic monotonicity limitation.

**§20 and final note,219–220:** extensions to Weber/Meyer series are discussed with analytic hypotheses still to be established in some cases. The final note explicitly acknowledges independent work of de la Vallée Poussin and emphasizes the μ>1 absolute-convergence device. It is not an admission that all proofs using Perron inversion fail. Source criticisms and their target formulas must be read with this distinction.

## Dependency architecture

Euler logarithm with positive coefficients + unique simple boundary pole → boundary nonvanishing.

Continuation + entire-function growth/canonical product estimates → zero-count and selected-contour control → absolute reciprocal-power zero tail for μ>1 → smoothed prime-power asymptotic → negligible higher prime powers → μ2 monotone unsmoothing → theta~x → PNT.

For progressions: Hurwitz/character analytic theory + Dirichlet L(1) nonvanishing + positive logarithm of the total character product → boundary nonvanishing for all factors → character-weighted smoothed integral → fixed-residue theta asymptotic.

The particularly reusable mathematical distinction is between qualitative boundary exclusion and a quantitative zero-free strip. The former suffices here because smoothing makes the infinite tail uniformly summable. Recovering a sharp unsmoothed error demands more information. This paper supplies meaningful progress without moving every zero toward the critical line.

## Research-use questions and limits

1. Put the original μ>1 contour-tail argument and a modern Tauberian theorem into a single exact hypothesis table; identify which growth bounds are needed for each proof rather than asserting boundary nonvanishing alone proves PNT for every meromorphic model.
2. Quantify the smoothing-to-unsmoothing loss under a stated local error modulus. The elementary square-root loss is generically sharp for nondecreasing counting functions; arithmetic structure must justify any better deduction.
3. Audit the original imprimitive-character reduction with Euler factors explicit, preserving the distinction between boundary artifacts and nontrivial zeros of the primitive completion.
4. Read de la Vallée Poussin's original1896 treatment before attributing the later logarithmic zero-free region or exponential PNT error to this paper. This record makes neither attribution.
