# Real heat zeros at the mean-spacing scale outside a single exceptional set

**Proposed theorem for independent review.** Let \(L=\log X\), take \(F_0\le F\le\sqrt L\), and let \(h_0=F/L\). Given \(A>0\), outside a subset of \([X,2X]\) of measure \(O_A(XF^{-A})\), each ordinate \(T\) has the following property simultaneously for every \(u\) with \(F/L^2\le u\le1/8\): every zero of \(F_u\) of imaginary part \(T\) is on \(\Re s=1/2\) and simple. Here \(F_u(s)=\mathbb E\xi(s+N(0,2u))\); in Polymath's variables the physical height is \(2T\) and time is \(4u\). At each such time the number of nonreal or multiple zeros in the dyadic block is \(O_A(X L F^{-A})\), counted with multiplicity. The constants \(F_0,X_0\) may depend on \(A\). We in fact obtain the same exclusion within a fixed small multiple of \(h_0\) of each retained ordinate.

Thus \(F\to\infty\) can grow arbitrarily slowly before taking a density-one conclusion. The heat scale \(1/L^2\) is the square of the order of the mean zero spacing. The exceptional set can contain the locations of genuine zeta defects. The argument controls the actual deformed function pointwise on the retained region; it requires no independence of zero ordinates.

## Simultaneous controls on the physical zero set

Use zeros \(\rho=1/2+a+i\gamma\) of \(\xi\), counted with multiplicity. We use Selberg–Jutila density and Fujii's even increment moment, in the forms recorded by Rodgers in Theorems 2.2 and 2.4. For fixed \(R\), any \(0\le s\le 2R\), and each fixed \(k\), these imply
\[
 N(1/2+y,3X)\ll XL e^{-c yL},\qquad
 \frac1X\int_X^{2X}|N(T+s)-N(T)-sL/(2\pi)|^{2k}dT
      \ll_{k,R} [\log(2+sL)]^{2k}.
\]
The second statement uses Riemann–von Mangoldt and telescopes increments longer than one. The deterministic main-term correction is \(O_R(1)\) on this dyadic range. Negative increments obey the same estimate by translation. [Rodgers, *A central limit theorem for the zeroes of the zeta function*](https://arxiv.org/abs/1404.3080)

Choose a sufficiently large constant \(R\), specified in terms of fixed margins below. Except on a set of measure \(O_{A,R}(XF^{-A})\) one has at once
\[
 \begin{split}
 |N(T+d)-N(T)-dL/(2\pi)|&\le C_R F^{3/4}(1+|d|/h_0)^{3/4}
                                      &&(|d|\le R),\\
 |a|&\le C F^{-1/4}h_0(1+|\gamma-T|/h_0)^{3/4}
                                      &&(|\gamma-T|\le R).
 \end{split}                                                     \tag{1}
\]
For counts use a grid first on \(|d|\le h_0\) with mesh at most \(h_0 F^{-1/4}\), then on each shell \(r\le |d|\le 2r\) with \(r=2^j h_0\), with mesh comparable to \(r(rL)^{-1/4}\). Include endpoints, and use the same full shells up to \(2R\). The number of grid points on a shell is \(O((rL)^{1/4})\). The increment moment and Markov at threshold \((rL)^{3/4}\) give a total failure fraction on that shell \(O_{k,R}((rL)^{1/4-3k/2}\log^{2k}(2+rL))\). Monotonicity of \(N\) fills the grid because the expected count across one mesh interval costs only the same threshold. Sum geometrically, increasing \(k\). On the innermost range replace \(r\) by \(h_0\). For zero defects, centers in each shell with a violation lie within distance \(2r\) of a zero with \(|a|L\gg(rL)^{3/4}\). Reflection and the density theorem bound their total fraction by \(O(rL\exp[-c(rL)^{3/4}])\). Sum again including the innermost range. One-sided choices of endpoint counts have no effect on the measure statement.

## The logarithmic derivative on the right of a retained center

Fix any constants \(M,B>2\) and \(0<d_0<1/20\). Given \(\varepsilon>0\), choose \(R\) sufficiently large in terms of these, then take \(F_0\) sufficiently large. At every center satisfying (1), uniformly for
\[
 h_0\le h\le1,\quad |v-T|\le Bh,\quad d_0 h\le r\le M,
\]
there is no zero at \(s=1/2+r+iv\) and
\[
             |(\log\xi)'(s)-L/2|\le\varepsilon L .            \tag{2}
\]
This is a complex absolute bound. For nonvanishing, the second part of (1) gives \(|a|\ll_B F^{-1/4}h\) when \(|\gamma-T|\le (2B+4)h\).

For (2), subtract the logarithmic derivative at \(s_1=1/2+2+iv\). At this anchor the Euler series and Stirling give \(L/2+O(1)\). The Hadamard product expresses the difference as the absolutely convergent sum of
\[
 (r-a+i(v-\gamma))^{-1}-(2-a+i(v-\gamma))^{-1}.
\]
Beyond \(|\gamma-T|>R\), the strip bound and the unit interval zero count give \(O_M(L/R)\) for the whole difference when \(R>2B+2M+10\). The same bound holds for the continuous comparison with density \(L/(2\pi)\), including both signs of the ordinate. Indeed the shells beyond height \(X\) have only the extra factor \(O(\log(2+|\gamma-T|))\) in their numerators.

In the remaining sum replace each \(a\) by zero after pairing \(a,-a\). For a denominator \(z=r+i(v-\gamma)\) the average correction is \(a^2/[z(z^2-a^2)]\), bounded by \(2a^2/|z|^3\) when \(|a/z|\le1/2\). For \(|\gamma-T|\le (2B+4)h\), (1) bounds the number of terms by \(O_B(hL)\) and the ratio by \(O_{B,d_0}(F^{-1/4})\). The total error there is \(O_{B,d_0}(L F^{-1/2})\). On a dyadic shell \(w\le|\gamma-T|\le2w\) beyond that range, \(|z|\gg w\) and \(|a/z|\ll F^{-1/4}(h_0/w)^{1/4}\). There are \(O_R(wL)\) terms; summing the errors geometrically costs \(O_{R,B,d_0}(L F^{-1/2})\). The same argument applies to the denominator with real part 2.

For the resulting projected sum subtract the continuous density on \([-R,R]\) by Stieltjes integration by parts. The first line of (1) bounds the error by endpoint terms \(o_R(L)\) as \(F\to\infty\), and a constant times
\[
 \int_{-R}^R \frac{F^{3/4}(1+|d|/h_0)^{3/4}}
                       {r^2+(v-T-d)^2}\,dd\ll_{B,d_0} L F^{-1/4}.
\]
For example on \(|d|\ll_B h\) the estimate follows from \(r\ge d_0h\), and outside from integrating \(|d|^{-5/4}\). The same applies at \(r=2\). On the full real line the integral of the difference of the projected kernels is zero: both have symmetric integral \(\pi\) for positive real parts, with the same imaginary translation. This proves (2) on taking \(R\) first and \(F_0\) next. In a slightly smaller region Cauchy's formula gives \(|(\log\xi)''|\ll \varepsilon L/h\), enlarging the region in (2) by fixed factors when applying it.

A useful bound at the unprotected real parts is
\[
 |\xi(1/2+r+iv)|\le |\xi(1/2+r_0+iv)|
       \quad (|r|\le r_0),\qquad r_0=2d_0 h .                \tag{3}
\]
Here \(|v-T|\le Bh\). For a reflected zero pair the product of the squared distance factors at real displacement \(r\) is
\[
 P(r)=(r^2+(v-\gamma)^2+a^2)^2-4r^2a^2 .
\]
As a convex quadratic in \(r^2\), it is at most \(P(r_0)\) on the indicated interval if \(r_0^2+2(v-\gamma)^2\ge2a^2\). For near zeros \(|a|<d_0h\) by (1). For the other zeros within \(R\) we have \(|a|\le|v-\gamma|\), and outside \(R\) this follows from \(|a|\le1/2\). Critical-line factors themselves increase with \(|r|\). The comparison passes to the entire function: the centered even function \(\xi(1/2+z)\) has its genus-zero product over paired roots \(\{w,-w\}\) in \(z^2\), with a constant prefactor. One can take complete conjugation and reflection orbits, so comparisons of the distance factors pass to the product. This proves (3) without dividing by a zero on the axis.

## Heat exclusion

Put \(h=uL\). When \(h\ge 0.7\) the [uniform forward bound](nov18b-heat-forward.md) already gives the result for large \(X\). Hence take \(h_0\le h\le 0.7\) and \(D=hL\ge F\). We give details for bounded \(|\Im s-T|\le h/4\). Choose the auxiliary constants in the order described below. For \(s=1/2+y+iv\), \(-h/20\le y\le1/2\), the positive wave
\[
 W(s)=\int_0^\infty g_u(q)\xi(s+q)\,dq
\]
has the saddle approximation
\[
 W(s)=\exp(-(s_*-s)^2/(4u))\,\xi(s_*)\,[1+O(\varepsilon)+O(e^{-cD})],
 \qquad s_*=s+2u(\log\xi)'(s_*).                            \tag{4}
\]
Constants can be chosen uniformly on a fixed enlargement of the indicated height interval, and for \(-h/12\le y\le 1/2+h/12\).

Indeed (2) puts the fixed point in \(B(s+h,C\varepsilon h)\) by contraction, since \(u|(\log\xi)''|\ll\varepsilon\) there. The points in question have real displacement \(>h/2\). Deform \([h-h/4,h+h/4]\) to \(s_*-s+[-h/4,h/4]\) with straight connectors. Taylor expansion at the stationary point has main term \(-x^2/(4u)\) and error \(O(\varepsilon x^2/u)\). The integral equals the right side of (4) with the indicated relative error; the Gaussian tails and the connectors cost \(O(e^{-cD})\) in saddle units. Also
\[
 \left|\log\frac{|e^{-(s_*-s)^2/(4u)}\xi(s_*)|}
                        {e^{-h^2/(4u)}|\xi(s+h)|}\right|
       \ll \varepsilon^2 D,                                  \tag{5}
\]
by expanding the combined exponent near \(s+h\), whose first derivative after subtraction of the Gaussian slope is \(O(\varepsilon L)\).

For real \(q\ge0\) outside the local segment, if \(r=y+q\ge r_0\) and \(r\le M\), integrating (2) in real part gives the following log bound relative to \(e^{-h^2/(4u)}|\xi(s+h)|\), before Gaussian normalization:
\[
             -(q-h)^2/(4u)+\varepsilon L|q-h| .
\]
Since \(|q-h|\ge h/4\), this is \(\le-(q-h)^2/(8u)\) for small fixed \(\varepsilon\). If \(|r|\le r_0\), replace \(|\xi|\) by the comparator at \(r_0\) using (3), at an extra cost \(O(d_0D)\) in the logarithm of the same bound. If \(r<-r_0\) here, \(|r|\le h/12\) and \(y<0\). Reflecting to \(|r|\) in the real part costs at most \(D/12\), but now \(0\le q<h/12\), giving a Gaussian penalty at least \((11/12)^2 D/4\) before small errors. These losses still leave \(\gg D\) exponential saving. In all cases this beats (5).

When \(r>M\), the growth bound for \(\xi\) in the [Gaussian calculation](nov18b-heat-persistence.md) and the lower bound at \(s+h\) cost \(O(L+q\log(2+T+q))\) before Gaussian decay. For the lower bound integrate (2) to the absolute-convergence anchor \(1/2+2+iv\), giving \(|\xi(s+h)|\ge e^{-\pi v/4-C L}\) with an absolute \(C\). Taking \(M\) large, the Gaussian dominates because \(u\le0.7/L\); the total is negligible in (5). This proves (4). In particular the constants can be chosen by fixing a small \(d_0\) and a large \(M\) from the global growth estimate, then small \(\varepsilon\), large \(R\), and finally large \(F_0,X_0\).

On \(|y|\le h/20\) the stationary main factor in (4) has logarithmic derivative \((s_*-s)/(2u)=(\log\xi)'(s_*)\) by analytic implicit differentiation. The quotient in (4) is uniformly within \(1/2\) of one on a complex neighborhood of radius \(c h\), on taking \(\varepsilon\) small. Its Cauchy logarithmic derivative is \(O(1/h)=O(L/F)\). It follows that \(\Re(W'/W)\ge L/3\) here. The two exact waves \(F_u(s)=W(s)+W(1-s)\) therefore cannot cancel for \(0<y\le h/20\), since \(|W(1/2+y+iv)|>|W(1/2-y+iv)|\). At \(y=0\), the real oscillation \(2\Re W\) has only simple zeros by the same phase derivative.

For \(h/20\le y\le1/2\) use the full Gaussian integral for \(F_u(s)\). Its positive saddle is still (4). The part where \(r=y+q\ge r_0\), including negative \(q\), has the same Gaussian comparison just proved. The part \(|r|\le r_0\) costs \(O(d_0D)\) as above with \(|q-h|\gg h\). For \(r\le-r_0\), reflect to \(p=-r\ge r_0\). Relative to the same positive anchor the exponent is at most
\[
    -yL-\frac{(p+y-h)^2}{4u}+\varepsilon L|p-y-h|
                   \qquad(p\le M).
\]
This follows directly from (2) between \(p\) and \(y+h\). Since \(|p-y-h|\le |p+y-h|+2y\), the last term is absorbed into half the square and \(2\varepsilon yL+O(\varepsilon^2D)\). The loss \(yL\ge D/20\) beats (5) with a fixed margin. For \(p>M\) use the same global Gaussian tail as before. The full integral is thus nonzero. Reflection and the de Bruijn strip exhaust all possible real parts. These estimates are simultaneous for every allowed \(h\) and for a fixed neighborhood of size \(\gg h_0\) of the retained ordinate, as claimed.

The failed source estimate at an exceptional center is precisely specified by (1). No conclusion about every exceptional cluster follows from its total measure.

## Counting the exceptional heat zeros with multiplicity

For every \(A>0\) and every \(F/L^2\le u\le1/8\), the number of zeros of \(F_u\) in \(X\le\Im s\le2X\) that are nonreal in the \(\Xi\) coordinate or have multiplicity greater than one is
\[
                         O_A(X L F^{-A}),                     \tag{6}
\]
counted with multiplicity. The total number is asymptotic to \(XL/(2\pi)\), uniformly in these times, by Polymath15, Theorem 1.5(iv). The zero count requires further localization since a zero set itself has zero Lebesgue measure.

First, the preceding argument extends the exclusion at a retained center \(T\) to a cone. If \(F_u(1/2+y+iv)=0\) with \(y>0\), then
\[
                         |v-T|>4y+h/4 .                      \tag{7}
\]
For \(y\le h/20\) this only enlarges the previous height neighborhood to a fixed multiple of \(h\), already allowed in (2). For \(h/20\le y\le1/2\) set \(H=h+y\), use (2) and (3) at scale \(H\), and allow \(|v-T|\le5H\). The source estimates hold up to \(H\le2\) simply by enlarging the fixed ranges in their proof. On the saddle disk and its horizontal connectors the displacement is comparable to \(H\), and the disk radius needed for the saddle is at most \(h/3\). Thus \(u|(\log\xi)''|\ll \varepsilon h/H\), and all the local comparisons continue to hold. The small-real-part cutoff is now \(r_0=2d_0H\). Its replacement in (3) costs \(O(d_0HL)\) while \(|y+q|\le r_0\) implies \(|q-h|\ge(1-2d_0)H\), giving a penalty \(\gg H^2/u\ge HL\). All remaining tails have the estimates above, including the reflected loss \(yL\) on \(p\ge r_0\). This proves (7). It gives the same exclusion estimate for \(1/2\le y\le2\) if needed by increasing \(M,B,R\); the classical strip already excludes actual zeros there.

Second, for \(h\le r\le2\) the full stationary approximation with \(y=r\) at a retained \(T\) gives
\[
                  |F'_u/F_u(1/2+r+iT)|\ll L .                \tag{8}
\]
Its proof uses the previous full integral result, including uniform relative error less than \(1/2\), on a surrounding complex disk of radius \(c h\), and differentiates by Cauchy after division by the stationary factor as in (4). This covers the top of the displayed range by extending the fixed bounded strip slightly. For a nonreal heat zero \(1/2+a+i\gamma\), (7) gives \(|a|<|\gamma-T|/4\) after reflection. For a real heat zero take \(a=0\). Averaging the two reflected pole contributions, with \(d=T-\gamma\), gives
\[
 \frac12\sum_{\pm}\Re\frac{1}{r\pm a+id}
  =\frac{r(r^2+d^2-a^2)}{((r-a)^2+d^2)((r+a)^2+d^2)}
  \gg \frac{r}{r^2+d^2}.
\]
The deformed centered function has its even order-one Hadamard product, so the real parts sum to \(\Re(F'_u/F_u)\) in the symmetric convention. The inequality and (8) give at most \(C rL\) heat zeros of all types with \(|\gamma-T|\le r\), for \(h\le r\le2\). [Polymath15, Proposition 3.1 and equation (105)](https://arxiv.org/abs/1904.12438)

Finally define the good centers by (1) also on the fixed enlargement \([X-3,2X+3]\), using the same \(L\); its complement has measure \(O_A(XF^{-A})\) by the same moment arguments. Every exceptional heat zero in the original interval is at least \(h/4\) from this good set, decreasing the fraction \(1/4\) to a fixed absolute constant if needed in the simplicity neighborhood. The open set of points farther than half that threshold from the good set contains all exceptional ordinates. Each component containing such an ordinate has length \(\ell\gg h\), and the sum of the lengths inside the enlargement obeys the same exceptional measure bound. If \(\ell\le1\), a good center lies within \(O(h)\) of its boundary, so the local count just proved at radius \(\max(h,\ell+O(h))\) gives \(O(\ell L)\) roots; near the upper radius endpoint one can instead use the unit interval estimate. Components of length \(\ell>1\), including any component meeting an edge of the enlargement and the original interval, contain \(O(\ell L)\) roots by Polymath15's uniform unit interval bound. Summation proves (6). When \(h\ge0.7\) there are no exceptional zeros by the forward theorem.
