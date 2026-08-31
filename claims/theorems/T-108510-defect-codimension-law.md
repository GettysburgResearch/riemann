# T-108510 — The defect codimension law: numerator degree deficit = backward vanishing order

```text
Claim ID: T-108510
Status:   PROVED (Theorem 1 unconditional; Corollaries 1-5 with stated
          genericity where noted); the central reciprocity lemma is
          CLASSICAL (Stanley; reproved in two lines in the standalone so
          nothing is imported unverified)
Created:  2026-08-31 (pass 3)
Programme: #764 research modes 1/3; explains every defect degree in the
          programme and closes T-108508's open top-coefficient sign law
Depends on: T-108500 (d=2 degrees, as the special case), T-108508
Proof:    standalone/2026-08-31-defect-codimension-law/PROOF.md
Machine:  matrix/c1_defect_atlas.py Parts B/C (10 grid cells + transform
          families) + experiments/X-108510-codimension-law/ (stdlib
          replay; nu computed INDEPENDENTLY by backward recurrence)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

For any exponential-polynomial coefficient function `phi` with proper
rational generating function `N/Q` in lowest terms:

```text
deg N = deg Q - nu,    nu := min{ j >= 1 : phi(-j) != 0 },
c_top(N) = - q_D * phi(-nu),
```

where `phi(-j)` is the canonical backward continuation and `q_D` the
leading coefficient of `Q`. No genericity is needed for this equality.
Instantiations (using the classical backward vanishing
`h_{-1} = ... = h_{-(d-1)} = 0`, `h_{-d} = (-1)^{d-1}/e_d`):

1. **Codimension-d law**: `deg N_{m,d} = C(d+m-1, m) - d` for the m-th
   Hadamard power of a degree-d object (all 10 atlas grid cells).
2. **All-d top-coefficient law**:
   `c_top(N_{2,d}) = (-1)^{C(d-1,2)} e_d^{d-1}` — proving T-108508's
   sign conjecture for every d (previously proved only d <= 5).
3. **Hadamard products**: codimension = MAX of the factor degrees
   (generically). The X-108510 replay's mixed-triple test was first
   written expecting the min-law and REFUTED it; the corrected max-law
   is what the proof establishes (backward zeros of the factors
   reinforce). Rankin (2,2): codimension 2 = the classical numerator
   degree.
4. **Shifts destroy the deficit** (`nu = 1`); **sections divide it**
   (`nu = ceil(d/u)` for `k -> uk`), both verified including the new
   d=3, u=2 prediction (deg (N,Q) = (1,3)).

## Mechanism reading (for the #763/#764 matrix)

Two distinct shadows of the functional equation live in exact
coefficient sequences: BACKWARD VANISHING (h_{-1..-(d-1)} = 0) and
NUMERATOR SELF-DUALITY. This law proves they have different survival
grammars: backward vanishing is degree-robust (consumed whole by powers,
governed by the deepest factor in products, destroyed by shifts), while
self-duality is rank-2-specific (atlas Part B: scaled palindromy fails
for d >= 3). The two mechanisms are INDEPENDENT — a new row for the
mechanism-ablation matrix.
```
