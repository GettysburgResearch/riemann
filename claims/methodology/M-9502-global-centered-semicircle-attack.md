# M-9502 — Global centered-spectrum attack through semicircle totient geometry

Claim ID: `M-9502`  
Title: Replace shrinking finite positivity gates by one full RH-scale arithmetic decay problem  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9506`, `L-9507`, `T-9501`; connection to `T-19801`--`T-19802` and `L-15428`--`L-15432`  
Scope: repository-wide full-problem attack plan  
Related counterexample candidates: none

## Strategic reset

The repository contains many correct finite positivity, Schur, packet, and
certificate interfaces. Their repeated final obstruction is an escaping or
centered spectral mode. Enlarging another finite packet does not change that
fact.

The new attack centers the arithmetic transform **before** optimization and
attacks the exact decay exponent carrying the full zero set.

Define

\[
\mathcal E(x)
=\frac2x\sum_{n<x}\frac{\varphi(n)}n
 \sqrt{1-\frac{n^2}{x^2}}
-\frac3\pi.
\tag{M-9502.1}
\]

Then `T-9501` proves

\[
\boxed{
\mathrm{RH}
\iff
\mathcal E(x)=O_\varepsilon(x^{-3/2+\varepsilon})}
\tag{M-9502.2}
\]

and the best excess exponent is exactly the horizontal displacement of the
rightmost zeta zero.

This is the primary attack target.

## Why this target absorbs the existing programs

### Square-screw program

`T-19801`--`T-19802` encode the rightmost-zero displacement in the positive
excess of a logarithmic von-Mangoldt Riesz mean. `T-9501` encodes the same
quantity in a semicircle-smoothed totient error:

\[
\vartheta_{\rm screw}
=\vartheta_{\rm semicircle}
=\Theta_\zeta.
\tag{M-9502.3}
\]

The two arithmetic observables use different coefficients and smoothing.
Agreement of their measured exponent is a theorem, not a numerical analogy.

### Jordan/Volterra/de Branges program

`L-9506` proves that the full safe one-Green completed ratio is positive
unconditionally. Its centered regular density is the Jordan/Volterra quantity
`Y_s` of `L-15430`--`L-15431`.

At the endpoint `s=1`,

\[
Y_1(\log x)-\frac{12}{\pi^2x}
=\mathcal E(x)+O(x^{-3}).
\tag{M-9502.4}
\]

Thus the operator program's centered Green density and the finite arithmetic
observable have the same full RH exponent.

### Xi-logarithmic-derivative and Pick routes

The Mellin transform of `E` is

\[
B(z/2,3/2)\frac{\zeta(z)}{\zeta(z+1)}
-\frac{3/\pi}{z-1}.
\tag{M-9502.5}
\]

Its poles are exactly the shifted zeros `z=rho-1`, without cancellation. This
is the same resolvent geometry exposed locally by the `xi'/xi` scalar, Pick,
and shifted-Stieltjes criteria, but compressed into one real arithmetic
function.

## Three simultaneous attack fronts

### Front A — Bessel–Möbius cancellation

Use the exact identity from `L-9507`:

\[
\begin{aligned}
\mathcal E(x)
={}&-\frac\pi2\sum_{d\ge x}\frac{\mu(d)}{d^2}
-rac1x\sum_{d<x}\frac{\mu(d)}d\\
&+\frac1x\sum_{d<x}\frac{\mu(d)}d
 \sum_{\ell\ge1}\frac{J_1(2\pi\ell x/d)}\ell.
\end{aligned}
\tag{M-9502.6}
\]

The task is to bound the **combined** expression at scale
`x^(-3/2+epsilon)`, retaining cancellation among the tail, zero-frequency, and
Bessel channels.

Priority techniques:

1. dyadic bilinear decomposition in `d` and `ell`;
2. Voronoi/Poisson treatment of the complete Bessel series;
3. exponent-pair or spectral large-sieve estimates for the reciprocal phase
   `ell*x/d`;
4. exact summation by parts against the Mertens measure;
5. two-implementation directed checks of every proposed finite inequality.

### Front B — Visible-lattice/Farey geometry

The kernel is the vertical chord of the unit disk and `phi(n)` counts reduced
residues. Seek a direct discrepancy theorem for primitive lattice directions
under this radial chord weight.

A successful geometric proof must reach an additional factor `x^(-1/2)` beyond
the unconditional area-error scale. Potential tools include:

1. primitive-point Poisson summation;
2. Farey equidistribution with smooth radial weights;
3. spectral theory of the modular surface;
4. transfer operators or horocycle mixing with explicit Sobolev norms;
5. a trace formula in which the zeta-zero poles appear as the complete
   nontrivial spectrum.

This front is deliberately global: the target is not a fixed matrix or bounded
height.

### Front C — Dual-transform comparison

Evaluate the square-screw scalar and the semicircle error on matched scales.
Use one transform to control phase regions where the other kernel is weak.

The proof objective is a transform inequality of the form

\[
|\mathcal E(x)|
\le \mathcal T[\text{square-screw centered error}](x)
+O(x^{-3/2-\delta}),
\tag{M-9502.7}
\]

or the reverse. A positive-kernel transference between the two would allow a
bound proved in either arithmetic representation to close both.

No such transference inequality is currently proved; it is a high-priority
research target.

## Computation as theorem discovery, not proof replacement

The production experiment should:

1. compute exact integer `phi(n)`;
2. evaluate the semicircle weights with directed balls;
3. preserve `x^(3/2) E(x)` on logarithmic and adversarial grids;
4. compare against the first known zero contributions from the Mellin explicit
   formula;
5. fit no model into the proof object;
6. export any discovered inequality as an exact kernel statement with a separate
   checker.

A long finite run cannot prove (M-9502.2). Its purpose is to identify a
uniform analytic inequality, a transform domination, or a counterexample to a
proposed shortcut.

## Latest-literature connection

Recent work on smoothed summatory totient functions develops truncated Perron
formulae and emphasizes that smoothing depth controls the zero-driven error.
Recent generalized-totient criteria likewise encode zeta zeros as poles of
arithmetic Dirichlet series. The present criterion fixes a specific semicircle
kernel whose Mellin transform:

- has no zero at any shifted nontrivial zero;
- gives the exact `-3/2` RH exponent;
- is already the endpoint kernel of the repository's Jordan/Volterra program.

No literature-priority claim is made.

## Closed shortcuts

The following are not sufficient:

1. positivity of the uncentered safe one-Green kernel;
2. finitely many small values of `E(x)`;
3. separate absolute bounds on all three lines of (M-9502.6);
4. a floating fit to `x^(-3/2)`;
5. finite-height verification of zeta zeros;
6. increasing the dimension of an unrelated positive packet.

## SERIOUS RESOLUTION PATH

A serious full-resolution path is present:

\[
\boxed{
\text{prove }
\mathcal E(x)=O_\varepsilon(x^{-3/2+\varepsilon})
\text{ by Bessel--Möbius or visible-lattice analysis}.}
\tag{M-9502.8}
\]

This one statement proves RH directly by `T-9501`. There is no additional
operator limit, packet exhaustion, Schur complement, source conditioning, or
finite-versus-global bridge after it.

The exact blocker is therefore not another finite matrix sign. It is the
uniform RH-scale cancellation of the complete centered semicircle observable.
