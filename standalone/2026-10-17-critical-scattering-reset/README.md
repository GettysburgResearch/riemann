# Critical scattering, a free Mellin variable, and prime-memory stability

**Status: PROPOSED component mathematics and exploratory research. RH is not
proved, and this packet establishes no new zero-free half-plane.** The complete
written arguments, independent agent reads, and finite checks below are offered
for external mathematical review. No claim is promoted to integrated status.

This is a research reset after the proposed all-field `Re(s)>11/12` refinement
in [#959](https://github.com/GettysburgResearch/riemann/pull/959). Its frozen
base is `7b845294207d96b883c1fa95028663082267804f`, root tree
`b93445b2021ecadd032ef8a48214f8bcdcf8fe05`. Only this new standalone directory
is added. The existing theta/Cauchy estimate and its exponent ceiling are taken
seriously: the work here changes the mathematical object being estimated.

After the initial publication, the closing scan found concurrent #960 and
#961. [CONCURRENT_UPDATES.md](CONCURRENT_UPDATES.md) records their growing-shift
theorem, three-way endpoint tie, conditional theta escape and geometric route.
These additions refine the research priorities without changing the component
proofs or supplying their missing arithmetic estimates.

## What the packet establishes

| Component | Written result | Remaining limitation |
|---|---|---|
| [Critical scattering](CRITICAL_SCATTERING.md) | The completed angular quotient is an unconditional inner function. Its stripping operator has an exact gamma smoothing factor, a causal Hardy subspace, and an explicit orthogonal defect. | A bounded boundary operator does not prove that the original arithmetic source belongs to the required space. |
| [Free second Mellin variable](PRINCIPAL_TWO_VARIABLE_FACTOR.md) | The principal residue before the usual second residue has an exact two-variable factorization. Fixing real `z0>1/3` gives a correction and inverse with finite critical convolution mass and no possible target-zero cancellation. | The signed principal-residue projection is not bounded by the inherited theta estimate. Its physical `X` factor must be retained. |
| [Prime-memory equation](PRIME_MEMORY.md) | The literal Gaussian Möbius source satisfies an exact prime-power delay equation and energy identity, with a rigorous all-past truncation bound. | The required lower bound for the signed memory correlation is open. |
| [Pole calibration](POLE_CALIBRATION.md) | A finite Laplace/Gram argument gives sharp limsup energy lower constants for arbitrary zero multiplicity, without a rightmost-zero or spacing premise. | It is a lower bound, not the missing arithmetic upper bound. |
| [Prime detector](PRIME_DETECTOR.md) | An exact Gaussian log-derivative detector has a fully convergent explicit formula and an RH-equivalent boundedness criterion compatible with multiple zeros. | Boundedness is explicitly unproved; the underlying explicit-formula criterion is classical. |
| [Fourier transfer](FOURIER_TRANSFER_AND_COVARIANCE.md) | Uniform additive and quadratic logarithmic cancellation transfers to four coefficient families, with quantitative complete-covariance consequences for growing shifts. | No square-root power estimate or estimate for every individual growing shift follows. |
| [Unstable causal control](SCATTERING_CONTROL.md) | A rational multiplier of modulus one on the boundary can still have an exponentially growing causal solution. | This is a synthetic logical control, not an arithmetic counterexample. |

## The main change of attack

The known angular stripping multiplier is

\[
R(s)=\frac{L(6s-2,\eta)}{L(6s-3,\eta)},\qquad \eta=\theta^6.
\]

For `r=s-1/2`, the exact factorization is

\[
R(r+\tfrac12)=\frac{C_\eta}{(3+6r)^g}\frac1{\Theta(r)},
\qquad
\Theta(r)=\frac{\Lambda_\eta(6r)}{\Lambda_\eta(1+6r)}.
\]

Here `Theta` is inner without assuming GRH. Boundary division by `Theta`
becomes causal exactly on `Theta H^2`; the complementary model-space
projection measures the failure. The proposed new spectral question is to
construct a localization of the actual automorphic source which retains that
divisibility and controls the target-pole terms. The operator theorem alone
does not do so.

A second route avoids the singular stripping operator. Before taking the
usual `z=1/6` residue, keep

\[
P(\xi,z)=
\frac{\zeta_F^S(6z)}{\zeta_F^S(6z+1)}
\frac{L_F^S(6\xi+6z-4,\eta)}{\zeta_F^S(\xi)}J(\xi,z).
\]

At every fixed real `z0>1/3`, this is a nonzero harmless correction times
`1/zeta_F^S(xi)` on the critical half-plane. In particular `z0=1/2` eliminates
the physical factor `X^(1/2-z0)`. A signed square-root estimate for this genuine
principal projection would finish zero exclusion. Such an estimate has not
been obtained. The proof also shows that coefficient completion alone cannot
provide it: the new coefficients and native Möbius coefficients are related
by invertible convolution kernels with finite critical mass.

## A necessary correction to the energy goal

Write the native Gaussian source as

\[
G_{a,t}(x)=\sum_{\mathfrak n}\mu_F^S(\mathfrak n)
(N\mathfrak n)^{-1/2-it}
\frac{e^{-(x-\log N\mathfrak n)^2/(4a)}}{\sqrt{4\pi a}}.
\]

A critical zero of order `m` forces cumulative energy of at least order
`U^(2m-1)` along a sequence. Multiple zeros are known unconditionally for
many Dedekind zeta functions, so a universal `O(U)` native energy claim would
be false. The earlier all-epsilon subexponential target remains appropriate.
This does not refute #952's stated open target or #959's proposed bound.

The companion prime detector replaces `1/zeta` by `-zeta'/zeta` and subtracts
the exact smoothed pole at one. Multiplicity then changes amplitude instead
of pole order. For each fixed field, width and height,

\[
\mathrm{RH}_F\iff P_{a,t}(x)=O(1)
\iff\int_0^U|P_{a,t}(x)|^2\,dx=O(1+U).
\]

This is a correctly calibrated stability target. It is not an established
upper estimate or a new equivalent formulation claimed without precedent.

## Read and reproduce

1. Read [STRATEGY.md](STRATEGY.md) for the research decisions, alternatives
   tested, exact open estimates, and reasons the argument does not close.
2. Read the two operator/Poisson notes, then the prime-memory and detector notes.
3. Read [SOURCES.md](SOURCES.md), [AUDIT_SCOPE.md](AUDIT_SCOPE.md), and
   [REVIEW.md](REVIEW.md) for exact inputs and review boundaries.
4. From this directory run `python replay.py`, or
   `python replay.py --with-probe` to reproduce the finite prime-side sample too.
   [VALIDATION.md](VALIDATION.md) describes what those commands establish.

The component checkers use exact integer/rational arithmetic where stated;
Gaussian quadrature and the sample trajectory use ordinary binary64. Four
component reports were independently rerun in both ordinary and optimized
Python. A hash manifest binds the delivered files. None of these checks
certifies the infinite analytic arguments, the imported quasi-RH papers, an
actual zero census, or RH.
