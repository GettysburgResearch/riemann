# The alternant closed form: every powered-coefficient defect numerator in explicit finite terms, and the general-rank square defect solved

```text
Status:  PROVED (Lemmas 1-2, Theorems A-B, Corollary — complete
         elementary proofs below). Machine: symbolic equality with the
         proved rank-3 and rank-4 closed forms; exact-integer-point
         agreement at ranks 5, 6, 7 (beyond every previously known
         closed form); the general-m series identity verified at
         (m,d) = (3,2), (3,3), (4,2), (4,3), (5,2); the top-coefficient
         law re-derived symbolically at d = 3, 4, 5.
Machine: research/exploratory/2026-08-30-two-programme-pass/matrix/
         alternant_defect.py + alternant_defect.json (ALL OK);
         stdlib replay experiments/X-108522-alternant-defect/.
Resolves: the OPEN general-d law of T-108508 (square defects had
         proved closed forms only for d <= 5, found by expansion);
         supplies the analytic engine predicted by T-108515
         Corollary 2 (the Lascoux-strand deposit).
Novelty position (boundary check 2026-08-31, web): rationality of
         Hadamard products of rational series is classical (Jungen),
         and the DENOMINATOR is classically computed by resultants;
         the current literature states that a general closed form for
         the Hadamard-product NUMERATOR "has not been found" (Kar,
         Rose-Hulman Undergrad. Math. J. 23 (2023); resultant/
         determinant methods compute instances). The alternant here
         is a closed numerator for the special family of Hadamard
         POWERS of a degree-d rational series — apparently stronger
         than what is standard, but the partial-fraction technique is
         elementary, so we position it as: new-in-context closed form
         answering T-108508's open law, with the technique classical.
RH status: RH and GRH are unproved; nothing here addresses them.
```

## Setting

`A` generic of rank d with distinct inverse roots `x_1, ..., x_d`;
`h_r = h_r(x)` the complete homogeneous coefficients;
`N_{m,d}(T) = det(1 - Sym^m(A) T) * sum_r h_r^m T^r` the defect
numerator (T-108500/T-108508/T-108510). All identities below are
polynomial identities in the `x_i` (denominators `x_j - x_a` cancel
in the total sums), hence extend to all points by continuity.

## Lemma 1 (Lagrange form of h_r)

For distinct `y_1..y_d` and every integer `r >= 0`:

```text
sum_{j=1}^d  y_j^{d-1+r} / prod_{a != j} (y_j - y_a)  =  h_r(y).
```

*Proof.* The bialternant form of the one-row Schur function:
`h_r = s_(r) = a_{(r+d-1, d-2, d-3, ..., 0)} / a_delta`. Expand the
numerator determinant along its first row (the `y_j^{r+d-1}` entries);
the j-th cofactor is the Vandermonde of the remaining variables, and
the sign bookkeeping turns the ratio of Vandermondes into
`1/prod_{a != j}(y_j - y_a)`. ∎

(Also used below with `r = -d`:
`sum_j y_j^{-1}/prod_{a != j}(y_j - y_a) = (-1)^{d-1}/e_d`, the
standard partial-fraction expansion of `prod_j y_j^{-1}`-type — proof:
apply partial fractions to `1/(w prod_j (w - y_j))` at `w = 0`, or
directly the same determinant expansion with the column
`(y_j^{-1})`.)

## Lemma 2 (partial-fraction form of the powered series)

For every `m >= 1`:

```text
sum_{r>=0} h_r(x)^m T^r
  = sum_{jvec = (j_1..j_{m-1}) in [d]^{m-1}}
      [ prod_t x_{j_t}^{d-1} / prod_t prod_{a != j_t}(x_{j_t} - x_a) ]
      * prod_{i=1}^d (1 - T x_i w_jvec)^{-1},     w_jvec = prod_t x_{j_t}.
```

*Proof.* Write `h_r^m = h_r * h_r^{m-1}` and apply Lemma 1 to each of
the `m-1` factors: `h_r^{m-1} = sum_{jvec} prod_t x_{j_t}^{d-1} *
w_jvec^r / prod_t prod_{a != j_t}(x_{j_t} - x_a)`. Then for fixed
`jvec`, homogeneity gives `sum_r h_r(x) w^r T^r = sum_r h_r(w x) T^r
= prod_i (1 - T x_i w)^{-1}`. Sum over `jvec`. ∎

This exhibits the powered series as a finite sum of `d`-fold
geometric products — the exact-denominator rationality of T-108500(1)
with an EXPLICIT numerator, for every m and d, and multiplying by
`det(1 - A^{tensor m} T) = prod_{i-vec} (1 - T prod x_{i_t})` (which
each summand's denominator divides) gives the equivariant
K-polynomial `K_{m,d}` in closed form.

## Theorem A (the general-rank square defect, closed form)

```text
N_{2,d}(T) = sum_{j=1}^d  x_j^{d-1}
             * prod_{a != j} (1 - x_a^2 T)
             * prod_{a < b, a,b != j} (1 - x_a x_b T)
             / prod_{a != j} (x_j - x_a) .
```

*Proof.* Lemma 2 at m = 2 and multiply by
`det(1 - Sym^2(A)T) = prod_{i <= i'} (1 - x_i x_{i'} T)`. For the
j-th summand, the denominator `prod_i (1 - T x_i x_j)` cancels
exactly the pairs involving j (including `(j,j)`), leaving
`prod_{a != j}(1 - x_a^2 T) * prod_{a<b, a,b != j}(1 - x_a x_b T)`. ∎

Degree check: each summand has T-degree
`(d-1) + C(d-1,2) = C(d,2)` — exactly `deg N_{2,d}` (T-108510).
Instances: d = 2 gives `1 + e_2 T` by hand; d = 3 equals `G_3` and
d = 4 equals `G_4 + 2 e_4 h_2 T^3 - 2 e_4^2 e_2 T^5` (both SYMBOLIC
machine identities, A1); d = 5, 6, 7 verified at exact integer points
against the independent matrix route (A2) — closed forms at ranks 6
and 7 did not previously exist in the repo.

## Corollary (T-108510's top-coefficient law re-derived)

The `T^{C(d,2)}` coefficient of Theorem A's j-th summand is
`(-1)^{(d-1) + C(d-1,2)} x_j^{d-1} prod_{a != j} x_a^2 *
prod_{a<b != j} x_a x_b / prod(x_j - x_a)`, and
`prod_{a != j} x_a^{2 + (d-2)} = (e_d/x_j)^d`, so the total is

```text
(-1)^{C(d,2)} e_d^d * sum_j x_j^{-1}/prod_{a != j}(x_j - x_a)
  = (-1)^{C(d,2)} e_d^d * (-1)^{d-1} / e_d
  = (-1)^{C(d-1,2)} e_d^{d-1}
```

(using `C(d,2) + d - 1 = C(d-1,2) + 2(d-1)`). This reproves the
all-d top-coefficient sign law of T-108510 by a second route.
(Machine: symbolic at d = 3, 4, 5.)

## Theorem B (general m)

Lemma 2 itself, together with the multiplication bookkeeping, gives
closed alternant forms for every `K_{m,d}` and (after dividing by the
T-108515 excess factors or `det(1 - Sym^m T)` directly) every
`N_{m,d}`: an `(m-1)`-fold alternant sum with fully explicit terms.
The series identity is machine-verified coefficientwise (r <= 12) at
five (m, d) pairs (A3). For d = 2 this re-expresses the T-108509
deformation-spectrum objects; the two-parameter (t, u)-plane of
L-108516 acts on it by the weighted scaling of every `x`-monomial.

## Addendum (same day): the stable layer theorems

T-108508's correction layers become theorems for ALL d via a
stability argument on the alternant.

**Stability Lemma.** (a) Setting `x_d = 0` maps `N_{2,d} ->
N_{2,d-1}` and `G_d -> G_{d-1}` (the h-series and the Sym^2/Lambda^2
weight multisets restrict; one line from Theorem A as well). Hence
each correction `corr_j(d) := [T^j](N_{2,d} - G_d)` is a sequence of
weight-2j symmetric polynomials compatible under restriction. (b)
The inverse limit of the weight-w graded pieces under restriction is
the weight-w part of the ring of symmetric functions, and the
projection to d variables is injective (indeed bijective) for
`d >= w`. So the WHOLE sequence is determined by its member at
`d = 2j`, and any e-polynomial identity verified symbolically in
`2j` variables holds for every d. ∎

**Layer Theorem 1 (T-108508's continuation guess, now for all d).**

```text
corr_3 = 2 sum_{i >= 4} (-1)^i e_i h_{6-i}
       = 2 (e_4 h_2 - e_5 h_1 + e_6)          for EVERY rank d.
```

Machine-verified as an exact symbolic identity at the determining
rank d = 6 (stable_layers.py; e-basis decomposition
`2 e_6 - 2 e_{5,1} - 2 e_{4,2} + 2 e_{4,1,1}` matches); the
Stability Lemma lifts it to all d. This upgrades T-108508's
"proved at ranks 4-5, exact-verified at rank 6, general d OPEN" to
PROVED for all d.

**Layer Theorem 2 (new; the T^4 layer for all d).**

```text
corr_4 = 2 sum_{i >= 5} (-1)^i e_i h_{8-i}
       = 2 (-e_5 h_3 + e_6 h_2 - e_7 h_1 + e_8)   for EVERY rank d
```

— the SAME alternating law with threshold shifted to `i >= j+1`.
Machine-verified at the determining rank d = 8 (e-basis
`2e_8 - 2e_{7,1} - 2e_{6,2} + 2e_{6,1,1} - 2e_{5,3} + 4e_{5,2,1}
- 2e_{5,1,1,1}`, equal to the displayed form); at d = 5 it collapses
to exactly T-108508's `-2 e_5 h_3`. Both theorems verified again by
the direct identity checks `corr_j == 2 sum_{i>=j+1} (-1)^i e_i
h_{2j-i}` at d = 6 and d = 8.

**The T^5 layer.** The same linear law CANNOT be complete at j = 5:
T-108508's rank-5 closed form has terms quadratic in the deep
elementaries (`e_2 e_4^2`, `e_5^2`) which the linear form cannot
produce at d = 5 (where all `e_i, i >= 6`, vanish). The stable
`corr_5` at the determining rank d = 10 — the first SECOND-LAYER
stable form — is computed by the same script (in progress at the
time of this addendum; deposited in stable_layers.json when
complete, with the linear part `2 sum_{i>=6} (-1)^i e_i h_{10-i}`
split off).

## What this changes

- T-108508's structure problem ("the general-d law is OPEN, the layer
  pattern deposited as machine-verified structure") is CLOSED: the
  correction layers are the expansion of Theorem A's alternant minus
  the Gauss-sign polynomial. The `e_4/e_5`-grading and the
  `corr_3 = 2 sum_{i>=4} (-1)^i e_i h_{6-i}` patterns become
  expansion identities of the alternant (their uniform derivation is
  now finite work per layer, not a search).
- T-108515's deposited Lascoux direction is realized analytically:
  the alternant IS the diagonal-restricted K-polynomial data of
  `P^{d-1} x P^{d-1}` divided by `det(1 - Lambda^2 T)`, with the
  d = 3 equivariant Betti table freshly ground-truthed by machine
  (matrix/segre_d3m2_betti.py: (1, 9, 16, 9, 1) at twists
  0, 2, 3, 4, 6, per-weight characters deposited).
- The survival-ladder analysis of #764 gains a uniform tool: every
  pointwise-power transform's obstruction is now an explicit finite
  expression, at every rank, ready for specialization (torsion loci,
  degeneration strata, natural-boundary criteria inputs).
```
