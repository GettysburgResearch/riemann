# M-15104 — Production protocol for the Ward target-preservation gate

Methodology ID: `M-15104`  
Status: **PROOF-PRODUCING PROTOCOL**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15138`, `T-15116`, `X-15118`  
Scope: test whether the nonlinear finite-jet Ward amendment preserves the completed-zeta target  

## 1. Required finite objects

For each finite window/readout pair `(M,N)`, preserve:

1. the original linear Guinand--Weil coefficients
   
   \[
   a_{\ell,M}^{\rm lin};
   \]

2. the raw and renormalized comparison maps
   
   \[
   \widetilde R_{M,N},\quad
   C_{M,N},\quad
   R_{M,N}=\widetilde R_{M,N}-C_{M,N};
   \]

3. the raw and renormalized seam operators
   
   \[
   A_{M,N}=\widetilde R^*S_R\widetilde R,
   \quad
   K_{M,N}=R^*S_RR;
   \]

4. directed Schatten-four bounds for the three comparison maps;
5. directed trace intervals for `A^ell` and `K^ell`;
6. the exact target defect
   
   \[
   e_{\ell,M,N}
   =a_{\ell,M}^{\rm lin}-\operatorname{Tr}K_{M,N}^{\ell}.
   \]

Do not infer a target-preservation verdict from test-function convergence alone.

## 2. First gate: order four

The first production computation is

\[
 \boxed{
 e_{4,M,N}
 =a_{4,M}^{\rm lin}-\operatorname{Tr}K_{M,N}^{4}.}
\]

The exact centered-zeta target is

\[
 \boxed{
 \tau_4
 =-\frac16\left[
  \frac{\xi^{(4)}(1/2)}{\xi(1/2)}
  -3\left(\frac{\xi''(1/2)}{\xi(1/2)}\right)^2
 \right].}
\]

A proof-producing quartic record must independently enclose

\[
 a_{4,M}^{\rm lin},
 \qquad
 \operatorname{Tr}A_{M,N}^{4},
 \qquad
 \operatorname{Tr}K_{M,N}^{4},
 \qquad
 \tau_4,
\]

and bind the normalization and finite-window parameters. The desired ladder is

\[
 a_{4,M}^{\rm lin}\to\tau_4,
 \quad
 \operatorname{Tr}A_{M,N}^{4}\to\tau_4,
 \quad
 \operatorname{Tr}K_{M,N}^{4}\to\tau_4.
\]

If `e_4` remains separated from zero, the Ward-amended determinant has a
different target. If it tends to zero, proceed to orders `6,8,...`.

## 3. Schatten-smallness route

Certify

\[
 \|A_{M,N}-K_{M,N}\|_2
 \le
 (\|\widetilde R_{M,N}\|_4+\|R_{M,N}\|_4)
 \|C_{M,N}\|_4.
\]

The strongest economical target is

\[
 \sup(\|\widetilde R\|_4+\|R\|_4)<\infty,
 \qquad
 \|C_{M,N}\|_4\to0.
\]

This makes every relative determinant trace vanish with one uniform majorant.
The singular-seam map must be estimated after the complete
`Tr_cmp -> LCI -> Pi_R` chain; a norm on the source test function is not a
substitute.

## 4. Raw target-pullback route

On a fixed disk, compute

\[
 \rho_{M,N}(r)
 =\sup_{|w|\le r}
 \left|g_M^{\rm lin}(w)
  -\frac d{dw}\log\det{}_2(I+iwA_{M,N})\right|.
\]

Target preservation requires both

\[
 \rho_{M,N}(r)\to0
\]

and

\[
 \|A_{M,N}-K_{M,N}\|_2\to0.
\]

The first equality is the raw scalar/cyclic pullback; the second is finite-jet
decoupling. Record them separately so one cannot mask failure of one gate with
the other.

## 5. Exact target-ratio output

The certificate consumer must emit

\[
 \log\frac{F_M^{\rm lin}(w)}{F_{M,N}^{\rm Ward}(w)}
 =\sum_{\ell\ge2}
  \frac{(-i)^{\ell-2}}{\ell}
  e_{\ell,M,N}w^\ell.
\]

At centered parity, the first output is

\[
 -\frac14e_{4,M,N}w^4.
\]

A constant or linear exponential correction may not be used to absorb this
term.

## 6. Verdict classes

Use only:

```text
TARGET_PRESERVATION_CERTIFIED
TARGET_CHANGE_CERTIFIED_AT_ORDER_ELL
UNRESOLVED_INTERVAL_TOUCHES_ZERO
MISSING_RAW_PULLBACK
MISSING_SCHATTEN_JET_BOUND
```

No ordinary numerical midpoint is a target-preservation proof.
