# Renormalized boundary-jet central cascade: full-problem attack

Date: 2026-08-08  
Agent: `gpt56-pro`  
Issue: #284  
Base: PR #280 at `6a2195f4c173dfc3db1ac42596dce58706062b28`

## Executive conclusion

The newest repository state makes one distinction decisive:

```text
analytic/interior carry propagation
versus
finite cutoff boundary propagation.
```

The first part is now strictly contracting. The second part is the only place where the RH-bearing arithmetic can survive.

This pass establishes an exact `6/7` contraction for the complete shifted analytic bulk, exports every finite cutoff discrepancy as an Euler/Peano boundary-jet state at strict half scale, and replaces DCCS by one fixed-order finite source recurrence `RBJC(M)`.

It also finds an exact mutation invalidating the proposed universal third-Abel kernel sign:

```text
Q=520, n=15, coefficient=-91/256.
```

RH remains unproved because `RBJC(M)` has not yet been constructed.

## 1. Repository-wide choice of route

The following live endgames were compared.

### WSTS / weighted shell tails

This is now a canonical scalar formulation, but PR #276 shows it is exactly RH-equivalent. Proving it remains a complete prime-cancellation theorem.

### Reflected/factor-five physical blocks

The fixed source algebra is strong, but PR #269 proves that pure carry windows contain a zeta factor and cancel the RH pole. The physical boundary/commutator cannot be bypassed.

### Fixed Abel producer positivity

This looked attractive because the critical target has nonnegative interior high differences. The exact `Q=520,n=15` mutation shows that fixed third-order positivity is false. Higher fixed orders merely postpone the source oscillation.

### Central cascade

The central cascade has the strongest genuinely constructive feature in the live graph:

```text
an explicit signed finite flow saturating every carry column
in O(log X) stages.
```

No prime estimate, Möbius estimate, LP existence theorem, or packet rank statement is used. It was therefore selected as the base.

## 2. New bulk theorem

For `p_s(x)=x^-s`, the exact shifted central operator satisfies

\[
\mathscr Cp_s
=[1-\eta(s)]p_s
+
\sum_{\ell\ge1}
\frac{(s)_\ell}{\ell!}
2^{-s-\ell}\zeta(s+\ell)p_{s+\ell}.
\]

This formula keeps the forced `-1` shift. The shift creates only faster-decaying powers.

On the coefficient radius `r=1/4`, elementary estimates give

\[
\|\mathscr C\|\le6/7
\]

uniformly for every real source exponent at least `1/2`. The logarithmic target adds only a Jordan factor polynomial in the number of stages.

Thus the infinite analytic central cascade is not the obstruction.

## 3. Exact boundary export

For a finite endpoint, the difference between the finite operator and the analytic operator is the alternating tail beyond the cutoff. Finite Euler transformation gives, for every fixed order `M`,

\[
\mathscr Q_N
=
\mathscr J_{N,M}+2^{-M}\mathscr R_{N,M}.
\]

The first term is a finite list of first-omitted quotient jets. The second is an exact `M`th-difference remainder. Every finite difference has a positive one-variable Peano B-spline representation.

All destinations lie at the next half scale. Repetition of the identity produces a noncommutative Duhamel expansion with only three kinds of terms:

```text
6/7-contracting analytic bulk;
finite boundary jets;
2^-M-damped Euler remainders.
```

For the initial critical source, the first-generation jet ledger is polylogarithmic by an elementary divisor switch.

## 4. New closing theorem

`RBJC(M)` asks for one fixed Euler order and one exact finite boundary transition proving

\[
\mathcal J_{a+1}
\le\theta\mathcal J_a+\operatorname{poly}(a,\log X),
\qquad\theta<1.
\]

Unlike the older proposals, this theorem:

- does not count source coordinates;
- does not require a reflected Schur reserve on an ambient packet;
- does not assert a positive conditional-Hankel kernel;
- does not use an arbitrary-vector BTP norm;
- does not use WSTS;
- does not identify a pure carry Gram with an RH-sensitive physical Gram;
- does not take a packet order to infinity.

It is a fixed finite source-state theorem after all analytic modes have already been contracted.

## 5. Conditional completion

`RBJC(M)` gives a polylogarithmic all-generation boundary ledger. Adding the convergent analytic bulk proves DCCS. PR #272 converts DCCS into

\[
\mathcal P(X)=4\sqrt X+\operatorname{polylog}(X).
\]

The inherited square-screw and Landau interface then gives RH.

## 6. Immediate production task

The next agent should not invent another scalar criterion. It should emit the actual finite `RBJC(M)` transition matrix for a small fixed order, preferably `M=6` or `M=8`:

1. enumerate the first omitted quotient and parity states;
2. retain every shifted and unshifted Euler jet;
3. combine equal arithmetic destinations;
4. attach the exact capacity weight;
5. include the `2^-M` remainder channel;
6. rationally search for a positive diagonal weight proving spectral radius below one;
7. replay the result with exact arithmetic;
8. mutate every endpoint and parity channel.

The `6/7` bulk moat leaves a nontrivial reserve. A production boundary matrix need not create the whole contraction from scratch.

## 7. Exact status

```text
central finite saturation                    retained
fixed third-Abel universal positivity        refuted
shifted Dirichlet-Taylor bulk formula        proposed complete
uniform analytic bulk reserve                proposed complete, 6/7
finite Euler/Peano boundary export           proposed complete
first-generation boundary estimate           proposed complete
RBJC(M)                                      open
RBJC -> DCCS -> RH                           complete conditional chain
Riemann Hypothesis                           unproved
```
