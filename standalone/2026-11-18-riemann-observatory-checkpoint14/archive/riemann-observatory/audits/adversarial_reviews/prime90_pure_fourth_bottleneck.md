# Arithmetic fourth prime-band moment beyond the square-root length

18 November 2026. Assume RH and fix \(0<a<b\) with \(1/8<b<1/6\). Let \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\) and let \(E_Y\) denote the symmetric strict derivative-weighted tail expectation. The fourth cosine moment is reduced to one pure arm. The asymmetric continuous integral can be evaluated in the needed range. The remaining estimates concern the stationary-phase replacement and a signed sum over primitive characters for the reflected discrete contour integral. The fourth moment in this band remains open by this argument. [Heap–Li–Zhao (HLZ), Theorem 5 and proof of the shifted theorem](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## Exact fourth-moment target and mixed arms

Set \(W=\Re D\), \(H=\log(b/a)\), \(d=b-a\), \(J_j=(b^j-a^j)/j\), and \(P(z)=(1-dz)^4+2J_3z(1-dz)\). The mixed arms are \(D^3\overline D,D^2\overline D^2,D\overline D^3\). Each side of each bilinear form has length at most \(Y^{3b}\). The bounded-coefficient padding and real polarization therefore put every mixed arm in the established HLZ range. The exact finite identity is
\[
 E_Y W^4=\tfrac18\Re E_Y D^4+\tfrac12\Re E_Y D^3\overline D+\tfrac38 E_Y|D|^4.
\]
The formal pure target is
\[
 m_{4,\mathrm{pure}}=4![z^4]\,e^{Hz}\bigl(P(z)+3J_2^2z^2\bigr).
\]
The verified mixed-arm limits give
\[
 E_Y W^4-4![z^4]e^{Hz+Hz^2/4}P(z)
 =\tfrac18(\Re E_YD^4-m_{4,\mathrm{pure}})+o(1).
\]
The two polynomial expressions are the rooted CUE predictions, since \(4b<1\). [CUE formula](prime84_cue_moment_window.md) · [Arithmetic polarization and transfer](prime70_hlz_cutoff_extension.md) · [Formal cosine coefficient](prime79_hlz_formal_moment_obstruction.md)

Here is the signed extraction on the arithmetic side. For four distinct primes with scaled logs \(x_i\), let \(h\) and \(k\) be the two disjoint slots, and \(\epsilon_i=1\) in \(h\) and \(-1\) in \(k\). The formal leading arithmetic kernel for each sign pattern is
\[
 K_4^{\rm cos}(\mathbf x)+6\sum_{i<j}\epsilon_i\epsilon_jx_i^2x_j^2 ,
\]
where \(K_4^{\rm cos}\) is equation (2) of prime79. To extract this identity, use \(X_h=\sum_{i\in h}x_i\), \(X_k=\sum_{i\in k}x_i\). The reflected average of the continuous kernel, before extracting \(\alpha\beta\), is
\[
\frac{(-\beta X_h-\alpha X_k)^3+(-\alpha X_h-\beta X_k)^3
-(\alpha X_h+\beta X_k-\alpha-\beta)^3
-(\beta X_h+\alpha X_k-\alpha-\beta)^3}
{12(\alpha+\beta)}.
\]
In each \(I\)-tuple \((u,v,w,t)\) use \(v/((u+v)(v+w))\) times the degree-four part of
\[
 \frac{e^t}{2}\left[
 e^{-vX_h}\prod_{i\in k}(e^{-u x_i}+e^{-w x_i}-1)
 +e^{-vX_k}\prod_{i\in h}(e^{-u x_i}+e^{-w x_i}-1)\right].
\]
Sum the three tuples and their shift reflections from prime79, differentiate the auxiliary shift at zero, and extract \(\alpha\beta\). Exact rational expansion for \(|h|=0,1,2\) gives the stated kernel after dividing by \(1/12\). The calculation evaluates the formal residue expression for the pure arm, whose sharp asymptotic is the missing step. For mixed signs repeated primes survive only as opposite-sign pairs. A paired prime contributes its harmonic mass and drops from the reduced kernel. The corresponding coefficients at lower order follow from the same signed expression by setting the unused \(x_i\) to zero, since each omitted source factor tends to 1. Within a pure arm the repeated-prime residues contribute \(o(1)\) using the lcm denominator. These facts give the mixed limits and the displayed equivalence.

Small-height and remote-tail issues can be avoided in a local proof. For \(Y\le U<V\ll Y\), the \(D^2\overline D^2\) asymptotic also shows that the total derivative-weighted absolute mass of \(D^4\) on \((U,V]\) is \(O((V-U)\log^4 Y)+o(Y\log^4Y)\), uniformly at comparable heights, with the same bound on intervals starting just below \(Y\). Here the prefix derivative moment has order \(T\log^4 T\). This follows by differentiating the continuous time factors in the aggregate main term and applying the bounded lcm and scaled Cauchy-circle estimates. It means that smooth approximations to a compact tail interval would suffice if the pure asymptotic were shown against such weights. The relative contribution beyond \(RY\) is \(O(R^{-1}(1+\log^4 R))\) by the known positive fourth-mass prefix bound and inverse-quadratic Stieltjes integration. [Fourth absolute mass bound](prime81_joint_third.md)

## The continuous integral has a larger asymmetric range

Let \(Q(s)=\sum_{h\le y}a_hh^{-s}=D(s)^4\), with \(y\le Y^{4b}\) and \(0\le a_h\le24\), and take \(T\asymp Y\). Apply the same product approximate functional equation as in prime75 to the one-sided polynomial \(Q(s)\cdot1\). The coefficients of a Fourier frequency pair have denominator \(\sqrt{K_1K_2}\), where \(K_1=hu\), \(K_2=v\), \(uv\) is the product of the two zeta summation indices, and \(h\le y\). For \(uv\le P_0\) and comparable \(K_1,K_2\), both are at most \(\sqrt{2yP_0}\). One integration by parts and the harmonic gap estimate give an off-diagonal bound \(T^\epsilon\sqrt{yP_0}\). The multiplicity of each pair is at most \(\tau(K_1)\). Outside comparability the inverse logarithm is bounded, and absolute summation gives \(O(\sqrt{yP_0}\log(2P_0))\). Summing product shells on a height block \(t\asymp X\) gives \(O(T^\epsilon\sqrt{yX})\), with the same bound after inserting the log weight. The diagonal has \(v=hu\), so the Mellin-line error costs
\[
 X^{3/4}\sum_{h\le y}|a_h|h^{-3/4}
 \ll y^{1/4}X^{3/4}.
\]
Shift uniformity and the diagonal pole cancellation are as in prime75. The \(O(1/t)\) part of the functional-equation log derivative uses the same first derivative weight bounds on each block, with the leading diagonal term bounded by \(O(X\log^{O(1)} T)\). Summing blocks, including the rapidly decaying completed-zeta AFE residues, gives \(O(T^\epsilon(\sqrt{yT}+y^{1/4}T^{3/4}))\). This saves a power for every fixed \(y\le T^\theta\) with \(\theta<1\). [Unshifted and shifted AFE estimates used here](prime75_hlz_sharp_aggregate_review.md) · [Primary product AFE](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf)

## The discrete obstruction in source notation

HLZ §4 first uses a wide rectangle, giving \(O(yT^{1/2+\epsilon})\) on the horizontal sections. Lemma 4 at the stationary-phase step §4.2 gives another \(O(yT^{1/2+\epsilon})\). These quoted errors both exceed \(T\) in the desired region \(y\asymp Y^{4b}\). The original horizontal estimate itself can be avoided for the shifted discrete generating sum: on a narrow strip \(1/2-\delta\le\sigma\le1/2+\delta\), choose a height uniformly separated from all zero ordinates by \(\gg1/\log T\). On RH, \(\zeta'/\zeta\ll\log^{O(1)}T\) there, and RH Lindelöf on the right plus the functional equation on the left bounds the product of the two shifted zeta factors by \(T^{\delta+\epsilon}\). The one-sided polynomial has absolute bound \(O(y^{1/2+\delta})\) on this strip. Thus these narrow horizontals save a power, with \(\delta>0\) sufficiently small. Moving the two narrow verticals to the absolute-convergence lines still requires endpoint control, or an analytic weight and a new stationary-phase estimate. This observation alone gives no sharpened version of Lemma 4.

In the two discrete verticals, apply the functional equation to the reflected zeta factor and use \(\eta\) for the auxiliary shift in the ratio. Define
\[
 c_{\alpha,\beta,\eta}(m)=
 \sum_{m_1m_2m_3m_4=m}
 \mu(m_1)m_2^{-\eta}m_3^{-\alpha}m_4^{\beta}.
\]
It is the Dirichlet coefficient of \(\zeta(s+\eta)\zeta(s+\alpha)\zeta(s-\beta)/\zeta(s)\). The unreflected arm has \(k=1\), \(h\) in the support of \(Q\), so every stationary phase has \(e(-m/k)=1\). It has no nonprincipal-character remainder. The reflected arm has \(h=1\) and nontrivial \(k\), so the exact nonprincipal sum after the source stationary-phase replacement is
\[
 {\cal E}(\alpha,\beta,\eta;T)=
 \sum_{k\le y}\frac{a_k}{k^{1-\beta}}
 \sum_{m\le Tk/(2\pi)}\frac{c_{\alpha,\beta,\eta}(m)}{m^\beta}
 \left[
 e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}
 \right].
\]
Here \(\alpha,\beta\) are interchanged for the reflected contour if the original orientation puts the long polynomial in the \(h\) slot. The subtraction is exactly the principal part of the additive character on the reduced modulus, including modulus 1. This is (40) with \(b(m)=c(m)\). The principal terms are the two one-sided specializations of §4.3. In their truncated Perron proofs the summation cutoff is \(Tk/(2\pi h)\), which lies between constant multiples of \(T/y\) and \(Ty\), hence has logarithm comparable to \(\log T\) throughout this range. Shiu's short-interval step therefore applies to the source choice \(U=\exp(c\sqrt{\log T})\), since the cutoff interval has length comparable to \(Tk/(h\sqrt U)\). Its weighted error after summation is \(O_A(T(\log T)^{-A})\) by the same harmonic divisor sums as in §4.3. The zero-free contour shift and the three residue extractions are uniform for these same polynomially bounded cutoffs. Thus the principal-term calculation does not impose the \(1/2\) exponent. A uniform \(o(T\log T)\) bound for the displayed sum on fixed separated shift circles of radii \(\asymp1/\log T\) would be sufficient for the normalized fourth moment, since the three shift derivatives cost \(O(\log^3 T)\). This would be needed alongside an \(o(T\log T)\) stationary-phase comparison for the auxiliary integrals and the corresponding horizontal control. Bounds solely for \(\eta=0\), where \(c_{\alpha,\beta,0}\) reduces to a two-factor convolution, cannot justify the auxiliary derivative; the logarithmic derivative produces the \(\Lambda\) convolution after differentiation.

On \(T\asymp Y\), every nonprincipal conductor \(q\mid k\) is at least the smallest band prime and thus exceeds \(Y^a\). This eliminates the Siegel-type small-modulus part of HLZ §5. It leaves the large-modulus argument §6. Even within squarefree \(k\), the conductor-\(k\) contribution is present with \(d=1\). Its dyadic \(k\asymp Q\) block is
\[
 \sum_{\substack{k\asymp Q\\k\ {\rm squarefree}}}
 \frac{a_k}{k^{1-\beta}\varphi(k)}
 \sum_{\psi\bmod k}^{*}\tau(\bar\psi)\psi(-1)
       \sum_{m\le Tk/(2\pi)}
           c_{\alpha,\beta,\eta}(m)\psi(m)m^{-\beta}.
\]
There are also lower-conductor and common-divisor blocks in \({\cal E}\). The Gauss phase is still available in this expression. HLZ (69), (74), and (77) take absolute values before the average over primitive characters. The \(Q^2\) term of the hybrid large sieve then costs \(T^\epsilon Q\sqrt T\) when the convolution length is \(X\asymp TQ\): the normalization is \(Q^{-3/2}\) and the two squared coefficient norms have product of square roots \(\ll X^{1/2}T^\epsilon\). Proposition 8 also includes \(y^{4/3}T^{1/3+\epsilon}\) and \(y^{1/3+\epsilon}T^{5/6+\epsilon}\). Each of these powers reaches \(T\) at \(y=T^{1/2}\). A uniform bound \(a_k\le24\) does not remove the \(Q^2\) term or exploit the phases \(\tau(\bar\psi)\psi(-1)\). Establishing cancellation in the signed sum above, with the exact shift dependence preserved, would address a concrete large-modulus part of the extension. The longer continuous twisted-moment literature addresses a different integral and therefore does not supply this signed discrete estimate. [HLZ §§4.2–6](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Pratt–Robles, Theorem 1.1](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf)
