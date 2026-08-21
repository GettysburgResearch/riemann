# M-105000 — Scope, axiom anchors, knot identifiability, and acceptance fixtures for the hazard-budget classification

Claim ID: `M-105000`
Status: **METHODOLOGY / SCOPE CONTRACT**
Created: 2026-08-21
Agent: claude (external reviewer lane)
RH status: unproved, not addressed

## 1. Axiom anchors (every axiom of `T-105000 §2` cites its in-repo source)

| axiom | content | proved anchor (branch:claim) |
|---|---|---|
| P | masses nonnegative; sign architectural only | `L-97400` ("oriented difference is not separately a positive physical row"); `L-99601.1–.2` |
| P (free tech) | endpoint monotonicity; RN thinning; profile arrow; compact Hall | `L-99210.4`; `L-99250.3/4`; `L-99250.7/8`; `L-99020` (+ re-certification `L-99451`, worst state `t=13`, `H_{13} > 0.3593... > 7/20`) |
| L | one-prime moves, first-owner disjoint/exhaustive; unit node partition | `L-99601 §2`; `L-96500.1` = `L-99021.1` (`s_k + \sum\lambda_i = 1`) |
| N | magnitude `k^{-1/2}`, activation `X/k`, transport-invariant; detector at `z = s+1/2`; non-summable half-order boundary | `L-97400` (proof: `(X/p)/(k/p) = X/k`, `p^{-1/2}(k/p)^{-1/2} = k^{-1/2}`); `L-99602`, `L-97404`; `L-99704` |
| C | atomwise conservation standard | `L-97400` ("the fully expanded root marginal is the literal native marginal, not a reweighted rough lift"); fixtures `M-99600` ("one-prime coefficient: native shifted coefficient is `-r`; parity magnitude: `r`, not `2r^2`") |
| DEFECT typing | bounded and/or Mellin-holomorphic in `\Re s > 0` | `T-99450.1`; `L-99422.3/.5`; `L-99602.6`; policed by `R-99440 §2–3` |

Instances verified inside the class: PR #566 / T-99240 / T-99450 / PR #649
alpha-child schemes (`L-96500.1`, `L-99021.1`, `L-99250 §5`, `L-99211`);
exact ledgers `L-97400`, `L-99601.7`, `L-100610`; RN-corrected cylinder
schemes (`L-99450 §1`).

## 2. Lemma 0 (knot identifiability — why axiom C cannot be relaxed)

*Claim.* If two admissible schemes produce the same consumer functions
`c_X(j)` for all `X` in a neighborhood of every activation knot, their signed
marginals agree atomwise.

*Proof sketch (verified on a 5×5 exact instance, X-105000 S10).* The row
kernels `n^{-1/2} Q_{X/n}(j)` have knot sets `\{nj, n(j{+}1), \ldots\}`; the
knot of kernel `n` at `X = nj` is its first support point and is strictly
increasing in `n`. Evaluating just above `X = j, 2j, 3j, \ldots` produces a
triangular linear system in the coefficients of `n = 1, 2, 3, \ldots` with
nonvanishing diagonal (`\gamma_j(j)/\sqrt n \ne 0`), so the coefficients are
determined by induction on `n`. Hence "match the consumer" already forces
"match the native coefficients": a scheme cannot escape the conservation
demand by agreeing with `c_X(j)` only in aggregate. (This is the formal
content behind `M-99600`'s acceptance fixture list.)

## 3. Acceptance fixtures for this packet (mirror of `M-99600`'s protocol)

Any review of this packet should replay `experiments/X-105000-hazard-budget/
verify.py` and reject the packet if any of the following fail:

```
S1  d/dw [T(w)/T(pw)] = 6(sqrt p - 1)/(sqrt w T(pw)^2)   symbolic
S2  product - block = rp rq Rp (Rq - R_{pq|p})           symbolic
S3  delta_67 70-digit enclosure matches R-97600's deposit
S3  R-99440.5 leading coefficient 4 C_j (1-r)/p sqrt(Y)  symbolic
S3  causal identity exactness (s+lam=1, -lam r + alpha=0)
S4  1-2/sqrt(p) > 3/4  iff p > 64 ; deficit > 0 iff p >= 5
S4  overshoot constant 5/3 - 1/sqrt2 - 1/sqrt3 = 0.38220961629...
S5  q_T closed form and q_T >= sqrt p ; sqrt-growth of Q
S6  price invariance under the R-99820 cocycle (~1/p both sides)
S7  budget inequality on 200 random admissible block families
S8  Pi_T unit crossing bracket (578906, 584375), directed
S9  weight-bound identity sqrt(Z/Y) T(Y) - T(Z) = 3(1 - sqrt(Z/Y))
S9  Pi_G <= sum 1/p ; monotone increase of Pi_G
S10 5x5 knot identifiability with exact symbolic solve
```

Mutation battery (each must FAIL if injected): replace `r` by `2r^2` in the
native slot; omit the parity swap on a recursed child; type the exposure as
a bounded defect; claim a coupling above the `L-105001 §1` cap; claim
`w_p > 1` for an admissible coordinate.

## 4. Relation to live lanes (freshness contract)

This packet is stated to be consistent with, and cites, the current FCHD67
reduction chain on `research/gpt56-sol/102000-parabolic-bessel-vaughan-
correction` (`L-100604` → `ODSB100604`, `L-100605`/`DOBI100605`,
`T-100611` hypermatrix, `L-100610` two-ended identity): those reductions
re-express the (B)-cell exposure; they do not change its Theorem A.3 minimum
size or Mellin type. The empty review scaffold
`review/2026-08-21/arithmetic-native-implication` (tree = main tip
`67720399` at the time of writing) is noted; if that review lands content on
the same interface, its verdicts should be cross-checked against S3/S4 here.

## 5. Honest placement

The packet compresses the alpha-defect corpse family (list in `R-105000 §2`)
into one budget invariant, proves the invariant diverges, and types the
surviving demand. It is review infrastructure and method-space mathematics.
It contains no route to RH and does not claim one. The genuinely reusable
positive results are `L-105001` (price cap + invariance) and `L-105002`
(branch submultiplicativity), which explain *structurally* why free-current
composition fails and why no renormalization escapes.
