# T-108507 — The cube-defect bridge: the obstruction to cubing is the L-datum of the trace-doubled deformation

```text
Status:  PROVED for Theorems 1-4 below (complete elementary proofs, machine-
         verified in X-108507); the natural-boundary corollary is
         CONDITIONAL on a NAMED imported criterion and labelled so
Scope:   local/exact for the generic degree-2 object; the global identity
         is a formal Euler-product identity in the stated half-plane at
         good primes; nothing analytic beyond that is claimed
         unconditionally; RH and GRH are unproved and unaddressed
Exact sources or dependencies: T-108500 (defect law), O-108506 (purity
         stratification); classical inputs cited inline
What was actually run: experiments/X-108507-cube-defect-bridge/verify.py
         (stdlib, EXACT_RATIONAL)
Smallest remaining gap: the conditional corollary's imported criterion is
         not reproved here; making it unconditional for this specific
         family is the named follow-up target
```

Programme context: issue #764, axes A/B and central question 9 ("do
coherent twisted functional equations force a transformed object back into
a representation-theoretic or automorphic class?"). This theorem makes
that question EXACT for the cube transform: the analytic survival of the
cubed L-function is equivalent to the L-object status of a specific,
explicitly non-tempered coefficient deformation.

## Setting

Generic degree-2 local object `A` with Satake polynomial `1 - aT + bT^2`
(inverse roots `alpha, beta`; `a = alpha + beta`, `b = alpha beta`), and
its m=3 pointwise-power defect from T-108500:

```text
N_3(T) = 1 + 2ab T + b^3 T^2 ,      sum_k h_k^3 T^k = N_3(T) / det(1 - Sym^3(A) T).
```

**Definition (trace-doubled deformation).** `A_2` is the degree-2 local
datum with Satake polynomial `1 - 2a T + b T^2`: trace doubled,
determinant kept. This is a point on issue #764's deformation axis A
(a coefficient transform of the local parameter), chosen not by us but —
as Theorem 1 shows — by the cube transform itself. Write `gamma, delta`
for its inverse roots: `gamma + delta = 2a`, `gamma delta = b`.

## Theorem 1 (the bridge factorization)

```text
N_3(T) = (1 + b gamma T)(1 + b delta T) = det( 1 + b A_2 T ).
```

The m=3 defect is EXACTLY the local L-datum of the trace-doubled
deformation, rescaled by `b = det A` and sign-twisted: its inverse roots
are `-b gamma` and `-b delta`.

*Proof.* `(1 + b gamma T)(1 + b delta T)
= 1 + b(gamma + delta) T + b^2 (gamma delta) T^2
= 1 + 2ab T + b^3 T^2 = N_3(T)`. ∎

## Theorem 2 (the splitting-field identity — why the defect exits the character ring)

`Q(a,b)(gamma) = Q(a,b)(sqrt(a^2 - b))`, the SAME quadratic extension that
T-108500's Theorem 2 exhibited as the splitting field of `N_3`. So the
exit of the m=3 defect from the character ring of `A` is EXPLAINED: the
defect's inverse roots fail to be weight monomials of `A` because they are
(rescaled) weight monomials of a DIFFERENT object — the trace-doubled
deformation, whose Satake field is genuinely larger than the weight field
of `A`.

*Proof.* `gamma, delta = a ± sqrt(a^2 - b)` (roots of `X^2 - 2aX + b`),
so `Q(a,b)(gamma) = Q(a,b)(sqrt(a^2-b))`; and the inverse roots of `N_3`
are `-b gamma, -b delta` by Theorem 1, generating the same extension.
That this extension is neither trivial nor equal to
`Q(alpha, beta) = Q(a,b)(sqrt(a^2-4b))` is the content of T-108500
Theorem 2 (both `a^2-b` and `(a^2-b)(a^2-4b)` are nonsquares in
`Q(a,b)`). ∎

## Theorem 3 (the stratification transfer)

The purity stratification of the defect (O-108506) IS the temperedness
stratification of the deformation: for real specializations with
`b = p > 0`,

```text
|gamma| = |delta| = sqrt(p)   <=>   a^2 <= p   <=>   N_3 pure of weight 3 ;
a^2 > p: gamma, delta real with |gamma| = p^{1/2+theta}, |delta| = p^{1/2-theta},
         theta > 0 — the deformation VIOLATES the Ramanujan/purity bound,
         and the defect is impure, at exactly the same primes.
```

*Proof.* `gamma delta = p` and `gamma + delta = 2a`: complex-conjugate
pair iff `disc = 4(a^2 - p) < 0`, in which case both moduli are
`sqrt(gamma delta) = sqrt(p)`; real distinct otherwise, with product `p`
and distinct absolute values (equal absolute values with product `p` and
real sign pattern would force `gamma = delta = ±sqrt p`, i.e. `disc = 0`).
The defect's inverse roots are `-p gamma, -p delta` (Theorem 1), of moduli
`p^{3/2±theta}`; O-108506's two-case criterion is precisely `a^2` vs `p`. ∎

For a non-CM GL(2) eigenform datum, the violating stratum
`{p : a_p^2 > p}` has Sato-Tate density

```text
ST(|cos| > 1/2) = 2/3 - sqrt(3)/(2 pi) = 0.39100...
```

(exact value of the measure `(2/pi) sin^2` on `|cos theta| > 1/2`;
Sato-Tate is a THEOREM for non-CM elliptic modular forms — Clozel-Harris-
Shepherd-Barron-Taylor lineage, CITATION-NEEDED precision — imported as a
labelled input, not proved here).

## Theorem 4 (the global reduction, formal at good primes)

For a weight-normalized GL(2) coefficient system (`b = p` at every good
prime), in the half-plane of absolute convergence, as an identity of
Euler products over the good primes:

```text
sum'_n a_n^3 n^{-s} = L^{good}(Sym^3, s) x D(s),
D(s) := prod_p N_3(p^{-s}) = prod_p (1 + gamma_p p^{1-s})(1 + delta_p p^{1-s}),
```

(`sum'` = the multiplicative extension over good primes). `D(s)` is a
degree-2 Euler product whose parameter data is the TRACE-DOUBLED
deformation's Satake data, Tate-shifted by 1, sign-twisted. Hence the
question "does the cube of an L-function admit a good completion?" is
EQUIVALENT, modulo the standard `Sym^3` factor (automorphic: Kim-Shahidi;
CITATION-NEEDED precision), to "is the trace-doubled deformation an
L-object?" — a coefficient deformation that is provably non-tempered on a
density-`0.391` set of primes.

*Proof.* `a_n^3` is multiplicative in `n`, so its Dirichlet series over
good primes is the Euler product of the local series
`sum_k a_{p^k}^3 T^k = N_3/det(1 - Sym^3 T)` (T-108500); split each local
factor by Theorem 1 and collect. Absolute convergence of all three
products in a right half-plane follows from `|a_p| <= 2 sqrt p`
(Ramanujan-Deligne for the source object, imported) and the explicit root
bounds of Theorem 3. ∎

## Conditional corollary (labelled; NOT a theorem of this pass)

The governing theory for the meromorphy of Euler products is
Estermann's theorem (a uniform one-variable Euler product continues
meromorphically to all of C iff its local polynomial is a product of
cyclotomic factors; otherwise `Re s = 0` is a natural boundary), extended
by Dahlquist, and by Kurokawa's meromorphy theorems for non-uniform
products (T. Estermann ~1928; G. Dahlquist ~1952; N. Kurokawa, "On the
meromorphy of Euler products" I-II, Proc. London Math. Soc. 1986, announced
Proc. Japan Acad. 1978; multivariable extensions: Bhowmik-Essouabri-
Lichtin; Delabarre). Under the applicability of the Kurokawa-type
criterion to the family `{N_3(p^{-s})}` — whose parameter data
equidistributes per Sato-Tate and is non-tempered on a fixed-density
stratum, hence is "of non-Galois/non-automorphic type" in the sense those
criteria quantify — `D(s)` has a NATURAL BOUNDARY, and consequently the
cubed series `sum' a_n^3 n^{-s}` occupies stratum S3 of T-108500's
survival trichotomy: the cube transform destroys L-ness irreparably, not
just at the level of missing functional equations. This corollary is
CONDITIONAL on the imported criterion applying to this specific
non-uniform family; verifying that applicability (or proving the boundary
directly for `D`) is the named follow-up target, deliberately not claimed
here.

## What the bridge changes structurally (#764 reading)

The three previously separate exact facts about the cube transform —
defect self-duality (T-108500(4)), character-ring exit (T-108500 Thm 2),
angle-stratified purity (O-108506) — are now ONE fact seen three ways:
the cube's obstruction is the L-datum of another deformation. Self-duality
of the defect = self-duality of `A_2`'s Satake pair; the exit field
`Q(sqrt(a^2-b))` = `A_2`'s Satake field; the purity stratification =
`A_2`'s temperedness stratification. Deformations obstruct each other in
a structured way: the failure of one point of the deformation space to be
functorial is measured by the local data of ANOTHER point. Whether this
"obstruction duality" extends beyond the cube (is the m=5 defect a
product of L-data of other named deformations? the recurring factor
`a^2 - b = tr Sym^2 A_2 /... ` in the m=5,6 tables suggests yes) is
deposited as the sharpest new question of this pass.
```
