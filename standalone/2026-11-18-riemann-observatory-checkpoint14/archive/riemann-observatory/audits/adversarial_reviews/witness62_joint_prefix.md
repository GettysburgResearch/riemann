# Independent joint-limit check of the finite Legendre prefix cost

Starting from the adjudicated finite identity
\[
 c_m(b)=m^2+2\int_1^{(1+b)/(1-b)}[P'_{m-1}(x)]^2\,dx,
 \qquad 0\le b<1,\quad P_n(1)=1,
\]
I checked both proposed joint asymptotics. The bounded crossover follows from a uniform derivative estimate on the power series. The large-regime estimate uses a positive Laplace integral and controls its derivative directly even near both edges. This is a finite polynomial result with no arithmetic moving-prefix interpretation. [Exact identity and scope](director_prefix_cost_round6.md)

## Bounded crossover parameter

Let \(r=m^2b/(1-b)\), \(n=m-1\), and \(F_m(s)=P_n(1+2s/m^2)\). The Legendre binomial formula gives
\[
 F_m(s)=\sum_{k\ge0}\frac{a_{m,k}s^k}{(k!)^2},\qquad
 a_{m,k}=\prod_{j=1}^k\left(1-\frac1m-\frac{j(j-1)}{m^2}\right)
 \quad(0\le k<m),
\]
with \(a_{m,k}=0\) for \(k\ge m\). The product comes from
\(\binom{n}{k}\binom{n+k}{k}m^{-2k}\). Each factor is in \([0,1]\). For \(k<m\), the inequality \(1-\prod_j(1-u_j)\le\sum_j u_j\) gives
\[
 0\le1-a_{m,k}\le \frac{k}{m}+\frac1{m^2}\sum_{j=1}^k j(j-1)
                  \le \frac{k+k^3}{m}.
\]
For \(k\ge m\), the same bound is immediate. Hence \(F_m\) converges to \(F(s)=I_0(2\sqrt{s})=\sum_{k\ge0}s^k/(k!)^2\) uniformly in \(C^1([0,R])\) with error \(O_R(1/m)\). This follows by summing the majorized coefficients and their derivatives, including at \(s=0\).

The affine change of variables gives \(c_m(b)/m^2=1+\int_0^r[F'_m(s)]^2ds\). The derivative \(F'(s)=I_1(2\sqrt s)/\sqrt s\) has continuous value one at zero. The modified Bessel derivative identities \(I'_0(z)=I_1(z)\), \(I'_1(z)=I_0(z)-I_1(z)/z\) give
\[
 \frac{d}{ds}\left[I_0(2\sqrt{s})^2-I_1(2\sqrt{s})^2\right]
   =\frac{I_1(2\sqrt{s})^2}{s}.
\]
The bracket has value one at zero. Squaring in the uniform \(C^1\) estimate and integrating therefore proves, uniformly for \(0\le r\le R\),
\[
 \frac{c_m(b)}{m^2}
   = I_0(2\sqrt r)^2-I_1(2\sqrt r)^2+O_R(1/m).
\]

## Large \(m\sqrt b\), including boundary sequences

Put \(\eta_*=\operatorname{arcosh}((1+b)/(1-b))=2\operatorname{arctanh}\sqrt b\) and \(q(\eta)=1-e^{-2\eta}\). For \(\eta>0\), the positive Legendre integral gives
\[
 P_n(\cosh\eta)=e^{n\eta}J_n(q(\eta)),\qquad
 J_n(q)=\frac1\pi\int_0^\pi(1-q\sin^2(\theta/2))^n\,d\theta .
\]
The integral representation also follows by summing the integrals of powers of \(\cosh\eta+\sinh\eta\cos\theta\) into the Legendre generating function. For every \(0<q\le1\) with \(K=nq\to\infty\), the change \(\theta=2u/\sqrt K\) gives
\[
 J_n(q)\sim \frac1{\sqrt{\pi K}}.
\]
Indeed, for fixed \(u\), \(nq\sin^2(u/\sqrt K)\to u^2\) and the logarithm remainder has size \(O(u^4/n)\). On the scaled integration interval, \(\sin(\theta/2)\ge\theta/\pi\), so the rescaled integrand is dominated by \(e^{-4u^2/\pi^2}\). This proves the claim along every sequence with \(K\to\infty\), and therefore uniformly as the threshold \(K\) grows.

To take the derivative, use the exact identity
\[
 P'_n(\cosh\eta)=\frac{e^{n\eta}}{\sinh\eta}
                 \left(nJ_n(q)+q'(\eta)\partial_qJ_n(q)\right).
\]
For \(n\ge2\), differentiate the polynomial under the integral. The factor \(\sin^2(\theta/2)\) is at most \(\theta^2/4\), and the remaining factor is at most \(\exp(-(n-1)q\theta^2/\pi^2)\). Thus \(|\partial_qJ_n|\le Cn K^{-3/2}\), uniformly once \(K\) grows. Since \(0\le q'\le2\), its contribution relative to \(nJ_n\) is \(O(K^{-1})\). This justifies the derivative estimate without differentiating an asymptotic or requiring the point \(q\) stay away from 0 or 1.

Now \(q(\eta_*)=4\sqrt b/(1+\sqrt b)^2\asymp\sqrt b\), and \(q(\eta_*/2)\ge q(\eta_*)/2\). Therefore \(m\sqrt b\to\infty\) supplies uniform \(K\to\infty\) on the whole interval \([\eta_*/2,\eta_*]\). Since \(q=2e^{-\eta}\sinh\eta\), there
\[
 2[P'_n(\cosh\eta)]^2\sinh\eta
  =(1+o(1))\frac{n e^{(2n+1)\eta}}{\pi\sinh^2\eta}.
\]
Write \(H=2n+1\) and \(h=\eta_*/2\). At the endpoint, substitute \(y=H(\eta_*-\eta)\). Relative to \(e^{H\eta_*}/(H\sinh^2\eta_*)\), the integral of \(e^{H\eta}/\sinh^2\eta\) over this interval becomes
\[
 \int_0^{Hh} e^{-y}
      \left(\frac{\sinh\eta_*}{\sinh(\eta_*-y/H)}\right)^2dy .
\]
Since \(Hh\to\infty\), the ratio tends to one for each fixed \(y\). Also its logarithm, including the square, is bounded above by \(2(y/H)\coth h\). Here \(\coth h\le1+1/h\) and \(\coth h/H\to0\), so the integrand is eventually bounded by \(e^{-y/2}\). This gives a limit of one uniformly along the joint-limit sequences, including when \(\eta_*\to\infty\).

For \(0\le\eta<h\), positive Taylor coefficients make \(P'_n(x)\) nondecreasing on \(x\ge1\). Thus this part of \(2\int[P'_n]^2\,dx\) is at most \(2(\cosh h-1)[P'_n(\cosh h)]^2\). Divide by \(e^{2Hh}/\sinh^2(2h)\), the scale of the main term. The derivative estimate at \(h\) bounds this ratio by
\[
 Cn\,\frac{\cosh h-1}{\sinh h}\cosh^2h\,e^{-Hh}.
\]
For \(h\le1\) it is \(O(nh e^{-Hh})\to0\). For \(h\ge1\) it is \(O(n e^{-(H-2)h})\to0\). The initial \(m^2\) term is negligible as well: its ratio to \(e^{H\eta_*}/\sinh^2\eta_*\) is \(O(m^2\eta_*^2e^{-H\eta_*})\) when \(\eta_*\le1\) and \(O(m^2e^{-(H-2)\eta_*})\) otherwise. Both vanish. As \(n/H\to1/2\), the resulting asymptotic is
\[
 c_m(b)\sim
 \frac{e^{(2m-1)\eta_*}}{2\pi\sinh^2\eta_*}
 =\frac{(1-b)^2}{8\pi b}
       \left(\frac{1+\sqrt b}{1-\sqrt b}\right)^{2m-1}
 \qquad (m\to\infty,\ m\sqrt b\to\infty).
\]

The endpoint cutoff only discards a contribution controlled by monotonicity and the derivative estimate at its half-height. In particular the proof requires no unproved uniform expansion on \(0\le m\sqrt b\ll1\). Conversely the compact-\(r\) asymptotic does not give an error bound for unbounded \(r\). These two precise asymptotic regimes do not establish any uniformity for the arithmetic approximation theorem with a moving prefix.

## Intermediate comparison scale

For fixed \(\lambda>0\), take \(r=\lambda m^{4/3}\), \(b=r/(m^2+r)\), and write \(F(r)=I_0(2\sqrt r)^2-I_1(2\sqrt r)^2\). The standard fixed-order large-argument expansion
\[
 I_\nu(z)=\frac{e^z}{\sqrt{2\pi z}}
       \left(1-\frac{4\nu^2-1}{8z}+O(z^{-2})\right)
\]
gives \(F(r)\sim e^{4\sqrt r}/(8\pi r)\): the leading terms of the two squares cancel, leaving their first correction. The prefactor of the proven large-\(m\sqrt b\) asymptotic for \(c_m(b)/m^2\) is \((1-b)/(8\pi r)\). Moreover, \(\eta_*=2\operatorname{arsinh}(\sqrt r/m)\). If \(x=\sqrt\lambda\,m^{-1/3}\), then
\[
 (2m-1)\eta_*-4\sqrt r
 = (4m-2)(x-x^3/6+O(x^5))-4mx
 \longrightarrow -2\lambda^{3/2}/3.
\]
Because \(b\to0\), the ratio \([c_m(b)/m^2]/F(r)\) tends to \(\exp(-2\lambda^{3/2}/3)\). The estimates are uniform for \(\lambda\) in compact subsets of \((0,\infty)\). This calculation concerns the finite cost comparison on this scale. [DLMF, large-argument expansion of \(I_\nu\)](https://dlmf.nist.gov/10.40.E1)
