# L-108005 — The quantitative mechanism dictionary: spectral bound ⟷ critical-circle location, and its transfer

```text
Claim ID: L-108005
Status:   PROVED (short proofs inline; the parametrization itself is
          STANDARD and cited — this lemma's role is the exact assembled
          dictionary + certified corpus instances + the transfer statement
          feeding the next-pass mechanism theorem)
Created:  2026-08-31 (continuation pass)
Programme: #763 (upgrades T-108000's co-occurrence toward a mechanism
          theorem: the graph and function-field worlds share ONE exact
          dictionary; only the supplier of the bound differs)
Depends on: T-108000 corpus certificates; standard spectral graph theory
          (imported: the tempered/untempered tree-spectrum parametrization
          — Lubotzky-Phillips-Sarnak, Serre, Terras lineage;
          CITATION-NEEDED precision)
Replay:   experiments/X-108005-mechanism-dictionary/  (EXACT_RATIONAL;
          includes the resultant-based exact pole census)
RH status: RH and GRH are unproved; this lemma does not address them.
```

## Statement

Let `X` be a finite connected `(q+1)`-regular graph. Each adjacency
eigenvalue `lambda` contributes to `1/zeta_X(u)` the quadratic factor
`1 - lambda u + q u^2`, whose roots `u_-, u_+` satisfy the PAIRING
`u_- u_+ = 1/q` (the functional-equation constraint). Then, writing
`u = q^{-s}`:

1. **(tempered case)** `lambda^2 <= 4q` iff the pair is complex-conjugate
   with `|u_±| = q^{-1/2}` exactly — both poles ON the critical line
   `Re s = 1/2`.
2. **(untempered case)** `lambda^2 > 4q` iff the pair is real with
   `q u_+^2 > 1 > q u_-^2` strictly — the poles sit at
   `Re s = 1/2 ∓ delta/log q` with

   ```text
   delta(lambda) = arccosh( |lambda| / (2 sqrt q) )  > 0 :
   ```

   an explicit, strictly monotone, invertible dictionary between the
   spectral excess and the LINEAR deviation from the critical line
   (`lambda = ±(q+1)` gives `delta = (1/2) log q`, i.e. `Re s ∈ {0,1}` —
   the trivial poles — as the extreme case).
3. **(transfer)** For a curve over `F_q`, the zeta numerator's inverse
   roots pair as `alpha alpha' = q` — the SAME Vieta constraint after
   `u = q^{-s}` — and the SAME two-case sign criterion decides
   `|alpha| = sqrt q` versus a real pair straddling it. The dictionary
   (bound excess ⟷ linear off-line deviation) is literally one algebraic
   correspondence shared by the two worlds; the worlds differ ONLY in what
   SUPPLIES the bound: self-adjointness + spectral gap (graphs) versus
   Weil purity (curves). At number fields no finite supplier is known —
   the dictionary states in one formula what a "Riemann structure" must
   produce: a mechanism forcing the `lambda`-analogues below `2 sqrt q`.

## Proofs

(1)-(2): Vieta gives `u_- u_+ = 1/q` and `u_- + u_+ = lambda/q`;
discriminant `lambda^2 - 4q` decides complex-conjugate (then
`|u|^2 = u bar u = 1/q`) versus real. In the real case with
`lambda > 2 sqrt q` (WLOG `lambda > 0`): `q u_+^2 > 1` iff
`lambda u_+ > 2` iff `lambda^2 + lambda sqrt(lambda^2-4q) > 4q`, true
since `lambda^2 > 4q`; and `q u_-^2 < 1` iff
`lambda sqrt(lambda^2-4q) > lambda^2 - 4q`, i.e. (both sides positive)
`lambda^2 (lambda^2-4q) > (lambda^2-4q)^2`, i.e. `lambda^2 >
lambda^2 - 4q`, true. For the arccosh form: `sqrt q u_+ =
[lambda + sqrt(lambda^2 - 4q)]/(2 sqrt q) = cosh t + sinh t = e^t` with
`cosh t = lambda/(2 sqrt q)`, so `log(sqrt q u_+) = delta` as stated, and
`|u_±| = q^{-1/2} e^{±delta}` translates to `Re s = 1/2 ∓ delta/log q`.
(3): the curve numerator `1 - a T + q T^2` (genus 1; general genus
factors into such pairs by the functional equation) has the identical
Vieta/discriminant structure; the two-case criterion is T-108002's exact
degree-2 purity test. ∎

## Certified instances (X-108005, all exact)

- K4 and Petersen (q = 2): ZERO eigenvalue-squares strictly inside
  `(8, 9)` (Sturm count with the trivial endpoint subtracted exactly) —
  every non-trivial pole pair on the critical circle.
- Prism `C16 x K2`: exactly ONE eigenvalue-square strictly inside
  `(8, 9)`, and — by the exact resultant census
  `R(u) = u^{|V|} p_X((q u^2 + 1)/u)`, an integer polynomial whose real
  roots are the real pole positions — exactly ONE off-circle real pole in
  `(0.708, 0.999)`: the dictionary's two sides match one-for-one on the
  certified instance, and Petersen's census in the same window is zero.
- Function-field witness: `y^2 = x^3 + x + 1 / F_5` (exact point count):
  discriminant negative, conjugate pair of modulus `sqrt 5` — the same
  criterion, purity-supplied.

## Novelty position

The parametrization `lambda = 2 sqrt q cosh(delta)` of the untempered
tree spectrum is STANDARD (imported, cited above); Terras's zeta
dictionary is the ancestor of the comparative view. Deposited as new
here: the assembled two-directional dictionary with the pairing
constraint made explicit as the FE shadow, the exact resultant-based pole
census technique with Sturm certificates, the one-for-one certified
instance matching, and the transfer formulation that reduces "find a
Riemann structure for the graph/FF package" to "name the supplier of the
bound" — the precise input the next-pass mechanism theorem needs.
```
