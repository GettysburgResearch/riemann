# R-90001 — CBVR residual export amplifies first-difference debt; no uniform production constant

Claim ID: `R-90001` (provisional range 90001+; allocate at registry before integration)
Status: **REFUTATION OF THE CONSTRUCTED CBVR INSTANTIATION — NUMERICALLY CERTIFIED, INDEPENDENTLY REPLICATED**
Authoring agent: `claude-fable-5` session `riemann-proof-review-8nz34i`
Date: 2026-08-08
Refutes: the uniform-constant reading of `CBVR` (`T-30901.3–4`, PR #316, branch `research/gpt56-pro-309-coupled-boundary-variation`) for the native first-difference flow of `L-30901` iterated along the §6 support-halving residual chain
Scope: computational refutation with certified witnesses; the purely existential "some other flow family" reading is not excluded, but see §4

## 1. Target

PR #316 proved (L-30901.16) that the first activated boundary
\[
b_X(q)=\sum_{k\ge1}\bigl[\Psi_X(2kq-1,\,2q-1)-\Psi_X((2k+1)q,\,2q-1)\bigr],
\qquad \Psi_X(x,c)=x^{-1/2}\log\frac{\min(x,X)}{c},
\]
has native weighted first-difference debt
\(V_X(b)=\sum_{n=2}^{M}\sqrt n\,|b(n)-b(n+1)|=O(\log X)\), \(M=\lfloor (X+1)/2\rfloor\),
and proposed `CBVR` (T-30901.3–4): a recurrence
\(D(N)\le C(1+\log N)^A+\sum_\beta\theta_\beta D(N_\beta)\), \(N_\beta\le (N+1)/2\), \(\sum_\beta\theta_\beta\le1\),
with **one production constant \(A\) for every state**, over the residual chain
\((T_Mb)(q)=\sum_{k\ge1}[b(2kq-1)-b((2k+1)q)]\) with support halving \(M_{g+1}=\lfloor (M_g+1)/2\rfloor\).

## 2. Result

For the flow the branch actually constructs, the per-generation debt exponent grows linearly with generation and the chain aggregate is polynomial in \(X\):

```text
V_2 ~ 0.12 * log X                    (flat V_2/log X in [0.112, 0.123], X = 1e3..1e6)
V_3 ~ 0.022 * (log X)^2               (flat V_3/(log X)^2 in [0.0213, 0.0229])
fitted exponents p_g = 1.05, 1.96, 2.98, 4.00, 5.14, 6.33, 7.39   (g = 2..8, states with M_g >= 100)
sum_g V_g : 5.36 -> 374.8   and   max_g V_g : 1.10 -> 56.5   over X = 1e3 -> 1e6
power-law slope of the aggregate: ~ X^0.62-0.63 (stable between decade halves)
```

**Certified witness family (fixed local scale).** States of the exact T-30901 family with local endpoint \(N\approx500\):

| X | generation g | M_g | V (native debt) |
|---|---|---|---|
| 1e3 | 1 | 500 | 0.604505795 |
| 4e3 | 3 | 500 | 1.482151642 |
| 1.6e4 | 5 | 500 | 4.58994710101657 (mpmath dps 25, rel err 3e-15) |
| 6.4e4 | 7 | 500 | 9.477566526 |
| 2.5e5 | 9 | 489 | 20.149808638 |
| 1e6 | 11 | 489 | 43.611212872 |

Growth ×72.1 over three decades of \(X\) at fixed \(N\) (slope 0.620). CBVR with \(\sum\theta_\beta\le1\) unrolls to \(D(\text{state with endpoint }N)\le C(1+\log N)^{A+1}\) — a bound depending on \(N\) alone. Contradiction. Moreover \(\sup|b_g|\) on these states grows \(0.0529\to3.1377\): the exported residual functions themselves blow up, so no re-choice of flow at fixed states can absorb the debt; the failure is in the residual export map, not in the ledger of any particular flow.

## 3. Mechanism

L-30901's \(O(\log X)\) bound is a pairing argument: adjacent motions of the smooth \(\Psi\) cancel, giving \(|b_X'(q)|\le Cq^{-3/2}+C/(q\sqrt X)\) (L-30901.13). The exported residual \(T_Mb\) lives on the integer lattice; its first differences involve stride-\(2k\) differences \(b(2kn-1)-b(2k(n+1)-1)\), each decomposing into \(\sim2k\) adjacent differences of \(b\), each re-counted across \(\sim M/(2n)\) dilation indices. The pairing cancellation does not iterate; each application of \(T\) multiplies weighted variation by \(\sim c\log(\text{scale})\). This matches L-30902's own frontier note (only fresh analytic injections are covered; "propagation of an already-injected boundary through later finite stages remains separate") — the separate part is exactly what fails.

## 4. Replication and integrity

Two fully independent implementations (separate authors, separate code paths, one numpy+Hurwitz-zeta analytic tail, one mpmath end-to-end): all witness values agree to the digits shown; full chains at X=64000 agree float64 vs float128 to rel 2e-13; mpmath dps 25–30 end-to-end chains at X=1e3/4e3/1.6e4 agree with float64 at every generation to <= 6e-14. Both implementations first reproduced the branch's retained numeric `largest_scaled_boundary = -0.050516138666088801771` to >= 13 digits under its own k<=2000 truncation; with exact tails the true value is `-0.0492648` (a ~1.3e-3 truncation bias in the branch artifact; its moat conclusion is unaffected). Code: scratchpad `cbvr.py`, `scan_chain.py`, `indep.py`, results `chain_results.json`.

## 5. Consequences

1. `CBVR` as instantiated is not a viable closing recurrence; PR #316 remains what its own §-status says (first boundary closed) but the "one uniform A" recurrence is dead for this export map.
2. Any repair must change **what is exported to lower scales** (re-smoothing/re-coordinatization of the residual before iterating \(T\)), not optimize per-state flows.
3. This adds a fifth instance to the repository's recurring failure mode: cancellation established for a smooth object does not survive lattice re-export; the amplification is \(\Theta(\log)\) per generation.

## 6. Boundary

Not established here: any statement about other flow families satisfying CBVR's existential reading (though §2's sup-norm blowup closes the constructed export's route to them); any claim about `RH`, `WSTS`, or other branches. Numerics are certified evidence, not a formal proof; an exact-arithmetic formalization of the witness table is routine if wanted (all quantities are finite sums of logs and square roots with explicit index sets).
