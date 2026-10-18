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
file inventory were inspected only. No Lean theorem or comparator was built,
and this review makes no claim of formal verification of our new mathematics.

The native moment theorems in PROOF.md depend on the standard Hecke source
and the nonvanishing Gaussian Mellin multiplier. They do not assume CT's
theta theorem. Its final, separately labeled §8 DOES adopt CT's printed
31/32 finite-order Hecke theorem as an additional input, to derive an
explicit native high-moment improvement. That input is absent from §§1–7;
the distinction is part of the theorem ledger, not an implicit dependency.
