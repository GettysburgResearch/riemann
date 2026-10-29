# Why the density and Gram bounds do not yet give an individual region

**Status:** An obstruction to a deduction from the present moment inequalities alone. It is not a counterexample to an additional arithmetic amplification argument, and it does not prove an individual zero-free region.

Let L≥2 be an integer, `0<δ<1`, and let `A` be the L×L Fourier-character matrix `A_jk=exp(2πijk/L)`, with j,k modulo L. Then `A A* = L I` and hence `||A||²=L`. Choose

    λ_k=L^((δ−1)/2) · conjugate(A_0k)/sqrt(L).

We have `||λ||²=L^(δ−1)≤1`, while `(Aλ)_0=L^(δ/2)` and `(Aλ)_j=0` for every j≠0. Thus one row has squared response L^δ, even under the ideal operator bound `||A||²=L`, all entries have modulus one, and every other row vanishes for this coefficient vector. Any upper bound that permits at least one exceptional row, including an `X^(1−δ²/2+ε)` density bound, is compatible with this pattern. In the cubic detector the saturated lower bound at source length D has the form `|M(D)|²≥D^δ X^(−o(1))`, with δ<1; an upper bound of order D or D+R² cannot contradict it for one row. This linear-algebra example demonstrates insufficiency of the inequalities, not that a true Hecke character realizes the example or that a stronger arithmetic argument is impossible.

One might try to replicate an exceptional primitive character by replacing a family label g with `g h^n`. This gives many imprimitive presentations of the same n-th-order character away from primes of h, and their L-functions differ from the primitive L-function by a finite Euler product. For `Re s>0` those deleted factors are nonzero, so the presentations retain the primitive zeros. But the conductor-density family is indexed by n-th-power-free labels, and its sieve count is not a bound for this repeated presentation family. Counting these duplicates as distinct would therefore apply the density theorem outside its hypotheses. Twisting by distinct primitive characters produces genuinely different L-functions, and no zero propagation or analytic closeness sufficient to force the twists to share a zero has been established.

The type of extra pointwise estimate needed can be made precise. Fix a nonprincipal unitary Hecke character ψ and a real θ<1. Suppose that, for every smooth W supported in [1/2,2], uniformly in dyadic D≥1 with a constant controlled by finitely many smooth seminorms of W,

    |Σ_a μ(a) ψ(a) W(Na/D)| ≪_W D^θ.                         (1)

Then `L(s,ψ)` has no zeros in `Re s>θ`. To see this, take a smooth dyadic partition of unity and apply (1) to the compact-family profiles `W(x)x^(−s)` as s ranges over a fixed compact subset of `Re s>θ`. The dyadic blocks of `Σ μ(a)ψ(a)(Na)^(−s)` are `O(D^(θ−Re s))`, so the series of blocks defines a holomorphic function there, locally uniformly. In `Re s>1` it is the Euler product `1/L(s,ψ)`. Analytic continuation identifies the holomorphic function with the meromorphic reciprocal throughout `Re s>θ`, which precludes zeros of L there. Principal pole cases can be treated separately; this statement assumes ψ nonprincipal.

At a target σ, a normalized inverse block bounded by `D^(2σ−1−κ)` in square would amount to an unnormalized bound of size `D^(σ−κ/2)` for the corresponding smooth profile. If such a bound were uniform over all dyadic scales and profiles as in (1), it would already give a zero-free half-plane extending strictly left of σ. The saturated detector only needs a restricted range of scales and allows conductor-dependent powers, so its desired pointwise bound is not literally equivalent to (1); nevertheless, the all-scale comparison identifies the missing strength. The present family-averaged density and Gram results do not supply that pointwise estimate.
