# Fixed-shift native transfer and actual signed correlations

Status: proposed mathematics, requiring independent review. RH remains open.

This packet supplies an exact bounded bridge from one fixed real-shift ratio
source to the complete native Mobius Gaussian, and then evaluates genuine
signed sectors of the resulting ordinary-integer energy.

1. **One fixed shift suffices quantitatively.** For h>1/2, the complete sources
   are inverse causal dilation transforms. Their finite-horizon critical Lp
   norms have two-sided constants independent of T and p, simultaneously for
   1<=p<=infinity. At ordinary zeta h=1 the constants are zeta(3/2) and
   zeta(3/2)/zeta(3). The full one-sided continuum has finite critical norm.
2. **Even one small shift suffices qualitatively.** If its critical energy
   were subpower, every denominator zero would have to propagate to its
   positive translates, eventually beyond Re s=1. Averaging over h is not
   needed to prevent that global cancellation chain. The energy premise is
   still unproved.
3. **The arithmetic is signed and explicitly non-diagonal.** The h=1
   coefficient is a(n)=product_(p|n)(1-p)/n. Its energy diagonal is
   C_c C_a log T+O(1), with C_a=product_p(1-3/(p^2+p+1)). Tao's published
   logarithmic correlation theorem makes every fixed additive off-diagonal
   band o(log T). The entire infinite sector where one index divides the
   other has a NEGATIVE main coefficient L_div C_c C_a log T, where a
   rational directed certificate proves -21/10<L_div<-7/5.

The full complement remains unsolved. All fixed coprime ratio rays have an
exact local mean, but the putative absolute double sum of their limiting
constants diverges. The finite-scale Gaussian cutoff therefore cannot be
dropped before summing the complete correlation problem.

Read PROOF.md for the transfer and criterion, ARITHMETIC.md for the exact
kernel and signed arithmetic, SOURCES.md for dependencies and reviewed heads,
and VALIDATION.md for the finite/infinite boundary.

Run `python replay.py`. It uses only Python's standard library. `verify.py`
regenerates the 512-term sign certificate from exact arithmetic, checks full
finite divisor identities, and numerically cross-checks finite Gaussian
integrals. No precomputed JSON is an input to mathematical acceptance.
The runner compares ordinary and optimized execution and separately launches
three corruptions. Its finite checks do not prove Tao's theorem, the zeta
contour argument, or the open RH-strength energy estimate.

No CT zero-free theorem, de Faveri family bound, capped reciprocal law or
unreviewed quasi-RH claim is an analytic premise. No worldwide priority claim,
repository integration, or independently accepted RH result is asserted.
