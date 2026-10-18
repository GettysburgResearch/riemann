# Fresh primary-source comparison for #976's theta input

Status: **PARTIAL SOURCE-INTERFACE REVIEW**, not mathematical acceptance
of CT, the metaplectic construction, or the complete higher-moment theorem.
Reviewed repository object: `THETA_ALL_MOMENTS.md` at
`bf845aa1d9d06b0ce62440edc5726de997a888db` (#976).

The CT primary source was unavailable in #976's recorded session. In this
session the browser fetch still failed, but an ordinary direct HTTP GET
successfully obtained the versioned primary TeX source:

    https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex

The exact byte length, SHA-256, formula spans and block hashes are in
CT_SOURCE_AUDIT.json. `audit_ct_source.py` authenticates a separately
downloaded copy before locating those spans. It treats TeX as data and
does not compile it. The primary text is credited to Dean Cureton and
Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*,
Hexagon 2610.00200v2. No source manuscript is redistributed here.

## Comparison and disposition

The following are textual/mathematical interface checks against the actual
primary body, rather than a deduction from its abstract or an old PR title.

| #976 input | Primary TeX labels/section | Finding |
|---|---|---|
| Actual B_m, with all c and cube n columns | `eq:B`, family overview | Matches the named Gaussian theta source; c and n may share primes |
| Reflection for all m and Z, before choosing support lengths | `prop:reflection`, `eq:reflection` | The reflection itself has no long-support M>1 restriction; its sum is stated absolutely convergent |
| Two logarithmic derivatives; x^(1/8) at zero and arbitrary power decay at infinity | `eq:profile-bound` in `prop:reflection` | Matches #976's R-P, with fixed field/data constants and a finite profile list |
| q(c)^(-1/2) q(n)^(-1), and argument Z q(a) q(c) q(n)^3/[q(d)^2 q(f)^2] | `eq:separated-reflection` | Matches the exact norm powers used in the higher-moment proof |
| Quadratic interaction chi_d(c)^3 | `eq:quadratic-pairing` | Matches the order-two family; it is not a sextic diagonal sieve |
| All four local beta branches | `eq:beta` | Matches #976's R-B, including zero in the 2 mod 3 branch |
| Masks (d,h n)=1 and (c n,f)=1 | Paragraph after `eq:beta` | Matches; the extra (d,n)=1 condition is separate from the quadratic nonunit zero; there is no new (c,n)=1 condition |
| Number-field quadratic Q2 with both indices squarefree | `sec:quadratic-family`, `eq:quadratic-sieve` | Primary text explicitly checks the Kummer conductor/product interface and finite local classes before invoking Goldmakher–Louvel |
| Two-derivative Fourier separation uniform in effective length | `eq:localized-fourier-bound` and its proof | Matches the local separation used before #976 sums all c,n,a,f tails |
| Printed global second moment | `prop:moment`, `eq:moment` | Still stated for M0=419/400. Its simplified Z^(2M0-1) corollary is not a general subcritical-support theorem |

The direct source therefore confirms that #976 accurately transcribes the
reflection, profile, local-majorant and mask contracts on which its own
higher-moment deduction rests. It also confirms the distinction between
an unrestricted reflection and the printed long-support moment corollary.
This removes the *access/transcription* uncertainty recorded in #976; it
does not establish an independent proof of the imported analytic contracts.

The Cai–Fan–She citation was checked at
[arXiv:2507.15279v2, §2 and Proposition 2.2](https://arxiv.org/html/2507.15279v2).
Its twisted Jacquet module is an irreducible genuine representation of the
covering center, whose irreducible dimensions are d|d|^(-1/2). With CT's
c=2, d=3/gcd(1+4c,3)=1, this gives dimension one at wild places too.
The following explicit coefficient recursion assumes |3|=1; it is not a
wild-place formula. CT uses the dimension statement here. This confirms
that citation boundary; the deep proof remains outside this partial review.

The complete one-page body of the published
[Kazhdan--Patterson correction](https://www.numdam.org/item/PMIHES_1985__62__203_0.pdf)
was also rendered and read. Its catalog page is 203 (the scan prints 419).
The 157,152-byte PDF has SHA-256
`4f6eb1ed12f8bd25ff54349bfd2cbd778b36d5c0fbb8ff6ddd763a0d1868e77d`.
The correction withdraws the auxiliary spherical-functional vanishing and
changes the global normalization in Theorems II.2.2, II.2.3 and the page-130
discussion. Its corrected product formula includes T(S)^(-1), with the
coefficient normalization defined by a stabilizing limit. CT explicitly
excludes the withdrawn assertion and fixes a scalar using a nonzero global
coefficient. This is consistent at statement scope; it does not verify
that every upstream normalization has been propagated. That further check
would require following the corrected constants through the full global
realization, not merely citing the erratum.

I then followed this particular issue into the cited primitive-root
manuscript, pinned at OpenAI mathematics commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Its 891,737-byte PDF has SHA-256
`671ac4b3ece879f614ed8f4b782e61a07805e533f385a694fe4d7afbda3c9365`.
Appendix A.1--A.2 (printed pages 85--87) was rendered and read. A.2
explicitly includes the corrected rank-two T(S) and proves the exterior
product by normalizing a nonzero global functional on a pure tensor,
then varying finitely many components using local uniqueness. Thus the
correction is accounted for in the cited normalization argument, beyond
the presence of a bibliography entry. This check does not reconstruct
the original residual representation, all local calculations, or CT's
smooth-global-realization estimate.

## Remaining mathematical boundary

CT itself imports the local coefficient normalization, reflection and
finite-place constructions from the cited OpenAI primitive-root manuscript,
with Kazhdan–Patterson and its published correction and later Whittaker
uniqueness results as inputs. I read CT's relevant construction/normalization
discussion and the reflection-to-quadratic-sieve sections, but did not
reconstruct all of those deep upstream arguments. The fact that CT prints
a contract cannot substitute for that reconstruction.

The new fixed-order powering, square removal, all auxiliary tails and
support estimates in #976 remain their own proposed proof obligations.
The present comparison found no mismatch in the specific adopted formulas
listed above; it is not an exhaustive independent referee verdict on that
packet. No new theta-to-native signed projection or principal extraction
bound follows from source authentication.

The AxiomMath/DedekindZetaZeroFree repository was located at commit
`09afbb4ce6570c1615d58509dc197fc9f0956b7d`, and its public statement and
file inventory were inspected. A local external build was then started;
it did not complete. Three dependency artifacts reported failed-to-create-
file errors on long Windows paths; the remaining build was intentionally
stopped after about two hours, with its cache preserved. The tracked source
remained unchanged. CT_BUILD_RECEIPT.json pins the diagnostics and final log.
The existing public compile
job at that exact upstream commit was also read and reported success;
the separate Palomar preflight job was skipped. The receipt links the job
and records this read-only observation. No completed LOCAL external
theorem build or successful comparator run is claimed by this comparison,
and it does not formally verify our new mathematics.

An additional static source check compared both exported theorem signatures,
the RayClassCharacter structure, and its IsPrincipal definition with the
Challenge, exactly after whitespace normalization. All four agree; their
source and normalized-block hashes are in the build receipt. This is a
source-text result only, distinct from elaboration, kernel axiom inspection,
or an accepted sandboxed-comparator verdict. Any completed local build or
axiom inspection is reported separately in that receipt.

The native moment theorems in PROOF.md depend on the standard Hecke source
and the nonvanishing Gaussian Mellin multiplier. They do not assume CT's
theta theorem. Its separately labeled §8 DOES adopt CT's printed
31/32 finite-order Hecke theorem as an additional input, to derive an
explicit native high-moment improvement. That input is absent from §§1–7;
the distinction is part of the theorem ledger, not an implicit dependency.
