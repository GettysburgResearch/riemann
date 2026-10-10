# Independent review of the packet README

**Reviewer:** \(\texttt{/root/amplification}\), reviewing the root-authored packet summary and its new sufficient arithmetic target.

**Date:** 2026-10-10.

**Verdict:** PASS at the exact content hash below. No blocking mathematical overclaim was found. The sampled small-gcd criterion is a valid sufficient reduction under its stated pointwise premise. Its remaining arithmetic estimate is not proved.

## 1. Exact scope

The reviewed file is:

    riemann/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/README.md

Its SHA-256 is:

    63dc04d705bade6c4a3d7714ac82dfee9bfe96da4bbe1bce2ff646c4e6772cf3

I read the whole README and checked the theorem summaries against these local proof files:

| Packet proof | SHA-256 |
| --- | --- |
| MOBIUS_OVERLAP_TAILS.md | 980c0e5d4e82e4c6105a21db37aeeb84ff19da9c985be571002fe4f3e9bfba04 |
| QUADRATIC_INVERSE_PRODUCTS.md | 7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696 |
| SAMPLED_MOMENT_CRITERION.md | 18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de |
| JOINT_REFLECTED_BLOCKS.md | c75be63f43de6efb0d9f820da008f256afc53351fdbfe38870f9e97207955bd5 |

The quadratic and reflected notes have separate full mathematical reviews by this reviewer. I authored the sampling note, so this receipt is an independent review of the root's summary and new composition, not a nonauthor review of the underlying sampling proof. For the expanded grouped-cubic summary, I read the corresponding mixed correction, physical cubic-product lemma, grouped corollary, and numerical comparisons in the overlap note. This receipt does not replace that note's separate full nonauthor audit.

No packet file was modified.

## 2. Section 6: the sampled small-gcd target

Fix the stated pointwise premise with \(b=7/8\), \(1<h\le11/10\), and \(\gamma=(9-2h)/11\). The identity

\[
A_u(D;W_*)^2
=T_{\ge D^\gamma}(u;D)+T_{<D^\gamma}(u;D)
\]

is an exact partition of the original ordered two-column polynomial by its ordinary gcd. The overlap theorem gives, uniformly at each \(D\) in the dyad,

\[
\sum_{0<Nu\le D^h}|T_{\ge D^\gamma}(u;D)|^2
\ll_\epsilon D^{h+2+\epsilon}.
\]

This applies to the sharp common-factor cutoff under the smooth pointwise premise because the sharp indicator remains on the arbitrary-coefficient cubic axis. It does not require the separate sharp quadratic inverse premise used for the degree-three application.

For the logarithmic grid \(D_j=X\exp(j\Delta_X)\), \(0\le j\le N_X\), the total positive grid mass is

\[
\Delta_X(N_X+1)=\log2+\Delta_X=O(1).
\]

Since \(D_j\in[X,2X]\), the large-gcd sampled energy is therefore \(O_\epsilon(X^{h+2+\epsilon})\). If the displayed remaining small-gcd sampled bound holds, the elementary pointwise inequality

\[
|A_u(D;W_*)|^4
\le2|T_{\ge D^\gamma}(u;D)|^2
+2|T_{<D^\gamma}(u;D)|^2
\]

gives the full sampled fourth moment with the same exponent. Both pieces are signed polynomials before their squared absolute values are taken; no false positivity of their internal tuple contributions is used.

The sampling theorem is then applied to the original smooth fixed-row function \(t\mapsto A_u(Xe^t;W_*)\). It is not applied to a discontinuous sharp-cutoff remainder or to a row vector with moving entry points. At every grid point, the original height \(D_j^h\) contains the common lower row set \(Nu\le X^h\). The recovered integral consequently has fixed height \(X^h\), exactly as required by the proved criterion.

Substituting \(k=2\) and excess \(e=0\) gives the conditional region

\[
\Re s>\frac12+\frac{5h}{24}.
\]

If the proposed arithmetic estimates are obtained at heights arbitrarily close to one, every fixed real part strictly greater than \(17/24\) is covered by one such height. No uniformity of constants as \(h\downarrow1\) is needed for that conclusion. This statement concerns the open half-plane to the right of \(17/24\), not zero exclusion on its boundary line. The README's strict-region notation and conditional language preserve this distinction.

The claimed small-gcd estimate remains an unproved arithmetic target. The existing large-gcd theorem and interpolation alone do not provide it.

## 3. Other theorem summaries and numerical comparisons

The fourth-order tail powers and its cutoff \((9-2h)/11\) match the proof. The exponent improvement over the parent is

\[
\frac{6-h}{7}-\frac{9-2h}{11}
=\frac{3(1+h)}{77}.
\]

The examples \(99/140\), \(69/110\), \(5/7\), and \(7/11\) are correct. The general designated-factor statement retains the character order, support restrictions, and distinction between polynomial portions and a positive partition of a moment.

The quadratic summary correctly states the physical product bound with \(P=\prod L_i\), \(R=\prod L_i^{b_i}\), all nonzero rows, and moving exclusions. Its comparison of the second term and its \(L^{7/4}\) sufficient diagonal height at \(b=7/8\) are correct. The sharper degree-three sharp tail explicitly retains the reciprocal or interval premise.

The grouped double-triangle expression matches Corollary 7.2 of the overlap note. At \(b=7/8\), its three sufficient cutoff exponents are \(3/10\), \(1/2-4h/27\), and \((27-4h)/66\), with the displayed switch at \(27/26\). At \(h=21/20\), the maximum is \(19/55\), and \(33/80-19/55=59/880\). The README correctly restricts this estimate and its higher-order embedding to complete specified incidence families. It does not infer a bound after arbitrary deletion of signed tuples.

The sampling summary states a fixed lower row budget, distributed retained sets or the prescribed finite grid, a fixed detector, and an unproved sampled arithmetic bound. The stated vanishing retained fraction satisfies the quantitative condition in the proof. The slower derivative-growth detector has the displayed iterated-logarithm grid scale. No arithmetic estimate is transferred between detectors. The modulation theorem is separately stated with its growing-aperture limitation.

The reflected-family summary matches the fixed cube dyad and fixed positive ratio profile in Theorem 6.1. It retains the active-conductor length, all repeated-prime rows, local amplitude costs, and strict-margin interpretation of the exponent \(1/3\). Its \(D^{5/2-\theta+\epsilon}\) example and \(5/12\) exponent comparison are correct. The preceding comparison is expressly for a squarefree-row block, whereas the new physical result includes all rows in the specified component.

Finally, the cofinal discussion correctly requires sublinear excess and height along cofinal fixed orders. The described two-native-moment architecture has excess \((2b-1)(k-1)\), which at \(b=7/8\) is \(3(k-1)/4\). Inserting this into the extraction formula returns the limit \(7/8\) when \(h_k=o(k)\). This is a limitation of those estimates, not an impossibility theorem for arithmetic cancellation.

## 4. Qualifications preserved

The README distinguishes the imported pointwise and reciprocal assumptions, the source-qualified theta applications, unconditional sampling inequalities, exact finite diagnostics, and unproved moment targets. It explicitly leaves the full short-row fourth moment, generalized diagonal hierarchy, and RH unproved. It makes no external novelty claim.

This is a content-hash review of the README and its summaries. The eventual frozen source commit and publication receipts require their separately recorded provenance checks. No human acceptance, formal proof assistant validation, or certification of imported analytic hypotheses is implied.

**Signed:** \(\texttt{/root/amplification}\), reviewer, 2026-10-10.
