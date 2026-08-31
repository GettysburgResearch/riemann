# Independent review: theta-source quotient and tensor coherence

Verdict: PASS for the corrected theorem and declared finite panel at
`b0e3b18e690accdee6d77b3b3c4c68850f6cb671`.
This review does not approve the false locally-L1 tensor-closure obligation
in the original design. The explicit regularity correction and retained
counterexample are essential parts of the accepted packet.

The reviewer read the complete theorem/design note, producer, tests and
source manifest at that exact SHA.
No frozen scientific file was edited. This audit is a separate successor.

## Analytic and algebraic proof review

1. The minimizing-lift identity is correct in the stated conjugate-linear
   convention. For H>0 and a surjection pi, J=H^-1 pi* H_Q is a right inverse;
   the H-orthogonal splitting of every lift proves the minimum-energy
   property and the maximality of H_Q among F with pi*F pi<=H.
   This maximality concerns the full metric, not its vacuum-subtracted
   excess C_Q, and requires no privileged Euclidean coordinate choice.

2. Quotient associativity follows by inverting the quotient metric.
   Multiplication of the two canonical minimizing lifts cancels the
   intermediate H_Q exactly. Covariance transforms BOTH H and G, and
   the quotient coordinates; it is not an identity-vacuum rule under
   arbitrary nonunitary changes.

3. In fixed vacuum-orthonormal adapted coordinates, 0<=H_Q-G_Q<=R11
   pays local integrability, local boundedness when assumed, and every
   rapid upper-tail bound. Homogeneity pays the exact reciprocal law.
   Its affine form makes C_Q strictly positive below t=1 even when the
   upper source has zero excess. Strict upper-side excess is not asserted
   for the generic class.

4. The tensor theorem is valid for the locally bounded subclass, or for
   locally-L1 sources only with separate local integrability of their
   tensor field. The scalar |t-3/2|^(-2/3) example disproves the original
   unconditional locally-L1 claim: its square has exponent 4/3. Assigning
   a finite value at the singular point does not repair the divergent
   integral. The amended design predates the finite calculations.
   Same-weight direct sums are valid; unequal weights are not silently
   assigned a common reciprocal scalar. No weight-zero tensor unit is
   claimed in this positive-weight class.

5. The Mellin integral converges for Re s>alpha, since the reciprocal
   source has the exact vacuum singularity at zero and an all-order
   flat remainder. The change of variables t->1/t yields
   alpha G_Q/[2s(s-alpha)] plus an entire upper-half integral. Compact
   complex parameter sets and all logarithmic derivatives are controlled
   by the all-order tail and local L1. Both endpoint residues, reflection
   and matrix Schwarz symmetry follow. Entrywise simple endpoint poles
   do not imply simple poles for a determinant of arbitrary rank.

6. The feature-kernel argument has the correct complex orientation:
   the finite Gram sum is the C_Q-energy of sum t^(bar z_j) v_j under
   dt/t. Re z_j>alpha/2 gives convergence. This is kernel positivity,
   not a Herglotz property or a zero-location theorem. Actual MP theta
   sources satisfy the stronger locally bounded hypotheses by its
   locally uniform cusp domination and continuity. Their generated
   tensor/quotient family is source-derived, not an asserted new
   automorphic representation or Euler product.

7. For finite positive compact weighting, the Schur averaging defect is
   exactly the D-weighted variance of L=D^-1 B*. Its integrability follows
   from 0<=L*DL<=A. The cross terms simplify without a commutativity
   assumption or normalization of the measure to probability. D>=dI
   pays the full-matrix equality characterization; directional equality
   is weaker. The full unrenormalized Mellin integral of H has divergent
   vacuum and is expressly excluded from this lemma.

8. The scalar vacuum example has L_alpha=alpha/[2s(s-alpha)].
   Its tensor source weight adds, whereas L3-L1 L2 has numerator
   3s^3-9s^2+5s+3 over the displayed common denominator. Thus coherent
   source tensor operations do not imply multiplication of their
   completed scalar observations. In particular these operations do
   not identify the source quotient with the old period-side Schur
   quotient, whose separate genuine poles remain intact.

The shorted-operator maximality and quotient algebra are classical.
The reviewer checked the publisher abstract of
[Anderson--Trapp, Shorted Operators II](https://epubs.siam.org/doi/10.1137/0128007),
which credits the earlier finite-dimensional treatment. Full paid text
was not obtained, and no external theorem is imported without a proof:
the finite-dimensional arguments above are self-contained. The accepted
programme content is the source/completion dictionary and its hypotheses,
not an external priority claim.

## Independent exact arithmetic

The accompanying independent script imports NO author arithmetic or
scientific producer. It reads the frozen Git fixture and sources, then
uses SymPy rational complex matrices and a constrained stationary-energy
(KKT) solve. This is independent of the producer's Gaussian elimination
and inverse-compression route.

It verifies all six base source cells, all three tensor cells and
same-weight sums, all eighteen source/vacuum nested-chain stages, both
averaging controls and the complete Mellin nonmultiplication polynomial.
The recorded quotient and minimum-energy lift are checked separately,
including nonunitary changes and both transformed vacua. Positive and
semidefinite comparisons are verified through complete exact principal
minors, not floating eigenvalues.

Additional deterministic controls cover twelve rational complex
subspaces of dimensions 2,3,4, independently comparing KKT and inverse
quotients, maximality and coordinate/lift covariance. These are reviewer
controls, not a claim of a blinded preregistered discovery campaign.
The two averaging determinants are exactly 77/2316 and zero.

The independent report records 119 KKT solves, 216 published contraction
minor checks, 100 additional contraction minor checks, 18 nested quotient
and lift comparisons, seven source identities and four scientific
artifact seals. Normal and optimized executions emit byte-identical LF
reports. The quotient stream SHA256 is
b579763fcb6c3a1bf32faf0e64c5857795c91efd35a6bcc7dc217a8b1b6bd2f8.

## Fresh execution and hostile acceptance

On the exact scientific tree plus only these review files:

- 36 source tests passed normally in 54.774 seconds.
- 36 source tests passed with -O in 51.590 seconds.
- Sixteen additional fully resealed hostile reports were rejected in
  EACH mode through the actual unmocked full validator. They alter
  source/vacuum energies, reciprocal data, coordinate maps, tensor
  weights/excess, sums, nested lifts, averaging values, observation
  polynomial, unequal-weight and weak-regularity assertions, source pins
  and scientific scope.
- Both producer checks passed; all four normal/-O fixture/manifest
  emits matched frozen LF bytes.
- Ruff lint/format and the full scientific-base whitespace check passed.

Frozen fixture LF SHA256:
6413c704116108ab3f1a06400087b8154297ffe13f3631436a96b49502ee3419.
Manifest LF SHA256:
12ebd09865d1b184d08fd519a8801970457854d42f93789ecd69e2ddbb0d0f7a.

Use system Python with SymPy for the independent matrix helper.
The scientific producer and hostile helper use only the standard library.
All commands use -B; repeat with -O:

    python -B research/l-families/atlas/generalized/theta_source_coherence_independent_review.py
    python -B research/l-families/atlas/generalized/theta_source_coherence_hostile_review.py
    python -B -m unittest discover -s tests -p test_theta_source_quotient_tensor_coherence.py

The exact finite evidence does not machine-prove the infinite source
quantifiers. Those are the written proof obligations reviewed above.
Preferred flag selection, Euler compatibility, an arithmetic purity
principle, critical-line zeros and RH/GRH remain unproved.
