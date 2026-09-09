# L-108516 — The two-parameter deformation plane: fibration over the trace-scaling line, the Dahlquist axis, the purity wedge, and four-point rigidity

```text
Claim ID: L-108516
Status:   PROVED (Lemmas 1-4 and the Rigidity Theorem below are
          complete elementary proofs, UNCONDITIONAL — the single
          witness prime p = 2 settles every impurity needed; the
          density refinement outside the wedge imports Sato-Tate as
          labelled; natural-boundary refinements on the Dahlquist
          axis are NOT claimed, only referred to the pinned
          Estermann/Dahlquist criteria). Machine layer: every lemma
          certified exactly (n <= 20000 coefficientwise in Z[t,u];
          9591-prime exact wedge scan).
Created:  2026-08-31 (pass 3 continuation, Lane 2; extends L-108511's
          line to the full plane)
Programme: #764 (deformation moduli; survival trichotomy)
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          tu_atlas.py + tu_atlas.json (stdlib-exact; ALL OK)
Data:     11a1 exact a_p table (matrix/ap_table_11a1.json)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Setting

For `(t, u) in R^2` let

```text
Z_{t,u}(s) := prod_{p != 11} (1 - t a_p p^{-s} + u p^{1-2s})^{-1}
            = sum b_n(t, u) n^{-s}   (good-support n),
```

the two-parameter deformation plane of 11a1's local data. The
L-108511 trace-scaling line is the slice `u = 1`. Each `b_n in Z[t,u]`
(built from `H_k = t a_p H_{k-1} - u p H_{k-2}` at prime powers,
multiplicatively extended).

## Lemma 1 (grading; the plane fibers over the line)

Every `b_n(t, u)` is weighted-homogeneous of degree `Omega(n)` with
`wt(t) = 1`, `wt(u) = 2`.

*Proof.* Induction: `H_0 = 1`, `H_1 = t a_p` are graded, the
recurrence adds weight 1 via `t` and 2 via `u` while `Omega` counts
prime-power steps; products of graded coefficients are graded. ∎
(Machine: every monomial of every `b_n`, `n <= 20000`: True.)

Three consequences, each a one-line substitution:

1. **Fibration** `b_n(tau v, v^2) = v^{Omega(n)} b_n(tau, 1)`: over
   `Q(sqrt u)` (u > 0), `Z_{t,u}` is the `sqrt u`-root-scaling of the
   line point `Z_{t/sqrt u, 1}` — the upper half-plane is the
   L-108511 LINE times the Omega-graded scaling flow. Every
   structural question descends to the line plus bookkeeping.
2. **Liouville parity** `b_n(-t, u) = lambda(n) b_n(t, u)`
   (Omega odd/even; recovers L-108511's `Z_{-1}` as the Liouville
   twist of `Z_1`).
3. **Parabola** `b_n(t, t^2) = t^{Omega(n)} a_n`: the parabola
   `u = t^2` is the Omega-graded flow through `L(f)` itself
   (machine: `b_n(1,1) = a_n` re-derived by the Hecke recurrence on
   all prime powers).

## Lemma 2 (the Dahlquist axis t = 0)

With `zeta_u(s) := prod_p (1 - u p^{-s})^{-1} = sum u^{Omega(n)}
n^{-s}` (Dahlquist's family; superscript (11) = good primes only):

```text
Z_{0,u}(s) = zeta_{u^2}^{(11)}(4s - 2) / zeta_u^{(11)}(2s - 1).
```

*Proof.* Locally with `y = p^{1-2s}`:
`(1 + u y)^{-1} = (1 - u y) / (1 - u^2 y^2)`. ∎
(Machine: `Z_{0,u} * zeta_u(2s-1) == zeta_{u^2}(4s-2)`
coefficientwise as polynomials in `u`, all good `n <= 20000`: True.)

- `u = 1` recovers L-108511 Lemma 1.
- `u = -1` COLLAPSES: `zeta_{-1}(s) = zeta(2s)/zeta(s)` gives
  `Z_{0,-1} = zeta^{(11)}(2s - 1)` exactly (also directly: the local
  factor is `(1 - p^{1-2s})^{-1}`). Machine: `b_n(0,-1) = sqrt(n)` on
  good squares, else 0, all `n <= 20000`: True.
- For integer `u`, `zeta_u(s) = zeta(s)^u H_u(s)` with `H_u` an Euler
  product absolutely convergent for `Re s > 1/2` (elementary:
  `(1-ux)^{-1}(1-x)^u = 1 + O(x^2)`), so every integer point of the
  axis is meromorphic in a half-plane past the abscissa as a quotient
  of classical objects: stratum S2 in the trichotomy. Beyond that
  strip this axis is LITERALLY the family of the pinned
  Estermann/Dahlquist natural-boundary criteria; no boundary claim is
  made here.

## Lemma 3 (the purity wedge)

At a good prime, the local roots have equal moduli ("purity") iff
`t^2 a_p^2 <= 4 u p` or `t a_p = 0`. Consequently:

- **Inside** `{u >= t^2} union {t = 0}`: purity at EVERY good prime,
  unconditionally (Hasse: `t^2 a_p^2 <= 4 t^2 p <= 4 u p`; on the
  axis the roots are `+-` pairs).
- **Outside** (`{u < t^2, t != 0}`, which includes all `u <= 0` with
  `t != 0`): impurity occurs.
  UNCONDITIONAL witnesses suffice for the rigidity theorem below:
  `p = 2` (`a_2 = -2`, `a_2^2/2 = 2`) is impure whenever
  `4 u / t^2 < 2`, e.g. for every `|t| >= 2` on `u = 1` and for every
  `t != 0` at `u <= 0`. For `0 < u < t^2` the DENSITY of impure
  primes is the deformed Sato-Tate mass of
  `{|cos theta| > sqrt(u)/|t|}` (ST IMPORTED, as in L-108511; closed
  form elementary calculus); for `u <= 0, t != 0` every prime with
  `a_p != 0` is impure.
- Machine (exact, all 9591 good primes `p <= 1e5`, 54-cell grid):
  every inside cell has ZERO impure primes; every strictly-outside
  cell has thousands (1354-9550), first witness `p = 2` or `p = 61`:
  True in all cells.

Weight normalization: the product of the ROOT MODULI is `|u| p`, so
purity of MOTIVIC WEIGHT 1 (moduli exactly `sqrt p`) additionally
forces `|u| = 1`.

## Lemma 4 (integrality locus = Z^2 exactly)

`b_n(t, u) in Z` for all good n iff `(t, u) in Z^2`.

*Proof.* `b_5 = t a_5 = t` forces `t in Z` (`a_5 = 1`). Then
`b_4 = t^2 a_2^2 - 2u = 4 t^2 - 2u` forces `2u in Z` and
`b_9 = t^2 a_3^2 - 3u = t^2 - 3u` forces `3u in Z`, hence `u in Z`.
Conversely integer `(t, u)` preserve integrality through the
recurrence. ∎ (Machine witnesses: `b_5(1/2, 1) = 1/2`,
`b_9(1, 1/2) = -1/2`.)

## Rigidity Theorem (four classical points; unconditional)

The points of the ENTIRE plane that are simultaneously
(i) integral and (ii) weight-1 pure at every good prime are EXACTLY

```text
(1, 1)  = L^{(11)}(f, s) = L(f, s) (1 - 11^{-s})     [S1; modularity
                                                      IMPORTED]
(-1, 1) = sum' lambda(n) a_n n^{-s}
        = L^{(11)}(Sym^2 f, 2s)/(zeta^{(11)}(2s-1) L^{(11)}(f,s))
                                                     [S2; L-108511]
(0, 1)  = zeta^{(11)}(4s-2)/zeta^{(11)}(2s-1)        [S2; L-108511]
(0, -1) = zeta^{(11)}(2s-1)                          [S2-classical;
                                                      Lemma 2]
```

(All four rows are good-prime (p != 11) Euler products, matching the
definition of `Z_{t,u}`; since `a_11 = 1 != 0`, restoring the bad
factor changes `(1,1)` by exactly `(1 - 11^{-s})` — verification-wave
correction of an inherited bare-`L(f,s)` display, also fixed in
L-108511.)

*Proof.* Integrality forces `(t, u) in Z^2` (Lemma 4); weight-1
purity forces `|u| = 1` (Lemma 3). On `u = 1`: purity at `p = 2`
forces `2 t^2 <= 4`, so `t in {0, +-1}`. On `u = -1`: purity at
`p = 2` forces `4 t^2 <= -8` unless `t a_2 = 0`, so `t = 0`. Each
survivor is the displayed classical object. ∎

**Reading.** L-108511's rigidity ("on the line, survival as an
L-object singles out the arithmetic points") globalizes to the plane
with no new survivors: two parameters buy NO new arithmetic points —
the plane's entire arithmetic locus was already on the line. The
first non-survivor in each direction is named: `(2, 1)` is the
cube-defect bridge deformation `A_2` (T-108507, conditional S3), and
the parabola's integer points `|t| >= 2` (`sum a_n t^{Omega(n)}
n^{-s}`) are deposited as the parabola's S3 candidates. Combined with
the weighted homogeneity of all defect invariants (T-108500's
coefficient formula; T-108515), the (t, u)-deformation of the
pointwise-transform machinery pulls back the master (a, b)-atlas —
the resonance/collision atlas computed at `u = 1` (T-108509/T-108513)
is UNIVERSAL for the plane: deformation discovers no resonances the
(a, b)-plane does not already contain.
```
