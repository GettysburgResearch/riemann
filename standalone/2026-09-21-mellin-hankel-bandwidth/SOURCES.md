# Sources, reading boundaries, and verification of previous publication

## GitHub snapshot and previous packet

Read #904 at `aaea3f9605a430600bea0189397d93ca315b5f98`, branch
`research/astra/20260919-divisor-square-mesh`. Current PR metadata, the
MCB31 directory, its checksum manifest, and individual executable/receipt
file identities were retrieved from the connected GitHub API.

The prior companion archive supplied in chat was extracted. These local
raw Git blob identities match the remote files:

| Artifact | Git blob SHA |
|---|---|
| MCB31 PROOF.md | `c96be13fabd9210f383693ed7d9794cede9177bb` |
| MCB31 check.py | `9b21098b2aebeb3ac880c439d76a7dcbdeb7144f` |
| MCB31 exact.py | `52aa363c85e67e71bf5fb15adc78a3177ab789d5` |
| MCB31 receipt.json | `8460f793699056b15fe7199b6d058d2f09ebc32b` |
| MCB31 test_check.py | `a44d7343381e2db03de4790c1068c12c66e3bedb` |

Publisher-only Markdown and publisher receipts differ from the original
companion as expected; they are not claimed byte-identical. The executable
publication is complete, so no redundant import or overwrite was needed.
The previous publisher recorded full ordinary/optimized reconstruction but
one Windows symlink-permission error in each suite. Fresh Linux replays in
this pass passed both complete reconstructions and both 12-method suites,
including actual symlink refusal. Earlier Windows scope is not rewritten.

MCB31 full report SHA-256 reproduced in both new runs:
`825800dd0f0759d787944daa23fe6cb31e5df7275b23a418e3d961e238c3c4d9`.

## Repository mathematics used

- MCB31, `standalone/2026-09-20-microscopic-composite-band/PROOF.md`, at the
  above #904 head: same smooth mask, exact product/innovation summation,
  complete mode derivative, completion price, recent-energy overlap and
  generic quadratic sharpness. Full local proof read; corresponding bytes
  authenticated remotely. The bandwidth theorem is improved here, not
  retrospectively edited there.
- NCL29, `standalone/2026-09-20-native-frequency-localization/PROOF.md`,
  preserved on #904: full angular-complement estimate, especially Section 3
  and its Fourier coefficient/Schur/tail derivation. Its extension to bounded
  multiplier weights is explained in MHB32 Section 6. This is a proposed
  repository component, not external mathematical acceptance.
- NIR26/PCR26/BNR26 on #848: innovation isometry, cap-three completion and
  short-source Newton reconstruction, read through the supplied prior proof
  packets and their exact lineage. The needed algebra is rederived locally
  or explicitly attributed; no full predecessor certificate campaign is
  claimed from this reading.
- #905 at `98cf588261473724178231c667595fc09cc216fe`,
  `standalone/2026-09-20-anchored-composite-covariance/MELLIN_DENSE.md`,
  blob `6ef0282f4e03af14dc3752549e5ad7f6cd1a61b9`: Sections 1–5 read from
  the live connector. Its complete Mellin norm, source fourth moment,
  Patel–Yang high-frequency tail and continuous Hardy adapter motivated the
  comparison. None is represented as newly discovered here. The new argument
  does not assume that its Mellin projection commutes with the #904 angle mask.
- Recent #903/#848/#905 bodies and updated covariance search received
  contextual reconnaissance, not a fresh all-repository mathematical audit.

## Primary external sources

1. Dhir Patel and Andrew Yang, *An explicit sub-Weyl bound for
   zeta(1/2+it)*, arXiv:2302.13444v1, submitted 27 February 2023.
   https://arxiv.org/abs/2302.13444v1
   The exact imported statement is `|zeta(1/2+it)|<=66.7 t^(27/164)` for
   `t>=3`, given on the primary abstract. This is a fixed unconditional input;
   its deep proof was not independently reconstructed here. No claim that it
   is currently optimal is required or made. DMC31 already uses this input.
2. Hélder Lima, *On Müntz-type formulas related to the Riemann zeta function*,
   arXiv:1705.09386v1, submitted 25 May 2017.
   https://arxiv.org/abs/1705.09386v1
   The primary abstract was consulted to establish that the Mellin/Müntz
   framework is classical. No unseen theorem of this paper is imported as a
   premise: Section 3 directly checks the needed logarithmic-kernel formula.
3. M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the
   Möbius function*, arXiv:1807.05890v1; Chebyshevskii Sb. 19(3), 2018, 19–34.
   https://arxiv.org/abs/1807.05890v1
   Primary abstract and its explicit quadratic identity consulted. Short-source
   inversion, its matrix viewpoint and relation to contour integrals are
   established antecedents, not novelty claims of this packet.

All external consultations in this pass were primary HTML abstracts; no PDF
or independent external proof audit is represented as performed. Plancherel,
finite summation by parts and elementary nonstationary integration estimates
are classical; their needed normalizations/estimates are shown in PROOF.md.

## Code provenance

`exact.py` is copied byte-for-byte from MCB31, itself an attributed NCL29
144-bit outward arithmetic excerpt. SHA-256:
`68a70dfd171a9cd66b2815197d7ad81c16c466bf96cbc981a7dad557d30c450c`.

`inherited_mcb.py` is a byte-for-byte copy of MCB31 `check.py`, renamed only.
SHA-256: `cb605c06a8b299770d618014a748071623b84d137a8ede2b833b9c9d14d006fe`.

The new producer authenticates both before use. It adds exact polynomial
centering controls, integer-root exponent evaluation, direct shell differences,
complete shell covariance and rigorously reseeded rotations. Shared backend
and same-author tests are not independent mathematical corroboration.

No full checkout, repository-wide validator, remote CI, Lean build, updated
external zero record, or independent referee acceptance is claimed.
