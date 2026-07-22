# Cross-disciplinary transfer ledger for Issue #32

Agent: `gpt56-06`  
Date: 2026-07-23  
Purpose: search outside the repository's conventional RH-equivalence atlas for
theorem shapes that solve current certification bottlenecks.

Inspection levels:

- **FULL** — full primary text inspected;
- **ABSTRACT** — publisher abstract/metadata inspected;
- **DOCS** — official software documentation inspected;
- **SECONDARY** — used only for orientation, never as the sole support for a
  mathematical claim.

## Source ledger

| ID | Field | Source | Level | Exact imported fact | Repository use |
|---|---|---|---|---|---|
| S-3201 | analytic number theory / Pick functions | J. C. Lagarias, *On a positivity property of the Riemann xi-function*, Acta Arith. 89 (1999), 217--234 | FULL | RH iff `Re(xi'/xi)>0` on `Re(s)>1/2`; Theorem 1.1 gives the general zero-half-plane criterion; equation (1.19) identifies a Pick function | D-3201, L-3201; foundation of the passivity route |
| S-3202 | erratum audit | J. C. Lagarias, correction, Acta Arith. 116 (2005), 293--294 | FULL | Corrects Lemma 3.1 and the sign of `1/(s-1)` in equation (3.8); foundational Theorem 1.1 remains in force | prevents a wrong evaluator formula |
| S-3203 | function theory / sampled PSD tests | A. Hinkkanen, *On functions of bounded type*, Complex Variables 34 (1997), 119--139, doi:10.1080/17476939708815042 | ABSTRACT plus Lagarias's detailed description | Sample-dependent PSD matrix conditions can characterize bounded-type half-plane maps and yield RH inequalities | historical prior art; cautions against claiming novelty for matrix positivity itself |
| S-3204 | passive systems / interpolation | C. I. Byrnes and A. Lindquist, *On the Duality between Filtering and Nevanlinna--Pick Interpolation*, SIAM J. Control Optim. 39 (2000), 757--775, doi:10.1137/S0363012999351115 | ABSTRACT | Positive-real rational functions and Nevanlinna--Pick interpolation are central in systems, circuit synthesis, filtering, and robust control | M-3201 proposal mechanisms and terminology |
| S-3205 | passivity optimization | A. Fazzi, N. Guglielmi, C. Lubich, *Finding the Nearest Passive or Nonpassive System via Hamiltonian Eigenvalue Optimization*, SIAM J. Matrix Anal. Appl. 42 (2021), 1553--1580, doi:10.1137/20M1376972 | ABSTRACT | Nonpassivity can be localized/quantified through structured Hamiltonian eigenvalue optimization | inspires cluster scoring; not a proof step |
| S-3206 | data-driven rational realization | A. C. Ionita and A. C. Antoulas, *Data-Driven Parametrized Model Reduction in the Loewner Framework*, SIAM J. Sci. Comput. 36 (2014), A984--A1007, doi:10.1137/130914619 | ABSTRACT | Loewner matrices and barycentric formulas construct rational transfer models directly from samples, with pointwise error diagnostics | reconnaissance surrogate for `xi'/xi`; never direct evidence |
| S-3207 | rigorous numerics | FLINT 3.6/3.7 official `acb`, `acb_dirichlet`, and Arb documentation | DOCS | complex balls, `zeta_jet`, Riemann--Siegel jets, `xi`, and `digamma` are implemented with rigorous bounds | concrete producer/checker path for M-3201 |
| S-3208 | multiplicative number theory / convex duality | L. Alaoglu and P. Erdos, *On highly composite and similar numbers*, Trans. AMS 56 (1944), 448--469, doi:10.1090/S0002-9947-1944-0011087-2 | FULL for definition and factorized maximization context | CA numbers maximize `sigma(n)/n^(1+epsilon)` for some epsilon | L-3203 support-line interpretation |
| S-3209 | semidefinite optimization / signal processing | T. Roh and L. Vandenberghe, *Discrete Transforms, Semidefinite Programming, and Sum-of-Squares Representations of Nonnegative Polynomials*, SIAM J. Optim. 16 (2006), 939--964, doi:10.1137/040612646 | ABSTRACT | one-variable nonnegative trigonometric polynomials have structured SDP/SOS formulations | candidate global carrier envelopes; mapping gap remains |
| S-3210 | robust control | T. Iwasaki and S. Hara, *Generalized KYP lemma: unified frequency domain inequalities with design applications*, IEEE TAC 50 (2005), doi:10.1109/TAC.2004.840475 | ABSTRACT | frequency-domain inequalities over finite ranges can become LMIs | candidate carrier certificate only after a rational state-space reduction |
| S-3211 | proof logging / combinatorial optimization | D. Vandesande, J. Coll, B. Bogaerts, *Certified Branch-and-Bound MaxSAT Solving*, AAAI 40 (2026), doi:10.1609/aaai.v40i17.38449 | ABSTRACT | modern branch-and-bound look-ahead and pseudo-Boolean encodings can emit checkable proof logs | workflow transfer to Issue #25; no new Robin inequality |
| S-3212 | validated dynamics | A. Szymczak, *A combinatorial procedure for finding isolating neighbourhoods and index pairs*, Proc. Roy. Soc. Edinburgh A 127 (1997), 1075--1088, doi:10.1017/S0308210500026901 | ABSTRACT | finite cubical isolating neighborhoods and Conley-index computations can certify invariant dynamics | speculative de Bruijn--Newman continuation transfer |
| S-3213 | multiplicative number theory / CA completeness | G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*, J. Math. Pures Appl. 63 (1984), 187--213 | CITATION plus multiple later restatements; original full text pending | Later literature attributes Proposition 1, p. 204, the result that RH false implies infinitely many CA violations | T-3201 corrects the route classification; direct source audit still required |

## Candidate-transfer audit

### A. Positive-real passivity of `xi'/xi` — **promote now**

**Native field:** passive electrical networks, Herglotz/Pick functions, robust
control.

**Exact bridge:** Lagarias supplies the half-plane positivity equivalence. The
new repository kernel in L-3202 is a direct zero-resolvent Gram sum under RH.
A negative scalar or fixed-vector Pick Rayleigh interval is a finite
counterexample certificate.

**Why it is useful:** finite point evaluation is much lighter than contour
winding; control theory supplies adaptive sampling and nonpassivity-ranking
machinery.

**Falsifier:** any normalization error, failed functional equation, denominator
containing zero, or negative result not reproduced by direct ball evaluation.

**Novelty label:** not claimed as new mathematics in the literature. The
operational certificate, repository normalization, proof architecture, and
connection to current routes are new work for this repository.

### B. CA transitions as thermodynamic supporting lines — **promote now**

**Native field:** convex duality and equilibrium phase diagrams. `epsilon` is a
chemical-potential-like slope; CA states are exposed free-energy maximizers.

**Literature correction:** Robin's Proposition 1 is consistently cited as
showing that RH false implies infinitely many CA violations. The original paper
was not directly obtained, so T-3201 preserves a source-audit blocker and is marked `PARTIAL` rather
than treating the citation as proved inside this branch.

**Exact bridge:** co-maximizers give a global support line for
`(log n,log(sigma(n)/n))`; the logged Robin barrier is concave, so two endpoint
certificates cover the entire interval (L-3203). This supplies a constructive
finite-prefix version of the literature-level completeness result.

**Why it is useful:** it corrects X-0201's classification from merely heuristic
subsequence scanning at the route level, and can convert its huge event stream
into whole-integer coverage after exact event certification.

**Falsifier:** inability to prove common global maximization at one exact
`epsilon`, unresolved event order, or non-strict endpoint enclosures.

### C. Generalized KYP/SOS for carrier-shifted Weil searches — **retain as speculative**

**Native field:** robust control and FIR filter design.

**Desired bridge:** replace dense frequency/carrier scans by an LMI or SOS
certificate valid over a continuous band.

**Blocking mismatch:** the prime block contains many incommensurable
frequencies `log p/(2pi)` and the full Weil functional is not yet represented
as a finite rational state-space transfer function. Applying KYP directly
would be analogy, not theorem.

**Next falsification experiment:** derive an exact finite rational realization
for one fixed compact-support basis and one finite prime block. If the resulting
frequency inequality is not rational/trigonometric-polynomial in one common
phase, abandon the direct LMI claim.

### D. Loewner rational reconstruction for hidden pole localization — **use only for proposals**

**Native field:** data-driven system identification.

**Desired bridge:** fit `xi'/xi` from samples and use surrogate right-half-plane
poles/passivity violations to propose exact evaluation points.

**Blocking mismatch:** interpolation at finitely many points supplies no
uniform analytic error bound by itself. A surrogate pole is not a zeta zero.

**Safe use:** reconnaissance only, followed by L-3201/L-3202 direct evaluation.

### E. SAT/MaxSAT proof logging for Robin branch-and-bound — **workflow handoff**

**Native field:** certified combinatorial optimization.

**Bridge:** encode exponent choices and subtree coverage in a proof log checked
by a minimal verifier, separating search correctness from certificate
correctness.

**Limit:** pseudo-Boolean proof systems do not natively certify transcendental
Robin endpoint inequalities; those must remain external exact/ball lemmas.

### F. Conley-index continuation for de Bruijn--Newman flow — **defer**

**Native field:** computer-assisted dynamical systems.

**Desired bridge:** certify persistence or bifurcation of zero configurations
under heat flow using isolating blocks rather than tracking individual roots.

**Blocking mismatch:** the state is an entire function/infinite zero ensemble,
not a finite-dimensional map with a presently available isolating
neighborhood. No finite reduction with rigorous truncation has been derived.

## Exclusion map

This work deliberately does not repeat the conventional RH-equivalence atlas
in draft PR #21, the hinge lemmas in draft PR #33, the existing Weil/Robin/Li
implementations, or the contour and Speiser issue statements. It imports
machinery whose native problem is passivity, convex duality, model
identification, proof logging, or validated dynamics.
