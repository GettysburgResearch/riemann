# Re-identification and publication provenance

The supplied Q4 route used identifiers that now collide with the independently
published critical-resonance route in PR #597. Publication therefore applies
the following collision-only map:

| Supplied identifier | Published identifier |
|---|---|
| `L-95500` | `L-95520` |
| `L-95501` | `L-95521` |
| `R-95500` | `R-95520` |
| `T-95500` | `T-95520` |
| `X-95500` / `X95500` / `x95500` | `X-95520` / `X95520` / `x95520` |

Paths, internal cross-references, equation tags, replay schema, and replay
verdict were changed consistently. The retained result was regenerated from
the re-identified verifier, producing proof-object SHA-256
`efd06455c291019ae7a0f500d6cebfe9313e5d58cbec58789aeb4b0b5609f5ad`.

The only non-identifier change inside the seven scientific files is a
publication-hardening edit to `verify.py`: the retained JSON is now written
with explicit UTF-8 encoding and LF newlines, making its bytes stable across
Windows and POSIX hosts. No definition, formula, theorem, proof status, or
scientific conclusion was changed.

## Relationship to sibling Q4 successors

- PR #595 proves one-sided subpower sufficiency and finite moment compression.
- PR #597 analyzes critical resonance and a classical subexponential gain.

Neither sibling contains or supersedes this route's arbitrary zero-moment
tower, intrinsic order-two/order-one cancellation at `z=1/2`, or the stable
filter barrier. All three are separate successors of the exact PR #580 head.

SACF, FOCC, OCHD, and RH remain open exactly as stated in the supplied packet.
