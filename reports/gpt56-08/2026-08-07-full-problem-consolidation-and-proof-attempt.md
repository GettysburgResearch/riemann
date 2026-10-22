# Full-problem consolidation and proof attempt — 2026-08-07

## Verdict first

I did **not** obtain a valid unconditional proof of the Riemann Hypothesis.

I did obtain:

1. an exact new Volterra--virial identity connecting the classical total and
   arithmetic totient mean squares to the analytic RH energy;
2. an exact finite verifier for that identity;
3. one unified conditional proof spine consuming the strongest global routes in
   the repository;
4. an independent diagnosis that every route stops at the same signed critical
   correlation;
5. a scope refutation of the three most tempting false closures.

Presenting the resulting conditional spine as a full proof would require
silently assuming the very estimate that excludes off-line zeros. I have not
done that.

## 1. Repository-wide consolidation

The major global programmes can be arranged around one rightmost-zero exponent.

### Analytic-totient energy

`L-9512/T-9504/T-9506` identify

\[
E^{\rm AN}(x)
={1\over2}\left(1+\sum_d\mu(d)\{x/d\}^2\right)
\]

and prove the transfer

\[
\mathrm{RH}
\iff
\int_X^{2X}|E^{\rm AN}(x)|^2dx
\ll_\varepsilon X^{2+\varepsilon}.
\]

The best mean-square exponent is exactly twice the horizontal displacement of
the rightmost zero.

### Square-screw and logarithmic Riesz routes

PR #202 compresses the same exponent into a complete finite prime-power scalar
at square cutoffs. Its transfer theorem is complete, while the eventual
one-sided/subpolynomial arithmetic estimate is open.

### Terminal-prime and pole-free windows

PR #165 and its descendants isolate pole-free terminal-prime statistics and
bounded-mean-square criteria. Exact endpoint cancellation is available. The
cofinal signed terminal-prime estimate remains open.

### Prime-only Hardy and Selberg routes

PRs #216/#222/#224 turn the complete off-diagonal prime energy into a balanced
squarefree-semiprime Type-II form and derive the exact centered Selberg Riccati
equation. Diagonal and forcing identities are closed; the balanced signed
Type-II estimate is open.

### Dyadic transport

PR #218 converts the same obstruction into a curvature-normalized one-sided
prime-transport reserve. Exact knot reduction and finite identities are closed;
the transport-versus-dispersion inequality is open.

### Localized Weil/operator route

The cardinal, radical, Schur, complete-frame, source-conditioning, and soft-block
work identifies how an off-line zero escapes every fixed packet. It supplies
valid finite and conditional algebra but no independent sign theorem for the
complete escaping mode.

## 2. New exact virial bridge

Let

\[
E_\varphi(x)=\sum_{n\le x}\varphi(n)-{3\over\pi^2}x^2,
\]

\[
f(x)=-\sum_d{\mu(d)\over d}\{x/d\},
\]

and `A=E^AN`. The classical decomposition is

\[
E_\varphi=xf+A.
\]

The new observation is that

\[
A'=-f
\]

almost everywhere, so

\[
E_\varphi=A-xA'.
\]

Therefore

\[
\boxed{
2\int_a^bA(x)^2dx
=
\int_a^bE_\varphi(x)^2dx
-
\int_a^bx^2f(x)^2dx
+
[xA(x)^2]_a^b.}
\]

This is exact and unconditional.

It says that the RH-bearing analytic square mean is precisely the joint
remainder after the total and arithmetic cubic mean squares cancel, with the
endpoint energy flux retained.

This connection was not explicit in the prior repository spine. It provides a
direct adapter between the Kaczorowski--Wiertelak totient decomposition and the
new Farey/Type-II/transport programmes.

## 3. Exact replay

`X-9514` verifies the virial identity on every integer endpoint `2<=N<=64` over

```text
Q[C], C=1/zeta(2)=6/pi^2.
```

The retained verdict is

```text
PASS_EXACT_L9514_VOLTERRA_VIRIAL_IDENTITY
```

with proof-object SHA-256

```text
8c6a2dfa0425ff479c096519091babe922927bbd0637957d76e69e32422b58f5
```

This is a finite algebra check only.

## 4. Why the classical mean-square theorem does not already close RH

The summatory-totient error has a cubic mean-square asymptotic, and under GRH
its published remainder can be sharpened. These are separate estimates for the
total error.

The virial identity requires the correlated difference between the total and
arithmetic mean squares down to scale `X^(2+epsilon)`. Independent remainders of
size

```text
X^3 exp(-c sqrt(log X))
```

or even `X^(3-delta)` with `delta<1` are too large. Equality of the leading cubic
constants does not control their difference at the RH scale.

The arithmetic Fourier packet contains a divisor weight `1/d`; the analytic
Volterra primitive removes it. This is the exact one-power loss that prevents a
direct transplant of the arithmetic dispersion estimate.

## 5. Exact common obstruction

After extracting exact resonances, the analytic local square contains

\[
\sum_{d,e\asymp D}\mu(d)\mu(e)
\sum_{h,k\ne0}c_h\overline{c_k}
\int_D^{2D}e^{2\pi i(h/d-k/e)x}dx.
\]

- full-period resonances have the positive Jordan-square factorization of
  `L-9513` and size `O(D)`;
- separated frequencies are controlled by standard large-sieve/integration
  estimates;
- the unresolved region consists of frequencies separated by at most `1/D`;
- denominators of size `D` have Farey spacing `D^-2`;
- a phase-blind estimate loses one full power;
- the Möbius common-cell cancellation is load-bearing.

PR #229 independently arrived at the same common gate and identified its prime,
transport, and totient formulations.

## 6. Closure attempts made in this pass

### Separate cubic asymptotics

Rejected by `R-9504`: the remainders and endpoint flux must be combined before
absolute values.

### Full-period Bohr transfer

Rejected: the common period is exponentially larger than the physical interval,
and near frequencies can remain coherent on a critical interval.

### Generic Farey large sieve

Insufficient by one power because the minimum spacing is `D^-2` while the
interval length is only `D`.

### Modern Kloosterman-fraction bounds

They give partial savings for broad coefficient classes, not the complete
Möbius-specific square-root cancellation required here. A recent claimed
improvement also carries a published correction noting that its advertised
improvement does not follow.

### Möbius short-interval uniformity

Current almost-all short-interval results give qualitative or logarithmic
cancellation, not the square-root local moment whose Mellin consequence would
already be RH.

### Prime-by-prime contraction

Closed earlier by `R-9503`: the critical prime filter has norm
`1+p^(-1/2)>1` on every ordinary translation-invariant energy.

### Positive Selberg exponential adjoint

The real exponential adjoint identity is exact and useful, but produces
`H(s)^2`. The required vertical energy is `|H(s)|^2`, so a reflected/two-sided
correlation theorem is still necessary.

### Finite operator positivity

Finite ladders and corrected Schur blocks do not control the weakly escaping
cardinal mode. The same mode is the critical Farey/Type-II correlation in the
present coordinates.

## 7. Complete conditional proof spine

`T-9507` records the proof:

1. prove the signed critical correlation at `D^(2+epsilon)`;
2. combine it with exact resonances and far-frequency estimates;
3. obtain the analytic-totient second moment;
4. use Mellin Cauchy--Schwarz to continue
   \[
   -{\zeta(s-1)\over s(s-1)\zeta(s)}+{3/\pi^2\over s-2}
   \]
   through `Re s>1/2`;
5. an off-line zero would be a genuine pole;
6. exclude right-side zeros and use functional-equation symmetry;
7. conclude RH.

Equivalent completions are the prime Type-II recurrence or the oriented dyadic
transport inequality.

## 8. Exact theorem still missing

The strongest direct statement is

\[
\boxed{
\sum_{d,e\asymp D}\mu(d)\mu(e)
\sum_{h,k\ne0}c_h\overline{c_k}
\mathcal J_D(h/d-k/e)
\ll_\varepsilon D^{2+\varepsilon},}
\]

with exact resonances removed and all tails included.

It is equivalent, through the existing dictionaries, to the doubly centered
balanced prime Type-II recurrence and to the curvature-corrected dyadic
transport reserve.

No valid proof of this estimate was found in the repository or in the primary
literature checked during this pass.

## SERIOUS RESOLUTION PATH

**Present:** yes. The transfer architecture is complete and the missing
arithmetic theorem is singular, explicit, and shared by the main global routes.

**Full proposed proof:** no. A proof document that replaces the boxed critical
correlation by an assertion would only rename RH. It would not be suitable for
review as a claimed resolution.

## Files added in this pass

```text
claims/lemmas/L-9514-volterra-virial-totient-energy.md
claims/refutations/R-9504-separate-cubic-means-do-not-prove-critical-energy.md
claims/theorems/T-9507-unified-critical-correlation-proof-spine.md
claims/methodology/M-9504-full-problem-critical-correlation-program.md
claims/experiments/X-9514-exact-volterra-virial-regression.md
experiments/X-9514-volterra-virial/
reports/gpt56-08/2026-08-07-full-problem-consolidation-and-proof-attempt.md
```
