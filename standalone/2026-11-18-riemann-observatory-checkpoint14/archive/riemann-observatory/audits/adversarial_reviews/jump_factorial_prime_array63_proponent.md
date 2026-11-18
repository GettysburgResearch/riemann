# The prescribed prime array for a factorial target

Date 2026-11-17. The proposed logarithmic taper gives the exact squared error asymptotic under RH. Its constant agrees with the best anchored length-\(N\) approximation. The proof needs neither a simplicity assumption nor an estimate for \(1/\zeta'(\rho)\). The upper argument is a residue calculation for a logarithmic derivative, and the lower argument uses Burnol's primary cutoff vectors. No priority claim is made. [Jump generator](jump_generator63_proponent.md) · [Burnol's primary cutoff construction](https://arxiv.org/pdf/math/0103058v2)

## Normalization and the exact coefficients

Fix an integer \(k\ge2\), write \(a(s)=k^{1-s}-1\), \(F(s)=\zeta(s)a(s)\), and let
\[
 R_k(n)=k\log(\lfloor n/k\rfloor!)+k\lfloor n/k\rfloor\log k-\log(n!)
\]
be the value on \([n,n+1)\). Use \(0!=1\). The bounded step vector \(f_k(n)=k\lfloor n/k\rfloor-n\) has jump \(k\mathbf1_{k\mid n}-1\). Hence \(iR_k=Gf_k\), where \(G\) is the strong jump generator. In particular \(R_k(n)=O_k(\log(2+n))\) by the generator formula, and \(R_k\) belongs to the weighted unit-step space \(S\). In Mellin coordinates the target is
\[
 T(s)=M R_k(s)=-\frac{F'(s)}{s}
\]
on \(\Re s>1/2\), and its squared boundary norm is in \(dt/(2\pi)\). Write \(Q=-F'/\zeta\). On \(\Re s>1\),
\[
 Q(s)=a(s)\sum_{d\ge1}\Lambda(d)d^{-s}+k^{1-s}\log k
     =\sum_{d\ge1}w_k(d)d^{-s},
\]
where
\[
 w_k(d)=k\mathbf1_{k\mid d}\Lambda(d/k)-\Lambda(d)+k\log k\,\mathbf1_{\{d=k\}}.
\]
As a check, using \(\sum_{e\mid n}\Lambda(e)=\log n\) gives
\(\sum_{d\mid n} w_k(d)=(k\mathbf1_{k\mid n}-1)\log n\), the exact jump of \(R_k\). The term at \(d=k\) includes the derivative of \(a\). The pole of \(\zeta\) at 1 is canceled in \(F\), so \(Q\) is holomorphic at 1 and \(Q(1)=0\).

For \(N>1\) put \(L=\log N\) and define
\[
 A_N(s)=\sum_{d\le N}w_k(d)\left(1-\frac{\log d}{L}\right)d^{-s},
 \qquad B_N(s)=A_N(s)-A_N(1).
\]
The coefficient at an integer endpoint \(d=N\) is zero. The polynomial \(B_N\) satisfies the anchor \(B_N(1)=0\) at the same length. Let \(V_N\) consist of \(\zeta(s)B(s)/s\) for all such anchored length-\(N\) polynomials \(B\). Equivalently it is the Mellin image of the span of \(f_d\), \(2\le d\le N\), since every anchored polynomial is a linear combination of \(d^{-s}-d^{-1}\). All norms and distances for \(T,V_N\) below use the full line measure \(dt/(2\pi)\).

## Exact Perron formula and the analytic remainder

Assume RH. For a distinct nontrivial zero \(\rho=1/2+i\gamma\) of multiplicity \(m_\rho\), the residue of \(Q\) is
\[
 r_\rho=-m_\rho a(\rho).
\]
These poles are simple even at a multiple zero of \(\zeta\). Such a zero is included just once in residue sums. For \(s=1/2+it\) outside those zeros, and also for \(s=1\), start the smoothed Perron integral on \(\Re w=2\). Absolute convergence of the Dirichlet series and the kernel \(w^{-2}\) gives
\[
 A_N(s)=\frac{1}{2\pi iL}\int_{(2)}Q(s+w)N^w\,\frac{dw}{w^2}.
\]
Shift to \(\Re(s+w)=-1\). Besides \(w=0\), the crossed poles are exactly \(w=\rho-s\). The apparent singularity at \(s+w=1\) is removable, and trivial zeta zeros start at \(-2\). On the line \(\Re z=-1\), the functional equation and the absolutely convergent log derivative at \(1-z\) give \(Q(z)\ll_k\log(2+|\Im z|)\). To justify the horizontal limits, select heights \(H\) of the argument \(z=s+w\) tending to positive and negative infinity whose distance from all zero ordinates is \(\gg1/\log(2+|H|)\), using the unconditional \(O(\log(2+|H|))\) multiplicity count in each unit interval. On these segments the Hadamard log-derivative formula gives \(Q\ll_k\log^2(2+|H|)\) uniformly in the finite strip. The \(w^{-2}\) factor sends their integrals to zero for fixed \(s,N\). The residue sum converges absolutely at each permitted \(s\) by the same unit-interval zero count. Thus
\[
 A_N(s)=Q(s)+\frac{Q'(s)}L+
         \frac1L\sum_\rho\frac{r_\rho N^{\rho-s}}{(s-\rho)^2}
          +I_N(s).
 \tag{1}
\]
On the critical line,
\[
 |I_N(1/2+it)|\ll_k
  \frac{N^{-3/2}}L\,\log(2+|t|).
 \tag{2}
\]
This follows by integrating \(\log(2+|t+v|)/(1+v^2)\) along the new line. At \(s=1\) the same bound is \(O_k(N^{-2}/L)\) and the residue sum in (1) is \(O_k(N^{-1/2}/L)\). In particular
\[
 A_N(1)=\frac{Q'(1)}L+O_k(N^{-1/2}/L),\qquad
 Q'(1)=-F'(1)=\gamma_{\!E}\log k-\tfrac12(\log k)^2 .
 \tag{3}
\]

We also need the cancellation of the local double poles of \(Q'\). The logarithmic derivative of the completed zeta gives, with multiplicities,
\[
 K(s)=\frac{\zeta'}{\zeta}(s)
 =\sum_\rho m_\rho\left(\frac1{s-\rho}+\frac1\rho\right)+D(s),
\]
where \(D(s)=C-1/s-1/(s-1)+(\log\pi)/2-\frac12\psi(s/2)\). The paired series and its derivative are locally normal away from the zeros. Since \(Q'=-a'K-aK'-a''\), it follows that
\[
 Q'(s)=-\sum_\rho\frac{r_\rho}{(s-\rho)^2}+U(s),\qquad
 U(1/2+it)\ll_k\log^2(2+|t|).
 \tag{4}
\]
Here the remaining contribution per zero, before multiplication by its multiplicity, is
\[
 \frac{a(s)-a(\rho)-a'(s)(s-\rho)}{(s-\rho)^2}
 -\frac{a'(s)}{\rho}.
\]
For \(|t-\gamma|\le1\) the divided difference is bounded by Taylor's formula along the critical line. The \(O(\log(2+|t|))\) total near multiplicity then bounds the near sum. For \(|t-\gamma|>1\), split the same expression as a bounded numerator times \((s-\rho)^{-2}\) and the paired term \(-a'(s)(1/(s-\rho)+1/\rho)\). The first sum is \(O_k(\log(2+|t|))\) by unit windows. The second uses \(|1/(s-\rho)+1/\rho|=|s|/(|\rho|\,|s-\rho|)\). With \(T_0=2+|t|\), ordinates much smaller than \(T_0\) give \(O(\log^2 T_0)\) by the sum of \((1+|\gamma|)^{-1}\) against the zero count. Comparable ordinates give a harmonic sum of total size \(O(\log^2 T_0)\), and ordinates larger than \(2T_0\) give \(O(\log T_0)\) by summing \(T_0/(1+|\gamma|)^2\). The gamma and polar contributions \(-a'D-aD'-a''\) on the line satisfy the same bound.

RH implies \(\zeta(1/2+it),\zeta'(1/2+it)\ll_\epsilon(2+|t|)^\epsilon\) for every \(\epsilon>0\). For the derivative, the usual Lindelöf bound on the right, the functional equation just to the left, and Cauchy's formula in a small fixed disk give the bound after choosing its radius in terms of \(\epsilon\). In particular, (2)–(4) and \(\zeta/s\in L^2\) show that
\[
 \sqrt L\left(T(s)-\frac{\zeta(s)B_N(s)}s\right)
 =
 \frac{\zeta(s)}{s\sqrt L}
 \sum_\rho r_\rho\frac{1-N^{\rho-s}}{(s-\rho)^2} + o_{L^2}(1).
 \tag{5}
\]
In (5) the three discarded terms are \(-\zeta U/(s\sqrt L)\), \(-\sqrt L\,\zeta I_N/s\), and \(\sqrt L\,\zeta A_N(1)/s\). Their norms tend to zero by the stated bounds. The contour identities and (5) only need to hold away from the countable set of ordinates of zeros to determine the \(L^2\) claim.

## Uniform tails and the local asymptotic

On the line put
\[
 h_L(u)=\frac{1-e^{-iLu}}{i\sqrt L\,u},
\]
with its removable value at zero. Plancherel for the Fourier transform of \(L^{-1/2}\mathbf1_{[0,L]}\) gives \(\int_{\mathbb R}|h_L(u)|^2\,du/(2\pi)=1\). For every fixed \(\delta>0\) its squared mass at \(|u|>\delta\) tends to zero as \(L\to\infty\). The summand in (5) can be written
\[
 r_\rho \,\frac{\zeta(s)}{s(s-\rho)}\,h_L(t-\gamma).
 \tag{6}
\]

First discard all terms with \(|t-\gamma|>1\) in (5). In that range \(|1-N^{\rho-s}|\le2\), and \(|r_\rho|\ll_k m_\rho\). The sum of \(m_\rho/|t-\gamma|^2\) over the discarded terms is \(O(\log(2+|t|))\), which gives an \(O_k(L^{-1/2})\) error in full \(L^2\) by the bound for \(\zeta/s\).

Choose \(0<\epsilon<1/2\). For the remaining terms, \(|t-\gamma|\le1\) implies
\[
 \left|\frac{\zeta(s)}{s-\rho}\right|\ll_\epsilon(2+|t|)^\epsilon
\]
by integrating \(\zeta'\) along the segment of the line. For the near terms with \(|\gamma|>Y\), Cauchy–Schwarz with the weights \(m_\rho\) and the local zero count give the pointwise square bound
\[
 C_{k,\epsilon}(2+|t|)^{-2+2\epsilon}\log(2+|t|)
 \sum_{\substack{|\gamma|>Y\\|t-\gamma|\le1}}
      m_\rho |h_L(t-\gamma)|^2 .
\]
Over this near interval the external factors are bounded by the same expression with \(t\) replaced by \(\gamma\) up to a constant. Integrate each \(h_L\) using its total mass 1, then sum by unit ordinate windows. The squared norm of the near tail is bounded by
\[
 C_{k,\epsilon}\sum_{j\ge Y-2}(2+j)^{-2+2\epsilon}\log^2(2+j)
 \ \longrightarrow\ 0
\]
uniformly in \(N\), as \(Y\to\infty\). This estimate holds when distinct zeros approach one another and uses their total multiplicities.

For the finitely many \(|\gamma|\le Y\), restrict (6) to disjoint fixed small neighborhoods of their ordinates. The additional discarded portion has norm \(O_{Y,k}(L^{-1/2})\) by the bound for \(h_L\) outside a fixed neighborhood. On each neighborhood \(\zeta(s)/(s(s-\rho))\) is continuous with value \(\zeta'(\rho)/\rho\) at its center. Concentration of \(|h_L|^2\) at zero therefore gives the contribution \(|r_\rho\zeta'(\rho)/\rho|^2\). In the multiple-zero case \(\zeta'(\rho)=0\). Taking \(N\to\infty\) first and then \(Y\to\infty\) proves
\[
 \lim_{N\to\infty} L
 \left\|T-\frac{\zeta B_N}{s}\right\|_2^2
 =
 C_k,\qquad
 C_k=\sum_{\substack{\zeta(\rho)=0,\ \Re\rho=1/2\\m_\rho=1}}
       \frac{|\zeta'(\rho)(k^{1-\rho}-1)|^2}{|\rho|^2}.
 \tag{7}
\]
The series is finite by the same derivative bound and the unit-window zero count. Ordinates of both signs are included.

## Matching best-distance lower bound

It suffices to test only simple critical zeros. Let \(\mathcal I(s)=(s-1)/s\), an inner multiplier on the half-plane, and let \(Z(s)=(s-1)\zeta(s)/s^2\). In the Mellin convention \(\widehat f(s)=\int_0^\infty f(x)x^{s-1}dx\), physical inversion \(x\mapsto1/x\) identifies the time-domain target with a function supported in \((0,1]\). The range \(\mathcal I V_N\) is contained in Burnol's cutoff dilation space \(C_{1/N}\), because \(\mathcal I(\zeta B/s)=Z B\) and \(B\) is supported on indices \(n\le N\), with multiplier \(n^{-s}\) the dilation at \(1/n\). Burnol Corollary 4.4 makes the vectors \(Y_{\rho,0}^{1/N}\) at zeros orthogonal to the cutoff space. For any fixed finite set of distinct simple zeros, Theorem 5.3 gives the identity as limiting Gram matrix of \(X_{\rho,0}^{1/N}=L^{-1/2}Y_{\rho,0}^{1/N}\). [Burnol, Definition 4.2, Corollary 4.4 and Theorem 5.3](https://arxiv.org/pdf/math/0103058v2)

Here the needed target pairing is valid for \(T=-F'/s\). Burnol's unitary multiplier is
\[
 V(s)=\left(\frac{s}{1-s}\right)^3\frac{\zeta(1-s)}{\zeta(s)},\qquad
 V(s)\mathcal I(s)T(s)
   =\frac{sF'(s)}{(1-s)^2}\frac{\zeta(1-s)}{\zeta(s)}.
\]
The zeta ratio has the analytic gamma expression
\(\pi^{1/2-s}\Gamma(s/2)/\Gamma((1-s)/2)\) in a strip around the critical line. It contributes \(O((2+|t|)^{\sigma-1/2})\) for \(\sigma=\Re s\) in a fixed small left strip. On that strip RH and the functional equation give \(\zeta,\zeta'\ll_\epsilon(2+|t|)^{1/2-\sigma+\epsilon}\) uniformly. For \(\zeta'\), differentiate the functional equation and use the right-half strip bounds for \(\zeta,\zeta'\), absorbing the logarithm of the gamma derivative. The product \(V\mathcal I T\) is therefore analytic on the fixed left strip and uniformly \(O((2+|t|)^{-1+\epsilon})\). If \(g=(V\mathcal I T)^\vee\), shifting the Mellin line left by a fixed small \(b>0\) gives \(x^{-b}g\in L^2(dx)\) by Plancherel. This ordinary strip shift can also be tested against smooth compactly supported functions in \(\log x\), whose transforms suppress the horizontal contours.

For \(w\) approaching \(\rho\) from the left, let \(\Phi_w=V(x^{-w}\mathbf1_{(0,1]})\) in the physical notation. Theorem 4.7 and the Hardy averages defining \(V\) give \(|\Phi_w(x)|\ll_\rho x^{-1/2}\) on \(0<x<1\), uniformly in such \(w\) near \(\rho\). Indeed the initial profile is \(O(x^{-\Re w}+1)\) there, and a Hardy average preserves that bound with constants uniform on a compact parameter set about \(\rho\). Burnol Definition 4.2 gives the \(L^2\) limit \(Y_{\rho,0}^{\lambda}=\lim_{w\to\rho^-}V^{-1}\mathbf1_{[\lambda,\infty)}\Phi_w\). Before the cutoff, unitarity gives
\[
 \langle g,\Phi_w\rangle=(\mathcal I T)(1-\bar w).
\]
This evaluation uses the positive-half-plane Hardy support of \(\mathcal I T\), since \(\mathcal I\) is bounded and analytic there. The removed integral over \((0,\lambda)\) is \(O_\rho(\lambda^b)\) by Cauchy–Schwarz with \(x^{-b}g\). This estimate is uniform in the approaching \(w\), so
\[
 \sqrt L\,\langle\mathcal I T,X_{\rho,0}^{1/N}\rangle
 \longrightarrow(\mathcal I T)(\rho).
\]
The finite-dimensional projection onto these witnesses now gives
\[
 \liminf_{N\to\infty} L\,\operatorname{dist}(T,V_N)^2
 \ge\sum_{\rho\in\mathcal R}|T(\rho)|^2
\]
for each fixed finite set \(\mathcal R\) of simple zeros, using \(|\mathcal I(\rho)|=1\). Exhausting such sets gives \(C_k\). The explicit admissible array in (7) gives the matching limsup. The same finite witness argument works for any candidate spaces contained in the indicated cutoff dilation space after multiplication by \(\mathcal I\).

## Necessity of RH for convergence

Suppose an off-line zero exists. Zeta symmetry gives a zero \(\rho\) with \(1/2<\beta=\Re\rho<1\). Let its multiplicity be \(m\). On \(S\), the functional \(u\mapsto (Mu)^{(m-1)}(\rho)\) is bounded, with norm at most \(\sqrt{(2m-2)!}/(2\beta-1)^{m-1/2}\). It annihilates every \(V_N\), since the polynomials multiply the same zeta zero. Its value on \(T=-F'/s\) is
\[
 T^{(m-1)}(\rho)
   =-\frac{\zeta^{(m)}(\rho)(k^{1-\rho}-1)}{\rho}\ne0,
\]
because the modulus of \(k^{1-\rho}\) exceeds one. Thus the target has positive uniform distance from all \(V_N\), including from the prescribed approximants. Combined with (7), this proves that convergence of the explicit prime array is equivalent to RH. [Single-member jet argument](jump_generator63_single_member_skeptic.md)
