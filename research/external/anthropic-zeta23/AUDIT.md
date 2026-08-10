# Audit of the Anthropic Zeta23 package

**Verdict of this pass:** `HIGHLY CREDIBLE EXTERNAL THEOREM PACKAGE; NO FATAL JOINT FOUND; INDEPENDENT LEAN REPLAY STILL PENDING HERE`.

This is not a referee report and does not replace expert publication review. It records what was inspected, what appears load-bearing, what survived, and what was not independently replayed.

## 1. Sources inspected

- the 35-page paper dated 2026-08-10;
- the 5-page condensed proof note;
- Anthropic's official research page;
- `anthropics/zeta-23-lean` at commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`;
- the external repository's `README.md`, `AUDIT.md`, statement layer, and multiplicity-aware final theorem layer;
- the cited predecessor papers isolating the unconditional pair-correlation input and the narrow-box obstruction.

## 2. Statement audit

The paper distinguishes correctly among:

- `N`: zeros counted with multiplicity;
- `N0star`: distinct points on the line;
- `N0simple`: simple points on the line;
- `Ndist`: distinct zeros in the full strip.

The pinned Lean statement layer defines these directly from Mathlib's `riemannZeta` and `analyticOrderAt`. The top-level multiplicity-aware theorems in `Zeta23/FinalMult.lean` state the `2/3` simple-on-line and `5/6` distinct bounds with no user hypotheses. This materially reduces the risk of a formalization that proves only an abstract or weakened surrogate.

## 3. Zero-side audit

### 3.1 Hermitian symmetry

With `gamma_rho=(rho-1/2)/i`, the functional equation sends `rho` to `1-conj(rho)` and hence `gamma_rho` to `conj(gamma_rho)`. Pairing these terms makes the compression Hermitian.

### 3.2 On-line atoms

For `gamma_rho` real, the evaluation vector is real in the chosen even-window coordinates and contributes a positive rank-one form. No orthogonality or independence of evaluation vectors is required; only a rank upper bound and an atom trace bound are used.

### 3.3 Off-line pairs

A reflected pair contributes a pullback of the two-dimensional form

```text
(x,y) -> 2m Re(x conj(y)),
```

whose matrix has signature `(1,1)`. Pullback cannot increase positive index. This remains valid if evaluation vectors coincide, nearly coincide, or are badly conditioned.

### 3.4 Non-orthonormal coordinates

The proof intentionally does not orthonormalize the Gabor family. This is not a defect. Inertia is coordinate invariant, while trace and Frobenius norm are evaluated for the actual coefficient-coordinate matrix and the atom trace bound is proved in the same normalization by the Poisson identity. The proof never substitutes an orthonormal-basis trace for a coefficient-basis trace.

### 3.5 Tail localization

A compactly supported `C^2` taper gives quadratic decay of the entire Fourier transform uniformly in the zero depth `|beta-1/2|<1/2`. Summing rank-one tail norms against the local zero-count bound makes the far-zero perturbation `o(1)` at every fixed `lambda<=1`. The sharp cutoff would fail here; the paper explicitly identifies and repairs that failure.

**Zero-side conclusion:** no missing positivity, independence, or orthonormality assumption was found.

## 4. Linear-algebra audit

For `P>=0`, write `Q=Q_+-Q_-`. Von Neumann's trace inequality controls the adverse interaction `tr(PQ_-)`. Completing squares in the eigenvalues gives

```text
||P+Q||_F^2
 >= c tr(P) - c^2 rank(P)/4 + 2c tr(Q) - c^2 n_+(Q).
```

Equality occurs on orthogonal projection configurations of the stated sizes and eigenvalues, so the inequality has the correct scale and sharpness.

The multiplicity-aware charge

```text
k_c(m)=c^2-(c-m)_+^2
```

matches the scalar envelope `2cm-m^2` for `m<=c` and the flat charge `c^2` for `m>=c`. The paper's `c=2` and the Lean route's `c=3` recover the advertised constants.

The local stress suite in this packet checks equality configurations, random unitarily mixed examples, nearly cancelling large eigenvalues, rank-deficient atoms, and random `c` values. It is evidence against sign or coefficient mistakes, not a proof substitute.

## 5. Prime-side audit

The first trace is the expected mean density plus a lower-order prime oscillation. The second trace splits into:

- the archimedean `mu*mu` main term;
- the diagonal prime-power term;
- Montgomery–Vaughan-controlled off-diagonal prime powers;
- lower-order cross and pole terms;
- finite-grid end effects.

At `X=(T/2pi)^lambda`, `lambda<=1`, the off-diagonal bound remains smaller than the `T L^3` main term, including at the endpoint `lambda=1` by logarithmic saving. The raw main term is

```text
lambda + lambda^3/3,
```

and after normalization the Frobenius constant is

```text
kappa(lambda)=1/lambda+lambda/3.
```

This is exactly the unconditional bandwidth-one Montgomery input isolated in the predecessor literature. The paper does not silently discard complex zero terms or assume termwise positivity on the zero side.

**Prime-side conclusion:** no hidden RH input was found in the moment evaluation as stated for `lambda<=1`.

## 6. Assembly audit

With `tr(R)=N+o(N)` and `||R||_F^2=kappa N+o(N)`:

```text
N0simple >= 4 tr(R)-||R||_F^2-2N-o(N)
          = (2-kappa)N-o(N),
```

and at `lambda=1`, `kappa=4/3`, giving `2/3`.

The multiplicity-aware `c=3` certificate gives

```text
Ndist >= [6 tr(R)-||R||_F^2-3N]/2-o(N)
       = [(3-kappa)/2]N-o(N),
```

hence `5/6` at `lambda=1`.

The optimized profile solves the Euler equation for

```text
lambda (int v)^2 /
[int v^2 + lambda^2 int int |s-t| v(s)v(t)],
```

so `v(s)=cos(sqrt(2) lambda s)`. The constant at `lambda=1` reproduces `0.67250...`.

## 7. Formalization audit

The external audit records:

- a successful build of the library and comparator solutions;
- no `sorry` under `Zeta23/` or the solution modules;
- no project-specific axiom declarations;
- only Lean's standard `propext`, `Classical.choice`, and `Quot.sound` in headline axiom reports;
- successful comparator checks, including an independent kernel mode.

This pass inspected the source and audit record but did **not** independently rebuild the 9,000-job dependency closure. Therefore this packet records the Lean status as **externally reported and source-inspected**, not independently replayed here.

## 8. Residual review targets

The joints most worth a cold expert recheck are:

1. the exact spectral explicit-formula normalization, especially the pole-density rewrite;
2. the finite-grid end-effect estimate in the second trace;
3. the bilinear Montgomery–Vaughan reduction of the off-diagonal prime-power term;
4. the endpoint `lambda=1` error bookkeeping;
5. the seam from Mathlib's analytic zero order and functional equation to the abstract zero configuration;
6. the Dirichlet `L`-function extension, especially character conjugation and uniformity claims;
7. the later `xi'` package, whose technical supplement is not present as a standalone human-readable source in the pinned repository.

## 9. Bottom line

The result is far beyond a plausible-looking informal calculation. Its central mechanism is simple enough to audit, the main constants cohere across paper, note, code, and Lean statements, the known obstruction in prior work is addressed at the correct joint, and no fatal issue emerged in this pass.

The proper status is therefore neither blind acceptance nor routine skepticism. It is a very strong theorem package that deserves immediate independent analytic-number-theory and formal-proof replay.
