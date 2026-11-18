# A sharp arithmetic comparison at a Riemann–Siegel carrier

**Proposed unconditional calculation.** At every large real \(q\), a term from each integer \(dnm\) within \(O(\sqrt q)\) of \(q\) contributes to the interaction between the two [Mellin packet families](nov18b-weil-combs.md). For their coherent vectors with coefficients \(n^{-1/2}\), that complete prime-power interaction has a two-term asymptotic. The leading coupling is a unitary Fresnel transform. It can approach the coefficient one required to cancel the gamma contribution. The calculation below includes the individual divisors and the oscillating phase, and uses no zeta zero census.

Take fixed smooth unit vectors \(\phi,\psi\) of compact support. Choose \(R\ge1\) such that the supports lie in \([-R,R]\), and fix \(0<\kappa<1/(4R+4)\). In the notation of the comb construction put \(r=\sqrt q\), \(T=2\pi q\), \(N=\lfloor\kappa r\rfloor\). Use all indices from 1 through \(N\). The support length in the logarithmic variable is at most \(\log q+2R/r\). The separation within each family implies that only exact divisor shifts contribute to its prime term; the two families have disjoint physical supports. Let \(u,v\) denote the sums of the low and high packets with coefficients \(n^{-1/2}\) and \(m^{-1/2}\), respectively, with carriers centered at their packet locations as in the companion. Write
\[
 H_N=\sum_{n\le N}\frac1n,\quad J_x=\sum_{n\le x}\frac{\log n}{n},
 \qquad b=\log(q/N^2),\qquad E=\gamma_E^2+2\gamma_1,
\]
where \(\gamma_1=\lim_{x\to\infty}(J_x-\tfrac12\log^2x)\). Also set
\[
 D(b)=\sum_{d\le e^b}\frac{\Lambda(d)}d (b-\log d)
            -b^2/2+\gamma_E b-E,\qquad
 I=\int e^{i\pi s^2}\!\int\psi(t+s)\overline{\phi(t)}\,dt\,ds.
\]
Then, uniformly as real \(q\to\infty\),
\[
 \min_{|\eta|=1}\frac{W(u+\eta v)}{\|u+\eta v\|_2^2}
    =(1-|I|)H_N+b-\frac{E+|I|D(b)}{H_N}+o(H_N^{-1}).
 \tag{1}
\]
The constants here may depend on the fixed profiles and \(\kappa\). In particular every such fixed pair has a strictly positive asymptotic margin. However, for every \(\epsilon>0\) there exist fixed smooth profiles for which \(1-|I|<\epsilon\). The signed prime term can therefore reach \((1-\epsilon)\log q\) per unit norm for all sufficiently large \(q\), on compact smooth tests without inserting any zero locations. The relative phase may depend on \(q\).

## The exact integer sum

Inside each separate comb \(\|u\|^2=\|v\|^2=H_N\) and \(P(u)=P(v)=2J_N\), by \(\sum_{d\mid l}\Lambda(d)=\log l\) and the exact common profile on each divisor edge. In the cross term define
\[
 K(s)=\int \psi(t+s)\overline{\phi(t)}dt,\qquad \Psi(s)=e^{i\pi s^2}K(s).
\]
The scalar to be combined with its conjugate is
\[
 S=\sum_{l\ge1}\frac{e^{-2\pi i q\log(l/q)}}{\sqrt l}\,
             K(r\log(l/q))\,a(l),\qquad
 a(l)=\sum_{nmd=l,\ n,m\le N}\Lambda(d).
\]
For \(|l-q|\le C r\) put \(s=(l-q)/r\). Then
\[
 e^{-2\pi i q\log(l/q)}
      =e^{2\pi i q} e^{i\pi s^2}(1+O_R(1/r)).
\]
The entire linear oscillation cancels since \(l\) is an integer. Replacing the argument of \(K\) by \(s\) and the denominator by \(r\) similarly costs \(O_R(1/r)\) relative to the common absolute majorant. As \(a(l)\le \tau(l)\log l\ll_\epsilon q^\epsilon\) on the support, this yields
\[
 e^{-2\pi i q}S=\frac1r\sum_l \Psi((l-q)/r)a(l)+O_\epsilon(q^{-1/2+\epsilon}).
 \tag{2}
\]

## Divisor summation at the square-root interval length

Let \(Q=q/N\) and \(c(h)=\sum_{nd=h,\,n\le N}\Lambda(d)\). Exactly
\[
 a(l)=\sum_{n\mid l,\,n\le N}\log(l/n)-\sum_{h\mid l,\,h<l/N}c(h).
\]
On the support in (2), the threshold \(l/N\) differs from \(Q\) by \(O_{R,\kappa}(1)\). Only a bounded number of \(h\asymp r\) can be affected, and only a bounded number of multiples of each occur. Using \(c(h)\le\log h\) costs \(O(q^{-1/2}\log q)\) after dividing by \(r\). Replacing \(\log(l/n)\) by \(\log(q/n)\) costs \(O_\epsilon(q^{-1/2+\epsilon})\). For the resulting divisor sums apply Poisson summation on the lattice of multiples of each \(h\le Q\). The zero Fourier term is
\[
 I A,\qquad
 A=H_N\log q-J_N-J_Q+
       \sum_{d\le Q/N}\frac{\Lambda(d)}d (H_{\lfloor Q/d\rfloor}-H_N).
 \tag{3}
\]
Indeed \(c(h)=\log h-\sum_{d\mid h,\ h>Nd}\Lambda(d)\). All the latter divisors satisfy \(d\le Q/N=O_\kappa(1)\). This frequency calculation also includes endpoints at integral \(N\) or \(Q\).

Here are details for the other Fourier terms. On each dyadic \(h\asymp H\le Q\), the coefficient before Poisson summation is a finite linear combination of smooth logarithms truncated to intervals, and constants on multiples of the finitely many \(d\le Q/N\), likewise restricted to intervals. For the additive dual frequency \(j\ne0\) the phase is \(e^{\pm 2\pi i j q/h}\). The classical van der Corput second derivative estimate on any such interval or fixed-step progression bounds its partial sums by
\[
 O_\kappa\big( (|j|q/H)^{1/2} + (H^3/(|j|q))^{1/2}\big).
\]
Indeed the second derivative with respect to the progression index has order \(|j|q d^2/H^3\). Partial summation with \(h^{-1}\widehat\Psi(\pm j r/h)\), where the Fourier transform here has \(2\pi\) in the exponential, costs at most
\[
 C_{k,\Psi,\kappa}\frac{\log(2q)}H(1+|j|r/H)^{-k}
\]
including the logarithmic coefficient. Since \(H\le C_\kappa r\), summing over \(j\) and dyadic \(H\) costs \(O_{\Psi,\kappa}(q^{-1/4}\log^2(2q))\); for \(H<r\) the factor \((H/r)^k\) absorbs the first derivative-test term's factor \((r/H)^{3/2}\). This gives a power saving for the signed arithmetic sum (2) beyond the constant term in (3).

Now \(H_N=\log N+\gamma_E+O(N^{-1})\), \(J_x=\tfrac12\log^2x+\gamma_1+O(\log(2x)/x)\). Substituting \(\log q=2\log N+b\) and \(\log Q=\log N+b\) in (3) yields \(A=H_N^2+D(b)+o(1)\). Therefore \(|S|=|I|(H_N^2+D(b))+o(1)\). The signed prime term for the maximizing phase is \(4J_N+2|S|\), and the squared norm is \(2H_N\).

## The gamma comparison and the sharp coefficient

The negligible-tail argument for the combs applies off the narrower band \(|t-T|\le q^{3/4}\); on that band the actual gamma multiplier is \(\log q+O(q^{-1/4})\). The two poles cost arbitrarily small powers per unit norm. These estimates are uniform in \(\eta\), hence also hold when minimizing \(W\). The expansion \(2J_N/H_N=\log N-\gamma_E+E/H_N+o(H_N^{-1})\) now proves (1).

Convolution by \(e^{i\pi x^2}\) is unitary on \(L^2(\mathbb R)\): its Fourier multiplier is \(e^{i\pi/4}e^{-i\pi\xi^2}\), obtained by Gaussian damping. Consequently \(|I|\le1\). Equality would require one compact profile to be the conjugate Fresnel transform of the conjugate of the other, up to phase. For a nonzero compact input that transform is, up to a quadratic phase, the entire Fourier transform of a compact input, so it cannot itself be compactly supported. Conversely, after choosing one compact unit profile, approximate its target conjugate Fresnel transform in \(L^2\) by a compact smooth unit profile to make \(|I|\) arbitrarily close to one. Choose \(R,\kappa\) after this approximation. This order of choices asserts no uniform error rate in the profiles.

Formula (1) resolves the coherent two-vector comparison, including its bounded term, for fixed compact profiles. The leading coefficient alone cannot distinguish a negative mode of polynomially small size. A full estimate still needs the other arithmetic coefficients, the space between packet locations, and their cross terms.
