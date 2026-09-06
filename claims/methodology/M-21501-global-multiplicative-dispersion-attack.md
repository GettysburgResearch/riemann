# M-21501 — Global multiplicative-dispersion attack

Claim ID: `M-21501`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215

## Strategic reset

The repository now contains many exact finite cones, finite Schur reductions,
finite zero frames, and proof-producing level checks. Those are valuable, but
none supplies a global completeness mechanism by itself.

`T-21501` and `L-21502` reduce the full Riemann Hypothesis to one explicit
arithmetic estimate:

\[
 \boxed{
 \mathcal O_G^+(X)=\exp(o(X)),}
 \tag{M-21501.1}
\]

where `O_G` is the off-diagonal part of one finite positive-semidefinite
prime-pair Gram energy. The exact exponent of failure is the rightmost
horizontal displacement of a zeta zero.

This is the route to attack directly. It does not require selecting a finite
candidate height, increasing a response degree, or building another local
packet.

## 1. Work in unit logarithmic blocks

Put

\[
 \mathcal B_G(j)=\int_j^{j+1}|Q_G(x)|^2dx.
\]

The block uses only prime powers with

\[
 e^{j-C}\le n\le e^{j+C}
\]

for one fixed constant `C=3+log4`. Expand it exactly as

\[
 \mathcal B_G(j)
 =\sum_{m,n}
  \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
  K_j(\log m,\log n).
 \tag{M-21501.2}
\]

The target is

\[
 \boxed{
 \mathcal B_G(j)\le\exp(o(j)).}
 \tag{M-21501.3}
\]

A polynomial bound in `j` would prove RH.

## 2. Separate the easy diagonal

The diagonal is `O(j^3)` by elementary estimates. It should be removed exactly
before any inequality is applied. Every proof attempt must report

```text
total energy
diagonal energy
off-diagonal signed energy
positive off-diagonal excess
```

and must never spend cancellation by taking entrywise absolute values of the
full Gram.

## 3. Exploit bounded multiplicative ratio

The autocorrelation kernel vanishes unless

\[
 e^{-(2+\log4)}\le m/n\le e^{2+\log4}.
\]

Decompose into finitely overlapping ratio sectors and dyadic size blocks. On
one block, write

\[
 m=d r,
 \qquad
 n=d s,
 \qquad
 (r,s)=1,
\]

or use an additive parameterization `m=n+h` after fixing a ratio sector.
The compact piecewise-cubic kernel is explicit; no Fourier-window numerical
error is present.

## 4. Use identities that preserve bilinear cancellation

Promising proof mechanisms are:

1. **Heath–Brown/Vaughan decomposition.** Expand each von Mangoldt factor into
   short Type I/II bilinear sums, keeping the positive-semidefinite kernel until
   the final contraction.
2. **Multiplicative large sieve.** Mellin-expand the interior autocorrelation
   and control the resulting Dirichlet-polynomial energy uniformly in the
   logarithmic block.
3. **Selberg nonlinear equation.** Use `L-21503`
   \[
   y\nu+2P_0*\nu+\nu*\nu=R
   \]
   to combine the quadratic prime-pair term with the Möbius forcing before
   estimating either one.
4. **Dispersion / shifted convolution.** Convert the off-diagonal energy into
   averaged correlations of `Lambda(n)Lambda(m)` at comparable scales, with the
   exact cubic kernel supplying smoothness and cancellation.
5. **Hardy-space positive-real methods.** Prove the filtered Riccati solution
   has zero `H^2` abscissa by an accretive Volterra estimate.

A phase-blind PNT error bound is not an acceptable substitute: the desired
estimate is RH-equivalent and its cancellation is quadratic.

## 5. Proof-producing computational role

Computation should support, not replace, the global theorem:

1. enumerate complete prime powers in successive unit-log blocks;
2. evaluate the exact piecewise-cubic Gram, with outward arithmetic;
3. record total/diagonal/off-diagonal energies;
4. test candidate bilinear decompositions and scale-recursive inequalities;
5. retain counterexamples to false inequalities immediately;
6. never infer a cofinal bound from a finite positive ladder.

Useful finite output is a conjectured inequality with constants stable across
blocks, followed by an analytic proof.

## 6. Serious resolution path

A serious full-resolution path is present:

```text
explicit safe finite window
-> exact raw-prime Laplace transform
-> Hardy H2 exponent = rightmost-zero displacement
-> exact finite multiplicative prime-pair Gram
-> global subexponential off-diagonal energy bound
-> RH.
```

The first four arrows are supplied by `L-21501`, `T-21501`, and `L-21502`.
The sole RH-bearing step is (M-21501.1).

This is intentionally a large target. It is not advertised as easier than RH;
it is advertised as the direct global arithmetic statement that the repository
should now attack instead of repeatedly strengthening finite necessary tests.

## 7. Cross-route integration

Subject to independent review of their transfer theorems:

- PR #202 measures the same exponent through negative square-screw excursions;
- PR #208 embeds that scalar in every square-support D-0001 matrix;
- PR #165 supplies the terminal-prime translation philosophy;
- PR #215 turns it into a phase-robust `L^2` energy and a finite prime-pair
  correlation problem.

A proof of the global energy bound simultaneously closes the scalar and matrix
principal-coordinate obstructions. No additional finite cone optimization is
then needed.
