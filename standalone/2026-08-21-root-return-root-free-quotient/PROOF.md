# A scalar Schur quotient for root-return and root-free packing

## Abstract

We isolate a general conditional implication used by the live Riemann proof
program.  A positive quadratic form that contains the critical detector as a
root term is insufficient when only its excess is controlled.  We prove that a
strict source-owned return of the root, even with a subpower shrinking moat,
combines with a root-free packing estimate to give subpower one-sided negative
mass for the fixed detector.  We also give exact finite countermodels to the
principal invalid promotions.  The two terminal arithmetic estimates are not
proved, and the Riemann Hypothesis remains unproved.

## 1. Setup

Let `G` be one fixed real-valued conclusion-facing detector.  On the dyadic
block `B_L=[2^L,2^(L+1)]`, suppose an exact positive form has been opened as

```text
Q_L=|G|^2+E_L,
E_L>=0.
```

The word *fixed* is essential: the Mellin consumer must see one observable,
not an endpoint-dependent family of completed observables.

## 2. Root return

Assume there are `0<=theta_L<1` and `R_L>=0` such that

```text
|G|^2<=theta_L Q_L+R_L.
```

The remainder must arise from source data chosen before the sign of `G` is
observed.  This prevents the tautological circular choice `R_L=|G|^2`.

## 3. Exact absorption

Substitute the positive-square identity:

```text
|G|^2<=theta_L|G|^2+theta_LE_L+R_L.
```

With `delta_L=1-theta_L`,

```text
delta_L|G|^2<=theta_LE_L+R_L<=E_L+R_L.
```

Hence

```text
G_-<=|G|
   <=delta_L^(-1/2)[sqrt(E_L)+sqrt(R_L)].
```

This is the scalar Schur complement.  It is also the one-dimensional case of
the nonnegative Perron absorption in PR #697.

## 4. Packing and negative mass

Assume

```text
delta_L^(-1)=2^o(L)
```

and

```text
integral_(B_L)[sqrt(E_L)+sqrt(R_L)]dX/X=2^o(L).
```

Integrating the pointwise bound gives

```text
integral_(B_L)G_-dX/X=2^o(L).
```

Dyadic summation preserves the subpower exponent.  When `G` is instantiated as
the fixed zero-safe detector inherited from PR #697/#704, the frozen
Mellin--Landau consumer implies RH.

## 5. Why the inputs are separate

The signed measure

```text
nu=(2/5)delta_2-delta_1
```

has negative critical first moment and positive moments of every order at least
two.  Thus a complete supercritical positivity hierarchy does not supply root
return.

The positive-definite matrix

```text
[[1,3/4],[3/4,1]]
```

has a negative signed linear witness.  Thus PSD geometry does not supply root
return either.

Finally, `Q=x^2+e^2` with `e=0` shows that perfect excess control does not bound
the root.  The return inequality and root-free packing are genuinely distinct
typed obligations.

## 6. Scientific status

The algebraic implication is proved.  Neither `SORR104100` nor `RFCP104100` is
proved.  Consequently this document does not prove the Riemann Hypothesis.
