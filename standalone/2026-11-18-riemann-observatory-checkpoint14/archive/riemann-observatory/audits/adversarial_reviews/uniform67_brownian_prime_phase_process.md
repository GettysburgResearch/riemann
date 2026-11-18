# Functional prime-phase central limit theorem in reciprocal-prime time

18 November 2026. Assume RH. Let \(L=\log Y\), \(b=\log L\), \(H=\log b=\log\log\log Y\), and use the normalized strict two-sided derivative-tail probability on \(|\gamma|>Y\), with weights proportional to \(|\zeta'(1/2+i\gamma)|^2/(1/4+\gamma^2)\). For fixed \(0\le u_0<1\), define on \([u_0,1]\)
\[
 P_Y(u)=\exp(b^u),\qquad
 X_Y(u)=\frac{1}{\sqrt{H/2}}
        \sum_{p\le P_Y(u)}
        \left(\frac{\cos(\gamma\log p)}{\sqrt p}-\frac1p\right).
\]
Then \(X_Y\) converges in distribution in \(D([u_0,1])\) with the \(J_1\) topology to the restriction of standard Brownian motion to this interval. In particular the limiting value at \(u_0\) has variance \(u_0\), rather than being reset to zero. The argument supplies effective conditional convergence in bounded-Lipschitz distance for fixed computable \(u_0\) and tolerance, using the effective scalar prefix restriction and fixed-dimensional argument. No numerical onset is calculated. [Restricted prefix estimate](uniform64_exceptional_prime_clt_skeptic.md) · [Fixed-dimensional comparison](uniform65_joint_exceptional_prime_clt.md)

## Fourth moment proportional to squared interval mass

Fix \(Y\); \(P_Y(1)=L\). Temporarily take any deterministic subset \(I\) of the primes up to \(L\). Set \(h_I=\sum_{p\in I}1/p\), \(W_I=\sum_{p\in I}p^{-1/2}\cos(\gamma\log p)\), and \(S_I=W_I-h_I\). The required bound, before clock normalization, is
\[
 \mathbb E_Y |S_I|^4\le C h_I^2.                                      \tag{1}
\]
The constant is uniform in \(I\), including arbitrarily short or empty intervals.

In the independent Poisson-circle model of radii \(p^{-1/2}\), \(E_*W_I=h_I\) and the centered increments have range length \(2/\sqrt p\). The log moment generating function for a centered coordinate has second derivative at most \(1/p\), since it is a variance under an exponential tilt. Thus \(E_*e^{tS_I}\le e^{t^2h_I/2}\) for all real \(t\). For \(h_I>0\), optimization and integration of the resulting two-sided bound give \(E_*|S_I|^j\le C_j h_I^{j/2}\) for \(1\le j\le4\). For \(h_I=0\) the quantity vanishes. In particular
\[
 0\le E_*W_I^j\le C_j(h_I^j+h_I^{j/2})\qquad (1\le j\le4).
\]
The lower bound, even for odd \(j\), follows by expanding the raw power in characters. All its coefficients are nonnegative and all model character expectations are nonnegative.

At an arbitrary prefix \(T\ge Y\), write \(L_T=\log T\). Use the effective HLZ estimate with fixed character range \(m,n\le L_T^4\) and any desired fixed saving \(L_T^{-B}\). Exclude the possible exceptional prime \(\ell_T\) as in the scalar proof. Denote the retained subset of \(I\) by \(I'\) and write \(h=h_{I'}\). All the raw Fourier words through degree four for \(W_{I'}\) fit the range \(m,n\le L^4\), since each word contributes one prime to the numerator or denominator per factor. The divisor-closed support avoids \(\ell_T\). On this finite block, the effective real prefix character error is bounded by a constant times
\[
 \kappa(m,n)\frac{\log(2L)}{L_T}+L_T^{-B},
 \qquad \kappa(m,n)=\frac{(m,n)}{\sqrt{mn}} .
\]
This uses the refined relative term in the prefix estimate and absorbs the degree into its constant. Model expectations of the individual characters are exactly \(\kappa\). If taking the older unrestricted character estimate, the same calculation first gives a qualitative version of (1). Nothing here requires an effective individual exceptional-character estimate.

For each raw \(j\)-th moment, the sum of the positive coefficients weighted by \(\kappa\) is its Poisson expectation. In the binomial expansion \(S_{I'}^4=(W_{I'}-h)^4\), use absolute values on the centered coefficients. The total majorant for the relative error is
\[
 \sum_{j=1}^4\binom4j h^{4-j} C_j(h^j+h^{j/2})
 \le C(h^2+h^4).
\]
In particular every exponent \(4-j/2\) lies between 2 and \(7/2\), and no term independent of \(h\) or linear in \(h\) is introduced at small interval mass. The \(j=0\) expectation is exact. For the absolute Fourier error, the total absolute coefficient mass of the centered fourth power is at most
\[
 \left(h+\sum_{p\in I'}p^{-1/2}\right)^4
 \le 16L^2 h^2.
\]
Here \(h\le\sum p^{-1/2}\), and Cauchy–Schwarz bounds the sum by \(\sqrt{Lh}\). Thus the absolute prefix discrepancy through degree four on this centered increment is at most
\[
 C_B^{\rm eff}\left(\frac{\log(2L)}{L_T}(h^2+h^4)
                     +L_T^{-B}L^2 h^2\right).
\]
Using \(h\le1+\log L\) suffices to bound this by a computable constant times \(h^2\), uniformly in \(T\ge Y\), with \(B>2\). With the model bound, the retained fourth moment is therefore at most \(C h^2\).

Restore the omitted coordinate **inside the prefix**. If \(\ell_T\in I\), its centered increment has absolute value at most \(2/\sqrt{\ell_T}\), hence fourth power at most \(16h_I^2\). The pointwise inequality \(|x+y|^4\le8(|x|^4+|y|^4)\) bounds the full prefix fourth moment by \(C h_I^2\). If \(I'\) is empty its centered moment is exactly zero and the same restoration applies. No averaged omission error divided by a small interval length is needed. The left side after restoration is the fixed full statistic \(S_I\), even though \(\ell_T\) was allowed to depend on \(T\). Fourth powers are nonnegative, and the cosine statistic is even in the ordinate.

Let \(A(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2\), \(A_I(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2|S_I(\gamma)|^4\), and \(f(t)=(t^2+1/4)^{-1}\). Then \(0\le A_I(T)\le C h_I^2 A(T)\) for all \(T\ge Y\). Stieltjes integration with the inclusive prefix subtracts \(-f(Y)A_I(Y)\) for the strict tail, including when \(Y\) is a zero ordinate. The upper endpoint vanishes by the effective ordinary derivative-moment bound and the finiteness of the fixed prime block. Consequently
\[
 \int_{(Y,\infty)} f\,dA_I
 \le C h_I^2\int_Y^\infty (-f')A
 =C h_I^2\bigl(B_Y^+ + f(Y)A(Y)\bigr),
 \qquad B_Y^+=\int_{(Y,\infty)} f\,dA .
\]
The effective untwisted derivative moment gives a bounded ratio \(f(Y)A(Y)/B_Y^+\). Dividing proves (1). Both signs multiply the numerator and denominator by the same 2. This argument does not sum character errors over a list of small intervals. It bounds every interval with its own local mass and so retains the required fourth-moment scaling even at the smallest interval. [Scalar prefix and strict-tail proof](uniform64_exceptional_prime_clt_skeptic.md)

## Continuous interpolation on the exact reciprocal clock

Enumerate the primes \(p_1<\cdots<p_M\le L\). Define \(v_0=0\) and \(v_j=H^{-1}\sum_{i\le j}1/p_i\). Let \(Z_Y\) be the continuous linear interpolation in this clock, with \(Z_Y(0)=0\) and \(Z_Y(v_j)\) the normalized cumulative centered sum through \(p_j\). For large \(Y\), \(v_M\le2\); extend constantly to \(2\). Bound (1) gives for all grid points
\[
 \mathbb E|Z_Y(v_j)-Z_Y(v_i)|^4\le C(v_j-v_i)^2.                       \tag{2}
\]
This uses the same deterministic \(H\) in the normalization and in the clock.

For two times in one interpolation cell, their increment is a fraction \(\theta\in[0,1]\) of the full prime increment. Its fourth moment is at most \(C\theta^4(\Delta v)^2\le C(\theta\Delta v)^2\). For times in different cells, split the difference into at most three pieces: the initial fractional cell, the full grid interval, and the final fractional cell. The constant extension causes no difficulty. Minkowski's inequality in \(L^4\), followed by the bound \(\sum_{i=1}^3\sqrt{\Delta_i}\le\sqrt{3\sum_i\Delta_i}\), gives
\[
 \mathbb E|Z_Y(t)-Z_Y(s)|^4\le C'|t-s|^2\qquad(s,t\in[0,2]).
\]
This is a uniform Kolmogorov tightness bound in \(C([0,2])\), with initial value fixed. It can be read effectively: on a dyadic grid, the probability that any adjacent increment at level \(j\) exceeds \(A2^{-\alpha j}\) is at most \(C'A^{-4}2^{-(1-4\alpha)j}\) for \(0<\alpha<1/4\). Sum this over \(j\ge k\). On the complement, the dyadic continuous chaining bound gives modulus at scale \(2^{-k}\) bounded by a constant depending on \(\alpha\) times \(A2^{-\alpha k}\). This proves an effective modulus-in-probability estimate. The original process's largest jump is also deterministically \(O(H^{-1/2})\); the fourth-moment interpolation argument retains the stronger local scaling.

Elementary Mertens summation with a bounded effective remainder gives \(H(x)=\sum_{p\le x}1/p=\log\log x+O(1)\) uniformly for \(x\ge e\). In this scope it follows from the effective Chebyshev bound \(\sum_{n\le x}\Lambda(n)=O(x)\) and the identity \(\sum_{n\le x}\Lambda(n)\lfloor x/n\rfloor=\log(\lfloor x\rfloor!)\), which yield \(\sum_{n\le x}\Lambda(n)/n=\log x+O(1)\). Remove the convergent contribution of higher prime powers, then sum by parts with \(1/\log x\). Since \(P_Y(u)\in[e,L]\) and \(\log\log P_Y(u)=uH\) for \(u\in[0,1]\),
\[
 c_Y(u)=\frac{H(P_Y(u))}{H}=u+O(H^{-1})
\]
uniformly and effectively on \([0,1]\). The height-\(Y\) process is exactly \(X_Y(u)=Z_Y(c_Y(u))\), because \(c_Y(u)\) is a grid point with the inclusive prime cutoff. This remains true at the jump instants. Consequently \(\sup_{u\in[0,1]}|X_Y(u)-Z_Y(u)|\) tends to zero in probability, by the uniform modulus bound. It is not necessary to assert continuity of the step clock itself.

## Identification of the process limit

Fix \(u_1,\dots,u_d\in[u_0,1]\). The column for prime \(p\) in the corresponding vector has \(i\)-th entry \(\sqrt{2/H}\,p^{-1/2}\mathbf1_{p\le P_Y(u_i)}\). Its maximal norm tends effectively to zero and the model covariance entry is
\[
 H^{-1}\sum_{p\le P_Y(\min(u_i,u_j))}(p^{-1}-p^{-2})
 \ \longrightarrow\ \min(u_i,u_j).
\]
The covariance convergence is effective by the preceding mass bound and convergence of \(\sum_p p^{-2}\). The fixed-dimensional prime-array comparison therefore gives the joint Gaussian limit. It also follows directly by projecting this vector onto one direction, using the finite-order signed Fourier majorant and the infinitesimal model increments. Thus \(Z_Y|_{[u_0,1]}\) is tight in the continuous uniform topology and all its subsequential limits have the finite-dimensional laws of Brownian motion on that interval. These determine a unique law on the continuous path space using a dense countable time set. The uniform approximation in probability then transfers convergence to \(X_Y\) in \(D\) with \(J_1\) topology, since the \(J_1\) distance is bounded by the uniform distance. The tightness argument uses (1)–(2), not finite-dimensional convergence alone.

For an effective bounded-Lipschitz onset on \(D\), choose a deterministic finite mesh on \([u_0,1]\). The uniform modulus estimate and the effective clock error make the expectation of the bounded path-test error from replacing \(X_Y\) by its mesh-value polygonal interpolation arbitrarily small. In detail, between two mesh points the image clock times differ by at most the mesh width plus \(2\|c_Y-\mathrm{id}\|_\infty\); the polygonal value is a convex combination of endpoint evaluations and is therefore within the corresponding modulus of \(Z_Y\). The same argument for Brownian motion uses its fourth moment \(3|t-s|^2\). On this fixed mesh, mapping the vector of values to its polygonal interpolation is 1-Lipschitz from the sup norm to the uniform path norm and hence to \(J_1\). The effective fixed-dimensional bounded-Lipschitz comparison applies at the mesh values, including a possible degenerate component at \(u=0\). Combining the two modulus errors and the mesh-vector error gives an effective conditional path-space onset for fixed parameters. This asserts neither a numerical threshold nor an effective arbitrary-coordinate twist estimate.

No canonical records changed.
