# L-104545 — Excursion persistence pairing and exact threshold reverse Rolle

Claim ID: `L-104545`  
Status: **PROVED EXACT**  
Created: 2026-08-24  
RH status: **not assumed**

Let `f` be a real `C^2` function on the real line such that

1. `f(t) -> 0` as `t -> +/-infinity`;
2. every nonzero critical point is simple;
3. every positive level used below is regular.

For a regular `y>0`, let

\[
G_y=\#\{c:f'(c)=0,\ c\ {\rm good},\ |f(c)|>y\},
\]

\[
W_y=\#\{c:f'(c)=0,\ c\ {\rm wrong},\ |f(c)|>y\},
\]

and let

\[
N_y=\#\{t\in\mathbb R:|f(t)|=y\}.
\]

A critical point is good when `f(c)f''(c)<0` and wrong when the product is
positive.

## 1. Component identity

The open set

\[
\Omega_y=\{t:|f(t)|>y\}
\]

is a disjoint union of bounded intervals. On each component `f` has constant
sign.

On a positive component the critical points alternate

```text
positive maximum, positive minimum, ..., positive maximum.
```

The maxima are good and the minima are wrong. Hence that component contains
exactly one more good than wrong critical point. The same statement, with
minimum and maximum exchanged, holds on a negative component.

Every component has two regular boundary crossings of `|f|=y`. Therefore

\[
\boxed{
G_y-W_y
=
\#\pi_0(\Omega_y)
=
\frac12N_y.
}
\tag{L-104545.1}
\]

In particular,

\[
\boxed{G_y\ge W_y\qquad(y>0).}
\tag{L-104545.2}
\]

Thus the good critical-value multiset dominates the wrong multiset at every
amplitude threshold, not merely after one chosen weighting.

## 2. Persistence pairing

Apply the one-dimensional elder rule separately to the positive excursion
tree of `f` and the positive excursion tree of `-f`.

Every wrong positive minimum merges two positive superlevel components. Pair it
with the lower of the two component maxima that dies at the merge. The paired
maximum is good and has strictly larger amplitude. The same construction pairs
every wrong negative maximum with a good negative minimum of larger amplitude.

Consequently there is an injection

\[
\boxed{
\mathfrak p:\{\text{wrong extrema}\}
\hookrightarrow
\{\text{good extrema}\}
}
\tag{L-104545.3}
\]

such that

\[
\boxed{
|f(\mathfrak p(c))|>|f(c)|
}
\tag{L-104545.4}
\]

for every wrong extremum `c`. Unpaired good extrema are the persistent
components surviving the corresponding merge trees.

The pairing is defined before any amplitude weight is chosen. Therefore every
increasing nonnegative test function `Phi_amp` obeys

\[
\sum_G\Phi_{\rm amp}(|f(c)|)
\ge
\sum_W\Phi_{\rm amp}(|f(c)|),
\tag{L-104545.5}
\]

whenever the sums converge.

## 3. Xi specialization

For `f=Xi''`, Stirling decay makes all positive-amplitude superlevel sets
compact and the critical set locally finite. Hence (L-104545.1--5) apply by
regular exhaustion.

This is an unconditional Xi-specific reverse-Rolle dominance theorem. It is
weighted/thresholded and does not by itself assert a positive unweighted
asymptotic density.
