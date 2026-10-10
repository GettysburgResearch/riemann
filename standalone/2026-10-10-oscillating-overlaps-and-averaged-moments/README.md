# Oscillating overlaps and scale-averaged inverse moments

**Status:** proposed standalone research, 10 October 2026. This continuation proves a larger controlled part of the fourth moment and specified higher moments, a uniform theorem for averaging the exact removal operators, and a weaker sufficient moment hypothesis for the same zero-free extraction. **The full short-row fourth moment and the generalized moment hierarchy remain open. No new zero-free boundary or proof of RH is claimed.**

The arithmetic theorem retains the common-factor character instead of bounding it by its modulus. The operator theorem retains the exact identities between scales and averages them before inversion. A separate factorwise theta calculation identifies the precise reciprocal angular Hecke L-factor encountered by the transformed balanced coefficient.

This packet is stacked on [PR #912](https://github.com/GettysburgResearch/riemann/pull/912), frozen at `6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`. It also uses the explicitly pinned results of the sibling [PR #913](https://github.com/GettysburgResearch/riemann/pull/913), frozen at `6498d6cc2eded03159c7332b25fd224ad07f89c1`. Those are proposed research packets with their own review boundaries. No literature-novelty claim or integration verdict is made here.

## 1. The exact problem

Work over \(K=\mathbb Q(\sqrt{-3})\). Fix a finite-order Hecke character \(\nu\) and a finite set \(S\) containing the bad primes. With the original zero-extended sextic residue symbol, set

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\]

The desired arithmetic bound, for every fixed integer \(k\ge1\), is

\[
M_{2k}(D,H):=\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{k,\epsilon,\nu,S,W}HD^{k+\epsilon},
\qquad H=D^{1+\theta},\quad0<\theta\le1/10.
\tag{1.1}
\]

The row sum includes all nonzero Eisenstein elements, including sixth powers and rows meeting fixed bad primes. No nonunit zero is replaced by a primitive character's value one.

## 2. Proved arithmetic gain: preserve the cubic gcd phase

Let \(T_{\ge C}(u)\) be the exact portion of \(A_u(D)^2\) with \(N\gcd(n_1,n_2)\ge C\). It is a polynomial piece whose squared row norm is estimated; it is not asserted to be a positive summand of \(|A_u(D)|^4\).

[OSCILLATING_OVERLAPS.md](OSCILLATING_OVERLAPS.md), Theorem 4.1 and Section 5, proves

\[
\boxed{
\|T_{\ge C}\|_2^2
\ll (DH)^\epsilon D^4
\left[HC^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}\right].
}
\tag{2.1}
\]

For \(H=D^{1+\theta}\), this reaches the desired fourth-moment scale whenever

\[
\boxed{C\ge D^{(5-\theta)/7}.}
\tag{2.2}
\]

The preceding core method in PR #913 required \(C\ge D^{(3-\theta)/4}\). The decrease in the cutoff exponent is

\[
\frac{3-\theta}{4}-\frac{5-\theta}{7}
=\frac{1-3\theta}{28}>0.
\]

| Row-height parameter | Previous gcd cutoff exponent | New gcd cutoff exponent |
|---|---:|---:|
| \(\theta\downarrow0\), limiting comparison | \(3/4\) | \(5/7\) |
| \(\theta=1/20\) | \(59/80\) | \(99/140\) |
| \(\theta=1/10\) | \(29/40\) | \(7/10\) |

These are **gcd cutoff exponents**, not zero-free boundaries.

The proof writes \(n_1=ca\), \(n_2=cb\), freezes \(a,b\), and applies an all-row cubic sieve to the retained factor \(\chi_c(u)^2\). The cubic row decomposition \(u=\varepsilon v^3ab^2\) gives the bracket \(H+H^{1/3}L+(HL)^{2/3}\), with the cube mask retained. Classical squarefree character sieves and elementary ideal counting are the only analytic inputs to this fourth-moment gain.

The same note gives a rectangular version, a designated-incidence theorem for every character order \(6/\gcd(m,6)\), and an explicit extension to a specified portion of every moment of order \(4\ell\). In that extension the outside pairs have designated common factors of norm comparable to \(D\); the first pair uses the improved cutoff (2.2). This is a cofinal collection of controlled configurations, not the cofinal full-moment hypothesis.

Section 7 gives a further Möbius-specific overlap bound under a separately stated imported second-moment premise. That conditional section is not used in (2.1), (2.2), or the new operator theorems.

## 3. Proved operator theorem: exact masks preserve weighted energy

For a fixed core \(r\), put \(\eta(n)=\nu(n)\chi_n(r)\), including all zeros, and define

\[
T_v f(x)=\sum_{d\mid v^\infty}\eta(d)f(x/Nd).
\]

The exact arithmetic identity is \(T_v A_r=A_{rv^6}\). Let \(J(Y)\) count integral ideal bases \(v\) with \(Nv\le Y\). [AVERAGED_MASK_OPERATORS.md](AVERAGED_MASK_OPERATORS.md), Theorem 5.1, proves for every \(\sigma>0\), \(1\le p<\infty\), \(Y\ge1\), and \(T>0\),

\[
\boxed{
\int_0^T|f(x)|^p x^{-p\sigma}\frac{dx}{x}
\asymp_{K,\sigma,p}
\frac1{J(Y)}\sum_{Nv\le Y}
\int_0^T|T_vf(x)|^p x^{-p\sigma}\frac{dx}{x}.
}
\tag{3.1}
\]

The constants are uniform in every completely multiplicative \(\eta\) with \(|\eta|\le1\). The cutoff \(Y\) is fixed throughout this integral. There is no \(Y^\epsilon\) loss, no scale supremum, and no assumption that \(f\) is a finite sum of Mellin modes.

The mean mask operator has exact coefficients

\[
M_Y=\sum_d\eta(d)
\frac{J(Y/N\operatorname{rad}d)}{J(Y)}S_d,
\qquad S_df(x)=f(x/Nd).
\]

In the norm \(\sum_d|c_d|(Nd)^{-\sigma}\), it converges at rate \(O(Y^{-\delta})\), for \(0<\delta<\min(\sigma,1/2)\), to

\[
M=\sum_d\frac{\eta(d)}{N\operatorname{rad}d}S_d.
\]

The limit and its explicit inverse are bounded causal operators. Jensen's inequality supplies the lower energy bound after inversion; an averaged Euler-factor estimate supplies the upper bound. The identity base \(v=1\) covers bounded \(Y\).

The note also proves the corresponding two-sided integrated transfer over all sixth-power-free cores at a fixed row budget. It gives strict separation of finitely many Mellin modes and an exact synthetic model showing why removal identities alone cannot force an improved arithmetic exponent. The finite-mode application has an additional asymptotic hypothesis; it is distinct from the unconditional operator theorem.

## 4. A weaker sufficient generalized-moment hypothesis

[SCALE_AVERAGED_CRITERION.md](SCALE_AVERAGED_CRITERION.md) proves the moving-cutoff argument required for \(Y=(D^h/Nr)^{1/6}\). It then establishes the following implication for the single nonnegative test \(W_*\) from PR #912, whose Mellin transform never vanishes in \(\Re s>0\):

\[
\boxed{
\int_X^{2X}M_{2k}(D,D^h)\frac{dD}{D}
\ll_\epsilon X^{h+k+e_k+\epsilon}
\quad\Longrightarrow\quad
\Re s>\frac12+\frac{5h}{12k}+\frac{e_k}{2k}
\text{ is zero-free for the fixed twist family.}
}
\tag{4.1}
\]

The arithmetic estimate on the left remains a hypothesis. The theorem permits exceptional individual column scales: it asks only for their dyadic integral. The desired pointwise moment bound would imply this averaged bound directly.

The proof uses a separate perturbation estimate for the moving mean operator on functions zero below a sufficiently large scale. It retains the lower-scale forcing term and proves inversion first on finite intervals. This avoids assuming the integrability of the unknown tail. The resulting weighted \(L^{2k}\) estimate makes the Mellin transform holomorphic by Hölder's inequality.

For fixed \(h=1+\theta\) and \(e_k=0\), the boundary in (4.1) is unchanged from the earlier extraction. Along cofinal fixed orders, \(h_k=o(k)\) and \(e_k=o(k)\) would make it approach \(1/2\). Constants need not be uniform in \(k\). The cofinal arithmetic premise is still missing.

## 5. Exact factorwise reflection and the angular reciprocal

[FACTORWISE_THETA_REFLECTION.md](FACTORWISE_THETA_REFLECTION.md) retains an individual outer factor \(a\) through the pinned October 5 theta reflection. Its normalized cubic Gauss phase cancels exactly:

\[
\gamma_2(a)\gamma_4(a)=1.
\]

After including all CRT and row phases, the surviving coefficient contains a quadratic row character, the angular factor \(\overline{\alpha(a)}^3\), and the exact Ramanujan sum

\[
c_a(x)=\sum_{d\mid(a,x)}Nd\,\mu(a/d).
\]

At a fixed reflected frequency, its Dirichlet series is

\[
\sum_{a\ \mathrm{squarefree}}
\frac{\tau_k(a)c_a(x)}{(Na)^w}
=\frac1{L^S_{\tau_k}(w)}
\prod_{\substack{p\mid x\\p\notin S}}
\frac{1+(Np-1)\tau_k(p)(Np)^{-w}}
{1-\tau_k(p)(Np)^{-w}},\qquad \Re w>1.
\tag{5.1}
\]

The character \(\tau_k\) has infinity type \(-3\). It is outside the finite-order family of the imported quasi-Riemann theorem. The note does not use that theorem to cross possible reciprocal poles.

For each fixed frequency, the quadratic sieve can be applied at the original factor length. The frequency sum remains coupled through the Ramanujan factors and transformed scale. The exact reflection is therefore a structural reduction with a specific unresolved norm estimate; it is not a completed proof of the fourth moment.

## 6. The next sufficient arithmetic estimate

Put \(h=1+\theta\) and \(\gamma=(6-h)/7\). Define \(T_{<D^\gamma}\) as the complementary small-gcd portion of \(A_u(D;W_*)^2\). The new large-gcd theorem already controls \(T_{\ge D^\gamma}\). Thus a sufficient remaining fourth-moment estimate is

\[
\boxed{
\int_X^{2X}\sum_{0<Nu\le D^h}
|T_{<D^\gamma}(u;D)|^2\frac{dD}{D}
\ll_\epsilon X^{h+2+\epsilon}.
}
\tag{6.1}
\]

Indeed \(|A_u(D)^2|^2\le2|T_{<D^\gamma}|^2+2|T_{\ge D^\gamma}|^2\). Applying (2.1) and (6.1) would supply the \(k=2\) premise of (4.1). The nearly coprime balanced coefficients are contained in (6.1), and their cancellation has not been proved in this pass.

## 7. Sources, audits, and reproduction

The primary classical inputs are Blomer–Goldmakher–Louvel, [Theorem 1.3](https://arxiv.org/html/1112.1650v1), and Goldmakher–Louvel, [Theorem 1.1 and Corollary 1.2](https://arxiv.org/html/1112.1642v2), in the fixed-field residue-symbol conventions stated in the proofs. Their squarefree-index scope and primitive-character convention are respected before any all-row extension is applied.

The exact sibling input is [REFINED_ALL_ROW_SIEVE.md at PR #913's frozen head](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md). The exact predecessor Mellin test is [MELLIN_AND_SPIKES.md at PR #912's frozen head](https://github.com/GettysburgResearch/riemann/blob/6afd64e042ce7b59d550c3d76e9e2cca8b2c7379/standalone/2026-10-10-generalized-inverse-moments/MELLIN_AND_SPIKES.md). The theta input is the resident October 5 source pinned at OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

[REVIEW.md](REVIEW.md) identifies the proof scopes and independent agent audits. [VALIDATION.md](VALIDATION.md) records exact finite arithmetic coverage and the reproduction commands. [PROVENANCE.json](PROVENANCE.json) binds the source and artifact hashes. These are written mathematical audits and finite checks, not Lean formalization, human peer review, or an integration verdict.

The proof files are byte-identical copies of the reviewed working notes. Review reports retain their original working filenames; the provenance manifest maps those names to the published files. Only this new standalone packet and a navigation entry in the root README belong to this continuation.
