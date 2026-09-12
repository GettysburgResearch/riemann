# Four-route follow-up: arithmetic, gamma, Ising and branching

Status: **PROPOSED component mathematics and finite certificates; RH remains open.**

Scope: assessment and new work completed 12 September 2026, packaged for
publication 13 September in PR #869. The earlier
[three-route packet](../2026-09-12-three-route-completion/README.md) remains
at its original source. This follow-up examines pinned research through #875;
it is not an assessment of later revisions.

Start with [REPORT.md](REPORT.md), then the relevant route:

- [Arithmetic](arithmetic.md): exact covariance/annular-energy identity,
  normalized exponent, a nonnative growing counterfamily and the unconditional
  qualitative trace refinement.
- [Gamma](gamma.md): sharp shape/scale comparison, whole-current review and
  positive-density controls against moment/Fisher-only sign arguments.
- [Ising](ising.md) and [new component proof](ising-computation/PROOF.md):
  certified degree-eight seed, connected infinite continuation and full
  growth calibration; a nonzero tenth-moment discrepancy remains.
- [Branching height](height.md): uniform exponential zero-defect tail and
  convergence, and a sharper part of the sufficient cutoff with all remainder
  terms retained.

Exact dependencies are in [SOURCE_LOCK.json](SOURCE_LOCK.json), the pinned
links in each proof and the primitive provenance records. Mathematical
cross-review within the session is distinguished from external acceptance.

## Reproduction

The accepting computations use Python 3.12 standard-library arithmetic.
Run from this packet directory:

```text
python -B verify_packet.py
python -B arithmetic-counterfamily.py --write arithmetic-counterfamily.json
python -I -S -B gamma-controls.py
python -I -S -B -O gamma-controls.py
python -B height-cutoffs.py
python -B ising-computation/test_algebra.py
python -B ising-computation/test_provenance.py
python -B ising-computation/test_acceptance.py
python -B ising-computation/certify_dimer.py
python -B ising-computation/certify_dimer.py --mesh 160 --output dimer-certificate-mesh160.json
```

The Ising output path is interpreted by its script; see its
[reproduction guide](ising-computation/README.md). The optional scout uses
mpmath and is not part of acceptance. The extraction script is optional:
the exact predecessor modules are already included. Runtime reproduction of
the certificate and cutoff does not need another branch's Git history.

`verify_packet.py` checks copied-source hashes, saved exact inequalities and
local links, and regenerates the packet manifest. It does not reconstruct
theta moments or replace the source-producing certificate commands above.
The arithmetic synthetic norm panels use ordinary binary64; they are not
directed certificates. [VALIDATION.md](VALIDATION.md) states the original and
publication checks and every relevant non-replay boundary.

## Remaining completion steps

Arithmetic needs a native subpower upper estimate. Gamma needs cofinal decay
of complete signed defect production. Ising needs admissible realization at
unbounded orders. Branching needs centrality of limiting clusters or a
vanishing native defect. None is treated as a routine missing final detail.
