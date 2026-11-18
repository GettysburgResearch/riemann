# First-generator membership for fixed Dirichlet characters

Date 2026-11-17. For a fixed nonprincipal Dirichlet character \(\chi\), let \(f_\chi(x)=\sum_{n\le x}\chi(n)\), and let \(X_\chi\) be the closed span of its integer dilates in the unit-step space \(S\). Then \(\mathrm{GRH}_\chi\) is equivalent to \(Gf_\chi\in X_\chi\) for the Manzur–Noor jump generator. For a fixed principal character and any integer \(k\ge2\), write \(g_{\chi,k}(x)=f_\chi(x/k)-k^{-1}f_\chi(x)\), and let \(W_\chi\) be the closed span of these anchored generators. Then RH is equivalent to \(Gg_{\chi,k}\in W_\chi\). The reverse implications below use bounded Mellin jets and the same-character zero symmetry. The forward implications invoke previously established integer-dilation density. [Jump generator and Mellin identities](jump_generator63_proponent.md) · [Fixed primitive approximation theorem](director_selberg_transfer_round6.md) · [Manzur–Noor v1, criterion (A)](https://arxiv.org/pdf/2610.03568v1)

## Domains and Euler factors

Set \(U_df(x)=f(x/d)\) for integer \(d\ge1\), with zero extension below 1. With the norm \(\int_1^\infty|f(x)|^2\,dx/x^2\), change of variables gives \(\|U_df\|=d^{-1/2}\|f\|\). Integer \(d\) ensures that \(U_d\) preserves unit-step functions. The operators form the commuting system \(U_dU_e=U_{de}\). The jump of \(U_df\) at \(n\) is zero unless \(d\mid n\), and in that case it is the jump of \(f\) at \(n/d\). The exact jump law yields
\[
 J_\tau U_d=d^{i\tau} U_d J_\tau.
\]
Differentiation in the strong norm shows that \(U_dD(G)\subseteq D(G)\) and, for \(f\in D(G)\),
\[
 G U_df=U_dGf+i(\log d)U_df.
\]

A nonprincipal character has vanishing sum over a complete residue period, so \(f_\chi\) is bounded. A principal character has mean \(r_\chi=\varphi(q)/q>0\) modulo \(q\), so \(f_\chi(x)=r_\chi x+O_q(1)\) for \(x\ge0\). The linear parts cancel in \(g_{\chi,k}\), which is bounded on \([1,\infty)\). All these bounded step vectors belong to \(D(G)\) because \(\sum (\log n)^2/[n(n+1)]<\infty\). In particular no raw principal summatory seed needs to be placed in \(S\).

Write \(\chi_*\) for the primitive inducing character of conductor \(q_*\), and put \(D=\prod_{p\mid q,\ p\nmid q_*}p\). The finite Euler factors act by
\[
 E(s)=\prod_{p\mid D}(1-\chi_*(p)p^{-s}),
 \qquad E(U)=\prod_{p\mid D}(I-\chi_*(p)U_p)
          =\sum_{d\mid D}\mu(d)\chi_*(d) U_d .
\]
All statements include \(D=1\) with the empty product. For each \(p\mid D\), \(|\chi_*(p)|=1\), and \(\|\chi_*(p)U_p\|=p^{-1/2}<1\). Thus \(E(U)\) is invertible on \(S\), with inverse the norm-convergent product of geometric series. Any closed subspace invariant under every \(U_d\) is invariant under both \(E(U)\) and \(E(U)^{-1}\).

Inclusion–exclusion of the Euler primes gives the pointwise identity
\[
 f_\chi(x)=\sum_{d\mid D}\mu(d)\chi_*(d)f_{\chi_*}(x/d).
\]
First suppose \(\chi\) is nonprincipal. Then \(\chi_*\) is nonprincipal as well, both seeds are in \(S\), and this gives \(f_\chi=E(U)f_{\chi_*}\). Since \(X_{\chi_*}\) and \(X_\chi\) are invariant under all \(U_d\), the identity and its inverse give the unconditional equality \(X_\chi=X_{\chi_*}\).

For the anchored span, commute the pointwise finite sum with \(U_k-k^{-1}I\) before moving into \(S\). This gives \(g_{\chi,k}=E(U)g_{\chi_*,k}\) for both principal and nonprincipal characters using bounded vectors on both sides. Set \(g_{\chi,1}=0\). The identity
\[
 U_d g_{\chi,k}=g_{\chi,dk}-k^{-1}g_{\chi,d}
\]
makes every anchored closed span invariant under \(U_d\). Again \(E(U)\) and its inverse give \(W_\chi=W_{\chi_*}\) unconditionally. In particular \(W_\chi=W_\zeta\) for every principal character, with conductor-one seed used in the latter anchored space.

There is also direct transfer of each tested generator membership. On \(D(G)\) the commutator with \(E(U)\) is the bounded operator
\[
 [G,E(U)]=i\sum_{d\mid D}(\log d)\mu(d)\chi_*(d)U_d .
\]
Let \(h_*\) denote the appropriate single primitive seed, either \(f_{\chi_*}\) for \(X_{\chi_*}\) or \(g_{\chi_*,k}\) for \(W_{\chi_*}\), and let \(Y\) denote the corresponding common closed span. Then \([G,E(U)]h_*\in Y\) by dilation invariance, and \(E(U)\) maps \(Y\) onto itself. Consequently
\[
 GE(U)h_*\in Y\quad\Longleftrightarrow\quad Gh_*\in Y .
\]
This uses ordinary integer dilations, including integers divisible by ramified primes. It makes no deduction for a restricted set of dilation indices or a fixed finite coefficient budget. [Earlier finite-length Euler transfer](director_imprimitive_anchor_round8.md)

## One derivative and all multiplicities

Use \(M f(s)=\int_1^\infty f(x)x^{-s-1}\,dx\) and \(L_\chi(s)=L(s,\chi)\). The identities
\[
 sM(U_n f_\chi)(s)=n^{-s}L_\chi(s)\quad(\chi\text{ nonprincipal}),
 \qquad
 sM g_{\chi,k}(s)=L_\chi(s)(k^{-s}-k^{-1})
\]
hold on \(\Re s>1/2\). They follow by summing the integer jumps in \(\Re s>1\) and continuing analytically. In the principal case the factor \(k^{-s}-k^{-1}\) cancels the pole of \(L_\chi\) at 1. By the established strong-domain formula,
\[
 M(Gh)(s)=-\frac{i}{s}\frac{d}{ds}\big(sMh(s)\big)
 \qquad\big(h\in D(G),\ \Re s>1/2\big).
\]

For every \(a\ge0\) integer and \(\beta=\Re \rho>1/2\), the jet \(\mathcal L_{\rho,a}(h)=(Mh)^{(a)}(\rho)\) is continuous on \(S\). Differentiation under the integral and Cauchy–Schwarz give
\[
 \|\mathcal L_{\rho,a}\|^2
 \le\int_1^\infty(\log x)^{2a} x^{-2\beta}\,dx
 =\frac{(2a)!}{(2\beta-1)^{2a+1}} .
\]
The domination on every compact subset of the open half-plane gives the holomorphic derivatives as well. If \(L_\chi\) has a zero \(\rho\) of exact order \(m\) with \(1/2<\beta<1\), every displayed generator of the relevant space has a Mellin zero of order at least \(m\). Therefore \(\mathcal L_{\rho,a}\) annihilates its whole closed span for \(a<m\).

For the nonprincipal test take \(h=f_\chi\) and \(P(s)=1\). For the principal anchored test take \(h=g_{\chi,k}\) and \(P(s)=k^{-s}-k^{-1}\). In each case \(sMh(s)=H(s)=L_\chi(s)P(s)\) with \(P(\rho)\ne0\). For the anchored factor this follows from \(k^{-\beta}>k^{-1}\). The exact jet is
\[
 \mathcal L_{\rho,m-1}(Gh)
   =-\frac{i}{\rho}H^{(m)}(\rho)
   =-\frac{i}{\rho}L_\chi^{(m)}(\rho)P(\rho)\ne0 .
\]
Indeed the Leibniz terms where the derivative hits \(1/s\) contain \(H^{(j)}(\rho)\) with \(j<m\) and vanish. There is no extra factorial because the jet denotes the ordinary derivative itself. This handles a real zero in the open right half of the strip and arbitrary multiplicity. The jet contradicts the claimed membership whenever such a zero exists.

The factors of \(E(s)\) have their zeros exclusively on \(\Re s=0\), and so preserve the multiplicity of every zero in the open critical strip. For the primitive inducer, the functional equation followed by conjugation gives same-character reflection \(\rho\mapsto1-\bar\rho\). Thus exclusion in the open right half of the strip yields GRH for the primitive inducing function. In the principal case that function is \(\zeta\), yielding RH. Classical nonvanishing on \(\Re s=1\) permits the equivalent open-right-half-plane formulation. The extra Euler zeros play no role in either criterion.

Conversely, under \(\mathrm{GRH}_\chi\), the fixed primitive nonprincipal approximation theorem gives finite Dirichlet polynomials \(A\) with \(\|(1-L_{\chi_*}A)/s\|_{H^2}\to0\). Mellin isometry identifies these approximants with \(1\) and finite sums of \(U_n f_{\chi_*}\). Hence \(1\in X_{\chi_*}\). The space is dilation-invariant, so it contains every tail \(U_n1\), whose differences give a dense finite-cell span. It follows that \(X_\chi=X_{\chi_*}=S\) and \(Gf_\chi\in X_\chi\). Under RH the classical Noor criterion transferred to the unit-step space gives \(W_\zeta=S\), so \(W_\chi=S\) and \(Gg_{\chi,k}\in W_\chi\) in the principal case. These directions use the density criteria explicitly.

For a nonprincipal character the anchored space always has \(Mh(1)=0\) for every \(h\in W_\chi\). On the first derivative,
\[
 M(Gg_{\chi,k})(1)=i\,L_\chi(1)\frac{\log k}{k}\ne0.
\]
Nonvanishing here is the usual nonprincipal Dirichlet value at 1. Thus \(Gg_{\chi,k}\) never belongs to \(W_\chi\) in that case. This is consistent with the principal pole cancellation, which instead gives \(M g_{\chi,k}(1)=-r_\chi\log k/k\). [Independent anchor computation](witness62_anchor_nonprincipal.md)
