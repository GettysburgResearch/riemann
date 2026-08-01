# M-18506 — Production protocol for the absorbed row and deficit bridge

Status: `METHODOLOGY / FAIL-CLOSED PRODUCTION INTERFACE`

The next cofinal artifact must not extend the finite `W` ladder. It must add two
new proof objects at the same supports.

## A. Absorbed-row object

Emit the exact `R_N` basis and a global-radical synthesis

```text
R_global = J_R + T_R
```

with a directed packet bound on the complete exterior tail. The checker must
retain

```text
T_R* G_tail T_R
complete Weil-form tail Gram
corrected R/W and R/ambient row Grams
```

and return the actual rates `e_N` and `kappa_N`. A source constraint or local
Möbius reconstruction is not accepted as a small-tail certificate.

`L-18515` supplies a mandatory falsification gate: for every certified complex
zero candidate `z`, the tail interval must contain the exact identity

```text
V_z(T_R) = -V_z(J_R).
```

Any claimed vanishing bound incompatible with that evaluation is rejected.

## B. Deficit-projector object

Emit

```text
G_lambda, D_lambda, g_lambda, Gamma_lambda,
Q_0, Y_D, Y_C, source Y_S.
```

The exact consumer applies `L-18516`. Only

```text
cross = 0,
high > 0,
low > 0,
span(Y_S)=span(Y_D)
```

promotes the source flag to the global deficit-canonical augmentation.

## C. Assembly

For each frozen finite support, directed precision and form-core size may be
chosen so the assembly radius is at most `2^-j`; hence `delta_j -> 0` is a
standard diagonal proof-engineering step once the analytic remainder formulas
are bound. The RH-bearing work is the absorbed-row tail and the actual deficit
projector, not numerical precision.
