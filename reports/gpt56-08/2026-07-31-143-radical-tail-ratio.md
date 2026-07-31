# Cofinal radical-tail/coercivity ratio closure

Agent: `gpt56-08`  
Date: 2026-07-31  
Stack: PR #152 / positive localized-Weil lower-floor route  
Classification: proposed analytic theorem plus exact finite regression; no RH proof claimed

## Result

The requested asymptotic ratio is closed in the block Temple--Schur setting.
Use the fixed exact self-Fourier Riemann source

\[
 h_R(x)=\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2},
\]

whose two source constraints vanish exactly.  Its global `E`-image is a Weil
radical vector.  Truncation to `[lambda^-1,lambda]` leaves a double-Gaussian
external tail.  Direct contraction of the archimedean multiplier, both
boundary evaluations, and every prime-power translation gives

\[
 \mathfrak T_{\lambda,\tau_\lambda}
 \le C\lambda^M(1+\log\lambda)^{3/2}e^{-\pi\lambda^2},
 \qquad
 \tau_\lambda=\frac12-\frac1{\log\lambda}.
\]

`L-14311`'s exact multiband symbol theorem supplies, at every support, a finite
complete low packet whose complement has a fixed `L2` floor.  In the moving
Hardy metric this yields

\[
 h_{\lambda,\tau_\lambda}\ge\lambda^{-1}.
\]

Therefore, along `lambda_j=e^j`,

\[
 \mathfrak T_j/h_j\to0,
 \qquad
 \mathfrak T_j^2/(h_j\|k_j\|^2)\to0.
\]

## Important scope

The denominator is the complement of an enlarged finite complete packet, not
the complement of one trial vector alone.  This proves the requested weaker
squared-residual condition for the block lower-floor route.  It does not close
the growing finite low block and therefore does not yet prove RH.

## New exact files

- `L-14312` — Gaussian global-radical tail contraction.
- `L-14313` — finite packet and polynomial Hardy moat, including form-domain
  closure.
- `T-14303` — both cofinal ratios.
- `O-14303` — exact remaining low-block theorem.
- `X-14307` — exact source and ratio regression.

## Exact regression

The synthetic packet verifies

```text
Hardy coercivity lower    3/512
cross residual upper      1/2^20
trial norm-square lower   1/2
linear ratio upper        1/6144
squared ratio upper       1/3221225472
```

All six mutation tests pass.  The regression is finite arithmetic only.
