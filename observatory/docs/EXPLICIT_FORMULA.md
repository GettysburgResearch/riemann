# The implemented Gaussian Weil explicit formula

**Status:** classical infinite identity; new finite numerical implementation/scout. No RH assumption is used to promote the returned finite critical-line list to all zeros. No rigorous tail or quadrature error enclosure is supplied by this implementation.

## Exact convention

For real `b` and `a>0`, define

\[
h(t)=e^{-at^2}\cos(bt),\qquad
H(u)=\int_{\mathbb R}h(t)e^{-iut}\,dt
=\frac{\sqrt{\pi/a}}2\left[e^{-(u-b)^2/(4a)}+e^{-(u+b)^2/(4a)}\right].
\]

There is no `2π` in the forward exponential and no normalization in the forward transform. `b` is a logarithmic center. The prime-side transform is concentrated near `log n = b`, with a second even image centered at `-b`.

Writing `ψ=Γ'/Γ` for the digamma function and `Λ(n)` for the von Mangoldt coefficient, the implemented convention is

\[
\begin{aligned}
\sum_\rho h\!\left(\frac{\rho-1/2}{i}\right)
={}& 2e^{a/4}\cosh(b/2)
-\frac{\log\pi}{2\pi}H(0)\\
&+\frac1{2\pi}\int_{\mathbb R}h(t)\Re\psi\!\left(\frac14+\frac{it}{2}\right)dt
-\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}H(\log n).
\end{aligned}
\]

The left sum is over **all nontrivial zeros, with multiplicity**, not merely the critical-line zeros returned by a numerical library. If `ρ=β+iγ`, its argument is `γ-i(β-1/2)`. The Gaussian test is entire, even and rapidly decreasing in every fixed horizontal strip. The prime and zero sums converge absolutely for this test; these convergence facts do not provide the application's finite tail budgets.

## Derivation and normalization check

Use the classical completed meromorphic zeta

\[
\Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Lambda_\zeta(s)=\Lambda_\zeta(1-s).
\]

It has simple poles at `0,1` and nontrivial zeta zeros as its zeros. Let `F(s)=h((s-1/2)/i)`. Evenness gives `F(1-s)=F(s)`. A symmetric rectangle with right edge `Re s=c>1`, the residue theorem, and the functional equation for the logarithmic derivative give

\[
\sum_\rho F(\rho)-F(0)-F(1)
=\frac1{\pi i}\int_{(c)}\frac{\Lambda_\zeta'}{\Lambda_\zeta}(s)F(s)\,ds.
\]

Take heights avoiding zeros before passing to the limit. Gaussian decay suppresses the horizontal edges; the standard logarithmic-derivative bounds on such contours justify the limit. This is the usual explicit-formula argument, not a new theorem claimed by this software contribution.

Expand the logarithmic derivative as

\[
-\tfrac12\log\pi+\tfrac12\psi(s/2)+\zeta'(s)/\zeta(s).
\]

On the right edge, `ζ'/ζ=-Σ Λ(n)n^{-s}` converges absolutely. Fourier contour shifting gives

\[
\frac1{\pi i}\int_{(c)}n^{-s}F(s)ds
=\frac1{\pi\sqrt n}H(\log n).
\]

Shift the gamma/constant part to `Re s=1/2`; there are no gamma poles between these lines. Odd imaginary parts cancel because `h` is even. Finally `F(0)+F(1)=2e^{a/4}cosh(b/2)`. These steps give precisely the four displayed terms and their signs/factors.

**Do not append a separate trivial-zero sum.** The gamma contribution already encodes their effect in this completed-zeta convention. A different explicit formula with a separate trivial-zero series needs a different, independently checked decomposition.

Primary background: [NIST DLMF §25.4](https://dlmf.nist.gov/25.4) for completion/functional equation, and [T. Tao, 254A Supplement 3 (2014)](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/) for the classical contour/explicit-formula framework. The displayed Gaussian specialization and code normalization are written out above rather than inferred from plot agreement. Digamma implementation: [official SciPy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.digamma.html).

## What the finite desk actually evaluates

- Every prime power `p^k <= N`, coefficient `log p`, including `k>1`. Smooth weighting has no endpoint half-weight; `N` is a finite implementation cutoff.
- The first `K` approximate positive ordinates returned by `mpmath.zetazero`, converted to binary64 for the Gaussian weights and paired with factor two. The provider produces no independent complete zero census.
- The gamma integral restricted to `|t| <= T`. Evenness reduces it to `1/π` times the integral on `[0,T]`. Composite Gauss–Legendre panels of length at most one use the specified order, with SciPy complex digamma.
- The elementary pole and log-π terms in binary64.

All five fields `prime_tail_bound`, `zero_tail_bound`, `gamma_tail_bound`, `rounding_bound`, `quadrature_error_bound` are **null**. The discrepancy is simply finite RHS minus finite selected zero sum. It combines all omissions and numerical errors. A tiny discrepancy neither proves all error components are tiny separately nor proves RH.

Working digits affect the initial zero ordinates, not the binary64 Fourier transforms/quadrature. The selected `b` ledger includes every finite prime-power and zero-pair contribution. The visible prime table shows its largest 80 entries; the complete list stays in the exported result. A zero-band view is a literal subset contribution, not an attribution of one zero to one prime.

## Checks and examples

Tests compare the closed-form Fourier transform with independent mpmath cosine integration, and the gamma integral at three centers with independent high-precision mpmath quadrature. Other tests check prime-power enumeration, the exact composition of the displayed ledger, literal zero bands, and a deliberately inadequate prime cutoff that makes the discrepancy large.

For the default finite setup (`a=.015`, `b=log 10`, `N=5000`, `K=24`, `T=100`, order 24), the observed selected discrepancy was about `5.3e-16` on the implementation machine. This is an observed floating diagnostic, not an error bound or a novel result. Changing the environment can change low bits.

Review tasks before any certification claim: an independent mathematical/code review of this normalization; authenticated primitive zero data and completeness scope; outward gamma integration; explicit prime, zero and gamma tails; propagation of rounding enclosures through the entire identity. None is silently assumed by the current plot.
