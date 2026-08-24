# L-105628 — The infinite-line base-Xi phase collision contracts throughout the zero-free safe region

Claim ID: `L-105628`  
Status: **PROVED UNCONDITIONAL BASE-RUNG SAFE-REGION SOURCE-ENERGY THEOREM; DESCENT BELOW THE EXTREMAL HEIGHT OPEN**  
Created: 2026-08-25  
Depends on: `L-105620--L-105627`  
RH status: **not assumed**

## 1. Literal source scope and the two height parameters

This theorem is stated at the base Xi rung, where the Fourier source is the
literal positive even kernel `Phi`. Put

\[
\beta_0=\sup\{\Im z:\Xi(z)=0\}.
\]

Fix a safe base and microscope scale

\[
b\ge\beta_0,
\qquad h>0,
\qquad H=b+h.
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

## 2. Both hypotheses are paid in the safe region

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

Because `H>b>=beta_0>=beta_1`, `L-105627` proves that `U_H` is inner. Hence
`V_H` is a causal isometry. Applying `L-105625` gives

\[
\boxed{
V_H^*M_{r_{b,h}}V_H
\preceq
M_{r_{b,h}}.
}
\tag{L-105628.5}
\]

Thus the actual Xi-prime all-pass cannot amplify the canonical
current-normalized base-Xi Turan source anywhere in the complete zero-free safe
region `b>=beta_0`.

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
rung **above its unknown extremal height**:

```text
standard Xi source log-concavity                    PROVED
actual current/Turan profile monotonicity            PROVED
safe-height Xi-prime all-pass innerness              PROVED
causal weighted contraction                         PROVED
safe-region infinite-line phase collision           PROVED
```

This is not yet the desired base descent. If `b<beta_0`, then for small `h` the
total height `H=b+h` may cross zeros of `Xi'`; the all-pass may cease to be
inner and the zero-height variational obstruction is active. That is exactly
the RH-bearing region.

## 5. Reduced descent gate

Define

```text
SAFEDESC105628 — continuation of the safe contraction below beta_0

Show that the source-owned contraction (L-105628.5), together with its
finite-window index ledger, extends from every b>=beta_0 to all b>=0 without a
denominator pole or positive zero-height charge.
```

Equivalently, identify a mechanism which prevents the inner/causal property or
its weighted contraction from failing at the first descending base. By the
zero-height variational theorem, `SAFEDESC105628` implies RH.

A finite-window implementation must additionally retain the exact upper/lower
trace gauges, common-zero confluent factors and one telescoping endpoint charge.

## 6. Scope

The theorem proves the source/phase sign only in the zero-free safe region. It
does not analytically continue an operator inequality through a denominator
zero and does not prove `SAFEDESC105628`, `MCTPHYS105610`, the finite shell
theorem or RH.
