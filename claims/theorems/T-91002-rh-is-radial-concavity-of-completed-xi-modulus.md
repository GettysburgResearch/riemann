# T-91002 — RH is equivalent to radial concavity of the completed xi modulus

Claim ID: `T-91002`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT DIFFERENTIAL CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91004`, the standard zero count and xi symmetries  
RH status: **unproved**

## 1. Statement

For real `x` and `t>0`, define

\[
 J_x(t)
 =t\frac d{dt}
 \log\left|\xi\left(\frac12+\sqrt t+ix\right)\right|
\]

away from zeros, and put

\[
 \mathcal C_x(t)=-J_x''(t).
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal C_x(t)\ge0
 \quad\text{for every }x\in\mathbb R,
 \ 0<t<\frac14.
 }
\tag{T-91002.1}
\]

Equivalently, RH holds exactly when every `J_x` is concave on `(0,1/4)`; one may replace `(0,1/4)` by `(0,infinity)`.

A second equivalent scalar form is

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal A_x(w)\ge0
 \quad\text{for every }x\in\mathbb R,
 \ 0<w<1,
 }
\tag{T-91002.2}
\]

where `A_x` is the one-safe-line generator of `T-91001`.

## 2. RH implies radial concavity

Under RH, `L-91004` gives

\[
 \mathcal C_x(t)
 =\sum_\gamma m_\gamma
 \frac{(\gamma-x)^2}
 {[t+(\gamma-x)^2]^3}
 \ge0.
\tag{T-91002.3}
\]

The sum is absolutely convergent. Moreover every alternating derivative is nonnegative:

\[
 \boxed{
 (-1)^k\mathcal C_x^{(k)}(t)
 =\frac{(k+2)!}{2}
 \sum_\gamma m_\gamma
 \frac{2(\gamma-x)^2}
 {[t+(\gamma-x)^2]^{k+3}}
 \ge0.
 }
\tag{T-91002.4}
\]

Thus under RH the radial curvature is completely monotone, not merely nonnegative.

The Peano identity of `L-91004` then gives `A_x(w)>=0` for real `0<w<1`.

## 3. Every off-line zero forces a local negative blow-up

Assume

\[
 \rho=\frac12+y+i\gamma,
 \qquad 0<y<\frac12,
\]

is a zero of multiplicity `m`. Evaluate at the matching centre `x=gamma`. Its reflected pair contributes

\[
 -\frac{2my^2}{(t-y^2)^3}.
\tag{T-91002.5}
\]

Every other term is meromorphic near `t=y^2`. A second term can have the same pole only when its centred coordinate squares to `y^2`; in the chosen right half-strip this is the same reflected pair, so the residue adds with the same sign. Consequently

\[
 \boxed{
 \mathcal C_\gamma(t)\longrightarrow-\infty
 \qquad(t\downarrow y^2,\ t>y^2).
 }
\tag{T-91002.6}
\]

Since `y^2<1/4`, this violates (T-91002.1). No terminal-pair selection, zero separation or Gram argument is required.

Likewise the matching contribution to `A_gamma` is

\[
 -\frac{4my^2}
 {(1-y^2)^2(1-y^2-w)}.
\tag{T-91002.7}
\]

As `w` increases to `1-y^2` from below, it tends to `-infinity`, while all noncoincident terms stay finite. Thus real-ray positivity (T-91002.2) also fails.

## 4. Countable reduction and finite witnesses

The false-RH violations in (T-91002.6) and (T-91002.7) are strict on open parameter intervals. Therefore rational `x,t` or rational `x,w` suffice.

For every fixed safe-line coefficient used to approximate the Peano integral, the arithmetic side is one absolutely convergent prime-power series on `Re(s)=3/2` plus explicit rational/polygamma terms. Hence false RH gives a finite directed prime certificate after choosing a sufficiently high finite order and an outward-rounded rational point. No negative Riemann-data instance is claimed here.

## 5. Exact frontier

```text
RH -> complete radial curvature monotonicity       PROPOSED COMPLETE
one off-line pair -> negative curvature blow-up    EXACT
RH <=> radial concavity on 0<t<1/4                 PROPOSED COMPLETE
RH <=> positive real unit-disc ray                  PROPOSED COMPLETE
terminal-pair selection                            NOT NEEDED
prime-side proof of radial concavity                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```
