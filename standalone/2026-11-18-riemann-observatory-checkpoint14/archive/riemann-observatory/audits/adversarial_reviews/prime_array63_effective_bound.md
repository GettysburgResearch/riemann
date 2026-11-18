# An explicit global bound for the prescribed prime array

Date 2026-11-17. Write
\[
 E_{N,k}=\left\|-\frac{[\zeta(s)(k^{1-s}-1)]'}s
                  -\frac{\zeta(s)B_N(s)}s\right\|_{L^2(dt/(2\pi))}^2,
 \qquad s=\tfrac12+it ,
\]
with the anchored tapered \(B_N\) of the prime-array proof. Assuming RH, the following numerical bounds hold for every integer \(N\ge3\):
\[
 E_{N,2}\le\frac{10^{44}}{\log N},\qquad
 E_{N,k}\le\frac{10^{44}k^6}{\log N}\quad(k\ge2).
\]
They use no zero list. The constants below come from elementary Euler summation, a strip estimate and Jensen's formula. In particular, the numerical constants do not require tabulating the estimates implicit in the earlier asymptotic proof. Trudgian's primary paper uses pole removal and explicit strip interpolation in §2, Lemma 1. Here a Gaussian-weighted three-lines argument gives a sufficiently small exponent, including the Cauchy disk needed for \(\zeta'\). [Prime-array proof and exact Perron formula](jump_factorial_prime_array63_proponent.md) · [Trudgian, §2](https://arxiv.org/pdf/1406.3416v2)

## Explicit boundary and zero-count estimates

Put \(T=2+|t|\). We use
\[
 |\zeta(1/2+it)|,\ |\zeta'(1/2+it)|
 \le10^5 T^{7/16}.                                            \tag{1}
\]
This estimate is unconditional. For integer \(M\ge1\), Euler summation gives
\[
 \zeta(z)=\sum_{n\le M}n^{-z}
       +\frac{M^{1-z}}{z-1}
       -z\int_M^\infty\{x\}x^{-z-1}\,dx
 \qquad(\Re z>0,\ z\ne1).
\]
For \(|t|\ge1\), on \(\Re z=1\) use \(M=\lceil T\rceil\) to get \(|\zeta(1+it)|\le 3+\log(2T)\). For \(0<|t|\le1\) take \(M=1\), giving \(|\zeta(1+it)|\le4/|t|\). The functional equation and the exact values of \(|\Gamma(iy)|^2\) and \(|\Gamma(1/2+iy)|^2\) from reflection give
\[
 |\zeta(it)|
 =\sqrt{\frac{|t|}{2\pi}\tanh\!\left(\frac{\pi |t|}{2}\right)}
       |\zeta(1-it)|\quad(t\ne0).
\]
The square-root factor is at most \(\sqrt T\) everywhere and at most \(|t|/2\) for \(|t|\le1\). Since \(\log T\le32T^{1/32}\), these estimates and continuity at \(t=0\) give \(|\zeta(it)|\le40T^{17/32}\).

For the interpolation set \(h(z)=(z-1)\zeta(z)/(z+1)\), analytic on \(0\le\Re z\le2\), and put \(\nu=17/32\). The bounds on the edges are \(40T^\nu\) and 2, since \(\zeta(2)\le 2\) and \(|z-1|\le|z+1|\) on the strip. For any fixed real \(t_0\), apply the bounded three-lines theorem to \(h(z+it_0)e^{z^2}\). The function \(h\) has polynomial growth on the strip by the Euler formula below. The Gaussian makes the product bounded. Since \(\sup_y e^{-y^2}(1+|y|)^\nu\le2\), the left-edge bound is \(80(2+|t_0|)^\nu\), and the right-edge bound is \(2e^4<200\). Evaluating at \(z=\sigma\) gives
\[
 |h(\sigma+it_0)|\le200(2+|t_0|)^{\nu(1-\sigma/2)}.
\]
For \(7/16\le\sigma\le9/16\), one has \(|(z+1)/(z-1)|\le25/7<4\) and \(\nu(1-\sigma/2)\le425/1024<7/16\). Hence \(|\zeta(\sigma+it_0)|\le800(2+|t_0|)^{7/16}\). A Cauchy circle of radius \(1/16\) about \(1/2+it\), with \(2+|\Im z|\le2T\), gives \(|\zeta'(1/2+it)|\le 16\cdot1600\,T^{7/16}\). This proves (1).

For the polynomial bound and Jensen's formula we use one more integration in the \(M=1\) Euler formula. The periodic \(P_2(x)=B_2(\{x\})/2\) has derivative \(\{x\}-1/2\) away from integers and satisfies \(P_2(1)=1/12\), \(|P_2|\le1/12\). Integration by parts gives
\[
 \zeta(z)=\tfrac12+\frac1{z-1}+\frac z{12}
         -z(z+1)\int_1^\infty P_2(x)x^{-z-2}\,dx
 \qquad(\Re z>-1,\ z\ne1).                                   \tag{2}
\]
Consequently \(H(z)=(z-1)\zeta(z)\) has an explicit polynomial bound on \(\Re z\ge-1/2\). On the disk of radius \(5/2\) about \(2+it\), we have \(|z|\), \(|z-1|\), \(|z+1|\le3T\) and the absolute integral in (2) is at most \(1/6\). The resulting bound \(|H(z)|\le1000T^3\) includes the removable value at 1. At the center \(|H(2+it)|\ge1/2\), since the absolutely convergent reciprocal series gives \(|1/\zeta(2+it)|\le\zeta(2)\le2\). Under RH every zero with \(|\gamma-t|\le1\) is strictly inside radius 2 about that center. Jensen's formula with the two radii bounds its total multiplicity by
\[
 \frac{\log(2000T^3)}{\log(5/4)}\le100\log T.
\]
Here \(\log(2000)<11\log2\) and \(\log(5/4)\ge1/5\). We will use the consequent bounds
\[
 \sum_{|\gamma-t|\le1}m_\rho\le100\log T,\qquad
 \sum_{j\le|\gamma|<j+1}m_\rho\le200\log(j+3)\quad(j\ge0).
 \tag{3}
\]
All multiplicities are included. A possible central zero would obey the same estimates.

## Explicit log derivative bounds

Assume RH in the rest of the proof. Set \(a(s)=2^{1-s}-1\), \(F=\zeta a\), \(Q=-F'/\zeta\), \(K=\zeta'/\zeta\), and \(r_\rho=-m_\rho a(\rho)\). The completed zeta log derivative yields
\[
 K(s)=\sum_\rho m_\rho\left(\frac1{s-\rho}+\frac1\rho\right)+D(s),
 \qquad
 D(s)=c_\xi-\frac1s-\frac1{s-1}+\frac{\log\pi}{2}
                    -\frac12\psi(s/2).
 \tag{4}
\]
To bound \(c_\xi\), evaluate the completed-zeta log derivative at 2. The usual gamma factors give \(|\xi'(2)/\xi(2)|<10\), since \(|K(2)|\le\sum_{n\ge2}(\log n)/n^2<2\), \(|\psi(1)|<1\), and \(\log\pi<2\). The log-weighted sum bound follows by the first term plus the integral from 2 because the summand decreases there. For a critical zero, \(|\rho|\ge(1+|\gamma|)/3\) and \(|2-\rho|\ge|\rho|\). Thus the absolute sum of the paired fractions at 2 is at most
\[
 18\cdot200\sum_{j\ge0}\frac{\log(j+3)}{(1+j)^2}
 \le18\cdot200\cdot12.
\]
Indeed \(\log(j+3)\le4\sqrt{1+j}\) and \(\sum_{j\ge0}(1+j)^{-3/2}\le3\). This gives \(|c_\xi|<10^5\).

For \(z=\alpha+it/2\), \(1/4\le\alpha\le1\), the digamma series gives \(|\psi(z)|\le30\log T\) and \(|\psi'(z)|\le18\). To see the first estimate, split
\(\psi(z)=-\gamma_E+\sum_{n\ge0}(1/(n+1)-1/(n+z))\)
at \(n=\lceil T\rceil\). The \(n=0\) term is bounded by 5 and the remaining head by \(2(1+\log\lceil T\rceil)\). In the tail \(|z-1|\le T\) and the denominator has modulus at least \(n^2\), so that tail is at most 1. The derivative series is bounded by \(16+\sum_{n\ge1}n^{-2}\le18\). It follows on the critical line that \(|D|\le10^6\log T\) and \(|D'|\le100\).

On the left line \(z=-1+it\), the log derivative of the functional equation reads
\[
 K(z)=\log\pi-\tfrac12\psi((1-z)/2)
               -\tfrac12\psi(z/2)-K(1-z).
\]
The recurrence for \(\psi\) moves \(z/2=-1/2+it/2\) to real part \(1/2\) at cost at most 2. Also \(|K(1-z)|\le2\) by the Euler product on \(\Re(1-z)=2\). Consequently \(|K(z)|\le40\log T\). Since \(|a(z)|\le5\) and \(|a'(z)|\le4\) on that line,
\[
 |Q(-1+it)|\le 10^4\log T.                                     \tag{5}
\]

On the critical line use \(|a|\le3\), \(|a'|,|a''|\le2\). The derivative satisfies
\[
 Q'(s)=-\sum_\rho\frac{r_\rho}{(s-\rho)^2}+U(s),
 \qquad |U(1/2+it)|\le10^8\log^2 T.                           \tag{6}
\]
Here are explicit bounds for the remainder. After (4), its summand per zero divided by \(m_\rho\) is
\[
 \frac{a(s)-a(\rho)-a'(s)(s-\rho)}{(s-\rho)^2}
       -\frac{a'(s)}{\rho}.
\]
Within \(|t-\gamma|\le1\), Taylor's formula and \(|\rho|\ge1/2\) bound this by 5, so the near sum is at most \(500\log T\). In the rest of the sum the numerator \(a(s)-a(\rho)\) is bounded by 6. The unweighted remote kernel sum satisfies
\[
 \sum_{|t-\gamma|>1}\frac{m_\rho}{|t-\gamma|^2}
 \le200\sum_{j\ge1}\frac{\log T+\log(j+2)}{j^2}
 <10^4\log T.                                                \tag{7}
\]
Each distance shell \(j\le|t-\gamma|<j+1\) is covered by two unit windows, \(\log(T+j+1)\le\log T+\log(j+2)\), and \(\sum j^{-2}\le2\), \(\sum j^{-2}\log(j+2)\le12\).

For the remaining paired sum, write
\[
 P(t)=\sum_{|t-\gamma|>1}
       \frac{m_\rho|s|}{|\rho|\,|t-\gamma|}.
\]
For \(|\gamma|\le T/2\), \(|t-\gamma|\ge T/6\). This follows from \(T=2+|t|\) for \(T\ge6\), and from the remote cutoff otherwise. The ratio is then at most \(18/(1+|\gamma|)\). Summing (3) uses \(\log(T+3)\le3\log T\) and \(1+\log(T+1)\le4\log T\), and gives at most \(43200\log^2 T\). For \(T/2<|\gamma|\le2T\), the ratio is at most \(2/|t-\gamma|\). The distance shells up to \(3T+1\) have multiplicity at most \(200\log(5T+2)\le800\log T\) per shell, and the harmonic sum is at most \(5\log T\), giving \(8000\log^2 T\). For \(|\gamma|>2T\), bound the ratio by \(2T/|\gamma|^2\). A dyadic shell \(2^jT<|\gamma|\le2^{j+1}T\), \(j\ge1\), has total multiplicity at most \(600\cdot 2^jT(j+3)\log T\) by (3). Its contribution is at most \(1200\cdot 2^{-j}(j+3)\log T\). The sum over \(j\ge1\) is \(6000\log T\), at most \(12000\log^2 T\). Thus \(P(t)<10^5\log^2 T\). Adding the gamma terms \(-a'D-aD'-a''\) from (4), the near sum, (7) multiplied by 6, and \(P(t)\) multiplied by 2 proves (6).

## Full-norm error and numerical constant

The contour formula in the prime-array proof shifts from \(\Re(s+w)>1\) to \(\Re(s+w)=-1\), crossing \(w=0\) and the nontrivial zeros of zeta. There are no trivial zero residues in this strip or pole of \(Q\) at 1. With \(L=\log N\) it gives the exact identity
\[
 A_N(s)=Q(s)+\frac{Q'(s)}L+
          \frac1L\sum_\rho\frac{r_\rho N^{\rho-s}}{(s-\rho)^2}
           +I_N(s).
 \tag{8}
\]
The absolute bound (5) at the left endpoint and the log-derivative control on a sequence of heights separated from all ordinates justify the shift, as in the primary proof of this array. In particular, the critical-line estimate for \(I_N\) is
\[
 |I_N(1/2+it)|\le10^6 N^{-3/2}\log T/L .
 \tag{9}
\]
To verify the number, dominate \(|w|^{-2}\) by \((1+v^2)^{-1}\) on \(\Re w=-3/2\). Use \(\log(2+|t+v|)\le\log T+\log(2+|v|)\), with the two integrals bounded by \(4\) and \(10\), respectively, by splitting at \(|v|=1\). The same left-line estimate at \(s=1\) gives \(|I_N(1)|\le10^6 N^{-2}/L\). Moreover \(Q(1)=0\), \(|Q'(1)|\le2\) from \(Q'(1)=\gamma_E\log 2-(\log2)^2/2\), and
\[
 \sum_\rho \frac{|r_\rho|}{|1-\rho|^2}\le
 27\cdot200\cdot12 <10^5
\]
by (3) and \(|1-\rho|=|\rho|\ge(1+|\gamma|)/3\). In (8) at 1, \(|N^{\rho-1}|\le1\). Consequently \(|A_N(1)|\le10^7/L\).

For convenient norm estimates put \(Z(s)=\zeta(s)/s\). Since \(1/|s|\le6/T\), (1) gives \(|Z(s)|^2\le10^{12}T^{-9/8}\). For \(p=0,1,2\), \((\log T)^{2p}\le128^{2p}T^{2p/128}\le10^9T^{1/32}\). Integrating \(T^{-35/32}\) gives an integral less than \(32\) even in \(dt\), so
\[
 \|Z(\log T)^p\|_{L^2(dt/(2\pi))}\le10^{12}\qquad(p=0,1,2).
 \tag{10}
\]
The errors from \(U\), \(I_N\), and anchoring in \(\sqrt L\,(T_k-ZB_N)\), where \(T_k=-F'/s\), are \(-ZU/\sqrt L\), \(-\sqrt L\,ZI_N\), and \(\sqrt L\,ZA_N(1)\). Their norms are bounded by \(10^{20}\), \(10^{18}\), and \(10^{19}\), respectively, by (6), (9), (10) and \(L=\log N\ge1\).

The remaining term in that scaled error is
\[
 Z(s)\sum_\rho r_\rho\,\frac{1-N^{\rho-s}}{\sqrt L(s-\rho)^2}.
\]
For \(|t-\gamma|>1\), both \(s,\rho\) have real part \(1/2\), so the numerator has modulus at most 2. Using \(|r_\rho|\le3m_\rho\), (7) and (10), the remote term has norm at most \(10^{17}\).

For the near term let \(h_L(u)=(1-e^{-iLu})/(i\sqrt L u)\). Its squared norm in \(du/(2\pi)\) is 1 by Plancherel for \(L^{-1/2}\mathbf1_{[0,L]}\). Each near summand is \(r_\rho\zeta(s)h_L(t-\gamma)/(s(s-\rho))\). By integration of the derivative estimate (1) along the line segment \(s\) to \(\rho\), its scalar coefficient before \(h_L\) has modulus at most \(10^8 m_\rho T^{-9/16}\). Weighted Cauchy–Schwarz and the near count in (3) bound the pointwise square of the summed near term by
\[
 10^{18} T^{-9/8}\log T
 \sum_{|t-\gamma|\le1}m_\rho\,|h_L(t-\gamma)|^2 .
\]
In the integration for each zero with \(T_\gamma=2+|\gamma|\), the factor \(T^{-9/8}\log T\) is at most \(8T_\gamma^{-9/8}\log T_\gamma\). Integrating each kernel using total mass 1 and (3) therefore bounds the squared norm by
\[
 10^{19}\sum_\rho m_\rho T_\gamma^{-9/8}\log T_\gamma
 \le 10^{19}\cdot800
      \sum_{j\ge0}(2+j)^{-9/8}\log^2(2+j)
 <10^{28}.
\]
For the last numerical inequality, bound the logarithmic square by \(10^5(2+j)^{1/64}\), then the resulting series by \(1+64/7<11\). These estimates sum the whole line and all zeros, counting multiplicities, without any separation condition on distinct ordinates.

Adding the five norm bounds yields
\(\sqrt L\,\|T_k-ZB_N\|_2<2\cdot10^{20}\) for \(k=2\). Squaring gives \(E_{N,2}\le10^{44}/L\), with room in the constants.

For arbitrary \(k\ge2\), repeat the proof with \(a(s)=(k^{1-s}-1)/k^3\), which scales \(T_k,Q,r_\rho,A_N,B_N\) and \(I_N\) by \(k^{-3}\). This choice of \(a\) obeys all the displayed \(k=2\) bounds on \(a,a',a''\) on the critical line and \(a,a'\) on the left line. Indeed \(\log k\le k\) gives \(\sqrt k(\log k)^2\le k^3\) and \(k^2\log k\le k^3\), while the corresponding zero-order bounds are immediate. Also \((\log k+(\log k)^2/2)/k^3\le2\), so the anchor bound still applies. Undoing the scaling gives \(E_{N,k}\le10^{44}k^6/L\). This is a coarse effective bound for the prescribed error. It does not supply a rate of convergence of \(L E_{N,k}\) to its limiting constant.
