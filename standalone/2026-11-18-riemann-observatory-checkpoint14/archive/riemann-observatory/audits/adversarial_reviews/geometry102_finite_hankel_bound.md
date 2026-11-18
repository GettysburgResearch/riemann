# A finite Hankel witness from the rooted cosine extrapolation zero

Fix \(J\ge1\) and \(0<a<b<1\). Let \(d=b-a\), \(H=\log(b/a)\), and write the formal rooted cosine series as
\[
 M(z)=e^{(J-1)Hz+Hz^2/4}P_J^{\rm det}(z)
      =\sum_{k\ge0}\mu_k\,z^k/k!.
\]
The fixed-rank determinant proof gives \(M(0)=1\) and a real zero \(t_*\in(0,1/d]\). For \(J=1,2\) one can take \(t_*=1/d\). I derive a nonsharp explicit finite degree bound, using only an upper majorant on a circle and this zero. The Hankel statements are about the extrapolated sequence \((\mu_k)\). [Fixed-rank proof](geometry93_rank_three_barrier.md) · [Director scope](director_cue_windows_round13.md)

## Finite two-polynomial test

Suppose \(B\ge1\) bounds \(|M(z)|\) for \(|z|=R=2/d\). Take
\[
 L=\left\lceil \log_2\big(8B(B+1)\big)\right\rceil,\qquad
 p_\pm(x)=\sum_{j=0}^{L}\frac{(\pm t_* x/2)^j}{j!}.
\]
Let \(\Lambda(x^k)=\mu_k\), acting linearly on polynomials. By Cauchy's estimate, \(|\mu_k|/k!\le B R^{-k}\). In the double series for each \(\Lambda(p_\sigma p_\tau)\), the omitted pairs \(j>L\) or \(k>L\) have \(j+k\ge L+1\). Absolute summation in that total degree bounds the difference from \(M((\sigma+\tau)t_*/2)\) by
\[
 B\sum_{m>L}\left(\frac{t_*}{R}\right)^m
 \le B2^{-L}=:\epsilon .
\]
Here \(\sigma,\tau\in\{-1,1\}\), with \(|\sigma|=|\tau|=1\), and the binomial sum accounts for the two Taylor factorials. The limiting two-by-two evaluation matrix is
\[
 \begin{pmatrix}M(t_*)&M(0)\\M(0)&M(-t_*)\end{pmatrix}
 =\begin{pmatrix}0&1\\1&M(-t_*)\end{pmatrix}.
\]
Its determinant is \(-1\) regardless of the sign at \(-t_*\). In the finite matrix the diagonal product is at most \(\epsilon(B+\epsilon)\) in absolute value, and the squared off-diagonal is at least \((1-\epsilon)^2\). With \(\epsilon\le1/[8(B+1)]\), the first number is at most \(1/8\) and the second is at least \((7/8)^2\). The finite determinant is strictly negative. In particular the order-\(L\) Hankel matrix \((\mu_{i+j})_{0\le i,j\le L}\) is not positive semidefinite. The witness uses moments only through degree \(2L\). If the first diagonal \(G_{++}\) of this two-by-two matrix is negative, \(p_+\) is already a witness. If \(G_{++}>0\), take \(p_--(G_{+-}/G_{++})p_+\). If \(G_{++}=0\), take \(p_--(G_{--}+1)/(2G_{+-})\,p_+\), whose value under \(\Lambda\) after squaring is \(-1\).

## Explicit circular majorant in \(J,a,b\)

The following choice removes the need to find the coefficient maximum:
\[
 R=2/d,\qquad
 D=(2J-1)16^{2J-2}(2J-1)!\exp(1+Rd e^b),\qquad
 B=J!\,D^J\exp\big((J-1)HR+HR^2/4\big).
\]
To see this, write the oriented polynomial entry of the fixed-rank compression, before averaging, in the form
\[
 B_{ij}(p,q)=\ell\int_0^1 u_i(p+\ell t)u_j(q+\ell t)\,dt,\qquad
 \ell=1-p-q,\qquad 0\le i,j<J .
\]
The shifted Legendre polynomial \(u_i(x)=\sqrt{2i+1}P_i(2x-1)\) has absolute coefficient sum at most \(\sqrt{2i+1}\,8^i\). Indeed its unsigned monomial coefficients before normalization are \(\binom{i}{k}\binom{i+k}{k}\), with second binomial bounded by \(4^i\), while the first sum to \(2^i\). In the ring of polynomials in \(p,q\) let \(s=1+p+q\). Under coefficientwise absolute-value majorization, \(\ell\) is bounded by \(s\), and \(p+\ell t\), \(q+\ell t\) are bounded by \(2s\) for \(0\le t\le1\). Since \(s\) has constant coefficient one and nonnegative coefficients, this gives the entry majorant
\[
 \sqrt{(2i+1)(2j+1)}\,16^{i+j}s^{i+j+1}.
\]

For the formal expectation \(\mathcal E_z\) used in the compression, the coefficients in \(z\) of the expectation of any monomial \(p^\alpha q^\beta\) are nonnegative. This follows from the positive jump measure in each independent compound-Poisson exponent, whose formal cumulants are \(z m_h/2\). Thus taking absolute values for \(|z|\le R\) is bounded by the corresponding real probability expectation \(\mathcal E_R\) applied to the entry majorant. Under \(\mathcal E_R\), \(p,q\ge0\), so \(s^{i+j+1}\le s^{2J-1}\le(2J-1)!\,e^s\). Also
\[
 \mathcal E_R e^s
 =\exp\left(1+R\int_a^b \frac{e^x-1}{x}\,dx\right)
 \le \exp(1+Rd e^b).
\]
This gives \(D\) entrywise. The Leibniz determinant has \(J!\) terms, and the exponential factor in \(M\) contributes the displayed absolute bound on the circle. These inequalities include \(J=1\), where the raw entry is precisely \(\ell\) and the entry bound reduces to \(e^{1+Rd e^b}\), and \(J=2\), where the largest exponent needed is \(3\). At either rank the endpoint \(t_*=1/d\) has \(t_*/R=1/2\), so the same geometric estimate applies without a strict cutoff assumption.

## Sharp criterion at removed rank one

Set \(\sigma^2=H/2\). At \(J=1\), \(M(z)=e^{\sigma^2z^2/2}(1-dz)\), whose coefficients are the signed Gaussian moments of the density modifier \(1-dx/\sigma^2\) with respect to \(N(0,\sigma^2)\). Indeed Gaussian integration gives \(\mathbb E[Xe^{zX}]=\sigma^2z\mathbb E[e^{zX}]\), so this signed-density identity holds coefficientwise. In the orthonormal probabilists' Hermite basis \(\operatorname{He}_k(x/\sigma)/\sqrt{k!}\), \(0\le k\le L\), the order-\(L\) moment form is congruent to \(I-(d/\sigma^2)T_L\), where \(T_L\) is the symmetric Jacobi matrix with zero diagonal and neighboring entries \(\sigma\sqrt{k}\), \(1\le k\le L\). This is the compression of multiplication by \(x\) from the Hermite recurrence. Its characteristic polynomial is \(\sigma^{L+1}\operatorname{He}_{L+1}(x/\sigma)\), again by the same recurrence for tridiagonal determinants.

Consequently the **least** witness degree at \(J=1\) is the least \(L\) for which the largest zero of \(\operatorname{He}_{L+1}\) strictly exceeds \(\sigma/d\). Equality gives a null direction and leaves the form positive semidefinite. For \(L\ge1\) the last two adjacent basis vectors give \(\lambda_{\max}(T_L)\ge\sigma\sqrt L\), while the norm bound for the two truncated weighted shifts gives \(\lambda_{\max}(T_L)\le2\sigma\sqrt L\). Thus a witness requires \(L>\sigma^2/(4d^2)\), and \(L=\lfloor\sigma^2/d^2\rfloor+1\) always suffices at rank one.

The leading degree in narrow bands can also be determined directly. Use the last \(q=\lfloor\sqrt L\rfloor\) vertices of \(T_L\) and the positive first sine vector of the constant-weight path on those vertices. Every connecting entry is at least \(\sigma\sqrt{L-q+1}\). Its Rayleigh quotient is therefore at least \(2\sigma\sqrt{L-q+1}\cos(\pi/(q+1))\). Together with the upper norm bound this gives \(\lambda_{\max}(T_L)/(\sigma\sqrt L)\to2\). As \(\sigma/d\to\infty\), the strict root criterion and these bounds show that the least witness degree is asymptotic to \(\sigma^2/(4d^2)\).

This also disproves a general identification of the witness degree with the first crossing. For the fixed-ratio bands \([a,b]=[b/2,b]\) as \(b\downarrow0\), the least rank-one Hankel witness degree is asymptotic to \((\log 2)/(2b^2)\). The first crossing in raw moments occurs at \(\lfloor1/b\rfloor+1\), on the order of \(b^{-1}\). The parity sign of the crossing remains fixed along this family.

## Relation to the true window

Let \(r_0=\lfloor1/b\rfloor\). If \(2L'\le r_0\), then the Hankel matrix of order \(L'\) is positive semidefinite because all its entries agree with the true rooted cosine law, including the endpoint \(rb=1\) when present. The first crossing has known sign and occurs at \(r_0+1\). That compares one actual moment with its extrapolated counterpart. It alone supplies no sign for a Hankel quadratic form. The upper bound above uses the separate positive-zero argument and can greatly exceed the first crossing. It gives a finite witness for all fixed \(J,a,b\), without identifying the least witness degree beyond rank one or extending the arithmetic \(rb<1/2\) range. [First-crossing calculation](geometry93_rank_three_barrier.md) · [Arithmetic scope](prime79_hlz_formal_moment_obstruction.md)
