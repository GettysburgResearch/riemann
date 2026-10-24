# Exact-commit fourth-pass review receipt

24 October 2026. Reviewer: `new_work_bridge`. This receipt is outside the
mathematical packet. No remote write or change to frozen mathematical
bytes was performed by this reviewer.

## Frozen object and verdict

Repository: `GettysburgResearch/riemann`.

Mathematical commit:
`8c88fd23300bba093ce2f78295c4e27dbd60147d`.

Directory:
`standalone/2026-10-23-structured-moment-gains/fourth-pass/`.

**Verdict: the exact remote files match the reviewed local mathematics,
the manifest is internally consistent, and the formal checker replays
in both required modes. No blocking issue remains within the reviewed
scope described below.** This does not certify a smaller global
zero-free half-plane or reprove the analytic imports.

## 1. Exact remote-byte authentication

I fetched `SOURCES.json` and every one of its 13 components separately
through the GitHub connector, always using the full mathematical commit
above as the explicit `ref`. Each result was saved by its returned UTF-8
content into a new directory:

`new_work_lane/pass4/frozen_8c88/remote_bytes/`.

For each of the 14 files I recomputed the SHA-256 hash and the Git blob
SHA-1, the latter using the exact `blob <byte-count>\0` prefix. Every
computed Git blob agrees with the connector's returned blob. All 13
component byte counts, SHA-256 hashes and Git blobs agree with the
manifest. The manifest itself was independently hashed and compared
with the local publication copy; it does not purport to hash itself.

All 14 files equal their local repository copies byte for byte. The ten
mathematical author files also equal their frozen lane copies. The
README equals the final composition-reviewed version. Thus the earlier
hash-bound reviews apply to these remote mathematical bytes without an
editorial equivalence assumption.

| File | Bytes | SHA-256 | Git blob SHA-1 |
| --- | ---: | --- | --- |
| CUBIC_POWER_RECTANGULAR_EXTENSION.md | 5941 | `30b3df5f463bf6735b04dc22dfb2bf62f5287d5ae3b827870302eef43ebfc96e` | `76c918569c74899cd9fab17fa6716066a9f41d96` |
| CUBIC_RAW_CONSUMER.md | 8350 | `5a2b2627dea424665ad5b1733a6a1e307ff4503a83819d23b3a94eb017c035e0` | `4402fd254e92503029e4f6c23480bc4d2dda9d61` |
| M2_CAPACITY_AND_RECIPROCAL_CHECKS.md | 7269 | `5fdea43698ea35e7d50d56bbbb937ae18c2e8084d0c2abcf3861c9685dedd4df` | `35bd2d7449112a17598cd11989f5092d46546dfb` |
| MOBIUS_DIVISOR_COEFFICIENT_ADAPTER.md | 20242 | `8d2b8e49149008a4541b8d6e8b993254252f124c2259241d24d65f4d6ce1bb7d` | `47e4b309a4aaee51875392349c465724e79d71ea` |
| MOVING_SEXTIC_TWIST_EXTENSION.md | 9946 | `b43ee0452b171420aad77f5dc345c65b12ada1a269c8228ea9bebf95c804ee23` | `f3dc04185843af6407d23a9acce2ebe457df1303` |
| NATURAL_PRESENTATION_TWIST_EXTENSION.md | 12291 | `fda494d598fa01a5f6c652b9bf503bad2fc95f4fe1a3af7e594b41b43ce6775f` | `56bd05436cb342741bf571fa4dc489009a19c48c` |
| PRIME_AMPLIFIER_COMPLETION_AND_KERNEL.md | 21824 | `c16494980a4c5a9264cad605150cf38ce9839652fdf5f183c76dba7a500ae623` | `d9350e6ab3ad0847939a6f47774fd907f9b1060e` |
| README.md | 12358 | `0cd4600baf0a407fae3f5b8a89361c2dc9375fd3094ffbf58cdb99374598aa3a` | `4097ccb54140e69807c09d8a88d8e3e85b5f4ba8` |
| RECTANGULAR_EXPONENT_OBSTRUCTION.md | 7221 | `543b36ecc9171594957ac895510bc3156db84b5d8af69efa75f89bb7251f5b56` | `7df1292e36c7461b1882e6b1eb871d43d9f622d3` |
| ROOT_NUMBER_FOURTH_MOMENT_SMALL_CORE.md | 12264 | `a12398f93f73d1f769fd97e95490ab4648894cba899c41c836f17b06f8846546` | `cdd4680d862ba7f84eba38802d6ed4f5895efc94` |
| SIXTH_MOMENT_ROOT_NUMBER_REDUCTION.md | 18267 | `071bf3c7f9d6ec109e92e016f8fbeb8dd0ad75356e538ebb39316eee7ee1c10f` | `6af12589ad6ec03e34d49eaa4733abdc92f393fa` |
| SOURCES.json | 15967 | `d510252bcd6241575dbd5a7669a9be3dcf199b0f366640bdf2fdb3096c0eacba` | `28ba5e748adcc08a24724e41cd49dcbb293f42c3` |
| check_cube_amplification.py | 4967 | `9c0ab571a8d3acf0af34fa7fa9d3c3bdfb11a47418ab8fdf739074307785fcd0` | `2ccb86e092a0f5efcf7daaf9938f00b64a63a75b` |
| cube_amplification_report.json | 423 | `f4598895d8947823d1a446cc30116b277efc1beb1c8affee1851355a553b1811` | `781afa54c322730e186051d616448ac417fb54bc` |

The machine-readable evidence is `BYTE_AUDIT.json` alongside this receipt.
`REMOTE_FETCH.json` records the exact connector responses used to create
the fresh directory. These are review evidence, not changes to the
mathematical packet.

## 2. Formal checker replay from the fresh remote bytes

I inspected the remotely fetched checker and ran, from the fresh
`remote_bytes/` directory:

```sh
python3 -I -S -B check_cube_amplification.py
python3 -I -S -B -O check_cube_amplification.py
```

Both processes exited with code zero. Their complete stdout strings
are identical to each other and to the remotely fetched
`cube_amplification_report.json`, byte for byte. The report contains:

- 27 formal multiplicativity and normalization checks;
- 6,912 complete cube-amplification checks, with natural zeros;
- 1,331 full divisor-square fibre checks;
- 174 instances rejecting omission of the required divisor in the row.

`REPLAY_AUDIT.json` records the commands, exit statuses and exact report.
The checker uses an exact integer reciprocity model in the Eisenstein
ring. It neither evaluates primitive Gauss sums nor proves any analytic
estimate. Optimized Python still checks its explicit `demand` calls.

## 3. Mathematical review scope and authorship

This reviewer independently checked the following authored work before
the remote freeze, at the identical hashes listed above:

- The rectangular cubic-power identity, its all-row fibre bound, profile
  uniformity, and shortened-column range.
- The full cubic raw consumer's primary-coset Poisson normalization,
  complex dilation, exact f,m,l weights, masks and diagonal treatment.
- The odd-local moving sextic-twist extension, including its conductor
  budget, unmasked Gram placement and distinct small-parameter handoff.
- The signed fourth-moment small-core component, including its primitive
  nonprincipal AFE, exact conjugate cubic orientation, d4 coefficient
  mass, conductor condition, common profiles and growing-height tails.
- The fixed-divisor adapter's Sections 2--4 and its Section 8 modification:
  exact Euler identity, powerful support, bounded convolution-factor
  argument, both large-divisor tails and natural-presentation handoff.
- The sixth-moment note's exact root-number, AFE and angular Poisson
  reductions in Sections 2--5, and its final orientation addendum.
- The two specified exponent-limitation notes and the README's composition
  and scope claims. The M2 note includes the reviewed live-slot condition
  that rules out premature escape to its unrestricted zero-slot case.

The prime-amplifier note received my targeted independent check of the
finite local completion statements in Sections 2--3. I do not claim a
separate full independent analytic review of its later kernel analysis.
The coordinating agent and the other lane reviews supply the broader
packet review; their scopes should remain distinguished.

**Authorship exclusion:** I authored
`NATURAL_PRESENTATION_TWIST_EXTENSION.md`. My authentication of its remote
bytes is not an independent mathematical review. Its separate independent
review is `cubic_review_lane/pass4/NATURAL_PRESENTATION_REVIEW.md`, SHA256
`48b8a0042f0d3c3fbcfc9a533f31acee3486802c1dd287d7c897c8b6e9d931f2`,
which binds exactly the natural-extension hash in the table. The
coordinating agent separately reviewed that proof.

The complementary full dispersion and reciprocal audit of the divisor
adapter is `cubic_review_lane/pass4/REVIEW_MOBIUS_DIVISOR_HANDOFF.md`,
SHA256 `47d69cce48cc8568abfeb06a8a3ff9f0e38bfa349df4d89c2ca99aec3d28e8db`.
It explicitly covers Sections 5--8 subject to the independently checked
exceptional estimate. I read both of these separate review receipts and
verified their hashes while preparing this exact-commit receipt.

The detailed local receipts from this reviewer are:

| Receipt in `new_work_lane/pass4/` | SHA-256 |
| --- | --- |
| REVIEW_CUBIC_RECTANGULAR_EXTENSION.md | `58040ac9418069a356640284f33624cc01bcf05cea1f96bb25c3808b42cf1820` |
| REVIEW_MOVING_SEXTIC_TWIST_EXTENSION.md | `7c7ca2b8ea7e6c71274e0b0669ad1fdea147524aa3bca951b55cef6f58759341` |
| REVIEW_ROOT_NUMBER_FOURTH_MOMENT_SMALL_CORE.md | `afb82c0ed1f5c941bd6e424da5ab81d371f0eedae0009801ddb63fea4aa8e1ad` |
| REVIEW_MOBIUS_DIVISOR_COEFFICIENT_ADAPTER.md | `c3c5bdc0da80c1acbd5a5205a8c86b51e2295ffba5e9f986f552eca0b7005888` |
| REVIEW_SIXTH_MOMENT_ROOT_NUMBER_REDUCTION.md | `665fd1246fd7668cb0a2ab2685895c80fba940267e358ad9bbac74036c2b1c96` |
| REVIEW_FOURTH_PASS_COMPOSITION.md | `df737fab6c4d641a3fe7472bb039d1619004d1cd1505e570d4c6d62ec6479bfe` |

## 4. Exact conclusion and remaining gap

The combined coefficient theorem has its explicit all-finite-character
zero-free premise, fixed angular order, fixed divisor order, and common
moving natural presentation. The complete presentation radical is
bounded by B^(2/3) in the large-row range and by the stated shortened
column bound in the rectangular range. Its positive saving is
existential. The signed fourth-moment estimate covers only its specified
small-core component.

The cubic raw diagonal estimate needed for the example boundary
131/150 is not proved. The projection complement in PR1019 remains
uncontrolled by that projection theorem. The full sextic sixth-moment
coupling, its opposite square-frequency orientation, and nonsquarefree
sectors remain separate analytic requirements. No arithmetic
counterexample or impossibility theorem is inferred from the exponent
models. No new global zero-free boundary follows from this packet alone.

The frozen `SOURCES.json` identifies the analytic imports and the
source-qualified numerical benchmark. This receipt authenticates the
published packet and records the bounded review above; it does not
independently validate every cited external theorem, replace external
peer review, or provide proof-assistant verification. A later change to
any mathematical file requires a new byte binding.
