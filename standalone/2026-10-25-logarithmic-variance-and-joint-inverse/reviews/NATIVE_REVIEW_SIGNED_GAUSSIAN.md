# Independent review: signed Gaussian selector

Date: 25 October 2026. Reviewer: `native_bootstrap`, independent of the author.

## Exact object and verdict

Reviewed file:
`third-pass/spectral/SIGNED_GAUSSIAN_SELECTOR.md`.

Final reviewed SHA256:
`3572375e7c00898cd284d3a843955dbdd07cbd075c7e98d8bc6823e3b85f0efa`.

**Verdict: PASS as the stated conditional analytic component**, after the
explicit `eta >= 0` repair to Theorem 2. No construction of the all-scale
bounded-variance selectors is supplied or approved, and no unconditional
zero-free improvement follows from this review.

The original reviewed bytes had SHA256
`c64678b7ea0fa7d4a86b49fe3b4ad1aa4061a29abc3d3e2aea5ea8b92851102c`.
They omitted `eta >= 0` from Theorem 2. I reported that omission before
author changes. The author added the hypothesis; I then read the repaired
statement and recomputed the final hash. This review does not silently
approve the original unrestricted statement.

## Sources actually checked

I read the exact PR 1017 source at
`450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, including its resident
`browse/PROOF.md` and `browse/THETA_RESIDUAL.md`. I also opened the primary
paper [Connes--van Suijlekom, arXiv:2511.23257v1](https://arxiv.org/html/2511.23257v1),
Theorem 5.6 and its proof, and the primary
[Connes--Consani--Moscovici source, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1).
The finite real-zero theorem and the theta annihilation identity remain
identified external inputs; this is not a reproof of every claim in those
papers.

## Reconstruction and normalization checks

1. **Complete source.** Equation (1) agrees with the pinned additive Weil
   form for `F(t)=integral f(x)exp(-itx)dx`, including both pole evaluations
   and all prime powers. I independently checked (21) against the digamma
   multiplier. The constant `log(4 pi)+gamma` and the bracket
   `r(x+t)+r(x-t)-2exp(-t/2)r(x)` have the stated signs. In particular,
   shifting the alternative digamma integral to this bracket changes the
   constant by `2 log 2`, exactly as required.

2. **Finite real zeros and full legality.** For `B=T-kappa I>0`, the
   subtraction `B-|1><1|/<1,B^(-1)1>` is positive semidefinite with
   one-dimensional kernel spanned by `B^(-1)1`. Its identity and
   constant-kernel changes preserve the source distributional matrix
   class. Reflection makes the kernel even. This is the correct setting
   for the imported finite real-zero theorem. A shift below only the even
   minimum is not substituted for full legality.

3. **Signed variance.** The Fourier transform is entire of exponential
   type and even, normalized at zero, and real-rooted. Paired Hadamard
   factorization therefore has no residual exponential factor and gives
   `-F''(0)=2 sum t_j^(-2) >= 0`. This does not assume a positive physical
   selector. The compulsory lattice zeros and the gamma product of the
   cosine-power example have the correct factors of `a`, `pi`, and two.
   The example checks compatibility only; it is not identified as a Weil
   resolvent.

4. **Overlap.** The product bound `|F(z)|<=exp(M|z|^2/2)` follows from the
   variance. Parseval with the heat factor gives exactly
   `(2-sqrt(2)-V_X/(4M))/(2 sqrt(pi M))`. It is positive under
   `M>=max(1,V_X)`. No sign has been assigned to `f_a` in this calculation.

5. **Gaussian schedules and residuals.** The norm growth exponent in (15)
   is `121 pi^2/(5000M)`. The physical Gaussian approximation exponent is
   `49/(200M)`, strictly larger; the Fourier-tail exponent is larger
   still. Endpoint subtraction makes both the polynomial and its first
   derivative compatible with zero extension. The residual estimate uses
   the complete operator, including the entire prime tail. Its bound
   `exp(2|x|) sum (log n)n^(-5/2)` is valid. The logarithmic Fourier
   multiplier is in `L2` for these test functions, so the operator/form
   pairing used in the variational argument is legitimate.

6. **Shift convergence.** The broad null comparator has mass one,
   `L2` norm squared `O(1/a)`, and vanishing complete-source residual.
   Comparing the normalized minimizer with it gives (39). Pairing with
   the positive-overlap approximant gives (38). These inequalities force
   negative shifts to zero. For positive shifts, the Rayleigh estimate
   uses the lower bound `||w_a||_2^2>=1/(2a)`; this is the correct
   direction for (41).

7. **Quadratic-schedule spectral consumer.** For the real even translated
   Gaussian, the Weil zero-side expression is the square of its entire
   Fourier transform at the spectral zero, not an absolute square there.
   It gives (44) with `z_rho=(rho-1/2)/i`; consequently a zero of real part
   `beta` contributes growth `exp((beta-1/2)t)`. The Gaussian coefficient
   never vanishes. Periodization and Fourier truncation at `ca^2` have
   Gaussian errors that beat the full operator's exponential loss. The
   polarized estimate (48) thus justifies passing the finite lower bound
   to the translated Gaussian.

8. **Landau step.** For `eta>=0`, the fixed `q[g]` term is absorbed into
   the positive exponential in (49). The nonnegative function introduced
   there has a finite Laplace convergence abscissa. Its meromorphic
   continuation has no real pole above `alpha`, since zeta has no real
   nontrivial zero. Landau's singularity argument therefore makes the
   transform holomorphic to the right of `alpha`. A zero there would
   give a pole with nonzero residue, yielding the stated contradiction.
   Taking the small positive parameters to zero gives Theorem 2.

## Required repair and remaining gap

The missing sign restriction on `eta` was a real statement defect: for
negative `eta`, the constant Gaussian contribution cannot be absorbed in
a decaying exponential, and a nonnegative Weil form would satisfy the
hypothesis while the conclusion would exclude critical-line zeros.
The final hash repairs this. The main application uses `eta=0` and was
not affected by the defect.

I found no further load-bearing gap in the repaired component. The
remaining arithmetic assertion is precisely the author's stated one:
actual, fully legal source resolvents must have the uniform variance
bound on every sufficiently large integer scale. The proof neither
constructs them nor infers them from the cosine-power witness or finite
data.

## What ran and what did not

I read all of the authored proof, rederived the source constants and
critical inequalities above, checked the specified primary theorem, and
computed SHA256 from the local bytes. No numerical eigenvalue experiment
or finite zero census was used. No claim about the source's all-scale
selector existence, the integrated repository status, or RH itself is
approved by this component review.
