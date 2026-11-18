# A single soft direction in the two-comb arithmetic matrix

**Proposed unconditional theorem.** Retain the [squeezed Mellin packet space](nov18b-weil-squeezed.md), normalized by physical \(L^2\), and put \(L=\log q\). Its smallest Weil eigenvalue is of order \(\log\log L\). There exists an absolute \(c>0\) (for the fixed choices of cutoffs in that construction) such that its **second** smallest eigenvalue is at least \(cL\) for all sufficiently large \(q\). Any sequence of unit vectors with Weil value \(o(L)\) approaches the line given by the matched coherent coefficients in the two combs, with the carrier-dependent relative phase. Thus only one direction in this entire growing subspace nearly cancels the gamma main term. No estimate on the orthogonal complement of the packet space in the full Weil domain is implied.

The key additional input is that the signed arithmetic cross block, after division by its natural size, becomes rank one on *all sequences of sublinear divisor energy*. The weights, the modulus range and the transfer to this subspace are specified below.

## Large-prime pruning at sublinear energy

For one of the two cutoffs \(N\), put \(U=\log N\asymp L\); use probability \(\mu_N(n)=1/(nH_N)\) and normalized energy \(\mathcal E_N\) from [the finite divisor-section proof](nov18b-weil-divisor-edge.md). Suppose \(\|b_N\|_{\mu_N}\le1\) and \(\mathcal E_N(b_N)\le K=o(U)\). The vector is within \(o(1)\) in this same norm of a function \(b^\flat\) that is a linear combination of divisibility indicators \(\mathbf1_{r\mid n}\) with \(r\le\exp(o(U))\). Its total absolute indicator coefficient sum is \(\exp(o(U))\), and it has bounded norm in the independent product measure used below. The rates can be chosen simultaneously for any fixed finite number of vector sequences.

Here are details that allow growing energy. Set \(V=\sqrt{(K+1)U}\), \(P=e^V\), and \(D=\sqrt{VU}\). Then \(K=o(V)\), \(V=o(D)\), \(D=o(U)\), and \((K/V)(1+\log(U/V))\to0\). The pruning inequality (6) of the finite-section proof therefore costs \(o(1)\) in squared norm. Its bounds (4) and (5) show that the vector mass outside the rectangle \(\log s_P(n)\le D,\ \log(n/s_P(n))\le U-D\) is \(o(1)\), including the upper half of the smooth transition \(\log s_P(n)>D/2\). With the same common rough-factor average and smooth cutoff, obtain a function \(B(s)\) on the independent \(P\)-smooth product, with bounded norm and energy
\[
 \mathcal E_P(B)\ll K+1+V^3/D^2=o(U).
\]
This follows by taking coefficients 2 and 2 in the product-difference inequality, so it needs no relative precision at this step.

We record why pulling this function back to the finite integer set does not amplify the error. If \(Z_R(t)\) denotes the harmonic sum over \(P\)-rough integers through \(t\), then
\[
  [Z_R(N)-Z_R(Ne^{-D})]\!
   \sum_{s\le e^D,\ P\text{-smooth}}s^{-1}
     \le \sum_{Ne^{-D}<n\le Ne^D} n^{-1}\ll 1+D.
\]
The product map \((r,s)\mapsto rs\) is injective. The smooth factor on the left is \((1-o(1))Z_s\), \(Z_s=\prod_{p\le P}(1-1/p)^{-1}\), by its independent first moment \(\mathbb E\log s\ll V\). On the rectangle, as in the finite-section argument, \(Z_R(Ne^{-D})Z_s/H_N=1+o(1)\), by testing the constant vector. Hence \(Z_R(N)Z_s/H_N=1+o(1)\). It follows pointwise in \(s\) that the law of \(s_P(n)\) under \(\mu_N\) is at most \((1+o(1))\) times its independent product probability \(1/(sZ_s)\). The upper rough shell's law is itself at most \(o(1)\) times that probability. Thus \(B(s_P(n))\) approximates the original vector in finite norm: on the rectangle this follows from the common average and cutoff estimates, and outside it the pulled-back smooth function is zero above the smooth cutoff and negligible on the upper rough shell.

Expand \(B\) in the orthonormal one-prime contrasts from the finite-section proof. Keeping product levels at most \(M=\sqrt{(1+K+V^3/D^2)U}\), increasing the fixed implicit constant if needed, loses \(o(1)\) in product norm by the spectral energy bound. Here \(M=o(U)\). A retained tensor contrast with levels \(j_p\) involves divisibility indicators whose moduli divide \(r_0=\prod p^{j_p+1}\le e^M\). Distinct tensor contrasts give distinct such integers, so there are at most \(e^M\) of them. Each normalized one-prime factor is a combination of two indicators \(\mathbf1_{p^j\mid n},\mathbf1_{p^{j+1}\mid n}\), with absolute coefficient sum \(O(p^{(j+1)/2})\). This follows by computing the weighted norm of the contrast, which has squared value \(p^{-j}/(p-1)\). Products and Cauchy–Schwarz over the retained coefficients therefore cost at most \(e^{O(M)}\). The independent norm remains bounded and the pointwise measure domination gives the same \(o(1)\) approximation in the finite norm. This proves the claim.

## Cross terms for the retained divisibility indicators

Write \(N_1,N_2\) for the low and high cutoffs. Let \(H_i=H_{N_i}\), \(b_0=\log(q/(N_1N_2))\). In the notation of [the signed Fresnel calculation](nov18b-weil-fresnel.md), put a divisibility condition \(r_1\mid n\), \(r_2\mid m\) on its unnormalized coherent cross sum. Uniformly for \(r_1,r_2\le\exp(o(L))\), the result is
\[
 \frac{e^{2\pi i q} I}{r_1 r_2}
 \left[ H_{\lfloor N_1/r_1\rfloor}H_{\lfloor N_2/r_2\rfloor}
                  +D(b_0)\right]+O(q^{-1/4+o(1)}).
 \tag{1}
\]
Here the original matched, truncated profiles are used; \(|I|=1+O(L^{-20})\). To see uniformity, change \(n=r_1 n'\), \(m=r_2 m'\); the integer being sampled is \(l=r_1r_2 n'm'd\). The linear carrier phase still cancels since \(l\) is integral. The new center for \(n'm'd\) is \(q'=q/(r_1r_2)\), and the sampling width is \(\sqrt q/(r_1r_2)\); the zero Fourier coefficient gains exactly \(1/(r_1r_2)\). In the divisor proof use cutoffs \(\lfloor N_i/r_i\rfloor\), and \(Q'=q'/\lfloor N_2/r_2\rfloor\). The size \(Q'/(\sqrt q/(r_1r_2))\) is \(q^{o(1)}\), as are all step sizes in the divisor correction, all cutoff displacements in the threshold replacement, and each fixed profile seminorm. The smallest harmonic cutoff remains \(q^{1/2-o(1)}\). Summing the van der Corput bound there with the Schwartz Fourier weight consequently changes its \(q^{-1/4}\) cost only by \(q^{o(1)}\). The divisor correction uses \(\log(q'/(\lfloor N_1/r_1\rfloor\lfloor N_2/r_2\rfloor))=b_0+O(q^{-1/2+o(1)})\); the sum defining \(D\) is continuous at integer cutoffs, and its local Lipschitz norm is \(O(1+b_0)\) by Mertens. These estimates give (1), including the harmonic-expansion error.

For physical coefficients \(a_n=b(n)/\sqrt{nH_1}\) and \(c_m=f(m)/\sqrt{mH_2}\), bilinearity now evaluates the cross form on any two retained approximants. The harmonic term in (1) factors exactly into their two finite means, since \(\sum_{r\mid n,\ n\le N}1/n=H_{\lfloor N/r\rfloor}/r\). The coefficient of \(D(b_0)\) factors into their two independent means, which stay bounded by the product norm. Also \(D(b_0)=O(1+b_0^2)\) and \(H_i\asymp L\). The total coefficient loss on the power-saving error is only \(\exp(o(L))\). The full cross matrix has norm \(O(L)\) by the squeezed-space row estimate. Hence replacing each approximant by its original vector gives, for sublinear energy,
\[
 \text{oriented cross form}
  =e^{2\pi i q}I\sqrt{H_1H_2}\,
       \overline{\mathbb E_{\mu_{N_1}} b}\,
                   \mathbb E_{\mu_{N_2}} f+o(L),
 \tag{2}
\]
with the conjugation convention of the comb note. The error is uniform in the sequential sense just proved. In particular all fixed nonconstant centered prime contrasts have vanishing leading cross coupling.

## Isolation of the direction

Consider a unit coefficient vector with \(W=o(L)\). For these profiles \(G=L+o(1)\) and the pole term is \(o(1)\). The diagonal prime forms are \(\log N_i\) times the squared norms minus their nonnegative divisor energies and bounded potentials. The norm of the cross block is at most \(L/2+o(L)\) by the two weighted row estimates, since both \(\log N_i=L/2+o(L)\). Therefore the sum of the two nonnegative divisor energies is \(o(L)\); otherwise the sum of the diagonal and cross terms falls short of \(L\) along a subsequence. Formula (2) applies.

After dividing the prime form by \(L\), the diagonal contribution is \(1/2+o(1)\). The two orientations of the cross form must supply the remaining \(1/2+o(1)\). If the two coefficient norms are \(s,t\), their squared sum is one, and the product of their mean magnitudes is at most \(st\le1/2\). Since \(2\sqrt{H_1H_2}/L\to1\) and \(|I|\to1\), equality is required asymptotically in both inequalities, including the real phase alignment in (2). Thus \(s,t\to1/\sqrt2\), and each vector converges in normalized harmonic norm to its own constant. Their relative phase converges, modulo a common phase, to the one maximizing the coherent cross term. The normalized vector is therefore at distance \(o(1)\) from that specified line.

If the claimed lower bound for the second eigenvalue failed, positivity on the squeezed space would give a sequence of real \(q\to\infty\) with two orthogonal unit eigenvectors having \(W=o(L)\). Both would approach the same line, a contradiction. The first eigenvalue bounds are those proved in the squeezed-space theorem. This argument gives existence of \(c>0\) without an evaluated numerical value.

## Absolute asymptotic for the soft eigenvalue

The actual minimum and its unit eigenvector admit the sharper estimates
\[
 \lambda_{\min}(W|_{V_q})=b_0+o(1),\qquad
 \operatorname{dist}(v_{\min},\mathbb C v_{\rm coh})
          \ll \sqrt{\log L}/L.
 \tag{3}
\]
Here \(v_{\rm coh}\) is the normalized matched coherent pair, with the relative phase that aligns the signed Fresnel main term. The lower and upper cutoffs are those of the squeezed theorem.

It suffices to bound the residual norm on this vector by \(O(A)\), where \(A=C\sqrt{\log L}\). In each diagonal chart the exact weighted row on its coherent vector is \(\log N_i-R(N_i/n)\), with \(R\) bounded. For the cross block, keep the signed correlation \(\Psi(w)=e^{i\pi w^2}K(w)\) in place of its absolute majorant in the pointwise row argument. For the untruncated matched Gaussians its Fourier transform satisfies
\[
 \widehat\Psi(\xi)=I e^{-i\pi\xi^2} R_\phi(\xi),\qquad
 R_\phi(\xi)=\int \phi(u+\xi)\overline{\phi(u)}\,du,
 \tag{4}
\]
where \(|R_\phi(\xi)|=\exp(-c\xi^2/e^2)\) with an absolute \(c>0\), and \(|I|=1\). Indeed \(\widehat K(\xi)=e^{i\pi\xi^2}|\widehat\phi(\xi)|^2\), and convolution with the Fourier transform of \(e^{i\pi w^2}\) gives (4). The truncation error is bounded by \(L^{-20}\) on the relevant support and by the Gaussian tail upon restoring the full Gaussian; after normalization its total cost in the row is \(o(1)\) as in the squeezed proof.

In a row starting at \(n\), write \(x=q/n\), \(y=r/n\), and \(D=x/N_{\rm opposite}\). On \(|w|\le 5A/e\) the condition on the omitted divisors is \(d<l/N_{\rm opposite}\). It may be replaced by \(d\le D\) at cost \(O(1)\) in the row. In detail the ambiguous integers are in a range of length \(O(1+DA/(er))\) about \(D\). Each costs \(O((\log(2D))(1/D+e/y))\) by (2) of the squeezed note and summing a sampled Gaussian on multiples of \(d\). Here \(D\gg A^2\) and \(e/y\ll A/D\) in both row orientations. These inequalities make the product of the displayed estimates bounded.

The main integer sampling has negligible nonzero aliases since \(y/e\gg A\). For the subtracted divisors \(d\le D\), (4) shows that the absolute alias error after summation is at most
\[
 C\sum_{d\le D}\frac{\Lambda(d)}d
             \sum_{j\ge1}\exp(-c(jy/(ed))^2)\ll 1+eD/y\ll A.
\]
Below \(y/e\) use dyadic exponential decay; above it use the elementary Gaussian sum bound \(C ed/y\) and Chebyshev. Restricting the spatial Gaussian sum to \(|w|\le5A/e\) costs \(O(e^{-c'A^2}(\log(2D)+eD/y))\), by a Gaussian tail comparison at each spacing. The Taylor error in replacing the true carrier phase by the Fresnel phase is \(O(q^{-1/2}L^{O(1)})\) times the row majorant. The main term is therefore \(e^{2\pi i q}I(\log x-\sum_{d\le D}\Lambda(d)/d)=e^{2\pi i q}I(\log N_{\rm opposite}+O(1))\), with uniform error \(O(A)\). Complex conjugation applies in the opposite orientation. The untruncated Gaussian coupling and the normalized cutoff coupling differ by \(O(L^{-20})\); either phase choice gives the same estimate.

These diagonal and cross rows, and the uniform scalar gamma approximation, yield \(\|(W-b_0)v_{\rm coh}\|\ll A\). The preceding coherent Rayleigh calculation gives \(\langle Wv_{\rm coh},v_{\rm coh}\rangle=b_0+o(1)\) for either phase choice. The lower bound \(cL\) for the second eigenvalue, the spectral theorem and the Temple inequality now give an eigenvalue error \(O(A^2/L)+o(1)=o(1)\) and the stated angle estimate. This completes (3).
