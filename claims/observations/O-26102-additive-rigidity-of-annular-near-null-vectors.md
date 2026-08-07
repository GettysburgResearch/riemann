# O-26102 — Additive rigidity of annular near-null vectors

Observation ID: `O-26102`  
Title: The Annular Dual Frame denominator is the second-difference energy of an additive arithmetic function, with the von-Mangoldt vector as the logarithmic near-null mode  
Status: **PROPOSED STRUCTURAL CONTINUATION — RIGIDITY THEOREM OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `L-26105`

## 1. Exact additive-function coordinate

For a nonnegative prime-power vector `lambda`, define

\[
\boxed{
 L_\lambda(n)
 =\sum_{\substack{q=p^a\\q\mid n}}\lambda_q.
}
\tag{O-26102.1}

This is an additive arithmetic function in the usual coprime sense:

\[
 (m,n)=1
 \quad\Longrightarrow\quad
 L_\lambda(mn)=L_\lambda(m)+L_\lambda(n).
 \tag{O-26102.2}

The annular adjoint is exactly

\[
\boxed{
 (A_X^*\lambda)_j
 =2L_\lambda(j)-L_\lambda(j-1)-L_\lambda(j+1).
}
\tag{O-26102.3}

Therefore the `ADF` denominator is the discrete curvature energy

\[
\boxed{
 \|A_X^*\lambda\|_2^2
 =\sum_{j\in I_X}
  |\Delta^2L_\lambda(j)|^2.
}
\tag{O-26102.4}

The annular flow problem is thus a quantitative rigidity problem for additive functions with small second differences on one long interior interval.

## 2. Exact logarithmic direction

For

\[
 \lambda_q=\Lambda(q),
\]

one has

\[
 L_\Lambda(n)=\log n.
 \tag{O-26102.5}

Consequently

\[
 -\Delta^2L_\Lambda(j)
 =\log\frac{j^2}{j^2-1}
 \asymp j^{-2}.
 \tag{O-26102.6}

This is precisely the near-null direction isolated in `L-26105`. The small denominator is not an accidental matrix condition number; it is the discrete curvature of the logarithm.

## 3. Proposed quantitative rigidity theorem

The natural strengthening of `ADF` is a decomposition theorem.

For every nonnegative prime-power vector `lambda`, find a scalar `c_lambda>=0` and a transverse vector `lambda^perp` such that

\[
 \lambda=c_\lambda\Lambda+\lambda^\perp,
 \tag{O-26102.7}

and

\[
\boxed{
 \|\lambda^\perp\|_{\mathrm{source}}
 \le X^{o(1)}\|A_X^*\lambda\|_2.
}
\tag{O-26102.8}

The source norm must be strong enough to control

\[
 |\langle\lambda^\perp,r_X\rangle|.
\]

Equivalently, prove directly that an additive `L_lambda` with small annular curvature is close, in the prime-power coefficient metric seen by `r_X`, to `c log n`.

The exact same-base Toeplitz floor controls prime-power-chain fluctuations. Complete-period orthogonality controls different prime bases away from the annular boundaries. The remaining issue is a quantitative stability theorem across those boundary ledgers.

## 4. Scalar logarithmic mode

After transverse rigidity, `ADF` reduces to the scalar term

\[
 c_\lambda\langle\Lambda,r_X\rangle.
\]

But

\[
 \langle\Lambda,r_X\rangle
 =J_X(b_X^{(0)})-P(X),
\]

where `P(X)` is the complete prime ramp. This is the RH-bearing scalar mode and cannot be bounded by a generic frame theorem.

The factor-two child descent and the signed constraint-dipole identity of PR #254 suggest the correct final step: derive a strict-scale recurrence for the positive part of this logarithmic mode while the transverse directions are paid by curvature.

A schematic target is

\[
\boxed{
 \langle\Lambda,r_X\rangle_+
 \le X^{o(1)}
 +\rho\max_{Y\le X/2+O(1)}
  \langle\Lambda,r_Y\rangle_+,
 \qquad\rho<1.
}
\tag{O-26102.9}

Iteration would close the scalar near-null direction and, together with (O-26102.8), prove `ADF`.

## 5. Why this is a genuine new route

The proposal separates the transport theorem into two qualitatively different statements:

```text
transverse additive fluctuations
    -> annular second-difference frame;

logarithmic near-null mode
    -> signed factor-two scalar recurrence.
```

This avoids trying to prove a false generic frame floor and explains why highly composite collectors and the Mertens/prime-ramp firewall appear in the same finite matrix.

## 6. Proof boundary

Exact:

- the additive-function representation;
- the second-difference denominator;
- the logarithmic/von-Mangoldt near-null mode.

Open:

- the quantitative transverse rigidity estimate;
- the scalar factor-two recurrence;
- `ADF` and RH.