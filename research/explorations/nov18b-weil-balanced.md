# Two arithmetic packet families at exact Riemann–Siegel balance

**Proposed unconditional theorem.** Let \(L=\log q\), \(r=\sqrt q\), and \(T=2\pi q\), with real \(q\to\infty\). The two Mellin families below have opposite cutoffs with product \(q+O(q^{1/2+o(1)})\). Their physical supports meet, and prime shifts need not map an integer center exactly to another one. Equip their linear span with its actual \(L^2\) metric. If \(\lambda_1\le\lambda_2\le\cdots\) are the Weil eigenvalues of this space, then
\[
 |\lambda_1|\le q^{-1/2+o(1)},\qquad \lambda_2\ge c\log q
 \tag{1}
\]
for a fixed \(c>0\) and all sufficiently large \(q\). The first unit eigenvector is within \(q^{-1/4+o(1)}\) of the coherent pair of truncated zeta sums, up to a scalar phase. The estimate on the absolute value leaves its sign undetermined. A signed or positive conclusion for arbitrary tests in the full Weil domain requires additional control.

## Cutoffs and physical metric

Write \(e=L^{-1/3}\). Use the normalized low Gaussian \(\phi(u)\propto\exp(-\pi u^2/e^2)\) and high Gaussian \(\widehat\psi(\xi)=e^{i\pi\xi^2}\widehat\phi(\xi)\), with Fourier kernel \(e^{-2\pi i u\xi}\). Truncate as in [the separated construction](nov18b-weil-squeezed.md), now at \(A=C\sqrt L\) standard widths with \(C\) chosen so large that the lost norms are \(O(q^{-100})\). Smooth renormalization has the same cost. Use the usual unit packets \(r^{1/2}\phi(ru)e^{-iTu}\), \(r^{1/2}\psi(ru)e^{-iTu}\) translated to \(\log n,\log(q/m)\). Let \(K_0\) be a sufficiently large fixed constant and take all integer indices starting at 1 up to
\[
 N_1=\lfloor r/(K_0 e)\rfloor,\qquad N_2=\lfloor K_0re\rfloor.
\]
Thus \(b=\log(q/(N_1N_2))=O(q^{-1/2+o(1)})\). The dimension is \(N_1+N_2\asymp rL^{1/3}\) for this fixed \(K_0\). Any fixed derivative of a profile or correlation, and the support diameters in scaled coordinates, cost at most a fixed power of \(L\). Errors on restoring the untruncated Gaussians inside these supports remain negligible after multiplying by any of the matrix sizes and prime sums used here. Outside any sufficiently large fixed power of \(L\) in the scaled coordinate the restored Gaussian correlations are \(O(q^{-100})\), also in their sampled tails.

Both within-family autocorrelations of the untruncated profiles equal \(R(v)=\exp(-\pi v^2/(2e^2))\), because the chirp preserves the Fourier magnitude. In an individual Gram matrix use the harmonic Schur weight \(w_n=n^{-1/2}\). Its off-diagonal absolute weighted row is bounded by
\[
 C\exp[-c(r/(en))^2]+O(q^{-20}). \tag{2}
\]
Indeed when the support permits an overlap, the second index is \(n+j\asymp n\), so \(r|\log(1+j/n)|\gg r|j|/n\). Here \(r/(en)\ge K_0\) in the low chart and eventually also in the high chart. These estimates hold with absolute \(C,c\) independent of \(K_0\).

For the cross Gram matrix the pointwise absolute majorant, up to negligible tails, is
\[
 B(v)=\sqrt2 e(1+4e^4)^{-1/4}
               \exp[-2\pi e^2v^2/(1+4e^4)],\qquad v=r\log(q/(nm)).
\]
If \(i=N_1-n,j=N_2-m\), then \(ev\ge K_0 e^2 i+j/K_0\). Its squared Hilbert–Schmidt norm is thus at most
\[
 2e^2\sum_{i,j\ge0}\exp[-(4\pi-o(1))(K_0 e^2 i+j/K_0)^2]+o(1)
 \le (4\pi)^{-1}+O(K_0^{-1})+o(1).
\]
For the last inequality compare each decreasing sum with its integral plus its first summand; the double integral is \(2\int_0^\infty t e^{-4\pi t^2}dt\). In particular this norm is less than \(0.31\) for sufficiently large fixed \(K_0\). It costs \(O(q^{-20})\) to restrict both indices to \(n>N_1/\mathrm e\), \(m>N_2/\mathrm e\), where \(\mathrm e=\exp(1)\). Outside this range the profiles are actually disjoint for large \(q\). With (2), the physical Gram matrix \(G\) and its inverse have uniformly bounded norms.

## The divisor energy still controls every low state

For a coefficient vector \(a_n=b_n/\sqrt{nH_N}\), let \(E_N(a)\) be its normalized divisor difference energy from [the finite divisor theorem](nov18b-weil-divisor-edge.md). If \(U=\log N\) and \(M_D(a)=\sum_{n>Ne^{-D}}|a_n|^2\), its boundary inequality with explicit leading coefficient reads
\[
 (U-D)M_D(a)\le (1+\delta)E_N(a)+C_\delta(1+D)\|a\|^2
 \quad(0<D<U). \tag{3}
\]
Use \(|b_n|^2\le(1+\delta)|b_n-b_{n/d}|^2+(1+1/\delta)|b_{n/d}|^2\) in its proof. A consequence, by summing (3) over boundary bands of integer width up to \(U/2\), is
\[
 L\sum_n e^{-c(r/(en))^2}|a_n|^2
 \le C_c e^{-c'K_0^2}(E_N(a)+\|a\|^2).
 \tag{4}
\]
The remaining lower half has a superexponentially small weight. In both families \(U=L/2+o(L)\).

The same-chart prime matrix is the exact-divisor matrix \(A_N\) plus all overlaps \(m\ne dn\). For a fixed target \(m\), group the latter by \(h=dn\ne m\): their absolute harmonic Schur row is at most \(CL\exp[-c(r/(em))^2]+O(q^{-20})\), since \(\sum_{d\mid h}\Lambda(d)=\log h\). For a fixed source \(n\) the outgoing absolute row is at most \(C e^{-c'K_0^2}+O(q^{-20})\). To see this, only \(dn\le2N\) can overlap. At a fixed \(h=dn\) the sum of its nonidentical target correlations is bounded by \(C\exp[-c(r/(eh))^2]\) as in (2), even when \(h>N\). The remaining weight is \(\Lambda(d)/d\). Group \(dn\) in dyads below \(2N\) and use \(\sum_{d\asymp X}\Lambda(d)/d\ll1\); the exponential improves by a square factor at every dyad. The weighted Schur quadratic bound and (4) therefore control the entire off-divisor form by \(C e^{-c'K_0^2}(E_N(a)+\|a\|^2)\). The same bound applies to \(L\) times the off-diagonal part of a single-chart Gram form.

The cross prime matrix has only the orientation with \(dnm\) near \(q\). In its absolute row set \(x=q/n\), \(y=r/n\), and \(N'=N_{\rm opposite}\). The integer majorant in the separated construction still gives
\[
 \text{weighted cross row}\le\log N'+O_{K_0}(1)+CL\exp[-c(y/e)^2]. \tag{5}
\]
Specifically subtract all divisors through \(D=\min(y/e,x/(2N'))\) inside \(|l-x|\le yL^C\) on the effective support, enlarging the fixed polynomial as needed. Their multiples do not satisfy \(l/d\le N'\). The Gaussian Poisson errors for these subtracted divisors sum to \(O(1)\) as \(D\le y/e\). The unsubtracted full-lattice alias has relative size \(O(e^{-c(y/e)^2})\) and is multiplied by \(\log x\). Since both \(N'\ge re\) for all sufficiently large \(q\), \(\log x-\log\max(D,1)\le\log N'+O(1)\). The absolute correlation mass is \((1+4e^4)^{1/4}=1+o(1/L)\). These facts give (5), including rows with \(D<1\). Taylor replacement of the logarithmic scaled coordinate by \((l-x)/y\) costs \(q^{-1/2+o(1)}\) uniformly, by \(y^{-1}=L^{O(1)}\) or smaller and the divisor identity.

On coefficients \((a,c)\) write \(E=E_{N_1}(a)+E_{N_2}(c)\), \(J=\|a\|^2+\|c\|^2\). The actual gamma term is \(L\langle G(a,c),(a,c)\rangle+O_\delta(q^{-1/2+\delta})J\) for each \(\delta>0\), and the pole form is \(O(q^{-20})J\). For the gamma bound use the band \(|t-T|\le q^{1/2+\delta/2}\), Stirling there, and enough fixed integrations by parts outside to absorb the dimension; all involved profile seminorms are polylogarithmic. The residual diagonal prime form \(\log N_i-A_{N_i}\) equals the divisor energy plus a bounded potential. Weighted Schur in (5) costs at most \(\sum_i(\log N_{\rm opposite})\|a_i\|^2+O_{K_0}(J)+Ce^{-c'K_0^2}(E+J)\) for both cross orientations combined. The remaining cross physical Gram contribution, multiplied by \(L\), can cost up to
\[
 0.31 L(M_1(a)+M_1(c))+o(J)
 \le (0.62+o(1))(1+\delta) E+O_\delta(J)
\]
by (3). Choose \(\delta=0.1\), then \(K_0\) large enough for all the exponentially small multiples of \(E\). As \(\log N_1+\log N_2=L+o(1)\), we obtain
\[
 W(a,c)\ge c_0 E-O_{K_0}(J),\quad c_0>0. \tag{6}
\]

Every physical unit vector with \(W=o(L)\) now has \(E=o(L)\). Its endpoint mass is \(o(1)\) by (3), so its coefficient norm is \(1+o(1)\) by (2), (4) and the cross Gram bound. The same off-divisor estimates show that its diagonal prime errors are \(o(L)\). The sublinear-energy pruning and divisibility-indicator calculation in [the separated single-direction theorem](nov18b-weil-single-edge.md) carry over to the present cutoffs: the indicator formula has \(b=O(q^{-1/2+o(1)})\), all fixed profile seminorms are polylogarithmic, both cutoffs are \(q^{1/2+o(1)}\), and the norm bound \(O(L)\) for the cross block follows from (5). The within-chart disjointness was never used for that signed cross formula. Thus the leading cross form on these vectors is the product of the two harmonic means. The equality argument there implies convergence in coefficient norm, up to overall phase, to the normalized coherent vector with coefficients \(w_n,\eta w_m\), \(\eta=e^{-iT-i\pi/4}\). Here \(I=e^{i\pi/4}\) for the untruncated matched Gaussians. Boundedness of \(G\) gives the same physical convergence. By (6) all eigenvalues are bounded below by a constant. Two orthogonal eigenvectors with sublinear Rayleigh values would approach the same line, proving \(\lambda_2\ge cL\) once any one vector of value \(o(L)\) is exhibited.

## Cancellation of the individual divisor aliases

Here is the additional signed calculation needed to obtain a *two-sided* estimate for the first eigenvalue. All vectors and matrices in this paragraph use packet coordinates. Let \(v\) have coefficients \(n^{-1/2}\) and \(\eta m^{-1/2}\) in the two charts. Let \(P\) denote the Hermitian matrix of the prime term and \(G\) the physical Gram matrix. We prove
\[
 |v^*(P-LG)v|\le q^{-1/2+o(1)},\qquad
 \|(P-LG)v\|_{\ell^2}\le q^{-1/4+o(1)} .
 \tag{7}
\]
The constants implicit in \(o(1)\) allow fixed powers of \(L\) and the ordinary divisor bound.

Use the untruncated Gaussian correlations in the following formulas. The truncation errors can be made \(O(q^{-20})\) in each weighted row: retain only scaled distances \(O(L^C)\) for a sufficiently large fixed \(C\), restore the Gaussian there and use its tails on the extended lattices. The underlying truncated prime sum has \(d\ll q^{1+o(1)}\), so the original choice of the truncation constant absorbs all its entries. The estimates below use infinite Gaussian sums only over the sampled, linearized variables. No prime sum with the untruncated packets at unbounded scale is needed.

For an integer \(z\) with \(1\le z\le 2\max(N_1,N_2)\) put
\[
 {\cal G}_z=\sum_{j\in\mathbb Z}
 e^{2\pi i(q/z)j-i\pi(q/z^2)j^2} R(rj/z).
\]
This is a bounded sum up to a fixed power of \(L\). The same holds for the absolute Gaussian sum. We first calculate at a low-chart row \(n\), divide its value by \(v_n=n^{-1/2}\), and write \(N=N_1\), \(N'=N_2\). The high-chart calculation after division by \(\eta m^{-1/2}\) is the complex conjugate calculation with \(N,N'\) exchanged. Indeed the high coordinates are \(\log q-\log m\); reversal of the prime orientation gives conjugate carrier phases and the autocorrelations in the two charts are the same real even \(R\).

Choose an integer \(B=L^{O(1)}\), rounded upwards and with a sufficiently large fixed exponent to cover every endpoint displacement below. At an integer center \(z\) an unrestricted same-chart row sum with coefficient weights has the value
\[
 \sum_{h\ge1}(z/h)^{1/2}e^{iT\log(h/z)}R(r\log(h/z))
     ={\cal G}_z+O(q^{-1/2+o(1)}).                       \tag{8}
\]
On the retained support write \(h=z+j\); then \(|j|/z\le L^C/r\). The linear and quadratic terms of the carrier are \(2\pi(q/z)j\) and \(-\pi(q/z^2)j^2\), with remainder \(O(L^{3C}/r)\). Taylor's theorem gives the same power saving, with polylogarithmic factors, for the square-root weight and the argument of \(R\). There are at most \(L^{O(1)}\) retained integers. The other terms in (8) are below any required power by Gaussian decay. For example, the original log-Gaussian tail can be bounded by its endpoint and the integral with \(h=z\exp(s/r)\), so the infinite upper tail introduces no lattice-length loss. If a target cutoff \(h\le N\) is present, (8) can be used with the cutoff replaced by \({\bf1}_{z\le N}\) outside \(|z-N|\le B\). Within that band both sums are \(L^{O(1)}\). Centers \(z>2N\) give no actual outgoing prime overlap for sufficiently large \(q\).

The within-chart prime sum has an incoming term indexed by \(l=dh\) near \(n\). Its weight after division by \(v_n\) is \(\sqrt{n/l}\). All divisors \(d\ge2\) there are present, since \(h=l/d\le N\). The identity \(\sum_{d\mid l}\Lambda(d)=\log l\), (8), and \(\log l=\log n+O(L^C/r)\) give \((\log n){\cal G}_n+O(q^{-1/2+o(1)})\). The outgoing term has center \(z=dn\) and weight \((\Lambda(d)/d)\sqrt{z/h}\). Its main sum by (8) is therefore
\[
            \sum_{d\le N/n}\frac{\Lambda(d)}{d}\,{\cal G}_{dn}.           \tag{9}
\]
In addition to \(O(q^{-1/2+o(1)})\), allow an endpoint error
\(L^{O(1)}\sum_{|dn-N|\le B}\Lambda(d)/d\).
Summing the regular errors in (8) costs only \(\sum_{d\le 2N}\Lambda(d)/d\ll L\).

For the cross term set \(x=q/n,\ y=r/n\) and \(l=dm\). Since \(nl\) is integral, expansion of \(e^{-iT\log(l/x)}\) about \(l=x\) removes the linear phase and leaves \(e^{iT}e^{i\pi((l-x)/y)^2}\). After the square-root weights and correlation argument are expanded, the cross term divided by \(v_n\) is
\[
 \frac{\eta e^{iT}}y\sum_{l\ge1}\Psi((l-x)/y)
                  \sum_{\substack{d\mid l\\l/d\le N'}}\Lambda(d)
       +O(q^{-1/2+o(1)}),\qquad
 \Psi(s)=e^{i\pi s^2}\int\psi(t+s)\overline{\phi(t)}\,dt .
 \tag{10}
\]
For clarity, \(r\log(l/x)=(l-x)/y+O(L^{2C}/r)\) on \(|l-x|\le yL^C\); also \(\sqrt{n/l}=y^{-1}(1+O(L^C/r))\). The phase error is \(O(L^{3C}/r)\), and the divisor sum is at most \(\log l\). Summing these errors loses \(L^{O(1)}\), since \(y^{-1}=L^{O(1)}\) or smaller.

Rewrite the divisor sum in (10) as \(\log l-\sum_{d\mid l,\,d<l/N'}\Lambda(d)\). Replace \(\log l\) by \(\log x\) and extend the Gaussian integer lattices to all of \(\mathbb Z\) (the excluded nonpositive terms lie beyond \(r\) scaled units). In the subtracted sum replace \(d<l/N'\) by \(d\le N/n\). At an ambiguous divisor,
\[
 |dn-N|\le (r/N')L^C+|q/N'-N|+O(1)\le B,
\]
since the cutoff floors give \(q/N'=N+O(L^{O(1)})\). For each such \(d\), the absolute Gaussian mass on its multiples with the factor \(1/y\) is \(O(1/d+e/y)\ll L^{O(1)}/d\). This follows by bounding a sampled Gaussian by its supremum and its integral, and using \(d/y\ll L^{O(1)}\) in the endpoint band. Thus the same permitted endpoint error as in (9) covers these replacements.

The Fourier identity for the matched Gaussian profiles is
\[
 \widehat\Psi(\xi)=I e^{-i\pi\xi^2}R(\xi),\qquad I=e^{i\pi/4}.
\]
It follows by convolving the transform of the Fresnel phase with \(e^{i\pi\xi^2}|\widehat\phi(\xi)|^2\); the remaining Fourier integral is the real even autocorrelation \(R\). By Poisson summation, for every \(1\le d\le N/n\),
\[
 \frac1y\sum_{l\in d\mathbb Z}\Psi((l-x)/y)
   =\frac I d\sum_j e^{2\pi i (x/d)j-i\pi(y/d)^2j^2}R(jy/d)
   =\frac I d{\cal G}_{dn}.
\]
Reversing the sign of \(j\) is permitted because the quadratic phase and \(R\) are even. The full lattice has \(d=1\). Since \(\eta e^{iT}I=1\), the cross term equals
\((\log x){\cal G}_n\) **minus** (9), within the stated errors. The other prime cross orientation is absent: its centers are separated by at least \(\log 2\) for \(d\ge2\). Adding incoming, outgoing and cross rows leaves \(L{\cal G}_n\), using \(\log x+\log n=L\).

The within-chart physical Gram row on \(v\), divided by \(v_n\), equals \({\cal G}_n\) by (8), with extra error \(L^{O(1)}{\bf1}_{|n-N|\le B}\). The cross Gram row is supported within this same band up to negligible Gaussian tails: \(nm\le NN'\le q\) and \(r\log(q/(nm))\le L^C\) force \(|n-N|, |m-N'|\le L^{O(1)}\). On these bands the two coefficient weights are within polylogarithmic factors, and summing the remaining \(m\)'s costs a power of \(L\). This proves that each row of \((P-LG)v\), after division by its corresponding coherent coefficient, is bounded in absolute value by
\[
 q^{-1/2+o(1)}+
 L^{O(1)}\left({\bf1}_{|n-N|\le B}
       +\sum_{|dn-N|\le B}\frac{\Lambda(d)}d\right).               \tag{11}
\]
The analogous conclusion holds in the other chart. The parenthesis is \(O(L^{O(1)})\) uniformly. Its \(1/n\)-weighted sum is \(q^{-1/2+o(1)}\): for its divisor term group by \(h=dn\) and use
\(\sum_{|h-N|\le B} h^{-1}\sum_{d\mid h}\Lambda(d)\ll (B+1)L/N\).
Its weighted sum of squares is bounded by the same power. These two estimates prove (7).

## The first eigenvalue and the scope of the test

Write \(W\) here for the Hermitian matrix of the full Weil form in packet coordinates and put \(H=G^{-1/2}W G^{-1/2}\). The gamma comparison and pole estimate above, (7), and the bounded condition number of \(G\) show that the unit coherent vector \(v_0=G^{1/2}v/\|G^{1/2}v\|\) satisfies
\[
  |\mu|=|\langle H v_0,v_0\rangle|\le q^{-1/2+o(1)},\qquad
           \|(H-\mu)v_0\|\le q^{-1/4+o(1)} .
\]
In particular the argument following (6) now proves \(\lambda_2\ge cL\). The variational upper bound is \(\lambda_1\le\mu\). The spectral theorem (equivalently Temple's inequality) gives
\(\mu-\lambda_1\le\|(H-\mu)v_0\|^2/(\lambda_2-\mu)\); the squared projection of \(v_0\) orthogonal to the first eigenspace is at most \(\|(H-\mu)v_0\|^2/(\lambda_2-\mu)^2\). This proves (1) and the stated angle estimate. In particular the signed prime aliases are needed for the two-sided conclusion; a small coherent Rayleigh quotient by itself would give only its upper side.

One can see the small direction explicitly on the Mellin side. Before the negligible truncation, at \(s=1/2-it\) its transform is
\[
 r^{-1/2}\widehat\phi\!\left(\frac{T-t}{2\pi r}\right)
 \left\{\sum_{n\le N_1} n^{-s}
   +\eta q^{it}\exp\!\left(i\pi\left(\frac{T-t}{2\pi r}\right)^2\right)
                                  \sum_{m\le N_2}m^{s-1}\right\}.
\]
The second multiplier is the quadratic Stirling approximation at \(T\) to the factor in \(\zeta(s)=\chi(s)\zeta(1-s)\). The two sums thus have the shape of the classical unbalanced approximate functional equation; this interpretation is not used in (7). A proof of Weil positivity still needs the sign of the one small eigenvalue, the complement of this finite-dimensional space, and the coupling to that complement. Positivity on a collection of different packet spaces alone would not control cross terms between the spaces.

## The contribution from an individual displaced zero

Center the physical coordinate at \(u_0=\log N_1\), writing \(\widehat g_c(t)=e^{-itu_0}\widehat g(t)\). The products of reflected zero evaluations in the Weil form are invariant under this translation. For each fixed \(0<d_0<1/2\), uniformly in real \(\gamma\), \(|d|\le d_0\), and all \(g\) in the packet space,
\[
       |\widehat g_c(\gamma-id)|^2
       \ll_{d_0}\big(K_0^{-1}+K_0e^2\big)\|g\|_2^2 .
 \tag{12}
\]
The implicit constant can be taken independent of all sufficiently large fixed \(K_0\), with the large-\(q\) threshold depending on \(K_0\). The two squared additive Fourier transforms are \(O(e)\) uniformly at complex arguments with \(|\Im \xi|\le 1/r\). For the chirped Gaussian this follows by maximizing
\(\left|\exp(-\pi e^2\xi^2+i\pi\xi^2)\right|^2\) over \(\Re\xi\); the imaginary shift costs \(\exp(O(1/(e^2r^2)))\). The omitted Gaussian tails, even with the factor \(\exp(2\pi |u|/r)\), have negligible \(L^1\) norm. Cauchy–Schwarz in coefficient space therefore bounds the squared evaluation norm by a constant times
\[
 \frac e r\left(\sum_{n\le N_1}(n/N_1)^{2d}
             +\sum_{m\le N_2}(q/(mN_1))^{2d}\right)
     \ll_{d_0} (e/r)(N_1+N_2).
\]
The integrable endpoint powers here use \(2d_0<1\). The uniform lower physical Gram bound proves (12). Thus an individual reflected zero pair of defect bounded by \(d_0\) contributes only \(O_{d_0}(K_0^{-1}+K_0e^2)\) per unit norm, while the gap above the soft eigenspace grows as \(\log q\).

There is a stronger estimate on the coherent test itself. For a zero \(\rho=\beta+i\gamma\) with \(|\gamma-T|\le rL^C\), put \(s=1-\rho=\sigma-i\gamma\), \(t=\gamma+i(\sigma-1/2)\). For each fixed \(C\) and \(d_0<1/2\), uniformly when \(|\beta-1/2|\le d_0\),
\[
       |\widehat v_c(t)|\le q^{-1/2+o(1)} .                       \tag{13}
\]
Indeed \(\zeta(s)=0\) by reflection. Apply the classical approximate functional equation at \(x=N_1\), \(y=\gamma/(2\pi N_1)\), whose error is \(O(x^{-\sigma}+\gamma^{1/2-\sigma}y^{\sigma-1})=q^{-\sigma/2+o(1)}\). Replacing \(y\) by \(N_2\) moves only \(L^{O(1)}\) terms, at the same cost after the factor \(\chi(s)\). Stirling's formula expanded at \(T\) gives a relative error \(q^{-1/2+o(1)}\) when \(\chi(s)\) is replaced by \(\eta q^{it}\exp(i\pi((T-t)/(2\pi r))^2)\). Multiplication by the absolute sum of the dual terms costs at most \(q^{1/2-\sigma+\sigma/2+o(1)}\), so its additive error is again \(q^{-\sigma/2+o(1)}\). The bracket in the displayed Mellin formula has this bound. Multiplying by \(r^{-1/2}\widehat\phi\) and the centering factor \(N_1^{\sigma-1/2}\) gives (13); the truncation errors are negligible. [Ivić, *The Riemann zeta-function*, equation (4.10)](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/86/6d/866d1cf0-a942-4f8a-9d30-7cb3b03e1b1c/i_ivic-66.pdf)

Consequently one zero and its horizontal reflection have total absolute contribution \(q^{-1+o(1)}\) on the coherent unit test. This quantifies a difficulty with using this direction to rule out one off-line zero even once its own Weil value is known to be small.

## Distance to an exact Weil null test

The interpretation above can be upgraded to a norm statement. On the centered physical line there is a smooth rapidly decreasing test \(k_q\) in the radical of the zero-side Weil form for which
\[
       \|e^{d_0|u|}(v_c-k_q)\|_{L^2(du)}
                         \le q^{-1/4+o(1)}
           \qquad (0\le d_0<1/2\text{ fixed}).
 \tag{14}
\]
Here \(v_c(u)=v(u+u_0)\). For example take
\[
 \widehat k_q(t)=e^{-itu_0}r^{-1/2}
   \widehat\phi\!\left(\frac{T-t}{2\pi r}\right)
   \left(1-e^{-(t-i/2)^2/r^2}\right)\zeta(1/2-it),
\]
using the full Gaussian \(\phi\). The extra factor kills the pole at \(t=i/2\) with negligible effect on the carrier band. The product is entire; on each bounded horizontal strip it and each fixed derivative have rapid decay in \(|\Re t|\) by the Gaussian and polynomial vertical-strip bounds for zeta. Fourier inversion and shifts therefore give rapid decay of every physical derivative against every fixed exponential weight. All prime, gamma, pole and zero sums in the bilinear explicit formula are admissible. At each zero evaluation \(t=\gamma-i(\beta-1/2)\) the zeta argument is \(1-\rho\), also a zero. This gives \(W(k_q,h)=0\) for every admissible test \(h\), independently of RH.

The approximate-functional-equation calculation for (13) before setting \(\zeta(s)=0\) gives \(|\widehat v_c(t)-\widehat k_q(t)|\le q^{-1/2+o(1)}\) on \(|\Re t-T|\le r L^C\) for either of the two lines \(\Im t=\pm d_0\). Integrating its square over that band costs at most \(q^{-1/2+o(1)}\). Choose \(C\) sufficiently large: beyond the band the full Gaussian envelopes of both charts, including the quadratic phase at bounded imaginary shift, decay faster than any power of \(q\), even with the polynomial zeta bound and the two finite sums. To bound the truncation remainder there in \(L^2\), use Plancherel directly on each shifted line. The weighted physical tail of one discarded packet is \(O(q^{-90})\) before its center translation. The center weights and the sum of the absolute coefficients together cost only a fixed power of \(q\). The pole-killing factor at \(\Re t\) far from the carrier stays bounded on the lines under consideration. This proves the same integrated estimate on the full lines. Applying Plancherel with the exponential weights \(e^{\pm d_0u}\) yields (14). The exact null test lies in the unrestricted Weil domain. Its approximation rate explains why a nearly null vector in the finite section can occur regardless of the horizontal positions of the zeros.
