# Correction: the exact-row peel is false; the bounded-debt reset must retain the finite Euler and quantization layers

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Status: scope correction and revised attack; **RH remains unproved**

## Blocking finding

`L-91112` promoted the continuum Volterra identity

\[
 \overline b_X^\star(m)
 =\int_m^X L(X/s)\partial_s b_s(m)ds
\]

to the finite identity `b_X^star=overline b_X^star`. That promotion is false.
The exact finite seed is a left Riemann sum; the Volterra seed is its integral.

The smallest counterexample is `X=3,m=2`:

\[
 b_3^\star(2)=\frac1{\sqrt2}\log\frac32,
\]

whereas the asserted integral differs by

\[
 4\sqrt2-4\sqrt3+
 \frac{5\sqrt2}{2}\log\frac32>0.
\]

See `R-91102` for the exact derivation.

## Status consequences

The following labels in `L-91112` are withdrawn:

```text
exact finite equality-row Volterra representation;
exact finite outer-row positivity from L>0;
exact ordinary/detail saturation by truncating those rows;
exact deletion of the terminal annulus and score collar.
```

The real-endpoint infinitesimal row positivity remains useful, but it applies to
the continuum endpoint frame.

## Correct finite route

The valid reset still has unusually favorable quantitative structure:

1. `L-91106/L-91107` give a positive continuum endpoint density on the factor-54
   window.
2. `L-91110` gives nonnegative integer endpoint weights, exact two-moment bulk
   reproduction and favorable score curvature.
3. `L-91111` makes the width-three quantization collar coefficientwise positive
   and quantitatively small.
4. `L-91303` retains the first Euler correction, quotient-knot atoms and an
   `O(X^-3/2)` remainder.
5. `L-91306` localizes the terminal taper to bounded-width quotient collars.
6. `L-91109/L-91113` provide the parity-resolved finite forcing and delayed
   rough-prime state.

The remaining proof must therefore combine these valid layers rather than erase
them.

## New quantitative observation

Let

\[
 d_X^\star(t)=
 \sum_{k\le X/t}\frac{\mu(k)}{\sqrt{kt}}
 \log\frac X{kt}
\]

and let `E_X` be the finite Riemann-sum seed minus its continuum integral. Then

\[
 E_X(n)-E_X(n+1)
 =d_X^\star(n)-\int_n^{n+1}d_X^\star(t)dt.
\]

On `n>=X/55`, differentiation of the finitely many active terms gives

\[
 |E_X(n)-E_X(n+1)|\ll n^{-3/2}.
\]

Consequently its ordinary carry disturbance is `O(q^-3/2)` and its radix-four
detail disturbance is also `O(q^-3/2)`. The seed mismatch is visible at order
`X^-1/2`, but the carry's adjacent difference gains a full power. This is the
correct mechanism for the bounded-debt repair.

The next theorem packet should combine this bound with the positive
quantization collar and a fixed top omission or triangular terminal repair.

## Correct frontier

```text
continuum factor-54 density positivity             RETAINED
positive endpoint/B-spline quantization             RETAINED
finite Euler correction and robust Hall margins     RETAINED
positive width-three collar                          RETAINED
terminal quotient localization                       RETAINED
exact finite-row peel of L-91112                     REFUTED
bounded outer capacity/score repair                  OPEN, now quantitative
rough-prime coefficient-one state allocation         OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
