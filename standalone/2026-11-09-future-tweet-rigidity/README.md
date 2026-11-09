# Future-tweet research: a hypergeometric adapter and the information it must preserve

9 November 2026.

**Status:** proposed standalone research. Complete elementary local identities,
an explicit application of an external analytic theorem, exact finite native
rank certificates, and identified open arithmetic estimates. **No new
zero-free region or proof of RH is claimed.**

**Scope:** the native Mobius projection in PR #1019 and the signed affine
covariance in PR #1022. These are different source objects and are kept
separate throughout. This package adds files; it does not promote or rewrite
an integrated result.

**Exact sources:** repository base
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`; commit-pinned sources in the
individual notes and [inverse/SOURCES.json](inverse/SOURCES.json). The external
analytic input is Fouvry–Kowalski–Michel–Sawin,
[*Bilinear forms with trace functions*, arXiv:2511.09459v2](https://arxiv.org/html/2511.09459v2),
Theorems 1.1/9.1 and Section 9.6. These imported results are distinguished from
the elementary proofs written here.

**What was run:** exact cyclotomic checks of the local kernels and weighted
completion; exact reconstruction checks of the paired channels and CRT
sectors; actual Eisenstein ideal enumeration, sextic symbols, Gauss phases,
Mobius coefficients, and modular rank certificates. Projection energies are
ordinary floating diagnostics. See [VALIDATION.md](VALIDATION.md).

**Smallest remaining gap:** prove an aggregate estimate for the actual signed
arithmetic coefficients after the local transformation, at a cost that beats
the native transfer budget. The identities below supply a kernel and a
reconstruction map, not that estimate.

## The proposed short instruction

> Keep the shift and Fourier frequency together. Recognize their sextic
> correlation as a rank-two hypergeometric kernel. Pair distinct character
> channels to repair its weak mode. Preserve cross-norm Mobius interference
> when returning to the arithmetic source.

This is a research instruction, not a compressed proof of an open conjecture.
The useful progress is that each clause now has either a proved mathematical
meaning or a precisely identified missing estimate. In particular, saying
only “apply trace-function bounds” would conceal the joint coefficient that
completion produces.

## 1. A genuine local route to an existing analytic theorem

For a nontrivial character chi on F_q, zero-extended at the origin, define

\[
 S_\chi(z)=\sum_y\chi(y)\overline{\chi(y-1)}e_q(zy),
 \qquad K_\chi(z)=q^{-1/2}S_\chi(z).
\]

The completed shifted correlation is exactly

\[
 \sum_x\chi(x)\overline{\chi(x-h)}e_q(tx)=S_\chi(ht),
 \qquad h\ne0.
\]

The axes have explicit different values and must be retained. The decisive
identification is

\[
 q\operatorname{Hyp}(z;\{1,1\},\{\bar\chi\})
   =\bar\chi(-1)G(\chi)S_\chi(z),\qquad z\ne0.
\]

Thus K is a normalized type-(2,1) hypergeometric trace function, up to a unit
scalar. At prime q>3 its disjoint character lists and automatic primitivity
fit the cited monodromy theorem. The imported FKMS bilinear theorem then
gives a saving for separated coefficients on its specified intervals:

\[
 \sum_{h\sim H,t\sim T}\alpha_h\beta_tK_\chi(ht)
 \ll\|\alpha\|_2\|\beta\|_2(HT)^{1/2-\eta},
\]

when H,T<=q/2, H>=q^delta and HT>=q^(3/4+delta), for a suitable eta>0.
This is a proved interface with an existing theorem, rather than an analogy
between unrelated sums. The prime-field interval hypothesis is not silently
extended to inert-prime fields, Eisenstein boxes, or composite conductors.

The distinction between the two Fourier arrangements is essential. Holding a
Fourier frequency fixed in the bare ratio kernel leaves a rank-one product.
Keeping h and t together produces the hypergeometric function of ht.

**Full proof, source audit, spectrum and masks:**
[coupled/LOCAL_KERNEL.md](coupled/LOCAL_KERNEL.md).

## 2. Two channels recover the mode that one channel almost loses

Let B_chi have product kernel S_chi(ht)/q on F_q^*, and let P_1,P_chi denote
the orthogonal projections onto the constant and chi character vectors.
The entire Gram operator is explicit:

\[
 B_\chi^*B_\chi
 =I-(1-q^{-2})P_1-(1-q^{-1})P_\chi.
\]

A single channel suppresses the constant mode by q^(-1) and the chi mode
by q^(-1/2). Subtract the constant component to obtain C_chi. If chi and
its conjugate are distinct, their normalized pair satisfies

\[
 \boxed{
 \frac{1+q^{-1}}2\|(I-P_1)f\|_2^2
 \le\frac{\|C_\chi f\|_2^2+\|C_{\bar\chi}f\|_2^2}{2}
 \le\|(I-P_1)f\|_2^2.}
\]

The lower bound is sharp and the decoder is explicit. This removes the
single-channel square-root loss. Any two distinct nontrivial characters
give the same repair; this matters for a quadratic native local character,
whose conjugate alone is the same character. The supplementary output still
needs its own arithmetic estimate.

For a squarefree ideal conductor with r prime factors, tensoring the pair
uses 2^r channels on the space mean-zero at every local coordinate. To
reconstruct all unit-space sectors, retain each local constant projection as
a third output, giving 3^r channels. Retaining zero coordinates gives 4^r.
The total losses are subpower in the conductor norm for a fixed number field.
No constant-coordinate or nonunit sector disappears without being named.

This is an unconditional finite reconstruction result. It does not identify
the global theta contribution with the local constant mode, and does not
bound the transformed outputs. The subpower algebraic channel count also
does not establish a uniform composite-modulus version of FKMS.

**Full proof and exact CRT accounting:**
[local_operator/TWO_CHANNEL_LOCAL_ADAPTER.md](local_operator/TWO_CHANNEL_LOCAL_ADAPTER.md).

## 3. The missing bridge has a measurable cost

For a factored arithmetic block f,g, completion produces the joint weight

\[
 W(h,t)=w(h)\sum_xf(x)\overline{g(x-h)}e_q(-tx).
\]

The local off-axis source is q^(-1/2) sum W(h,t)K_chi(ht), together with
the two explicitly retained axes. The automatic identity

\[
 \sum_{h,t}\left|\sum_xf(x)\overline{g(x-h)}e_q(-tx)\right|^2
 =q\|f\|_2^2\|g\|_2^2
\]

does not make W a product weight. On a permissible rectangle the bilinear
theorem extends rigorously as

\[
 \left|\sum_{h,t}W(h,t)K_\chi(ht)\right|
 \ll(HT)^{1/2-\eta}\|W\|_*,
\]

where ||W||_* is its nuclear norm. A saving follows if its ratio to the
Frobenius norm is sufficiently small. No such estimate is asserted for the
native Mobius/prime coefficients.

There is a sharp reason this cannot follow just from a same-vector origin:
take w=1 and f=g=e_q(cx^2), with c nonzero. Then W is supported on t=2ch and is a phase-weighted
permutation matrix. On nonzero h,t, its nuclear/Frobenius ratio is exactly
sqrt(q-1). Large separation cost already occurs on rectangles in the size
range of the imported theorem. A direct estimate exploiting the curve could
still succeed; the counterexample targets generic cheap separation.

**Exact identity, sufficient criterion, proof and counterexample:**
[transfer/WEIGHTED_ADAPTER.md](transfer/WEIGHTED_ADAPTER.md).

## 4. Norm-twist averaging erases precisely the Mobius information we need

For good squarefree Eisenstein ideals, mu_E(n) depends only on the integer
norm Nn. Split primes contribute (-1) to each degree-one ideal; inert primes
contribute (-1) to their degree-two ideal. Equal-norm ideals therefore have
the same sign and must be grouped coherently.

Write a_m for the unsigned coherent packet with norm m and sigma(m) for
that sign. Then

\[
 y_\mu(t)=\sum_m\sigma(m)a_mm^{it},\qquad
 y_+(t)=\sum_m a_mm^{it}.
\]

After any fixed linear row operator, their infinite norm-twist covariances
are exactly equal. The orbit closures for each finite packet are also identical, by
continuous-time Kronecker approximation on rational-prime logarithms.
Consequently a method using only this fully averaged covariance cannot
distinguish the signed source from the unsigned one.

The exact finite-window difference is

\[
 C_T^\mu-C_T^+
 =-2\sum_{\sigma(m)\ne\sigma(k)}
       a_ma_k^*\operatorname{sinc}(T\log(m/k)).
\]

This identifies the information to retain: interference between different
norms carrying opposite signs. The note proves a quantitative dephasing bound
and the optimal finite-dimensional criterion for extending a proposed frame.

### Actual native calculation

This uses Eisenstein ideals and their actual symbols, not a random matrix.

| D | U | Squarefree rows | Squarefree columns | Exact coherent norm-packet rank |
|---:|---:|---:|---:|---:|
| 256 | 128 | 37 | 74 | 31 |
| 1024 | 512 | 139 | 294 | 115 |
| 4096 | 2048 | 583 | 1,145 | 413 |

The ranks are certified by nonzero minors modulo 1009. At the largest scale,
14 actual Gauss labels with K=43 capture about 2.194% of the specified
untwisted source energy and 4.595% of its norm-twist mean energy. An optimal
extension needs 107 more dimensions to capture 90% of that mean, according
to the numerical covariance spectrum.

These energy figures are floating diagnostics. K=43 exceeds #1019's separate
K<=D^(1/7) range; no theorem from that PR is applied there. At the tested
natural label cap D/U=2, only the unit label occurs. These experiments neither
establish a limiting exponent nor disprove a fixed-source asymptotic estimate.

**Proofs, exact ranks, native code and complete numerical scope:**
[inverse/README.md](inverse/README.md).

## 5. A sharper statement about scalar filters

Finite words in prime divisibility shifts and valuation masks, at a fixed
finite set of primes, can change only those Euler factors of a reciprocal
L-function. This includes the exact defect in the naive Mobius sign-flip
rule: multiplication by p kills the p-divisible sector.

There is also an optimal cost for a scalar profile filter supported at
scales 1<=d<=R. If its Mellin multiplier preserves a real mode beta and kills
lambda>beta, then its weighted coefficient mass is at least

\[
 \coth\!\left(\frac{(\lambda-\beta)\log R}{2}\right).
\]

The bound is attained at the two endpoints. This prices the support/amplitude
tradeoff explicitly; it does not forbid a new signed arithmetic estimate for
the filtered source. The existing paired-scale notch in PR #1002 remains
properly credited.

**Proofs and exact hypotheses:**
[local_operator/SCALAR_FILTER_BUDGET.md](local_operator/SCALAR_FILTER_BUDGET.md).

## Where to work next

The priority is the signed aggregate after completion. Freeze the actual
lambda coefficient and prime-extracted source from #1022, including all
four Mobius signs, coprimality conditions, local axes and the whole
sixth-power-core resonance. Derive its completed joint weight. Then establish
a sufficiently economical rectangle decomposition, or an estimate adapted
directly to that weight's arithmetic dependence. Restore the D log U factor
and sum the complete shift family before invoking the consumer.

The parallel inverse route must retain the signed cross-norm kernel above,
or find independently controlled local relations for the actual untwisted
source. Infinite norm-twist averaging cannot supply the missing Mobius
advantage.

The paired local frame is available as an exact source-return map in either
route, provided the same complete vector and every retained sector are
carried through the estimates. This package supplies the map and identifies
the estimates it would have to connect.

## Reproducibility and review

The three local checkers use Python's standard library only. The native
projection calculation also requires NumPy. Commands and replay scope are
listed in [VALIDATION.md](VALIDATION.md). Proofs, imported results, exact
finite certificates, numerical diagnostics, and open hypotheses are separate
claim types; no test count is treated as evidence for a global theorem.

The publication contains file-bound independent review notes and a SHA-256
manifest. The PR identifies the frozen commit to which they apply. This is
proposed mathematics for review, not an integrated or independently accepted
resolution of an existing open cut.
