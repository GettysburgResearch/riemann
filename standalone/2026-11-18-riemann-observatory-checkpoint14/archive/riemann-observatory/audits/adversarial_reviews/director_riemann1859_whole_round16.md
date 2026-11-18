# Riemann's first print: whole-memoir historical proof adjudication

18 November 2026. PAPER-S001. The director read all ten actual German first-print page images, pp.671–680, alongside the complete nine-page Wilkins English translation, and inspected the controlling 1892 collected display and Genocchi's original pp.57–58. The two independent complete source reconstructions were then compared with a third adjudication. This supports a whole-work Level 3 **historical proof audit of this exact first print**, with the unproved original claims, established later proofs, known corrections and remaining conjecture explicitly distinguished. It does not certify every printed sentence as a theorem, prove RH, reproduce the historical numerical tables, or identify a new mathematical error.

Controlling source: the ten-page November 1859 Academy first print, DjVu SHA-256 `9e2b9cd404dd8d054689607ef4b7c49734fd0d6648a272244451f6ae9a5f9b4c`, with per-image hashes in the [source manifest](../../sources/history_round4/source_manifest.json). Page 671 records Kummer's presentation on 3 November of Riemann's letter to Encke dated 19 October; the communication, proceedings session and collected editions are distinct source facts. The English preliminary translation, December 1998, has SHA-256 `6b24341e3406d165baeb7ab1e00cfa0a544d0399e2b33175dfa71480bdddd24f`. It is a parallel witness; the original controls formula discrepancies.

Independent evidence: [complete advocate and page ledger](analytic144_riemann1859_whole_advocate.md), [complete skeptic and page ledger](geometry144_riemann1859_whole_skeptic.md), [third source and historical adjudication](geometry151_riemann_whole_third_adjudication.md). The later source comparison includes the 1892 collected PDF SHA-256 `55f149d350e4541d0c536222b4a26d74ce5f751a2f0ef97c3b8d3559894de358` and Genocchi's eight-page extract SHA-256 `60c40a680b855cf36b17a588b94e70692d019416ce05654d895a82f149b5a35c`. Those are targeted supplementary inspections, not whole audits of the collected volume or Genocchi article.

## Complete coverage and proof dependencies

| First-print pages | Source content and audit disposition |
|---|---|
| 671–672 | Euler product and series on Re s>1; gamma Mellin transform; Hankel continuation with an explicit logarithmic cut. Reconstructed with absolute convergence and a fixed inner circle. |
| 673 | Negative-half-plane residue deformation, functional equation, Jacobi theta transformation and split. The outer contours must avoid the poles; exponential theta convergence supplies an independent entire continuation argument. |
| 674 | Completed even function, two cosine kernels, strip and count forecast; probable reality of all roots. Count boundary estimates are later inputs, and RH is explicitly conjectural. |
| 675 | Paired product and arithmetic midpoint counts. Product convergence alone does not prove the source's zero-free quotient assertion; a modern finite-order factorization supplies that step. |
| 676–677 | Mellin/Fourier inverse, integration by parts, gamma product and elementary inverse kernels. Arithmetic bounded variation gives midpoint inversion; two local first-print slips are already repaired in 1892. |
| 678–679 | Logarithmic-integral branches, ordered zero series and contour comparison, prime-count inversion and finite spectral derivatives. The constant is Genocchi's known correction; pointwise ordering needs a later explicit-formula input. |
| 680 | Historical tabulation, suggested numerical investigations and empirical weighted-count comparison. These remain reported observations and heuristics. |

The dependencies are

```text
Euler absolute convergence → gamma transform → Hankel continuation
Jacobi transformation → entire symmetric theta integral → entire even Xi
theta decay → finite-order growth → Hadamard product
Euler logarithm → weighted prime-power transform → BV midpoint inversion
normalized product + gamma factors + branches → distributional inverse
von Mangoldt ordered formula + summable kernel remainder → pointwise J_0
finite Möbius inversion → midpoint prime count.
```

The zero count additionally uses argument control, Stirling and Jensen on a fixed-strip real-part proxy. The supplemental proof of the rearrangement warning uses later Landau sums, a mean real-part-displacement estimate and Weyl equidistribution. RH is not an input to these reconstructed identities. The last two additional historical assertions—the approximately full count of real roots and universal reality—are not proved by this tree.

## Continuation and the product: the exact missing steps

On Re s>1 all Mellin integrals and the Euler logarithm are absolutely convergent. With log(-z) real on the negative real axis, the inward and outward Hankel lips have the prescribed opposite arguments. Keep an inner radius smaller than 2pi for continuation rather than asserting convergence of the original real integral outside its domain. For Re s<0, expanding outer rectangles at imaginary heights (2n+1)pi avoids poles of 1/(exp z-1); the exterior edges are O_s(R^(Re s)) and vanish. Gamma reflection and duplication give the functional equation.

The independent theta route is particularly clean:

```text
pi^(-s/2)Gamma(s/2)zeta(s)
 =1/[s(s−1)]
  +integral_1^infinity theta_+(x)[x^(s/2−1)+x^(-(s+1)/2)] dx,
theta_+(x)=sum_(n≥1)exp(−pi n²x).
```

The integral is entire locally uniformly. The intermediate theta(1/x) integral in original p.673 is over 0<x<1. Both accessed Wilkins transcriptions instead print 1<x<infinity on that intermediate line; at s=2 their integrand tends to 1/2 and diverges. Their final formula remains correct. This discrepancy belongs to the transcription apparatus, not the original memoir.

Write xi_*(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 and Xi(t)=xi_*(1/2+it), Riemann's xi(t). The theta kernel gives log M_Xi(R)=O(R log(R+2)). Thus G(w)=Xi(sqrt(w)), defined by the even Taylor series, is entire of order at most 1/2. Its genus-zero Hadamard factorization yields

```text
Xi(t)=Xi(0) product_(Re alpha>0)(1−t²/alpha²),
```

counting multiplicities. This proof does not need the count asymptotic. For completeness the order is exactly 1/2: Stirling on the positive real s axis, where zeta(s) tends to 1, gives log Xi(iR)=R log R/2+O(R) by the functional equation, providing the matching lower growth along w=-R². The second cosine kernel is positive on x>=1, termwise because pi n²x-3/2>0. It gives Xi(i v)>0 for real v, so no zero lies on the imaginary t axis and the opposite-pair convention is legitimate. The first cosine formula also gives Xi(0)<1/2. Reflection in t and complex conjugation are different symmetries; off-line zeros generally require quartets. The original quotient-growth paragraph does not itself supply the modern factorization theorem or a global logarithm through zeros.

## Exact arithmetic identity, branches and the known constant

Let pi_0 count primes below x and add half at a prime, and let J_0(x)=sum_(m≥1)pi_0(x^(1/m))/m. The Euler logarithm gives log zeta(s)/s as its Mellin transform on Re s>1. Its exponentially tilted log-coordinate step function is integrable and has finite variation, so Dirichlet–Jordan inversion gives the printed symmetric inverse with midpoint values at every prime power. For fixed x>1, the integrated-by-parts boundary is O_x(1/T), since the Euler logarithm is bounded on this line. Separating divergent constituent logarithm integrals before that step would be invalid; Riemann explicitly recognizes the issue.

The correct modern pointwise identity is

```text
J_0(x)=li(x)−lim_(T→infinity)sum_(abs(Im rho)≤T)E_rho(x)
       +integral_x^infinity du/[u(u²−1)log u]−log 2,  x>1.
```

Here li(x)=PV integral_0^x du/log u, and E_rho(x) is the logarithmic integral continued with log(x^rho)=rho log x. Taking a new principal logarithm of the already exponentiated number x^rho would change the terms. With the usual Ei continuation, E_rho=Ei(rho log x)-i pi sgn(Im rho); the offsets cancel under the ordered conjugate grouping. The zeros include multiplicity, and neither RH nor simplicity is assumed.

The paired normalization is decisive:

```text
1+(s−1/2)²/alpha²
 =(1+1/(4alpha²))(1−s/rho)(1−s/(1−rho)),
Xi(0) product_alpha(1+1/(4alpha²))=xi_*(0)=1/2.
```

Thus the center-normalized logarithms carry the absolutely convergent real shift D=log(1/2)-log Xi(0)>0. The final constant is log Xi(0)+D=-log 2. Genocchi's original p.58, equation (11), explicitly makes this correction after the calculation on pp.57–58; the director inspected those pages. The 1892 editorial note p.155 states the same replacement. The centered zero-only contour on p.678 differs by -D log x before division by log x; it is the same normalization issue, not a second discovery. Branch offsets are imaginary and cannot supply this real constant.

Distributional inversion of the normally convergent paired product is justified against smooth compact tests in log x>0 by its polynomial vertical majorant. It does not alone prove raw pointwise convergence. The later von Mangoldt midpoint formula for psi_0 supplies the required ordered main term, because

```text
E_rho(x)=x^rho/[rho log x]+O_I((1+abs(Im rho))^(-2))
```

uniformly on any compact I in x>1. The remainder sums normally. This identifies the pointwise representative with its jump midpoints. The unit-height O(log T) zero count and individual O_x(1/T) terms equate height order with the source's magnitude order in alpha. These later inputs are explicitly accepted dependencies, not hidden parts of the 1859 printed proof.

The missing sum in the p.676 substituted logarithm and the missing minus in the p.677 simple-pole inverse are both visibly repaired in the 1892 collected p.150, which the director inspected. The general sine/cosine sentence also needs its reflected contributions separated; their cancellation gives the correct combined inverse, as the collected note already explains. No new author-error entries are added for these longstanding repairs.

## What the last page establishes

The Möbius inversion pi_0(x)=sum_m mu(m)J_0(x^(1/m))/m is exact and locally finite; midpoint values propagate. Differentiating a finite zero truncation gives the displayed oscillatory approximation. It does not differentiate the infinite conditional series term by term, give an ordinary derivative of a staircase, or control an unconditional square-root prime-count error. Off-line complex frequencies would introduce their own hyperbolic growth.

The smooth subtraction -li(sqrt x)/2 explains a tendency of one part of the expression, not a global sign theorem for li(x)-pi(x). The Gauss–Goldschmidt tabulation through three million is reported history; it was not independently recalculated here. The original phrase concerns the range from the first hundred thousand onward, while the accessed English wording says in the first hundred thousand. The final weighted-count comparison on p.680 repeats the printed +log Xi(0); the corrected exact formula uses -log 2. None of these observations proves RH.

This audit elevates the source's traceable proof status, not its conjecture. Its main reusable lesson is the need to keep product normalization, branches, summation order and jump values together. The modern signed-contour criterion in [the parallel Round 16 campaign](director_signed_mellin_round16.md) supplies a different valid test-function interface; it is not a retrospective claim that the nonsmooth prime staircase satisfies that criterion. The next historical task is a similarly complete audit of the later von Mangoldt ordered-limit proof rather than another rediscovery of Genocchi's constant.
