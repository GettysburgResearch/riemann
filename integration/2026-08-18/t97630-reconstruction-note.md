# Reconstruction note

The earlier local ZIP was unavailable. This packet is a deterministic faithful
reconstruction of the full quoted T-97630 cutoff-239 research digest supplied
by the user. It is deliberately distinct from PR #576 and from the later
`1/42` hardening packet. It is not claimed byte-identical to an unavailable
earlier archive.

The quoted mathematical constants, cutoff, source interfaces, `1/960` margin,
Mellin transform, and status boundary are preserved. The original digest's
intended branch was
`research/gpt56-pro/97400-corrected-p61-bias-annular-closure`; this collision-safe
archival publication actually lives at
`research/gpt56-pro/97630-cutoff239-annular-reconstruction`.

The included C++ is not the original production certificate: it checks the
`x=184` witness and the integer endpoints `67..238` only. It does not perform
the quoted full 2.5-million-endpoint sweep and contains no implementation of
the quoted analytic tail. The Python tests are likewise a lightweight contract
replay. Thus the archive preserves the digest's candidate content while
explicitly not claiming recovery of its original computational evidence.
