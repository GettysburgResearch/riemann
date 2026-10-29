# Mellin positivity of the physical radial Fourier transform

This is a direct calculation in the quasi-RH manuscript's self-dual normalization, not an assertion of a theta asymptotic or an individual zero-free region. It shows that the nonnegative physical row profile cannot by itself cancel a putative real 5/6 Mellin residue. It does not show that such a residue exists or survives the arithmetic signs.

Let `W∈C_c^∞((0,∞))` be real, nonnegative and not identically zero. Put `w(z)=W(|z|²)` on C. Use the source's additive pairing `e(zy)=exp(4πi Im(zy)/√3)` and self-dual measure `dμ(z)=(2/√3) dx dy`. Its Fourier transform is radial: `ŵ(y)=W̃(|y|²)`. The sign of the Fourier kernel does not affect this radial formula. Set `λ=2/√3`. For every complex s with Re s>0,

    M W̃(s) := ∫₀∞ W̃(x)x^(s−1) dx
      = λπ (π²λ²)^(−s) Γ(s)/Γ(1−s)
          · ∫₀∞ W(t)t^(−s) dt.                              (1)

Consequently

    M W̃(σ)>0   (0<σ<1, σ real),       M W̃(1)=0.               (2)

In particular,

    M W̃(5/6)
      = (2π/√3)(4π²/3)^(−5/6) Γ(5/6)/Γ(1/6)
          · ∫₀∞ W(t)t^(−5/6)dt >0.                           (3)

These inequalities are strict for each fixed W. They do not supply a uniform positive lower bound over arbitrary varying W without an additional normalization/compactness condition.

## Derivation

In Euclidean polar coordinates, the additive pairing acts by a fixed reflection/rotation and scale λ. Integrating the angle and putting t=|z|² gives

    W̃(x)= λπ ∫₀∞ W(t) J₀(2πλ√(xt)) dt.                      (4)

For `0<Re s<1/4`, absolute convergence permits interchanging the two integrals. With `u=2πλ√(xt)` the classical Bessel integral gives

    ∫₀∞ x^(s−1)J₀(2πλ√(xt)) dx
       =(π²λ²t)^(−s) Γ(s)/Γ(1−s).                            (5)

Thus (1) holds in that strip. Since W is compactly supported away from 0, w is smooth compactly supported on the plane, and W̃ is smooth at x=0 and rapidly decreasing as x→∞. Therefore its Mellin integral is holomorphic for Re s>0. The t-integral on the right is entire in s, and Γ(s)/Γ(1−s) is holomorphic for Re s>0. Analytic continuation proves (1) throughout that half-plane. For real `0<σ<1` all displayed factors are positive, giving the first part of (2). At s=1 the reciprocal Γ(1−s) vanishes while the remaining factors are finite, giving the second.

The zero at s=1 also follows from Fourier inversion: w(0)=0 since W is supported away from 0, so the integral of ŵ over C is zero; in radial coordinates that integral is a nonzero constant multiple of M W̃(1). Thus W̃ is not generally nonnegative, despite W≥0.

If an independently proved, fixed-sign spectral or theta contribution factors as a nonzero constant times `M W̃(5/6)`, (3) excludes eliminating it by selecting such a W. Actual physical expressions contain characters, gcd projectors, masks and coupled or Fourier-separated profiles. Their coefficients can be signed or complex, and the Mellin positivity of one unseparated row profile alone does not rule out cancellation among those contributions. At complex s the Mellin transform can have zeros, and the analytic order or existence of any arithmetic pole is a separate issue.

**Independent review.** Literature checked the self-dual scale and measure, Bessel normalization, the absolute-convergence strip and analytic continuation, and positivity/zero statements. The signed physical-kernel limitations remain essential.
