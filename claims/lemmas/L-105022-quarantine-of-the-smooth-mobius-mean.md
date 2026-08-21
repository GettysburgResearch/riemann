# L-105022 — Quarantine: the negative set of the smooth Möbius mean is exactly 19 points, all below the rough cutoff, with global minimum −2323/30030 at t = 13

Claim ID: `L-105022`
Status: **PROVED EXACT (complete finite enumeration; replay `X-105020/verify_pivotal.py`)**
Created: 2026-08-21
Agent: claude (external reviewer lane)
RH status: not assumed, not addressed

## 1. Statement

Let `P_61 = \prod_{p \le 61} p` and, for real `t \ge 1`,

```
A_t = sum over squarefree d | P_61, d <= t of mu(d)/d
```

(the smooth Möbius mean — the prefix functional that drives every compact
Hall/moat inequality of the program, `H_t(x) = 4\sqrt x\,A_t - 3B_t`,
`L-99020` @ `review/gpt56-pro/99600-three-interface-hostile-audit`). Then,
over the ENTIRE divisor lattice (all `2^{18}` squarefree divisors, i.e. all
real thresholds up to `P_61` itself):

1. `A_t < 0` exactly on the 19 threshold points
   `{5, 7, 11, 13, 14, 19, 21, 23, 30, 31, 33, 34, 37, 43, 47, 51, 53, 55, 61}`
   (each negative value persisting on `[d, d')` to the next divisor `d'`);
   **every negative excursion lies below 67**, and `A_t \ge 0` for every
   `t \ge 62`, all the way to the top of the lattice
   (`A_{P_61} = \prod_{p\le61}(1 - 1/p) = 0.13158735\ldots > 0`).
2. The global minimum is `A_{13} = -2323/30030` (`2323 = 23\cdot101`),
   attained exactly at `t = 13`.

*Proof.* Complete enumeration of the finite lattice (262,144 divisors,
exact rational prefix sums), deposited and replayable in
`experiments/X-105020-t13-wall/verify_pivotal.py`. ∎

## 2. Why this is the program's load-bearing finite structure

* The smooth/rough boundary 61/67 **exactly quarantines** every negative
  excursion of the Möbius mean inside the compact block. This is the
  structural reason the compact-fibre Hall technology works at all: for
  `x < 67` the negative `4\sqrt x\,A_t` term is bounded by `4\sqrt{67}|A_t|`
  and the positive `-3B_t` dominates (the certified moat, worst case
  `t = 13`, `x = 67^-`, `H = 0.35931766\ldots` — `L-99600.4` @ the 99600
  review branch).
* The same 19-point set with the same minimizer `t = 13` is,
  simultaneously: the killer of the grown compact block (`L-105021`: true
  Hall feasibility dies at `C^* = (45045|B_{13}|/4646)^2 = 87.3589\ldots`),
  and the universal Hoffman min-cut of the global two-leaf circulation at
  every odd-history witness (`O-105023`: deficit law
  `(371342/1006005)\sqrt X - 3.25857`).
* The minimizer is `t = 13` as a property of the **global smooth lattice**,
  not of any witness's terminal coordinate: it remains 13 for witnesses
  with `y = 43` or `61` (ladder data, `O-105023 §3.2`).

## 3. Scope

A finite exact fact plus its structural reading; no asymptotic claim, no
gate closed or opened. It explains (does not justify) the factor-67 choice:
67 is the first prime past the last negative excursion of `A_t`.
