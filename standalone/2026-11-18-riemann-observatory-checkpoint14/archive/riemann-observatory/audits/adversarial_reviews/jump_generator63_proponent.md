# Generator and compact resolvent of the Manzur–Noor jump group

Date 2026-11-17. The exact jump transport has the closed generator \(G=i(L-H)\) on the logarithmic moment domain. The resolvent is compact and the spectrum consists of the algebraically simple points \(i\log n\), \(n\ge1\). The group norm and the norms of its spectral projections both obstruct normality under an equivalent Hilbert norm. The calculations use the step-space transport reconstructed from Manzur–Noor (13)–(14) and Proposition 4.1, with the sharp norm established in the director adjudication. These are deductions about the transport operator. [Manzur–Noor v1](https://arxiv.org/pdf/2610.03568v1) · [Step-space and sharp norm adjudication](director_manzur_noor_round8.md)

The underlying group has an exact antecedent. With \(\mathcal S\) the forward shift on canonical coefficient sequences, Sklyar–Marchenko's \(H_1\) in Theorem 8 is the completion in the norm \(\|(I-\mathcal S)c\|_2\), and their group multiplies the \(n\)-th coordinate by \(n^{it}\). The map \(U=I-\mathcal S\) extends to a unitary from that \(H_1\) onto \(\ell^2\) because its initial range is dense. Manzur–Noor (15), with the disk coordinate \(j=n-1\), identifies the transported group as \(U V_t U^{-1}=T_{-t}^*\) for the earlier diagonal group \(V_t\). Sklyar–Marchenko's later Theorem 3.1 gives the spectrum and coordinate resolvent for that exact family. The calculations below reconstruct them in the Manzur–Noor weighted cell coordinates and derive the additional estimates there. [Sklyar–Marchenko v2, Theorem 8](https://arxiv.org/pdf/1405.2731v2) · [Resolvent theorem](https://doi.org/10.4171/JST/344) · [Detailed source comparison](finite_moment63_manzur_noor_operator_antecedents.md)

## Closed generator and cores

Write \(S\) for the unit-step subspace of \(L^2([1,\infty),dx/x^2)\), \(w_n=1/[n(n+1)]\) for the cell weights, and \(b_n\) for the cell values of \(f\in S\). Set \(b_0=0\), \(d_n=b_n-b_{n-1}\), and \(v_n=\mathbf 1_{[n,\infty)}\). Thus \(v_n\) has only one nonzero jump, at \(n\). The transported group has
\[
 (J_\tau b)_n=\sum_{k\le n}k^{i\tau}d_k
   =n^{i\tau}b_n-\sum_{k<n}\big((k+1)^{i\tau}-k^{i\tau}\big)b_k .
\]
The finite span of the \(v_n\) is dense since it contains every finite cell sequence. The group acts continuously on that span and is locally bounded in operator norm, since \(\|J_\tau\|=\sqrt{1+\tau^2}+|\tau|\). Hence it is strongly continuous on \(S\).

Define
\[
 (Lb)_n=(\log n)b_n,\qquad
 (Hb)_n=\sum_{k<n}\ell_k b_k,\qquad
 \ell_k=\log((k+1)/k).
\]
The operator \(H\) is bounded with \(\|H\|\le2\). Indeed, on cell \(n\) its absolute value is bounded by \(\int_1^x|f(y)|\,dy/y\) for \(x\in[n,n+1)\). Under the isometry \(f\mapsto e^{-u/2}f(e^u)\), that unsigned integral operator becomes one-sided convolution with \(e^{-u/2}\mathbf 1_{[0,\infty)}(u)\), which has \(L^1\) norm 2. The estimate is sharp. For \(1/4\le \alpha<1/2\), take \(b_n=n^\alpha\). Comparing \(H b_n=\int_1^n \lfloor y\rfloor^\alpha\,dy/y\) with \((n^\alpha-1)/\alpha\) gives a uniformly bounded error in \(n,\alpha\), by the mean-value bound \(y^\alpha-\lfloor y\rfloor^\alpha\le C y^{\alpha-1}\) for \(y\ge2\). Meanwhile \(\|(n^\alpha)\|_S\to\infty\) as \(\alpha\uparrow1/2\), so \(\|H b\|/\|b\|\to2\).

The infinitesimal generator is
\[
 Gb=i(L-H)b,\qquad
 D(G)=D(L)=\left\{b\in S:
   \sum_{n\ge1}\frac{(\log n)^2 |b_n|^2}{n(n+1)}<\infty\right\}.
\]
For necessity, every fixed cell evaluation is continuous on \(S\). Differentiating its finite jump sum gives \(i(L-H)b\). If this derivative is in \(S\), boundedness of \(H\) gives \(Lb\in S\). For sufficiency, in the difference quotient of the second expression for \(J_\tau b\) the diagonal quotient \((n^{i\tau}-1)/\tau\) is bounded by \(\log n\). The off-diagonal coefficient
\[
 \frac{(k+1)^{i\tau}-k^{i\tau}}{\tau}
   =i\int_k^{k+1}y^{i\tau}\,\frac{dy}{y}
\]
is bounded by \(\ell_k\). Thus the off-diagonal sums are dominated by \(H|b|\in S\), and both parts converge in \(S\) by dominated convergence. This identifies the maximal domain of strong differentiation. The formula is closed because \(L\) is a closed multiplication operator and \(H\) is bounded. Their graph norms are equivalent. Truncation of the cell values converges in the graph norm of \(L\), so finite cell sequences are a core. Every \(v_n\) belongs to \(D(G)\), because the weighted logarithmic square is summable on its tail. The finite span of the \(v_n\) contains the finite cell core and is also a core.

## Mellin domain and evaluation

Let \(F=Mf\) with \(Mf(s)=\int_1^\infty f(x)x^{-s-1}\,dx\). For \(\Re s>1/2\), evaluation is bounded on \(S\) by Cauchy–Schwarz in the ambient space. The exact identity
\[
 M(J_\tau f)(s)=\frac{s-i\tau}{s}F(s-i\tau)
\]
then gives
\[
 M(Gf)(s)=-i\left(F'(s)+\frac{F(s)}s\right)
          =-\frac{i}{s}(sF(s))',\qquad f\in D(G).
\]
The derivative itself has an exact domain characterization. The difference between \(\log x\) and the cell multiplier \(\log \lfloor x\rfloor\) is bounded. Write \(g(u)=e^{-u/2}f(e^u)\) and let \(a>0\). The derivative \(F'(1/2+a+it)\) is the Fourier transform of \(-u e^{-au}g(u)\) on the positive half-line. Plancherel gives
\[
 \int_{\mathbb R}|F'(1/2+a+it)|^2\,\frac{dt}{2\pi}
   =\int_0^\infty u^2e^{-2au}|g(u)|^2\,du .
\]
Consequently \(f\in D(G)\) exactly when \(F'\) belongs to the half-plane Hardy space, by monotone convergence as \(a\downarrow0\). Multiplication by \(1/s\) is bounded there, so the same characterization holds using \(F'+F/s\).

Point evaluation has different thresholds in the original norm and the graph norm. On finite cell sequences let \(q_n(s)=\int_n^{n+1}x^{-s-1}\,dx\). For each fixed \(s\), \(|q_n(s)|\sim n^{-\Re s-1}\). Evaluation extends boundedly on \(S\) exactly when \(\sum_n|q_n(s)|^2/w_n<\infty\), which gives \(\Re s>1/2\). In the graph norm one may replace \(w_n\) by \(w_n(1+(\log n)^2)\). The threshold is then \(\Re s\ge1/2\), and Cauchy–Schwarz gives absolute Mellin integrability at the boundary for every \(f\in D(G)\). The boundary evaluation of \(F'\) is still unbounded in this graph norm. Its coefficients have magnitude asymptotic to \((\log n)n^{-\Re s-1}\), and at \(\Re s=1/2\) the squared functional norm diverges harmonically. The displayed generator evaluation therefore has the open-half-plane domain stated above.

Any bounded unit-step function belongs to every power domain of \(G\). More generally, the formula for \(L-H\) carries \(O((1+\log n)^r)\) cell growth to \(O((1+\log n)^{r+1})\), using the telescoping sum of the \(\ell_k\). Every such growth bound implies the domain condition for \(G\). Iterated evaluation on a power domain gives
\[
 M(G^m f)(s)=\frac{(-i)^m}{s}(sF(s))^{(m)}.
\]
For example, the nonprincipal anchored generators \(g_{\chi,k}(x)=S_\chi(x/k)-k^{-1}S_\chi(x)\) are bounded. Their Mellin transform gives the nonzero anchor derivative
\[
 M(Gg_{\chi,k})(1)=i\,L(1,\chi)\frac{\log k}{k}.
\]
This recovers the infinitesimal failure of invariance of the anchored space from its annihilating evaluation at 1. [Anchored Mellin formula](witness62_manzur_noor_step_bridge.md)

## Spectrum, resolvent, and projection norms

On the graph domain the jump of the generator is a scalar multiple of the original jump.
\[
 d_n(Gb)=i\log n\,d_n(b).
\]
It gives \(Gv_n=i\log n\,v_n\) directly. For \(z\notin\{i\log n:n\ge1\}\), put \(c_n=(z-i\log n)^{-1}\) and \(d(z)=\inf_n|z-i\log n|>0\). Solving in jumps forces the formula
\[
 (R_z b)_n=\sum_{k\le n}c_k d_k(b)
  =c_n b_n-\sum_{k<n}(c_{k+1}-c_k)b_k,\qquad
 c_{k+1}-c_k=i\ell_k c_k c_{k+1}.
\]
With \(D_a\) denoting multiplication by a bounded sequence \(a\), the formula is
\[
 R_z=D_c-H D_{(i c_k c_{k+1})_{k\ge1}},\qquad
 \|R_z\|\le d(z)^{-1}+2d(z)^{-2}.
\]
This is a bounded operator on \(S\), and both diagonal sequences in the formula tend to zero, so \(R_z\) is compact. Put \(u=R_z b\). Its jump identity implies \((z-i\log n)u_n+i(Hu)_n=b_n\) coordinatewise, hence \(Lu\in S\). Thus \(u\in D(G)\) and the equation gives \((z-G)R_z=I\). The jump equation likewise gives \(R_z(z-G)=I\) on \(D(G)\). This proves
\[
 \sigma(G)=\sigma_p(G)=\{i\log n:n\ge1\},\qquad R_z=(z-G)^{-1}.
\]
All spectral points are isolated. At \(\lambda=i\log n\) an eigenvector is uniquely determined by its jump at \(n\), so the eigenspace is one-dimensional. The \(n\)-th jump of \((G-\lambda)u\) is zero for every \(u\in D(G)\). Hence no nonzero multiple of \(v_n\) can be the last nonzero vector in a generalized eigenvector chain, proving algebraic simplicity.

The Riesz projection is \(P_n b=(b_n-b_{n-1})v_n\). To see this, integrate the resolvent over a small positively oriented circle around \(i\log n\) and evaluate each jump. The only surviving residue occurs for jump \(n\). Since \(\|v_n\|^2=1/n\), and the \(n\)-th jump functional has squared norm \(2n^2\) including the case \(n=1\), we get
\[
 \|P_n\|=\sqrt{2n}.
\]
In particular, the dense eigenvector span does not give a Schauder basis of the tails in any order. Any such ordering would have uniformly bounded single-coordinate projections, as differences of uniformly bounded partial-sum projections. Its projected coefficient at \(v_n\) would have to be \(d_n(b)\), by applying the continuous jump functional to the basis expansions.

In fact the singular values of the compact resolvent satisfy \(s_j(R_z)\sim1/\log j\) as \(j\to\infty\). Write \(R_z=(I+K)D_c\) with \(K=-H D_{(i c_{k+1})_{k\ge1}}\) compact. Given \(0<\epsilon<1\), split \(K=K_0+E\) with \(K_0\) of rank \(r\) and \(\|E\|<\epsilon\). The singular values of \((I+E)D_c\) lie between \((1-\epsilon)s_j(D_c)\) and \((1+\epsilon)s_j(D_c)\), by applying the standard ideal inequality to \(I+E\) and its bounded inverse. Adding \(K_0D_c\) shifts the singular-value comparison by at most \(r\) places in each direction, by finite-rank interlacing. For large \(k\), \(|c_k|\) decreases and is asymptotic to \(1/\log k\). Rearranging its finitely many early values does not affect that asymptotic. Sending \(j\to\infty\) and then \(\epsilon\downarrow0\) gives the result. Thus the resolvent belongs to no Schatten class of finite exponent.

For \(\tau\ne0\), the bounded group element \(J_\tau\) has the whole unit circle as spectrum. The eigenvalues \(n^{i\tau}\) are dense in that circle, by taking \(n\) nearest to growing real solutions of \(\tau\log x=\theta+2\pi k\). The exact group norm growth gives spectral radii 1 for both \(J_\tau\) and its inverse by taking powers. Therefore the spectrum is confined to the circle and contains it by closedness. The operator \(J_0=I\) has spectrum \(\{1\}\).

## Bounded similarity and the role of arithmetic evaluations

Put \(A=-iG\), so \(A\) has real spectrum and \(J_\tau\) is generated by \(iA\). If a bounded invertible \(X\) made \(XGX^{-1}\) normal, its imaginary spectrum would make it skew-adjoint by the spectral theorem. Its strongly continuous group would be unitary, and uniqueness of the generator would give
\[
 \|J_\tau\|\le\|X^{-1}\|\,\|X\|\qquad(\tau\in\mathbb R).
\]
The exact norm \(\sqrt{1+\tau^2}+|\tau|\) is unbounded, which rules out such a similarity. The same argument rules out bounded similarity of \(A\) to a normal or self-adjoint operator. Equivalently, a bounded positive metric with bounded inverse cannot furnish those properties on \(S\). Independently, normality under bounded similarity would bound all the Riesz projection norms by the same condition number, conflicting with \(\|P_n\|=\sqrt{2n}\).

Coercivity is essential to that metric conclusion. For example \(Cb=(d_n(b)/n^2)_{n\ge1}\) defines an injective Hilbert–Schmidt operator into \(\ell^2\), since its row norms squared sum to \(2\sum n^{-2}\). It has dense image since each \(v_n\) maps to one nonzero coordinate. One has \(CJ_\tau=D_{(n^{i\tau})}C\), and the bounded positive injective operator \(C^*C\) defines a weaker norm in which the group acts by isometries. Its inverse is unbounded. Completion in that weaker norm gives the diagonal unitary group on \(\ell^2\), with the same integer-indexed frequencies.

The positive frequency count for \(G\) through \(T\ge0\) is \(\lfloor e^T\rfloor-1\). The Riemann–von Mangoldt count grows as \(T\log T/(2\pi)\). Fixed nonzero frequency rescaling preserves exponential count growth for the former. The exact resolvent already accounts for the entire spectrum on \(S\).

Zeta zeros occur in the source construction as arithmetic evaluations. For \(r_k(x)=\lfloor x/k\rfloor-\lfloor x\rfloor/k\), \(k\ge2\), the bounded step sequence satisfies
\[
 sM r_k(s)=\zeta(s)(k^{-s}-k^{-1}).
\]
At a right-half critical-strip zero \(\rho\) of multiplicity \(m\), \(M(\,\cdot\,)(\rho)\) annihilates the closed span of the \(r_k\). The power-domain formula gives
\[
 M(G^m r_k)(\rho)
   =\frac{(-i)^m}{\rho}\,\zeta^{(m)}(\rho)(k^{-\rho}-k^{-1})\ne0 .
\]
Here \(1/2<\Re\rho<1\) makes the moduli of the terms in parentheses unequal. Thus invariance of that arithmetic span under \(G\) on its graph domain would force RH, by applying \(G\) repeatedly to \(r_k\) and then using zeta symmetry. The converse follows from the established density criterion when RH holds. This is a subspace-invariance criterion. Its proof uses the arithmetic Mellin factors and the already established density theorem. [Source criterion and evaluation formula](https://arxiv.org/pdf/2610.03568v1)

A sharper version evaluates the \((m-1)\)-st Mellin derivative of \(Gr_k\) at \(\rho\). This bounded functional annihilates the closed arithmetic span and has value \(-i\zeta^{(m)}(\rho)(k^{-\rho}-k^{-1})/\rho\) on \(Gr_k\). Thus the membership of the single first derivative \(Gr_k\) suffices for each fixed \(k\ge2\). [Single-member proof and jet bound](jump_generator63_single_member_skeptic.md) · [Fixed-character extension](jump_generator63_fixed_character_independent.md)
