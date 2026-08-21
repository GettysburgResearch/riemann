# L-21911 — Csordas–Varga gives the first Bernstein shadow exactly

Claim ID: `L-21911`  
Title: The classical Riemann-kernel moment inequality is precisely strict log-concavity of the canonical Mellin–gamma interpolant on the integers and strict increase of its shift quotient  
Status: **PROPOSED EXACT TRANSLATION OF A PUBLISHED THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Primary source: Csordas–Varga, *Moment inequalities and the Riemann hypothesis*, Constructive Approximation 4 (1988), 175–198, DOI 10.1007/BF02075457  
Dependencies: `L-21910`  
Scope: first finite-difference/Turán sign only; no higher complete alternation or zero-location theorem

## 1. Moment normalization

Let

\[
 b_n=\int_0^\infty x^{2n}\Phi(x)\,dx,
 \qquad n=0,1,2,\ldots,
 \tag{L-21911.1}
\]

where `Phi` is the positive Riemann Fourier kernel. The probability moments in
`L-21910` are one fixed positive multiple of `b_n`, so ratios are unchanged.

The Csordas–Varga theorem proves, more generally after the heat deformation
`e^(lambda x^2)`, that for every real `lambda` and every integer `n>=1`,

\[
 \boxed{
 b_n(\lambda)^2
 >\frac{2n-1}{2n+1}
  b_{n-1}(\lambda)b_{n+1}(\lambda).}
 \tag{L-21911.2}
\]

At `lambda=0` this is unconditional for the actual Riemann kernel. Their proof
uses the strict concavity of

\[
 t\longmapsto\log\Phi(\sqrt t).
 \tag{L-21911.3}
\]

## 2. Canonical interpolation values

Recall

\[
 C_\Xi(n)=\frac{n!m_{2n}}{(2n)!},
 \tag{L-21911.4}
\]

with `m_(2n)` proportional to `b_n`. Direct factorial cancellation gives

\[
\begin{aligned}
 \frac{C_\Xi(n)^2}
      {C_\Xi(n-1)C_\Xi(n+1)}
 ={}&
 \frac{2n+1}{2n-1}
 \frac{m_{2n}^2}
      {m_{2n-2}m_{2n+2}}.
\end{aligned}
 \tag{L-21911.5}
\]

Consequently (L-21911.2) is exactly

\[
 \boxed{
 C_\Xi(n)^2
 >C_\Xi(n-1)C_\Xi(n+1),
 \qquad n\ge1.}
 \tag{L-21911.6}
\]

Thus the positive integer samples of the entire function `C_Xi` are strictly
log-concave.

## 3. Shift-quotient form

The canonical quotient is

\[
 \phi_\Xi(n)=\frac{C_\Xi(n-1)}{C_\Xi(n)}.
 \tag{L-21911.7}
\]

Equation (L-21911.6) is equivalent to

\[
 \boxed{
 \phi_\Xi(n+1)>\phi_\Xi(n),
 \qquad n\ge1.}
 \tag{L-21911.8}
\]

This is the first necessary Bernstein sign. It is not numerical evidence: it is
a direct restatement of the published strict moment inequality.

## 4. Entire-function interpretation

If a positive real entire function has only simple negative zeros and belongs to
the Laguerre–Pólya type-I geometry, then its logarithm is concave on the positive
half-line. Therefore (L-21911.6) is exactly the first discrete shadow expected
from the final zero-location theorem for `C_Xi`.

Likewise, if `phi_Xi` were a Bernstein function, it would be increasing, so
(L-21911.8) is the first shadow of the Pick–Bernstein route `T-21903`.

The classical theorem therefore supports both new interfaces without proving
either one.

## 5. Why this does not finish the interpolation problem

A Bernstein restriction requires the complete alternating hierarchy

\[
 (-1)^{r-1}\Delta^r\phi_\Xi(n)\ge0
 \qquad(r\ge1),
 \tag{L-21911.9}
\]

plus the minimality/holomorphy conditions needed to recover a Bernstein
function from its integer values. A complete Bernstein/Pick conclusion is
stronger still.

Equation (L-21911.8) proves only the case `r=1`. Strict log-concavity is a
`TP_2` statement; it cannot be promoted to the total-positivity or
Laguerre–Pólya conclusion by terminology.

## 6. Status boundary

Closed here:

- exact normalization of the Csordas–Varga inequality;
- strict log-concavity of the integer `C_Xi` samples;
- strict monotonicity of the canonical quotient samples.

Open:

- every higher finite-difference sign;
- Bernstein or Pick interpolation;
- real-negative zeros of `C_Xi`;
- RH.