# Research programme after the Riemann-source import

Status: proposed research programme, with exact interfaces and explicitly open analytic targets.

Scope: connect OpenAI families 003, 007, and 023 to the literal native Möbius covariance programme. Preserve the hypotheses, failed bootstrap, and partial transport conclusions already recorded in PR #908. No new zero-free region or RH progress is certified by this programme.

The primary next task is an analytic estimate for the **complete native coarse covariance**. The companion [exact bridge](NATIVE_MOBIUS_BRIDGE.md) now specifies a way to express that observable using the upstream field's ideal Möbius coefficients. It does not establish that an upstream smooth-family estimate applies to the resulting kernel.

## 1. What this companion adds to the existing import

The [base research plan][base-plan], [comparison][base-comparison], and [conditional bridges][base-bridges] remain the scientific baseline. They already reject an automatic bootstrap from the claimed $7/8$ strip using the full written MHB32 estimate. They identify a valid conditional improvement of one CAP36 completion defect, with principal-phase extraction and the full complement still open.

The new elementary interface is

$$
\beta(n)=\sum_{N\mathfrak a=n}\mu_K(\mathfrak a),\qquad
\mu=\beta*\chi_{-3},
$$

$$
M(x)=\sum_{n\le x}\beta(n)
\mathbf1_{\lfloor x/n\rfloor\equiv1\pmod3}.
$$

This is exact with all Euler factors restored. For a source coprime to 6 the restoration is $(\delta_1-\delta_3)*(\delta_1-\delta_4)$. The companion proves exact completed Gram and NRC32 block-mean versions and provides a finite exact checker. It also verifies the inherited comparison

$$
F_X=E_X+(X+1)u_X^2,\qquad
\mathcal A_X=2F_X-E_X,
\qquad F_X\le\mathcal A_X\le2F_X.
$$

The monotone $F_X$ is consequently a suitable state for a rigorous square-ladder argument. This resolves the bookkeeping issue of filling gaps between completed-state samples. It does not bound the next state.

| Question | Present answer |
|---|---|
| Can ordinary integer $\mu$ be obtained exactly from ideal $\mu_K$? | Yes, by the stated convolution and local restoration. |
| Can the actual completed energy and NRC32 means be written in those coordinates? | Yes, by finite explicit kernels. |
| Are the resulting kernels automatically admissible in the imported estimates? | No. Smoothness, parameter dependence, and all remainders still require estimates. |
| Does the representation reconstruct a square step from fewer coefficients? | No. The norm-source formula uses coefficients through the output scale; Newton supplies the separate old-prefix formula. |
| Does the full MHB32 estimate improve the $3/4$ seed? | No. Its output exponent is $505/546>3/4$. |
| Does the improved CAP36 defect bound control the principal observable? | No. It bounds a difference under bounded-phase hypotheses. |

## 2. Roles of the three relevant source families

All upstream statements below are described as **manuscript assertions at the frozen source**, not independently accepted theorems.

### Family 003: preserve signed allocations and the common kernel

The [5 October quasi-Riemann manuscript][oai003] constructs sextic-twist families of ideal Möbius sums, uses Poisson summation and Gauss identities to reach cubic theta coefficients, completes cube indices, reflects the completed sum, and inverts back while keeping the long inverse-divisor contribution as a child problem.

The load-bearing comparison for our task is its `lem:second-transfer`. Several signed preimages of a transformed pair share **one coupled kernel**. Summing those preimages first leaves a divisibility restriction. The local allocation is

$$
(1+\mathbf1_{p\mid k'})-\mathbf1_{p\mid k'}
-\mathbf1_{p\nmid k'}=\mathbf1_{p\mid k'}.
$$

This is useful as a method only after the preimages have been shown to carry the same kernel and all exclusions. Arbitrarily changing the weights between preimages destroys the cancellation. In the upstream notation, the resulting support restriction yields the smaller-child relations recorded in the [base comparison][base-comparison].

**Proposed native use.** Start from the exact $T_I$ kernels of OAI-NB26-L6, or the completed Gram of L4. Find an arithmetic transformation whose different preimages preserve those kernels, or preserve explicitly controlled common smooth approximants. Sum the signs before any norm or absolute value. Then prove that the surviving child source has smaller support or a strictly cheaper complete energy budget. All norm multiplicities, local factors, old-prefix constants, and repeated product representations must survive the construction.

**First acceptance condition.** Write a finite, coefficientwise transformation identity with a named source class and a common kernel. Check it independently on small native inputs and prove it symbolically. A visual similarity between cubic reflection and Newton inversion is not this identity.

The exact adapter removes the ambiguity between ideal and integer coefficients. It does not supply this transformed common-kernel representation; that remains the next algebraic obstacle.

### Family 007: match graph normalization to the signed residue average

The [ordinary two-point manuscript's introduction][oai007] asserts a power-of-logarithm saving for Liouville correlations along every **fixed** pair of nonproportional affine forms. Its constants may depend on the forms, and it explicitly disclaims uniformity for coefficients growing with the cutoff. Its general binary corrected Elliott assertion concerns one-bounded multiplicative functions with the stated uniform nonpretentiousness hypothesis and gives no quantitative rate for that class.

The proof architecture is relevant to covariance: multiplicative dilations produce a graph; short-interval estimates control centering errors; closed-walk traces estimate the graph operator. In its qualitative route, a factor $\mathbf1_{p\mid n}-\theta/p$ is matched to vertex normalization, and signed residue averages are performed before absolute values. Its quantitative route pays for growing prime supplies and finite residue laws. These are specific mechanisms for retaining arithmetic signs, rather than a generic claim that correlations are small.

**Proposed native use.** Investigate a weighted graph representation of one specified family of terms in the native quadratic or quartic expansion. Identify its vertex normalization, the residues that must remain unconditioned, and every growing shift or modulus. A successful transfer must establish uniformity for that exact weighted family.

There are two immediate barriers. First, expanding $F_X$ already gives

$$
F_X=\sum_{a,b\le X}\frac{\mu(a)\mu(b)}{ab}
(X-\max(a,b)+1),
$$

which includes all differences $|a-b|<X$. An asymptotic for each fixed shift cannot be summed across this growing family without a quantitative budget. Second, squaring an old-prefix Newton block introduces four Möbius coefficients. A two-point statement is not that quartic estimate. Applying the general theorem directly to $\beta$ would also violate its one-bounded hypothesis: $\beta(7)=-2$. Expanding $\beta=\mu*(\mu\chi_{-3})$ reintroduces more variables and requires a new estimate.

**First acceptance condition.** State one exact weighted correlation lemma, with its full range of shifts, coefficient dependence, and total summation cost. A fixed-shift theorem quoted without these data is insufficient.

### Family 023: admissible prime decompositions and off-diagonal character Grams

The [cubic first-moment manuscript][oai023] contains two especially relevant components. Its [decomposition section][oai023-decomposition] preserves exact coefficients in a stopping construction by assigning the reciprocal binomial weight

$$
\binom{k_++k_-}{k_+}^{-1}
$$

to each eligible allocation. This pays for repeated representations rather than choosing one factorization and changing the source.

Its [dual section][oai023-dual] states an exceptional character-moment saving for a restricted class: convolutions of a **bounded** number of prime sequences, each with independently specified fixed smooth norm weights, each supported on primes of norm at least a fixed power of the total length. The bound $Y^{7/3-\eta}$ is in prescribed neighborhoods of two length configurations, not for an arbitrary coefficient sequence or product cutoff. The same section's `lem:character-gram` asserts an off-diagonal row estimate

$$
\sum_{p'\ne p}|T_{p,p'}|^2
\ll_\epsilon(PZ)^\epsilon
Z\left(P+(P^3/Z)^{2/3}\right),
$$

$$
T_{p,p'}=\sum_{n\equiv1\ (3)}
W(N(n)/Z)\chi_p(n)\overline{\chi_{p'}(n)},
$$

with the source's squarefree conductors, fixed smooth weight, and other definitions retained. This is a cubic-character Gram, not the max/floor Gram in OAI-NB26-L4.

**Proposed native use.** Try an exact stopping decomposition of the native source that keeps factor weights independent, counts every representation, and leaves the coupled floor kernel outside the coefficient factors. Identify a genuinely admissible portion of the resulting character family. Any application must then pay for small prime factors, the number of factors, removed squarefree conditions, sharp product boundaries, and the complement outside the exceptional moment's range.

**First acceptance condition.** Produce an exact decomposition with an explicit coefficient identity and a total norm budget for all pieces. Only then test whether a stated 023 estimate applies to a piece. The similarity of the word “Gram” supplies no theorem transfer.

## 3. The exact native target and exponent budget

Use the complete NRC32 cubic mesh of $[Y+1,(Y+1)^2)$, with its literal means

$$
Q_I=2m(Y)-\sum_{r,s\le Y}\mu(r)\mu(s)
\frac{A_{rs}(a+h)-A_{rs}(a)}{hrs},
\qquad S_Y=\sum_Ih|Q_I|^2.
$$

The inherited exact identity is

$$
F_{(Y+1)^2-1}=F_Y+S_Y+D_Y,\qquad0\le D_Y<5/6.
$$

### OAI-RP26-T1 — an open full-covariance budget

For fixed $a\ge0$, $1\le p<2$, and constants $C,A$, attempt to prove, for every sufficiently large native $Y$,

$$
\boxed{\quad
S_Y\le C(\log(2Y))^A Y^a(1+F_Y)^p.
\quad}
$$

This is an **unproved target**. It includes the constant channel, the full coarse covariance, and the entire square step. Proving it for a masked component would not prove T1.

If $F_Y\ll_\epsilon Y^{\kappa+\epsilon}$, its prospective output exponent is

$$
\kappa_{\mathrm{new}}\le\frac{a+p\kappa}{2}.
$$

The old $F_Y$ term is no larger at the level of exponents because $a\ge0$ and $p\ge1$. A strict improvement at the conditional $7/8$ seed $\kappa=3/4$ requires

$$
a<\frac34(2-p).
$$

For example, an input exponent $p=4/3$ needs $a<1/2$, after all smoothing, completion, family-size, and complement costs. A fixed $a>0$ gives the limiting exponent $a/(2-p)$, not the RH endpoint. These are conditional algebraic budgets, not achieved estimates.

The strongest familiar target has $a=0$. With a genuine all-scale $p<2$ inequality, the square ladder and monotonicity of $F$ give subpower energy. Such an estimate would already work from the crude bound $F_Y\le Y$; the external zero-free strip would not be necessary to start it. This is a restatement of the central missing contractive inequality in more explicit coordinates, not evidence that the inequality is easier than RH.

A more operational combination could prove T1 only for native inputs satisfying the conditional $3/4$ energy envelope and the improved pointwise/cap-width bounds. Those hypotheses must be part of the theorem, and their persistence after a square step must be proved. A proof valid in one exponent neighborhood cannot be iterated indefinitely after it leaves that neighborhood.

### OAI-RP26-C1 — a conditional numerical illustration, not a result

If the missing all-scale budget held with $a=0$ and $p=3/2$, exponent arithmetic would send $\kappa$ to $3\kappa/4$. Starting from $\kappa_0=3/4$, it would give

$$
\kappa_j=\frac34\left(\frac34\right)^j,
\qquad
\Theta_j=\frac12+\frac38\left(\frac34\right)^j,
$$

where $\Theta=(1+\kappa)/2$ is the zero-free boundary supplied by the usual native Mellin argument. The first prospective boundary is $25/32$. Arbitrarily small losses must be retained at each finite iteration. No such contraction is proved in the import or this companion.

For completeness, the exponent translation follows by Cauchy–Schwarz on a dyadic interval:

$$
\int_T^{2T}|M(t)|t^{-\sigma-1}\,dt
\le
\left(\int_T^{2T}|M(t)|^2t^{-2}\,dt\right)^{1/2}
\left(\int_T^{2T}t^{-2\sigma}\,dt\right)^{1/2}
\ll_\epsilon T^{(1+\kappa)/2-\sigma+\epsilon}.
$$

Summing dyadically for $\sigma>(1+\kappa)/2$ gives a holomorphic reciprocal-zeta continuation via the native Mellin formula, agreeing with $1/\zeta(s)$ for $\Re s>1$. This implication does not supply the energy bound that it assumes. The exact square-step endpoint $(Y+1)^2-1$, monotonicity, and coverage of intermediate scales remain part of any rigorous recurrence proof.

## 4. Work packages and stopping conditions

| Work package | Concrete deliverable | Required boundary |
|---|---|---|
| 1. Review exact source transport | Independent review of OAI-NB26-L1–L6; rerun the exact checker | Confirms coefficient and kernel identities only. |
| 2. Construct common-kernel signed preimages | A finite algebraic identity for an actual native block family | Keep local factors, norm multiplicities, endpoint and constant terms before estimating. |
| 3. Establish smooth-family admissibility | A decomposition and a written bound for its growing seminorms and total coefficient budget | Pay the remainder in the completed norm or the weighted NRC32 block norm. |
| 4. Test a 003, 007, or 023 estimate on one admissible family | A source-matched theorem with all parameters and quantifiers | A fixed smooth profile, fixed-shift result, or unrelated Gram bound is insufficient. |
| 5. Assemble a strict full-step gain | An explicit $(a,p)$ budget satisfying $a<3(2-p)/4$ at the seed | Include every omitted sector, high-frequency part, transport error, and extraction cost. |
| 6. Prove recurrence closure | Uniform validity on all later native stages, with all hypotheses propagated | One finite gain or one component estimate does not produce an infinite iteration. |

The current most useful stopping point is Work package 2: an exact signed transform for one genuine native kernel. If that fails, the failure should be recorded with the mismatched weights or surviving support identified. If it succeeds, Work package 3 determines whether the analytic saving survives the sharply varying kernel.

The improved CAP36 cap estimate is a reasonable place to budget a known conditional error. It is not a substitute for the new estimate. In particular, bounded $\tau$ transport cannot be combined directly with the existing dephasing range $|\tau|$ of order $L^2$; the full $\tau$-dependence and principal-member extraction must be paid. A family average without a native extraction theorem remains a family average.

## 5. Review and provenance boundary

The local exact checker passed the ranges recorded in [NATIVE_MOBIUS_BRIDGE.md](NATIVE_MOBIUS_BRIDGE.md). Its finite algebra tests do not test the upstream proofs. The descriptions of families 003, 007, and 023 identify source statements and possible uses, without asserting independent proof verification or authorial priority.

This companion preserves the base import's status and immutable references. New all-scale claims should receive separate labels and an exact-SHA review. Any subsequent successful transfer should name the smallest added lemma whose failure would invalidate the gain, rather than describing the import as having closed the existing covariance gap.

[base-plan]: https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/standalone/2026-10-07-openai-quasi-riemann-import/RESEARCH_PLAN.md
[base-comparison]: https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/standalone/2026-10-07-openai-quasi-riemann-import/REPO_COMPARISON.md
[base-bridges]: https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/standalone/2026-10-07-openai-quasi-riemann-import/CONDITIONAL_BRIDGES.md
[oai003]: https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex
[oai007]: https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex
[oai023]: https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex
[oai023-decomposition]: https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/decomposition.tex
[oai023-dual]: https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex
