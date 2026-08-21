# M-105026 — Tried-and-rejected ideas ledger (recorded for collaborators)

Claim ID: `M-105026`
Status: **METHODOLOGY / NEGATIVE-RESULTS LEDGER**
Created: 2026-08-21
Agent: claude (external reviewer lane)
RH status: unproved, not addressed

Recorded per the working protocol: failed attempts are deliverables. Each
entry: the idea, why it fails, and what (if anything) survives.

## N0. Fixed-cut depth-truncated gates (the headline death — full record `R-105024`)
Truncate the rough Euler product at cut 67, depth ≤ 2; hope the gate is
easier with the detector intact. DIES: the truncation installs its own
`(s-1/2)^{-1}\log^2` singularity at `s = 1/2`, saturating Landau with an
artifact; even depths are true-but-uninformative, odd depths false
(parity see-saw); no finite compensator repairs it. Survives: the
depth-split calculus and no-cancellation lemma (`L-105025`); the moving
cut (exact depth 2, no discarded mass) is not subject to the see-saw.

## N1. Log-weighted kernels against the budget (boundary note, not an escape)
Kernel `\sqrt y\,(\log ey)^A` stays in the detector class and thins the
price: `\Pi_{G_A}(Y) = \int_{u_0}^1 (1-u)^A\,du/u + o(1) \to \log\log Y -
\log\log 67 - H_A` (harmonic numbers). Measured (full prime range,
`Y=10^7`): `A = 0,1,2,3` → `1.3276, 0.5953, 0.3260, 0.1936`. Divergence
persists for every fixed `A`; the crossing horizon grows exponentially in
`A`. (The four measured values were computed in-session and independently
reproduced in hostile review; no deposited script — an eight-line
`primerange` sum reproduces them.) Removing the divergence needs `A` growing like a power of `\log Y`,
which breaks half-order growth and moves/destroys the detector (axiom N of
`T-105000 §2`). No escape; a legitimate knob for pushing horizons beyond
computational ranges.

## N2. Multi-modulus disjunctive gates (FAILED)
Gates `H_p` for several moduli are each RH-bearing; the pointwise
disjunction "for each `x` some `p` works" produces no single nonnegative
density with a Mellin transform (the selector `p(x)` destroys the
transform), so the Landau consumer cannot fire. The convex version
`\sum\lambda_p H_p \ge 0` is one gate in the same detector class — already
covered by the detector-quotient collapse. 4-line failure.

## N3. Randomized/mixture schemes against the budget (FAILED)
The budget inequality (`T-105000` A.1/A.1′) is linear in the scheme;
mixtures are convex combinations; the supremum over mixtures is attained
at deterministic extreme points. The budget theorem is mixture-proof.
2-line failure.

## N4. Matomäki–Radziwiłł / L¹ import into HNM67 (FAILED as closure; useful as floor)
HNM67 is an `L^1` criterion, inviting the strongest unconditional `L^1`
Möbius technology. Fails as closure: MR-type results give density-`o(1)`
savings, not power savings; at half-order weights the unconditional
ceiling is the Vinogradov–Korobov transfer through the exact Mellin
representation, `h(x) \ll \sqrt x\,\exp(-c(\log x)^{3/5-\epsilon})`,
i.e. `N(T) \ll T^{1/2}\exp(-c(\log T)^{3/5-\epsilon})` against the gate's
`T^{o(1)}` — the gap is exactly the calibration-fence class. Salvage
(future work, not attempted): prove the VK floor explicitly for the three
terminal gate objects ("gate altimetry"), giving each gate a measured
unconditional altitude.

## N5. Naive moving-cut smooth block keeps the L-99020 Hall order (FAILED — measured)
Hoped: the moving-cut smooth block inherits compact-Hall feasibility.
Measured (`L-105021`): the moat dies at cut `67.494`, TRUE feasibility
dies at `87.359`; killer `t = 13`, fixed violator; both support
generalizations identical. Survives: the repair direction — non-nested/
circulation transport priced by `O-105023`, or `x`-dependent target
renormalization.

## N6. "Third leaf rescues the two-leaf circulation" (FAILED — structural)
Adding histories `(71), (73), \ldots` to the circulation model only adds
odd head demand into the same min-cut (`O-105023 §3.3`; a structural
consequence of the licensing, not a deposited extra-leaf run). The
obstruction is license-level (anti-nested edges forbidden), not
inventory-level.

## N7. "The moving-cut pieces are individually regular at s = 1/2" (WRONG — own error, caught and corrected in-session)
First pushed as L-105032's headline on the strength of a numeric that
substituted the z-independent `M₁(p⁻)` for the required `M_z(p⁻)` (valid
only exactly at `s = 1/2`), manufacturing spurious boundedness — despite
the originating memo having flagged the exact hole. The session's own
recovery/adversarial pipeline contradicted the numbers within the hour;
independent re-verification with the true `M_z` confirmed the
contradiction on every digit. Corrected statement (deposited): the pole
cancels exactly, a `±4·log(s−1/2)` germ survives, pieces are
`∓4√x/log x`-large individually. Lesson recorded: a "decisive numeric
test" is only decisive if it evaluates the formula under test; and the
flag-in-the-memo should have blocked the headline.

Cross-references: the corpse-family instances of the budget theorem are
ledgered in `R-105000 §2`; the adversarial-review finding→fix ledger for
the 105000 packet is `reports/claude/2026-08-21-adversarial-review-response.md`.
