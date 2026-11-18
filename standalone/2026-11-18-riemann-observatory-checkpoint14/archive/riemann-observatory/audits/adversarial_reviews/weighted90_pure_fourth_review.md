# Arithmetic fourth moment past the square-root twist range

Assume RH. Fix \(0<a<b\) with \(1/8<b<1/6\), set \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\), and let \(W=\Re D(1/2+i\gamma)\) under the symmetric strict tail with mass proportional to \(|\zeta'(1/2+i\gamma)|^2/(\gamma^2+1/4)\) for \(|\gamma|>Y\). The unresolved fourth-moment input is a real one-sided twist by \(D^4\). The continuous part of the asymmetric contour calculation has a power saving even for a length \(Y^{4b}\). The reflected discrete contour still requires an improved estimate. [HLZ journal, Theorem 5 and §§4–6](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [HLZ arXiv, Theorem 2 and §§4–6](../../sources/classical63_derivative_moments/hlz2022.pdf)

## Exact moment reduction

The binomial identity is
\[
 W^4=\tfrac18\Re D^4+\tfrac12\Re(D^3\bar D)+\tfrac38|D^2|^2.
\]
For \(T\ge Y\), both mixed pairs are within the HLZ scope with a fixed \(\delta\) satisfying \(3b<\delta<1/2\). The Dirichlet coefficients of \(D^j\) are nonnegative integers bounded by \(j!\), by unique factorization and the count of ordered tuples. For mixed pairs with coefficients bounded by \(M\), put a positive baseline \(B=8(1+M)\) on the divisor closure of their combined support. On that closure the four coefficient arrays \(B+\sigma U+\tau V\), \(\sigma,\tau=\pm1\), have moduli in \([B-2M,B+2M]\), so \((B-2M)^2\ge B+2M\) gives fixed submultiplicativity. Outside the closure any supported multiple has all its divisors inside, as required. The signed sum with weights \(\sigma\tau/8\) extracts the cross real part after RH and the two outer derivatives. The same cancellation holds in the sesquilinear main kernel. \(U=V=D^2\) gives the square and the same padding with \(D^3\) gives \(E_T|D|^6=O(1)\), using the uniform fixed-order local factors and the bounded prime harmonic sum. The sixth moment also ensures uniform integrability of the fourth power.

The shifted aggregate remainder, after Cauchy extraction and division by \(A(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2\sim T(\log T)^4/(24\pi)\), is \(o(1)\) uniformly in \(T\ge Y\). Each of the finitely many repeated-prime patterns has weight \(\prod p^{-\max(u_p,v_p)}\) from the lcm, where \(u_p,v_p\) count occurrences on the two sides. Any exponent at least two costs \(O(\sum_{p>Y^a}p^{-2})=o(1)\) times bounded harmonic powers. The remaining paired primes, with counts \((1,1)\), supply a factor \(1/p\) and disappear from the reduced arithmetic-factor arguments. In the pure term every repeated prime has exponent at least two. The squarefree normalized main factors, with \(x_p=\log p/\log T\), are the finite-degree polynomials obtained by simultaneous shift scaling. The uniform errors in the local comparisons are \(O(1/\log T+\sum 1/p)\) times the lcm weight. The resulting normalized errors are integrated as aggregates. [Padding and local factors](prime70_hlz_cutoff_extension.md) · [Formal coefficients and repeat accounting](prime79_hlz_formal_moment_obstruction.md)

To pass to the strict tail let \(F(t)\) denote a weighted inclusive prefix and \(f(t)=(t^2+1/4)^{-1}\). Its strict sum is \(-f(Y)F(Y)-\int_Y^\infty f'(t)F(t)\,dt\). Both terms have scale \(Y^{-1}(\log Y)^4\) when \(|F(t)|\ll A(t)\), and the strict normalizing denominator is asymptotic to \(Y^{-1}(\log Y)^4/(24\pi)\). For a normalized prefix target given by a bounded polynomial in the \(x_p\), freezing \(t=Y\) inside those arguments has total normalized cost \(O(1/\log Y)\), by bounded derivatives and integrability of \(\log(t/Y)\) against the normalized tail kernel. This works for complex prefixes as well. The negative ordinates give the conjugate, so only a real positive-prefix estimate is needed. An estimate obtained only for \(T\ge Y^{1+c}\) for any fixed \(c>0\) leaves out the cutoff and the dominant part of the strict-tail integration.

## The asymmetric continuous term

Write \(P(s)=D(s)^4\), \(y=Y^{4b}\), and \(|\alpha|,|\beta|\ll1/\log T\). The one-sided continuous integral is
\[
 J_P=\frac1{2\pi}\int_1^T
       (\log(t/2\pi)+O(t^{-1}))\,
       \zeta(\tfrac12+\alpha+it)\zeta(\tfrac12+\beta-it)
       P(\tfrac12+it)\,dt .
\]
The same bounds apply to \(P(1/2-it)\). In the direct sharp product approximate functional equation, on \(t\asymp X\) and \(uv\le R\), the frequency pair is \(K_1=hu,\ K_2=v\) with \(h\le y\). Its product is at most \(yR\). For comparable frequencies the usual first integration by parts bounds the summand by a fixed log power times \(|K_1-K_2|^{-1}\). The divisor multiplicities and harmonic gap sum cost \((yR)^\epsilon \sqrt{yR}\). For noncomparable frequencies the bound follows by absolute summation of \(h^{-1/2}\) and \((uv)^{-1/2}\), of size \(O(\sqrt{yR}\log(2R))\). Both AFE weights have rapid product decay past \(R=X\) and first derivatives smaller by \(1/X\). Thus the total off-diagonal cost is \(O(T^\epsilon\sqrt{yX})\) per sharp block, including the extra logarithmic weight. The diagonal has \(hk=h\le y\) in the local Mellin integral. The shift to real part \(-1/4\) after annihilating the displaced zeta poles costs \(O(T^\epsilon y^{1/4}X^{3/4})\) on that block. This is the asymmetric form of the direct sharp argument.

The rapidly decreasing AFE residue error is \(O(T^\epsilon \sqrt y)\) because \(\sum_{h\le y}|[h^{-s}]P|h^{-1/2}\ll\sqrt y\). On RH the \(O(t^{-1})\) weight costs \(O(T^\epsilon\sqrt y)\) by the pointwise Dirichlet bound and Lindelöf for microscopic shifts. The two diagonal residues give exactly the one-sided specialization of HLZ (5), with its pole at \(\alpha+\beta=0\) removable. Prove on separated Cauchy circles and absorb fixed log losses before differentiating. The resulting errors are power saving for any fixed \(y\le T^\theta\), \(\theta<1\). Thus the symmetric bound \(O(T^{3/20} y^{33/20}+y^{1/2}T^{1/2+\epsilon})\) quoted from Pratt–Robles in HLZ §4.1 is not necessary here. Taken as printed with maximum length \(y\), its first term is power saving only for \(\theta<17/33\) and the Pratt–Robles smoothing hypotheses also require care. [Sharp AFE details](prime75_hlz_sharp_aggregate_review.md) · [Pratt–Robles v3](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf)

## The discrete contour and a sufficient missing estimate

Write \(a_T=1+C/\log T\), with \(C\) fixed large enough for the shifts. In the unreflected right-edge integral, \(P(s)\) is on the absolutely convergent side. In the reflected orientation it is \(P(1-s)\). Use \(\lambda\) for the auxiliary shift to avoid confusing it with zero height. Define the latter contour term by
\[
 K_{\mathrm{long}}(\alpha,\beta,\lambda;T)=
 \frac1{2\pi i}\int_{a_T+i}^{a_T+iT}
   \frac{\zeta(s+\lambda)}{\zeta(s)}
   \zeta(s+\alpha)\zeta(1-s+\beta)P(1-s)\,ds .
\]
The shifted functional equation produces the saddle phase \(e(-m/k)\) in the convention \(e(x)=e^{2\pi i x}\), with \(k\) from \(P\). Let \(c_k=[k^{-s}]P\) and
\[
 B_\beta(m)=
 \sum_{m_1m_2m_3m_4=m}\mu(m_1)m_2^{-\lambda}m_3^{-\alpha}m_4^\beta .
\]
The two candidate arithmetic sums in this orientation are
\[
 S=\sum_{k\le y}\frac{c_k}{k^{1-\beta}}
      \sum_{m\le Tk/(2\pi)}\frac{B_\beta(m)}{m^\beta}e(-m/k),
 \qquad
 M=\sum_{k\le y}\frac{c_k}{k^{1-\beta}}
      \sum_{m\le Tk/(2\pi)}\frac{B_\beta(m)}{m^\beta}
      \frac{\mu(k/(m,k))}{\varphi(k/(m,k))}.
\]
Here \(S-M\) is exactly the nonprincipal part of the additive character decomposition. With \(k=1\) in the unreflected orientation the analogous nonprincipal part is empty. There the denominator support consists of 1 alone, and the coefficient on the other side has fixed divisor bound after convolution with \(c_h\). Declaring a denominator length \(T^\eta\) for arbitrarily small fixed \(\eta>0\) meets the stationary-phase lemma's printed lower length restriction and gives a power-saving error. The principal Perron step on that side has inner length \(T/(2\pi h)\gg T^{1-\theta}\), and the reflected principal step has inner length \(Tk/(2\pi d)\gg T\) after the modulus grouping \(d\mid k\). The standard zeta zero-free shift consequently retains a fixed \(\sqrt{\log T}\) margin, and the additive principal factors sum with harmonic coefficients. More explicitly, on the long-denominator side the outer sum of errors is majorized by a fixed log power times \(\sum_{k\le y}|c_k|\tau_R(k)/k\), using \(k/\varphi(k)\le\tau(k)\). On the other side it is bounded by a fixed log power times \(\sum_{h\le y}|c_h|/h\). This is the principal residue computation of HLZ §4.3 with one coefficient supported at 1, and the range \(T^{1-\theta}\ll x\ll T^{1+\theta}\) for its Perron variable. Its three residues produce the corresponding specialization of (24), with poles removed by combining the residues before extraction.

The original contour horizontal bound is \(O(yT^{1/2+\epsilon})\), but here the horizontal terms can be reduced by choosing the good height in a short power interval. Choose \(T'\in[T,T+H]\) with \(H=T^\kappa\), \(\theta<\kappa<1\). Outside intervals of radius \(c/\log T\) about the zeros a positive proportion of this interval remains, by the classical unit-height count. There \(\zeta'/\zeta\ll \log^2T\) across the horizontal segment. For \(\sigma\) in the fixed contour strip \([-C/\log T,1+C/\log T]\) the ordinary continuous Dirichlet-polynomial mean-value bound gives
\[
 \int_T^{T+H}|P(\sigma+it)|^2\,dt
 \ll (H+y)\sum_{n\le y}|c_n|^2n^{-2\sigma}\ll Hy.
\]
Averaging the integral of \(|P|\) along the horizontal over the good subset and using classical convexity for the two zeta factors gives a simultaneous bound \(O(T^{1/2+\epsilon}\sqrt y)\), for both orientations and all microscopic shifts. If the shift of the stationary-phase segment requires endpoint connectors, the same selection can control \(P\) over the surrounding unit-height interval by also averaging its local Sobolev majorant, at the cost of fixed log powers. The lower horizontal costs \(O(T^\epsilon y)\). To restore from \(T'\) to \(T\) after the derivatives, use RH Lindelöf for \(\zeta'(\rho)\). Local Sobolev on unit intervals, the \(O(\log T)\) unit zero count and the continuous mean-value bound for \(D^2\) and its derivative bound \(\sum_{T<\gamma\le T+H}|D(\rho)|^4\ll T^\epsilon(H+Y^{2b})\), with endpoints handled by extending the continuous interval by a constant. Indeed \(\sum |[n^{-s}]D^2|^2/n=O(1)\) and differentiation costs a log. This reinstatement is \(o(T)\) after absorbing sufficiently small fixed powers in \(T^\epsilon\). The residue main terms change by at most \(O(H(\log T)^C)\) because their time factors are explicit integrals with bounded microscopic exponents and harmonic arithmetic weights. The existence argument chooses the good height for the one fixed polynomial at each \(Y,T\).

Consequently a sufficient missing estimate is
\[
 \Re\left.\partial_\alpha\partial_\beta\partial_\lambda
      (K_{\mathrm{long}}-M)\right|_{\alpha=\beta=\lambda=0}
      =o(T(\log T)^4)
\]
uniformly at such usable good heights for \(T\ge Y\), with \(P=D^4\) held fixed. The all-shift estimate \(K_{\mathrm{long}}-M=o(T\log T)\) on separated microscopic circles is a stronger sufficient condition. A proof proceeding through \(S\) would need estimates for \(K_{\mathrm{long}}-S\) and \(S-M\), or a joint estimate exploiting their cancellation. Small-conductor errors can be treated separately, or included in the displayed missing estimate.

## What prevents the direct extension

- HLZ journal Lemma 7, sourced to Conrey–Ghosh–Gonek (1998), Lemma 2, gives the stationary-phase error \(O(yT^{1/2}(\log T)^C)\). On the reflected edge the relevant length really is \(y\). The denominator \(k\) also sets the stationary cutoff \(m\asymp Tk\), so absorbing \(P\) into the bounded-divisor numerator series in both orientations is unavailable.
- On the reflected orientation, the principal-character residue sums are only one part of the saddle sum. HLZ journal Proposition 11 gives the large-modulus errors \(yT^{1/2+\epsilon}\), \(y^{4/3}T^{1/3+\epsilon}\) and \(y^{1/3+\epsilon}T^{5/6+\epsilon}\), in addition to the log-split term. Each reaches order \(T\) at \(y=T^{1/2}\), and each exceeds it by a fixed power for \(y=T^{4b}\) near \(T=Y\). In the proof the Type I cost is \(Q^2T^{1+\epsilon}/U_0\) with \(U_0=(KQT)^{2/3}\). The Type II bound includes \(QT^{1/2}\) and \(T^{1/2}U_0^{1/2}K^{-1/2}\). In the one-sided specialization \(q=k\) is allowed, corresponding to \(Q\asymp y\) and the residual modulus factor of size one. Concretely \(k'=1,d=1,q=k\) in the outer sum of §4.4 already has the nonprincipal primitive Gauss weight \(\overline{\tau(\psi)}/\varphi(k)\) in the appropriate sign convention. Squarefree products of four distinct primes contribute to those moduli. Restricting to these products does not reduce the maximal modulus by a power.
- The Bui–Heath-Brown precursor obtains a shorter-looking bound after using \(y\le T^{1/2}\). Its §3.4 pre-substitution bound includes \(yT^{1/2+4\epsilon}\), \(y^{1/2}T^{3/4+3\epsilon}\), and \(y^{1/3}T^{5/6+3\epsilon}\), each with the same square-root threshold. The small-modulus GRH remark in the HLZ journal supplies no improvement to the large-modulus or saddle terms. These barriers are limitations of the cited estimates, without a lower bound for the true error. [Bui–Heath-Brown, Lemma 2 and §3.4](../../sources/analytic79_prior_art/bui_heath_brown_1302_5018v1.pdf)

## Formal target and disposition

For four distinct primes the formal normalized kernel for \(\Re D^4\), apart from the weight \(\prod p^{-1}\), is
\[
 K_{\rm pure}(\mathbf x)=1+\sum_i(-4x_i+2x_i^3)
  +\sum_{i<j}(12x_ix_j-2x_ix_j(x_i^2+x_j^2)+6x_i^2x_j^2)
  -24e_3(\mathbf x)+24e_4(\mathbf x).
\]
I extracted this directly from the one-sided arithmetic factors in (5) and (24). In a residue tuple \((u,v,w,t)\), average \(\prod_i e^{-vx_i}\) with \(\prod_i(e^{-ux_i}+e^{-wx_i}-1)\), reflecting the outer shifts as in (24). Retain degree four of the exponential numerator multiplying \(v/((u+v)(v+w))\), and then extract the auxiliary derivative. In (5) use the average of the two extreme assignments for the \(h,k\) monomials and retain numerator degree three. For an exact coefficient check, after the auxiliary derivative the homogeneous quadratic in the outer shifts is evaluated at \((1,1),(1,2),(1,3)\) with weights \((-5/2,4,-3/2)\) to extract the cross coefficient. The constant, single-slot, pair, triple and four-slot terms come from retaining full-support monomials in respectively zero through four frequencies. Division by \(1/12\) gives the displayed normalization. The additional \(6x_i^2x_j^2\) compared with the cosine-sign-averaged kernel is specific to taking the two pure assignments.

With \(H_0=\log(b/a)\), \(m_j=(b^j-a^j)/j\), and \(d=m_1\), the predicted pure-tail limit is the integral of \(K_{\rm pure}\) against \(\prod dx_i/x_i\), namely
\[
 H_0^4+4(-4d+2m_3)H_0^3
 +6(12d^2-4dm_3+6m_2^2)H_0^2-96d^3H_0+24d^4 .
\]
If the missing reflected estimate holds, the mixed arms and the binomial weights then give the formal quartic fourth moment already obtained by the arithmetic kernel calculation on shorter bands. The CUE calculation predicts this moment since \(4b<1\) lies within its own moment window. The reduction here uses the analytic arithmetic formulas and establishes neither the missing estimate nor a transfer from CUE. [CUE window](prime84_cue_moment_window.md)
