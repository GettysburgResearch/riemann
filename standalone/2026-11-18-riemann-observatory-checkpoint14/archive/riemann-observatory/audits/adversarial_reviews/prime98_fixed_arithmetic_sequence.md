# The smooth fourth-order twist reduces to one fixed coefficient sequence

18 November 2026. Assume RH for the compact-local contour reduction in analytic95 and prime96. Its three auxiliary shifts can be differentiated out before estimating the reflected nonprincipal term. The differentiated term separates into a shifted-divisor contribution that is negligible by elementary Poisson summation, and a single fixed arithmetic convolution whose signed sum remains open. The Poisson argument itself is unconditional. [Smooth contour reduction](analytic95_pure_fourth_adjudication.md) · [Independent saddle check](prime96_smooth_saddle_review.md)

## Exact differentiation and the unit average

Use \(T\asymp Y\), \(\theta=4b\), \(y=Y^\theta\), \(a_k=[k^{-s}]D(s)^4\), and the real compact time cutoff \(w_T\) of transition width \(H=T^\kappa\), where \((1+\theta)/2<\kappa<1\). The original exponent \((2+\theta)/3\) is also admissible. In the reflected edge, after saddle replacement, write
\[
 {\cal E}(\alpha,\beta,\eta;T)
 =\sum_{k\le y}\frac{a_k}{k}
 \sum_{m\ge1} w_T(2\pi m/k)\,R_k(m)\,(k/m)^\beta
 [m^{-s}]\frac{\zeta(s+\eta)\zeta(s+\alpha)\zeta(s-\beta)}{\zeta(s)},
\]
where
\[
 R_k(m)=e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))},
 \qquad e(v)=e^{2\pi i v}.
\]
In the notation of the source, the shift \(\beta\) is the shift belonging to the reflected zeta factor. Interchanging the outer shifts on this edge does not change the mixed derivative. The cutoff has already been made independent of the complex shifts by the smooth saddle comparison. The sums over both \(k\) and \(m\) are finite. Thus differentiation is term by term, and at zero the mixed derivative of the coefficient contribution is precisely
\[
\begin{aligned}
 &\left.\partial_\alpha\partial_\beta\partial_\eta
 \left((k/m)^\beta[m^{-s}]
  \frac{\zeta(s+\eta)\zeta(s+\alpha)\zeta(s-\beta)}{\zeta(s)}
 \right)\right|_0\\
 &\hspace{10mm}
 =\log(k/m)\,[m^{-s}]\zeta'(s)^2
   +[m^{-s}]\Bigl(-\frac{\zeta'(s)^3}{\zeta(s)}\Bigr).
\end{aligned}
\]
In particular only one lower-order term survives the actual mixed derivative. It arises when the \(\beta\) derivative hits \((k/m)^\beta\). The derivative on \(\zeta(s-\beta)\) has a minus sign. No differentiation of the cutoff or the principal subtraction occurs in this comparison. With \(d_2=1*1\) and \(\Lambda\) the von Mangoldt function,
\[
 [m^{-s}]\zeta'(s)^2=\sum_{de=m}\log d\,\log e,\qquad
 [m^{-s}]\left(-\frac{\zeta'(s)^3}{\zeta(s)}\right)
 = A(m):=(d_2*\Lambda*\Lambda*\Lambda)(m)\ge0.
\]
The second identity follows in the absolutely convergent half-plane from \(-\zeta'/\zeta=\sum_n\Lambda(n)n^{-s}\).

The subtraction is exactly a unit average on the original modulus:
\[
 \frac{\mu(k/(m,k))}{\varphi(k/(m,k))}
 =\frac1{\varphi(k)}\sum_{\substack{u\bmod k\\(u,k)=1}} e(um/k).
\]
To see this for every gcd block, put \(g=(m,k)\) and \(q=k/g\). The map of unit groups modulo \(k\) onto the unit group modulo \(q\) is surjective by prime-power lifting and the Chinese remainder theorem. All fibers of the surjective homomorphism have equal cardinality. Since \(m/g\) is a unit modulo \(q\), the normalized sum is the normalized Ramanujan sum at a unit, equal to \(\mu(q)/\varphi(q)\) by inclusion–exclusion. This includes \(q=1\). No squarefreeness assumption on \(k\) or \(m\) is used.

## Uniform cancellation of the divisor term

For a fixed \(k\le y\), set \(X=kT\) and write the \(\zeta'^2\) coefficient as a sum over \(d,e\ge1\) with \(de=m\). Its smooth multiplier is
\[
 W_k(d,e)=\log(k/(de))\log d\,\log e\ w_T(2\pi de/k)
\]
and has \(de\asymp X\). Choose a smooth partition \(\psi(r)+\psi(1/r)=1\) on positive \(r\), with \(\psi(r)=0\) for \(r\ge2\). Inserting \(\psi(d/e)+\psi(e/d)\) and interchanging \(d,e\) in the second half represents the sum by twice the half with \(\psi(d/e)\). This symmetry uses the exact log factors of \(\zeta'^2\). In either half the designated outer factor satisfies \(d\ll\sqrt X\).

For such \(d\), define \(f_{k,d}(v)=\psi(d/v)W_k(d,v)\) for \(v>0\) and extend by zero. Its support is contained in \(v\asymp X/d\). Throughout the support, derivatives of \(\psi(d/v)\) and of the logs cost powers of \(d/X\). Derivatives of the cutoff cost \(O_j((d/(kH))^j)\) by the chain rule. Since \(H\le T\), the combined bounds and integration by parts give, for any fixed integer \(B\),
\[
 |\widehat f_{k,d}(\xi)|
 \ll_B (X/d)\log^3 T\, (1+ (kH/d)|\xi|)^{-B}.
\]
The implied constants are independent of \(d,k,T,Y\), including when the partition vanishes on all or part of the support. For a unit \(u\bmod k\), standard Poisson summation with Fourier convention \(e(-v\xi)\) gives
\[
 \sum_{e\in\mathbb{Z}} f_{k,d}(e)e(ude/k)
 =\sum_{\ell\in\mathbb Z}\widehat f_{k,d}(\ell-ud/k).
\]
If \(k\mid d\), the sum on the left is independent of \(u\) exactly and cancels under the unit-average subtraction, including all its nonzero modes. If \(k\nmid d\), every \(|\ell-ud/k|\) is at least \(1/k\), uniformly over unit \(u\), and all but at most two terms have distances of order \(1,2,\ldots\). For \(B>1\), the sum is consequently
\[
 \ll_B (X/d)\log^3 T\, (1+H/d)^{-B}.
\]
For example, terms of distance at least a fixed positive constant contribute \(O_B((kH/d)^{-B})\) times the prefactor, which obeys the same bound. This works at all rational numerators appearing in the full modulus average. It does not require a formula restricted to \((m,k)=1\).

Because \(d\ll\sqrt X\ll T^{(1+\theta)/2}\), the quantity \(H/d\) grows at least as a fixed positive power of \(T\). Summing over \(d\) costs only its harmonic sum, giving \(O_M(XT^{-M})\) for the difference between any unit-twisted sum and its unit average, for any fixed \(M\). Thus the entire divisor contribution, even in absolute value after summing over \(k\), is
\[
 \ll_M \sum_{k\le y}\frac{|a_k|}{k}\,kT\,T^{-M}
 \ll_M yT^{1-M}
\]
using \(0\le a_k\le24\). This yields arbitrary power saving at fixed \(\kappa>(1+\theta)/2\). The same argument covers any fixed additional polynomial in the logarithms of the two factors and of \(k\). A shifted Voronoi formula is unnecessary for this conclusion. The only Fourier identity used is classical Poisson summation on a compact smooth function, applicable here to each positive support \(v\asymp X/d\).

## Remaining compact-local estimate

The exact remaining sufficient input for the real fourth cosine moment is
\[
 \Re\sum_{k\le y}\frac{a_k}{k}
 \sum_{m\ge1} A(m)\,w_T(2\pi m/k)
 \left[e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}\right]
 =o(T\log^4T).
\]
The other edge has modulus 1 and no nonprincipal term. The two complex shifts and the auxiliary ratio shift are only needed for the established contour comparison and its formal principal residue extraction. They no longer need to be retained in the fixed coefficient sequence or in the remaining estimate. The fixed arithmetic sequence is nonnegative, but the signed kernel still requires cancellation. In particular the two-factor Poisson proof depends on a smooth unrestricted long factor and cannot be applied directly to a variable carrying \(\Lambda\). Neither the remaining estimate nor the fourth moment is established here. [One-sided principal residue and strict tail transfer](prime90_pure_fourth_bottleneck.md) · [HLZ primary source, §§4–6](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## Further reduction to a single von Mangoldt factor

Let \(L(s)=\zeta'(s)/\zeta(s)\). The quotient rule gives
\[
 L'=\frac{\zeta''}{\zeta}-\frac{\zeta'^2}{\zeta^2},
 \qquad
 L''=\frac{\zeta'''}{\zeta}
       -3\frac{\zeta'\zeta''}{\zeta^2}
       +2\frac{\zeta'^3}{\zeta^3}.
\]
Multiplying by \(\zeta^2\), rearranging, and putting \(C(s)=\zeta(s)^2(-L(s))''\) yields
\[
 -\frac{\zeta'(s)^3}{\zeta(s)}
 =\frac12\left(C(s)+\zeta(s)\zeta'''(s)-3\zeta'(s)\zeta''(s)\right),
 \qquad
 [m^{-s}]C(s)=(d_2*(\Lambda\log^2))(m).
\]
Here \((\Lambda\log^2)(n)=\Lambda(n)(\log n)^2\). Both derivatives of the Dirichlet series for \(-L\) act on \(n^{-s}\), so the sign in the last formula is positive. The identity is coefficientwise by absolute convergence in \(\Re s>1\). For \(m=p,p^2,p^3\) respectively, the three coefficient lists in units of \((\log p)^3\) are \(1,6,20\) for \(C\), \(-1,-9,-36\) for \(\zeta\zeta'''\), and \(0,-1,-6\) for \(\zeta'\zeta''\). The half-combination gives \(0,0,1\), as required by the three von Mangoldt factors defining \(A\).

Apply the same smooth hyperbola and Poisson proof to each divisor product. Their coefficients have the form \(-\sum_{de=m}(\log e)^3\) and \(-\sum_{de=m}(\log d)(\log e)^2\). These weights are asymmetric, so after splitting by \(\psi(d/e)+\psi(e/d)=1\), swap \(d,e\) in the second term and bound the two logarithmic polynomials separately. Each resulting term has \(d\ll\sqrt{kT}\), and the derivative and Fourier estimates are unchanged. The term \(\log(k/m)[m^{-s}]\zeta'^2\) from differentiating the outer \((k/m)^\beta\) remains exactly the divisor term already treated. The further algebra concerns \(A\) alone, so no logarithmic prefactor multiplies \(C\). The principal subtraction is the same linear unit-average operation for every coefficient sequence, and the resonant \(k\mid d\) sums still cancel exactly.

Writing \({\cal S}_T[B]\) for the signed sum in the preceding section with any sequence \(B\), before taking its real part, the result is
\[
 {\cal S}_T[A]=\tfrac12 {\cal S}_T[d_2*(\Lambda\log^2)]+O_M(T^{-M})
\]
for each fixed \(M\). The fixed power loss \(yT\) from summing the per-modulus estimates is absorbed by choosing the Poisson decay order larger. Consequently the precise remaining condition is
\[
 \Re\sum_{k\le y}\frac{a_k}{k}
 \sum_{m\ge1}(d_2*(\Lambda\log^2))(m)\,w_T(2\pi m/k)
 \left[e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}\right]
 =o(T\log^4T).
\]
The reduction supplies no estimate for this single-von-Mangoldt sum.
