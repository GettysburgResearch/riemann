# Independent review of the cofinal companion component

Reviewer: `/root/cofinal_final_review`, a separate reviewing agent from the component author. Review completed 2026-10-31 in the session's user date. Status: **no blocking mathematical or implementation defect found in the reviewed component**. This is a mathematical review and an exact finite replay, not a formal verification or a proof of RH.

## Frozen scope

The review binds these exact SHA-256 digests:

| File | SHA-256 |
|---|---|
| `COFINAL_COMPANION.md` | `2a66e0ebe6cd9654162e0c1505e478a0ccf4b740f0854192dc34ed6c076116fc` |
| `verify_companion_structure.py` | `a6b840b7c6a96eb7de8f86127e37b25b899e581d1a72ed3d6a8d73375cf29a17` |
| `STRUCTURE_CHECKS.json` | `8f0822b2de165dbb2d70e6afdb745e40f9d9ee96009437cf2f3c34934dee907e` |

The source normalization and order reduction were checked against the preceding frozen packet, `2026-10-30-operator-theta-swarm`, on PR #1026 at commit `11b4f6612275955a1fddb5c53f67dc21124783f8`:

| Dependency | SHA-256 |
|---|---|
| `theta/PROOF.md` | `35b85c39bec2c69f5cffba0986bf61c416d873696829479cc00737cb94b55f37` |
| `theta/BESSEL_BOUNDARY.md` | `c2e2d3a9db19238d7e802b9f1288546e115d0f6430eb05358ccf4ea92b44498a` |

The reviewer read the entire companion manuscript and checker, reconstructed the principal analytic steps, and consulted the source normalization and boundary reduction. The current DLMF statements for the modified-Bessel integral, Wronskian, and large-argument expansions were also read. The reviewer did not author or edit the component manuscript or checker. Edits to any bound file require a renewed review of the changed claim.

## Reconstructed analytic checks

### Source normalization and the closed-strip estimate

The limiting half-line integral in the manuscript is exactly `Xi(2 sqrt(E))`: the substitution `t=2u` and evenness of the theta kernel supply the required factor of two. The radial derivative in the boundary reduction is `a*d/da`, with the sample coefficients held fixed when applying the differential operator.

For the strip endpoint `x=i`, put `v=x-i` and `epsilon=x+sqrt(1+x^2)-i`. Within the closed strip, `v` is in the lower half-plane. Consequently `sqrt(2iv+v^2)` lies in a fixed right sector for sufficiently small `v`; adding `v` does not destroy the uniform bound `Re(epsilon)>=c|epsilon|`. Gaussian Poisson summation at the odd theta cusp therefore gives exponential flatness in `1/|epsilon|`, with all fixed derivative losses absorbed by that exponential. The same argument applies at `-i`. Together with the literal theta-series tails on the horizontal lines, this justifies the contour shift to strip height exactly one and the subsequent integrations by parts. The resulting endpoint Fourier estimate includes every polynomial weight used by the angular cancellation argument.

This check does not infer analytic continuation across either cusp. Infinite flatness in the relevant closed sector is the property needed here.

### Quantitative full-source approximation

The tilted Skellam distribution has mean `a*sinh(2t)` and variance `a*cosh(2t)`, so its first-order Taylor term has zero expectation before the good/bad-event split. On the good event, exponential decay of the actual second derivative supplies the integrable source tail. On the bad event, the displayed centered moment generating function, evaluated at `+/-1/10`, gives the stated probability bound with exponent `as/40`; Cauchy-Schwarz gives the first absolute-moment bound. The remaining factors of `a` and `s` can be absorbed by splitting the exponential, yielding an integrable error of order `1/a` uniformly for `a>=1`.

The finite-cutoff estimate retains the complete omitted source sum. Its two inequalities in `a` follow respectively from the positive series for `cosh` and the monotonicity of `a(1-exp(-c/(2a)))`. The resulting majorant remains integrable after multiplication by every fixed exponential in `|t|`. Thus the cofinal schedule in the manuscript controls the complete kernel, rather than a finite theta prefix or a bounded sampling interval.

### Companion limit and the angular cancellation

Averaging the standard integrals for `I_nu` and `I_-nu` produces the **positive** sine-times-sinh term in the companion formula. Applying the finite Chebyshev operator at fixed weights gives the stated exact two-integral representation.

For the full angular sum, Fourier inversion and the Bessel generating function give the exponential `a[cos(theta)-cos(theta+omega/a)]`. Both this exponent and its limit `omega*sin(theta)` are at most `|omega|`. Their difference is bounded by `omega^2/(2a)`. The endpoint Fourier estimate therefore supplies a common integrable majorant and the uniform `1/a` error, including `theta=pi/2`.

The cutoff estimate follows from the positive generating-function bound with `h=arsinh(M/a)`. The exponent is precisely `a H(M/a)`. Since `H'(S)=-arsinh(S)` and `H(3)<0`, it decays along every stated cofinal sequence. The evenness in order of both integrals makes the companion entire in energy; reality on the real axis follows from conjugation.

The manuscript's warning about the sign of the angular source is consistent with its cusp expansion. Along `Y=exp(i theta)` approaching `i`, the leading theta-derivative term has negative real phase after the power of `Y`, the power of `epsilon`, and `exp(-pi/(4 epsilon))` are combined. No unproved positivity of this angular kernel is used.

### Wronskian identities, zero pairing, and residues

The radial Wronskian is `y*dot(u)-dot(y)*u=1`. Direct inversion gives both normalized cancellation identities and

`r = dot(u)/u + J/(u^2 D)`, where `D=-B/u`.

The large-positive-argument expansion has `u ~ exp(a)/sqrt(2*pi*a)` and `y/u ~ pi*exp(-2a)`. These signs and constants agree with the manuscript. Uniform compact-order expansions and Cauchy estimates provide the required energy derivatives. Rouché's theorem can therefore be applied to the normalized polynomials on fixed compact domains, retaining multiplicities.

At a simple target zero, the unique nearby zeros converge to that target and the derivatives converge to the nonzero derivative of the source transform. Expanding `D=F-(y/u)J` gives the separation at scale `exp(-2a)`. The exact residue formula then gives the additional factor `2*pi*a`. The manuscript explicitly requires a nonzero limiting companion value before concluding a genuine pole or its eventual sign; no common factor is discarded.

For the uniform imaginary-part quotient away from target-zero neighborhoods, the two-case argument is valid. If the imaginary part is bounded below, the absolute estimate suffices. If it is small, the vertical segment to the real axis stays uniformly separated from every target zero, and a derivative bound controls the quotient. This also handles the holomorphic remainder in the growing Weyl function. It supplies no sign conclusion inside the excluded zero neighborhoods.

### Negative energy and the exact companion controls

The order recurrence has nonnegative coefficients for the `P_n` family and nonpositive coefficients for `Q_n`. Taking their even parts and substituting `nu^2=-E` preserves these signs for `E<=0`. The actual positive `c_0` and `c_1` make `A>0` and `B<0` strict for `M>=1`. The decaying Bessel integral makes its Weyl function negative on the same axis. The separate `M=0` case is harmless.

The appendix's integration by parts was reconstructed independently. With `h(t)=exp(t/4)*theta(exp(t))` and `k=h-exp(t/4)`, one has `g=2h''-h/8=2k''-k/8`, `h'(0)=0`, and `k'(0)=-1/4`. The flat angular endpoint and decaying real endpoint leave the boundary term `-2*nu*sin(pi*nu)`. At `nu=1/4`, the integral coefficient vanishes and gives exactly `J_infinity(-1/16)=-1/(2*sqrt(2)*pi)`. The folded cosine factor supplies the negative-energy zeros. These zeros, and the alternating reduced-quotient values, correctly exclude the two proposed global anti-Herglotz shortcuts without deciding the required positive-energy signs.

## Exact replay

Both commands were executed independently:

```sh
python -I -S -B verify_companion_structure.py
python -I -S -B -O verify_companion_structure.py
```

Both returned `PASS`, and their stdout was byte-identical to each other and to the bound `STRUCTURE_CHECKS.json`. The receipt includes 24 independent order-versus-differential recurrence equalities, 48 coefficient-sign checks, three explicit low-order formulas, exact positive-series remainder bounds for the concentration constants, and the special-value ODE factor. All acceptance decisions use exact rational arithmetic and explicit exceptions; optimization does not remove them.

The finite replay corroborates the algebra and constants. It does not certify the infinite-dimensional analytic arguments, evaluate every residue, prove simplicity of all target zeros, or exclude any nonreal target zero. Ordinary diagnostic programs and their numerical values were not used as proof premises in this review.

## External identities checked

- [NIST DLMF 10.32.4](https://dlmf.nist.gov/10.32.E4): modified-Bessel integral used to derive the symmetric growing-solution formula.
- [NIST DLMF 10.28.2](https://dlmf.nist.gov/10.28.E2): Wronskian and its radial normalization.
- [NIST DLMF 10.40](https://dlmf.nist.gov/10.40): large-positive-argument expansions. The manuscript additionally explains the needed compact-order uniformity through its integral formulas.

The component remains a proposed source-specific analytic development. A theorem proving the needed companion residue signs at all relevant zeros, together with independent exclusion of nonreal target zeros or an adequate expanding local gate, is absent and is correctly identified as remaining work. Worldwide novelty is not established by this review.
