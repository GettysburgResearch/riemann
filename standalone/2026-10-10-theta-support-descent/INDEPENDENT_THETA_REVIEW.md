# Independent review of the opposite derivative and fixed angular extension

Review date: 10 October 2026.

Reviewer: the independent `theta_review` research agent. The reviewer did not author `OPPOSITE_DERIVATIVE_REFLECTION.md` or the fixed-angular extension. The reviewer separately authored `ALL_CUSP_REFLECTION.md`; that file is explicitly excluded from this report and requires another reviewer.

Research baseline: PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`. The newly authored files below did not exist at that baseline. The exact byte identities reviewed here are recorded by SHA256, rather than being incorrectly attributed to the baseline commit. The publication validation record must retain the frozen mathematical source commit as well as these hashes.

Imported analytic source: OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, retained locally in the October 7 import. This review treats its explicitly named arithmetic, automorphy, Fourier coefficient and analytic estimates as inputs. It is not a new verification of that imported paper or of its theta automorphy.

## 1. Opposite derivative: exact reviewed object and verdict

File: `OPPOSITE_DERIVATIVE_REFLECTION.md`.

SHA256: `9532f14dc452edf9a50e7ec905e0629c54d510fd9937c5d8c19bcf7dfb4e9ccb`.

**Verdict: pass at the stated source-conditional scope.** The completed standard infinity-cusp negative component is exactly zero beyond the displayed support threshold. The review found no unresolved step in this theorem after its finite Fourier multiplier was clarified. This conclusion applies to the exact inherited transformed weight and the complete cube sum.

The load-bearing calculation was independently reconstructed as follows.

For the source cusp coordinates, the derivative in z at z=0 is `-(bar(c)*v)^(-2) partial_bar-z'`, while the height derivative and the derivative of z' are zero. This gives the scalar `alpha(c)^2`, swaps the input `alpha(ell)` to the dual `bar(alpha(ell'))`, and retains the source Bessel gamma factors. Consequently the functional equation in equation (2.5), including `(Nc)^(-2t)(2*pi)^(4t)R(t)^(-1)`, is correctly normalized.

The reflected Mellin transform is

\[
\widehat{V^\sharp}(t)=\widehat V(-t)R(t)
\bigl((2\pi)^4/27\bigr)^{-t},\qquad \Re t>-5/6.
\]

The shift from `Re(t)=3/4` to `Re(t)=-3/4` stays inside this half-plane. The first possible numerator gamma pole is at -5/6, so no kernel residue is crossed. The differentiated theta Mellin transform is entire because every cusp constant is removed and the remaining modes decay exponentially at both ends. The source functional equation and strip-growth argument supply the polynomial Dirichlet-series bounds needed to combine this shift with the rapid vertical decay of the weight.

The resulting kernel is exactly

\[
\widehat{V^\sharp}(-t)R(t)(2\pi)^{-4t}
=\widehat V(t)27^{-t},
\]

so the second reflection returns `V(27x)`. The factor 27 is necessary. Since a reduced translation denominator satisfies `Nc<=Nq` and the three source frequency sequences are supported on `lambda^(-4)O`, every nonzero dual frequency has norm at least 1/81. These two facts give the raw support condition `X>3R(Nq)^2`, exactly as in (3.3).

The periodic selection in equation (4.1) is an actual selection of Fourier coefficients of the full source theta function. On its support, `m=lambda^3 ell` is good and primary, and the source theta support gives the unique factorization `m=n b^3` with n squarefree and n,b good and primary. The primary condition removes the remaining unit. Thus this multiplier picks precisely the inherited good standard face and retains its entire cube completion. The supplementary factor `vartheta(n)` belongs to `d_0`; it is correctly absent from the finite Fourier multiplier itself.

The norm and phase calculation in the application is also exact:

\[
\alpha(\lambda^{-3})=i,\quad N(\lambda^{-3})=1/27,
\quad X=\frac{(Ng)^2(Nk)^2}{27cB},\quad
S^+_{\phi_k}(X;V^\sharp)=81i\,I_{k,g}.
\]

This proves the stated cutoff `(Ng)^2>81cR(NM)^2B`, uniformly in k, and the balanced all-negative vanishing whenever the lower support endpoint of the outer divisor weight satisfies the displayed condition (4.7). Retaining a general Dirichlet exponent instead of 1/2 gives equation (5.1), `G^+_(phi_k)(s)=i 3^(5/2)27^s T(s,Psi^+)`. Its factor is nonzero and entire, so the continuation applies to that exact formal completed Dirichlet series.

Finally, the normalized finite Fourier transform of `-1+Np*1_(p|x)` is zero at the zero frequency and one at every nonzero frequency. Equation (6.1) and the explanation of restored local activity are correct. The theorem therefore does not claim that reuniting every Ramanujan allocation lowers the conductor of the whole theta sum.

### Scope and first remaining boundary

This review does not establish a bound after removing cube terms, a zero statement for an individual n or b dyad, or an inverse bound for the separate angular Hecke L-function. Those conclusions do not follow by taking absolute values in the completed identity. The full fourth moment, its initial adverse row range, the unbounded hierarchy and RH remain outside this result.

What was actually run: independent hand reconstruction of the coordinate, Bessel, Mellin, finite Fourier and normalization identities; comparison with the local primary source; complete reading of the reviewed file; and SHA256 identification of the exact bytes. No numerical experiment, Lean build, automorphy proof replay or zero computation was run.

## 2. Fixed angular extension

File: `HIGHER_ANGULAR_SECOND_MOMENT.md`.

SHA256: `82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959`.

**Verdict: pass at the stated source-conditional scope.** The derivative, completion, transfer and initialization adapters support the fixed-angular conclusions as stated. The separate conductor-uniform reciprocal argument in Section 6 is also valid under the resulting common zero-free half-plane. This review covers the final distinction between the exceptional canonical parameter and the exceptional full-row inverse parameter; the earlier draft's more restrictive two-sign exclusion is not the statement reviewed here.

### Higher derivatives and the completed estimate

The pure higher derivative formula (1.2) is exact. Holding `bar(z)=0` while taking the pure z Taylor coefficient makes z' and v' constant and makes `bar(z')` affine in z. Every omitted coordinate term retains a factor of `bar(z)`, which cannot be removed by a pure z derivative. Thus there are no lower horizontal derivatives or height derivatives. This reasoning applies to a smooth function of its real coordinates; holomorphy is not required.

The chosen Mellin power `v^(2s+m-2)` gives the gamma factors `Gamma(s+m/2-1/6)Gamma(s+m/2+1/6)`. Multiplication by the Fourier derivative `(2*pi*i*ell)^m` leaves exactly `alpha(ell)^m(Nell)^(-s)` and the scalar `i^m/[4(2*pi)^(2s)]`. The reflected coordinate factor is `(-1)^m alpha(c)^(2m)(Nc)^(1-2s)` for a plus input. Its norm exponent is independent of m. For angular exponent `j=r-1`, the raw coefficient relation is `G_j(s)=i^j 3^(5/2)27^s T_r(s)`, giving the stated primal factor `i^(m+j)` in (2.5). These constants were reconstructed independently.

The first left kernel pole occurs at `-m/2-1/3`. For every fixed `m>=1`, the source kernel shifts and smooth seminorm estimates therefore remain available. The derivative removes all cusp constants. The excluded m=0 case would both retain constants and have a different first kernel pole; it is not covered by this argument.

The reviewer compared Proposition 3.1 with the source's full preparation of its quadratic columns, including `eq:prepared-theta-sum`, `eq:auxiliary-conductor-bound`, `eq:theta-separated-columns`, and `eq:prepared-mean-square`. At each good active prime, the same finite Fourier calculation produces the same local factor. In particular, the varying squarefree row primes still produce `chi_p^3`.

The derivative changes the source angular scalar by a fixed unit-modulus power. Within a fixed auxiliary/active group the source denominator is `c=c_*k_0`, so this change factors into a phase depending on k_0 alone and a fixed auxiliary phase. The new power of `alpha(ell)` belongs to the column coefficient and has modulus one. Thus it neither makes the arithmetic column depend on the row nor changes its magnitude. The prepared amplitude and effective length bounds are unchanged. Fixed ray splits, the repeated-prime masks, the ramified decay and the all-row decomposition `k=u_0 s v^2` retain their source scope. The final convergent v sum therefore yields the same completed mean-square exponents. This is an adapter for a fixed angular order, not an arbitrary coefficient extension of the theta theorem.

### Transfer, initialization and the exact exceptional types

Cube inversion is still a literal multiplicative identity with the coefficient (4.1); every added angular factor has modulus one. Its norm powers, cube cutoff, short-cube estimate and long-cube regrouping are unchanged.

For the two Poisson transfer, the exact residual coefficient identity from PR #913 gives `v(r_0 f'n_1) overline(v(r_0 f'n_2))`. With `v(n)=alpha(n)^r`, complete multiplicativity and modulus one cancel the common factor. The surviving coefficient is exactly `alpha(n_1)^r overline(alpha(n_2)^r)`. Hence the parameter r stays fixed under the transfer, before the source signed local regrouping is performed. No extra finite class expansion of an angular factor is being assumed. The exclusion-removal step uses the unchanged CRT relation. Consequently the source finite induction has the same scales and closes for canonical `r!=1`.

The initial inverse-to-Gauss step has the other sign. The primary source first conjugates the inverse sum. Its paired Gauss identity is therefore multiplied by `alpha(z_1)^(-r)alpha(z_2)^r`, giving precisely `a_(-r,xi)(z_1) overline(a_(-r,xi)(z_2))` in (5.2a). Only the finite ray function is expanded. The common divisor phases cancel at the subsequent splittings. The initial scale ratio remains `Hcal/Sigma << D^(-theta)`, so the canonical theorem applies whenever `-r!=1`, that is, inverse `r!=-1`.

The improved exception statement in the final draft is sound. Inverse r=+1 initializes at canonical -1 and is covered. Inverse r=-1 is not claimed to satisfy the full-row second moment. Its fixed-row sum at u=1 is the conjugate of the covered r=+1 sum with conjugated finite character and weight, as in (5.3b). That identity yields the fixed-row conclusion without changing the row parameter range or asserting an unavailable mean square.

The sixth-power extraction only uses the literal row zeros, the absolute value of the multiplicative coefficients, and the fixed-field prime count. Its inequality (5.3a) agrees with the source: the first contribution is `D^(1+epsilon_0)H^(5/6)` and the puncturing error is `D^2 H^(-1/3)`. The finite smooth seminorm bound survives both terms. Taking a sufficiently small fixed theta gives the stated `11/12+epsilon` exponent. On compact sets of s, the same seminorm estimate applied to `W_s(x)=W(x)x^(-s)` gives normal convergence of the smooth dyadic reciprocal series. Thus the zero-free conclusion at `Re(s)>11/12` follows for every fixed integer type, including the exceptional inverse type through its fixed-row conjugation argument.

### Native conductor-uniform reciprocal estimate

The reviewer also reconstructed the argument that makes the separate reciprocal bound uniform in the finite modulus. It does not assume uniform constants in the preceding fixed-character second moment.

For fixed odd type, unit compatibility gives `psi(-z)=-psi(z)`, including the zero extensions. Therefore psi has zero sum over every complete residue system modulo q. Since the Eisenstein ideal lattice q is a rotated and scaled copy of O, a fundamental cell has diameter `O(sqrt(Nq))`, contains exactly Nq lattice points representing the residue classes, and has constants independent of the orientation of q.

Subtracting the center value of `alpha(z)^r` in a full cell at distance T gives `O_r((Nq)^(3/2)/T)`, because the angular gradient is `O_r(1/T)`. There are `O(T^2/Nq)` cells in a dyadic annulus with `T>=C sqrt(Nq)`, giving total error `O_r(T sqrt(Nq))`. Summing these annuli up to `sqrt(x)`, adding the finitely many central cells and the `O(sqrt(x/Nq)+1)` boundary cells, proves the stated `O_r(sqrt(xNq)+Nq)` ideal sum. The counting bound covers `x<Nq`. Dividing the lattice sum by six correctly accounts for the unit generators of an ideal.

Partial summation then gives the uniform polynomial bound (6.2) on every fixed half-plane to the right of 1/2. For r=+3 and -3, the preceding individually proved zero-free statements hold on a common half-plane `Re(s)>11/12`, for every finite character and every literal imprimitive extension. This common domain supplies an analytic logarithm of L, even though the earlier cancellation constants depend on the character.

Borel–Caratheodory, using the uniformly bounded Euler logarithm at `2+it` and the logarithm of the polynomial growth bound, gives `|log L(a+it)| << log Q` for fixed `a>11/12`, where `Q=Nq(2+|t|)`. The Euler logarithm is uniformly bounded on a fixed line b>1. Applying three-lines to `log L(s)*exp((s-it_0)^2)` gives `|log L(sigma+it_0)| << (log Q)^omega`, with omega strictly below one on each fixed interior half-plane. The Gaussian makes the boundary suprema finite uniformly in t_0. Exponentiation yields the claimed reciprocal `O_(delta,epsilon)(Q^epsilon)`.

The final draft explicitly handles larger delta by the Euler product and the boundary case by a smaller margin. Its modulus includes the finite multiplier and every excluded prime, rather than pretending that the angular coefficient is periodic. Imprimitive Euler factors introduce no zero to the right of zero, and the same logarithm argument applies to the literal imprimitive L-function. For the application `chi^-_(k,eta)`, the finite modulus norm is a fixed multiple of Nk, giving equation (6.6) with every moving k exclusion retained.

### Scope and first remaining boundary

This pass is conditional on the primary source's arithmetic identities, theta automorphy, quadratic sieve, finite descent and source transfer estimates. It does not independently establish those inputs, extend the angular order uniformly with D, prove the missing inverse r=-1 full-row mean square, or improve the prior zeta boundary.

The reciprocal bound holds on `Re(w)>=11/12+delta` for a fixed positive margin. It neither controls the deformed squarefree Gauss coefficients of the reunited Euler product nor supplies their joint continuation or their contour bounds. The canonical theorem retains `Hcal<=Sigma D^(-kappa)` and therefore does not cover the adverse initial higher-moment ratio. These are substantive remaining boundaries, not consequences of the new reciprocal estimate.

What was actually run: complete reading of the final file at the exact hash above; independent reconstruction of the higher derivative, Bessel and normalization calculations; direct comparison with the primary source's completed sieve, cube inversion, initialization and finite transfer interfaces; reconstruction of the lattice-cell discrepancy and logarithm interpolation proofs; and exact SHA256 identification. No numerical computation is used as evidence for these analytic statements.
