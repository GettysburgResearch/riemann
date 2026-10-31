# Independent review of the cosine/native continuation

Reviewer: `/root/cosine_final_review`, independent of the manuscript author. This review was performed on the complete files identified below, after reading the manuscript, source ledger, checker, and stored receipt. The reviewer did not edit the manuscript or checker.

**Disposition: no blocking mathematical or implementation defect found within the stated component-theorem scope.** The note does not prove RH, prove that the transformed minima tend to zero, or establish a new zero-free boundary. This is an internal research review, not an external peer-review certification or a formal proof-assistant verification.

## Exact reviewed identities

| File | SHA-256 |
|---|---|
| `COSINE_PHASE_AND_NATIVE_SYNTHESIS.md` | `17b4a55c7cb0845a8f20395d40dbb71fafb1154bf27b01421c4c637db7b9031d` |
| `SOURCES.md` | `d80a792c51286728be9538a8536d6545f7ec195e5eb5229762bf31d743361450` |
| `verify_cosine_native.py` | `bf7a854f2b76e82e57b6e90e273eee35cadc96dbbefa0a0e3e176284990a36cf` |
| `verification_receipt.json` | `8560eaff56b747a5f73cff03855fd50c902ba078d69bec5e64adf315713db2f8` |

Changes to any of these files require checking which conclusions of this review still apply.

## Analytic reconstruction

1. **Whole-strip multiplier and operator normalization.** I rederived the two integrations by parts giving equation (6), including the endpoint conditions `1<Re a<2`. Division gives equation (3) with the stated characteristic-function convention. The gamma/cosine asymptotic has polynomial order `3/2-alpha`, with its exponential factors canceling. The absence of gamma or cosine zeros on `theta+iR`, for `0<theta<1`, supplies the global lower bound. Mellin composition of cosine and inversion gives `W_theta C I W_theta^-1`; at `theta=1/2`, reflection and duplication give the unit-modulus gamma quotient. Direct transformation of the triangular function checks the normalization `T_alpha q_alpha=p_alpha`. The note correctly avoids inferring a multiplication-operator or positivity transfer from this identity alone.

2. **Literal native source and complete norm.** I reconstructed the reciprocal-cell integral, summation by parts, and the finite harmonic-cutoff difference. The surviving term is `y log(n)/n`; removing it would change the source. The isometries, the cancellation `I^2=1`, the Jacobian `dy/y`, the factor `2/pi`, the dilation cocycle, and the cosine-series formula (18) are consistent. Equation (14) is the entire norm with the same finite coefficients, not a finite frequency sampling approximation.

3. **Transported zero-functional and its domain.** The representer of `L_s` is square integrable precisely in the asserted half-plane. At `s=1`, equation (20) is understood through its removable singularity, giving `log(n)/n` as already stated in the text. The smooth extension on the unused negative half-line makes `w_s` Schwartz. Dividing its Fourier transform by the conjugate multiplier leaves an L2 function because the inverse has only polynomial growth. The native regularity lemma supplies the positive-order domain when `alpha<3/2`. The norm obstruction follows by Cauchy–Schwarz. The equivalence asserted for `alpha>=3/2` uses boundedness of `T_alpha` for one direction and the retained zero-functional for the other; the corresponding converse for positive-order `alpha<3/2` is appropriately left unclaimed.

4. **Sobolev regularity and interpolation.** For logarithmic cells of length comparable to `1/k`, the jump contribution to the fractional seminorm is bounded by a constant times `|f(k)|^2 k^(-2+2r)` for `r<1/2`. The cross-cell estimate is valid even for complex values and the infinite sum can be handled by nonnegative integration. Splitting at `ceil(B^2/E)` gives the exponents in (25). Solving the interpolation inequality after inserting this bound gives exactly `B^(4r/(1+2r)) delta^(1/(1+2r))` in (27).

5. **Complete frequency tail.** The even reciprocal-cell extension has exceptional translation measure at most `2Kh+2/K+h`, with `K=ceil(h^(-1/2))`. The stated `8 sqrt(h)` upper bound is valid for `0<h<=1`. With the unitary Fourier convention, its Fourier transform is exactly `C Ef` on the positive axis. Averaging translations through `2/Y` gives a multiplier at least one for `|y|>=Y`; symmetry supplies the factor two. The resulting constant is `32 sqrt(2)/3`, which is less than the advertised 16. Thus equation (28) controls the full omitted frequency range. Equation (31) is a different, valid remainder for the defining generator series, not a substitute for (28).

6. **Möbius synthesis and the remaining gap.** Absolute cubic tails justify the double-series regrouping in (32). I reconstructed the signs and both endpoint sums in (33). The classical Mertens decay quoted in the sources is sufficient, by partial summation, for both endpoint series to converge to their Abel limits. This supplies compact convergence only. The native prefix is exactly `k A_N`, and its energy is `|A_N|^2 (N+1-H_(N+1))`. For an exactly zero prefix, the first difference equation gives `sum c_n/n=1`; Möbius inversion forces `c_n=-mu(n)` through the prefix length. The linear coefficient-budget conclusion and the incompatibility of the two separate safe range bounds therefore follow. No passage from compact convergence to full-norm convergence is made.

## Independent execution

The following were run in separate isolated Python processes:

```sh
python -I -S -B pass2_fresh/verify_cosine_native.py
python -I -S -B -O pass2_fresh/verify_cosine_native.py
```

Both exited successfully and produced output **byte for byte identical** to `verification_receipt.json`, and therefore to each other. The receipt reports 30,783 checks, including one optimization-configuration check. All numerical acceptance comparisons use integers or rational arithmetic; failures raise explicit exceptions rather than relying on removable Python assertions.

The finite checks cover the selected exact arithmetic identities, rational logarithm enclosures, interval overlap checks for selected odd moments, the Möbius prefix formulas, and the scalar simplification of the tail constant. The moment interval-overlap checks alone do not prove their universal identities. The universal analytic conclusions, including the Sobolev, Fourier-tail, and density-equivalence arguments, rest on the manuscript proofs reviewed above.

## Sources and scope

I separately opened [Bagchi's primary preprint](https://arxiv.org/pdf/math/0607733) and checked Theorem 1 against the native weighted space and target used here. I also opened [Burnol's primary preprint](https://arxiv.org/pdf/math/0112254) and the [Lee–Leong primary abstract](https://arxiv.org/abs/2208.06141); the latter explicitly records an unconditional Mertens estimate stronger than the qualitative decay needed here after absorbing a logarithm into a smaller positive exponent constant. This review does not independently certify their full proofs or recent numerical claims. No such numerical claim is imported into the component results.

The manuscript correctly credits the cosine/inversion phase and the native RH criterion as classical. This review does not establish worldwide novelty of the source-specific formulas or estimates. The outstanding mathematical obligation is still a coherent coefficient construction with vanishing **complete** transformed norm and compatible tail control.
