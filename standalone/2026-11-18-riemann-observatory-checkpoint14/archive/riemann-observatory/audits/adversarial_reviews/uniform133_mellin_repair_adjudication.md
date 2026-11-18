# Third independent adjudication of the Sobolev–Mellin repair

18 November 2026. The sufficient strip condition and explicit zero-trace constant pass. The same mean-value method gives the central Sobolev trace used at the archimedean singularity. I checked the approximation in the full strip norm, the tail index, and the distinction from the compact tests with jumps. [Proposed repair](analytic132_mellin_trace_repair.md) · [Independent Sobolev check](weighted132_mellin_trace_repair_review.md)

## Exact trace constants

Keep the continuous test and its two endpoint value bounds from Analytic132, with \(0<\epsilon<\delta_0\) so that the Mellin integral represents \(h\) throughout the weighted norm strip. Write \(r=\min(\epsilon/2,1/4)\) and \(w_n=(1+n^2)^s\), with \(s>1/2\). In this derivation \(E_n\) denotes the **unweighted** area integral of \(|h|^2\) over \([-r,1+r]\) times the height interval \([n-r,n+1+r]\). Disks of radius \(r\) centered in \([0,1]\times[n,n+1]\) lie in that rectangle and inside the open holomorphy strip. The area submean inequality for \(|h|^2\) gives
\[
 \sup_{[0,1]\times[n,n+1]} |h|\le(\sqrt\pi r)^{-1} E_n^{1/2}.
\]
Within the rectangle \(|t-n|\le5/4\). Hence \(1+n^2\le1+2t^2+2(5/4)^2\le5(1+t^2)\), so \(w_n\le5^s(1+t^2)^s\). At each height at most two of the expanded intervals occur since their length is at most \(3/2<2\). Therefore \(\sum_n w_nE_n\le2\cdot5^s\mathcal N_s(f)^2\).

Choose \(C_N\) so that the number of zeros with multiplicity in \(n\le\Im\rho<n+1\) is at most \(C_N\log(2+|n|)\). Such a fixed constant follows from the unconditional local zero count. The cell sup bound and Cauchy–Schwarz prove exactly
\[
 \sum_\rho |h(\rho)|
 \le \frac{C_N}{\sqrt\pi r}
  \left(2\cdot5^s
   \sum_{n\in\mathbb Z}\frac{\log^2(2+|n|)}{(1+n^2)^s}
  \right)^{1/2}\mathcal N_s(f).
\]
The half-open convention counts a zero at a cell boundary only once. A cell containing \(t\ge T\) has \(n>t-1\), so \(n>T-1\). A cell containing \(t\le-T\) has \(n\le t\), so \(|n|\ge T\). Thus restricting the explicit series to \(|n|>T-1\) gives the tail for \(|\Im\rho|\ge T\), including real \(T\) and equality at an integer boundary. Dyadic grouping for \(|n|\ge\lfloor T\rfloor\) proves that the restricted series is \(O_s(T^{1-2s}\log^2(2+T))\). At \(s=1/2\) the full series diverges. This argument makes no decision on the endpoint by other methods.

## Central trace and the archimedean singularity

One can also integrate the disk submean inequality along a fixed interior vertical line. On the central line, if \(|t-v|\le r\) then \(1+t^2\le3(1+v^2)\), and a point of ordinate \(v\) lies within the possible disk centers for a total height length at most \(2r\). Fubini gives the explicit bound
\[
 \int_{\mathbb R}(1+t^2)^s|h(1/2+it)|^2\,dt
 \le \frac{2\cdot3^s}{\pi r}\mathcal N_s(f)^2.
\]
The same argument with radius \(r/2\) works on the fixed exterior lines \(-\epsilon/2\) and \(1+\epsilon/2\). The positive-phase Fourier transform of \(F(u)=e^{u/2}f(e^u)\) is \(h(1/2+it)\). For \(0<\alpha<\min(1,s-1/2)\), use \(|e^{itv}-1|\le2^{1-\alpha}|tv|^\alpha\) and Cauchy–Schwarz in Fourier inversion. The integral \(\int |t|^{2\alpha}(1+t^2)^{-s}\,dt\) is finite. This bounds the Hölder seminorm and pointwise norm of \(F\) by the strip norm. It gives a representative equal to the original continuous profile, so no independent central trace hypothesis is used.

With \(u=\log x>0\), the paired numerator equals
\[
 e^{-u/2}(F(u)+F(-u))-2e^{-2u}F(0).
\]
Writing each \(F(\pm u)\) as its value at zero plus an \(O(u^\alpha)\) error bounds the result by \(O(u^\alpha)\) as \(u\downarrow0\); the remaining smooth-factor difference is \(O(u)\). Since the measure is \(e^{2u}du/(e^{2u}-1)\), the resulting singularity is integrable for \(\alpha>0\). The exterior trace bounds also give \(|f(x)|\ll\mathcal N_s(f)x^{\epsilon/2}\) below 1 and \(|f(x)|\ll\mathcal N_s(f)x^{-1-\epsilon/2}\) above 1. Thus the ordinary integrals, the compensated integral away from 1, and the prime sum converge absolutely. Applying the same bounds to differences makes each term a continuous functional in the strip norm, and gives a second way of justifying the limits in the proof.

## Density and scope

In logarithmic coordinates the slice profiles are \(G_\beta(u)=e^{(\beta-1/2)u}F(u)\). The required initial real decay ensures integrable and square-integrable slices on the norm strip. Plancherel expresses the norm as the integral of the slice \(H^s\) squares up to the Fourier normalization. Multiplication by \(\chi(u/R)\) is uniformly bounded on \(H^s\): its Fourier multiplier kernel has weighted \(L^1\) norm bounded by changing variables from \(t\) to \(Rt\) and using \(R\ge1\). Strong convergence on each admissible slice follows first for compact smooth functions and then by density. Integrating the square bounds proves strip-norm convergence as \(R\to\infty\).

At fixed \(R\), mollify the compact central profile. On a general slice the convolution uses the kernel \(e^{(\beta-1/2)u}\varphi_\tau(u)\) exactly. Its \(L^1\) norm is bounded uniformly on the whole norm strip because the mollifier support is \(O(\tau)\), and its Fourier transform tends pointwise to 1. Plancherel and dominated convergence give convergence in the full weighted strip norm. Each smooth test is compactly supported in the logarithmic coordinate and hence qualifies for the compact smooth Guinand–Weil formula. The zero-trace bound and the continuous arithmetic functionals just proved permit the two successive limits. This uses the classical compact smooth class and avoids assuming the broad printed (A)–(B) formula.

The compact approximants \(g_{n,\epsilon_0}\) in Bombieri–Lagarias Theorem 2 have a genuine jump at 1 for \(n\ge1\), and therefore cannot have a central \(H^s\) profile with \(s>1/2\). A value assigned at the jump does not alter this obstruction. Their symmetric zero sum and midpoint proof remain separate. The present result is sufficient, unconditional, and makes no optimality or field-priority claim. No canonical record was changed. [Pinned author manuscript, pp. 5–8](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)
