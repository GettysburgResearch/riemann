# Exact-commit receipt for the joint and post-reflection series reviews

**Verdict: PASS at the scopes recorded below.** The mathematical source
and review reports at commit
`1fc00c42c5c897291f4f941c4071da1d18649cfb` match the contents reviewed
in `INDEPENDENT_JOINT_SERIES_REVIEW.md` and
`INDEPENDENT_POST_REFLECTION_REVIEW.md`. Every checked current working
file was also byte-for-byte identical to its committed blob.

**Frozen source commit:**
`1fc00c42c5c897291f4f941c4071da1d18649cfb`.

**Verified parent commit:**
`9959364671f89b86f3992ec5ed5e19f804eb607b`, the PR #915 baseline.

**Observed HEAD at verification:** the same frozen source commit.
The working tree was clean before this receipt was written.

**Reviewer:** the independent joint-series review agent. This receipt
was written after source freeze. No source or existing review file was
edited in this exact-commit pass. The receipt is not itself part of the
source commit it authenticates, and a later commit containing the
receipt does not change the frozen source identity.

## 1. Committed mathematical targets

Paths in this table are relative to
`standalone/2026-10-10-theta-support-descent/`.

| File | Git blob ID at the frozen commit | SHA-256 of exact blob bytes |
| --- | --- | --- |
| `EULER_DOMAIN_EXTENSION.md` | `c6c605b717e5bf0a8f5dd532517b1a8572cb29b4` | `56ab7e05b0fde19c82eeea5f274da212bf63f07ac084de1b08c3d8c48aa78a2a` |
| `DEFORMED_GAUSS_CONTINUATION.md` | `d91fe4491b9f192a60733e69e921554e5b4389a7` | `b01b17194884b3e2331d9f668ee71abb33a5e2f1e047d16cb2e906a1c5b32c81` |
| `POST_REFLECTION_EULER_CONTINUATION.md` | `3a28bbd99315ea0b4e469c7e9cef5456f49c6a1a` | `7ddcaf96aba2f109fb5696880ed9098e435712e2075613e72474b76fc00a3072` |

All three SHA-256 values equal the final mathematical source hashes
recorded in the two substantive reviews. In particular, the final
post-reflection hash includes the inspected clarification that
`chi_p(-1)^2=1` removes its character factor separately from the
remaining exponent reductions modulo six. No formula changed in that
clarification.

## 2. Committed independent review reports

| File, relative to this packet | Git blob ID at the frozen commit | SHA-256 of exact blob bytes |
| --- | --- | --- |
| `INDEPENDENT_JOINT_SERIES_REVIEW.md` | `a4d59f2500c7da51cc635e8cd491f2f20ee27b27` | `5f98ea72a5a8b4df17740f4aa5f96088b72551c321be72c9c78233d67ea108d5` |
| `INDEPENDENT_POST_REFLECTION_REVIEW.md` | `811d2d5bf3396ab0e8bb26ea3db3709ac9c5a6a5` | `4544620167361ebff1274890f1aae9b94eb648348ee8826dc9898fe318fa91d5` |

Both committed reports are byte-for-byte identical to the working
copies authored by this reviewer. Their report hashes are explicitly
bound by this receipt; the mathematical source hashes they contain
were independently checked before freeze and again against the
committed source blobs in this pass.

## 3. Load-bearing dependency identity checks

The following additional committed blobs match the dependency hashes
recorded in the substantive review. Their current working copies also
match the committed bytes. Packet paths are relative to this directory;
the remaining paths are identified below the table.

| Dependency | Git blob ID at the frozen commit | SHA-256 of exact blob bytes |
| --- | --- | --- |
| `HIGHER_ANGULAR_SECOND_MOMENT.md` | `956445e9baa91356a352cc089852dbf34f90dbef` | `82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959` |
| `OPPOSITE_DERIVATIVE_REFLECTION.md` | `2966032ea89396ec2e0a423b1b23841645a1fb47` | `9532f14dc452edf9a50e7ec905e0629c54d510fd9937c5d8c19bcf7dfb4e9ccb` |
| Inherited `REUNITED_RAMANUJAN_EULER_PRODUCT.md` | `bc6b01263b5d3c0006c275c957d1854fcf7f506a` | `6d1f0e01d8645972de0c38897e37633d8bfc70d193f6e279dcf8f33b0e992433` |
| Inherited `NEGATIVE_BRANCH_DIRICHLET_SERIES.md` | `d061eab036051e8a2bd9a636a5be51b4ec067e6b` | `025b1f9507f7aff3794d93e80a10337e61732944ec3ba1cb28107c8a7d59326e` |
| Retained October 5 `paper2.tex` | `2000faddbbebac5de0ecfe0b962534ea61a852d5` | `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d` |

The two inherited Markdown files are in
`standalone/2026-10-10-sextic-critical-core/`.

The exact primary-paper path, relative to the repository root, is

`standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`.

That retained paper is attributed to OpenAI/math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The check here confirms
its committed bytes against the physically reviewed import; it does
not claim a new independent reconstruction of the upstream repository
or its formal implementation.

## 4. Verification actually performed

The pass resolved the requested source commit and its parent with Git,
resolved every path above to its actual committed blob ID, read each
blob with `git cat-file blob`, and computed SHA-256 over the exact
returned bytes using Python's standard `hashlib` implementation. It
then compared the eight mathematical/dependency digests with the
previously recorded review hashes and compared every one of the ten
committed blobs with its current working-file bytes.

All eight expected source digests matched. All ten working-file
comparisons matched. The parent and observed HEAD matched the stated
commits, and `git status --short` returned no changes before this
receipt was added. These are committed-byte and provenance checks;
the substantive mathematical verification is in the two bound
reports, including their independent exact algebra calculations.

## 5. Mathematical scope attached to this commit

The exact-commit PASS attaches to the following conclusions, with the
hypotheses and exclusions in the substantive reviews retained.

1. **Fixed-index Euler extension.** The local extraction identities,
   normally convergent remainders, finite-order nature of the newly
   extracted reciprocal, and stated fixed-index continuations check.
   The character types, moving masks, and both numerator conductor
   costs are retained. Ordinary Hecke continuation is an explicit
   analytic input.

2. **Complete reunited-series continuation.** The cube factor cancels
   exactly in the conditioned divisor identity. With
   omega=Re(w), sigma=Re(s), the normally convergent representation is
   valid on

   \[
   \omega>1,\qquad \omega+\sigma>2,\qquad
   \omega+\tfrac32\sigma>\tfrac52,\qquad
   \omega+3\sigma>\tfrac52.
   \]

   The uniform conductor exponents A(sigma), B(sigma) and the stated
   polynomial vertical bounds follow from the source theta
   functional equation and the full dual local majorant. This main
   complete-object theorem does not use an angular zero-free theorem.
   The distinct bare-Gauss consequence beyond Re(s)=17/36 retains its
   stated dependence on the companion angular reciprocal theorem.

3. **Post-reflection Euler continuation.** The exact Gauss and angular
   cancellation leaves the negative Ramanujan sign and a finite-order
   reciprocal L-function. The complete standard-face object continues
   meromorphically to

   \[
   \Re v>\tfrac12,\qquad
   \Re s<\min(0,\Re v-1),\qquad
   w=v-3s+\tfrac32.
   \]

   Its possible poles have the stated fixed finite-order divisors.
   Under the common finite-order zero-free boundary beta<1, the
   refinement Re(v)>beta is holomorphic apart from the possible
   simple principal-kappa pole at v=1, whose residue is specified by
   the convergent formula (5.2). The pole-removed joint polynomial
   bound has row cost `Q^(1-2 Re(s)+epsilon)`.

The imported theta automorphy, finite local transformation, and cusp
coefficient interfaces remain source assumptions. The finite-order
zero-free refinement retains its additional zero-free assumption.
Hashing the complete higher-angular file does not enlarge this
reviewer's mathematical coverage to a fresh independent proof of its
entire canonical second-moment induction.

The conductor comparison in the reviewed arguments still yields no
generalized-moment saving. The possible residue is not identified
with an initial Poisson diagonal. This receipt does not approve the
entire branch, claim formal verification, or prove the full fourth
moment, the generalized 2k-th moment hierarchy, or RH.

## 6. Published source identity confirmation

**Verdict: PASS for the published source commit**
`6aceafc1729ca0962eb12519b407b69c3b5a4d5f`, with precisely the
mathematical scope and dependency boundaries in Section 5 above.
This section was appended after independently inspecting the fetched
published Git object. The original receipt and the two substantive
review reports were preserved.

| Identity | Reviewed local source | Published source |
| --- | --- | --- |
| Commit | `1fc00c42c5c897291f4f941c4071da1d18649cfb` | `6aceafc1729ca0962eb12519b407b69c3b5a4d5f` |
| Complete tree | `ab9ea56041c100620cd825f9d98b17734ec27d49` | `ab9ea56041c100620cd825f9d98b17734ec27d49` |
| Sole parent | `9959364671f89b86f3992ec5ed5e19f804eb607b` | `9959364671f89b86f3992ec5ed5e19f804eb607b` |

The complete tree identities and sole parents were read independently
from both commit objects. A direct tree comparison returned no changed
paths. Thus the distinct published commit identity contains exactly
the same repository tree as the reviewed local source.

In addition to comparing complete trees, this pass independently
resolved all ten paths in Sections 1–3 at the published commit and
compared their Git blob IDs with those at the local source commit.
Every blob ID was identical. SHA-256 was recomputed from each
published blob and matched the corresponding value in those tables.
All ten published blobs also matched their current working-file bytes.
Consequently the tables in Sections 1–3 are valid, unchanged, for the
published source commit as well.

Before this append, the existing receipt still had SHA-256
`f91438cec771e96e1fc90139f96717782c0b2c159d4190af90e36427341ef54e`,
confirming preservation of the original local-source receipt. This
pass changed only this receipt by adding the published identity
confirmation; no mathematical source or substantive review report
was edited.

The two scoped independent mathematical reviews therefore apply
without a new mathematical argument to the identical source tree at
`6aceafc1729ca0962eb12519b407b69c3b5a4d5f`. This confirmation does
not extend their accepted mathematical scope or remove any imported
source, zero-free, conductor, or higher-moment limitation.
