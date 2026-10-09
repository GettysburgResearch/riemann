# OpenAI Riemann companions and the native Möbius bridge

Status: **IMPORTED / REVIEW_PENDING**, with separately stated exact identities,
conditional deductions, and proposed research. RH remains open.

Scope: a reproducible extension of [PR #908](https://github.com/GettysburgResearch/riemann/pull/908),
including related arithmetic sources, their advertised internal Lean dependency
closures, and the Riemann-specific insights from the October 7 comparison.

Exact sources: `openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`;
the inherited core is frozen at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`
in Riemann commit `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`.

What was actually run: see [VALIDATION.md](VALIDATION.md). Source integrity,
finite exact arithmetic, and lexical import checks have different meanings from
a Lean kernel/Comparator run or a complete mathematical proof audit.

Smallest remaining mathematical gap: a uniform estimate for the **actual signed
completed native covariance** after transferring the imported smooth arithmetic
families to the discontinuous floor kernels below. No such estimate is supplied
by merely importing the sources.

## Start here

| Reader's question | Entry point |
| --- | --- |
| What do the original 7/8, 11/12 and Siegel-zero papers say? | [Core result and proof guide](../2026-10-07-openai-quasi-riemann-import/RESULT_AND_PROOF.md) |
| Which additional papers matter, and why? | [Related results and exact scope](RELATED_RESULTS.md) |
| How do the ideal Möbius sums connect to our integer source? | [Native Möbius bridge](NATIVE_MOBIUS_BRIDGE.md) |
| What can we now prove, and what should we attempt next? | [Research programme](RESEARCH_PROGRAM.md) and the [inherited conditional bridges](../2026-10-07-openai-quasi-riemann-import/CONDITIONAL_BRIDGES.md) |
| Which source files were imported, and where are they? | [Selection](SOURCE_SELECTION.json), [complete manifest](SOURCE_MANIFEST.json), and [reproduction instructions](REPRODUCE.md) |
| What does the supplied formalization actually cover? | [Formalization map](FORMALIZATION.md) |
| How should this be reviewed? | [Review guide](REVIEW_GUIDE.md) |

## Mathematical contribution of this companion

The inherited family-003 packet already contains the three core papers and
their formal source. This companion adds a broader comparison and a concrete
exact arithmetic interface. Put

$$
\beta(n)=\sum_{N\mathfrak a=n}\mu_{\mathbb Q(\sqrt{-3})}(\mathfrak a).
$$

Then, with every Euler factor restored,

$$
\mu=\beta*\chi_{-3},\qquad
M(x)=\sum_{n\le x}\beta(n)
\mathbf1_{\lfloor x/n\rfloor\equiv1\pmod3}.
$$

The bridge document proves this identity, constructs the resulting exact
signed Gram and completion kernels, and records the moving-endpoint and
smooth-profile transfer obligations. It includes the ramified prime 3 and the
inert prime 2, whose ideal norm is 4. Norm coefficients need not be bounded by
one: for example, `beta(7) = -2`.

For the completed energies in our existing work,

$$
F_X=E_X+(X+1)u_X^2,\qquad
\mathcal A_X=E_X+2(X+1)u_X^2=2F_X-E_X,
$$

so `F_X <= A_X <= 2F_X`. The monotone state `F_X` is convenient for scale
recurrences. The imported 7/8 result conditionally supplies exponent
`3/4 + epsilon`; it does not supply the subpower bound needed for RH.

The earlier import already tested the full MHB32 estimate and found that
substituting this seed gives the weaker exponent `505/546`. Its CAP36
transport deduction has its own restricted scope. Both limitations are retained.

## Source coverage

The original three manuscripts remain in the [core packet](../2026-10-07-openai-quasi-riemann-import/README.md).
The companion includes **22 additional manuscript directories** across ten
families, with PDFs, LaTeX sources, bibliographies, and accompanying files.

| Family | Role in the Riemann programme |
| --- | --- |
| 007 | Ordinary multiplicative correlations and signed finite-law comparison |
| 011 | Weighted dilation graphs, shifted-prime statistics, and a dependency of 029 |
| 012 | Joint Dickman laws for actual consecutive integers |
| 014 | Secondary function-field, automorphic and Frobenius comparison |
| 021 | Sieve boundary terms and actual residue-survivor transfer |
| 023 | Cubic Gauss/theta moments and structured cutoff decomposition |
| 026 | Secondary prime-gap programme and large-gap stress cases |
| 029 | A further finite-order Hecke zero-free theorem over cyclotomic fields |
| 142 | Prime-field factorization application of the 029 Hecke theorem |
| 182 | Polynomial-difference applications, including a use of 003 |

An additional discovery in this intake is the Hecke theorem inside family 029:
it claims the half-plane `Re(s) > 1 - 10^-6` for finite-order Hecke L-functions
over cyclotomic fields containing the twelfth roots of unity. This has broader
field scope than 003, but does **not** improve the zeta boundary 7/8. Its
simultaneous-primitive-root companion is explicitly conditional.

The released abridged reasoning PDF for family 007 is included as historical
supporting material. It is not a proof certificate. No corresponding published
trace was identified for family 003.

Families 014 and 026 are secondary comparisons with programmes already in this
repository. Their inclusion does not assert a transfer to zeta. Unrelated
Barker, Littlewood-flatness and general combinatorial catalogue matches are not
part of this Riemann source intake.

## Preservation and attribution

This is a companion contribution based on PR #908, not a replacement for it.
The original core directory, manifest, validation record and review boundaries
are unchanged. Six general upstream metadata files changed between the old and
new snapshots; the selected papers and existing core implementation did not.
See [UPSTREAM_DRIFT.md](UPSTREAM_DRIFT.md).

`SOURCE_MANIFEST.json` records every file in the combined selected source view.
A file is physically reused from the core only when its upstream path, Git blob
and executable mode match the new snapshot. Additional or changed files are
stored under this packet's `upstream/`. [REPRODUCE.md](REPRODUCE.md) assembles a
fresh complete view from those exact entries.

Original integration notes and checks follow the repository's MIT terms.
Unmodified OpenAI source retains Apache-2.0 and its existing notices; see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The papers' authorship is not
attributed to this project. No assertion about the training provenance of the
internal model is made by this mathematical import.
