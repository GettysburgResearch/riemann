# Independent release audit of global Xi saddle f25599e0

Verdict: PASS for corrected source f25599e0bcb77cb716bf17120e54174a994e7402,
parent a45d816a2b390de0efaa468622be65bb87737361.

The original analytic review and four corrupted campaign orders are recorded
immutably in audit a7b3f8ce63d021e78c79e9e1b76f3cd95aaa279b,
XI_GLOBAL_ODD_ORDER_SADDLE_AUDIT_A45D816A.md. That report's analytic PASS
and original-artifact REPAIR verdict are not overwritten. This separate
review accepts the successor release after inspecting its exact delta.

## What changed and what did not

The live scout changes only its returned K field from Python integer to
canonical decimal string. Its phase, theta, quadrature and response
calculations are unchanged. The ten campaign cases were regenerated;
comparison shows that every field other than K, elapsed time and the new
scout source hash agrees exactly with the original record.

The source manuscript's analytic sections 1--6 are byte-identical after
LF normalization. Section 7 adds the transport contract and transparently
records the original JavaScript binary64 aggregation defect. The frozen
four-source manifest is unchanged. After removing artifact hashes and the
new campaign-contract result, the old exact fixture payload is unchanged.

All ten K fields are now canonical positive odd decimal strings. Independent
150-digit reconstruction of the declared nearest-odd rule agrees for every
case, including these four previously corrupted values:

    51734778565382343
    8420083094517158086385
    1370408867778821140395548619
    537623428363227089682525110316002717472222375

That transcendental reconstruction is a nondirected consistency check,
not an interval certificate. The important exact transport fact is that
the specific Python odd integer now survives serialization unchanged.

The new campaign validator checks the declared ordered case list, strict
xi type, canonical ASCII decimal K with positivity/parity/bit caps,
producer and parent identities, requested precision, upper quadrature
window, and the explicit non-certification labels. It does not certify
the numerical values or re-evaluate the transcendental nearest-odd rule.
Its stated scope is transport/source validation, not a complete hostile
unbounded-data parser or a quadrature certificate.

## Independent replay

On a fresh worktree at the exact successor SHA:

    python -B -m unittest tests.test_xi_global_odd_order_saddle tests.test_xi_odd_current_scaling
    python -B -O -m unittest tests.test_xi_global_odd_order_saddle tests.test_xi_odd_current_scaling

Both run 45 tests and pass, in 21.630 and 21.723 seconds. This includes
the new live replay above the binary64 exact-integer limit.

Both producer checks pass. All four LF-normalized report/manifest emits
match their frozen fixtures exactly. Ruff lint, Ruff formatting, and the
complete parent-to-successor whitespace check pass. No source file was
edited by this reviewer.

Twenty additional K-transport attacks were rejected, covering booleans,
numeric types, empty/zero/even/negative values, plus signs, leading zeros,
decimal/exponent text, whitespace, Unicode decimal digits, overlength
strings and integers exceeding the declared bit cap. The original two
large-order scout replays already reproduced all other nonelapsed fields.

All four source bindings and six successor artifact hashes authenticate:

- proof: eddb18ed5fdc4ba95fb449f3b8362e1cd30ef0eddf9f781981ecf95c72489341
- exact producer: 2328de4b82b279a7eb60db2d4cbb7a8e2c62526e54f014dab5a571541d62a5a7
- manifest: d2004cc18bba1907f9b8683c0f274543cfd90e7b044d8cd3ec246852de58c62c
- scout: bc762426bcf556e8388706c1eade716c4add639edb0354677378912198bccec6
- corrected campaign: 01f4c5477c9d911d3df35ae859a19e4a6d9608c6de923f96bbf3012d820054eb
- tests: 4e8be1241a3902faa032f791ef7abe897986787d30c6beeb27bbf3255b61d1ba

## Accepted boundary

The repaired campaign resolves the concrete original finding. The
independently reconstructed all-order phase, tail, normalization and
translated-response proofs remain as reviewed in a7b3f8ce. No new analytic
claim is introduced by the repair.

Acceptance does not turn the nondirected campaign into certification,
select a prescribed physical gauge, prove source capture or innerness,
settle topological free energy or RH, or establish external novelty.
