# X-18504 — Direct complete-complement residual-shorting verifier

Claim ID: `X-18504`  
Status: `EXACT SYNTHETIC REPLAY`  
Dependencies: `L-18512`, `T-18504`  

The standard-library verifier checks the scalar instance of

\[
S_W
=J_X^*\mathcal HJ_X
-\mathscr R_X^*C^{-1}\mathscr R_X
\]

and its coercive lower certificate. All arithmetic uses
`fractions.Fraction`.

The retained control is

\[
P=1,
\quad
E=9/10,
\quad
B=19/10,
\quad
C=Z=M=h=G=1,
\quad
X=3/4.
\]

It obtains exactly

```text
trial-lift energy       77/80
solve residual          1/4
residual penalty        1/16
certified direct floor   9/10
exact Schur floor        9/10
separated floor          0
joint improvement        9/10
```

Eight central/adversarial tests pass, including coercivity, decomposition,
verdict, Boolean-input, metric-sign, exact-solve, and deliberately crude-solve
mutations.

The experiment proves only the finite algebra and strict separation. It is not
a Riemann/Suzuki production result.
