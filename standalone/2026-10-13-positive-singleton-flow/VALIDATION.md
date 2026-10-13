# Validation, source boundaries and reproduction

Status: same-author proof reconstruction and exact finite checks. No independent
mathematical reviewer or proof assistant was available for this pass. A new
component is not integrated merely because its files and checks are published.

## What was actually run

From this directory:

    python check_positive_flow.py > /tmp/positive-flow.json
    python -O check_positive_flow.py > /tmp/positive-flow-opt.json
    cmp /tmp/positive-flow.json results.json
    cmp /tmp/positive-flow-opt.json results.json

Both modes were run after the final code change and produced byte-identical
JSON. Full per-prime profiles are reproducible with --profiles; --max-D 64
runs just the smallest declared census while retaining the local/atom checks.
Python and NumPy are required. NumPy is used for integer Gram products, not
floating-point eigensolvers, optimization or probabilistic simulation.

The default report contains 235,666 explicit predicates including setup and
repeated unit-type zero-block checks. It is not 235,666 independent arithmetic
or asymptotic cases. Its components are:

- 625 complex pairs U=a+b*omega,V=c+d*omega with all coordinates -2 through 2;
  5,625 all-order coercivity tests for k=2,...,10; fourth/sixth identities;
  raw two-atom moments through degree 60; 121 rational kernel evaluations.
- 192 auxiliary real three-coordinate models, all masks and frozen sets,
  comparing exact Q(sqrt(5)) atom enumeration with independent polynomial
  moment contraction. This small model is distinct from the native census.
- Complete squarefree good ideal columns and complete nonzero element rows
  at D=64,128,256 with H=79,164,338. The extra D=128,y=1 case tests schedule
  dependence. The native census is not restricted to a five-prime semigroup. Its fixed
  coefficient twist is trivial; other twists are covered by the proof, not
  by this particular census.

## Primitive arithmetic and scope

Good primes exclude those above 2 and 3. A split rational prime p=1 modulo 3
contributes BOTH ideals, identified by the two roots r of r^2+r+1 modulo p.
An inert p=2 modulo 3 contributes its norm-p^2 ideal. The residue fields are
F_p in the split case and F_p[omega]/(omega^2+omega+1) in the inert case.

Each local sextic character is computed by raising the row residue to
(Np-1)/6 and comparing with powers of 1+omega. Zero residues remain exactly
zero. Prime ideals with the same norm are never identified. Ideal columns
are all squarefree products of these distinct indices under the norm cap.
The product enumeration is unique by increasing prime index.

Every nonzero row a+b*omega with a^2-ab+b^2<=H is enumerated. The chosen
coordinate box strictly contains that ellipse. The census uses the hard
column annulus D/2<Nn<=D and sharp rows, not the smooth test needed by the
asymptotic source theorem. It is a finite identity diagnostic only.

The native moment is computed directly from the column sums and separately
from pair-product Gram assembly. The Gram uses integer representations in
Z[omega]. Before its int64 products the bound 6*number_of_rows<2^62 is checked;
individual entries are -1,0,1. Column sums have at most 37 terms in the declared
cases, so their quadratic norms are also far within int64. Final weighted
aggregations and local rational calculations use unbounded Python integers
and fractions. There is no numerical-rounding premise in the recorded values.

Checks reject erasing nonunit zeros, collapsing the split norm-7 ideals,
using symmetric signs in place of the matching law, setting m4=1 while
retaining the first three moments, and assuming every restoration step is
nonincreasing. The code uses explicit exceptions rather than Python assert,
so these checks remain active under python -O.

The causal identity (15) and all-scale Rankin/Peano proofs are written proofs,
not certified by the census. Positive compensation at all orders is justified
by the analytic kernel calculation, not extrapolation from k<=10 tests.

## Source and literature audit

- #940 head 59d5a8ebcd390ff898d63b2fc5ed7290995ae58b was checked live; it remains
  an open draft. Its entire singleton proof was read from the attached preserved
  packet and its claims compared with the live PR. The recovered source SHA
  and the two earlier packet directories are unchanged by this continuation.
- #943 at 24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed was read via live GitHub:
  full DEGREE_GEOMETRY.md and PR metadata. The code here was written separately;
  it shares the mathematical residue definitions, not the #943 helper source.
  The three native M4 benchmark values are credited to that prior census.
- #942 BANDLIMITED_PRUNING.md was read in full; its Fourier support construction
  is not needed in the new proof. #941 and #943's microscopic-phase result were
  inspected at description scope and used only as strategic warnings.
- The distribution and minimum fourth moment were recognized as Mammen's
  classical multiplier during the literature check. Roodman et al. (2019),
  DOI 10.1177/1536867X19830877, was inspected in its accessible primary full
  article, section 3.3. The original Mammen DOI landing page was unavailable
  through this tool. No new-law or new-extremality priority claim is made.
- The Peano method and random-multiplicative moment literature are credited in
  MATHEMATICS.md. No external bootstrap approximation result is applied to the
  physical rows, and Harper's sharper model theorem is not invoked.

## Publication and review boundaries

The package is intended for a new branch based exactly on #940. Its manifest
records SHA-256, Git blob identity and length for every other payload file.
These hashes authenticate file bytes, not theorem correctness. Publication
must be separately checked against GitHub before claiming it has landed.

Preferred mathematical review: Sections 2-3 (kernel positivity and coercivity),
Section 5 (positive completion and literal masked causal inverse), then Section
6 (native cofactor and telescoping) and Section 7 (the unresolved inequality).
No previous scientific-status label, integrated result, or source text is changed.
