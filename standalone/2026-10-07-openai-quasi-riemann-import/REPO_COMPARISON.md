# Relationship to the existing Riemann programme

Status: source comparison and research prioritization, not acceptance of the imported claims.
Snapshot: 7 October 2026.
Scope: selected current branch sources were read mathematically; this is not a fresh audit of every historical packet or a rerun of its computations.
Smallest missing bridge: an all-scale upper bound for the literal native coarse covariance, or an equally source-faithful alternative.

## 1. What is actually published, and where

The current remote main is **f99d9e3908dde4865377c75d9ca051c1f545bf4f**, whose most recent commit is dated 8 September 2026. The later work is present on remote branches, but the five PRs below were all **open drafts, unmerged**, when queried. In several cases the PR description's “final” SHA is older than its actual current head.

| Source | Frozen current head | Read material |
|---|---|---|
| Main | f99d9e3908dde4865377c75d9ca051c1f545bf4f | [Current statements and proof routes](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/research/integrated/CURRENT_RESULTS.md), [scientific status](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/STATUS.md) |
| [#901](https://github.com/GettysburgResearch/riemann/pull/901), research/vasyunin-support-leakage-20260918 | 93126fa9131ebfa93311c1874eeb4cbd93c97864 | [SRL support/Gram proof](https://github.com/GettysburgResearch/riemann/blob/93126fa9131ebfa93311c1874eeb4cbd93c97864/standalone/2026-09-18-vasyunin-support-leakage/PROOF.md) |
| [#903](https://github.com/GettysburgResearch/riemann/pull/903), research/sylvester-cutoff-boundary-20260919 | 72ad9bc0fecf52769d62942a8ad307efe46847ce | [Root-cell covariance and finite gain](https://github.com/GettysburgResearch/riemann/blob/72ad9bc0fecf52769d62942a8ad307efe46847ce/standalone/2026-09-21-root-cell-covariance/PROOF.md) |
| [#904](https://github.com/GettysburgResearch/riemann/pull/904), research/astra/20260919-divisor-square-mesh | 8c506696d8ad7772ccaf48fbb8678fcd889e8beb | [Native composite covariance](https://github.com/GettysburgResearch/riemann/blob/8c506696d8ad7772ccaf48fbb8678fcd889e8beb/standalone/2026-09-20-native-composite-covariance/PROOF.md), [Mellin–Hankel bandwidth](https://github.com/GettysburgResearch/riemann/blob/8c506696d8ad7772ccaf48fbb8678fcd889e8beb/standalone/2026-09-21-mellin-hankel-bandwidth/PROOF.md) |
| [#905](https://github.com/GettysburgResearch/riemann/pull/905), research/astra/20260920-anchored-composite-covariance | 0f82df3bf1d0bc669a1bbca09f8404b77c6fecde | [Dense Mellin covariance](https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-20-anchored-composite-covariance/MELLIN_DENSE.md), [native covariance compression](https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression/PROOF.md) |
| [#907](https://github.com/GettysburgResearch/riemann/pull/907), research/relative-arithmetic-boundary-20260925 | aa725eebf89201fcbefbf7f5e209a22ec318ba5a | [Completion-anchored phase](https://github.com/GettysburgResearch/riemann/blob/aa725eebf89201fcbefbf7f5e209a22ec318ba5a/standalone/2026-09-25-completion-anchored-phase/PROOF.md), [anchored dephasing](https://github.com/GettysburgResearch/riemann/blob/aa725eebf89201fcbefbf7f5e209a22ec318ba5a/standalone/2026-09-25-anchored-dephasing/PROOF.md) |

All branch mathematics above keeps its existing **proposed component proof** status. A remote hash authenticates what was published; it does not establish its theorem. The import must not describe these five branches as already integrated into main.

## 2. Exact mathematical comparison

### Native Möbius inversion and the unresolved full covariance

The current native programme uses
\[
M(k)=\sum_{n\le k}\mu(n),\qquad
m(k)=\sum_{n\le k}\frac{\mu(n)}n,\qquad
F_Y=\sum_{k\le Y}m(k)^2.
\]
Its physical energy is
\[
E_Y=\sum_{k\le Y}\frac{M(k)^2}{k(k+1)}.
\]
These are different from the best Nyman–Beurling approximation error also called \(E_N\) in the support packet.

For \(g(n)=\mu(n)\mathbf1_{n\le Y}\), the classical convolution identity
\[
\mu-(2g-\mathbf1*g*g)=\mu*(\delta-\mathbf1*g)*(\delta-\mathbf1*g)
\]
gives exact native coefficients for **every** \(n<(Y+1)^2\). The target is an all-scale energy gain across that complete square step. The paper's cubic completion/inversion machinery is conceptually close: a completed family is easier to estimate, but inversion introduces a long-divisor part that must be retained and controlled. It is not the same arithmetic source or the same transform.

NCG28 controls a full combined low-denominator contribution by an input-energy power \(F_Y^{4/3}\), with complete covariance and an exact harmonic-tail map; its moving cutoff reaches order \(Y^{16/11}\) near the square-step endpoint. The remaining transformed high composite part is explicitly open. MHB32 supplies an exact Mellin–Hankel adapter for the microscopic rational-angle band and a better bandwidth exponent, but its generic native input exponent remains quadratic. Neither fact can be promoted to a full estimate by adding a zero-free strip to its name.

### What the new zero-free strip would contribute if established

A valid all-height strip \(\Re s>\alpha\), supplemented with the standard reciprocal-zeta growth and summation interface, gives
\[
M(x)=O_\epsilon(x^{\alpha+\epsilon}),\qquad
m(x)=O_\epsilon(x^{\alpha-1+\epsilon}),\qquad
E_X,F_X=O_\epsilon(X^{2\alpha-1+\epsilon}).
\]
Thus the upstream \(7/8\) claim corresponds to energy exponent \(3/4\); the \(11/12\) claim corresponds to \(5/6\). These would be qualitatively important unconditional seeds, but neither is the subpower-energy endpoint.

The exact existing MHB32 exponent map is
\[
\kappa\longmapsto\frac{191+82\kappa}{273}.
\]
For \(\kappa=3/4\), this gives \(505/546\approx0.924908\), **worse** than \(3/4\). Hence the currently proved, completely assembled MHB32 estimate does not improve the claimed \(7/8\) line. See [CONDITIONAL_BRIDGES.md](CONDITIONAL_BRIDGES.md) for the complete bookkeeping and a real improvement to the CAP36 transport-error budget.

### The strongest direct conceptual connection: signed allocation before estimation

In the [5 October upstream source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), lemma \(\mathtt{lem:second-transfer}\), preimages of one transformed pair have the **same coupled kernel**. Their local signed allocation at every \(p\mid f'\) is
\[
(1+\mathbf1_{p\mid k'})
-\mathbf1_{p\mid k'}
-\mathbf1_{p\nmid k'}
=\mathbf1_{p\mid k'}.
\]
After all preimages are summed, the transformed terms have the support condition \(f'\mid k'\). With the paper's notation, this gives
\[
\frac{\mathcal H'}{\Sigma'}\le\frac{\mathcal H}{\Sigma},
\qquad
\Sigma'\le L,
\qquad
\mathcal H'\le\frac{\mathcal H L}{\Sigma F}.
\]
The outer source, residue exclusions, repeated representations and coupled smooth kernel are retained before estimating. The introduction's inversion cutoff satisfies
\[
H_c^3=\min\{X,X^2/\mathcal H^2\};
\]
the longer inverse divisors become an explicitly retained child problem.

This is the type of mechanism our unresolved covariance needs: signed arithmetic identities should force **smaller surviving support or a genuinely contracting child family**, rather than merely split the same large expression into positive pieces. Our Sylvester boundary work already shows why an isolated positive least-prime channel can be large on the actual Möbius source. Our root-cell and NRC32 compression show that almost all hard cancellation can remain in the coarse component after the fine residual is cheaply bounded.

The comparison is an informed research proposal. The displayed local identity is elementary once its common-kernel preimage representation has been justified. It does not prove that the upstream representation or its global induction is correct, and it does not construct its analogue for our real-integer Newton source. In particular, our product kernel, harmonic centering, finite cutoff and \(2m(Y)\) term cannot be substituted into the Eisenstein/cubic-character construction without a new proof.

### Schur, support leakage, heat and xi geometry

The SRL packet supplies exact Nyman–Beurling duals, a permanent \(1/92\) error floor for prime-power-only approximants, indispensability of every squarefree denominator, and
\[
G_N=F_N^{-1}+R_N,\qquad R_N\succeq0,\qquad\operatorname{tr}R_N<11.
\]
The inverse comparison goes in the upper direction; it does not supply the lower inverse-source bound required to make the approximation error tend to zero. A strip \(\Re s>7/8\) does not imply that the critical-line approximation problem converges. The import is useful for comparing completion/inversion methods, not for deleting composite support or replacing the physical Gram by its periodic surrogate.

The main branch's heat, cardinal-capture and effective-Schur results remain separate sufficient criteria or restricted-domain positivity theorems. A fixed zero-free strip would confine the possible off-line spectrum, but does not prove the complete all-window sign, a lower Schur certificate, or high-order xi positivity. Likewise the seven-point continuum certificate and its qualified scalar near \(0.6730085\) concern a different zero-statistical problem; they neither imply nor follow as a numerical refinement of the claimed \(7/8\) line. These boundaries are explicit in the frozen [current statement guide](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/research/integrated/CURRENT_RESULTS.md).

## 3. Why ordinary fixed-shift two-point Chowla is not the missing covariance theorem

For each fixed nonzero \(h\), a statement
\[
\sum_{n\le X}\mu(n)\mu(n+h)=o_h(X)
\]
does not provide a uniform power saving over \(h\) growing with \(X\), smooth cutoffs depending on \(X\), multiplicative/congruence restrictions, or the complete weighted sum of all shifts. It also does not directly control the four old-prefix coefficients that arise on squaring a Newton quadratic form.

This is visible without any heuristic. Exact finite expansion gives
\[
F_X=
\sum_{a,b\le X}\frac{\mu(a)\mu(b)}{ab}\,
      (X-\max(a,b)+1)
\]
and
\[
E_X=
\sum_{a,b\le X}\mu(a)\mu(b)
 \left(\frac1{\max(a,b)}-\frac1{X+1}\right).
\]
Every shift \(1\le |a-b|<X\) occurs. An asymptotic at each fixed shift cannot simply be summed over this growing range. Even an \(o(X)\) rate, if uniform but quantitatively too weak, need not pay all weights and shift counts.

The needed upgrade is a quantitative weighted, growing-family correlation estimate with exactly our kernels and endpoint terms. The explicit coarse target below is preferable to the claim that “Chowla controls covariance.” The elementary identities above are newly written explanatory identities, not a claim that the upstream two-point theorem has been reviewed or supplies the target.

## 4. The precise next native theorem to pursue

Use NRC32's complete cubic mesh of the cells from \(b=Y+1\) to \(b^2-1\). It has fewer than \(10b\) blocks \(I=[a,a+h)\). Define
\[
A_d(t)=tH_{\lfloor(t-1)/d\rfloor}
       -d\lfloor(t-1)/d\rfloor,
\]
\[
K_I(r,s)=\frac{A_{rs}(a+h)-A_{rs}(a)}{h\,rs},
\qquad
Q_I=2m(Y)-\sum_{r,s\le Y}\mu(r)\mu(s)K_I(r,s).
\]
All ordered product pairs, including repeated factorizations of the same product, are retained. Exact Newton reconstruction proves that \(Q_I\) is the mean of the **actual** \(m(k)\) over \(I\). Therefore
\[
F_{b^2-1}-F_Y
=S_Y+D_Y,\qquad
S_Y=\sum_I h\,|Q_I|^2,\qquad
0\le D_Y<5/6.
\]

**Open native contraction target.** Prove that for some fixed \(\delta>0\) and \(A\ge0\), and all sufficiently large \(Y\),
\[
\boxed{\quad
\sum_I h
\left|2m(Y)-\sum_{r,s\le Y}\mu(r)\mu(s)K_I(r,s)\right|^2
\le C(\log(2Y))^A(1+F_Y)^{2-\delta}.
\quad}
\]

This is a concrete all-scale mixed-covariance statement, with no unspecified complement. It includes the native constant and is quartic in old-prefix coefficients after expansion. Its truth is not established by this comparison. It is already identified in NRC32 in equivalent block-mean form; writing the kernel explicitly makes an attempted new transfer testable.

A proposed import-inspired proof should construct a common-kernel signed allocation for these forms, identify every surviving child source and its scale, and prove the cumulative kernel/normalization costs contract. It must explain why the cap-three nonnative counterexamples in the existing packets are excluded by the Möbius identity. The first useful milestone would be **one native block family with a strict power improvement and its full complement cost**, followed by a uniform recursion. Merely rewriting the target as a spectral supremum or proving an average across phases does not meet this milestone.

A contraction of this strength would bootstrap the native energy to subpower. It would already work from a crude polynomial initial bound; the claimed upstream strip is not, by itself, what makes that conclusion possible. A more realistic combined theorem may have hypotheses that explicitly exploit the \(3/4\) energy seed and the improved cap width in CONDITIONAL_BRIDGES.md. Those hypotheses and their persistence under the recursion must then be stated, rather than assumed.
