# Reciprocal Dirichlet zeros from shifted Möbius correlations

For a character \(\chi\bmod q\) let \(M_\chi(x)=\sum_{n\le x}\mu(n)\chi(n)\), extended by zero for \(x<1\). At each fixed modulus,
\[
 \int_1^X |M_\chi(x)|^2\,\frac{dx}{x^2}\ll_\chi\log(2X) \tag{1}
\]
holds if and only if the primitive inducing \(L\)-function satisfies GRH, its nontrivial zeros are simple, and
\[
       \sum_{\rho}\frac1{|\rho L'(\rho,\chi)|^2}<\infty. \tag{2}
\]
Here the derivative includes the Euler factors of the given character. An imprimitive factor \(1-\chi^*(p)p^{-s}\) and its reciprocal are uniformly bounded on \(1/2\le\Re s\le3/4\), so including those factors preserves convergence. Under these equivalent conditions the integral in (1) divided by \(\log X\) tends to the sum in (2).

There is an arithmetic test for shared nontrivial zeros. Suppose (1) holds for two characters \(\chi,\eta\), which may have different moduli. For each fixed real \(h\),
\[
 C_{\chi,\eta}(h)=\lim_{X\to\infty}
  \frac{e^{-h/2}}{\log X}\int_1^X
      M_\chi(e^hx)\overline{M_\eta(x)}\,\frac{dx}{x^2}
 =
 \sum_{\rho=1/2+i\gamma:\ L(\rho,\chi)=L(\rho,\eta)=0}
 \frac{e^{i\gamma h}}
      {|\rho|^2 L'(\rho,\chi)\overline{L'(\rho,\eta)}} . \tag{3}
\]
The series converges absolutely and uniformly in \(h\). In particular \(C_{\chi,\eta}\) vanishes identically exactly when the two functions have disjoint nontrivial zero sets. A single unshifted mean can combine contributions from different shared zeros. Uniqueness of Bohr coefficients of the entire shifted correlation recovers every individual common ordinate.

## Necessity directly from the Laplace transform

Set \(g_\chi(v)=e^{-v/2}M_\chi(e^v)\). Under (1), \(\int_0^R |g_\chi|^2\ll 1+R\). The Laplace transform converges absolutely and locally uniformly for \(\Re z>0\). Summation for \(\Re z>1/2\) and continuation give \(G(z)=1/[s L(s,\chi)]\), \(s=1/2+z\). Thus no zero lies to the right of the line. The functional equation, with conjugation of the conjugate character, gives reflection about that line for the zero set of the individual primitive character. Consequently its nontrivial zeros all lie on the line.

The probability measures \(d\mu_\epsilon(v)=\epsilon e^{-\epsilon v}dv\) on \(v\ge0\) have uniformly bounded \(\int |g_\chi|^2d\mu_\epsilon\) as \(\epsilon\downarrow0\), by (1) and integration by parts. Hence \(|G(\epsilon+it)|\ll1/\epsilon\) by Cauchy–Schwarz. Every boundary pole must be simple, and \(\int g_\chi(v)e^{-i\gamma v}d\mu_\epsilon(v)\to c_{\chi,\gamma}=1/[\rho L'(\rho,\chi)]\). On each finite set of distinct ordinates the exponential Gram matrix for \(\mu_\epsilon\) converges to the identity, by its explicit entries \(\epsilon/(\epsilon+i(\gamma_j-\gamma_k))\) up to conjugation. Finite-dimensional projection therefore bounds the sum of squared limiting coefficients by \(\limsup_{\epsilon\downarrow0}\int|g_\chi|^2d\mu_\epsilon\). Exhaust the ordinates to obtain (2).

## Sufficiency, including nonreal characters

The [adjacent-zero proof for the ordinary Möbius sum](trace-weak-mertens-nov18.md) extends as follows. For a primitive nonprincipal character multiply \(\Lambda(1/2+iz,\chi)\) by a constant of modulus one making it real on the real axis. Such a rotation exists by the functional equation and conjugation. This real entire function of order one has under GRH the canonical product \(C z^m e^{a z}\prod_{\gamma\ne0}(1-z/\gamma)e^{z/\gamma}\) with real \(a\), because division by the product leaves a zero-free exponential and the logarithmic derivative of that quotient is real on the axis. Central zeros are allowed when simple. Each finite product after removing two adjacent simple linear factors has log-concave modulus on the intervening segment and modulus increasing under vertical displacement. The real exponential factors preserve both properties, so they pass to the locally uniform limit. This gives (7) of the linked proof for the rotated completed function even when the ordinates do not occur in opposite pairs. The zeta function uses the usual pole-removing completion.

For the transform \(G(z)\) the ratios of elementary and gamma factors at neighboring ordinates are \(O_\chi((2+|t|)^{\epsilon/2})\) on \(\Re z=\epsilon\in(0,1/4]\), by Stirling and the bounded-gap consequence of the fixed-conductor Riemann–von Mangoldt formula. The finitely many imprimitive factors obey the same bound. Consequently the adjacent-pole majorant (8) in the linked proof applies with \(c_{\chi,\gamma}\). GRH gives \(M_\chi(x)\ll_{\chi,\delta}x^{1/2+\delta}\) for each \(\delta>0\) by Littlewood's reciprocal bound in closed substrips to the right of \(1/2\) and truncated Perron summation. This supplies the Laplace-domain Plancherel identity on all \(\epsilon>0\). The fine Gaussian smoothing on \([0,R]\) uses \(T=e^R\) and only the size of the jumps of \(M_\chi\), which are at most one. Thus (9) and the finite-pole truncation proof there give
\[
 \limsup_{R\to\infty}\frac1R\int_0^R
 \left|g_\chi(v)-\sum_{|\gamma|<V}c_{\chi,\gamma}e^{i\gamma v}\right|^2dv
 \ll_\chi \sum_{|\gamma|>V}|c_{\chi,\gamma}|^2
\]
at all cutoff ordinates \(V\) away from the absolute heights of zeros. Orthogonality of finite sums and (2) give the asserted asymptotic. This reasoning applies at each fixed conductor and requires no uniformity as the conductor varies.

Finally the same tail bound holds for the translates by any fixed \(h\) on \([0,R]\): translated intervals lie inside \([0,R+|h|]\) up to a bounded initial piece of finite squared integral. Cauchy–Schwarz allows both factors in (3) to be replaced in turn by finite exponential sums. Their mean keeps exactly matching ordinates, with the displayed phase. Absolute convergence follows from (2) for both characters. After \(x=e^v\) this gives (3).

For a fixed modulus, summing the squared means over all reduced classes is equivalent to summing over characters by the ordinary finite group Parseval identity. Thus a logarithmic upper bound for the sum of the mean squares of \(\sum_{n\le x,\,n\equiv a\ (q)}\mu(n)\) over reduced classes characterizes the simultaneous conditions above for every character modulo \(q\). This does not establish the required upper bound for any modulus.
