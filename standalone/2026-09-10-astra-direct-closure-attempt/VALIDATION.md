# Validation and limitations

Date: 2026-09-10. This is a failed completion attempt with proposed auxiliary
proofs. The finite checks do not establish RH, normalized phase monotonicity,
complete Laguerre positivity, or spectral reality of the actual theta operator.

## Source acquisition

Authenticated GitHub reads resolved PR #835 to
`4b8fa9abfa9aac5ed1feb7f30acaeeb418ed405c`. The two supplied local manuscripts
have the exact SHA256, Git blob identity and length in SOURCES.json. The current
TPR26 mathematical proof was also read through the connector at that commit.
Its accepting numerical program and the original 152-cell certificate were
NOT executed in this pass. Reading an author proof is not independent acceptance.

The determinant manuscript was read at
`f0e34780f4fe91bd5d07e791e8855189838c3df5`, sections 1--6. A later read found
PR #834 at `62bd9bbed134e20c1ee9cd92d008562079af9ceb`; the comparison and new
spectral-crowding README were read for orientation. No result from that new
proof is assumed in this packet. Recent-PR search is not an exhaustive audit.

The DLMF zero-distribution section and Csordas arXiv paper supply the named
classical context. The Csordas text and a rendered PDF page were inspected;
no broad audit of the literature or priority claim is made. An exploratory
Williams-PDF screenshot request failed; that paper supplies no premise here.

## Bounded implementation scope

The checker uses only Python standard-library integer/Fraction arithmetic.
Its five groups comprise 104 finite algebra panels:

- 64 complex first/second-jet product identities (including the phase sign).
- 16 inverse-power leading Laguerre expressions.
- Four substitutions for the theta-tail leading coefficient.
- Four normalization/quadratic-root identities for the non-theta mixture.
- 16 nonreal reciprocal-square sign panels.

These are identities and examples, not actual Xi evaluations. They do not
numerically establish analytic decay, a global zero count, any asymptotic, or
the existence theorem for critical-line zeros. No new quadrature is performed.

The CLI authenticates exactly seven regular nonsymlink files and all six
manifest entries before reconstructing its mathematical output. Its optional
receipt reader rejects duplicate keys, floating/nonfinite values, type aliases
that change canonical typed JSON, and changed results. No Python `assert`
controls acceptance. The checksum manifest is a consistency/authentication
boundary relative to this delivered packet, not an external signature.

Commands from this directory:

```
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The final execution receipts are retained outside the sealed packet. The three
test methods include two pristine CLI controls and ten altered CLI cases in
each mode: five receipt mutations and five package mutations. Two package
mutations are resealed to exercise reconstruction after checksum acceptance
(wrong source commit; wrong mixed-term coefficient). These are implementation
controls, not ten separate mathematical results.

## Publication boundary

No GitHub write operation is available in this session's exposed actions.
Discovery for create_blob/write/push returned read-only actions or none. Plugin
management found the already installed GitHub connector, not an additional write
capability. The direct `git ls-remote` fallback failed with
`Could not resolve host: github.com` (exit 128). No upload, commit, branch update,
PR creation, main edit, or settings change was performed by this continuation.

The add-only patch is intended for a new branch based on the exact #835 source.
The bundle's separate publication instructions and delivery receipt state its
local application tests. A temporary Git fixture is not a full checkout of the
Riemann repository. No full-checkout validator, previous research suite, Lean
build, remote CI, Windows run, or independent referee review is claimed.

## Mathematical stopping point

OPEN-PHASE and OPEN-CONVEX in ATTEMPT.md are unproved. The complete spectral
reality of the actual T is unproved. The modified-source examples have zeros
of those CHANGED functions only. The packet does not demonstrate a nonreal
zero of Xi and does not assert that a source-specific exact sign proof is
impossible. Its principal positive logical simplification is that proving
normalized vertical monotonicity already ends the RH implication; one does
not also need a second normalization-error domination inequality.
