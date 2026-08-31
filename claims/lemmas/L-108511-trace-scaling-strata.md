# L-108511 — The trace-scaling line crosses the survival trichotomy: exact quotient identities at t = 0 and t = -1

```text
Claim ID: L-108511
Status:   PROVED (both identities: complete elementary local proofs
          below, machine-certified coefficient-by-coefficient on all
          good-support n <= 20000); the t = 2 leg of the strata reading
          is CONDITIONAL (imported from T-108507's labelled corollary)
Created:  2026-08-31 (pass 3, campaign C2)
Programme: #764 (deformation moduli; survival trichotomy of T-108500)
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          c2_phase_diagram.py + c2_phase_diagram.json (exact checks) and
          c4_boundary_telescope.py + json (labelled float diagnostics)
Data:     11a1 (a_p exact by point counting, 9591 good primes <= 1e5,
          Hasse-verified; matrix/ap_table_11a1.json)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Setting

For `t in R` let `Z_t(s) := prod_{p != 11} (1 - t a_p p^{-s} + p^{1-2s})^{-1}`
be the trace-scaling line through the 11a1 local data (good primes
throughout; `f` = the weight-2 newform 11a1).

## Lemma 1 (t = 0). `Z_0(s) = zeta^{(11)}(4s-2) / zeta^{(11)}(2s-1)`.

*Proof.* Locally, with `y = p^{1-2s}`:
`(1 + y)^{-1} = (1 - y)/(1 - y^2) = (1 - p^{1-2s}) (1 - p^{2-4s})^{-1}`.
Multiply over good `p`. ∎

## Lemma 2 (t = -1). `Z_{-1}(s) = L^{(11)}(Sym^2 f, 2s) / ( zeta^{(11)}(2s-1) L(f, s) )`.

*Proof.* Locally, with Satake `alpha beta = p`, `alpha + beta = a_p`:

```text
(1 + a_p p^{-s} + p^{1-2s})^{-1}
  = (1 - a_p p^{-s} + p^{1-2s}) / (1 - (a_p^2 - 2p) p^{-2s} + p^2 p^{-4s})
```

(difference of the two quadratics: `(1+aT+pT^2)(1-aT+pT^2) =
1 - (a^2-2p)T^2 + p^2T^4`). The denominator is the local factor of the
Adams operation `psi^2` at `p^{-2s}` (eigenvalues `alpha^2, beta^2`),
and `det(1 - psi^2 X) = det(1 - Sym^2 X)/(1 - pX)`. Substitute
`X = p^{-2s}` and multiply over good `p`. ∎

Both identities are certified coefficient-by-coefficient on every
good-support `n <= 20000` (exact integer Dirichlet convolution;
c2_phase_diagram.json part2, both CONFIRMED).

## The strata reading (with labels)

One real line `{Z_t}` through the deformation space of 11a1's local
data meets the survival trichotomy of T-108500 as follows:

- `t = 1`: entire L-function with FE (S1) — IMPORTED modularity.
- `t = -1`: by Lemma 2, meromorphic on all of C as a quotient of
  automorphic L-functions (Sym^2 automorphy IMPORTED, Gelbart-Jacquet),
  with infinitely many poles at the zeros of `L(f, s)`: stratum S2.
  (`Z_{-1}` is the Liouville twist `sum lambda(n) a_n n^{-s}`.)
- `t = 0`: by Lemma 1, meromorphic on all of C with infinitely many
  poles at the zeros of `zeta(2s-1)`: stratum S2.
- `t = 2`: the trace-doubled deformation = the cube-defect bridge's
  `A_2` (T-108507); CONDITIONALLY (labelled corollary there) a natural
  boundary: stratum S3. Pass-3 addendum: the zero-constellation
  analysis (c4_boundary_telescope.json) places the conjectural
  accumulation line at `Re s = 3/2` — tempered primes put local zeros
  exactly there, the untempered band shrinks like `O(1/log p)` — and
  corrects an earlier working note (5/2 is the absolute-convergence
  edge, a different and irrelevant line). Honest control recorded
  there: dense local zeros alone do NOT imply a boundary (the t = 0
  quotient has them on `Re s = 1` and is meromorphic); the criterion
  input is the cyclotomic-vs-equidistributed root-angle dichotomy, and
  the measured angles match the deformed Sato-Tate law to L1 = 0.04.

## Rigidity + phase transition (exact + labelled parts)

- Integrality locus of the line is EXACTLY `t in Z` (`a_5 = 1` forces
  `t = t a_5 in Z`; conversely integral `t` preserves integrality).
- Temperedness of every local factor holds iff `|t| <= 1` (Hasse gives
  `t^2 a_p^2 <= 4p` for `|t| <= 1`, exact and exhaustively bookkept on
  the table; for `|t| > 1` violations exist and have the Sato-Tate
  density `D(t) = (2 theta* - sin 2 theta*)/pi`, `theta* =
  arccos(1/|t|)` — ST IMPORTED, closed form elementary calculus,
  empirical match at 9591 primes e.g. 0.3888 vs 0.3910 at t = 2).
- Hence the tempered + integral points of the line are exactly
  `t in {0, +-1}` — all of which are (quotients of) automorphic
  objects — while every integer `|t| >= 2` lies in the non-tempered
  regime whose first exemplar (t = 2) is the bridge deformation.
  Deposited as a rigidity phenomenon: on this line, "survives as an
  L-object with Euler product, FE, and temperedness" singles out
  exactly the arithmetic points.
```
