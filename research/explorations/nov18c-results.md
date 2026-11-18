# Analytic attempts to rule out an arbitrary off-line zeta zero

**Status.** This draft investigates the ordinary Riemann hypothesis. It gives a one-sided arithmetic sign test, an extremal theorem for the integer lattice, and a quantitative explanation of how zeros enter an Euler-product approximation. The necessary sign for the actual primes and zero confinement for the extremal transform both remain open. The arguments use no zero census or numerical optimization.

## A sign of an explicit sum would decide RH

Put $a_n=\Lambda(n)-1$, and let $\Theta$ be the supremum of real parts of the nontrivial zeta zeros. Sum over ordered pairs of distinct positive integers:
\[
 C(X)=\sum_{m\ne n}\frac{a_m a_n}{m+n}e^{-(m+n)/X}.
\]
On RH, $C(X)\sim-\tfrac14(\log X)^2$. If there is any off-line zero, $C(X)$ is eventually positive and $\log C(X)/\log X\to2\Theta-1$. Thus even an unbounded sequence with $C(X)\le0$ would settle RH. Restoring the diagonal gives a nonnegative square integral; its growth detects an individual zero including multiplicities and close neighbors. Removing the diagonal subtracts the explicit $\tfrac14(\log X)^2$ main term. The missing fact is that the off-diagonal sum actually takes the required sign. The note tests the factorial identity and root-of-unity averages against this question. The noncoprime component of the centered distinct-index Dirichlet series already has the full line $\Re s=1$ as a natural boundary, independently of RH. The coprime and noncoprime sums carry opposing terms of order $X$. [Sign theorem and arithmetic checks](nov18c-audit.md)

The exact divisor identity at every integer determines $\Lambda$ by Möbius inversion. Its smooth averages have much less force. Conditional on a hypothetical off-line divisor and the stated zero-free strip, one can remove the selected off-line zeros in a comparison Euler product, retain nonnegative integral Euler multiplicities, and preserve arbitrary prescribed finite Laurent data at one and all the stated smooth factorial bounds. These are altered Euler factors at an infinite sparse set of actual primes. The comparison does not have the exact zeta functional equation. If sources agreeing through $P$ did have a locally controlled zero-free continuation, Hurwitz's theorem could transfer that information to zeta. A zero $\rho$ forces the size of every such zero-free continuation to exceed $\exp(P^c)$ on a fixed compact set, for every $0<c<\Re\rho-a$ in the half-plane $\Re s>a$. Under the strip input the best possible compact growth exponent for these comparison families is $\max(\Theta-a,0)$. [Comparison Euler product](nov18c-goldbach.md) · [Quantitative obstruction to taking the limit](nov18c-hurwitz.md)

## What happens in a finite Euler-product proof

We completed and symmetrized the ordinary product over $p\le Y$ and tried to remove its poles. A bounded analytic multiplier on a strip, normalized at a real point $s_0>1$, pays a minimum logarithmic norm $(r-s_0+o(1))Y$, where $r>s_0$ is the right boundary. A Cauchy integral can remove the poles additively and gives locally uniform convergence to $\xi$. Every sufficiently large additive approximant has zeros in the classical Vinogradov–Korobov zero-free region of zeta. The zeros escape to increasing height while the approximants converge on every fixed compact set. [Strip Green function, contour projection and zero count](nov18c-euler-contour.md)

The same obstruction occurs if the reflected Euler-product correction is removed in full. Take any subset of positive integers, let $q$ be its first omission, and build the even transform using the actual Riemann theta summands indexed by that subset. Once $q$ is sufficiently large, the transform has $\gg(\log T)^{5/4}$ zeros in the known zero-free region at height $T+O(\log T)$, where $T=4q^2$. The explicit small tail from that first omission controls one side of a rectangle while the gamma factor controls the opposite side. The result even covers omission of a single term. [Proof for arbitrary subsets](nov18c-theta-cutoff.md)

A separate construction determines which finite polynomial changes of Euler factors a scalar functional equation permits. Some preserve every prime coefficient and finite analytic data while changing a higher prime-power tower and introducing a prescribed zero. Their conductor and prime-power growth are explicit. With the genuine local factors retained, the order of exhaustion of the primes still matters for a partial product in the critical strip. [Finite rigidity and convergence of Euler products](nov18c-rigidity.md)

## What theta extremality decides

Among even positive Fourier-selfdual measures with unit atom at zero and finite reciprocal-square energy $E(\mu)=\int_{x\ne0}x^{-2}\,d\mu(x)$, the integer comb uniquely minimizes energy, with value $\pi^2/3$. Using Cohn and Kumar's Gaussian minorant, the excess energy bounds the difference of the completed transforms uniformly on compact sets in the critical strip. An independently zero-confined family reaching that energy would give RH by Hurwitz. A support gap tending to one already guarantees the required energy convergence.

We tested a direct contradiction: delete a hypothetical quartet at $1/2\pm a\pm i\gamma$ and lower the energy. Its inverse transform develops negative density in the first gap between integers. A positive symmetric average of dilations can repair it. For high quartets the least possible leading relative cost is $\pi^2/(2\gamma^2)$, exceeding the $4/\gamma^2$ leading gain from deletion. An explicit three-point average attains the cost. The comparison rules out this repair as a proof by extremality. [Extremizer, stability and sharp cost of deleting a quartet](nov18c-theta.md)

## Spectral and dilation estimates

| Construction | Analytic conclusion | Unresolved input |
|---|---|---|
| Compressed translation associated to Suzuki's shifted xi quotient | The unsmoothed translation has norm one at every time. With smoothing of order $\alpha$, the operator norm has exact decay exponent $\min(\alpha,3/2-\Theta)$. [Proof](nov18c-shift.md) | Decay at exponent one with one order of smoothing. |
| The same translation in arithmetic coordinates | Its ordinary first-order Hilbert–Schmidt norm has decay exponent $1/2$ irrespective of the zeros. A stronger smoothing detects $3/2-\Theta$ even in that norm. The Hankel kernel is an explicit sum over divisors. [Schatten norms and localized Möbius sum](nov18c-hankel.md) | Cancellation among the actual Möbius coefficients in the remaining multiplicative range. |
| A single compact Weil test | Either translated sign $g\pm\tau_{kh}g$ can be tested for each $k$; positivity of both for every $k$ at any prescribed lattice spacing is equivalent to RH. The proof accommodates exact aliasing among ordinates. [Fixed test and prime shell](nov18c-weil.md) | Uniform accuracy of the smooth prime count in those shells. |
| Euler-sieved Nyman–Beurling approximation | Norm convergence requires $k\log y/\sqrt y\to\infty$ for a signed correction using $k$ arbitrary integer dilations after sieving through $y$. Suitable much shorter corrections already pass the real-axis approximation, while their physical norm diverges. [Sharp local bounds and full norm](nov18c-closure.md) | A correction with bounded norm on the entire half-line. |

These are proposed deductions with proofs in the linked notes. The zero-free strip used for the conditional Euler deformation is documented in the [earlier source audit](nov18b-quasi-rh-source.md).
