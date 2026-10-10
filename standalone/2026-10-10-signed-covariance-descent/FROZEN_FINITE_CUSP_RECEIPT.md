# Frozen-source receipt: finite rays, cusp composition, and scope

**Reviewer:** signed_series_bootstrap. **Date:** 2026-10-10.

**Frozen source commit:**
`8f2acaacddc10bd8fb053a66070a1d06d25aa922`.

**Source tree:** `94bf5570710b88d2bb254cc6d274b4654411510f`.

**Parent:** `2edc467ef4dea4aa685219ac6a558a158b88768d`.

**Verdict:** the independent reviews identified below apply to these
exact committed blobs and retain their recorded **PASS** verdicts at
their stated source-conditional scopes. This receipt creates no new
theorem and expands none of those scopes.

## 1. Exact committed sources checked

I extracted each file directly with `git show COMMIT:PATH`, hashed
the returned raw bytes with SHA256, and compared them with the
pre-freeze review hashes. All comparisons passed. The commit, tree,
and parent identifiers above were independently obtained from
`git show -s --format=%H%n%T%n%P COMMIT`.

Paths below, except the explicitly marked root README, are relative
to `standalone/2026-10-10-signed-covariance-descent/`.

| Source file | Bytes | SHA256 | Independently reviewed scope |
|---|---:|---|---|
| `FINITE_RAY_REUNION.md` | 18423 | `8897088fb7e89c66e18bf0652a913983c5120a61d854591f990cce2a6261f2e0` | All numbered claims: exact actual finite-ray reunion, pole cancellation, raw continuation and bound |
| `FINITE_CUBE_HOMOGENEITY.md` | 10455 | `e4f7b3ff0817c4b6deaf2e608657425c06ac97c1a7f4f60f3762eba7eca7b0e1` | Complete finite covariance, ramified Kubota case, and prescribed character support |
| `ALL_CUSP_COEFFICIENT_ADAPTER.md` | 17208 | `bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1` | Sections 1–4 only: exact coefficients, cube law, bad-part split and character interface |
| `FULL_CUSP_DESCENT.md` | 11988 | `b025af8af1ac13d07a04fbc7de71401d2a47ef2c8df5a1e89a4edc4973482504` | Complete composition, normal summation, glued domain, row mean and quantitative limitations |
| Packet `README.md` | 14386 | `d5cf29b97288fc756b05f0616315aa0be80bc918864e9435c7b9b5e0fdd59a4e` | Complete mathematical summary and consistency with the stated proof scopes |
| Repository-root `README.md` | 11216 | `04ef86e612e0832851d24bae6aae62764d825bd4140565d9000254820fe801c8` | Only the added “Further research: signed finite rays and conductor means” section |

The scope review of the README's short-row comparison does not extend
my adapter review to its Section 5. That quantitative theorem has its
separate author and independent review. The complete-cusp analytic
composition uses only adapter Sections 1–4.

## 2. Archived review records preserved in the source commit

I also extracted and hashed the committed review records. Their
contents and source hashes match the reviews I completed before the
freeze.

| Review record | Bytes | SHA256 |
|---|---:|---|
| `FINITE_RAY_INDEPENDENT_REVIEW.md` | 7228 | `3c33812a501c1bdf9ded8540aa0571e42a0e955ffbbded65edc351796d06bf7c` |
| `ADAPTER_INDEPENDENT_REVIEW.md` | 4442 | `da7193aae9047754c3e9ada17cbfc15e9d8e252577de2d83959e20c138f25660` |
| `FULL_CUSP_INDEPENDENT_REVIEW.md` | 8158 | `06eb53eb6a2099fae54cb9f3cfe6be1cfc73e11d7d64e61142e511fc69a6984b` |
| `NAVIGATION_SCOPE_REVIEW.md` | 4541 | `88ea46badb2b1aefb1fea87d90f940ffe1a27e00b87ee112a8a52bbba95f5497` |

This new receipt does not modify those archived records or any
mathematical source file.

## 3. Authorship and dependency disclosure

I authored `SECOND_REFLECTION_BOOTSTRAP.md`. My review of
`FULL_CUSP_DESCENT.md` is an independent review of root's new
composition, including its actual finite-sector identity and all
infinite bad-label summations; it is not an independent review of my
own bootstrap input.

The bootstrap and spectral inputs were independently reviewed by
scale_covariance_attack, who authored neither of them. I read the
committed input review and verified these exact committed contents:

| Dependency or independent input review | Bytes | SHA256 |
|---|---:|---|
| `SECOND_REFLECTION_BOOTSTRAP.md` | 18957 | `e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0` |
| `SPECTRAL_ROW_MEAN.md` | 11136 | `5154dc7d0502555f9a198eed386b9926bf1769ac61ae6b7c6fa319eadec7ace1` |
| `INDEPENDENT_SPECTRAL_BOOTSTRAP_REVIEW.md` | 10865 | `a356fa28787228ac87f70fc2452918063d5f1509aaf3257faf6c5a8470f78864` |

That input review covers the entire spectral note and the
load-bearing bootstrap Sections 1–4 and 6, together with its
interface and physical comparison. It expressly limits its review of
the explanatory involution narrative in Section 5. That narrative is
not used to prove the complete-cusp continuation or conductor mean.

## 4. Frozen mathematical verdict and boundaries

The committed finite-ray proofs establish the exact cancellation for
the actual complete Fourier data, the contragredient cube law, and
the prescribed output finite-character family, retaining every source
mask. The ramified middle Kubota case and the bad nonunit arguments
were explicitly checked in the independent reconstruction.

The committed complete-cusp composition has the stated domain

\[
a=\Re(v-s)>\tfrac12,
\qquad \Re v<\min\left(a,\frac{3a-1}{2}\right),
\]

and its squarefree-row mean holds for `5/8<a<1` strictly inside
that domain. The exact cusp and bad-label identity, uniform finite
character family, geometric ramified and bad-cube tails, and
Hilbert-space norm summation all remain within the reviewed contents.

The final comparison for a hypothetical threshold `1/2<=a0<1`
is included in this receipt. Its candidate `Q D^(1+a0)` is already
covered by the factorwise bound when `Q<=D^a0` and by the
classical bound when `Q>=D^(1-a0)`. Those ranges cover every
`Q>=1`. This limits the particular contour-and-Minkowski mechanism;
it does not preclude a different signed joint covariance argument.

The complete analytic object remains the second-reflection cusp sum
of the specified standard-face Dirichlet series. Its continuation is
not an identification with the entire original Möbius moment. The
distinct short-row physical improvement described in the README
does not enlarge the old balanced D-squared row range or resolve
the long fourth-moment initialization.

All verdicts retain the declared OpenAI/math theta interfaces and
classical sieve assumptions. This receipt is an independent AI-agent
content and review binding, not a Lean proof, external human
acceptance, or independent validation of the entire imported analytic
foundation. No generalized `2k`-th moment theorem, `17/24`
zero-free conclusion, or proof of RH is certified here.
