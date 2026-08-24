# L-105628 — The infinite-line base-Xi phase collision contracts down to the Xi-prime extremal height

Claim ID: `L-105628`  
Status: **PROVED UNCONDITIONAL ONE-RUNG SOURCE-ENERGY DESCENT; PHASE DESCENT BELOW BETA_1 OPEN**  
Created: 2026-08-25  
Depends on: `L-105620--L-105627`  
RH status: **not assumed**

## 1. Literal source scope and the two height parameters

This theorem is stated at the base Xi rung, where the Fourier source is the
literal positive even kernel `Phi`. Put

\[
\beta_j=\sup\{\Im z:\Xi^{(j)}(z)=0\},
\qquad
\beta_1\le\beta_0.
\]

Fix a base and microscope scale

\[
\boxed{b\ge\beta_1,\qquad h>0,\qquad H=b+h.}
\tag{L-105628.1}
\]

The total analytic height is `H`, whereas the differential microscope carries
the separate coefficient `h`.

Define

\[
\boxed{
r_{b,h}(\xi)
={h e^{-H\xi}\Lambda_2(\xi)\over j_H(\xi)},
\qquad \xi\ge0.
}
\tag{L-105628.2}
\]

This is the actual current-normalized first exterior-square chaos in the
microscope at base `b` and scale `h`.

Let

\[
\boxed{
U_H(x)
={D_H^{\#}(x)\over D_H(x)},
\qquad
D_H(z)=\Xi'(z+iH),
}
\tag{L-105628.3}
\]

with real common factors cancelled, and let `V_H` be its Paley--Wiener operator
on `L^2(0,infinity)`.

The restriction to the base Xi rung is load bearing. Odd Xi derivatives do not
have the same nonnegative even full-line Fourier source.

## 2. Both hypotheses are paid down to beta_1

Put

\[
R_H(\xi)
={H e^{-H\xi}\Lambda_2(\xi)\over j_H(\xi)}.
\]

`L-105626` proves that the standard Xi Fourier kernel is strictly
log-concave, and `L-105624` therefore gives

\[
R_H\text{ nonincreasing on }[0,\infty).
\]

Since

\[
\boxed{r_{b,h}={h\over H}R_H,}
\tag{L-105628.4}
\]

the actual microscope profile `r_(b,h)` is also nonincreasing.

Because `H=b+h>beta_1`, `L-105627` proves that `U_H` is inner. Hence `V_H` is
a causal isometry. Applying `L-105625` gives

\[
\boxed{
V_H^*M_{r_{b,h}}V_H
\preceq
M_{r_{b,h}}.
}
\tag{L-105628.5}
\]

Thus the actual Xi-prime all-pass cannot amplify the canonical
current-normalized base-Xi Turan source for **every base `b>=beta_1`**. The
source-weighted phase control descends one full derivative rung below the
parent extremal height `beta_0` whenever `beta_1<beta_0`.

No zero-freeness of the Xi numerator above `b` is used. The only innerness
threshold is the zero height of the denominator `Xi'`.

## 3. Exact energy form

For every source vector `f in L^2(0,infinity)`,

\[
\boxed{
\int_0^\infty
r_{b,h}(\xi)|(V_Hf)(\xi)|^2d\xi
\le
\int_0^\infty r_{b,h}(\xi)|f(\xi)|^2d\xi.
}
\tag{L-105628.6}
\]

The exact reserve is the delayed prefix energy

\[
\boxed{
\begin{aligned}
&\int r_{b,h}|f|^2-
 \int r_{b,h}|V_Hf|^2\\
&\quad=
\int_0^\infty
\left[
\int_0^T|f|^2-
\int_0^T|V_Hf|^2
\right]d(-r_{b,h})(T)
\ge0.
\end{aligned}
}
\tag{L-105628.7}
\]

This is the actual-source analogue of the one-sided Hardy gap, with no frozen
carrier or surrogate numerator.

## 4. What this closes—and what it does not

The following infinite-line rows are proved at the conclusion-facing base Xi
rung down to the adjacent derivative height:

```text
standard Xi source log-concavity                    PROVED
actual current/Turan profile monotonicity            PROVED
Xi-prime all-pass innerness for H>beta_1             PROVED
causal weighted contraction                         PROVED
base phase-energy descent to b=beta_1               PROVED
```

This is not yet the desired zero-height descent. If `b<beta_1`, then for small
`h` the total height `H=b+h` can cross zeros of `Xi'`; the all-pass acquires an
anti-inner factor and the denominator-pole obstruction is active.

The result is also an energy theorem, not the pointwise differential-
microscope inequality. `R-105630` keeps that separation binding.

## 5. Reduced descent gate

Define

```text
SAFEDESC105628 — continuation below the adjacent derivative height

Show that the source-owned contraction and its physical pointwise/index
consumer extend from every b>=beta_1 to all b>=0 without an anti-inner
Xi-prime factor, denominator pole, or positive zero-height charge.
```

The former interval `[beta_1,beta_0]` is therefore removed from the source-
energy descent problem. By the zero-height variational theorem, a pointwise
realization of `SAFEDESC105628` together with `POINTID105630` implies RH.

A finite-window implementation must additionally retain the exact upper/lower
trace gauges, common-zero confluent factors and one telescoping endpoint charge.

## 6. Scope

The theorem proves a one-rung source-energy descent, not RH. It does not
analytically continue an inner factor through a zero of `Xi'`, does not prove
the pointwise microscope sign, and does not prove the finite endpoint/index
ledger.
