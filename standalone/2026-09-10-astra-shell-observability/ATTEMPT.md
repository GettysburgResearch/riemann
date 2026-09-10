# Attempt at the full small-divisor estimate

**Research handoff, not a proof of RH.** This pass attacks the exact Q-AC26
coupling from the parent, keeping every input and cross term.

The intended closing argument was:

1. Use finite divisor inversion to control derivatives from the forcing.
2. Turn that regularity into compactness at a moving multiplicative boundary.
3. Combine the resulting shell inequality with the parent scalar recurrence.

Step 1 is now unconditional in a particularly explicit form: the infinite
matrix of discrete derivatives is Hilbert--Schmidt with squared norm 3/2,
with a complete tail bound and a sign-exact positive squarefree conjugacy.
Step 2 is NOT a generic compact embedding. Recovering the source by cumulative
integration is unbounded on growing intervals. The parent's nonnative control
has a smaller derivative norm and still violates shell compactness. For the
native arithmetic itself the raw transmitted norm diverges, by AC27-2.

## What survives from the attempted step 2

On every controlled relative range, the entire coupling has a quantitative
operator limit, not a sampled or diagonal approximation. In logarithmic
coordinates it asks whether the literal h(t)=e^(t/2)m(e^t) can generate a
large future window from a small forcing while its whole past response is
small. The parent old-energy term must remain. A critical zero gives an
explicit lower cost on C_eta but does not defeat an estimate that permits
that cost. No hypothetical off-critical zero is assumed.

This separates two missing upper estimates rather than supplying either:

- native future/past observability on arbitrarily long logarithmic histories;
- a source-faithful treatment of the discrete small-index boundary when the
  relative cutoff shrinks too fast for the proved grid-error bound.

The continuous model is obtained from actual divisibility data. Nevertheless,
its necessary condition is not automatically sufficient for the discrete
one. A proof must show the uniform lattice adapter, or remain discrete.

## The next genuinely sufficient target

Do not impose the unnecessarily strong goal ||D_A||<=C; it is false.
Retain either the parent eta||V_A f||^2 penalty with a uniform C_eta, or the
weaker estimate in Section 6 of PROOF.md with a subpower cutoff defect.
The latter still gives RH and can tolerate polylogarithmic losses.

For a proposed matrix multiplier, test the complete signed matrix

    C I+eta V_A^*V_A-D_A^*D_A,

not only individual bands, its diagonal, its determinant, or the first source
column. At A=81 every band passes with C=3/5 while the combined vector requires
more than 94/100. The stored rational witness and full matrices can falsify
an alleged orthogonality step immediately.

For a compactness argument, the sequence must satisfy BOTH bounded old norm
and vanishing arithmetic residual. The native mean-row witnesses prove
unbounded forcing-to-output norm, but do NOT prove that their old norms stay
bounded. They therefore do not refute Q-AC26. Conversely, the compactness of
the derivative only controls their differences and cannot prove Q-AC26.

## Scope of the finite reconnaissance

Floating exploratory eigenvalue calculations up to A=2187 suggested that
C=1 remains plausible for the sampled eta values. They were used only to
choose an exact rational band witness. They are neither directed enclosures
nor part of any universal theorem. The final certificate fixes A=81 and
checks the whole matrix exactly, with separate LDL and Bareiss calculations.

No claim is made that this pass has reduced RH to a routine task. Its completed
work identifies the real coupled prediction inequality, supplies a global
regularity tool and exact tests, and removes two false completion arguments.
The missing uniform/subpower arithmetic upper bound remains explicit.
