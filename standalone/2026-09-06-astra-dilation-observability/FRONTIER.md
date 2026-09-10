# Construction attempted, and the first theorem still missing

The goal was not another positivity reformulation. The concrete attempt was
to replace the repository's problematic signed-energy contraction by a
genuine best-approximation problem, where Gram positivity is automatic and
Schur updates compute the improvement exactly.

The attempt produces three useful changes of viewpoint:

**An observable rather than an entire coefficient law.** For the limiting
projection, the error at cell 1 is quantitatively comparable to the whole
squared residual. A hypothetical off-line zero therefore forces a fixed,
positive first-cell discrepancy, with the explicit bound in PROOF.md (19).
The first cell and dictionary are chosen before the zero. This is not just
pointwise convergence of arbitrary approximants: orthogonality and dilation
invariance are indispensable.

**Prediction gain rather than matrix positivity.** The old-to-new Schur
matrix is positive definite for every N. What could prove RH is that the
actual target coupling has nonsummable normalized gain. Formula (16) is
exact; the stronger estimate (G) would give an explicit logarithmic rate.
The matrix inverse here is finite and nonsingular, not an illicit inverse
on an unbounded energy completion.

**Arithmetic support rather than a bare zero signature.** Two multiplicatively
independent prime generators remove all extra common Mellin zeros, but a
two-prime arithmetic dictionary still misses a dual direction with a
1/52 lower bound. This makes an exact countermodel to using a zero-signature
argument as a substitute for source completeness.

## The three closing attempts actually tested

1. Try to infer RH from first-cell saturation at a finite stage. It fails
   exactly at N=2: g_2(1)=1 and delta_2=1-log2>0. At N=3 the value is even
   strictly greater than 1. The missing term is the finite dilation leakage.
2. Try to make D_2 g_N an always-positive improvement direction. The sign of
   its residual coupling is strictly negative at N=8. The squared coupling
   still yields a valid update, but it captures less than 0.032 of the full
   doubling gain there. No universal sign or dominance theorem is inferred.
3. Try to use just the two incommensurable prime dilations to retain the
   full zero information and close cyclicity. The omitted squarefree index
   5 gives an unconditional infinite-dictionary obstruction. The shortcut
   fails before any unknown zeta-zero input is needed.

The finite non-stagnation bound (10) remains valid through all three audits.
When the first-cell defect is small relative to delta_N it forces a useful
Schur gain. What is not proved is that the full arithmetic dictionary forces
that favorable relation at sufficiently many scales, or supplies enough
other innovation directions when it does not.

## Exact next target

For the complete predetermined dictionary h_2,...,h_N and N=2^j N_0,
prove, for some fixed c>0 and all sufficiently large j,

    z_N^T S_N^{-1} z_N >= c (1-b_N^T G_N^{-1} b_N)^2.

This is sufficient, not asserted necessary. A less rate-specific target is
that the sum of the actual normalized Schur gains diverges. The single-cell
alternative is to prove limsup g_N(1)>=1; the limit already exists.

A focused next proof attack should construct a *block* of arithmetic
innovation directions and lower-bound its pairing with the residual,
retaining every squarefree index. The one-dilation calculation demonstrates
why one cannot assume a fixed direction carries the entire gain. Another
finite sweep cannot settle the needed quantifier.

No bound proved in this packet implies the displayed target. The end-to-end
implication from that target to RH is complete; the target is the remaining
mathematical obligation. The work does not resolve RH.
