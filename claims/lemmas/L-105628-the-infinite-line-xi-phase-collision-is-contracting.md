# L-105628 — The infinite-line base-Xi phase collision is contracting

Claim ID: `L-105628`  
Status: **PROVED UNCONDITIONAL BASE-RUNG INFINITE-LINE SOURCE-ENERGY THEOREM; FINITE PHYSICAL TRANSFER OPEN**  
Created: 2026-08-25  
Depends on: `L-105620--L-105627`  
RH status: **not assumed**

## 1. Literal source scope

This theorem is stated at the base Xi rung, where the Fourier source is the
literal positive even kernel `Phi`. Put

\[
\beta_0=\sup\{\Im z:\Xi(z)=0\}.
\]

For `h>0`, let

\[
\boxed{
r_h(\xi)
={h e^{-h\xi}\Lambda_2(\xi)\over j_h(\xi)},
\qquad \xi\ge0,
}
\tag{L-105628.1}
\]

be the current-normalized first exterior-square chaos of the standard Xi
source.

Let

\[
\boxed{
U_{0,\beta}(x)
={D_{0,\beta}^{\#}(x)\over D_{0,\beta}(x)},
\qquad
D_{0,\beta}(z)=\Xi'(z+i\beta_0),
}
\tag{L-105628.2}
\]

with real common factors cancelled, and let `V_(0,beta)` be its
Paley--Wiener operator on `L^2(0,infinity)`.

The restriction to `r=0` is load bearing. Odd Xi derivatives do not have the
same nonnegative even full-line Fourier source. Extensions to higher rungs
require their own source theorem and are not inferred here.

## 2. Both hypotheses are paid at the base rung

`L-105626` proves that the standard Xi Fourier kernel is strictly
log-concave. `L-105624` therefore gives

\[
\boxed{r_h\text{ nonincreasing on }[0,\infty).}
\tag{L-105628.3}
\]

`L-105627`, specialized to `r=0`, proves that `U_(0,beta)` is inner, hence
`V_(0,beta)` is a causal isometry.

Applying `L-105625` gives the exact operator inequality

\[
\boxed{
V_{0,\beta}^*M_{r_h}V_{0,\beta}
\preceq
M_{r_h}
\qquad(h>0).
}
\tag{L-105628.4}
\]

Thus the actual Xi-prime all-pass cannot amplify the canonical
current-normalized base-Xi Turan source on the complete infinite one-sided
line.

## 3. Exact energy form

For every source vector `f in L^2(0,infinity)`,

\[
\boxed{
\int_0^\infty
r_h(\xi)|(V_{0,\beta}f)(\xi)|^2d\xi
\le
\int_0^\infty r_h(\xi)|f(\xi)|^2d\xi.
}
\tag{L-105628.5}
\]

The exact reserve is the delayed prefix energy

\[
\boxed{
\begin{aligned}
&\int r_h|f|^2-\int r_h|V_{0,\beta}f|^2\\
&\quad=
\int_0^\infty
\left[
\int_0^T|f|^2-
\int_0^T|V_{0,\beta}f|^2
\right]d(-r_h)(T)
\ge0.
\end{aligned}
}
\tag{L-105628.6}
\]

This is the physical all-pass analogue of the source-weighted one-sided Hardy
gap, now using the **actual base-Xi current/Turan contraction profile** rather
than a frozen coefficient packet.

## 4. What this closes

The following infinite-line source/phase rows are proved at the conclusion-
facing base rung:

```text
standard Xi source log-concavity                    PROVED
base-Xi current/Turan profile monotonicity           PROVED
extremal Xi-prime all-pass innerness                 PROVED
causal weighted contraction                         PROVED
base infinite-line phase-collision contraction      PROVED
```

Accordingly the variable Xi-prime phase is not itself an adverse infinite-line
energy at the base rung. The remaining difficulty is created only when the
cofinal physical problem is identified with finite zero-count traces and their
endpoint/index ledger.

## 5. Reduced finite physical gate

Define

```text
FPXFER105628 — finite physical restriction of the contracting base-Xi phase

Transfer (L-105628.4) to a cofinal family of regular Xi rectangles while
retaining:

  exact upper/lower trace gauges;
  boundary and common-zero confluent factors;
  finite horizontal/vertical endpoint charges;
  denominator-zero codimension;
  the source-to-zero-count index map.
```

No moving-carrier freeze, numerator reconstruction, raw all-pass phase norm,
or infinite-line phase commutator remains in this gate.

A pointwise-strength realization of `FPXFER105628` gives the differential
microscope sign and RH. A trace-strength realization gives the balanced shell
or robust-proportion theorem.

## 6. Scope

An infinite-line weighted contraction does not itself identify the physical
finite zero-count bank. Equation (L-105628.4) therefore does not prove
`MCTPHYS105610`, the finite shell theorem, or RH. Higher derivative rungs are
not covered by the positive full-line source argument in this file.
