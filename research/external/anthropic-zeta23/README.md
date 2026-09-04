# Anthropic Zeta23: external theorem import and repository fusion point

**Status:** `IMPORTED_EXTERNAL_SOURCE / PENDING EXACT-SHA REVIEW`

**Scope:** unconditional asymptotic theorems about proportions of zeta zeros; not a proof of RH.

**Pinned external proof repository:** `anthropics/zeta-23-lean@3635e74826a4c1fcece7d1cd2b6fa75e43a00510`

**Source fingerprints:** see `SOURCE_LOCK.json` in this packet.

## 1. Imported theorem package

For nontrivial zeros `rho=beta+i gamma` of the Riemann zeta function in `(T,2T]`, counted with multiplicity in `N(T,2T)`, the external package claims and formalizes:

```text
liminf N0star(T,2T) / N(T,2T) >= 2/3,
liminf N0simple(T,2T) / N(T,2T) >= 2/3,
liminf Ndist(T,2T) / N(T,2T) >= 5/6.
```

With the optimized Montgomery–Taylor window, the constants become

```text
on-line distinct  >= 0.67250...,
simple and on-line >= 0.67250...,
distinct           >= 0.83625....
```

The same architecture is stated for fixed primitive Dirichlet `L`-functions. The pinned Lean repository also contains later extensions for zeros of `xi'` and a formal bandwidth-one ceiling package.

## 2. The mechanism in one page

Let `W` be Weil's Hermitian form and restrict it to a finite-dimensional Gabor family of compactly supported test functions. In coefficient coordinates this produces a Hermitian matrix `R`.

The zero side splits as

```text
R = P + Q + tail,
```

where:

- each distinct zero on `Re(s)=1/2` contributes a positive rank-one atom to `P`;
- each reflected off-line pair `{rho,1-conj(rho)}` contributes a pulled-back hyperbolic plane of signature `(1,1)` to `Q`;
- a smooth taper makes the contribution from zeros outside the enlarged height window small in operator and trace norm.

The prime side evaluates the first two moments unconditionally at bandwidth `lambda<=1`:

```text
tr(R)       = N + o(N),
||R||_F^2   = (1/lambda + lambda/3) N + o(N)
```

in the normalization where one isolated simple on-line zero has unit atom trace.

The key finite-dimensional inequality is: if `P>=0`, `rank(P)<=r`, and `n_+(Q)<=b`, then for every `c>0`,

```text
||P+Q||_F^2
  >= c tr(P) - c^2 r/4 + 2c tr(Q) - c^2 b.
```

At `c=2`, this is the matrix analogue of `m^2 >= 2m-1`; with simple zeros isolated on the rank side it becomes the analogue of `m^2 >= 3m-2`. At `c=3`, the multiplicity-aware version yields the sharp `5/6` distinct-zero count.

The conceptual novelty is not a new prime-side asymptotic. It is the use of **positive index, rank, and a second trace moment** to read an indefinite zero-side compression without assuming RH.

## 3. What this does and does not settle

It does settle, subject to verification of the external proof package, a much stronger unconditional critical-line proportion than the previous mollifier record.

It does not control the remaining roughly one third of the zeros, prove that any zero is off the line, or prove RH. The two-moment, bandwidth-one mechanism has a structural ceiling close to `0.68183` for configuration-by-configuration simple-zero certificates; crossing that ceiling requires genuinely new information.

## 4. Why it belongs in this repository

This result lands exactly at the interface between two long-running repository programs:

1. **Weil/source normalization.** The paper supplies a clean centered zero coordinate, Fourier convention, compact-support contract, explicit-formula density, taper, Gabor sampling identity, and tail package. These are strong candidates for the repository's missing canonical B0/A0 interfaces.

2. **Kernel/operator synthesis.** The repository's kernel-defect classifier says an off-line cardinal direction survives positive-complement Schur elimination. Zeta23 supplies the complementary finite-compression language: off-line pairs are hyperbolic blocks, and their positive index can be bounded against prime-side moments. The two viewpoints are compatible and should be unified, not run as separate dialects.

## 5. Native extensions in this packet

The accompanying proof notes derive four reusable consequences.

### 5.1 Stable finite-error transfer

A single theorem converts certified finite trace bounds and a certified tail radius directly into finite lower bounds for on-line simple and distinct zeros. This is the bridge from the asymptotic paper to the repository's directed-computation culture.

### 5.2 Multiplicity-profile frontier

The full parameter-`c` rank–trace inequality yields a generating inequality for every multiplicity profile. Two exact refinements are extracted:

```text
S1 >= C2 - 2N + P2,
D  >= (C3 - 3N + P3)/2,
```

where `P2,P3` are explicit nonnegative penalties for high multiplicities and off-line pairs. The headline `2/3` and `5/6` bounds are the zero-penalty projections of a sharper joint frontier.

### 5.3 Block-direct-sum no-gain theorem

Taking several scalar-window certificates in block diagonal direct sum can only average their individual lower bounds. It cannot beat the best constituent window. Any genuine improvement from multiple windows must use cross-window matrix entries, additional moments, or additional arithmetic support.

### 5.4 Conditional support-extension optimizer

Under an explicit trace-extension hypothesis beyond bandwidth one, the optimal scalar window solves a Fredholm equation with saturated kernel

```text
K_lambda(s,t)=min(lambda |s-t|,1).
```

For `lambda<=1` this reduces to the paper's cosine. For `lambda>1` it becomes a delay equation. The supplied Nyström solver reproduces the `0.70`, `0.80`, and `0.90` support targets at approximately

```text
lambda = 1.0426, 1.2578, 1.7014.
```

Those numbers identify the exact arithmetic-support milestones a next theorem must cross.

## 6. Honest next frontier

The highest-value route is not to re-optimize another isolated scalar window at support one. That optimization is solved and block-diagonal ensembles provably add nothing.

The next fronts are:

- a **cross-window/matrix-valued compression** whose mixed moments use more than the scalar autocorrelation;
- a rigorously extended prime-side second moment beyond support one;
- a third or fourth spectral moment with a count functional that survives the off-line hyperbolic structure;
- a fusion with the repository's complete-kernel hierarchy, using Zeta23 moment bounds to constrain the dimension and inertia of the unresolved corrected kernel.

All four are harder than changing the taper, but unlike taper-only work they can cross the demonstrated ceiling.
