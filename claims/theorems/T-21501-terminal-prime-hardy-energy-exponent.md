# T-21501 — Terminal-prime Hardy-energy exponent

Claim ID: `T-21501`  
Title: One explicit raw prime-power signal has weighted-Hardy and cumulative-energy exponent equal to the rightmost zeta-zero displacement  
Status: `PROPOSED — COMPLETE GLOBAL TRANSFER THEOREM; PRIME-ENERGY BOUND OPEN`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Dependencies: `L-21501`; the classical logarithmic derivative of the Euler product; the Paley–Wiener theorem for Hardy `H^2` on a half-plane  
Cross-route dependencies, not used in the proof: `T-19801`, `L-19802`, `L-20704`

## 1. One fixed finite prime signal

Let `G` be the explicit compactly supported piecewise-linear window of
`L-21501`. Its bilateral Laplace transform

\[
 \widehat G(z)=\int_{\mathbb R}G(u)e^{-zu}\,du
\]

has the following exact properties:

1. `G` is real and supported in one fixed compact positive interval;
2. `\widehat G(1/2)=0`;
3. `\widehat G(z)\ne0` for
   \[
   0<\operatorname{Re}z<\frac12;
   \]
4. on every fixed vertical strip,
   \[
   \widehat G(\sigma+it)=O_\sigma((1+|t|)^{-2}).
   \]

Define the raw prime-power signal

\[
 \boxed{
 Q_G(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
              G(x-\log n).}
 \tag{T-21501.1}
\]

The sum is finite at every real `x`. No zero ordinate, prime cutoff tail,
continuous main subtraction, or spectral approximation occurs in its
definition.

Put

\[
 \Theta_\zeta
 =\sup_{\xi(\rho)=0}
   \left(\operatorname{Re}\rho-\frac12\right).
 \tag{T-21501.2}
\]

The functional equation gives

\[
 0\le\Theta_\zeta\le\frac12.
\]

The endpoint value `1/2` is not excluded a priori: the classical zero-free
line forbids an individual zero on `Re s=1`, but by itself does not forbid a
sequence of real parts approaching one.

## 2. Exact Laplace transform

For `Re z>1/2`, absolute convergence and a change of variables give

\[
\begin{aligned}
 \mathcal LQ_G(z)
 &=\int_{\mathbb R}e^{-zx}Q_G(x)\,dx\\
 &=\widehat G(z)
   \sum_{n\ge2}\frac{\Lambda(n)}{n^{z+1/2}}\\
 &=\boxed{
 -\widehat G(z)\frac{\zeta'}{\zeta}\!\left(z+\frac12\right).}
\end{aligned}
\tag{T-21501.3}
\]

The zero of `\widehat G` at `z=1/2` cancels the pole of `zeta` at `1`.
Every nontrivial zeta zero `rho` with `Re rho>1/2` produces a pole at

\[
 z_\rho=\rho-\frac12.
\]

The zero-free-strip property of `\widehat G` prevents cancellation of that
pole. Therefore the singularities of (T-21501.3) in `Re z>0` are exactly the
shifted off-critical zeros, with multiplicity.

## 3. Weighted `H^2` abscissa

Define

\[
 \sigma_2(G)
 =\inf\left\{
 \sigma>0:
 \int_{\mathbb R}e^{-2\sigma x}|Q_G(x)|^2\,dx<\infty
 \right\}.
 \tag{T-21501.4}
\]

Then

\[
 \boxed{\sigma_2(G)=\Theta_\zeta.}
 \tag{T-21501.5}
\]

### Lower bound

Suppose the weighted integral in (T-21501.4) is finite. For every `u>sigma`,
Cauchy–Schwarz makes

\[
 \int e^{-(u+it)x}Q_G(x)\,dx
\]

an analytic function of `u+it`. It agrees with (T-21501.3) for `u>1/2`, hence
by analytic continuation throughout `Re z>sigma`.

If a zero `rho` satisfied

\[
 \operatorname{Re}\rho-\frac12>\sigma,
\]

then (T-21501.3) would have an uncancelled pole inside that analytic half-plane,
a contradiction. Thus `Theta_zeta<=sigma`, and

\[
 \Theta_\zeta\le\sigma_2(G).
\]

### Upper bound

Fix `sigma>Theta_zeta` and write

\[
 F_G(z)=-\widehat G(z)\frac{\zeta'}{\zeta}\!\left(z+\frac12\right).
\]

The product, not its two factors separately, is analytic on `Re z>=sigma`.
If this half-plane contains `z=1/2`, the apparent singularity there is
removable because `widehat G(1/2)=0` with sufficient order.

Choose finite constants `U>1` and `T>1`. On the compact set

\[
 \{z:\sigma\le\operatorname{Re}z\le U,
       |\operatorname{Im}z|\le T\},
\]

the analytically continued product `F_G` is bounded, including at the removed
pole.

Outside that compact set:

- the line lies a positive horizontal distance from every nontrivial zero;
- standard logarithmic-derivative estimates give polylogarithmic growth in
  `|t|` on each fixed vertical strip away from the removed pole;
- `widehat G` supplies two inverse powers of `|t|`;
- for `u>=U`, the absolutely convergent Dirichlet series for
  `-zeta'/zeta(u+1/2+it)` is uniformly bounded, while the positive support of
  `G` prevents growth of `widehat G(u+it)` as `u` tends to infinity.

It follows that

\[
 \boxed{
 \sup_{u>\sigma}
 \int_{\mathbb R}|F_G(u+it)|^2dt<\infty.}
 \tag{T-21501.6}
\]

Thus `F_G` belongs to Hardy `H^2` of the half-plane `Re z>sigma`.
The half-plane Paley–Wiener theorem supplies one causal `L^2` inverse. On
`Re z>1/2` that inverse has the same Laplace transform as
`e^{-sigma x}Q_G(x)`; uniqueness of the Laplace transform identifies them.
Therefore

\[
 \int e^{-2\sigma x}|Q_G(x)|^2dx<\infty.
\]

Since this holds for every `sigma>Theta_zeta`, the reverse inequality follows.

## 4. Cumulative-energy exponent

Let `x_0` be any number below the support of `Q_G`, and put

\[
 \mathcal E_G(X)
 =\int_{x_0}^{X}|Q_G(x)|^2\,dx.
 \tag{T-21501.7}
\]

For every nonnegative locally integrable function, the abscissa of convergence
of its Laplace integral equals the upper exponential growth exponent of its
cumulative mass. Hence

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
  \frac{\log(1+\mathcal E_G(X))}{2X}.}
 \tag{T-21501.8}
\]

For completeness, if the limsup is `alpha`, then:

- for `sigma>alpha`, integration by parts and
  `E_G(X)<=exp(2sigma' X)` with `sigma'<sigma` prove weighted integrability;
- for `sigma<alpha`, a sequence with
  `E_G(X)>=exp(2sigma'X)`, `sigma'>sigma`, forces divergence because
  \[
  \int_{x_0}^{X}e^{-2\sigma x}|Q_G(x)|^2dx
  \ge e^{-2\sigma X}\mathcal E_G(X).
  \]

This proves (T-21501.8) without a phase or noncancellation hypothesis.

## 5. Full RH criterion

Equations (T-21501.5) and (T-21501.8) give

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal E_G(X)=\exp(o(X)).}
 \tag{T-21501.9}
\]

Equivalently,

\[
 \boxed{
 \mathrm{RH}
 \iff
 e^{-\sigma x}Q_G(x)\in L^2(\mathbb R)
 \quad\text{for every }\sigma>0.}
 \tag{T-21501.10}
\]

This is a phase-robust global criterion. A hypothetical off-line zero forces an
exponentially growing `H^2` energy mode and cannot hide through isolated
cancellation at selected translations.

More generally, a bound

\[
 \mathcal E_G(X)\le C_\varepsilon
 \exp\{(2\theta+\varepsilon)X\}
 \tag{T-21501.11}
\]

for every `epsilon>0` excludes zeros in

\[
 \operatorname{Re}s>\frac12+\theta.
\]

## 6. Three-way global exponent identity

Subject to independent verification of the named cross-branch transfer
claims, `T-19801/L-19802` and `L-20704` give the same invariant in two other
coordinates:

\[
\boxed{
\begin{aligned}
\Theta_\zeta
&=\limsup_{N\to\infty}
 \frac{\log(1+[-\mathscr S(N)]_+)}{2\log N}\\
&=\limsup_{M\to\infty}
 \frac{\log\!\left(
 1+[-\log M\,e_0^TA_{N,M^2}e_0]_+
 \right)}{2\log M}\\
&=\limsup_{X\to\infty}
 \frac{\log(1+\mathcal E_G(X))}{2X}.
\end{aligned}}
\tag{T-21501.12}
\]

Thus the square-screw scalar, the constant D-0001 matrix coordinate, and the
terminal-prime Hardy energy are not competing local routes. They measure the
same global rightmost-zero exponent.

## 7. Proof boundary

Closed here:

- the exact raw-prime Laplace transform;
- cancellation of the zeta pole without cancellation in the open
  counterexample strip;
- equality of the weighted-Hardy abscissa and `Theta_zeta`;
- equality with the cumulative `L^2` growth exponent;
- a single global RH-equivalent prime-energy estimate.

Open:

\[
 \boxed{\mathcal E_G(X)=\exp(o(X)).}
\]

No finite computation or finite positive ladder proves this estimate. The next
attack is arithmetic: use the exact prime-pair Gram identity of `L-21502` to
control the complete off-diagonal multiplicative coherence.
