# Independent review of the sharp moment, finite partials and weighted variation

18 November 2026. I checked the sharp continuous term and the finite-height certificate, then obtained a sharper explicit unconditional upper bound for the critical-line derivative series. The polynomial tail diagnostic is kept separate from the analytic majorants. RH is required for interpreting the critical-line series as the full tapered-array limit. No canonical files were edited. [Sharp continuous term](prime64_q2_sharp_j.md) · [Original finite certificate](prime64_q2_partial_tail_observation.md)

## Sharp continuous term

The direct fixed-ratio AFE proof gives the claimed $O(T^{3/4}(1+\log T)^4)$ error on the two Cauchy circles. With $|a|=c/\log T$ and $|b|=2c/\log T$, the smallest possible $|a+b|$ is $c/\log T$. Thus the pole annihilator $G_d(w)$ costs at most $(1+\log T)^2$ times a fixed polynomial in $w$ times the Gaussian. The four completion poles are separated for $t\ge1$ and the other completion factor at each is away from its poles. Their exponentially small residues survive division by the gamma factors. The first Dirichlet phase is $(n/m)^{it}$, and reflection of the completed factors gives shifts $(-b,-a)$ in the dual while retaining that phase.

For $|\operatorname{Im}w|\le t/2$, each gamma argument in the interpolation of the numerator and denominator has imaginary part bounded away from zero by a fixed multiple of $t$ when $t$ is large. Stirling and the trigamma series give the stated power of $t$ and $1/t$ derivative gain. For the remaining imaginary heights, the sum of the two numerator absolute imaginary parts is at least the sum for the two denominator parts. This follows from the opposite signs of the unshifted heights and the triangle inequality after the common translation by $\operatorname{Im}w/2$. The Gaussian then controls the remaining polynomial factors and derivatives. Moving the weight contour to $-1/4$ for products below the block height crosses only the Mellin pole at zero, with residue one and zero derivative. Moving right for larger products gives rapid decay. The actual bound is uniform for both weights including the dual gamma prefactor.

At the fixed ratio $(k/h)^{it}$ the zero frequency is exactly $hm=kn$, hence $m=ku,n=hu$ for coprime $h,k$. Off the diagonal, one integration by parts retains both sharp endpoint terms. Among comparable $m,n$, the coefficient cancels the factor in the inverse logarithmic gap, leaving $O(1/|kn-hm|)$. At fixed $m$ the gaps are distinct nonzero integers, so a product cutoff $mn\le P$ costs $O(\sqrt P(1+\log P))$. Outside comparability the phase inverse is bounded, and the bound $2\sqrt P(1+\log P)$ for the unweighted coefficient sum follows by summing $n^{-1/2}$ first. The stated dyadic product decay absorbs the shifts and extends both estimates beyond $P=X$. On the diagonal, the auxiliary pole of $\zeta(1+d+2w)$ is killed by $G_d$, and the $-1/4$ Mellin line leaves the asserted $O(X^{-1/4}(1+\log T)^2)$ pointwise error. Its integral is $O(X^{3/4}(1+\log T)^3)$ with the logarithmic weight. Endpoints $t=1,T$ and the main-term extension to $0$ are harmless by local integrability. This confirms the sharp $J$ input without a shrinking time-smoothing parameter. The $O(1/t)$ term in the functional-equation log derivative is separate and small enough by the prior strip estimate. [Primary product AFE](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf)

## Finite certificate and original Hardy splice

I checked the full-polynomial and partial-sum SHA-256 manifests against their files. The sharp-$J$ note hash is `873bd6e5485b9cf243bc1d54ff419683c8b54ca923426ed64ece0c66283a7ecd`. The finite script hash is `3f60c973d0ccba1d27c395d1fafbcbc46f4d853de78278f56768e16e5424ea54`; its imported symbolic evaluator has `b4a4e6972a9c359b9d5de32498d594f472cf2cf1c2183560b3aafcb20e1eaea1`. The pinned 128-bit and 160-bit JSON hashes are respectively `ee8a5484e52434dbd109af9b56de0debf8bffbc9322b4ba2275058dcc40d8989` and `fce5524c5fb7fd0c15a75c7ee825a193848b84e94b760c478206f3f764b0a5d8`.

In FLINT 3.6.0, the C documentation and implementation of `acb_dirichlet_zeta_nzeros` give the multiplicity-counted all-zero positive count through the supplied height. The C implementation of `acb_dirichlet_zeta_zeros` obtains certified Hardy zeros and sets the real coordinate to $1/2$. Thus one should not infer off-line completeness from that latter routine alone. The script instead compares the former exact integer at $Y+2^{-10}$ to the same number of disjoint positive critical-line enclosures strictly below $Y$. The interval derivative excludes zero at each enclosure. These checks exhaust the inclusive all-zero count, exclude any additional zero at the cutoff or in the margin, and certify all zeros in the finite positive range as simple. The eta series excludes a central ordinate, and complex conjugation supplies the negative contribution. Evaluation of $\zeta'$ is via an analytic Arb complex Taylor series at each enclosed root. The quotient-squared norms and exact outward dyadic endpoints are valid by interval arithmetic. This uses no RH assumption. [FLINT documentation](https://flintlib.org/doc/acb_dirichlet.html) · [Finite script](../../scripts/prime64_q2_partial_tail_observation.py)

The new 128-bit replay returned the three counts $29,202,649$ at heights $100,400,1000$. Both independent replay JSON files matched their pinned counterparts byte for byte. The 160-bit replay at $10000$ certifies $10142$ roots, with the pinned dyadic interval lying strictly between $0.61649875288731141829$ and $0.61649875288731141830$. The previously audited centered Hardy formula (2), independently evaluated at $Y=10000,J=8$ at 160 bits, gives $5.21886541544856297077222122895\ldots<5.218866$. Adding this to the finite upper endpoint gives $C_2<5.83537$. This upper bound does not involve the quartic model. The near agreement of the model totals is a numerical check of scale, and no numerical bound for its remainder was obtained. [Centered Hardy majorant](prime64_main_term_moments.md)

## Weighted variation and a tighter explicit bound

Put $q(t)=\sqrt2\,e^{-itd}-1$, $d=\log2$, and use the earlier two-sided cubic cutoff $\varphi$ on $[0.9T,2.1T]$. The complex function $f=\varphi q Z$ has both components zero at each selected critical-line zero. Apply the two-sided Rolle argument separately to $\operatorname{Re} f$ and $\operatorname{Im}f$. On each component one has a stationary point in every intervening gap and both outer endpoint derivatives are zero. Therefore the sum of the squares of sampled component derivatives is at most the integral of the absolute product of that component's first and second derivatives. The component stationary points may differ. Pointwise Cauchy–Schwarz in two dimensions, followed by the same inequality in time, gives
$$
\sum_{T<\gamma\le2T}|\zeta'(1/2+i\gamma)Q_2(1/2+i\gamma)|^2
 \le\int |f'||f''|\,dt\le\|f'\|_2\|f''\|_2.
$$
This removes the maximum bound on $|Q_2|^2$ at the sampled roots. Reflection supplies only a factor two. The derivation counts each distinct root, with any multiple-root terms vanishing.

I checked the same vector argument and the rounded constants in the companion vector note and reproduced its analytic bound $1.790675702477948744\ldots$ at $Y=10000$. The following separate choices improve the finite-height constant. Use $M=\lceil T/2\rceil$, $b_M=(\log M)/2$, $B_M=b_M+d$ and $\ell_n=\log n-b_M$. The coefficients of $P(s)Q_2(s)$ are $-1$ at odd $n\le M$, $1$ at even $n\le M$, and $2$ at even $M<n\le2M$. All other coefficients vanish. The original $M$ terms contribute diagonal norm at most $b_M^{2j}(\log M/(2j+1)+1.15)$. The extra evens contribute at most $2(d+2/M)B_M^{2j}$ to the diagonal, by summing $2/k$ over $M/2<k\le M$. For example $\sum_{M/2<k\le M}1/k\le\log(M/\lfloor M/2\rfloor)\le d+2/M$ for both parities.

In the weighted Hilbert correction, use the actual nonzero support and the local gap $2/(n+2)$ for extra evens. If $M$ is odd, the first tail even $n=M+1$ instead has gap at least $1/(n+1)$ and costs at most an additional $2B_M^{2j}$. For all tail evens the ordinary weight before the exception is $(n+2)4/(2n)=2+4/n$. There are at most $(M+1)/2$ of them. Thus the local-gap correction divided by $3\pi$ is at most the diagonal norm upper bound above plus $Mb_M^{2j}+(M+3)B_M^{2j}$. In particular the gap adjustment is applied to the first tail index even when it borders the original support.

For $V\ge400$ write $h=\log V$, $r=1+(d+\log(1.005))/h$ and $c_*=0.5025$. Set
$$
s_j=\frac1{2j+1}+\frac{1.15+2(d+4/V)r^{2j}}h,\qquad
v_j=2^{-j}\sqrt{\left(1.2+\frac{3\pi}{V}\right)s_j
       +\frac{3\pi}{h}\bigl[c_*+(c_*+3/V)r^{2j}\bigr]} .
$$
For $T\ge V$, the centered polynomial norms of $Q_2P$ for degrees $j=0,1,2$ are bounded by $v_j\sqrt T(\log T)^{j+1/2}$. This follows from the two preceding estimates with $b_M\le(\log T)/2$, $B_M\le(\log T+d+\log(1.005))/2$, and $M/T\le c_*$. The constants decrease with $V$.

For the remainder use the original $e_j=12 j!4^j V^{-3/8}h^{-j-1/2}$ and the real-axis product rule. This avoids a disk maximum for $Q_2$ itself. Let $p_0=1+\sqrt2$, $p_1=\sqrt2\,d$, $p_2=\sqrt2\,d^2$. Then the normalized bounds on the remainder after multiplying by $q(t)$ are $p_0e_0$, $p_0e_1+p_1e_0/h$, and $p_0e_2+2p_1e_1/h+p_2e_0/h^2$. Combining these with the centered phase terms gives
$$
\begin{aligned}
a_0&=v_0+p_0e_0,\\
a_1&=v_1+0.67v_0/h+p_0e_1+p_1e_0/h,\\
a_2&=v_2+1.34v_1/h+(0.67^2+1/V)v_0/h^2
                  +p_0e_2+2p_1e_1/h+p_2e_0/h^2.
\end{aligned}
$$
The cutoff norms in the vector bound therefore give the two-sign coefficient
$$
K_{\rm w}(V)=2\bigl(a_1+15a_0/(Vh)\bigr)
  \bigl(a_2+30a_1/(Vh)+600a_0/(Vh)^2\bigr).
$$
Use this coefficient in the earlier dyadic sum with $J=8$. The 128-bit tail majorant at $Y=10000$ is $1.7412013229555915479809633484\ldots$. With the exact outward finite interval this gives
$$
\boxed{0.61649875288731141829<C_2<2.35771}.
$$
At height $10^7$ it gives a tail majorant below $0.005901712$. A complete finite derivative sum through that height of width less than $0.00025$ would give an enclosure narrower than one percent of the existing certified lower bound. Such a larger finite census was not computed.

I also checked the companion's thin-block limiting argument. For a fixed relative block length $\eta$ and outer margins $\delta T$, replace $1.2$ in the leading diagonal coefficient by $\eta+2\delta$. All other terms are lower order with $\eta,\delta$ fixed. The weighted factor is then $2(\eta+2\delta)/\sqrt{960}$ per block. Summing heights in ratio $1+\eta$ multiplies it by $(1+\eta)/\eta$ in the leading coefficient. Taking the large-height limit first, then $\delta\downarrow0$ and $\eta\downarrow0$, yields the unconditional tail limsup $2/\sqrt{960}$. This is compatible with the smaller RH-conditional asymptotic coefficient $1/(12\pi)$. [Companion vector estimate](prime65_q2_vector_rolle.md) · [Independent Arb script](../../scripts/positivity65_weighted_rolle_checks.py)
