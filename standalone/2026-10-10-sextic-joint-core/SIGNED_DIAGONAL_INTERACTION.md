# Bounded audit of PR 914's signed initial diagonal

Status: independent mathematical audit of one theorem and its interaction with PR 915. Date: 2026-10-10. Reviewer: `/root/audit_formalization`. No published source was modified. This does not review the whole of PR 914 or certify its A2 completion, conductor sectors, checkers, or replica theorems.

**Verdict.** The exact signed identity and uniform discrepancy bound in PR 914, A2_COMPLETION.md, Section 6, pass this bounded audit. They remove the entire signed first-Poisson product-column diagonal before auxiliary dyadic localization or absolute values. They do not remove any currently load-bearing term from PR 915's scalar Gram high-value inequality, and they do not directly strengthen its positive coupled component estimates. They supply a precise centered signed target through which additional arithmetic information could escape those scalar bounds.

## Exact sources

All four repository files below were read directly from their exact Git objects. The October 5 source was also read from its pinned Git object. Links name immutable commits.

| Object | Exact location and SHA-256 |
| --- | --- |
| PR 914 theorem | [A2_COMPLETION.md, Section 6, lines 453–679](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md#L453), 36,064 bytes; `d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`; Git blob `c163d5e95d76e69eac07631600a3117e055a8046` |
| PR 915 high values | [HIGH_VALUE_SCALAR_OBSTRUCTION.md, Sections 1–4](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/HIGH_VALUE_SCALAR_OBSTRUCTION.md), 7,768 bytes; `de996cf077718d2ba9af351eb998337e8c5c63c8f9ed36bfaf0225128c1dc061`; Git blob `cca86bb0b9b85c728d4ba3682e417cfa664aab90` |
| PR 915 reflection | [COUPLED_THETA_COMPLETION.md, Sections 4–7](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/COUPLED_THETA_COMPLETION.md), 18,030 bytes; `f3b57f69338e8736ffe4addd5a6e2ebf6d5f8976ee9d2fda5921c83ff484eb36`; Git blob `981f102d643f0052489d9025ef305be23a458823` |
| PR 913 Gram inequality | [SEXTIC_GRAM_BOUND.md, Section 5, lines 233–278](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/SEXTIC_GRAM_BOUND.md#L233), 15,156 bytes; `c2b6c326f929de85a4f6d50ae2f4bdf4fc089f4f4705961d1c59ea1ad35d4fe1`; Git blob `e3ffd48f02baf087aab0a2926ddf9ed340f44c33` |
| Original Poisson normalization | [OpenAI October 5 paper2.tex, lines 875–931 and 1031–1175](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L875), 169,005 bytes; `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`; Git blob `2000faddbbebac5de0ecfe0b962534ea61a852d5` |

The load-bearing original labels are `lem:poisson`, `eq:initial-paired-gauss`, and `eq:initial-column-output`. The source's analytic theta theorem is not needed to prove this particular diagonal identity; the arithmetic regrouping and smooth lattice Poisson suffice.

## 1. Normalization and exact reversal

Let \(v\) be row independent, supported on squarefree ideals outside fixed \(S\), with \(Nn\asymp L\). The source conjugates the original polynomial before expanding it. Thus the correctly normalized residual column is

\[
R_L(n)=\sqrt{L/Nn}\,\overline{v(n)}.
\]

Replacing the source's \(W_0\) by this residual column is legitimate in the finite column sums. On \(m_1=m_2=m\), the coefficient is exactly

\[
\frac H{L^2}\mu(f)Nb\,|R_L(bfm)|^2
=\frac HL\frac{\mu(f)}{Nf\,Nm}|v(bfm)|^2.
\]

The squared Gauss coefficient is one. The literal character zeros retain \((m,f)=1\) and \((k,m)=1\); \(b,f,m\) are pairwise coprime squarefree ideals, while \(k\ne0\) is an element and need not be squarefree. This agrees with PR 914 (6.4).

The inverse change of variables is

\[
e=(f,k),\quad t=f/e,\quad h=k/e,\quad g=be,\quad z=tm.
\]

It gives \((h,z)=1\), \(e\mid g\), and \((g,z)=1\), with

\[
\frac{\mu(f)}{Nf\,Nm}=\frac{\mu(e)\mu(t)}{Ne\,Nz},\qquad
bfm=gz,\qquad
\frac{HNk}{(Nf)^2(Nm)^2}=\frac{HNh}{Ne(Nz)^2}.
\]

For fixed admissible \(g,z,e,h\), every \(t\mid z\) reconstructs a summand by \(b=g/e,f=et,m=z/t,k=eh\). The mask \((t,h)=1\) ensures that the reconstructed gcd really is \(e=(f,k)\). No remaining factor depends on \(t\), except \(\mu(t)\). Consequently summing all \(t\mid z\) kills every \(z\ne1\). The result is

\[
\mathcal D[v]=\frac HL\sum_g|v(g)|^2
\sum_{e\mid g}\frac{\mu(e)}{Ne}
\sum_{h\ne0}\Psi(HNh/Ne).
\]

The principal-modulus instance of the source's Poisson lemma gives exactly the stated centered original diagonal, including its lattice normalization:

\[
\mathcal D[v]=\frac1L\sum_g|v(g)|^2
\left\{\sum_{(u,g)=1}\Phi(Nu/H)
-H\Psi(0)\prod_{p\mid g}(1-(Np)^{-1})\right\}.
\]

The unit column and row zero are included with the conventions explicitly given in PR 914. The source removes only the zero Fourier frequency; it expressly retains the nonzero frequencies of the original principal column. There is no missing principal contribution. Evaluating the paired Gauss identity at both unit columns also gives \(\sum_\xi c_\xi=1\), so the fixed-ray recombination counts this common diagonal once.

## 2. The uniform bound is valid

For the fixed radial Schwartz smoothing, put

\[
E_\Phi(T)=\sum_{u\in\mathcal O_K}\Phi(Nu/T)-T\Psi(0).
\]

For \(0<T\le1\), its absolute value is bounded using \(\Phi(0)\), Schwartz decay, and the convergence of \(\sum_{u\ne0}(Nu)^{-a}\) for \(a>1\). For \(T\ge1\), source-normalized lattice Poisson gives

\[
E_\Phi(T)=T\sum_{h\ne0}\Psi(TNh)=O_{K,\Phi}(T^{1-a}).
\]

Thus \(E_\Phi(T)=O_{K,\Phi}(1)\) uniformly for all \(T>0\). Finite inclusion–exclusion bounds the coprime discrepancy by \(O_{K,\Phi}(\tau_K(g))\). Under \(\sum_g|v(g)|^2\ll L D^\epsilon\) and polynomial \(L\ll D^B\), the ideal divisor bound proves \(\mathcal D[v]\ll D^\epsilon\), after reallocating epsilon losses. The proof does not require a lower bound on \(H/L\) or on \(H\).

Fixed smoothing is essential to the displayed constant. The stronger band-limited choice in the source also permits the exact large-\(H/L\) cutoff described in PR 914. Neither assertion is a cancellation theorem for the remaining nonprincipal correlations.

## 3. Three distinct diagonals

| Object | Its role | What PR 914 proves about it |
| --- | --- | --- |
| Original algebraic column diagonal \(n_1=n_2\) | Positive contribution of target size \(H L D^\epsilon\) before division by \(L\) | Its zero Fourier main term remains; only its centered discrepancy is small |
| First-Poisson product-column diagonal \(m_1=m_2\) | Contains an outer signed \(\mu(f)\) sum created by the coprimality expansion | The entire signed sum is exactly the centered original diagonal, hence \(O(D^\epsilon)\) in the \(1/L\) normalization |
| BHM character-row diagonal \(p=p'\) | Positive self-inner-product of one character vector, of size its physical column length | No cancellation is supplied; it is a different Gram matrix with no outer \(\mu(f)\) sum |

In the PR 915 high-value argument, \(A_u(D)^m\) has an unrestricted physical product index of scale \(Z=D^m\) and coefficient energy \(A_2\ll D^{m+\epsilon}\). The BHM estimate is

\[
R V^{2m}\ll (DH)^\epsilon A_2\left[Z+\sqrt{R G(H,Z)}\right],
\qquad G(H,Z)=HZ+H^2Z^{1/3}.
\]

The term \(A_2Z/V^{2m}\), hence \(D^{2m}/V^{2m}\), comes from that positive character-row diagonal. At \(m=2\), integration gives the \(D^4\) term. The signed identity in PR 914 does not change this step.

That diagonal cannot simply be deleted from the same arbitrary-vector Gram statement. For one character row with squared norm comparable to \(Z\), take the coefficient vector proportional to its conjugate. Then the left side is comparable to \(Z^2\), whereas \(A_2\asymp Z\). At \(Z=D^2,H=D^h,h<5/3\), one has \(\sqrt{G(H,Z)}=o(Z)\), so the bound with only the off-diagonal majorant would fail, even allowing a sufficiently small fixed positive epsilon loss. This elementary witness concerns arbitrary Gram vectors, not an actual Möbius coefficient vector.

Nor does PR 914 improve the numerical bound on \(G(H,Z)\) by itself: that quantity averages squared absolute off-diagonal character correlations, after their phases have already been discarded in the norm. A new estimate on the actual balanced coefficients may bypass this route, but the signed diagonal identity is not such an off-diagonal estimate.

There is a further domain distinction. The coefficient of the literal power \(A_u(D)^m\) is generally supported on nonsquarefree products, whereas PR 914's displayed \(v\)-identity concerns a squarefree column polynomial. The balanced coprime product face does have that form; extending its conclusion to the full power requires retaining the exact shared-prime decomposition and its cross terms.

## 4. Consequence for the coupled reflection and scalar obstruction

Our PR 915 component estimates use positive square norms, freeze Ramanujan allocations, and apply triangle or Cauchy inequalities. Their every-cusp and standard-face bounds do not retain the signed first-Poisson auxiliary covariance. In particular, the negative Ramanujan allocation inside the reflected theta coefficient is not the same object as the outer \(\mu(f)\) cancellation in PR 914. The latter does not by itself remove the adverse term of an individually bounded negative component.

The useful combined target is the strict first-Poisson off-diagonal with its original signed auxiliary sum and coupled smooth kernel. In PR 914's notation it is

\[
|\mathcal O_\xi[v]|\ll H D^\epsilon.
\]

A version of the coupled reflection or A2 transfer for this centered sesquilinear form would have to preserve both possibly different auxiliary ideals, all zero masks, and the pulled-back equality of original product columns. PR 914 correctly states that this equality is \(s_t n_1n_2=s_{t'}n'_1n'_2\), rather than equality of factor pairs. Its positive Hilbert-norm transfer does not already prove this centered estimate.

The published scalar spike example remains an obstruction to the same listed scalar upper bounds, since none of those bounds has been improved. The example deliberately does not specify a common arithmetic coefficient vector, so it should not be advertised as a realization of PR 914's additional exact signed identity. An eventual upper bound for the strict signed off-diagonal would be genuinely new information beyond that scalar data and could escape the obstruction. The identity alone supplies no such upper bound.

## Review boundary

This audit derives the signed identity, its uniform estimate, and the distinction between the load-bearing diagonals. It uses no checker output or numerical asymptotic inference. It neither verifies nor rejects the separate A2 arithmetic completion and other PR 914 claims. No full fourth-moment estimate, new zero-free boundary, or RH conclusion follows from this bounded pass.
