# Which correlations can pay for negative mass after removing the Gaussian average?

Status — Proposed native diagonal asymptotic, necessary off-diagonal estimate under an off-line zero, and a separate synthetic obstruction to unsigned scale inversion.

Use the local curvature \(D^{\rm loc}\) and the constants in [the positive-deficit identity (4)](detector-diffusion-nov18.md). That identity gives the original cumulative negative mass to within 2400 from a signed sum over \(X^{0.998}\le n\le X^{1.002}\). The analysis below recombines all four dyadic carriers before squaring this sum.

## 1. A diagonal estimate for the actual arithmetic source

Put \(h=\log2,\ t=\epsilon u,\ \epsilon=10^{-6},\ d=0.002\), and
\[
 c=(-6,\,15/\sqrt2,\,-6,\,3/(2\sqrt2)),\qquad
 K_u(z)=\sum_{j=0}^3 c_j R_t(z-jh){\bf1}_{|z-jh|\le du}.
\]
For \(u>0\),
\[
 D^{\rm loc}(u)=\sum_{m\ {\rm odd}}\frac{\mu(m)}{\sqrt m}K_u(u-\log m).
\]
Indeed for odd \(m\) the four coefficients \(q(2^jm)\) equal \((-6,15,-12,3)_j\mu(m)\), apart from the additive 6 at \(n=1\); that endpoint lies below the local interval. All higher 2-adic valuations give zero.

The diagonal after summing the dyadic carriers has the unconditional asymptotic
\[
 \sum_{m\ {\rm odd}}\frac{\mu^2(m)}m K_u(u-\log m)^2
 =
 \frac4{\pi^2}\left(\frac{33}{2\sqrt2}-12\right)^2
 \frac{4(\sqrt2-1)}{3\sqrt\pi}\, t^{3/2}
 +O(\sqrt t)\qquad(u\to\infty).
 \tag{1}
\]
To verify the arithmetic replacement, the odd squarefree count equals \(\kappa x+O(\sqrt x)\) with \(\kappa=4/\pi^2\), by inserting \(\mu^2(n)=\sum_{k^2\mid n}\mu(k)\) on the odd integers. The summand as a function of real \(m\) is supported on \([e^{(1-d)u}/8,e^{(1+d)u}]\). The total variation of \(K_u^2\) before the \(1/m\) weight is \(O(t)\), since each truncated \(R_t\) is nonnegative, unimodal and bounded by \(O(\sqrt t)\). Partial summation therefore replaces the sum by \(\kappa\int_{\mathbb R}K_u(z)^2dz\) with error \(O(t e^{-(1-3d)u/2})\), including the jumps at the cutoffs.

The omitted Gaussian tails at \(|z-jh|>du\) have exponentially small \(L^2\) norm. In the uncut integral,
\(\langle R_t,R_t(\cdot-v)\rangle=\|R_t\|_2^2-\|R_t-R_t(\cdot-v)\|_2^2/2\). For fixed \(v\) the last squared norm is \(O(\sqrt t)\), by the translation bound \(|v|\,\|R_t'\|_2\) and \(R_t(z)=\sqrt t R_1(z/\sqrt t)\). Thus the leading factor from all shifts is \((\sum c_j)^2\). With Fourier convention \(\widehat f(\xi)=\int f(z)e^{-i\xi z}dz\), the distributional equation \(R_1''=G_1-\delta_0\), where \(G_1\) is the centered heat kernel at time one, yields
\[
 \|R_1\|_2^2=\frac1\pi\int_0^\infty\frac{(1-e^{-v^2})^2}{v^4}\,dv
 =\frac{4(\sqrt2-1)}{3\sqrt\pi}.
\]
Integrate by parts once and use
\(\int_0^\infty(e^{-a v^2}-e^{-b v^2})\,dv/v^2=\sqrt\pi(\sqrt b-\sqrt a)\).
These identities give (1).

For large \(u\), \((D^{\rm loc}-Au-B)_+\le(D^{\rm loc})^2/[4(Au+B)]\). Consequently the diagonal costs \(O((1+T)^{3/2})\) after integration through \(T\). This part by itself is subpower in \(Y=e^T\). The off-diagonal terms retain signs both from Möbius coefficients and from the actual combined kernels.

## 2. A large reduced ratio is forced by a zero

At a fixed time \(u\), expand \((D^{\rm loc})^2\) into ordered pairs \(m,n\) of odd positive integers. Write \(m=gr,\ n=gs,\ (r,s)=1\). The sum of absolute values of **all grouped pair terms having \(\max(r,s)\le R\)** is
\[
 \ll R(1+u)^2\qquad(R\ge1,\ u\ge4).
 \tag{2}
\]
In fact each kernel costs \(O(\sqrt t)\); its support forces \(g\le e^{(1+d)u}\). The common divisor contributes at most \(\sum_{g\le e^{(1+d)u}}1/g\ll1+u\), and \(\sum_{r,s\le R}(rs)^{-1/2}\ll R\). This crude bound is uniform in \(R\) and includes the primitive diagonal.

If a zero has displacement \(a=\Re\rho-1/2>0\) and multiplicity \(m_0\), the [positive isolator](detector-positive-isolation-nov18.md) and the integrable error in the local curvature identity show that, for some fixed \(b>0\) and all sufficiently large \(T\),
\[
 \int_{T-b}^T(D^{\rm loc}(u))_+\,du\gg e^{aT}T^{m_0-1}.
\]
Cauchy–Schwarz bounds the integrated square below by a constant times \(e^{2aT}T^{2m_0-2}\). Given \(0<\eta<2a\), use (2) with \(R=e^{(2a-\eta)T}\). Its integrated cost is negligible. The signed contribution of the complementary pairs to this square is therefore **positive and at least a constant times \(e^{2aT}T^{2m_0-2}\) on every such window**. At least one reduced factor exceeds \(e^{(2a-\eta)T}\), and the common divisor of those pairs is less than \(e^{(1+d-2a+\eta)T}\). This gives a necessary source-specific sector for an off-line zero, with all multiplicities and either possible order of the pair. No upper bound on that remaining sector has been shown.

### Requiring different large-prime factors as well

The large reduced-ratio condition can be combined with a growing odd-prime cutoff. Fix \(0<c<a\) and set \(y=(cT\log T)^2\), \(P_y=\prod_{3\le p\le y}p\). For squarefree odd \(m\), write \(m=sd\) with \(d\mid P_y\) and all prime factors of \(s\) exceeding \(y\). Then on the same window \([T-b,T]\) a positive contribution \(\gg e^{2aT}T^{2m_0-2}\) is still forced after requiring all of the following:

1. both rough parts exceed \(e^{\tau T}\), for any fixed \(0<\tau<2(a-c)\);
2. the two rough parts are different, so some prime exceeding \(y\) divides exactly one of \(m,n\);
3. the reduced-ratio cutoff from (2) is exceeded.

Here and below the window, zero and parameters are fixed before the large-\(T\) limit. Put \(M_y=\prod_{3\le p\le y}(1+p^{-1/2})\); the prime number theorem and partial summation give \(\log M_y=(2+o(1))\sqrt y/\log y=(c+o(1))T\). The entire scalar portion of \(D^{\rm loc}\) with \(s\le e^{\tau T}\) costs \(O(\sqrt T M_y e^{\tau T/2})=o(e^{aT})\), by \(|K_u|\ll\sqrt T\) and summing \(s^{-1/2}\). Removing it before squaring preserves the required \(L^2\) lower bound by the triangle inequality. On squaring the surviving sum, the absolute cost of *all* pairs with identical rough part is at most
\[
 C T M_y^2\sum_{s\le e^{(1+d)T}}\frac1s
 \ll T^2 M_y^2=\exp((2c+o(1))T)
\]
pointwise. It is negligible even if no small-prime cancellation is used. The small-ratio pairs still cost (2) in absolute value after either removal. This proves the simultaneous restriction. It supplies a growing range of prime relations that on their own cannot generate the energy forced by a hypothetical zero.

## 3. A squarefree signed sequence with exactly the same dyadic rule defeats scale inversion

Fix any \(0<a<1/2\). There exists a sequence \(b(n)\in\{-1,0,1\}\) with all of the following properties.

- \(b(n)=\mu(n)\) for every \(n\le3000\), and \(|b(n)|=\mu(n)^2\) for all \(n\).
- \(b(2m)=-b(m)\) for odd \(m\), and \(b(4m)=0\) for every \(m\).
- Substitute \(b\) for \(\mu\) in exactly the four-band formula for \(w\). Its Gaussian average is strictly positive for every center and every \(\epsilon\ge10^{-6}\).
- Its unsmoothed negative mass is \(\gg e^{aT}\) on every sufficiently large log window \([T-b_0,T]\) of a suitable fixed length \(b_0>0\).

This sequence does not model odd-prime multiplicativity. It explains precisely why complete squarefree occupancy, the dyadic signs, a verified arithmetic prefix, and global smoothing positivity alone cannot provide a subpower unsmoothed bound.

**Baseline.** Let \(N_0=3000\). On odd inputs keep \(\mu(m)\) through \(N_0\) and use zero above \(N_0\); extend by the dyadic rule. Form its native row \(w_0\) with the same additive \(6{\bf1}_{n=1}\). The [interval checker](check_detector_diffusion_nov18.py) proves
\[
 w_0(v)\ge 6(v-\log2)_+\quad(v\in\mathbb R).
\]
It tests the knot values through \(8N_0\), the maximum possible support of \(q\), and the final slope \(>6\). Below \(\log2\) the row is identically zero.

**Prescribed odd prefix.** Use \(\epsilon_0=10^{-6}\). Choose \(\gamma>0\) so large that \(a+\epsilon_0(a^2-\gamma^2)<0\), and put \(s_0=a+i\gamma\). Choose \(N\) sufficiently large, \(L=\log N\), and define
\[
 D_L(v)={\bf1}_{v\ge L}\big(\Re e^{s_0(v-L)}-1-a(v-L)\big).
\]
Its value and first derivative vanish at \(L\). Let \(B(x)=0\) for \(x<N\), and \(B'(x)=x^{-1/2}D_L''(\log x)\) above \(N\), with \(B(N)=0\). For \(x\ge N\),
\(|B'(x)|\le |s_0|^2N^{-a}x^{a-1/2}\). Its continuously weighted ramp is exactly \(D_L\), by changing variables:
\[
 \int_N^{e^v} x^{-1/2}(v-\log x)\,dB(x)=D_L(v)
\]
when \(v\ge L\), with both sides zero before \(L\).

Let \(j(x)\) count odd squarefree \(m\in(N_0,x]\). The density above gives \(N_0+j(x)/\kappa=x+O(\sqrt x)\) for \(x\ge N_0\). Choose a small \(\delta>0\) and assign to the first \(j\) eligible positions cumulative sum
\[
 S_j=2\left\lfloor\frac{j+\delta B(N_0+j/\kappa)}2\right\rfloor-j .
\]
Here \(S_0=0\). By choosing \(N\) large, consecutive arguments \(\delta B(N_0+j/\kappa)\) differ by less than one. Hence \(S_j-S_{j-1}\) equals either \(+1\) or \(-1\). Use that sign at each eligible position and zero at the ineligible odd positions. The constructed prefix above \(N_0\) satisfies
\[
 |S_{j(x)}-\delta B(x)|\le 2+C_{a,\gamma}\delta\,{\bf1}_{x\ge N/2}(x/N)^a .
\]
Indeed for \(x<N/2\) both continuous arguments are below \(N\) if \(N\) is sufficiently large. For \(x\ge N/2\) use their difference \(O(\sqrt x)\) and the derivative estimate on comparable arguments.

**Control of rounding.** Partial integration against the nonnegative decreasing ramp \(x^{-1/2}(v-\log x)\) shows that the weighted ramp sum of these odd tail coefficients is \(\delta D_L(v)+E(v)\), where
\[
 |E(v)|\le (2N_0^{-1/2}+C'_{a,\gamma}\delta N^{-1/2})(v-\log2)_+ .
\]
The constant discrepancy 2 costs at most \(2N_0^{-1/2}(v-\log N_0)_+\). For the other term integrate the absolute derivative \(x^{-3/2}[1+(v-\log x)/2]\) over \(N/2\le x\le e^v\) against \((x/N)^a\). The integral is \(O_a(N^{-1/2}(1+v))\) because \(a<1/2\), and it vanishes for \(v<\log(N/2)\).

The full filtered response of any odd ramp is the shift operator \((\mathcal L f)(v)=\sum_{j=0}^3 c_j f(v-jh)\). Since \(\sum|c_j|<25\), \(50/\sqrt{N_0}<1\). Taking \(N\) large makes \(|\mathcal L E(v)|\le2(v-\log2)_+\). The synthetic row is exactly \(w_0+\delta\mathcal L D_L+\mathcal L E\).

**Positivity after averaging.** For a normal variable \(V\) of mean \(U\), variance \(2\epsilon_0U\), the Gaussian means of all four shifted \(D_L\) have absolute value \(O_{a,\gamma}(1+U)\) uniformly in \(L\). The mean of the uncut exponential has modulus \(\exp[-a(L+jh)+(a+\epsilon_0(a^2-\gamma^2))U]\le1\). Its omitted portion \(V<L+jh\) has magnitude at most one. The remaining affine terms cost \(O(1+U)\). Take \(\delta\) sufficiently small so these four terms cannot exhaust \(4\mathbb E[(V-\log2)_+]\ge4(U-\log2)\) for \(U\ge4\). Choose \(N\) large enough for all preceding estimates with that \(\delta\). For \(U\le4\) the row matches the native one on \(v\le8\), and \(|q|\le24\) globally. The small-center Gaussian domination in Section 3 of the diffusion note applies verbatim. Positive subordination gives positivity for every \(\epsilon\ge\epsilon_0\).

**Unsmoothed oscillation.** For \(v>L+3h\) the exponential component of \(\mathcal L D_L(v)\) has complex coefficient
\[
 \sum_{j=0}^3 c_j e^{-s_0jh}
     =P(1/2+s_0)(1-2^{-(1/2+s_0)})\ne0.
\]
All other terms, including the rounding error, are \(O(1+v)\). Thus the synthetic source has a nonzero sinusoidal component growing as \(e^{av}\) with a linear-size remainder. Each sufficiently long log interval contains a fixed-width subinterval on which this sinusoid is negative by a fixed fraction of its amplitude. Integrating gives the claimed negative-mass lower bound.

The native odd-prime signs are the missing arithmetic information in this counterexample. Sections 1–2 describe what the actual grouped correlations must accomplish; the synthetic obstruction does not assign those correlations to the Möbius function.
