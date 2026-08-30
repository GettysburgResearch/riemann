# T-104600 — Persistence–Mellin fixed-order Xi''' to Xi'' frontier

Claim ID: `T-104600`  
Status: **UNCONDITIONAL EXCURSION/MELLIN THEOREMS + TWO SOURCE-SIDE GATES**  
Created: 2026-08-24  
Depends on: `T-104540`, `L-104545--L-104548`, `R-104520`  
RH status: **unproved**

## 1. Binding correction

The unit-amplitude phase identity of `T-104590` is exact, but its proposed
lower-bound gate is not an independent producer. Up to explicit bounded
endpoints,

\[
\Delta\arg(\Xi''-i\lambda\Xi''')
\]

is the number of real zeros of `Xi''` itself. `R-104520` therefore retains the
phase as a detector and withdraws `UPHASE104590` as a closure input.

## 2. New unconditional source geometry

For every regular amplitude `y>0`, the actual Xi function satisfies

\[
\boxed{
G_y-W_y=\frac12N_y,
}
\tag{T-104600.1}
\]

where `N_y` counts solutions of

\[
|\Xi''(t)|=y.
\]

Equivalently, every wrong extremum is injectively paired with a good extremum
of strictly larger absolute critical value.

For every `p>0`,

\[
\boxed{
\sum_G|\Xi''(c)|^p-
\sum_W|\Xi''(c)|^p
=
\frac p2\int_{\mathbb R}
|\Xi''|^{p-1}|\Xi'''|\,dt
>0.
}
\tag{T-104600.2}
\]

After normalization by `A=||Xi''||_infinity`, the left side is the Laplace
transform

\[
\boxed{
\mathfrak H_{\Xi''}(p)
=
\int_0^\infty e^{-px}N_{Ae^{-x}}\,dx.
}
\tag{T-104600.3}
\]

Hence the complete Mellin reverse-Rolle hierarchy is completely monotone and
Hankel positive.

These are unconditional weighted and thresholded reverse-Rolle facts for the
actual Xi function.

## 3. Route A — excursion complexity

For a threshold `y=y(T)`, let

```text
delta_y = fraction of real Xi''' critical points with |Xi''|>y;
kappa_y = (number of |Xi''|=y level components) /
          (number of retained critical points).
```

Precisely `kappa_y=(G_y-W_y)/(G_y+W_y)`.

If

\[
\boxed{
\delta_y(1+\kappa_y)\ge1+\eta+o(1)
}
\tag{T-104600.4}
\]

for some `eta>0`, then

\[
\boxed{
\alpha_2\ge\eta\alpha_3>0.9873\,\eta.
}
\tag{T-104600.5}
\]

Call this gate `EXCUR104600`. It uses only unsigned superlevel critical counts
and unsigned level-crossing counts.

## 4. Route B — windowed Mellin variation

For some fixed `p>=1`, form on each regular window

\[
D_{p,I}
=
\frac12
\left[
p\int_I|\Xi''|^{p-1}|\Xi'''|
+\text{explicit endpoints}
\right],
\]

and

\[
B_{p,I}
=
\sum_{\Xi'''(c)=0,\ c\in I}
|\Xi''(c)|^{2p}.
\]

If windows covering density one of Conrey's real derivative zeros satisfy

\[
\boxed{
\frac{(D_{p,I})_+^2}{R_I B_{p,I}}
\ge
\frac{1+\eta}{2}+o(1),
}
\tag{T-104600.6}
\]

then again

\[
\boxed{
\alpha_2\ge\eta\alpha_3>0.9873\,\eta.
}
\tag{T-104600.7}
\]

Call this gate `PVAR104600`.

Unlike `CM2X104590`, the signed numerator is no longer an unknown critical
orientation moment: it is the explicit positive p-variation of `Xi''` plus
declared endpoints.

## 5. Why this is a big structural change

```text
phase drift / parent zero count          DETECTOR ONLY
pointwise Laguerre positivity            NOT REQUIRED
critical-value amplitude uniformity      NOT REQUIRED
mixed-theta matrix PSD                    ALREADY REFUTED

excursion persistence                     PROVED EXACT
all positive amplitude moments            PROVED EXACT
Mellin complete monotonicity               PROVED EXACT
unsigned threshold transfer               PROVED EXACT
p-variation / marked-moment transfer       PROVED EXACT
```

The remaining inputs are now ordinary unsigned excursion geometry or one
positive variation-to-moment estimate. Neither premise inserts real zeros of
`Xi''`.

## 6. Exact boundary

```text
EXCUR104600            OPEN
PVAR104600             OPEN
alpha_2 from alpha_3   NOT YET ESTABLISHED
Riemann Hypothesis     UNPROVED
```
