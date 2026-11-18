# A weighted Mellin-strip condition for the raw-height explicit formula

A weighted strip norm supplies a sufficient replacement for the missing tail regularity in the pinned Bombieri–Lagarias formula. It controls the absolute zero sum without RH and requires no separate Sobolev assumption on the central vertical trace. The result is for continuous tests. The compact tests with jumps used in Theorem 2 keep their separate midpoint argument. [Pinned formula and counterexample scope](analytic131_explicit_formula_countermodel_adjudication.md)

## Statement

Let \(f:(0,\infty)\to\mathbb C\) be continuous with
\[
 f(x)=O(x^\delta)\quad(x\downarrow0),\qquad
 f(x)=O(x^{-1-\delta})\quad(x\to\infty)
\]
for some \(\delta>0\), and write \(h(z)=\widehat f(z)=\int_0^\infty f(x)x^{z-1}dx\). It is holomorphic on \(-\delta<\Re z<1+\delta\) by these bounds. For fixed \(0<\epsilon<\delta\) and \(s>1/2\), assume
\[
 \mathcal N_s(f)^2
 =\int_{-\epsilon}^{1+\epsilon}\int_{\mathbb R}
       (1+t^2)^s|h(\beta+it)|^2\,dt\,d\beta<\infty .
\]
Then, with the nontrivial zeros counted with multiplicity,
\[
 \sum_\rho|h(\rho)|\le C_{s,\epsilon}\mathcal N_s(f),\qquad
 \sum_{|\Im\rho|\ge T}|h(\rho)|
   \le C_{s,\epsilon}\mathcal N_s(f)\,
        T^{1/2-s}\log(2+T)\quad(T\ge2).
\]
The pinned formula holds with its ordinary symmetric height limit, which now equals the absolute sum. With \(\widetilde f(x)=x^{-1}f(1/x)\), it is
\[
\begin{aligned}
 \sum_\rho h(\rho)
 &=\int_0^\infty f(x)dx+\int_0^\infty\widetilde f(x)dx
 -\sum_{n\ge1}\Lambda(n)(f(n)+\widetilde f(n))\\
 &\quad-(\log\pi+\gamma)f(1)
 -\int_1^\infty
   \left(f(x)+\widetilde f(x)-\frac{2}{x^2}f(1)\right)
   \frac{x\,dx}{x^2-1}.
\end{aligned}
\]
The arithmetic terms have their ordinary absolute meaning. No assertion is made about the borderline \(s=1/2\) or the optimal test class.

## Strip sampling and the central trace

Let \(r=\min(\epsilon/4,1/4)\). For \(\beta\in[0,1]\) and \(t\in[n,n+1]\), the disk of radius \(r\) about \(\beta+it\) lies in the strip and in the expanded height rectangle used below. The mean inequality for \(|h|^2\) gives
\[
 \sup_{\substack{0\le\beta\le1\\n\le t\le n+1}}|h(\beta+it)|
 \le C_{s,\epsilon}\langle n\rangle^{-s} E_n^{1/2},
 \qquad
 E_n=\int_{-\epsilon}^{1+\epsilon}\int_{n-r}^{n+1+r}
          \langle v\rangle^{2s}|h(\sigma+iv)|^2dv\,d\sigma .
\]
Here \(\langle v\rangle=(1+v^2)^{1/2}\), and weights are comparable throughout the expanded rectangle. The rectangles overlap a bounded number of times, so \(\sum_n E_n\ll\mathcal N_s(f)^2\). The unconditional unit-height count with multiplicity is \(O(\log(2+|n|))\). Cauchy–Schwarz now gives the claimed zero-sampling bound, since \(\sum_n\langle n\rangle^{-2s}\log^2(2+|n|)<\infty\). Keeping only integer cells intersecting \(|t|\ge T\) gives the quantitative tail by the corresponding power-log tail integral. No restriction on where the zeros lie inside the critical strip is needed.

The same displayed supremum bound, integrated over one unit cell at a time, proves a vertical-trace estimate for **every** \(\beta\in[0,1]\),
\[
 \sup_{0\le\beta\le1}\int_{\mathbb R}
     \langle t\rangle^{2s}|h(\beta+it)|^2dt
 \le C_{s,\epsilon}\mathcal N_s(f)^2.
\]
Thus the central line cannot be an exceptional real parameter for Sobolev regularity. Put \(G_\beta(u)=e^{\beta u}f(e^u)\), and \(F=G_{1/2}\). Each \(G_\beta\) for \(-\epsilon\le\beta\le1+\epsilon\) is both integrable and square integrable by the endpoint bounds. The chosen Mellin transform is its Fourier transform with positive phase. Plancherel identifies \(\mathcal N_s(f)^2\) up to the Fourier normalization with \(\int\|G_\beta\|_{H^s}^2d\beta\). The fixed-line estimate gives \(F\in H^s\). For any \(0<\alpha<\min(1,s-1/2)\), Fourier inversion and Cauchy–Schwarz with \(|e^{itx}-1|\ll_\alpha |tx|^\alpha\) give a continuous \(\alpha\)-Hölder representative of \(F\). It equals the original continuous \(F\) pointwise.

The prime sum converges absolutely by the value bounds and \(\Lambda(n)\le\log n\), also for \(\widetilde f\), which obeys the same paired endpoint bounds. The smooth integrals are absolute as well. Near \(x=1\), put \(u=\log x\); then
\[
 f(e^u)+\widetilde f(e^u)=e^{-u/2}(F(u)+F(-u)).
\]
Subtracting \(2e^{-2u}F(0)\) gives \(O(u^\alpha)\) for \(u\downarrow0\). The integration measure \(e^{2u}du/(e^{2u}-1)\) is \(O(du/u)\) there. At infinity the paired value envelope gives integrability. Thus all the claimed terms are defined before the equality is proved.

## Approximation proof of the identity

For the starting identity use the usual Weil explicit formula on smooth compact log-coordinate profiles. In that subclass the Mellin transform is entire with rapid decay on every fixed vertical strip, so its zero side is absolute. In the pinned p. 6 convention, the variable change \(x=e^u\), the inversion pairing and the ordinary finite-part evaluation on pp. 6–7 give the displayed arithmetic expression. The subsequent approximation uses only this smooth compact formula, not the invalid extension to all printed (A)–(B) tests. [Pinned author manuscript, pp. 6–7](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf)

**First cut off the log coordinate.** Take even \(\chi\in C_c^\infty(\mathbb R)\) with \(0\le\chi\le1\) and \(\chi=1\) on \([-1,1]\). Set \(\chi_R(u)=\chi(u/R)\), \(R\ge1\), and \(f_R(x)=\chi_R(\log x)f(x)\). On each \(\beta\)-line this replaces \(G_\beta\) by \(\chi_R G_\beta\). Multiplication is uniformly bounded on \(H^s\), since the Fourier transform of \(\chi_R\) has uniformly bounded weighted \(L^1(\langle t\rangle^sdt)\) norm for \(R\ge1\), and weighted Young's inequality applies. The products converge strongly to \(G_\beta\) in \(H^s\) whenever \(G_\beta\in H^s\), by density of compact smooth functions and the fact that any fixed compact support eventually lies where \(\chi_R=1\). Integrated dominated convergence gives \(\mathcal N_s(f_R-f)\to0\). The already proved sampling bound gives convergence of the absolute zero sums in this norm. On the arithmetic side \(\widetilde f_R(x)=\chi_R(\log x)\widetilde f(x)\) by evenness. The bounds at zero and infinity dominate the ordinary integrals and the prime sum. The archimedean integrand agrees with the original one near 1 for all \(R\ge1\), including the value at 1.

**Then smooth at fixed \(R\).** Let \(\varphi_\tau(u)=\tau^{-1}\varphi(u/\tau)\) with \(\varphi\) a real even compact smooth mollifier of mass one. Set
\[
 F_{R,\tau}=\varphi_\tau*(\chi_R F),\qquad
 f_{R,\tau}(x)=x^{-1/2}F_{R,\tau}(\log x).
\]
These are genuine smooth compact log-coordinate tests. For \(a=\beta-1/2\), their \(\beta\)-profile is \((e^{a\cdot}\varphi_\tau)*(\chi_R G_\beta)\). Its Fourier multiplier is bounded uniformly for \(\beta\in[-\epsilon,1+\epsilon]\) and \(0<\tau\le1\), and tends to 1 at each fixed \(\beta,t\). Thus \(\mathcal N_s(f_{R,\tau}-f_R)\to0\) by integrated dominated convergence. Uniform compact support and uniform convergence in the log coordinate give convergence of both ordinary integrals and of the finite prime sum at fixed \(R\). Mollification gives a uniform Hölder bound on \(F_{R,\tau}\) near zero, either by its convolution action on the continuous Hölder function \(\chi_R F\) or by the central trace bound. The archimedean numerator is therefore dominated by \(O(u^\alpha)\) uniformly in \(\tau\) near zero, and outside this neighborhood it has a common compact-support envelope plus the fixed decaying subtraction. All terms converge in the smooth identity as \(\tau\downarrow0\). Finally send \(R\to\infty\) using the cutoff estimates above.

## Scope of the repair

The counterexample in the literal (A)–(B) class is excluded because this strip condition implies absolute zero sampling. The proof uses holomorphy on a strip of positive excess width and the absolute integration of its weighted square over that strip. It requires neither a nonexceptional trace chosen by hand nor an extra differentiability hypothesis on \(f\) beyond continuity and the two value bounds.

Fixed compact tests that are continuous and piecewise smooth can meet this condition, but the actual \(g_{n,\epsilon_0}\) in Theorem 2 has a nonzero jump at 1. Its central vertical trace therefore cannot belong to \(H^s\) with \(s>1/2\). The endpoint terms of order \(1/\rho\), the classical symmetric zero sum, and the midpoint mollification argument remain the appropriate justification for that application. The present quantitative criterion is sufficient and no priority claim or canonical change is made. [Compact jump calculation](analytic131_explicit_formula_countermodel_adjudication.md)
