# Formalization audit

```text
Status: SOURCE-LOCKED / REMOTE-AUDITED / LOCAL-REPLAY-PENDING
Upstream: AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7
Toolchain: leanprover/lean4:v4.34.0-rc2
License: Apache-2.0
RH: unproved
```

## 1. Repository surface

The default umbrella module imports four layers:

```text
ZetaZeros.Hilbert.*              abstract Hilbert-space proof
ZetaZeros.Zeta.*                 zero sets, reflection, pair sums, transfer
ZetaZeros.MontgomeryTaylor.*     extremal profile and analytic reduction
ZetaZeros.Numeric.*              rigorous numerical inequality for decimal constants
ZetaZeros.Main                   final conditional zeta proportions
```

The largest proof-engineering concentration is
`ZetaZeros/Hilbert/AlphaExpansion.lean`. It packages the long coefficient,
orthogonality, range-splitting, and Bessel argument. This is a review hotspot:
a successful kernel check is not a substitute for checking that the large
formal statement matches Proposition 2.1 exactly.

## 2. Six comparator targets

The Comparator configuration checks the following challenge declarations:

```text
ZetaZeros.Challenge.prop_simple_real_lower
ZetaZeros.Challenge.prop_distinct_lower
ZetaZeros.Challenge.thm_simple
ZetaZeros.Challenge.thm_distinct
ZetaZeros.Challenge.thm_simple_numeric
ZetaZeros.Challenge.thm_distinct_numeric
```

It permits only:

```text
propext
Quot.sound
Classical.choice
```

and enables Nanoda.

### Correct interpretation

This proves that the solution terms match the challenge theorem types and do
not depend on undeclared project axioms.

It does **not** prove that the final zeta statements are closed theorems in
Lean, because their types explicitly quantify over:

```lean
hRvM : RiemannVonMangoldt
hPC  : PairCorrelation
```

External mathematical facts encoded as theorem parameters do not appear in
`#print axioms`.

## 3. Closed versus conditional declarations

| Layer | Production declaration | Formal status at the pinned SHA |
| --- | --- | --- |
| abstract simple-real inequality | tagged `prop_simple_real_lower` implementation | closed under structural hypotheses on `eta`, `Z`, and `m` |
| abstract distinct-point inequality | tagged `prop_distinct_lower` implementation | closed under the same structural hypotheses |
| exact simple-line proportion | `ZetaZeros.simple_proportion_lower` | proved from explicit `hRvM`, `hPC` |
| exact distinct proportion | `ZetaZeros.distinct_proportion_lower` | proved from explicit `hRvM`, `hPC` |
| decimal `0.6725` corollary | `ZetaZeros.simple_proportion_d4` | proved from explicit `hRvM`, `hPC` |
| decimal `0.83625` corollary | `ZetaZeros.distinct_proportion_d5` | proved from explicit `hRvM`, `hPC` |

The first two are the immediate reusable theorem candidates. The last four are
formal conditional theorems whose premises are established in the literature
but not internally discharged here.

## 4. Encoded external inputs

### Riemann-von Mangoldt

The package uses the sufficient asymptotic interface

\[
N(T)\sim \frac{T}{2\pi}\log T.
\]

This deliberately omits lower-order terms. That is mathematically adequate for
the limiting ratio, but an adapter into Riemann's eventual canonical
zero-count source must prove exact normalization agreement.

### Pair correlation

The package encodes a weighted formula for every even, integrable,
support-`[-1,1]` test function satisfying an anchored Lipschitz condition. Its
main term is

\[
f(0)+2\int_0^1\alpha f(\alpha)\,d\alpha,
\]

and the error is bounded by a constant divided by `sqrt(log T)`.

Review must verify:

- ordered versus unordered pairs;
- multiplicities;
- the range `0 < Im rho <= T`;
- the scale `log T/(2 pi)`;
- Fourier sign and `2 pi` convention;
- the rational weight `4/(4-(rho-rho')^2)`;
- real/complex coercions;
- endpoint support convention;
- whether the source lemma supplies exactly the encoded regularity and error.

## 5. Challenge and production separation

`Challenge/Basic.lean` contains intentional `sorry` placeholders. The
production umbrella does not import the challenge module. A search of the
pinned default proof surface found the expected challenge placeholders, not a
production theorem hole.

This still needs an independent local command that rejects `sorry` and
`admit` in every production module rather than relying on filename
conventions.

## 6. CI and comparator

The pinned commit has a successful GitHub Actions run. The workflow file is
minimal:

```text
checkout
leanprover/lean-action
```

The README separately documents

```text
lake env comparator Comparator/comparator.json
```

as a local verification command. The workflow does not explicitly show that
Comparator or Nanoda ran. Therefore the following are separate evidence
classes:

```text
upstream default build success      observed
upstream claim of local Comparator  documented
independent Comparator replay       not performed here
independent Nanoda replay            not performed here
```

## 7. Toolchain boundary

Riemann main pins Lean `v4.33.0-rc2`; ZetaZeros pins `v4.34.0-rc2`. The source
is therefore retained as an isolated submodule and is not added to
`formal/RiemannFormal.lean`.

Two safe options exist:

1. backport the abstract theorem to the Riemann toolchain in an experimental
   module with exact theorem-type comparison; or
2. wait for a reviewed Riemann toolchain upgrade, then import the upstream
   modules unchanged.

A silent toolchain bump solely to consume this package is not acceptable.

## 8. Statement-alignment issues to review

### Finite multiset encoding

The source presents a support `Finset C` and an external multiplicity
function. Review must check that:

- only support members contribute;
- every support member has multiplicity at least one;
- conjugation preserves support and multiplicity;
- `simpleRealPart` means imaginary part exactly zero and multiplicity exactly
  one;
- `Z.card` is the number of distinct support points.

### Zeta-zero reflection

Review the exact bridge

```text
rho -> 1 - conjugate(rho)
```

against the rescaled coordinate and prove:

```text
rescaled point is real  <->  Re rho = 1/2
point multiplicity      =    zero multiplicity
```

with no sign reversal or endpoint loss.

### Count denominators

The final ratio proofs use eventual positivity of `zeroCount T` derived from
Riemann-von Mangoldt. This is sound in architecture, but the threshold
bookkeeping and use of strict inequalities should be replayed.

### Numerical constants

The decimal corollaries prove strict lower bounds `0.6725` and `0.83625`, not
the full decimal expansions. The exact cotangent expressions are the primary
theorems.

## 9. Recommended formal import stages

### Stage F0 - exact replay

Run the upstream build, Comparator, Nanoda, `#print axioms`, and a production
`sorry` scan from the pinned bytes.

### Stage F1 - abstract theorem extraction

Import only the finite conjugation-invariant multiset inequalities into
`formal/Experimental/`. Record the exact source theorem types and exclude all
zeta application claims.

### Stage F2 - source adapters

Prove Riemann-normalized adapters for:

```text
zero multiset and multiplicity
functional-equation reflection
Riemann-von Mangoldt asymptotic
BGST pair correlation
```

### Stage F3 - closed zeta theorem

Only after F2 should Riemann register a theorem with no explicit `hRvM` or
`hPC` parameter.

### Stage F4 - trusted release review

Require independent mathematical and formal reviews, source-lock validation,
Comparator, Nanoda, and a clean axiom audit.

## 10. Current verdict

The formal artifact is unusually substantial and appears well structured. The
abstract Hilbert proposition is the strongest immediate import candidate. The
headline zeta bounds are faithfully exposed as conditional formal theorems,
not falsely installed as axioms. A closed formal proof of the unconditional
analytic theorem still requires formalizing or securely adapting the two
classical analytic inputs.
