# T-105030 — The CIRC-13 theorem: every licensed transport certificate has deficit ≥ c₁√X + c₀; the licensed/unlicensed boundary is priced exactly

Claim ID: `T-105030`
Status: **PROVED FINITE THEOREM ABOUT THE FORMALIZED CLASS 𝒞(X) — licensing choices enumerated in §6; no RH gate closed or opened**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Upgrades: `O-105023 §4` (conjecture CIRC-13) to a theorem for `𝒞(X)`.
Depends on: `L-105022` (quarantine, exact `A₁₃ = −2323/30030`); atoms/licenses
from `L-96501` @ `paper/arxiv-factor67-two-row-parity-resummed-v2-republish`,
`L-97400` @ `paper/factor67-parity-lorenz-correction-97600`, `L-99020` @
`review/gpt56-pro/99600-three-interface-hostile-audit`, `R-96500` @
`research/gpt56-pro/96500-parity-covariant-gluing`.
Replay: `experiments/X-105030-maximal-license-and-circ13/lane_circ13/`.
RH status: **unproved, not addressed**

## 1. The class 𝒞(X) (Definition 1)

Fix real `X ≥ 67`. A licensed certificate structure is: **(D1)** a finite
prefix-closed set `L` of rough histories `h = (p₁ < ⋯ < p_t)`, primes
`≥ 67`, `π(h) = Πpᵢ ≤ X`, with `() ∈ L`; **(D2)** atoms = the literal
`L-97400` ledger rows: for `h ∈ L`, squarefree `d | P₆₁`, `d ≤ X/π(h)`,
one occurrence `(h,d)` of mass `k^{-1/2}T(X/k)`, `k = dπ(h)`, sign
`μ(d)(−1)^{|h|} = μ(k)`; negatives are hard demands, positives capacities;
**(D3)** licensed edges: within-leaf nested (`e ≤ o`, the `L-99020.2/.5`
row-monotone license) and cross-leaf same-`d` parent→child (the `L-97400`
parity swap; adjacent generations WLOG — an even-generation same-`d` jump
connects equal signs, proved in the deposit); **(D4)** a certificate = a
nonnegative flow meeting all demands within capacities. The `O-105023`
two-leaf model is the special case `L = {(), (67), (67,q)}`. Dropping score
and component rows is a relaxation, so infeasibility transfers to any full
certificate under the same transport licenses.

## 2. Theorem

Let `X ≥ 13` and `(L, atoms, edges) ∈ 𝒞(X)`. With
`F₀(13) = 4√X·A₁₃ − 3B₁₃` (lattice = integer sums here since all `d ≤ 13`),
`c₁ = 4(1/67 − A₁₃) = 371342/1006005`, `c₀ = 3(B₁₃ − 67^{-1/2}) =
−3.25856984835402273878…`:

**(i) CIRC-13 constants.** If `(67) ∈ L`, every licensed flow leaves unmet
target demand `≥ c₁√X + c₀`, strictly positive for every real
`X > X₀ = (|c₀|/c₁)² = 77.93027405427602596732…` (interval-certified; in
particular every integer `X ≥ 78`; at `X = 78` the bound is
`∈ [0.00145743145464…, …] > 0`, certified).

**(ii) Universal version.** For every `L` (odd histories present or not)
and every real `X > C* = (3|B₁₃|/(4|A₁₃|))² = (45045|B₁₃|/4646)² =
87.35893176924588158…` (every integer `X ≥ 88`):
`deficit ≥ −F₀(13) = (9292/30030)√X − 3|B₁₃|`. Note: **`C*` is identically
the true-feasibility cap of the grown compact Hall system (`L-105021`)** —
the two walls (grown-fibre Hall; global circulation) are governed by the
same closed form, because both are the sign flip of `F₀(13)`.

**(iii) Escape pricing.** Any global certificate meeting all demands with
licensed edges **plus arbitrary additional transport** must carry
unlicensed inflow into the root odd prefix `d ≤ 13` of at least
`(9292/30030)√X − 3|B₁₃| ≈ 0.30942√X − 2.89206`, and (when `(67) ∈ L`)
total unlicensed inflow `≥ c₁√X + c₀` into the cut of (i). Bounded-
score-debt machinery must carry `Θ(√X)` mass concentrated on the
`L-105022` quarantine address. This is `O-105023 §4`'s sentence, now a
theorem for `𝒞(X)`.

*Proof.* Three finite lemmas (full texts and machine checks in the
deposit): **Lemma 1** (Gale/Hoffman cut bound — two lines); **Lemma 2**
(cut validity, complete neighbourhood enumeration: the demand set
`S₁(L) = {((),o): o ∈ {2,3,5,7,11,13}} ∪ {((p),1): (p) ∈ L}` has licensed
neighbourhood contained in `{R₁, R₆, R₁₀}` — within-root because squarefree
`e ≤ 13` with `μ = +1` is exactly `{1,6,10}`; heads because an odd leaf's
head has no within-leaf supplier (the `R-96500` reversal in cut form) and
exactly one cross-leaf supplier `R₁`); **Lemma 3** (exact violation
`V(X,L) = 4√X(|A₁₃| + Σ_{(p)∈L}1/p) − 3(|B₁₃| + Σ p^{-1/2})`, monotone
increasing in `L` — adding leaves adds head demand, never new capacity).
Then (i) reduces to the two-leaf value, (ii) drops the nonnegative head
terms, (iii) is Lemma 1's corollary. ∎

## 3. Sharpness

On the ten-witness ladder of `O-105023` the bound is **exact**: the cut
`S₁(L)` is the true min-cut, `deficit = c₁√X + c₀` to 12 displayed digits
at all ten points (max relative deviation `3.9·10⁻¹²`); independently
validated by Edmonds–Karp max-flow including a depth-3 configuration at
`X = 4·10⁵` (deficit `230.196832636176 = V(S₁)` exactly).

## 4. Two corrections to the conjecture's phrasing (found and proved in
the upgrade)

(a) The cut must take **depth-1 heads only**: for an odd leaf of depth
`≥ 3` the head's unique licensed supplier is its even parent's head, not a
root capacity; the all-heads cut is valid but strictly weaker (measured
gap `0.48612` at the depth-3 test). Prefix-closure makes the depth-1
restriction costless. (b) The constants `(c₁, c₀)` require the history
**(67) specifically**; any odd leaf gives only the universal (ii) (at
`X = 61841` with `L = {(), (71)}` the true deficit is `87.709… <
88.535…`); 67 enters as the least rough prime.

## 5. What is proved vs licensed

Lemmas 1–3 and the Theorem are unconditional finite mathematics about
`𝒞(X)`: exact rationals, nine square roots, a two-line flow argument. The
conditional content is Definition 1 being the right formalization of
"licensed transport".

## 6. Contestable choices (exhaustive, ranked — stated against ourselves)

1. **Within-leaf `e ≤ o`** (load-bearing): `L-99020` constructs on nested
   edges and prices anti-nested ones; it does not prove every valid
   certificate avoids them. Dropping this voids the theorem — and part
   (iii) prices exactly this escape.
2. **Cross-leaf same-`d` parent→child**: same-`d` grounded in `L-97400`
   (only same-`d` swaps preserve magnitude and activation);
   adjacent-generation proved WLOG. Residue: cross-fibre edges at
   different `d` are covered by no deposited license but not refuted;
   aggregation-before-transport (`R-97400 §5`'s `Φ_X` LP) is a different
   constraint class — the theorem does not contradict its finite-`X`
   feasibility and precisely marks that boundary as where `CPSL67` must
   live.
3. **Odd occurrences as hard demands**: grounded in `L-97400` atomwise
   conservation; odd–odd internal pairing would reduce demands — priced,
   not forbidden, by (iii).
4. **Pre-terminal fibre-labelled reading** vs `L-96501.7`'s terminal
   relabelling: same atoms either way; whether the root-fibre `e ≤ o`
   order is the licensed order after relabelling is the same interpretive
   gap `O-105023 §5` declared.
5. **Target row only**: safe direction for infeasibility (relaxation);
   (iii)'s priced quantity is target mass specifically.

Not contestable (verified exhaustively): `{e ≤ 13, squarefree, μ=+1} =
{1,6,10}`; non-squarefree `4,8,9,12` are not atoms; odd-leaf heads have no
within-leaf suppliers; even-generation same-`d` jumps preserve sign.

## 7. Honesty

A theorem about a transport class, not about ζ. It does not close or open
any RH-bearing gate, does not contradict `CPSL67`'s aggregate-LP
feasibility, and its force against future certificates is exactly as
strong as Definition 1 — with the escape priced at
`(9292/30030)√X − 3|B₁₃|` across the `d = 13` boundary.
