# Sources, attribution and reproducibility lock

## Primary supplied paper

Ashay A. Burungale and Ye Tian, A proof of Sylvester's conjecture,
arXiv:2609.14893v2, printed date 15 September 2026.
https://arxiv.org/abs/2609.14893v2

The user-supplied 48-page PDF is the mathematical source for this import.
Its SHA-256 is
7b9d080156a764bc72d42f072ea44da7c32fb590d5bfb50229a76c054b70cca1.
Direct arXiv PDF retrieval and web screenshot attempts failed in this pass;
therefore no claim of independently matching current arXiv bytes is made.
The supplied PDF pages 24,33,42,43 were rendered and visually inspected for
the sign, projector and explicit-lift formulas used by the checker. The
machine-extracted full text was available as well. The full PDF is not
redistributed in this Git packet.

Most relevant places: Theorem 1.1; Sections 6.1-6.3, especially (6.5),
Proposition 6.7 and the sign table; Proposition 7.10; Lemma 8.6 and Theorem
8.7; Appendix A.2-A.3; Appendix B.4's exact/numerical distinction.

Imported: the global analytic-rank theorem and its cited arithmetic/analytic
dependencies. Checked here: three exact local reductions, both finite group
ring identities at five orders, good-prime coefficient algebra and elementary
rank-deflation statements. Not independently verified: global modular/CM
identification, full Galois orbit, nondivisibility fields, global non-torsion,
and Gross--Zagier. Local computational checks do not imply those inputs.

## Classical external inputs

M. N. Huxley and N. Watt, Mertens Sums requiring Fewer Values of the Mobius
function, arXiv:1807.05890 (2018):
https://arxiv.org/abs/1807.05890
Short-source inversion and its Meissel/Linnik/Vaughan antecedents are prior
art. This packet's use of them is not a novelty claim.

The prime number theorem pi(x)~x/log x is the only analytic input to the
new prime-block asymptotic. An independently sourced primary account of a
formalized proof is Mario Carneiro, Formalization of the prime number theorem
and Dirichlet's theorem, arXiv:1608.02029 (2016):
https://arxiv.org/abs/1608.02029
We import that standard theorem; we did not run its Metamath formalization.
Partial summation and the shell constant in PROOF_NOTES.md are derived here.

## Repository sources actually examined

- First #903 notes at 67132424e3cbe35a94752581a5b5271ab8bfc56f:
  PROOF_NOTES.md and the PR description; the prior conversation contains all
  five originally written files. CORRECTIONS.md records their limitations.
- #848 NSR26 at 617cfaca6130addd2d16bbce6af117a55aef761b:
  standalone/2026-09-19-newton-resonance-stress/PROOF.md and README.md.
  Source-first reconstruction and P=1,6,30,210 are independently replayed.
  The large resonance counterexample is NOT rerun.
- #848 RCB26 at 7de75c02417d5d8db7eafb1ceba364380e72d16a:
  standalone/2026-09-19-newton-rough-core/PROOF.md, read through the supplied
  kernel, block and completion-interface discussion. We do not certify all
  its dependency proofs or claim its within-block theorem as our result.
- Programme #738: objective, quadratic-twist scope, central-zero/rank and
  source-normalization requirements. This packet is a cubic-twist extension.

The source ledger is a targeted reading record, not a whole-repository audit.

## Transfer limit

The Sylvester boundary lives in a finite isogeny kernel and detects arithmetic
nondivisibility. Dividing a complex Hilbert-space vector by a nonzero scalar
cannot reproduce this phenomenon. The paper's nonvanishing conclusion also
cannot be substituted for a required Newton upper bound. The native cutoff
boundary and its GL(2) generalization are coefficient identities, not asserted
Tate cohomology classes. Their quantitative use still requires new signed
arithmetic control.
