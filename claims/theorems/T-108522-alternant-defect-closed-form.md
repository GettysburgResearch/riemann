# T-108522 — The alternant closed form for defect numerators; the general-rank square defect solved

```text
Claim ID: T-108522
Status:   PROVED (complete elementary proofs: Lagrange/bialternant
          lemma + partial-fraction lemma + multiplication
          bookkeeping). Machine: symbolic equality with the proved
          d = 3, 4 closed forms; exact integer-point agreement at
          d = 5, 6, 7; general-m series identity at five (m, d)
          pairs; top-coefficient law re-derived symbolically.
Created:  2026-08-31 (pass 3 continuation, Lane 6)
Programme: #764 (Generalized L-Objects)
Depends on: T-108500 (defect definition); resolves T-108508's OPEN
          general-d law; re-derives T-108510's top-coefficient law;
          realizes T-108515 Corollary 2's deposited direction
Proof:    standalone/2026-08-31-alternant-defect/PROOF.md
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          alternant_defect.py + .json (ALL OK); ground truth
          segre_d3m2_betti.py + .json (P^2 x P^2 equivariant Betti
          table (1,9,16,9,1) @ twists 0,2,3,4,6)
Replay:   experiments/X-108522-alternant-defect/ (stdlib)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

For rank d with inverse roots `x_1..x_d`:

```text
N_{2,d}(T) = sum_j x_j^{d-1} prod_{a != j}(1 - x_a^2 T)
             * prod_{a<b != j}(1 - x_a x_b T) / prod_{a != j}(x_j - x_a)
```

— the general-rank pointwise-square defect in CLOSED FORM (previously
proved only for d <= 5, by expansion). More generally, the
(m-1)-fold partial-fraction identity

```text
sum_r h_r^m T^r = sum_{jvec} [prod_t x_{j_t}^{d-1} / prod_t
  prod_{a != j_t}(x_{j_t} - x_a)] prod_i (1 - T x_i prod_t x_{j_t})^{-1}
```

gives every `K_{m,d}` and `N_{m,d}` explicitly. The T-108510
top-coefficient law `(-1)^{C(d-1,2)} e_d^{d-1}` drops out in three
lines. Novelty position (boundary check 2026-08-31): Hadamard-product
rationality is classical (Jungen) and denominators come from
resultants, but the literature states no general closed NUMERATOR
form is known (Kar, RHUMJ 23 (2023)); the alternant is a closed
numerator for Hadamard powers of degree-d rational series — claimed
new in context, technique elementary/classical.

## Why it matters

The #764 defect programme's central objects — the obstructions to
pointwise transforms surviving as L-objects — are now EXPLICIT at
every rank and power: T-108508's correction-layer search becomes
expansion of one alternant, and the geometric reading (T-108515: the
defect as Segre K-polynomial cofactor) acquires its analytic engine.
```
