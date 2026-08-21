# O-105023 — Hoffman circulation at the odd-history wall: the min-cut is the t = 13 prefix at every scale, with an exact √X deficit law (conjecture CIRC-13)

Claim ID: `O-105023`
Status: **OBSERVATION / VERIFIED COMPUTATIONS + NAMED CONJECTURE — model licensing stated explicitly; no gate closed**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Depends on: `L-105022` (quarantine); atoms and licenses from `R-96500` @
`research/gpt56-pro/96500-parity-covariant-gluing`, `L-96500`/`L-96502`/
`L-97400` @ `paper/arxiv-parity-completed-scalar-lorenz-v3-final` (and the
97600 paper branch for L-97400), `L-99020` @
`review/gpt56-pro/99600-three-interface-hostile-audit`, and the open-escape
clause of `R-97400 §4` (same v3-final branch).
RH status: not assumed, not addressed

## 0. Novelty

`git grep -il` for "hoffman" and "circulation" over `claims/` of main and
the relevant branches: zero hits. Circulation theory — the classical
signed/reversible generalization of Hall feasibility (Hoffman's theorem:
flows with lower and upper bounds exist iff every cut satisfies the
lower ≤ upper condition) — is new to this repository. It is the natural
formal home for the "reversed-datum realization + cross-history
compensation" escape that the orientation kills themselves leave open.

## 1. Reproduction of the wall

Independent 250-bit interval computation of the `R-96500` witness at
`X = 61841`: **239 active divisors** and
`E_T - O_T = 17.00508653821905259069845575\ldots` — matching the value
deposited in `X-97600`'s verification artifacts to all digits. The wall is
real and reproduced.

## 2. The two-leaf circulation model (licensing stated in full)

Nodes are literal `L-97400` ledger occurrences at the witness: root-leaf
atoms `R_d` (index `d`, mass `d^{-1/2}T(X/d)`, sign `\mu(d)`), the
`(67)`-history child atoms `A_d` (index `67d`, mass `(67d)^{-1/2}T(923/d)`,
sign `-\mu(d)`), grandchild `B_d`. Odd occurrences are demands, even are
capacities. Licensed edges: within-leaf `e \le o` only (the `L-99020.5`
row-monotonicity license — anti-nested edges create row debt and are
excluded); cross-leaf only parent→child at the same `d` (the `L-97400`
parity swap, which preserves coefficient magnitude and activation — this
edge IS the "one global completed-parity source" coupling `R-97400 §4`
names as the open escape). Feasibility ⟺ Hoffman cut condition. The cut
family was proved to reduce to nested down-sets and validated end-to-end
against brute-force max-flow at three truncations (exact agreement).

## 3. Results (computed, interval-certified at the base witness)

1. **The circulation is INFEASIBLE at `X = 61841` — and the binding
   obstruction is not the famous 17-margin.** The min-cut is
   `\{R_d : d \in \{2,3,5,7,11,13\},\ \mu(d) = -1\text{-side}\} \cup
   \{A_1\}` against neighbourhood `\{R_1, R_6, R_{10}\}`, with violation
   `V^*(X) = (371342/1006005)\,\sqrt X - 3.25856984\ldots`, where
   `371342/1006005 = 4(1/67 - A_{13})` and the constant is
   `3(B_{13} - 67^{-1/2})`. At the witness: `V^* = 88.535\ldots`, of which
   only `14.48` is the odd-history head — the rest is the root leaf's own
   `t = 13` excursion (`F_0(13) = -74.055`). The aggregate margin 17 of
   `R-96500` under-reports the per-threshold wall (worst reversed-leaf cut
   is `117.17` at the head).
2. **The dual is completely stable across the witness ladder.** For ten
   witnesses `X = 67\,q\,y` from `52327` to `1175381`: identical tight-cut
   structure (root odd prefix `d \le 13` plus history head), `F_0`-argmin
   at 13 every time, and the closed form `c_1\sqrt X + c_0` reproduces
   every computed slack to all displayed digits. Margins scale as
   `X^{1/2}` with constants built from the target pair `(4,3)` and the
   divisor class `d \le 13` — not from the 5:3 score constants.
3. **Adding leaves does not help.** Every additional history adds more odd
   head demand into the same cut. The obstruction is license-level: the
   demands at `d \in \{5,7,13\}` would have to draw on even mass at
   `d > 13` — anti-nested edges the row license forbids.
4. **Why 13 is universal**: `L-105022` — the global minimizer of the
   smooth Möbius mean over the whole `2^{18}` lattice, independent of the
   witness's terminal coordinates.

## 4. Conjecture CIRC-13 (what the dual data supports)

For every endpoint `X` of the odd-history family (and, by `L-105022`, any
`X \ge 67^2` with a completed-parity expansion): every globally-assembled
transport certificate for the two-row target using only row-monotone
(`e \le o`) moves and same-coordinate history swaps is infeasible, with
Hoffman min-cut `\{odd smooth d \le 13\} \cup \{history heads\}` and
deficit at least `4(1/67 - A_{13})\sqrt X + 3(B_{13} - 67^{-1/2})`.
Consequently any valid `CPSL67`-type global theorem must transport at
least `(9292/30030)\sqrt X + 3B_{13} \approx 0.30942\,\sqrt X - 2.892` of
target mass across the `d = 13` boundary by **anti-monotone (score-debt)
or paired-difference mechanisms**: the non-Hall component of any such
certificate is lower-bounded by a universal `\sqrt X` law concentrated on
the 19-point quarantine set. Bounded-score-debt machinery is therefore not
optional bookkeeping; it must carry `\Theta(\sqrt X)` head mass.

## 5. Honesty

* The model's licensing (row-monotone within leaves; same-`d` parent→child
  across) is an interpretation of the repo's own licenses; the load-bearing
  assumption is the row-monotone restriction, and the conjecture is
  conditional on that reading. Dropping it voids the row-positivity purpose
  of the transport (per `L-99020.5`), but a future construction may find a
  third licensed mechanism — that is exactly what CIRC-13 prices.
* This does **not** contradict `CPSL67`'s finite-`X` LP feasibility
  (`R-97400 §5`'s `\Phi_X` is aggregate-constrained, not nested-licensed),
  does not refute `c_X(j) \ge 0`, and does not close or open any RH gate.
  It converts "global compensation is needed" from prose into an exact
  priced demand with a stable combinatorial address.
