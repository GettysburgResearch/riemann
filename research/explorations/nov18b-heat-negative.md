# Nonreal heat zeros at negative mean-spacing-squared times

**Proposed theorem for adversarial review.** Let \(L=\log X\), \(F_0\le F\le\sqrt L\), \(h=F/L\), and \(u=F/L^2\). There are absolute \(F_0,X_0,c>0\) such that for every \(X\ge X_0\) the negative-time function \(F_{-u}\) has at least
\[
                          c X/h
\]
distinct zeros with \(X<\Im s<2X\) and \(0<\Re s-1/2\le 4h\). Here \(F_{-u}(s)=\int g_u(q)\xi(s+iq)\,dq\), \(g_u(q)=e^{-q^2/(4u)}/\sqrt{4\pi u}\), and \(F_{-u}(1/2+iz)=8H_{-4u}(2z)\). In particular for any fixed sufficiently large \(F\) the number is \(\gg_F X\log X\). For all sufficiently small negative Polymath times \(t\), a nonreal zero occurs at real coordinate at most \(\exp(C/\sqrt{|t|})\), by choosing \(X=\exp(2\sqrt{F_0/|t|})\).

Rodgers and Tao and, independently, Dobner proved the existence of nonreal zeros at every negative time. The theorem here concerns simultaneous vanishing times, their dyadic heights and a narrow window of defects. The constants are unevaluated. The proof uses an unconditional dyadic gap theorem at time zero. [Rodgers–Tao](https://arxiv.org/abs/1801.05914) · [Dobner](https://arxiv.org/abs/2005.05142) · [Simonič–Trudgian–Turnage-Butterbaugh](https://arxiv.org/abs/2010.10675)

## A positive measure of physical holes

The proof of Theorem 1, §2.1 between equations (9) and (10), of Simonič, Trudgian and Turnage-Butterbaugh gives fixed \(\lambda>1\), \(p>0\) such that for all sufficiently large \(X\),
\[
 \operatorname{meas}\{T\in[X,2X]: N(T+2\pi\lambda/L)=N(T)\}>pX .       \tag{1}
\]
Here \(N\) counts all physical zeta zeros in the strip. The constants in that paper can be very small. We use only their strict positivity. Endpoints within a fixed distance of \(X,2X\) may be discarded.

Use the [physical regularity conditions (1)](nov18b-heat-local-density.md) at a center \(T\). The excluded fraction is \(O_A(F^{-A})\) with constants depending on the desired accuracy and the fixed window. For arbitrarily prescribed \(d>0\), \(B,M\) and \(\epsilon>0\), those conditions give
\[
 |(\log\xi)'(1/2+r+iv)-L/2|\le\epsilon L\qquad
 (d H\le r\le M,\ |v-T|\le BH,\ h\le H\le2),                \tag{2}
\]
on choosing the fixed window and then \(F_0\) sufficiently large. Here and below the symbols for large fixed windows may be increased between estimates. We will show that a retained \(T\) in (1) must have a negative-time nonreal zero within distance \(O(h)\) in its ordinate and with defect at most \(4h\).

## An outer zero-free cone for the negative-time source

Write \(J=F_{-u}\). For \(3h\le r\le M\) and \(|v-T|\le B r\), with any fixed \(B,M\), one has \(J(1/2+r+iv)\ne0\). In the slightly smaller cone its logarithmic derivative satisfies
\[
                     J'/J=L/2+O(\epsilon L+L/F).              \tag{3}
\]
The constants may depend on the fixed cone; the error can be made arbitrarily small relative to \(L\). In this claim the near boundary \(3h\) can be replaced by \(5h/2\) for the nonvanishing before taking a Cauchy derivative.

For the proof use \(s=1/2+r+iv\) and the integral \(J(s)=\int g_u(q)\xi(s+iq)\,dq\). For \(r\ge5h/2\) the saddle is \(s_*=s-2u(\log\xi)'(s_*)\), within \(C\epsilon h\) of \(s-h\), by contraction from (2) and Cauchy estimates. Use (2) at scale \(\max(h,\min(r,1))\); when \(r>1\) all heights here stay within a fixed window. Translate the entire integration line to \(q_*+\mathbb R\), \(q_*=(s_*-s)/i\). The gamma bound for \(\xi\) makes the connectors at infinity vanish. Divide by the stationary factor \(e^{-q_*^2/(4u)}\xi(s_*)\). On \(|x|\le h/4\) the exponent is \(-x^2/(4u)+O(\epsilon x^2/u)\). On \(h/4\le |x|\le B_1h\) the derivative estimate (2) along the translated segment, whose real displacement is \(\ge1.4h\), leaves a net bound \(-x^2/(8u)\) by choosing the input tolerance small. Indeed the real linear gamma phase is removed at the saddle and the residual log slope is \(O(\epsilon L)\).

Here are details for the remaining tails, where (2) at the target height alone would not suffice. Put \(w=s_*\), \(b=ix\). The global genus-one product gives the upper bound
\[
 \log\frac{|\xi(w+b)|}{|\xi(w)|}-\Re(b\xi'(w)/\xi(w))
  \le \sum_\rho [\log|1+b/(w-\rho)|-\Re(b/(w-\rho))] .
\]
The identity holds away from the zeros; an upper bound remains true at a zero as a limit. Every \(w-\rho\) has modulus \(\gg_B h\), and for \(h\le k\le1\) there are \(O_{B,M}(kL)\) zeros at distance \(\le k\) from \(w\). To verify this last point when \(|v-T|\) is as large as \(Br\), first consider \(k\ge c r\). The count around \(T\) over \(O_B(k)\) from the physical conditions gives the claimed estimate. For \(k<c r\), there are no such zeros if \(c\) is a sufficiently small fixed constant: their ordinates would be within \(O_B(r+h)\) of \(T\), where (1) of the source note gives \(|a|=o(r)\), whereas \(\Re w-1/2\gg r\). This also proves the separation bound. The same reasoning works on any enlarged fixed range of \(k\) by changing constants.

For \(h\le |x|\le1\), sum the near terms at \(|w-\rho|\le2|x|\) in dyadic shells using \(\log(1+|b/d|)+|b/d|\). Sum the remaining terms using \(O(|b/d|^2)\), with the ordinary unit interval bound outside the local range. The total is
\[
             O_{B,M}(L|x|(1+\log(1+|x|/h))).
\]
Thus for \(|x|\ge B_1 h\), a sufficiently large fixed \(B_1\) leaves at least \(-x^2/(8u)\) after the Gaussian, since \(uL=h\). In choosing the constants, this near-pole count only uses \(w\) with \(|\Im w-T|\le Br+O(h)\) for the original cone \(B\); \(B_1\) is chosen afterwards, and (2) is then used on that larger fixed range. For \(|x|>1\), \(|\xi(w)|\ge e^{-\pi T/4-CL}\) by (2) integrated to the Euler anchor, and the fixed-strip gamma bound works since \(h\le L^{-1/2}\). The real part of the saddle linear exponential costs at most \(O(L|x|)\) there. Altogether the stationary factor has a holomorphic relative error \(O(\epsilon)+O(e^{-cF})\). Its logarithmic derivative equals \((\log\xi)'(s_*)\) by stationarity. Differentiating the bounded relative factor by Cauchy on a disk of radius \(c h\) proves (3).

## Local analytic continuation from the cone

Suppose, toward contradiction at a retained center, that no zero of \(J\) has \(0<\Re s-1/2\le4h\) and \(|\Im s-T|\le K h\). The constant \(K\) will be fixed sufficiently large, independent of \(F,X\). Both sides of the axis have this property by reflection. We claim that (3) continues with arbitrarily small relative error to
\[
  d h\le r\le 4h,\qquad |v-T|\le B_2 h                         \tag{4}
\]
for any fixed \(d>0,B_2\). The required initial error in (3) can depend on these constants and on the desired final error; take \(K>10(B_2+20)\).

The needed normal-family bound is as follows. On a disk of radius bounded below about \(1/2+iT\) one can write
\[
 J'/J=g'+\sum_{|\rho-(1/2+iT)|<1} (s-\rho)^{-1},
        \qquad |g'|+|g''|\ll L
\]
on the inner disk of radius \(1/2\), with the core zeros counted with multiplicity. The inverse Gaussian and the ordinary gamma bound give \(|J(\sigma+iv)|\le e^{-\pi v/4+CL}\) on every fixed disk here or about \(4+iT\). At \(4+iT\) we have \(|J|\ge e^{-\pi T/4-CL}\): move its inverse Gaussian contour to the right-half-plane saddle as in the preceding proof, or use that proof directly at \(r=7/2\) together with (2). Jensen and fixed-disk Blaschke factorization about this anchor give \(O(L)\) local zeros and a zero-free remainder with the displayed derivative bounds. After passing to the symmetric core disk, each omitted local zero is a fixed distance from the inner disk. Boundary zeros of modulus one can be included or omitted in complete reflected pairs.

At \(s_1=1/2+4h+iT\), (3) bounds \(|J'/J|\ll L\). Every non-axis core pair \(a,-a\) satisfies \(|a|<|T-\gamma|/4\) by the outer cone for \(|a|>4h\) and the contradiction hypothesis for \(|a|\le4h\). Thus each reflected pair contributes real part \(\gg h/(h^2+(T-\gamma)^2)\) at \(s_1\), by the elementary paired Poisson formula in the [positive-time count](nov18b-heat-local-density.md). Axis zeros obey the same bound. In particular
\[
        \sum_{\rho\text{ in core}}\frac{h}{h^2+(T-\gamma)^2}\ll L .
\]
For \(s=1/2+hz+iT\) with \(\Re z\in[d/2,6]\), \(|\Im z|\le 2B_2+4\), the distances to all core zeros satisfy \(|s-\rho|\gg_{d,B_2} h+|T-\gamma|\). For axis zeros this is immediate. Small non-axis pairs are farther than \(Kh\) in height; large non-axis pairs are excluded in the cone, whose fixed aperture may first be taken larger than \(10(B_2+20)\). Subtracting the pole sum at \(s_1\), each resulting summand has numerator \(O_{B_2}(h)\) and denominator \(\gg_{d,B_2} h^2+(T-\gamma)^2\). The bound above proves that the holomorphic functions
\[
              z\longmapsto L^{-1}(J'/J)(1/2+hz+iT)
\]
are uniformly bounded on this fixed rescaled rectangle. They are arbitrarily close to \(1/2\) on a disk about \(z=4\) by (3). Montel's theorem and the identity theorem imply arbitrarily close approximation to \(1/2\) on the compact (4). In detail, failure at a fixed desired accuracy for arbitrarily small outer-disk error would give a convergent subsequence whose limit is identically \(1/2\), a contradiction. All domain enlargements here are fixed before the physical error is chosen.

The same factorization also compares central moduli of \(J\). On \(|r|\le r_0=2dh\), \(|v-T|\le B_2h\), one has
\[
             |J(1/2+r+iv)|\le e^{C L r_0}|J(1/2+r_0+iv)|.
                                                                    \tag{5}
\]
All core pair distance products increase in \(|r|\), since for a non-axis pair \(|v-\gamma|>|a|\) by the preceding large aperture and the absence of small nearby pairs. This uses the even quadratic distance formula from (3) of the positive-time proof. The exponential cost comes from the regular factor \(e^g\). Its absolute log derivative bound is from the fixed disk, independent of how small \(d\) is chosen.

## Consequence for the physical real gaps

Now apply the real heat integral \(\xi(s)=\int g_u(q)J(s+q)\,dq\). This is the exact semigroup identity, again by the bilateral theta transform. In the positive half wave \(W(s)=\int_0^\infty g_u(q)J(s+q)dq\), for \(|\Re s-1/2|\le h/20\), \(|\Im s-T|\le h/2\), the saddle near \(s+h\) has logarithmic derivative
\[
                        \Re(W'/W)=(1/2+O(\eta)+O(1/F))L             \tag{6}
\]
for arbitrarily prescribed \(\eta>0\). This is the stationary calculation (4) of the [positive-time proof](nov18b-heat-local-density.md) with source \(J\) in place of \(\xi\). Precisely, (3) and (4) give \(|J'/J-L/2|\le\eta L\) from displacement \(dh\) to any fixed \(M\). Cauchy gives the needed second-derivative bound \(O(\eta L/h)\) around the saddle. The central replacement (5) costs \(O(CdF)\), absorbed into the Gaussian saving by first fixing sufficiently small \(d\). After this choice take the outer-cone tolerance sufficiently small to give the required \(\eta\) in (4). The uniform relative saddle approximation gives (6) by a Cauchy derivative on a fixed multiple of \(h\).

For clarity, the Gaussian tail for real shifts \(|q|>M\) uses
\[
 |J(\sigma+q+iv)|\le e^{-\pi|v|/4}(2+|v|)^C
                 \exp(C|q|\log(2+|v|+|q|))
\]
for bounded \(\sigma\), \(u\le1\), with an enlarged absolute constant. Integrate the corresponding bound for \(\xi(\sigma+q+i(v+x))\) against \(g_u(x)\); the ratio of its right side to the displayed expression is bounded by \(e^{C|x|}(1+|x|)^C\), using \(|q|/(2+|v|+|q|)\le1\). The saddle lower bound is \(e^{-\pi T/4-CL}\) by the Euler anchor and the integrated logarithmic derivative. The other central comparisons are just the real reflection \(|J(1/2-r+iv)|=|J(1/2+r+iv)|\) and (5).

On the critical line the physical function is \(2\Re W\). Since \(d\arg W/dv=\Re(W'/W)\), (6) forces a physical critical-line zero in every interval of length \(2\pi\lambda/L\) inside this neighborhood, if \(\eta\) is sufficiently small and then \(F_0\) sufficiently large. Such an interval starting at \(T\) fits inside \(|v-T|\le h/2\). This contradicts (1). The fixed exceptional fraction for the retained-center conditions can be made \(<p/2\) by increasing \(F_0\) after all the tolerances are fixed. At least \(pX/3\) eligible centers remain after trimming the endpoints. Each must be within \(Kh\) of a non-axis zero of \(J\) of positive defect at most \(4h\). A single such zero covers at most \(2Kh\) centers, proving the count.

The theorem locates nonreal zeros when the time magnitude is a fixed multiple of the square of the local mean spacing. It supplies no nonreal zero at time zero.
