# Third independent adjudication of the fixed arithmetic sequence reduction

18 November 2026. Both unconditional shifted-divisor arguments and the further reduction to \(C=d_2*(\Lambda\log^2)\) pass. They replace the differentiated nonprincipal reflected edge, in its established compact-local contour formulation, by \(\tfrac12 E_C\) plus errors from the discarded divisor products that decay faster than every fixed power. They give no estimate for \(E_C\). [First derivation](prime98_fixed_arithmetic_sequence.md) · [Independent Mellin derivation and appendix](weighted98_fixed_sequence_review.md)

## Differentiation and the original-modulus average

Start after the saddle weight has become the common shift-independent cutoff \(w_T(2\pi m/k)\). The sum is finite in \(k,m\). In the absolutely convergent series on a common right half-plane, hit the separate factors \(\zeta(s+\alpha)\) and \(\zeta(s+\eta)\) once each. With \(\beta\) still free, this leaves \((k/m)^\beta[m^{-s}]\zeta'(s)^2\zeta(s-\beta)/\zeta(s)\) when \(\alpha=\eta=0\). The remaining derivative either strikes the exterior power, yielding \(\log(k/m)[m^{-s}]\zeta'^2\), or strikes the reflected argument, yielding \([m^{-s}](-\zeta'^3/\zeta)\). The denominator is unshifted, and neither cutoff nor subtraction is differentiated. The mixed derivative is therefore exactly the asserted sum with coefficient \(A(m)+\log(k/m)\sum_{de=m}\log d\log e\), where \(A=d_2*\Lambda*\Lambda*\Lambda\). Taking the real part only after this coefficient extraction agrees with the original one-sided sufficient condition. [Smooth reflected edge](analytic95_pure_fourth_adjudication.md) · [Saddle and shift check](prime96_smooth_saddle_review.md)

For \(q=k/(m,k)\), the map of unit groups modulo \(k\) and \(q\) is onto with equal-size fibers. This follows prime power by prime power and by CRT, including factors of \(k\) absent from \(q\). The remaining numerator \(m/(m,k)\) permutes the units modulo \(q\). Inclusion–exclusion shows that the sum of \(e(u/q)\) over these units is \(\mu(q)\): writing the unit indicator as \(\sum_{d\mid(u,q)}\mu(d)\), only \(d=q\) has a nonzero complete sum. The normalized unit average is unchanged by sign reversal. Thus the projection is exactly \(\mu(q)/\varphi(q)\) on every gcd block and is identically the additive term at \(k=1\).

## First proof of rapid divisor decay

Consider any fixed polynomial of \(\log d,\log e,\log k\) as weight on factorizations \(m=de\), multiplied by \(w_T(2\pi de/k)\). This includes the external factor \(\log(k/m)\). Write \(X=kT\). The smooth two-factor split \(\psi(d/e)+\psi(e/d)=1\), with \(\psi(r)=0\) above 2, puts the designated outer factor at \(d\ll\sqrt X\). After interchanging factors in the second term, its polynomial weight may differ. Both terms have the same bounds. For the function in the other variable \(v\), the support has length \(O(X/d)\) in \(v\asymp X/d\), and each derivative costs at most a constant times \(d/(kH)\) per derivative, up to a fixed log power. Derivatives of the partition and logs instead cost \(d/X\). The compact support is away from zero, so zero extension and integration by parts give
\[
 |\widehat f_{k,d}(\xi)|\ll_B (X/d)(\log T)^D
                    (1+kH|\xi|/d)^{-B}.
\]
With a unit numerator the Poisson frequencies are \(\ell\pm ud/k\). For \(k\mid d\), the full original sum is identical for every numerator and cancels exactly. Otherwise the closest lattice distance is at least \(1/k\), uniformly in the numerator, and the remaining lattice distances grow linearly. Summing for \(B>1\) is bounded by a constant times \((1+H/d)^{-B}\) times the prefactor. Since \(H/d\gg T^{\kappa-(1+\theta)/2}\), a positive fixed power margin, the harmonic sum over \(d\) costs only logs and produces \(O_M(kT\,T^{-M})\) per modulus for any fixed \(M\). The outer sum with \(|a_k|/k\) and \(|a_k|\le24\) costs at most \(O(yT)\) before choosing the decay order. The partition derivative and resonance arguments apply to asymmetric log weights as well.

## Independent Hurwitz and Mellin proof

For a unit \(a\bmod k\), break both positive factors into representatives \(1,\ldots,k\). For the additive twist of \(d_{u,v}(m)=\sum_{de=m}d^{-u}e^{-v}\), this gives the exact finite expression
\[
 Z_a(s)=k^{-2s-u-v}\sum_{r,\ell=1}^k e(-ar\ell/k)
     \zeta(s+u,r/k)\zeta(s+v,\ell/k).
\]
The residue of either factor at argument 1 is one. Summing the pole contribution with the other class fixed picks out only class \(k\) and contributes a factor \(k\). This gives residues \(k^{-1+u-v}\zeta(1-u+v)\) and \(k^{-1+v-u}\zeta(1+u-v)\) for distinct shifts. To check coalescence, write each Hurwitz factor as its pole plus a function regular at argument 1. The product of the two pole terms has class sum \(k\), independent of \(a\). Every product with just one pole restricts the other class to \(k\) and also contributes an \(a\)-independent factor \(k\). The difference of two numerators is therefore jointly holomorphic across both pole loci, including their intersection. There is no leftover residue from the unit-average subtraction or from subsequent Cauchy differentiation.

On \(s=-B+it\) with fixed integer \(B\ge1\) and microscopic shifts, DLMF 25.11.9 applies with its series parameter \(1-s-u\) or \(1-s-v\). Both have real part strictly above 1, so the Fourier series is absolutely convergent including the class with argument 1. For any signed Fourier frequencies \(n,m\) the class sum is exactly
\[
 \sum_{r,\ell=1}^k e((-ar\ell+nr+m\ell)/k)
       = k e(m\,a^{-1}n/k).
\]
The \(r\)-sum enforces \(a\ell\equiv n\pmod{k}\) with a unique class \(\ell\) and requires no coprimality for the frequency \(n\). The remaining two Fourier series of absolute values are bounded uniformly on the shift disks. Stirling cancels the exponential factors from cosine expansion and gives \(|Z_a(-B+it)|\ll_B k^{1+2B+O(1/\log T)}(1+|t|)^{1+2B+O(1/\log T)}\), uniformly in the unit numerator. [DLMF 25.11.9 and domain](https://dlmf.nist.gov/25.11.E9)

For \(M=kT\) and \(\delta=H/T\), a cutoff \(F_k(x)=w_T(2\pi x/k)\log^j(k/x)\) with fixed \(j\ge0\) has Mellin transform bounded on this line by
\[
 \ll_{B,R,j} M^{-B}(\log T)^j(1+\delta |t|)^{-R}.
\]
This follows by differentiation in \(\log x\) on a fixed-length log-scale support. Move the numerator-minus-average integral to the left line after exact polar cancellation, using polynomial strip growth from the finite Hurwitz formula and rapid Mellin decay. Integration for \(R>2B+3\) produces
\[
 \ll_B (\log T)^j k\delta^{-2}(kT/H^2)^B.
\]
The microscopic exponent losses from integrating the power of \(1+|t|\) are bounded because \(k\) and \(\delta^{-1}\) are at most powers of \(T\). Differentiating any fixed number of times in the shifts via Cauchy adds only powers of \(\log T\). The finite outer sum also costs only powers, while \(kT/H^2\ll T^{1+\theta-2\kappa}\) uniformly. This proves the same arbitrary decay as the elementary hyperbola argument. The positive exponent margin is needed in both proofs. The inherited compact-local saddle construction permits this margin for its controlled two-transition tapers, or one may retain the coarser established range \(\kappa>(2+\theta)/3\).

## Reduction to the single Mangoldt convolution

Write \(L=\zeta'/\zeta\). Then \(\zeta''=\zeta(L'+L^2)\) and \(\zeta'''=\zeta(L''+3LL'+L^3)\) give
\[
 \zeta\zeta'''-3\zeta'\zeta''=\zeta^2(L''-2L^3).
\]
The absolutely convergent Dirichlet series of \(-\zeta^2L''\) is precisely that of \(C\) because two derivatives multiply a Dirichlet coefficient by \((\log n)^2\). Thus \(-\zeta'^3/\zeta=\tfrac12(-\zeta^2L''+\zeta\zeta'''-3\zeta'\zeta'')\), also coefficientwise. The two discarded derivative products have weights \(-\log^3 e\) and \(-\log d\log^2 e\) and fit either divisor argument. The extra derivative of \((k/m)^\beta\) was removed separately and introduces no prefactor into \(C\).

Let \(E_B\) denote the complex signed compact-local sum with sequence \(B\) and the same \(a_k/k\), cutoff and original-modulus subtraction throughout. Linearity gives \(E_A=\tfrac12 E_C+O_N(T^{-N})\) for every fixed \(N\) before taking the real part. This arbitrary decay is for the discarded divisor sums. The inherited contour and saddle errors retain their previously proved bounds. No new polar contribution occurs in this difference, and the remaining sufficient condition \(\Re E_C=o(T\log^4 T)\) remains open. No canonical records were changed.
