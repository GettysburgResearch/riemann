# Height, common-frequency moments, and higher inverse moments

**Status:** exploratory research note, 2026-10-10. The kernel statements and the conditional moment-to-cancellation transfer below are proved here, relative to the explicitly identified imported inputs. The small conditional geometry deduction developed in the final section is completed in its separately reviewed companion; no independent validation of the full upstream framework is claimed.

**Scope:** the two imported quasi-Riemann manuscripts over \(K=\mathbb Q(\sqrt{-3})\), their pure norm twists, and two possible ways to improve their inverse-moment input. This note does not reverify their complete arithmetic proofs or formalization.

**Exact sources:** OpenAI/math import at upstream commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, in the repository's `standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/`. The root agent checked that the relevant manuscripts are unchanged at upstream `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` on October 10. Source labels and line ranges below refer to the imported files. Existing integrated repository results are not silently assumed to cover these arithmetic families.

**What was actually done:** source inspection; a direct Mellin-kernel calculation, including a unitary identity, uniform demodulated bounds and a large-height asymptotic; propagation of those bounds through the completed quadratic-sieve estimate; exact Möbius recursions for prime extraction; examination of the fourth-moment convolution and of the information contained in separate inverse/plain moments. No Lean build, numerical zero computation, or full two-Poisson hybrid proof was performed.

**Smallest open gaps:** (i) extend the completed height estimate through the full two-Poisson inverse recursion without discarding the separated pure phases; (ii) prove a fourth moment for the exact Möbius/sextic family at row length \(H=D^{1+\theta}\), or a useful common-frequency inverse/plain correlation estimate; (iii) connect any height saving to a quantitative finite zero detector, rather than to an invalid height-local interpretation of an all-scale power bound.

**Late geometry finding:** Section 11 gives an explicit feasible perturbation of the low/high exponent geometry. The chosen tuple is not an algebraically invariant \(7/8\) floor. Its development is now completed in the companion `GEOMETRY_PERTURBATION.md`, whose explicit adapters and full conditional theorem received an independent mathematical review in this research pass. Conditional on the imported analytic framework, the resulting boundary is \(139999/160000=0.87499375\). This is a small constant improvement, independent of the speculative higher-moment route; it is not an independent validation of the upstream framework or a Lean-checked result.

## 1. Results of this pass

The concrete findings are:

1. A large pure norm twist moves the October 5 cubic-theta reflection kernel to a dual scale proportional to \(|t|^4\). After removing its pure oscillatory factor and rescaling, the kernel has uniform smooth bounds and tends to the reflected original profile. Its Mellin \(L^2\) norm is exactly preserved. This gives an explicit conductor cost, not a uniform decay gain.
2. Relative to the imported reflection formula and quadratic large sieve, the completed mean square admits the explicit refinement
   \[
   \sum_{0<Nk\le \mathcal H}|T(X;k,f;W_t)|^2
   \ll (D(1+|t|))^\epsilon\|W\|_{C^J}^2
   \left(\mathcal H+
   \frac{\mathcal H^2Nf(1+|t|)^4}{X}\right).
   \tag{1.1}
   \]
   Here \(W_t(y)=y^{it}W(y)\). Section 4 supplies the precise quantifiers and proof. This does not yet give a corresponding explicit height theorem for the uncompleted Möbius family.
3. A diagonal-size \(2k\)-th moment for the exact sextic family, at \(H=D^{1+\theta}\), would indeed give the exponent
   \[
   \frac12+\frac{5(1+\theta)}{12k}.
   \tag{1.2}
   \]
   The manuscript's one-shot prime-extraction error would obstruct this for \(k\ge2\), but an exact Möbius recursion removes that obstruction. This transfer is proved in Section 7; the higher moment itself remains unproved.
4. The fourth-moment convolution has the correct diagonal size \(D^{2+o(1)}\), but it is outside the coefficient class of both imported inverse-moment theorems. Repeated primes create cubic factors, and balanced divisor weights cannot be treated as a fixed finite list of short prime marks. The September 30 plain fourth moment is not a Möbius fourth moment.
5. Interpolating the existing inverse second moment and plain fourth moment cannot improve the best of their separate row counts. An improvement must use arithmetic correlation that these marginal estimates do not encode.
6. A smaller all-\(x\) power exponent at a single fixed norm twist is already a global statement. A factor \(|t|^{-c}\) at fixed \(t\) improves a constant, not a Mellin abscissa. A finite, quantitatively localized zero detector is the appropriate interface for a height-dependent boundary.

## 2. Source map and exact imported statements

Write **[O5]** for

`The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`

and **[S30]** for

`The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.

Both paths are relative to the imported `upstream/preprints/` directory above. We write \(N\mathfrak a\) for the ideal norm, use primary generators when the source does, and retain the source's zero extensions at all excluded primes.

| Input | Source location | Exact scope relevant here |
|---|---|---|
| Möbius/sextic mean square | [O5], `thm:ms`, lines 679–689 | Fixed finite-order \(\nu\), fixed bad-prime set \(S\), fixed \(0<\theta\le1/10\), fixed \(\epsilon>0\); a finite smooth seminorm controls all \(D\ge2\). |
| Prime extraction and Mellin contradiction | [O5], lines 694–756; `eq:prime-extract`, `eq:mobius-saving` | Sixth powers of primes copy the target row up to omitted multiples of that prime. The zero is fixed before the large scale tends to infinity. |
| Completed cubic-theta family | [O5], `eq:T`, `eq:completed-twist`, lines 1287–1308 | The completion is multiplicative in the cube index, with a fixed finite ray character and exact zero extensions. |
| Completed mean square | [O5], `prop:R`, lines 1317–1333 | \(\mathcal H+\mathcal H^2Nf/X\), with finite smooth derivative cost. |
| Cubic-theta Mellin kernel | [O5], `eq:theta-weight`, lines 1752–1758 | Two gamma ratios with shifts \(7/6\), \(5/6\); this determines the degree-four height scale below. |
| Reflection and moving-row uniformity | [O5], `lem:reflection`, `lem:reflection-uniformity`, lines 1805–1855 | Same cusp coefficient family on fixed ray classes; needed to preserve admissibility after introducing a pure phase. |
| Quadratic sieve and completed proof | [O5], `lem:quadratic`, `lem:squarefree-completed`, lines 1886–2213 | The quadratic sieve permits arbitrary complex squarefree-column coefficients; the prepared dual coefficients are independent of the moving squarefree row. |
| Smooth height bookkeeping | [S30], `lem:smooth-calculus`, lines 1095–1287 | Norm twists and rowwise height suprema have fixed polynomial costs; extra external derivatives improve transform tails. |
| Hecke functional equation and strip growth | [S30], `lem:hecke-strip-growth`, lines 1425–1529 | Finite-order Hecke \(L\)-functions over the complex quadratic field have archimedean conductor proportional to \(Q(1+|t|)^2\). |
| Logarithmic control | [S30], `lem:logarithmic-control`, lines 1531–1603 | A zero-free disk with a positive buffer is an input; the subpower bounds are not an independent proof of such a disk. |
| Common-frequency saturated pair | [S30], `lem:detector-dyads`, `prop:detector-witness`, lines 4385–4685 | Both inverse and plain witnesses use the same character and the same selected height. That height can vary with the row. |
| Auxiliary-height closure | [S30], `lem:late-height-closure`, lines 6514–6584 | A freely chosen cutoff \(T_1=Z^\tau\) absorbs polynomial height losses and external transform tails, after a common positive real-exponent margin is already proved. |
| Marked inverse moment and coefficient restriction | [S30], `lem:marked`, `lem:canonical-moment`, lines 9250–9350 | One inverse factor with a fixed finite list of disjoint prime slots; no arbitrary residual coefficient, even if row independent. |
| Plain fourth moment | [S30], `lem:plain`, lines 12531–12585 | Two plain factors, specific exceptional-row exclusions, and only the declared prime slots. For live slots, \(\kappa\ge3/4\). |

For clarity, the [O5] family is

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\tag{2.1}
\]

For every fixed \(0<\theta\le1/10\) and \(\epsilon>0\), there is a finite integer \(J=J(\theta,\epsilon)\) such that, for a fixed compact interval \(I\subset(0,\infty)\),

\[
\sum_{0<Nu\le D^{1+\theta}}|A_u(D;W)|^2
\ll_{\nu,S,I,\theta,\epsilon}
\left(\max_{0\le j\le J}\|W^{(j)}\|_\infty\right)^2
D^{2+\theta+\epsilon}.
\tag{2.2}
\]

This note uses this as an imported theorem, not as a newly independently verified result.

## 3. What a height twist means, and what it does not mean

### 3.1 Fixed finite order versus a moving archimedean parameter

For \(t\ne0\), the map \(n\mapsto(Nn)^{it}\) is generally not a finite-order Hecke character. It cannot simply be inserted into the words “fixed finite-order character” in (2.2). It can, however, be inserted into the smooth test:

\[
W_t(y)=y^{it}W(y),\qquad
A_u(D;W_t)=D^{-it}\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)(Nn)^{it}W(Nn/D).
\tag{3.1}
\]

The prefactor has modulus one. For every fixed compact support \(I\),

\[
\max_{j\le J}\|W_t^{(j)}\|_\infty
\ll_{I,J}(1+|t|)^J\max_{j\le J}\|W^{(j)}\|_\infty.
\tag{3.2}
\]

Consequently, the literal height-sensitive consequence of (2.2) is

\[
\sum_{0<Nu\le D^{1+\theta}}|A_u(D;W_t)|^2
\ll (1+|t|)^{2J}D^{2+\theta+\epsilon}\|W\|_{C^J}^2.
\tag{3.3}
\]

The elementary omitted-prime estimate uses only \(\|W_t\|_\infty=\|W\|_\infty\). The [O5] extraction therefore gives

\[
|A_1(D;W_t)|
\ll (1+|t|)^J D^{11/12+5\theta/12+\epsilon}
     +D^{5/6-\theta/6}.
\tag{3.4}
\]

For \(|t|=D^\tau\), the first term acquires the positive cost \(J\tau\) in its exponent. No negative height exponent follows from the source's general seminorm bound.

### 3.2 The all-scale quantifier is global

Let \(a_n\) be any sequence, and define

\[
M_t(x)=\sum_{n\le x}a_n n^{-it}.
\]

Partial summation gives the exact identity

\[
M_0(x)=x^{it}M_t(x)-it\int_1^x M_t(u)u^{it-1}\,du.
\tag{3.5}
\]

If, at one fixed \(t\), \(|M_t(x)|\le C_t x^\alpha\) for all \(x\ge1\), with \(\alpha>0\), then

\[
|M_0(x)|\le C_t\left(1+\frac{|t|}{\alpha}\right)x^\alpha.
\tag{3.6}
\]

The same reasoning works for ideal sums, grouped by their integral norm. Thus an all-\(x\) Möbius power exponent obtained at a high but fixed ordinate does not localize the conclusion to that ordinate. A sequence of such exponents approaching \(1/2\) would give the corresponding global cancellation exponents, with constants allowed to deteriorate.

For a smoothed formulation, the same issue is visible in the identity

\[
\int_0^\infty A_1(D;W_t)D^{-s}\,\frac{dD}{D}
=\frac{\widehat W(s+it)}{L_K^S(s,\nu)}.
\tag{3.7}
\]

The twist translates the numerator's profile. It does not move or remove the denominator's other poles. A particular compactly supported test can have Mellin zeros, so claims about an individual test must check those zeros. If the assertion is for every smooth annular test, arbitrary fixed translations of the test are again allowable, so it cannot be interpreted as a theorem about only one ordinate.

In particular, a bound \(D^\sigma(1+|t|)^{-c}\) with \(t\) fixed still has abscissa \(\sigma\). Setting \(D=|t|^B\) changes its appearance on one coupled range; it does not justify replacing that abscissa by \(\sigma-c/B\). The manuscript's contradiction fixes a proposed zero and then uses arbitrarily large \(D\).

There are two valid routes around this limitation:

* an actual improvement of the all-scale real exponent, which is correspondingly global; or
* a finite zero detector, with explicit control of its normalization, localization, residues or joint defect, used only on a quantitative range of \(D\) related to the ordinate.

The latter is the meaningful interface for the repository's proposed local height analysis.

## 4. An explicit height theorem for the cubic-theta reflection kernel

This section contains the main new proved calculation of this note.

Set

\[
c=\frac{(2\pi)^4}{27},\qquad
G(s)=\frac{\Gamma(7/6+s)\Gamma(5/6+s)}
           {\Gamma(7/6-s)\Gamma(5/6-s)}.
\tag{4.1}
\]

For \(V\in C_c^\infty((0,\infty))\), write

\[
\widehat V(s)=\int_0^\infty V(y)y^s\,\frac{dy}{y},\qquad
\mathcal T V(x)=\frac1{2\pi i}\int_{(0)}\widehat V(-s)G(s)(cx)^{-s}\,ds.
\tag{4.2}
\]

This is exactly [O5], `eq:theta-weight`, applied to \(V=V_*\). For real \(t\), let \(V_t(y)=y^{it}V(y)\), \(R=1+|t|\), and define the demodulated, rescaled profile

\[
F_t(z)=\frac{(R^4z)^{it}}{G(it)}\,
             \mathcal T V_t\!\left(\frac{R^4z}{c}\right).
\tag{4.3}
\]

Since \(|G(it)|=1\), no amplitude normalization is hidden here.

### Proposition 4.1. Uniform rescaled bounds

Fix a compact interval \(I\subset(0,\infty)\), \(A>0\), \(0<a<5/6\), and an integer \(j\ge0\). There are a finite integer \(J=J(A,a,j)\) and a constant \(C=C(I,A,a,j)\) such that, for every \(V\in C_c^\infty(I)\), every real \(t\), and every \(z>0\),

\[
\left|(z\partial_z)^jF_t(z)\right|
\le C\|V\|_{C^J(I)}\min\{z^a,z^{-A}\}.
\tag{4.4}
\]

In particular,

\[
\left|(x\partial_x)^j\mathcal T V_t(x)\right|
\ll R^j\|V\|_{C^J(I)}
\min\left\{\left(\frac{cx}{R^4}\right)^a,
           \left(\frac{cx}{R^4}\right)^{-A}\right\}.
\tag{4.5}
\]

**Proof.** On each fixed vertical line \(s=\sigma+iv\) with \(\sigma\ge0\), or \(-5/6<\sigma<0\), Stirling's formula and compact control at bounded \(v\) give

\[
|G(\sigma+iv)|\ll_\sigma (1+|v|)^{4\sigma}.
\tag{4.6}
\]

There are no numerator poles between \(\Re s=0\) and \(\Re s=\sigma\) in these ranges. The first pole to the left is \(-5/6\). The compact smooth support of \(V\) gives, for every fixed \(\sigma\) and integer \(N\),

\[
|\widehat V(-\sigma+i(t-v))|
\ll_{I,\sigma,N}\|V\|_{C^N(I)}(1+|v-t|)^{-N}.
\tag{4.7}
\]

After differentiating the demodulated expression, the derivative multiplier is \(it-s\), rather than \(-s\). Its \(j\)-th power is \(O_{\sigma,j}((1+|v-t|)^j)\). Shifting to \(\Re s=\sigma\) consequently bounds (4.4) by a constant times

\[
z^{-\sigma} R^{-4\sigma}
\int_{\mathbb R}(1+|v|)^{4\sigma}(1+|v-t|)^{j-N}\,dv.
\tag{4.8}
\]

The two inequalities

\[
1+|v|\le R(1+|v-t|),\qquad
R\le(1+|v|)(1+|v-t|)
\]

show that the integral after multiplication by \(R^{-4\sigma}\) is uniformly bounded as soon as \(N>j+4|\sigma|+2\). Use \(\sigma=A\) for the large-\(z\) bound and \(\sigma=-a\) for the small-\(z\) bound. Their minimum proves (4.4). The product rule applied to the pure phase in (4.3) gives (4.5). All contour tails vanish by (4.7). \(\square\)

The source uses the simpler small-argument exponent \(1/4\); the calculation above permits any fixed \(a<5/6\). This is an actual enlarged admissible range for this **kernel bound**, not a new zero-free range.

### Proposition 4.2. Exact norm preservation

For every such \(V\) and every real \(t\),

\[
\int_0^\infty|\mathcal T V_t(x)|^2\,\frac{dx}{x}
=\int_0^\infty|V(y)|^2\,\frac{dy}{y}.
\tag{4.9}
\]

**Proof.** On \(s=iv\), each gamma denominator is the complex conjugate of its numerator, so \(|G(iv)|=1\). Mellin Plancherel gives

\[
\|\mathcal T V_t\|_{L^2(dx/x)}^2
=\frac1{2\pi}\int_{\mathbb R}|\widehat V(i(t-v))|^2\,dv
=\|V\|_{L^2(dy/y)}^2.
\]

The constant dilation by \(c\) and the pure twist are unitary in logarithmic measure. \(\square\)

For nonzero \(V\), a uniform global estimate \(\|\mathcal T V_t\|_2\ll R^{-\delta}\) with \(\delta>0\) is therefore impossible. This does not prohibit cancellation of the arithmetic coefficients in a particular dual sum. It rules out obtaining such a gain from the kernel's global amplitude alone.

### Proposition 4.3. Large-height profile

Let \(q=|t|\ge2\). Uniformly for \(z\) in a fixed compact subinterval of \((0,\infty)\),

\[
\frac{(q^4z)^{it}}{G(it)}\,
\mathcal T V_t\!\left(\frac{q^4z}{c}\right)
=V(1/z)+O_V(q^{-1}).
\tag{4.10}
\]

The same assertion holds after any fixed number of logarithmic derivatives in \(z\), with the corresponding finite seminorm of \(V\).

**Proof.** Write \(G(iv)=e^{i\phi(v)}\), choosing a continuous phase on either sufficiently distant half-line. The logarithmic derivative of gamma gives

\[
\phi'(v)=2\Re\psi(7/6+iv)+2\Re\psi(5/6+iv)
=4\log|v|+O(|v|^{-2}),
\quad
\phi''(v)=4/v+O(|v|^{-3}).
\tag{4.11}
\]

Put \(v=t+u\) in (4.2). After removing the phase in (4.10), the remaining integral is

\[
\frac1{2\pi}\int_{\mathbb R}\widehat V(-iu)z^{-iu}
\exp\!\left(i[\phi(t+u)-\phi(t)-4u\log q]\right)\,du.
\tag{4.12}
\]

For \(|u|\le q/2\), the last exponent differs from zero by
\(O(|u|q^{-2}+u^2q^{-1})\). The complement has arbitrarily small polynomial mass because \(\widehat V(-iu)\) is rapidly decreasing; the gamma quotient on the original line has modulus one. Replacing the exponential by one therefore costs \(O_V(q^{-1})\), also after multiplication by any fixed power of \(u\). Mellin inversion identifies the remaining integral as \(V(1/z)\). \(\square\)

Thus a nonzero profile has order-one reflected amplitude near \(cx\asymp |t|^4\). The apparent high-frequency suppression at fixed \(x\) is accounted for by movement of the support to a longer dual range.

### Proposition 4.4. Explicit height in the completed mean square

Use exactly the family \(T(X;k,f;W)\) of [O5], `eq:T` and `eq:completed-twist`. Fix \(\epsilon>0\), \(C_0\ge1\), a compact interval \(I\subset(0,\infty)\), a finite ray character \(\xi\), and the bad-prime datum \(S\). There is a finite integer \(J\) such that, for every \(D\ge2\),

\[
1\le\mathcal H,X,Nf\le D^{C_0},
\]

every primary squarefree \(f\) prime to \(S\), every \(W\in C_c^\infty(I)\), and every real \(t\), estimate (1.1) holds. The implied constant depends only on the displayed fixed data, not on \(t,D,\mathcal H,X,f\).

**Proof relative to the imported arithmetic inputs.** Apply the exact reflection formula [O5], lines 1805–1821, with \(V_t(y)=y^{it}\sqrt y W(y)\). The finite character data stay unchanged: the pure norm twist is kept in the weight, rather than being falsely declared a finite ray character.

In the prepared dual sum [O5], `eq:prepared-theta-sum`, lines 1948–1955, the reflected argument is

\[
x=\frac{3^mNn\,(Nb)^3\mathcal H_0^2}{Y(Nk_0)^2}.
\tag{4.13}
\]

By (4.3), the reflected weight is a constant of modulus one times

\[
(cx)^{-it}F_t(cx/R^4).
\tag{4.14}
\]

The phase factors into a column factor \((Nn)^{-it}(Nb)^{-3it}\), a row factor \((Nk_0)^{2it}\), and factors depending only on the frozen labels. The column factors can be included in the coefficients \(A_m(n,b)\) of [O5], lines 2008–2018; they preserve their absolute-value bound and their independence of \(k_0\). The row and frozen-label factors have modulus one. Local reindexing at primes likewise adds only unit phases.

The quadratic large sieve [O5], `lem:quadratic`, permits arbitrary complex \(\beta(n)\), so these changes do not alter its hypotheses. The demodulated profile has the uniform bounds (4.4). The separation argument [O5], lines 2116–2156, can therefore be repeated with the effective dual length \(Y\) replaced by a fixed constant times \(R^4Y\), without a further polynomial cost in \(t\).

The prepared row estimate becomes

\[
\ll a^2(DR)^\epsilon\bigl(\mathcal H_0+R^4Y\bigr),
\tag{4.15}
\]

after the same convergent dyadic sums. The arithmetic conductor bookkeeping in `eq:auxiliary-conductor-bound`, lines 1963–1970 and 2063–2087, is unchanged:

\[
a^2\le1,\qquad
a^2Y\ll\frac{\mathcal H_0^2}{X}N(t_0)^2N(g).
\]

Here \(t_0\) denotes the source's frozen squarefree ideal, not the real twist height. It gives the squarefree-row bound

\[
\ll(DR)^\epsilon\|W\|_{C^J}^2
\left(\mathcal H+\frac{\mathcal H^2N(g)R^4}{X}\right).
\]

Finally write \(k=u_0sv^2\) exactly as in [O5], lines 2190–2213, and replace \(g\) by \(fv^2\). Both terms sum against the convergent \(\sum_v(Nv)^{-2}\). All scales involving \(R^4Y\) are bounded by a fixed power of \(DR\), which justifies the loss \((DR)^\epsilon\). This proves (1.1). \(\square\)

### What this does and does not buy

The completed family now has an explicit height-conductor term. It can guide a hybrid implementation and avoids replacing every derivative of \(W_t\) by an unnecessarily large unspecified power of \(t\).

It also exposes the tradeoff in the next step. If the cube-inversion proof is applied using (1.1), its short-cube contribution is

\[
\mathcal H+\frac{\mathcal H^2 F R^4 H_c^3}{X}.
\]

To keep this within \(\Sigma=XF\), a permissible cutoff is

\[
H_c^3\le\min\left\{X,\frac{X^2}{\mathcal H^2R^4}\right\}.
\tag{4.16}
\]

This is smaller than the untwisted cutoff in [O5], line 1336. A formal reuse of the two-Poisson scale relation would make the contraction condition more restrictive, with a factor \(R^4\) in the cube-length comparison. It is not a saving.

**Unproved extension:** we have not shown that both Poisson transforms and every normalization of the uncompleted canonical family preserve a demodulated profile class with no further height costs. The source's finite seminorm theorem allows polynomial costs, but does not identify them with the degree-four cost in (1.1). Claiming the same explicit bound for \(A_u\), or announcing a new \((D,t)\) admissible range from the formal contraction alone, would exceed this proof.

## 5. Height in the September 30 argument

### 5.1 Two different conductor scales

The ordinary Hecke functional equation in [S30], lines 1447–1455, has completion

\[
\Lambda(s,\psi)=(3Q)^{s/2}(2\pi)^{-s}\Gamma(s)L(s,\psi).
\tag{5.1}
\]

Accordingly the analytic conductor at height \(t\) has the scale
\(Q(1+|t|)^2\). Its ordinary reflected plain sum has the corresponding degree-two archimedean scale. The degree-four scale in Section 4 belongs to the **completed cubic-theta transform**, which has two gamma ratios. These are different analytic objects; neither conductor should be substituted for the other.

A shift by \(|\cdot|^{it_0}\) replaces the actual argument of the underlying Hecke function by \(s+it_0\), so its conductor is evaluated at the resulting actual ordinate. Relabeling a low zero as high by twisting does not manufacture a high-conductor gain.

### 5.2 The auxiliary cutoff already pays for height

The pointwise detector bounds [S30], `lem:detector-dyads`, have the structure

\[
|M_r|^2\ll U^{\delta r+\epsilon},\qquad
|S_m|^2\ll U^{\delta\min(m,1-m)+\epsilon},
\tag{5.2}
\]

provided \((1+T_1)^A\le U^{\epsilon/10}\), with a fixed finite height order \(A\) selected before the external tail exponent. The source carefully retains the twist in the \(L\)-function argument during the central contour shift. It estimates the remaining transform tails by integration by parts in an untwisted external profile.

The late-height lemma has errors of the form

\[
Z^{C\beta_*-m}(1+T_1)^{A_\eta}
+Z^{B_\eta}T_1^{-N},
\tag{5.3}
\]

where \(m>0\) has already been proved uniformly in the target datum. It chooses \(T_1=Z^\tau\), first sufficiently small to preserve the real-exponent saving, and then chooses \(N\) sufficiently large to kill the last term. \(A_\eta,B_\eta\) are independent of \(N\).

This is a sound mechanism for closing a previously obtained saving. It is not a theorem that larger actual zero height reduces the real boundary. The cutoff \(T_1\) is adjustable and incurs a cost in the first term.

The logarithmic-control lemma also cannot supply a new boundary by itself. Its subpower estimate for \(L\) and \(1/L\) assumes a zero-free disk with a buffer \(e>0\). Constants depend on that buffer. Using it with a buffer shrinking as the height grows requires a quantitative dependence on \(e\) and a proof that the disk remains zero-free.

### 5.3 Gaussian targeting suppresses coefficients, not poles

For a simple zero \(\rho=\beta+i\gamma\), the formal local contribution to a Gaussian-filtered residue is proportional to

\[
\frac{H_\eta(\rho)}{L'(\rho)}
\exp\bigl((\rho-a)^2\bigr)\,Z^{C(\rho)}.
\tag{5.4}
\]

Its Gaussian modulus includes \(e^{-\gamma^2}\). But that factor is fixed and nonzero once \(\rho\) is fixed. A meromorphic pole is not removed by multiplying its principal part by an extremely small nonzero constant. For a multiple zero, the same point applies to the highest-order nonzero principal-part coefficient, with the familiar polynomial in \(\log Z\) after inversion.

Centering the Gaussian at a target height \(T\) replaces it by

\[
G_T(s)=\exp\bigl((s-a-iT)^2\bigr),\qquad
|G_T(\beta+i\gamma)|=e^{(\beta-a)^2-(\gamma-T)^2}.
\tag{5.5}
\]

At \(\gamma=T\) there is no exponentially small target factor. The contour now traverses the corresponding actual conductor height. At other heights the Gaussian remains nonzero, so an all-scale holomorphy argument still sees their poles unless the numerator cancels them exactly.

Consequently a height-window supremum cannot simply replace the global \(\beta_*\) in the September 30 continuation argument. Its common-signal construction has a nonvanishing numerator at all relevant poles, and its tail cutoff grows with \(Z\). A finite detector can use quantitative suppression outside a window; an infinite-scale Mellin continuation must account for all uncancelled poles.

## 6. What common-frequency inverse/plain information is missing

### 6.1 The source already produces a joint witness

The proposition [S30], `prop:detector-witness`, gives, for a retained row, one character \(\psi\), one zero \(\sigma+i\gamma\), and one separated frequency \(\nu\), such that both polynomials are evaluated at the **same** height \(\gamma-\nu\). With \(\delta=2a-1\), the normalized dyads satisfy

\[
|M_rS_m|^2\gg U^{\delta(r+m)-\epsilon},
\quad |M_r|^2\gg U^{\delta r-\epsilon},
\quad |S_m|^2\gg U^{\delta m-\epsilon},
\tag{6.1}
\]

with

\[
r\le\ell+o(1),\quad r+m\ge\ell-o(1),
\quad r\ge\ell-1/2-O(\epsilon),\quad 0\le m\le1/2+O(\epsilon),
\quad 1\le\ell\le3/2.
\tag{6.2}
\]

We use \(\ell\) for the source's length-cutoff parameter called \(t\), to distinguish it from the actual ordinate.

The proof starts from a product of a truncated reciprocal and a plain \(L\)-series. The coefficient identity \(\mu_K*1=\mathbf1_{\{1\}}\) cancels the unit-scale beginning. Dyadic separation of the surviving product uses a common norm phase for both factors. Thus asking for common frequency is not a new detector hypothesis. The missing input is a sufficiently strong moment for their correlated product, uniformly under the rowwise choices the detector makes.

### 6.2 A precise no-gain statement for marginal interpolation

Suppose an abstract row family satisfies

\[
\sum_u|M_u|^2\ll U^{1+\epsilon},\qquad
\sum_u|S_u|^4\ll U^{1+\epsilon}.
\tag{6.3}
\]

Hölder gives, for \(0\le a\le1\),

\[
\sum_u|M_u|^{2a}|S_u|^{4(1-a)}\ll U^{1+\epsilon}.
\tag{6.4}
\]

On rows where \(|M_u|^2\ge U^{\delta r}\) and \(|S_u|^2\ge U^{\delta m}\), it implies

\[
\#\mathcal R\ll
U^{1-\delta[ar+2(1-a)m]+\epsilon}.
\tag{6.5}
\]

The bracket is a convex combination of \(r\) and \(2m\). Optimizing (6.5) reproduces the better of the separate bounds, with saving \(\delta\max(r,2m)\). It cannot beat both.

This is not merely a failure to choose a good Hölder exponent. With arbitrary nonnegative data \(X_u=|M_u|^2\), \(Y_u=|S_u|^2\), put

\[
R_0=\min\{U/A,U/B^2\},\quad
X_u=A,\ Y_u=B
\]

on \(\lfloor R_0\rfloor\) rows and zero elsewhere. Both moment constraints \(\sum X_u\le U\), \(\sum Y_u^2\le U\) hold, and the better separate count is attained up to rounding. No stronger general joint row count follows from those marginal constraints alone.

### 6.3 A sharp new target, and why the ordinary time mean is insufficient

A genuinely stronger input would be an arithmetic estimate such as

\[
\sum_{u\in\mathcal R}
|M_u(U^r;t_u)S_u(U^m;t_u)|^2
\ll U^{1+\epsilon},
\tag{6.6}
\]

on an explicitly stated nontrivial range with \(r+m\ge1\), preserving the source's masks and allowing the selected common height \(t_u\) for each row. The witness would then give the row-count exponent

\[
\#\mathcal R\ll U^{1-\delta(r+m)+\epsilon}.
\tag{6.7}
\]

Estimate (6.6) is **unproved here**. A fixed common height for every row is a weaker formulation than the detector needs; passing to rowwise heights requires a maximal, Sobolev, or carefully discretized estimate with its cost included.

For one fixed character and heights averaged over an interval of length \(2T\), write the product as

\[
M(t)S(t)=(DN)^{-1/2}
\sum_{\mathfrak r}\psi(\mathfrak r)c_{D,N}(\mathfrak r)(N\mathfrak r)^{-it},
\]

\[
c_{D,N}(\mathfrak r)
=\sum_{\mathfrak a\mathfrak b=\mathfrak r}
\mu_K(\mathfrak a)W(N\mathfrak a/D)V(N\mathfrak b/N).
\tag{6.8}
\]

Divisor bounds give \(\sum_{\mathfrak r}|c_{D,N}(\mathfrak r)|^2\ll(DN)^{1+\epsilon}\). Grouping ideals by their integer norm incurs only another arbitrarily small power, since the number of ideals of a given norm in this fixed quadratic field is divisor bounded. The usual finite Dirichlet-polynomial mean value therefore yields

\[
\int_{-T}^{T}|M(t)S(t)|^2\,dt
\ll (T+DN)(DN)^\epsilon.
\tag{6.9}
\]

One may use the repository's native finite-polynomial inequality with coefficient length \(X\asymp DN\) to prove (6.9). Summing it independently over \(U\) rows pays an extra factor \(U\); it does not give (6.6). It also does not supply a uniform saving at one arbitrarily selected height.

The exact cancellation \(\mu_K*1=\mathbf1\) is promising only if it survives the truncated, smoothed product with a useful quantitative saving. For full unrestricted convolution the identity is exact; for the detector's surviving dyads the divisor sum is restricted. Discarding the weights or replacing this restricted convolution by the full one would erase the actual difficult term.

## 7. A rigorous conditional route from higher inverse moments

### 7.1 Moment hypothesis

Fix \(k\ge1\), \(0<h<6\), the same finite-order \(\nu\), the same fixed set \(S\), and one test \(W\in C_c^\infty((0,\infty))\). Assume that for every \(\epsilon>0\),

\[
\sum_{0<Nu\le D^h}|A_u(D;W)|^{2k}
\ll_{k,h,\nu,S,W,\epsilon}D^{k+\epsilon}D^h
\quad(D\ge2).
\tag{7.1}
\]

This includes **all** rows in the displayed range, including the sixth-power rows that copy the target character. An estimate with those rows removed does not suffice for this extraction.

### Proposition 7.2. Higher-moment extraction with exact prime removal

Under (7.1), for every \(\eta>0\),

\[
A_1(D;W)\ll_{k,h,\nu,S,W,\eta}
D^{\alpha+\eta},\qquad
\alpha=\frac12+\frac{5h}{12k}.
\tag{7.2}
\]

The conclusion can be restricted to \(\alpha<1\) when a nontrivial cancellation result is desired; the proof of the implication itself does not need that restriction.

**Proof.** Let \(Y=D^{h/6}\), and let \(\mathcal P(D)\) be the prime ideals outside \(S\) with \(Y/2<N\mathfrak p\le Y\). The fixed-field prime ideal theorem gives

\[
J(D)=|\mathcal P(D)|\asymp Y/\log Y
\]

for sufficiently large \(D\). Define

\[
B_p(x)=A_{p^6}(x;W)
=\sum_{(n,S)=1,\ p\nmid n}\mu_K(n)\nu(n)W(Nn/x).
\tag{7.3}
\]

Because \(\mu_K(pm)=-\mu_K(m)\) if \(p\nmid m\), and vanishes otherwise, exact separation of multiples of \(p\) gives

\[
A_1(x;W)=B_p(x)-\nu(p)B_p(x/Np).
\tag{7.4}
\]

Iterating in the smaller argument gives the finite identity

\[
B_p(x)=\sum_{j\ge0}\nu(p)^j A_1(x/(Np)^j;W).
\tag{7.5}
\]

It is finite because compact support makes \(A_1(y;W)=0\) for sufficiently small \(y\). Thus

\[
A_1(D;W)=\frac1J\sum_{p\in\mathcal P(D)}B_p(D)
-\frac1J\sum_{p\in\mathcal P(D)}\sum_{j\ge1}
\nu(p)^jA_1(D/(Np)^j;W).
\tag{7.6}
\]

The prime sixth powers are distinct rows of norm at most \(D^h\). Hölder and (7.1) bound the first term by

\[
\left(\frac1J\sum_{p\in\mathcal P(D)}|B_p(D)|^{2k}\right)^{1/(2k)}
\ll D^{(k+h-h/6+\epsilon)/(2k)}(\log D)^{1/(2k)}.
\tag{7.7}
\]

Fix \(\beta>\alpha\), and choose the loss in (7.1) sufficiently small that (7.7) is \(O(D^{\beta-\delta})\) for some \(\delta>0\). Use induction on dyadic intervals to prove \(|A_1(x;W)|\le Cx^\beta\) for all \(x\) above the fixed lower support threshold. Every argument on the second line of (7.6) is at most \(2D/Y<D/2\) once \(D\) is sufficiently large. Under the inductive bound, its magnitude is at most

\[
\frac C J\sum_{p\in\mathcal P(D)}
\sum_{j\ge1}(D/(Np)^j)^\beta
\le C_\beta C D^\beta Y^{-\beta}.
\tag{7.8}
\]

For a fixed sufficiently large starting threshold this is at most \(\tfrac12CD^\beta\). Choose \(C\) large enough to cover the bounded starting interval and the first term (7.7). This closes the induction. Setting \(\beta=\alpha+\eta\) proves (7.2). All sums use the same fixed \(\nu,S,W\); no moving prime has been placed in the implied-constant datum. \(\square\)

### Consequences if the proposed moment could be proved

Take \(h=1+\theta\), with arbitrarily small fixed \(\theta>0\). The limiting exponents are:

| Moment input | Conditional cancellation exponent | Status |
|---|---:|---|
| \(\sum|A_u|^2\ll D^{1+\epsilon}H\) | \(11/12\) | Imported [O5] case. |
| \(\sum|A_u|^4\ll D^{2+\epsilon}H\) | \(17/24\) | New analytic input required. |
| \(\sum|A_u|^6\ll D^{3+\epsilon}H\) | \(23/36\) | New analytic input required. |
| \(\sum|A_u|^{2k}\ll D^{k+\epsilon}H\) | \(1/2+5/(12k)\) | New analytic input for each \(k\). |

For a zero-free conclusion, the moment hypothesis must hold for each smooth annular test needed by the Mellin argument. At each fixed \(k\), constants may depend on \(k\) and \(\theta\); no uniformity as \(k\to\infty\) is required to rule out a fixed zero strictly right of \(1/2\), if the moment theorem is available for all fixed \(k\).

The proof is stronger than blindly applying [O5], `eq:prime-extract`, to a higher moment. That one-shot argument retains an error \(D/Y=D^{1-h/6}\), which exceeds \(D^{17/24}\) when \(h\) is near one. Equations (7.4)–(7.8) are the necessary repair.

## 8. Why the fourth moment is not an imported corollary

Expanding the square of the polynomial, using the multiplicative extension of the sextic symbol in its denominator, gives

\[
A_u(D;W)^2=\sum_{\mathfrak r}b_D(\mathfrak r)\chi_{\mathfrak r}(u),
\]

\[
b_D(\mathfrak r)=\nu(\mathfrak r)
\sum_{\mathfrak a\mathfrak b=\mathfrak r}
\mu_K(\mathfrak a)\mu_K(\mathfrak b)
W(N\mathfrak a/D)W(N\mathfrak b/D).
\tag{8.1}
\]

Its support satisfies \(N\mathfrak r\asymp D^2\), and each prime valuation is at most two. Thus it is cube-free, not necessarily squarefree.

### 8.1 Diagonal size

The divisor bound and the number of pairs in the support imply, for every \(\epsilon>0\),

\[
\sum_{\mathfrak r}|b_D(\mathfrak r)|^2\ll_{W,\nu,S,\epsilon}D^{2+\epsilon}.
\tag{8.2}
\]

For example, bound one divisor count in \(|b_D|^2\) by \((N\mathfrak r)^\epsilon\), and bound the sum of the absolute coefficient mass by the \(O(D^2)\) admissible pairs. For nonnegative \(W\), all nonzero summands at a fixed \(\mathfrak r\) have the same Möbius sign \((-1)^{\Omega(\mathfrak r)}\) and the same factor \(\nu(\mathfrak r)\), so there is no artificially hidden sign cancellation in this diagonal estimate.

Moreover, if \(\chi_{\mathfrak r}\overline{\chi_{\mathfrak s}}\) is principal at every good prime, each prime exponent in \(\mathfrak r/\mathfrak s\) is divisible by six. Those exponents lie in \([-2,2]\), so they are all zero: \(\mathfrak r=\mathfrak s\). Thus the natural sextic diagonal here has precisely the ordinary multiplicative-energy scale. No oversized sixth-power column diagonal has been found that disproves the target \(D^2H\).

This compatibility is not a proof of the off-diagonal estimate.

### 8.2 The actual coefficient obstruction

Without the balanced smooth restrictions, the local coefficient of \(\mu_K*\mu_K\) is

\[
(1-z)^2=1-2z+z^2.
\tag{8.3}
\]

On squarefree \(\mathfrak r\), the coefficient contains \(\mu_K(\mathfrak r)\) times a divisor-decomposition weight, equal to \(2^{\omega(\mathfrak r)}\) in the unweighted full convolution. The balanced version in (8.1) still records all factorizations with both factors at scale \(D\).

Writing the two squarefree factors as

\[
\mathfrak a=\mathfrak c\mathfrak a_0,\qquad
\mathfrak b=\mathfrak c\mathfrak b_0,
\qquad
(\mathfrak a_0,\mathfrak b_0)=
(\mathfrak a_0\mathfrak b_0,\mathfrak c)=1,
\]

gives \(\mathfrak r=\mathfrak c^2\mathfrak a_0\mathfrak b_0\) and

\[
\chi_{\mathfrak r}(u)
=\chi_{\mathfrak c}(u)^2\chi_{\mathfrak a_0\mathfrak b_0}(u).
\tag{8.4}
\]

The repeated-prime part is a cubic character factor with its own exact zero extension. It cannot be dropped or relabeled a harmless fixed mask.

The canonical marked theorem [S30], lines 9306–9320, expressly disallows any additional residual coefficient on the squarefree column, even if independent of the row. Its allowed weights are products from a bounded fixed list of disjoint short prime slots. A full balanced divisor weight is not such a list: the number and distribution of prime factors are unrestricted as \(D\) grows. The fixed-ray cubic Gauss coefficient produced by the \(\mu\)-conversion also does not by itself produce the extra divisor weight or square part in (8.1).

The plain fourth moment [S30], `lem:plain`, concerns two ordinary Hecke polynomials without the Möbius coefficients, and uses exceptional-row exclusions. Those exclusions must be checked against the target's sixth-power rows, which the extraction in Section 7 needs to retain. One cannot replace its plain factors by inverse factors by a pointwise comparison of absolute values.

### 8.3 Why simply squaring the length loses the gain

Even an idealized arbitrary-coefficient sieve of the form

\[
\sum_{Nu\le H}\left|\sum_{Nr\asymp X}b(r)\chi_r(u)\right|^2
\ll(H+X)X^\epsilon\sum|b(r)|^2
\tag{8.5}
\]

would, at \(X=D^2\), give \(\ll D^{4+\epsilon}\) when \(H\asymp D\), not the desired \(D^{3+\epsilon}\). Formula (8.5) is used here only as an illustrative even-optimistic length comparison, not asserted as an available theorem for arbitrary sextic coefficients.

Similarly, treating \(A^k\) as a polynomial of length \(D^k\) and requiring a row range of roughly that length makes prime extraction return the old \(11/12\) scale. The useful new theorem must exploit the convolution's structure while retaining \(H\) near \(D\), rather than near \(D^k\).

## 9. Concrete next research steps

### A. Close the height-aware completed-to-inverse interface

Use Proposition 4.4 as a terminal estimate. Define a canonical family that stores a pure norm phase separately from the smooth compact profile. At each of the two Poisson transformations, record the phase's sign, its split between row and column variables, and the exact dependence of every remaining profile seminorm on height. Check closure before changing any real-exponent inequalities.

The success criterion is a theorem with explicit \((\mathcal H,X,F,t)\) hypotheses and an explicit analytic-conductor term. It may be useful even if it gives a height cost: it prevents incorrect optimistic optimization and tells the finite detector which scale ranges are actually affordable.

### B. Attempt the fourth moment in the original factorization variables

Keep \(\mathfrak a=\mathfrak c\mathfrak a_0\), \(\mathfrak b=\mathfrak c\mathfrak b_0\) instead of treating \(b_D\) as arbitrary length-\(D^2\) coefficients. Separate the common-prime cubic factor exactly. The candidate new closure theorem must allow two inverse blocks, with their coprimality masks and common factors, and show that the transformed factorization remains in the same class.

A bounded number of prime marks can plausibly help handle controlled parts of a factorization, but no finite-prime decomposition has yet been shown to cover the unrestricted balanced divisor weight with acceptable cost. The proof should first target \(\sum|A_u|^4\ll D^{2+\epsilon}H\), because Proposition 7.2 then converts it to \(17/24\) without any further prime-removal bottleneck.

### C. Prove a common-frequency mixed moment on the shortest useful range

The first useful target is a version of (6.6) near \(r+m=1\), with the source's same-character and same-frequency requirements and explicit rowwise-height control. The coefficient (6.8) retains a truncated \(\mu_K*1\) cancellation. That is an arithmetic advantage absent from marginal Hölder interpolation.

A theorem valid only after discarding the rows carrying the target character, or after allowing unrelated frequencies in the two factors, would not match the source detector. A theorem with arbitrary pointwise coefficients is stronger than needed; preserving this exact convolution could be the tractable route.

### D. Use a finite local detector for a height-dependent boundary

The native repository's proposed finite joint-defect detector is the appropriate place to test an actual high-height saving. Its bound must include the norm of the chosen witness, all derivatives used by Sobolev evaluation, off-window contamination, the scale at which the explicit formula is used, and any lower bound required for the signal.

A formal expression \(\sigma(T)=1/2+c/\log T\) is not evidence of such a bound. Establish one explicit inequality connecting a zero at \(\beta+iT\) to a positive localized energy lower bound, then show that the combined arithmetic/analytic estimates contradict it on a nonempty, explicitly stated \((\beta,T)\) range. That would be a real height-sensitive result even if the first range is modest.

## 10. Claims that this note does not make

The height and higher-moment calculations above do not independently establish a new zero-free region. The September 30 plain-moment input is stated only for \(\kappa\in[3/4,1]\); its final choice \(\kappa=2\beta_*-1\) does not authorize plugging in \(\kappa<3/4\) and iterating the same endpoint formulas toward \(1/2\). There is, however, a different valid route: keep \(\kappa=3/4\), use the already imported \(\beta_*\le7/8\), and perturb the physical geometry. Section 11 analyzes this route; the companion `GEOMETRY_PERTURBATION.md` completes the deduction conditional on the imported machinery.

The genuinely proved additions are the explicit reflection-kernel analysis and completed height bound in Section 4, and the conditional higher-moment extraction in Section 7. The higher moment and mixed moment remain clearly identified new inputs. A shrinking high-height zero-free boundary, if obtained only for the original untwisted function, would still need its low-height exceptions handled before implying full RH. By contrast, an all-scale Möbius exponent at even one fixed twist is already global by (3.5)–(3.6); these two claims must not be conflated.

## 11. Completed geometric follow-up

The final parameter investigation has been completed in [GEOMETRY_PERTURBATION.md](GEOMETRY_PERTURBATION.md). It proves, conditional on its listed imported analytic machinery, the boundary \(139999/160000\), using the corrected per-subset row norm and all explicit contour, normalization and capacity adapters. It introduces no new moment hypothesis. Its proof and independent scoped review are separate from the height and higher-moment lemmas above. The [exact envelope limit](GEOMETRY_ENVELOPE_LIMIT.md) explains why parameter tuning alone cannot produce a dramatic improvement with the same row-count function.
