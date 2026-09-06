# Global attack report — Hardy prime energy and multiplicative coherence

Agent: `gpt56-pro-17`  
Date: 2026-08-07  
Issue: #215  
Branch: `agent/gpt56-pro-17/215-global-hardy-prime-energy`

## Why the project needed a reset

The repository has made substantial progress on exact finite proof machinery:

- direct-`xi` response cones and Schur gates;
- cross-height Pick and product localizers;
- finite CCM/prolate source packets;
- selected-zero frames and complete Schur complements;
- source-canonical D-0001 ladders;
- square-screw and terminal-prime criteria.

However, the newest global branches reveal a common obstruction. The constant
coordinate of every square-support D-0001 matrix is already the RH-equivalent
square-screw scalar. Better packet conditioning cannot bypass its arithmetic
sign. Conversely, a finite ladder of positive scalar or matrix levels cannot
prove an eventual or cofinal statement.

The correct step back is therefore:

> identify one global arithmetic norm whose exponential growth exponent is
> exactly the rightmost zeta-zero displacement, and attack that norm directly.

## Main result

`T-21501` fixes one explicit compact piecewise-linear window and defines the raw
finite prime-power signal

\[
 Q_G(x)=\sum_n\frac{\Lambda(n)}{\sqrt n}G(x-\log n).
\]

Its Laplace transform is

\[
 -\widehat G(z)\frac{\zeta'}\zeta\!\left(z+\frac12\right).
\]

The window cancels the shifted pole at `z=1/2`, and its transform has no zeros
inside

\[
 0<\operatorname{Re}z<\frac12.
\]

Hardy-space Paley–Wiener theory then gives the exact global identity

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
  \frac{
   \log\left(1+\int^X|Q_G(x)|^2dx\right)
  }{2X}.}
\]

Consequently

\[
 \boxed{
 \mathrm{RH}
 \iff
 \int^X|Q_G(x)|^2dx=\exp(o(X)).}
\]

This criterion is robust against phase cancellation. A hypothetical off-line
zero produces an exponentially growing energy mode even if the signal happens
to be small at isolated translations.

## A simpler safe window than the existing smooth construction

`L-21501` uses the triangular spline

\[
 \phi=\mathbf1_{[0,1]}*\mathbf1_{[0,1]}
\]

and

\[
 G(u)=\phi(u-1)-2\phi(u-1-\log4).
\]

Its transform is exactly

\[
 \widehat G(z)
 =e^{-z}
  \left(\frac{1-e^{-z}}z\right)^2
  (1-2\,4^{-z}).
\]

The first factor has zeros only on `Re z=0`; the last factor has zeros only on
`Re z=1/2`. This finite piecewise-linear window is enough for the `H^2` attack
and has an explicit piecewise-cubic autocorrelation.

This does not replace the smoother terminal-prime windows when arbitrary-order
tail integration is needed. It removes unnecessary analytic machinery from the
global energy criterion.

## Exact prime-pair reduction

`L-21502` expands every finite energy as

\[
 \mathcal E_G(X)
 =\sum_{m,n}
 \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
 K_X(\log m,\log n),
\]

where

\[
 K_X(u,v)=\int_{-\infty}^XG(x-u)G(x-v)dx.
\]

This is one finite positive-semidefinite Gram matrix. In the interior its kernel
is the explicit autocorrelation

\[
 C_G(t)=5C_\phi(t)-2C_\phi(t-\log4)-2C_\phi(t+\log4).
\]

It vanishes outside

\[
 |t|\le2+\log4,
\]

so only bounded multiplicative ratios interact.

The diagonal is `O(X^3)` by the elementary bound `Lambda(n)<=log n`. Therefore
all possible positive exponential growth—and hence every possible failure of
RH—is carried by the coherent off-diagonal prime-pair form:

\[
 \boxed{
 \Theta_\zeta
 =\limsup_X
  \frac{\log(1+[\mathcal O_G(X)]_+)}{2X}.}
\]

This is the precise global arithmetic obstruction.

## Nonlinear Selberg equation

`L-21503` rewrites Selberg's coefficient identity as an exact additive-log
measure equation. With

\[
 dP=\sum\Lambda(n)n^{-1/2}\delta_{\log n},
 \qquad
 d\nu=dP-e^{y/2}dy,
\]

one has

\[
 \boxed{
 y\,d\nu+2dP_0*d\nu+d\nu*d\nu=dR.}
\]

The safe window annihilates `P_0`, so `Q_G=G*dnu` outside a fixed initial
interval. This exposes a genuinely nonlinear Volterra/Riccati structure behind
the prime-pair energy.

The next analytic breakthrough must use the quadratic convolution. Taking
absolute values or deleting it recovers only phase-blind PNT information and
cannot reach the RH scale.

## Three global routes are one exponent

Subject to independent review of their transfer layers, the repository now has
three exact coordinates for the same invariant:

\[
\begin{aligned}
\Theta_\zeta
&=\limsup_N
 \frac{\log(1+[-\mathscr S(N)]_+)}{2\log N}\\
&=\limsup_M
 \frac{\log(1+[-\log M\,e_0^TA_{N,M^2}e_0]_+)}{2\log M}\\
&=\limsup_X
 \frac{\log(1+\int^X|Q_G|^2)}{2X}.
\end{aligned}
\]

Thus:

- PR #202 gives a one-sided sampled scalar;
- PR #208 embeds it as the matrix constant coordinate;
- PR #215 gives a phase-robust global norm and exact prime-pair energy.

The last form is the most suitable target for a direct arithmetic attack because
it cannot be defeated by isolated phase cancellation.

## Exact finite checker

`X-21501` verifies the finite Gram expansion using integers and
`fractions.Fraction`. The retained synthetic control has

```text
energy        29
diagonal      28
off-diagonal   1
proof SHA-256 75fb476e2abec4ea872e01069e6944781dc0e949d7f048c75dc17bc27dca6834
```

Seven mutation tests are committed. It is a finite algebra regression, not a
Riemann computation.

## SERIOUS RESOLUTION PATH

A serious full-problem path is present:

```text
explicit safe compact window
-> exact raw-prime logarithmic derivative
-> Hardy H2 abscissa = rightmost-zero displacement
-> exact finite prime-pair Gram energy
-> subexponential off-diagonal multiplicative coherence
-> RH.
```

The first four steps are now explicit. The exact missing theorem is

\[
 \boxed{
 [\mathcal O_G(X)]_+=\exp(o(X)).}
\]

Promising attacks on that theorem are:

1. a Heath–Brown/Vaughan decomposition preserving the Gram until the final
   bilinear contraction;
2. a multiplicative large-sieve estimate for the explicit cubic
   autocorrelation kernel;
3. a Selberg-dispersion identity coupling `dnu*dnu` to the Möbius forcing in
   `L-21503`;
4. a dissipative Hardy-space estimate for the centered Volterra Riccati
   equation;
5. a recursive unit-log-block energy inequality.

This is not presented as a solved final step or an easier theorem disguised as
RH. It is the direct global arithmetic statement behind the currently leading
scalar and matrix programmes.

## Status

```text
safe finite window                         PROPOSED / proved algebraically
Hardy exponent transfer                    PROPOSED / complete proof supplied
finite prime-pair Gram identity            PROPOSED / exact
polynomial diagonal bound                  PROPOSED / elementary
Selberg log-convolution equation           PROPOSED / exact
subexponential off-diagonal energy         OPEN
Riemann Hypothesis                         UNPROVED
```
