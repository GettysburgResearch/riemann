# Full Dirichlet-series cancellation does not imply prime cancellation

**Status:** An unconditional abstract counterexample to an inference from a full Dirichlet series to its prime-supported subseries. Its coefficients are not claimed to be sextic Gauss coefficients, multiplicative, or squarefree-supported. It does not rule out a prime estimate using additional arithmetic structure.

Define a(n) for positive integers by

    a(n)= 1  if n is an odd prime,
         −1  if n−1 is an odd prime,
          0  otherwise.

The first case has odd n and the second even n, so the definition is unambiguous. For every real x≥1, with m=floor x,

    Σ_{n≤x} a(n) = 1 if m is an odd prime, and 0 otherwise.      (1)

Indeed each odd prime p contributes the adjacent pair `a(p)=1`, `a(p+1)=−1`. Thus the complete summatory function is bounded by 1. Yet

    Σ_{p≤x} a(p)=π(x)−1 ∼ x/log x,                              (2)

where the minus 1 removes the prime 2. For any fixed nonnegative, nonzero smooth annular W, partial summation and the prime number theorem sharpen this mismatch to

    Σ_n a(n)W(n/Y)=O_W(1),
    Σ_p a(p)W(p/Y)∼ [Y/log Y] ∫₀∞ W(t)dt.                    (3)

The full Dirichlet series has equally strong analytic continuation. For Re s>0,

    A(s)=Σ_n a(n)n^(−s)
        =Σ_{p odd}[p^(−s)−(p+1)^(−s)].                         (4)

The right side converges locally uniformly: for σ=Re s>0,

    |p^(−s)−(p+1)^(−s)|
       = |s ∫_p^(p+1) x^(−s−1)dx|
       ≤ |s|p^(−σ−1).

Its sum is at most `|s|ζ(σ+1)` in absolute value, so A is holomorphic on Re s>0 and has polynomial growth on each fixed vertical line there. The equality with the ordinary n-ordered series holds because the summatory function (1) is bounded, giving convergence there by summation by parts.

Therefore even holomorphic continuation well to the left of 1, polynomial vertical growth, and O(1) cancellation in every fixed smooth full sum do not, by themselves, control the corresponding prime sum. Applying a smooth Mellin shift to a full series can exploit cancellation between prime coefficients and neighboring composite coefficients, as it does exactly in this model. To deduce a ray-sector prime bound from a sextic or cubic full μ-Gauss series requires additional arithmetic input that separates prime coefficients from the rest—such as an Euler-product/logarithmic-derivative identity, a proved bilinear prime decomposition, or independent estimates of the composite terms. The model does not claim those structures are absent or insufficient in the actual Hecke problem.
