# The Segre bridge: the powered-coefficient defect is the equivariant K-polynomial of the Segre embedding of (P^1)^m

```text
Status:  PROVED. Theorem 1 (coarse bridge, all m): complete proof from
         the ballot decomposition + T-108500(1). Theorem 2 (fine
         bridge at m = 3): exact machine computation of the full
         equivariant Betti table (integer/Fraction Koszul homology, a
         finite exact computation = proof) + hand-verified identities.
         Theorem 3 (geometric second proof of the defect functional
         equation T-108500(3)): complete, with ONE imported classical
         ingredient labelled inline (Stanley reciprocity for normal
         affine semigroup rings); Lemmas A, B are proved here
         elementarily. Corollaries 1-2 proved. The Lascoux
         identification for general rank at m = 2 is a DEPOSITED
         DIRECTION, labelled, not a claim.
Machine: research/exploratory/2026-08-30-two-programme-pass/matrix/
         segre_coarse_check.py (symbolic verification of Theorem 1,
         m = 2..4 complete over Q(alpha, beta)),
         segre3_betti.py + segre3_betti.json (+ .log) (the Theorem 2
         table; stdlib-exact), segre_rank3_check.py (the Corollary 2
         held-out rank-3 identity), and the independent stdlib replay
         experiments/X-108515-segre-bridge/verify.py (coarse bridge at
         exact integer points through actual Kronecker/symmetric-power
         matrices and integral Faddeev-LeVerrier, m = 2..6; Eulerian
         specialization m = 2..6; self-duality instances) — all green,
         including under python3 -O.
Depends: T-108500 (defect law; statements (1) and (3)), T-108508
         (rank-3 square defect N_{2,3} = G_3, used in Corollary 2).
Context: this realizes Priority 1 of the external programme review
         (identify the defect numerator with syzygy/K-theoretic data
         of the Segre embedding), found and proved independently of
         the review's sketch.
RH status: RH and GRH are unproved; nothing here addresses them.
```

## Setting

`V` is a 2-dimensional space, `A in GL(V)` generic with inverse roots
`alpha, beta`; `a = alpha + beta`, `b = alpha beta`, so
`det(1 - A T) = 1 - aT + bT^2`. `h_r = h_r(alpha, beta) = Tr Sym^r(A)`
are the coefficients (`h_0 = 1`, `h_1 = a`,
`h_r = a h_{r-1} - b h_{r-2}`), and `N_m(T)` is the T-108500 defect
numerator: `sum_r h_r^m T^r = N_m(T) / det(1 - Sym^m(A) T)` with
`N_m(0) = 1`, `deg N_m = m - 1`.

The object that opens the bridge is the **Segre ring**

```text
R_m := (+)_{r >= 0} (Sym^r V)^{tensor m},
```

the homogeneous coordinate ring of the Segre embedding
`(P^1)^m -> P(W)`, `W := V^{tensor m}`. Since
`char (Sym^r V)^{tensor m} = h_r^m`, the A-equivariant Hilbert series
of `R_m` **is the powered-coefficient series**:

```text
Hilb_{R_m}(A; T) = sum_r h_r(A)^m T^r .
```

`R_m` is a module over the free ring `S = Sym(W)` (degree-1 generators
carrying the weight multiset of `W`), so its equivariant Hilbert
series has the standard K-theoretic numerator

```text
K_m(A; T) := det(1 - A^{tensor m} T) * Hilb_{R_m}(A; T)
           = sum_i (-1)^i sum_j char Tor_i^S(R_m, C)_j * T^j ,
```

the **equivariant K-polynomial of the Segre variety**. Everything
below computes this object and matches it against the defect.

## Lemma 1 (ballot decomposition of the tensor power)

As GL(V)-representations,

```text
V^{tensor m} = (+)_{k=0}^{floor(m/2)}
               (Sym^{m-2k} V (x) det^k)^{(+) c_k},
c_k = C(m, k) - C(m, k-1)      (ballot / Catalan-triangle numbers).
```

**Proof.** Characters: `char V^{tensor m} = (alpha + beta)^m =
sum_j C(m, j) alpha^{m-j} beta^j`, and
`char(Sym^{m-2k} (x) det^k) = (alpha beta)^k
sum_{i=0}^{m-2k} alpha^{m-2k-i} beta^i`. For `k <= m/2` the monomial
`alpha^{m-k} beta^k` occurs in the k'-th character iff `k' <= k`, each
time with coefficient 1; comparing coefficients gives
`C(m, k) = sum_{k' <= k} c_{k'}`, i.e.
`c_k = C(m,k) - C(m,k-1)`. ∎

## Theorem 1 (the coarse bridge, every m)

```text
K_m(A; T) = N_m(T) * prod_{k=1}^{floor(m/2)}
            det(1 - Sym^{m-2k}(A) * b^k T)^{c_k} .
```

**Proof.** By Lemma 1,
`det(1 - A^{tensor m} T) = prod_{k=0}^{floor(m/2)}
det(1 - Sym^{m-2k}(A) b^k T)^{c_k}`, and the `k = 0` factor is
`det(1 - Sym^m(A) T)` with `c_0 = 1`. Multiply T-108500(1),
`sum_r h_r^m T^r = N_m / det(1 - Sym^m(A) T)`, by the full product. ∎

Two readings, both exact:

1. **The defect is syzygy data.** `N_m(T)` = the equivariant
   K-polynomial of the Segre embedding of `(P^1)^m`, divided by the
   fully explicit "excess-strand" factors coming from the lower
   plethysm strands of `V^{tensor m}`. The object that arose in #764
   as an analytic obstruction (the defect of pointwise transforms) is
   IDENTIFIED with a finite free resolution's alternating character
   sum.
2. **Degree bookkeeping.** `deg K_m = (m-1) + sum_{k>=1} c_k(m-2k+1)
   = 2^m - 2`: the K-polynomial misses the ambient degree `2^m` by
   exactly 2 — the a-invariant of Theorem 3.

Example (m = 4): `K_4 = N_4 * det(1 - b Sym^2(A) T)^3 * (1 - b^2 T)^2`.

Machine: symbolic over `Q(alpha, beta)` for m = 2, 3, 4
(segre_coarse_check.py: tail-vanishing window + coefficientwise
equality, all True); exact integer instantiations for m = 2..6 through
an INDEPENDENT route — actual Kronecker-product and symmetric-power
matrices, integral Faddeev-LeVerrier determinants — in
X-108515-segre-bridge (all PASS). The m = 5, 6 symbolic expansions are
computationally heavy and were not completed; the proof above covers
all m, so machine work is corroboration, not the basis of the claim.

## Corollary 1 (the defect is an equivariant Eulerian polynomial)

At the trivial point `(a, b) = (2, 1)` (i.e. `alpha = beta = 1`):

```text
N_m(T)|_(2,1) = A_m(T),   the m-th Eulerian polynomial
                (A_2 = 1 + T, A_3 = 1 + 4T + T^2,
                 A_4 = 1 + 11T + 11T^2 + T^3, ...).
```

**Proof.** `h_r(1, 1) = r + 1` and
`det(1 - Sym^m(A) T)|_(2,1) = (1 - T)^{m+1}`, so T-108500(1)
specializes to `sum_r (r+1)^m T^r = N_m(2,1;T)/(1-T)^{m+1}`; comparing
with the classical Worpitzky/Eulerian identity
`sum_r (r+1)^m T^r = A_m(T)/(1-T)^{m+1}` (classical; equivalent to the
statement that the h-polynomial of the unit m-cube's toric ring is
Eulerian) gives the claim. ∎ (Machine: V3 of X-108515, m = 2..6.)

So the defect numerator is a **two-parameter GL_2-equivariant
deformation of the Eulerian polynomial**, and the self-duality
T-108500(3) specializes at `(2,1)` to the classical palindromy of the
Eulerian numbers. This also positions the tower invariants of
T-108509/T-108513 (spectrum polynomials, torsion resonances) as
structures living OVER the Eulerian polynomial's deformation space.

## Theorem 2 (the fine bridge at m = 3: exact equivariant Betti table)

The minimal free resolution of `R_3` over `S = Sym(V^{tensor 3})` has
equivariant Betti characters (machine-exact: integral Koszul homology
per torus weight, Fraction-exact ranks; segre3_betti.py, output
segre3_betti.json — a finite exact computation):

```text
Tor_0 = C                                   (internal degree j = 0)
Tor_1 = 3 * det^2 Sym^2                     (j = 2;  dimension 9)
Tor_2 = 2 * det^3 Sym^3 (+) 4 * det^4 Sym^1 (j = 3;  dimension 16)
Tor_3 = 3 * det^5 Sym^2                     (j = 4;  dimension 9)
Tor_4 = det^9                               (j = 6;  dimension 1)
```

(`det^k Sym^j` denotes the character `b^k h_j`; total Betti numbers
`(1, 9, 16, 9, 1)`, consistent with the known resolution of the
2x2x2 Segre — CITATION-NEEDED for the precise classical reference.)
Consequences, each verified coefficientwise by hand AND by machine:

1. **K-polynomial assembly.**
   `K_3 = 1 - 3 b^2 (a^2 - b) T^2 + 2 a^3 b^3 T^3
        - 3 b^5 (a^2 - b) T^4 + b^9 T^6`,
   where the `T^3` coefficient exhibits the strand cancellation
   `2 b^3 h_3 + 4 a b^4 = 2 a^3 b^3`.
2. **The bridge, fine form.** `K_3 = N_3 * (1 - abT + b^3 T^2)^2` with
   `N_3 = 1 + 2abT + b^3 T^2`: the cube-bridge defect (T-108500(4),
   T-108507) is recovered from syzygy characters alone, and the
   excess factor is `det(1 - A * bT)^2` — the two `c_1 = 2` copies of
   the strand `V (x) det` of Lemma 1.
3. **Equivariant Gorenstein self-duality, visible.** The table
   satisfies exactly
   `Tor_i @ j  ~=  det^9 (x) (Tor_{4-i} @ (6-j))^dual`
   (checked for all (i, j): e.g. Tor_1@2 has weights
   `{alpha^4 beta^2, alpha^3 beta^3, alpha^2 beta^4}` each x3, exactly
   `det^9 (x) (Tor_3@4)^dual`). This is the resolution-level
   Gorenstein duality with `omega_{R_3} ~= b^3 * R_3(-2)`, i.e. the
   canonical module is the `(-2)`-shift twisted by `det(V)^3` — the
   equivariant refinement of `(1, 9, 16, 9, 1)`-symmetry.

## Theorem 3 (geometric second proof of the defect functional equation)

**Claim (= T-108500(3)).**
`N_m(T) = b^{m(m-1)/2} T^{m-1} N_m(1/(b^m T))`.

The original proof was combinatorial (weight-multiset inversion +
homogenization). Here is the geometric mechanism.

**Lemma A (the Segre ring is the full cube semigroup ring;
normality).** `R_m` is the semigroup ring of ALL lattice points of the
cone over the unit m-cube: writing a monomial of
`(Sym^r V)^{tensor m}` as `(s_1, ..., s_m; r)` with `0 <= s_i <= r`
(`s_i` = the y-degree in factor i), every such lattice point is a sum
of `r` height-1 vertices, explicitly `v^{(t)}_i = [t <= s_i]` for
`t = 1..r` (each `v^{(t)} in {0,1}^m`, and
`sum_t v^{(t)}_i = s_i`). So the semigroup generated by the cube
vertices at height 1 is saturated — `R_m` is a normal affine semigroup
ring of dimension m + 1. ∎

**Lemma B (interior points = `b^m T^2`-shift).** The interior lattice
points of the cone (`0 < s_i < r` for all i) are in weight-exact
bijection with ALL lattice points via
`(s; r) -> (s - (1,...,1); r - 2)`: the constraint `0 < s_i < r`
becomes `0 <= s_i - 1 <= r - 2`, and the character ratio is
`prod_i alpha^{(r - s_i) - (r - 2 - (s_i - 1))} beta^{s_i - (s_i-1)}
* T^2 = (alpha beta)^m T^2 = b^m T^2`. Hence
`Hilb_interior(A; T) = b^m T^2 * Hilb_{R_m}(A; T)`. ∎
(Equivalently: `[-1, 1]^m` is reflexive — the cube is Gorenstein of
index 2 — and `omega_{R_m} ~= b^m * R_m(-2)`, the general-m form of
Theorem 2(3).)

**Imported ingredient (labelled).** Stanley's reciprocity theorem for
normal affine semigroup rings (fine-graded form; Stanley 1974 /
Danilov — IMPORTED_THEOREM): for a pointed, full-dimensional normal
affine semigroup of rank d,
`Hilb(x^{-1}) = (-1)^d Hilb_interior(x)` as rational functions. Here
d = m + 1 and inversion of all fine weights is
`(alpha, beta, T) -> (alpha^{-1}, beta^{-1}, T^{-1})` (the character
map is linear on the cone lattice), so with Lemma B:

```text
Hilb_{R_m}(alpha^{-1}, beta^{-1}; T^{-1})
   = (-1)^{m+1} b^m T^2 Hilb_{R_m}(alpha, beta; T).      (FE-H)
```

**Transfer to the defect.** Write `Q_m = det(1 - Sym^m(A) T)`, with
weight multiset `{alpha^{m-i} beta^i}` of product `b^{m(m+1)/2}`.
Inverting each factor,
`Q_m(inv) = (-1)^{m+1} b^{-m(m+1)/2} T^{-(m+1)} Q_m`. Multiplying by
(FE-H), the signs `(-1)^{m+1}` cancel:

```text
N_m(inv) = Q_m(inv) * Hilb(inv) = b^{-m(m-1)/2} T^{-(m-1)} N_m .
```

Finally, the T^i-coefficient `c_i in Z[a, b]` of `N_m` is homogeneous
of degree `m i` in `(alpha, beta)` and symmetric, and for a symmetric
homogeneous polynomial of degree `mi`,
`c_i(alpha^{-1}, beta^{-1}) = b^{-mi} c_i(alpha, beta)` (each monomial
`alpha^p beta^q`, `p + q = mi`, inverts to `b^{-mi}` times its
alpha-beta swap). So `N_m(inv) = sum_i c_i b^{-mi} T^{-i}`, and
comparing coefficients in the display above gives
`c_i = b^{m(m-1)/2 - m(m-1-i)} c_{m-1-i}` — precisely T-108500(3). ∎

**Mechanism, stated plainly:** the self-duality of the defect — "the
obstruction to functoriality is itself self-dual" — IS Gorenstein
duality of the unit cube (`[-1,1]^m` reflexive, canonical module =
`det^m`-twisted 2-shift). A functional equation discovered by
coefficient algebra now has a geometry supplying it. (Machine: V4 of
X-108515 checks the coefficientwise FE at every integer point.)

## Corollary 2 (held-out test at rank 3, and the general-rank m = 2 bridge)

For `dim V = d` and `m = 2`: `V^{tensor 2} = Sym^2 V (+) Lambda^2 V`,
so the same two-line argument as Theorem 1 gives

```text
K_{2,d}(A; T) = N_{2,d}(T) * det(1 - Lambda^2(A) T),
```

with `N_{2,d}` the rank-d square defect of T-108508. **Held-out
machine test at d = 3** (the identity was PREDICTED by the bridge and
then computed): `K_{P^2 x P^2}` equals
`G_3(T) * det(1 - Lambda^2(A) T)` exactly, where `G_3` is the
Gauss-sign exterior-square polynomial — matching `N_{2,3} = G_3`
(T-108508) — verified symbolically in the inverse roots
(alpha, beta, gamma), tail window zero. Rank 2 by hand:
`K_{2,2} = (1 + bT)(1 - bT) = 1 - b^2 T^2`.

**Deposited direction (not a claim):** `P^{d-1} x P^{d-1}` is the
determinantal variety of 2x2 minors of a generic d x d matrix, whose
minimal free resolution is classical (Lascoux; CITATION-NEEDED for
the precise strand characters). By the display above, T-108508's
correction layers (the `e_4`/`e_5`-graded corrections to the
Gauss-sign law) must be READABLE OFF the Lascoux strand characters —
a closed-form route to the general-d square-defect law that bypasses
the symbolic expansions of T-108508. This is the natural next
theorem; it is deposited, not proved here.

## What is new here vs imported

- IMPORTED (labelled inline): Stanley reciprocity for normal
  semigroup rings; the Worpitzky/Eulerian identity; the classical
  resolution shape of the 2x2x2 Segre (used only as a consistency
  note); Lascoux resolutions (deposited direction only).
- PROVED HERE: the identification
  `Hilb_{R_m} = sum h_r^m T^r` and Theorem 1 (the exact factorization
  of the Segre K-polynomial with the defect as cofactor); the
  equivariant Betti table at m = 3 with its `det^9`-self-duality; the
  Gorenstein second proof of T-108500(3) via Lemmas A + B; the
  Eulerian specialization `N_m(2,1) = A_m`; the rank-3 held-out
  corollary.
- The novelty risk to audit later: the UNGRADED statement "Segre
  rings of (P^1)^m are Gorenstein toric rings of the cube" is
  classical; what we have not found in the literature is the
  IDENTIFICATION of the powered-coefficient defect `N_m` (an
  L-function-side object from #764) with the Segre K-polynomial
  cofactor, the equivariant Eulerian deformation reading, and the
  defect-FE-as-cube-reflexivity mechanism. Flagged for the next
  boundary audit.
