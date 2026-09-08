# Exact Mobius work balance and boundary resonance

Status: **PROPOSED COMPONENT THEOREMS WITH COMPLETE PROOFS; REVIEW PENDING**.
RH and the critical source-domain completion remain unproved.
Date: 2026-09-06. Author: Astra, continuing PR #804.

Frozen source head: `b1a922f9e452cdd5c465a5c6214d51f8a1fc9090`.
This directory is add-only. It does not modify its four predecessor packets,
main, any reviewer report, the canonical graph, or the formalized library.

## Read first

- `WORK_IDENTITY.md`: exact four-state rational realization, positive future
  storage, literal Mobius work, and the OPEN subpower upper bound.
- `RESONANCE.md`: a finite-interval adjoint proof of sharp critical-line
  resonance lower bounds, including multiplicities and the compact inverse.
- `ATTEMPT.md`: attempted closure, exact failure, and what was not proved.
- `CLAIMS.tsv`, `EDGES.tsv`, `SOURCES.json`, `EXTERNAL_INPUTS.md` and
  `VALIDATION.md`: scope, dependencies, provenance and execution boundaries.

## Main outputs

The entire finite-input energy is

    J_N = D_N + W_N = H(log N) + x_N*Qx_N.

The positive last term is the complete infinite future of the stopped input,
not an omitted arithmetic tail. Q and the state update are explicit rational
four-dimensional objects. The remaining upper bound is on signed work W_N;
passivity supplies the opposite inequality and does not prove it. The actual
source has W_3>1/20, refuting universal diagonal domination.

Critical-line zeros alone force H(T)>=cT and J_N>=c log N eventually. The
finite-packet theorem retains multiplicities and derivative factors without
assuming RH or a global explicit formula. Applied to the parallel compact
inverse, it sharpens its input-energy divergence to a logarithmic lower
bound. No conclusion that output approximants must diverge follows.

The fixed directed computation covers all events n<=65536 and fifteen
checkpoints, with every stopped-input future accounted for. It is not a
cofinal positivity certificate, an estimate of growth beyond the cutoff,
or a new numerical zero census.

## Replay

    python checks.py --expect checks.normal.json
    python -O checks.py --expect checks.optimized.json
    python certify.py --expect certificate.normal.json
    python -O certify.py --expect certificate.optimized.json
    python validate.py

The scripts are standalone except that bounded symbolic checks use SymPy.
The directed source producer itself uses only the Python standard library.
Publication state is recorded outside this hashed directory in the handoff
receipt; no README claim substitutes for a verified remote write.
