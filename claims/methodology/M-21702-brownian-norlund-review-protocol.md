# M-21702 — Fail-closed review protocol for the Brownian Nörlund route

Claim ID: `M-21702`  
Status: **METHODOLOGY / REVIEW CONTRACT**  
Scope: `L-21705`, `L-21706`, `T-21704`, and any proposed BLNRZ completion

## 1. Review objective

The route is accepted as an unconditional RH proof only after both statements below are independently established.

1. The explicit finite functions `mathcal X_N` converge locally uniformly to `4 xi` in the open critical strip.
2. An unbounded sequence of these exact finite functions has no off-line strip zeros.

The first item is the elementary estimate in `L-21705/L-21706`. The second is BLNRZ and is presently open.

## 2. Frozen finite object

A review must use exactly

\[
\overline m_N(s)=H_N^{-1}\sum_{K=1}^NK^{-1}m_K(s),
\qquad
\mathcal X_N(s)=\overline m_N(s)+\overline m_N(1-s),
\]

with the `Gamma(2)` rates

\[
1^2,1^2,2^2,2^2,\ldots,N^2,N^2.
\]

Changing the averaging, rate multiplicity, symmetrization, or normalization creates a different proposal and requires a new claim ID.

## 3. Exact algebra checks

Reviewers should reconstruct independently:

1. `B_(N,n)` from the double-pole residue;
2. `A_(N,n)` by differentiating the remaining product;
3. the `3/(2n)` endpoint in the harmonic collapse;
4. the Mellin formula and `N=1` control;
5. the repeated-knot divided-difference identity;
6. the critical-strip error `|m_N-2xi|<=|s|/N`;
7. the Nörlund error `zeta(2)|s|/H_N`;
8. the Rouché/Hurwitz completion.

`X-21703/verify.py` is a replay aid, not a substitute for these derivations.

## 4. BLNRZ production requirements

A valid BLNRZ artifact must emit one of the following complete objects.

### Hermite–Biehler route

```text
explicit E_N;
exact identity X_N(1/2+iz)=E_N+E_N#;
zero-free half-plane ledger;
mean-type/exponential-factor normalization;
strict modulus inequality in the full upper half-plane or licensed strip.
```

### Integral-of-squares route

```text
exact product identity for |X_N(x+iy)|^2;
positive measure/kernel;
all boundary terms;
strict positivity when x!=1/2.
```

### Canonical-system route

```text
finite Hamiltonian or self-adjoint matrix;
positive Hamiltonian proof;
characteristic determinant equal to X_N;
endpoint normalization and multiplicity ledger.
```

### Spline/total-positivity route

```text
complete repeated-knot Dirichlet spline;
proof that logarithmic mixing preserves the required sign-regular class;
transform theorem with hypotheses checked at repeated knots and atoms.
```

## 5. Automatic rejection

Reject a completion upon any of the following.

1. It proves only finitely many contour counts.
2. It invokes zeros of `xi` or RH in the finite theorem.
3. It proves a statement also covering the raw truncations without addressing `O-21705`.
4. It replaces logarithmic averaging by a generic convex combination.
5. It invokes log-concavity, GGC, infinite divisibility, or `TP_2` where `TP_infinity`/Hermite–Biehler is required.
6. It claims a de Branges function without proving the half-plane modulus and mean type.
7. It applies a Pólya shift theorem without proving the complete zero strip of the base function.
8. It embeds into Eisenstein integrals only by analogy rather than equality.
9. It uses local Jensen-polynomial hyperbolicity as a global zero theorem.
10. It interchanges `N -> infinity` with a zero statement before proving compact uniform convergence.

## 6. Required mutations

Every future checker/reviewer should include:

```text
raw N=75 off-line count;
wrong 3/(2n) harmonic endpoint;
Gamma(shape 1) substituted for shape 2;
Cesaro weights substituted for 1/K;
random phase-type rates;
reflection term or gamma ratio omitted;
contour touching the critical line;
finite-height result advertised as cofinal.
```

## 7. Status vocabulary

```text
EXACT             finite symbolic identity proved;
DIRECTED          certified numerical interval statement;
RECONNAISSANCE    floating/high-precision discovery only;
OPEN              theorem not established;
REFUTED           exact hypothesis-matching contradiction.
```

At the present head, BLNRZ and RH are `OPEN`.
