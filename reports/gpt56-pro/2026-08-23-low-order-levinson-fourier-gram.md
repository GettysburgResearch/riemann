# Low-order Levinson continuation: endpoint telescope and Fourier-compound positivity

Date: 2026-08-23  
Branch: `research/gpt56-pro/105200-xi-natural-scale-residue-coherence`  
Scientific status: **RH unproved**

## Binding correction

The cumulative quantity formerly named `CRDB105200` is not an independent
low-order producer.  The exact complex reverse-Rolle identity gives

\[
\mathcal D_r
=O_0+2\sum_{j<r}
\left[R_j(1-\mathfrak C_j)-E_j\right].
\]

It is the unknown off-real zero count plus nonnegative slack.  The natural
high-derivative theorem removes the terminal `O_r`; it does not estimate the
fixed low-order boundary argument.  This correction is frozen as `R-105201`.

## One boundary quotient

For one fixed companion parameter across a derivative ladder,

\[
G_{k,\lambda}
=\xi^{(k)}+\lambda\xi^{(k+1)},
\]

all horizontal argument changes telescope:

\[
\sum_{k<r}
\Delta\arg {G_{k,\lambda}\over G_{k+1,\lambda}}
=
\Delta\arg {G_{0,\lambda}\over G_{r,\lambda}}.
\]

The top-boundary logarithmic derivatives telescope identically.  Thus the
actual Levinson boundary is one endpoint quotient.  At the natural terminal
parameter `lambda_r=M_r/M_(r+1)`, the high denominator is asymptotically an
explicit Gaussian exponential on bounded parts of the safe path.  The
numerator is the classical low-order function `xi+lambda_r xi'`.

## All-order low-derivative Fourier Gram

Let

\[
\Lambda_m(t)
=\Xi^{(m+1)}(t)^2
 -\Xi^{(m)}(t)\Xi^{(m+2)}(t).
\]

Using the positive two-sided Xi Fourier kernel, `L-105207` constructs exterior
vectors `omega_(a,t)` with

\[
\langle\omega_{a,t},\omega_{b,s}\rangle
=\Lambda_{a+b}(s-t).
\]

Therefore

\[
[\Lambda_{a_i+a_j}(t_j-t_i)]\succeq0
\]

for arbitrary derivative indices and translations.  Consequences include:

- every even `Lambda_(2a)` is a positive-definite function;
- every autocorrelation-windowed derivative Hankel matrix is PSD;
- odd Fourier defects satisfy the Schur bound
  \[
  |\widehat\Lambda_{2a+1}|^2
  \le\widehat\Lambda_{2a}\widehat\Lambda_{2a+2};
  \]
- every even derivative has an explicit central interval with no wrong
  extrema.

This is unconditional at every fixed low order.  It is a compound Fourier
positivity theorem, not a high-derivative asymptotic.

## Mean Hermite--Biehler orientation

For

\[
E_{k,\lambda}
=\Xi^{(k)}-i\lambda\Xi^{(k+1)},
\]

`L-105208` proves on every lower horizontal line

\[
\|E_{k,\lambda}\|_2^2
-
\|E_{k,\lambda}^{\#}\|_2^2
>0.
\]

It also proves the exact phase sum rule

\[
\int_{\mathbb R}|E_{k,\lambda}|^2\theta_{k,\lambda}'
=2\lambda\int_{\mathbb R}|\Xi^{(k+1)}|^2>0.
\]

Thus clockwise Levinson phase is always overpaid by counterclockwise
amplitude-weighted phase in the global source ledger.

## Remaining theorem

The unresolved step is no longer described as a high-tail coherence budget.
It is `HLOC105210`:

```text
convert the exact translation-invariant / line-averaged Fourier-compound
positivity into a fixed-height bound on the continued argument of the single
endpoint Levinson quotient at the last defective level.
```

A small set of ordinates can still carry the entire inward index, so the
average identities do not prove this localization.

## Exact replay

```text
PASS_X_105210_LOW_ORDER_LEVINSON_GRAM
```

The finite replay performs 233 exact Gaussian-rational checks of the quotient
telescope, CRDB correction, exterior-square Gram, Schur inequalities, mean
orientation, and phase zero mode.  It records `HLOC105210` and RH as unproved.
