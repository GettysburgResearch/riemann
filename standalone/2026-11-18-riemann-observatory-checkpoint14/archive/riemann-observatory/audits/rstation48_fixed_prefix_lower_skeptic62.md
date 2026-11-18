# Independent reconstruction of the fixed-prefix arithmetic lower bound

I reconstructed the compact zero-jet transfer in rStation 47/v1 §§3–6, including the changed parameters in rStation 48/v2 (88), and checked the two head and tail projections. The transfer is uniform over arbitrary bounded-residual sequences in the actual length-$N$ approximation space. The fixed-prefix arithmetic lower bound in Theorem 5 follows under RH with the stated coefficient constraint and norm. The proof fixes the prefix fraction and finite zero set before taking $N\to\infty$. It gives no moving-prefix result. [Paper 47/v1 primary text](../sources/ratio62_rstation48/rstation_47_v1.md) · [Paper 48/v2, Theorem 5](../sources/ratio62_q1_priority/rstation_48_v2.md)

## Step-space coefficient bound

Use $H=L^2([1,\infty),x^{-2}dx)$. For $u=\sum_{n=2}^N a_n\rho_n$, with $\rho_n(x)=\lfloor x/n\rfloor-\lfloor x\rfloor/n$, set $v_n=a_n$ for $n\ge2$ and $v_1=-\sum_{n\ge2}a_n/n$. Then $u=\sum_{n\le N}v_n\lfloor x/n\rfloor$. Its jumps are $u(j)-u(j-1)=\sum_{n\mid j}v_n$ for $j\le N$, with $u(0)=0$. Möbius inversion and counting multiples give
$$
\sum_{n=2}^N|a_n|
 \le \sum_{n\le N}|v_n|
 \le N\sum_{j\le N}\frac{|u(j)-u(j-1)|}j
 \le N\sqrt{4N+1}\ \|u\|_{[1,N+1)}.
$$
In the last step, the triangle inequality leads to the coefficients $1/j+1/(j+1)$ of $|u(j)|$; their weighted dual squared norm is $\sum_{j\le N}(4+1/[j(j+1)])\le4N+1$. This argument applies to complex coefficients. If $e=1-u$ has bounded norm even just on the first $N$ cells, this bounds the coefficient sum by $O(N^{3/2})$, since the target has norm at most 1 there. It also bounds $|u(x)|$ pointwise by $O(N^{3/2})$ because $|\rho_n|\le1$. No optimality assumption on $u$ is needed. [Paper 47, Lemma 3](../sources/ratio62_rstation48/rstation_47_v1.md)

## The new compact cutoff parameters

Put $L=\log N$, $k=\lceil L\rceil$, $R_N=\lceil4NL\rceil$. Set $B_k(z)=e^{-z}z^k/\Gamma(k)$, $\chi_k(z)=e^{-z}\sum_{j<k}z^j/j!$, $W_{k,s}=\chi_k+B_k/s$, and $h=1-W_{k,s}$. The scale is $N$, so these weights are evaluated at $x/N$. Write $C_K$ for bounds uniform on a fixed compact set $K\subset\{0<\Re s<1\}$. Since $z\chi_k'(z)=-B_k(z)$,
$$
h(z)z^{-s-1}=-s^{-1}\frac{d}{dz}\left((1-\chi_k(z))z^{-s}\right).
$$
The endpoint terms vanish and the constant Fourier coefficient of $x^{-s-1}h(x/N)$ is zero. This is exact and removes the periodic mean of every generator.

For nonzero angular frequency $\omega$, put $\xi=-i\omega$, $q=(1+\xi N)^{-1}$, $c_j=(-s)_j/j!$. The oscillatory transform is
$$
\Gamma(-s)(\xi+N^{-1})^s
\left(\sum_{j\ge k}c_jq^j-\frac{k}{s}c_k q^k\right).
$$
One can check the expression first with $\Re\xi>0$ and $\Re s<0$ by integrating the three terms of $h$ separately. The subtraction at the origin analytically continues the combined integral through $0<\Re s<1$, where the limit $\Re\xi\downarrow0$ is dominated by an integrable majorant. Expand $(1-q)^s$ and use $\Gamma(k-s)/\Gamma(k)=k\Gamma(-s)c_k$ to obtain the sum above. If $|\omega N|\ge1$, the gamma-ratio bound $|c_j|\le C_Kj^{-\sigma-1}$, $\sigma=\Re s$, and geometric summation give absolute value at most
$$
C_K k^{-\sigma}|\omega|^\sigma(1+|\omega N|^2)^{-k/2}.
$$

The period-$n$ Fourier expansion of $\rho_n=\{x\}/n-\{x/n\}$ has mean $-(n-1)/(2n)$ and nonzero coefficients $1/(2\pi i a)$ at angular frequencies $2\pi a/n$ for nonzero integers $a$ with $n\nmid a$. Integer cycles cancel. Integrate the bounded Fejér sums against the integrable cutoff kernel and then pass to the limit; the weighted frequency bound makes the integrated series absolutely convergent. For $v=N/n\ge1$, $y=|a|v$, the useful inequality is
$$
1+4\pi^2 y^2\ \ge\ (1+4\pi^2)y\qquad(y\ge1).
$$
Thus the positive-frequency majorant after taking out $C_K k^{-\sigma}N^{-\sigma}$ is bounded by
$$
(1+4\pi^2)^{-k/2}\,
v^{\sigma-k/2}\sum_{a\ge1}a^{\sigma-k/2-1}
\ll_K (1+4\pi^2)^{-k/2}.
$$
Negative frequencies give the same bound. Multiplying by the coefficient sum yields the full omitted transform bound $N^{3/2-\sigma-\frac12\log(1+4\pi^2)+o(1)}$. This verifies (48:88)'s modified Fourier exponent without inferring it merely from the least frequency.

For the physical truncation let $z_0=(R_N+1)/N=4L+O(N^{-1})$. Eventually $z_0\ge2k$. The geometric bound for the descending finite gamma terms at $z\ge z_0$ gives $|W_{k,s}(z)|\le C_Ke^{-z}z^k/\Gamma(k)$. Using the pointwise bound on $u$ gives tail at most $C_KN^{3/2-\sigma}\Gamma(k-\sigma,z_0)/\Gamma(k)$. Since the logarithmic derivative of $e^{-z}z^{k-\sigma-1}$ on $z\ge z_0$ is at most $-1/2$, the numerator is at most $2e^{-z_0}z_0^{k-\sigma-1}$. Stirling then bounds the ratio by $N^{-(3-\log4)+o(1)}$, uniformly on $K$. These are distinct estimates for distinct errors. [Paper 47, equations (9)–(19)](../sources/ratio62_rstation48/rstation_47_v1.md) · [Paper 48, equation (88)](../sources/ratio62_q1_priority/rstation_48_v2.md)

Define
$$
\mathcal L_{s,N}(f)=\int_1^{R_N+1}f(x)x^{-s-1}W_{k,s}(x/N)\,dx.
$$
Using the full Mellin transform of the generator and the two estimates above gives
$$
\mathcal L_{s,N}(u)
 =\frac{\zeta(s)}s\sum_{n=2}^N a_n(n^{-s}-1/n)+O_K(N^{-\eta_K})
$$
on fixed discs around any finite list of line zeros. Indeed the exponents on the line are $1-\frac12\log(1+4\pi^2)<0$ and $\log4-2<0$, leaving a strictly positive margin on each sufficiently small disc. The error is analytic by the finite physical integral and the full Mellin identity, which is first obtained for $\Re s>1$ and then extended using the bounded generators. Its estimates are uniform given a bound on the first $N$ cells of $e$. For the target, zero mean of $h$ gives $\mathcal L_{s,N}(1)=1/s+\int_0^1x^{-s-1}h(x/N)\,dx-\int_{R_N+1}^\infty x^{-s-1}W_{k,s}(x/N)\,dx$. The first error is bounded using $h(z)=O_K(z^k/\Gamma(k))$ at $z\le1$; the second uses the gamma tail without the coefficient factor. Both vanish with power saving. Analytic Cauchy estimates on smaller discs give the corresponding bounds for every fixed derivative. The explicit factor $\zeta$ then annihilates its full range of jets $j<m_\rho$, even though $a_n$ depend on $N$. With $T_{\rho,j,N}=(-1)^jL^{-j}\partial_s^j\mathcal L_{s,N}|_{s=\rho}$,
$$
T_{\rho,j,N}(e)=\frac{j!}{L^j\rho^{j+1}}+o(1).
$$
The convergence is uniform over sequences with the stated bound on their first $N$ cells. [Paper 47, §§4.3 and 6](../sources/ratio62_rstation48/rstation_47_v1.md)

## Prefix moments, including the drift

Fix $0<b<1$ and $X=N^b$. The constraint fixes $a_n=\mu(n)(1-\log n/L)$ for integers $n\le X$, including $a_1=1$. By divisor convolution,
$$
\sum_{n\le x} a_n\lfloor x/n\rfloor=1+\psi(x)/L\quad(1\le x\le X).
$$
Indeed $\sum_{d\mid j}\mu(d)=\mathbf1_{j=1}$ and $\sum_{d\mid j}\mu(d)\log d=-\Lambda(j)$. With $d_N=LA(1)-1$, $e=1-\sum_{n\ge2}a_n\rho_n$, and $R(x)=\lfloor x\rfloor-\psi(x)$, this gives $Le(x)=d_N\lfloor x\rfloor+R(x)$.

For clarity one can derive the integrated explicit formula needed here by applying the double Perron kernel $-(\zeta'/\zeta)(s)X^s/s^2$ to $\sum_{n\le X}\Lambda(n)\log(X/n)=\int_1^X\psi(x)\,dx/x$. Shift the right line to $\Re s=-1$ along good heights. Such heights have $\zeta'/\zeta=O(\log^2 T)$ in the fixed strip by the standard local logarithmic derivative identity, the unit zero count and choosing the heights at distance at least $c/\log T$ from all local ordinates. The quadratic denominator kills the horizontal integrals, and the functional equation bounds the left integral by $O(X^{-1})$. The residue at $s=0$ is $O(1+\log X)$, while the pole at $1$ and the nontrivial zero residues give the main and zero terms. Consequently
$$
J(X):=\int_1^X(x-\psi(x))\,\frac{dx}{x}
=\sum_\nu \frac{m_\nu}{\nu^2}(X^\nu-1)+O(1+\log X).
$$
The sum runs over distinct nontrivial zeros, and converges absolutely and uniformly on compact $X$-intervals under RH. The harmless subtraction at 1 is allowed by absolute convergence. In particular $J(X)=O(\sqrt X)$. Since $|R(x)|\ll x$ by Chebyshev, replacing $\lfloor x\rfloor$ by $x$ in $\langle R,\lfloor x\rfloor\rangle$ costs $O(\log X)$ and the remaining floor-vs-$x$ correction to $J(X)$ also costs at most $O(\log X)$. Thus $\langle R,\lfloor x\rfloor\rangle=O(\sqrt X)$ and $\|\lfloor x\rfloor\|^2=X+O(1+\log X)$ on $[1,X]$. On a sequence with $\|e\|=O(L^{-1/2})$, pairing $Le$ with $\lfloor x\rfloor$ gives $|d_N|\sqrt X=O(\sqrt L)$ and $A(1)=O(L^{-1})$.

Here is a justification of the weighted moment that avoids integrating a conditionally convergent pointwise zero sum. Integrate the absolutely convergent primitive $J$ against the derivative of $x^{-\rho}(\log x/L)^j$ on $[1,X]$. Its $O(1+\log x)$ error contributes $O_{\rho,j,b}(1)$, including the endpoint terms, since the derivative has an integrable $x^{-3/2}$ times polynomial logarithmic bound. The floor correction is also $O(1)$. For each zero term in the primitive, integrate by parts back to obtain
$$
\frac{m_\nu}{\nu}\int_0^{bL}(v/L)^j e^{(\nu-\rho)v}\,dv.
$$
The selected $\nu=\rho$ term is $(m_\rho/\rho)Lb^{j+1}/(j+1)$. All others sum absolutely after bounding the integral by $C_{j,b}/|\nu-\rho|$ using integration by parts in $v$. Under RH the exponent is purely imaginary. For large ordinates this bound is summable against $m_\nu/|\nu|$; for the finitely many nearby distinct frequencies their gaps are fixed. The drift divided by $L$ has weighted moment $O(|d_N|\sqrt X/L)=O(L^{-1/2})$. It follows that
$$
\int_1^X e(x)x^{-\rho-1}(\log x/L)^jdx
 \ \longrightarrow\ \frac{m_\rho}{\rho}\frac{b^{j+1}}{j+1}.
$$
This derives equations (85)–(87) with the actual approximate residual and no auxiliary estimate for the undeformed Möbius taper. [Paper 48, equations (85)–(87)](../sources/ratio62_q1_priority/rstation_48_v2.md)

## Tail and head Gram limits

In the inner product linear in the first argument, the representer for $T_{\rho,j,N}$ is supported on $[1,R_N+1)$ and equals
$$
x^{1-\bar\rho}\left[
(\log x/L)^j\chi_k(x/N)
+B_k(x/N)\sum_{r=0}^j\binom jr r!\frac{(\log x)^{j-r}}{L^j\bar\rho^{\,r+1}}
\right].
$$
This differentiates both $x^{-s}$ and $1/s$. After division by $L$, bump Gram terms vanish. The bump's squared norm is $O(\sqrt L)$ by the exact mass $\int_0^\infty B_k(z)^2\,dz/z=\Gamma(2k)/(2^{2k}\Gamma(k)^2)$; the fixed log polynomial is bounded on the physical interval since $\log(R_N+1)/L\le2$ eventually. Its cross norm with a main term is $O(L^{3/4})$. On $[1,N]$ the main cutoff differs from 1 by $O(1/k!)$, and its entire interval beyond $N$ contributes at most $O(\log L)$ to each Gram entry. The same-root calculation on $[X,N]$ is the exact logarithmic moment
$$
L\int_b^1 t^{i+j}\,dt
$$
up to $o(L)$. At two fixed distinct ordinates the integral over $[X,N]$ is $O(1)$ by integration by parts against the nonconstant exponential in $\log x$. Thus $\Gamma_{\rm tail}/L$ tends to the direct sum of the positive definite matrices $M_{m,b}$. This proves eventual invertibility for the fixed family. On the head $x/N\le N^{b-1}$, both $1-\chi_k$ and $B_k$ are smaller than every power of $N^{-1}$, using the gamma bounds above. The finite differentiated head pairing therefore equals the just-computed moment up to $o(1)$, by Cauchy–Schwarz and the $O(L^{-1/2})$ norm bound. Subtracting it from the full compact pairing gives exactly the tail vector $-v_{m,b}/\rho$ in the block for $\rho$.

Separately, project on the head onto $x^{1-\bar\rho}$ for one label per selected zero. Their Gram divided by $L$ tends to $bI$ by the same logarithmic integral, and their pairing tends to $bm_\rho/\rho$. These representers need no step projection because the approximation error lives in the ambient Hilbert space as well. The exact finite Gram projection inequality on each disjoint support now yields
$$
\begin{aligned}
\liminf_N L\|e\|_{[1,X]}^2&\ge b\sum_{\rho\in\mathcal F}m_\rho^2/|\rho|^2,\\
\liminf_N L\|e\|_{[X,R_N+1]}^2&\ge
\sum_{\rho\in\mathcal F}v_{m_\rho,b}^{\mathsf T}M_{m_\rho,b}^{-1}v_{m_\rho,b}/|\rho|^2 .
\end{aligned}
$$
Adding and exhausting fixed finite zero sets gives the anchored lower bound with $C_b$. It suffices to work on a subsequence with bounded scaled squared residual, since any larger liminf makes the lower claim immediate or can be tested on a bounded near-liminf subsequence. The limiting procedure never requires estimates uniform in a growing jet set. [Paper 47, §6](../sources/ratio62_rstation48/rstation_47_v1.md) · [Paper 48, equations (88)–(89)](../sources/ratio62_q1_priority/rstation_48_v2.md)

For the unrestricted comparison, the Mellin physical residual on $(0,\infty)$ is $r_A=\mathbf1_{x\ge1}+\sum_n a_n\{x/n\}$, exactly in the boundary norm by Mellin–Plancherel. On the head this is $A(1)x-\psi(x)/L$. Pairing with $x$ gives the same $A(1)=O(L^{-1})$ by the integrated formula and the bounded scaled squared norm. Extending the anchored residual by zero to $x<1$, the identity $r_A-e_A=A(1)\{x\}$ holds on all $x>0$. Since the fractional-part function belongs to $L^2(x^{-2}dx)$, the norm changes by $O(L^{-1})$, so the squared norm changes by $o(L^{-1})$. That proves the unrestricted lower bound as stated, with the prefix restriction still referring to $A$ before anchoring.

No mathematical transfer defect was found in these steps. The result uses the primary manuscripts' formulas and the classical Mellin and explicit-formula inputs. The platform's disposition is separate from this check. This reconstruction concerns the lower bound, while Theorem 5's upper construction and the finite formula for $c_m(b)$ have separate scope. [Paper 48, Theorem 5](../sources/ratio62_q1_priority/rstation_48_v2.md)
