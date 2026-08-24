# M-105620 — Hostile review contract for the current–Turán/log-concave causal packet

Status: **BINDING REVIEW SPECIFICATION**  
Created: 2026-08-25  
RH status: **unproved**

A reviewer must check each interface below independently before promoting the
packet.

## A. Fourier/current normalization

1. Re-derive
   `J_h=(1/2) partial_h |Xi(a+ih)|^2`.
2. Re-derive the frequency variables
   `u=x+xi/2`, `v=x-xi/2` and every factor of two in
   `Lambda_(2m)`.
3. Verify
   `j_h=sum h^(2k+1)Lambda_(2k+2)/(2k+1)!`.
4. Keep the upper source `exp(-h xi)` and reflected source `exp(h xi)` in
   separate causal channels. Do not replace either by `exp(-h|xi|)` before the
   two-trace split is made.

## B. Xi-kernel log-concavity

1. Confirm the standard theta normalization in `L-105626`.
2. Re-derive the score and curvature
   ```text
   a_n=9/2-2y_n+6/(2y_n-3),
   b_n=-4y_n-24y_n/(2y_n-3)^2.
   ```
3. Check the positive-mixture identity
   `(log Phi)''=E b+Var(a)`.
4. Verify every uniform tail bound, especially the monotonic ratio after
   `n=3` and the final `1881/7000<1` margin.
5. Do not infer RH, `TP_infinity`, or Fourier real-rootedness from ordinary
   log-concavity.

## C. Monotone profile theorem

1. Derive the conditional law
   `q_s(x) proportional x^2 Phi(s/2+x)Phi(s/2-x)`.
2. Check the quantile-velocity equation and its boundary conditions.
3. Verify the maximum-principle implication `|v_s|<=1/2`.
4. Recheck the exact divided-difference expectation and its constants.
5. Confirm that the microscope scale `h` and total height `H=b+h` are not
   conflated. The actual profile is `(h/H)R_H`.

## D. Inner/causal all-pass

1. Reconstruct the Cartwright factorization of
   `Xi^(r+1)(z+iH)` for `H>=beta_(r+1)`.
2. Check real boundary factors and common-zero cancellation.
3. Verify that the positive Xi Laplace moments orient the exponential factor
   toward `H-infinity`, yielding an inner quotient.
4. Confirm the Paley--Wiener direction: the chosen inner multiplier must act as
   a causal, not anti-causal, isometry on `L^2(0,infinity)`.

## E. Finite bank and shell firewalls

1. Reprove the model-space identity
   `ker H_(bar U)=UH^2` and isometry on `K_U`.
2. Verify `dim K_U=deg U` only at finite Blaschke scope.
3. Do not identify that degree with a finite Xi rectangle count without the
   endpoint argument-principle ledger.
4. Replay the exact family `p_N=z^N`, including
   `E_+=E_-=r^2` and `19/9>2` for `r=1/3`.
5. Retain the conclusion that raw negative shell energy is an overstrong
   sufficient gate, not a necessary real-rootedness invariant.

## F. Binding scope

The packet proves source hierarchy, Xi-kernel log-concavity, safe-region inner
causality, weighted contraction and exact source-owned compression. It does
not prove:

```text
descent below beta_0;
pointwise physical microscope sign;
finite endpoint/index closure;
MCTPHYS105610;
HSHE105602 or its balanced successor;
Riemann Hypothesis.
```

Any review which removes these fail-closed boundaries is invalid.
