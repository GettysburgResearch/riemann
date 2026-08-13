# Finite mismatch gains a carry derivative

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Status: corrected continuation after `R-91102`; **RH remains unproved**

## Main result

The false exact-row shortcut is unnecessary for the interior outer columns. Let
`E_X` be the exact finite equality seed minus the continuum Volterra seed. Its
adjacent difference is exactly one local quadrature error:

\[
 E_X(n)-E_X(n+1)
 =d_X^\star(n)-\int_n^{n+1}d_X^\star(t)dt.
\]

On the reset window only `k<=55` occurs. A directed certificate gives the
finite derivative constant

\[
 C_{55}<17.
\]

Therefore

\[
 |\Delta E_X(n)|<\frac{17}{2}n^{-3/2},
\]

\[
 |v_q(E_X)|<\frac{51}{2}q^{-3/2},
\]

and

\[
 |\mathcal D_4v_q(E_X)|<32q^{-3/2}.
\]

Combining this with the positive width-three B-spline collar of `L-91111`
gives, for every interior outer column `K<=q<=X/4`,

\[
 \frac{|\mathcal D_4v_q(C_X-E_X)|}{\Omega_X(q)}
 <\frac{174}{K}.
\]

Thus scaling the nonnegative quantized endpoint weights by

\[
 (1+175/K)^{-1}
\]

makes all interior detail columns feasible. The endpoint weights stay
nonnegative and the score cost is bounded per factor-54 generation.

## What remains

`L-91306` already shows that the terminal taper is a bounded quotient-collar
problem, not a macroscopic loss. The unresolved conclusion-producing operation
is still the capacity-faithful transfer of the contracted parity-resolved
rough-prime state.

The exact replay is `X-91105`:

```text
PASS_FINITE_CONTINUUM_ADJACENT_MISMATCH
```

## Current status

```text
L-91112 exact finite row peel                    REFUTED
finite mismatch adjacent/carry bound             PROPOSED COMPLETE
positive collar + mismatch interior safety       PROPOSED COMPLETE
terminal bounded quotient certificate            OPEN
rough-prime coefficient-one allocation           OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
