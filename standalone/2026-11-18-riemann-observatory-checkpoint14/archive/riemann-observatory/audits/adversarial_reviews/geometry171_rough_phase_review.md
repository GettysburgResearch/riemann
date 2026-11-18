# Independent review of rough support and the unit-baseline gap

2026-11-18. The restricted phase-energy statement and its nonnegative rough-supported corollary pass. The estimates do not yield progression bounds centered at \(P/\varphi(k)\). The original common-sequence example and this rough-support result apply to distinct sets of hypotheses. No canonical changes. [Construction under review](weighted170_unit_baseline_campaign.md) · [Earlier common-sequence review](geometry163_common_sequence_skeptic.md)

## Exact conditional coefficient and subfamily energy

Use \(K=X^4\asymp T^\theta\), \(1/2<\theta<2/3\), \(P\asymp KT\) integral, and a fixed proportional band \(\mathcal P=[X,(1+\eta)X]\cap\mathbb P\) with \((1+\eta)^4<2\). Let \(\mathcal S\subset[K,2K)\) be the specified squarefree four-prime family and put \(S=|\mathcal S|\asymp K/\log^4 X\). For any subfamily \(\mathcal U\), form \(H_\mathcal U=\sum_{k\in\mathcal U}d_k h_k\), where the \(d_k\) are bounded above and below by positive constants and
\[
h_k(n)=\mathbf1_{(n,k)=1}\bigl(\cos(2\pi n/k)-\mu(k)/\varphi(k)\bigr).
\]

If \(q\mid k\), write \(r=k/q\); here \((q,r)=1\). The conditional average over a class \(a\bmod q\) is precisely
\[
\mathbf1_{(a,q)=1}\frac{\mu(r)}r
 \left[\cos(2\pi a\bar r/q)-\frac{\mu(q)}{\varphi(q)}\right],
\]
with the evident zero convention for \(q=1\), and \(r=1\) understood by its trivial CRT factor. In fact the two CRT components of \(e(n/k)\) are \(e(a\bar r/q)\) and \(e(b\bar q/r)\); the second sums to \(\mu(r)\) over units \(b\bmod r\), with divisor \(r\) from taking the conditional average over *all* such \(b\). The constant term carries factor \(\varphi(r)/r\) before simplification. This proves the exact centering and bounds every such conditional average by \(2/r\). The projection to the exact reduced denominator \(q\) is an orthogonal subprojection of this dividing-\(q\) average, whence squared coefficient mass \(O(r^{-2})\).

If \(q\) has \(4-m\) band factors, there are \(O(X^m)\) compatible \(k\)'s in any subfamily. Weighted Cauchy–Schwarz on the vector of frequencies with exact reduced denominator \(q\) costs that factor. Summing over \(q\) and reversing the order gives, per \(k\in\mathcal U\), at most \(\sum_{q\mid k} O(X^m/X^{2m})=O(1)\). This proves \(\|\operatorname{coeff}(H_\mathcal U)\|_2^2\ll|\mathcal U|\), uniformly. For the full family, \(1/k\) is a unique contributor with uniformly positive coefficient, so the full coefficient energy is \(\asymp S\).

## Loss on each excluded lattice and centering on the rough set

The original rational Gram bound gives energy \(\asymp PS\) on \(J=[P,2P)\cap\mathbb Z\). For each band prime \(p\), its multiples kill exactly the terms with \(p\mid k\), while the rest have reduced denominators coprime to \(p\). The map \(a/q\mapsto pa/q\bmod 1\) is injective on these frequencies: the reduced denominator of the difference of any two such frequencies is coprime to \(p\), so \(p\) cannot turn a nonzero difference into an integer. Denominators remain at most \(2K\) after the map and the Gram estimate remains valid on the \(m\) interval with \(n=pm\). The length is \(P/p+O(1)\), and \(P/(p K^2\log K)\asymp T/(KX\log K)\to\infty\), since \(1-5\theta/4>0\). Hence lattice energy is \(O((P/p)|\mathcal U_p|)\le O((P/p)S)\).

The union \(J\setminus E\), with \(E=J\cap R\), has size \(O(P/\log X)\) and energy \(O(PS/\log X)\). This uses only \(\sum_{p\in\mathcal P}1/p=O(1/\log X)\) and absorbs the count's \(O(1)\) error per prime since \(P/p\) is large. Thus \(|E|=P(1+O(1/\log X))\) and restricted energy is still \(\asymp PS\). The sum of \(H\) on \(J\) is \(O(KS)\) by period and zero mean. Its sum on \(J\setminus E\) is \(O(P\sqrt{S}/\log X)\) by Cauchy–Schwarz. Removing the mean on \(E\) costs at most \(O(K^2 S^2/P+PS/\log^2 X)=o(PS)\). The first ratio is \(K^2S/P^2\ll K/T^2\to0\).

Let \(H_0=(H-\langle H\rangle_E)\mathbf1_E\) and \(M^2=\|H_0\|_2^2\asymp PS\). Then the proposed \(b^\pm\) of mass \(P\) are supported in \(E\). Orthogonal centering and Cauchy–Schwarz bound their negative corrections by \(K/\sqrt{|E|}=o(1)\), against baseline \(P/|E|\ge1\). Their phase difference against \(H/K\) is exactly \(M\), since \(H_0^+-H_0^-=H_0\) already has zero sum on \(E\) and \(\langle H,H_0\rangle=M^2\). One model therefore has absolute projection at least \(M/2\). This does not bound the maximum individual weight or centered progression errors.

## Why the variance is still missing

For the all-integer uniform baseline the unit discrepancy is
\[
 P/k-P/\varphi(k)+O(1)=-\Theta(P/(KX))+O(1),
\]
uniformly on the selected unit rows. Here \(1-\varphi(k)/k\asymp1/X\) follows from the four comparable distinct primes, and \(P/(KX)\asymp T/X\to\infty\). Squaring and summing over \(\asymp K\) unit classes for each of \(S\) moduli gives \(\asymp P^2/(X^2\log^4 X)\). Its ratio to \(PK\) is \(\asymp T/(X^2\log^4 X)\to\infty\). This is a calculation for the baseline only. It is not a lower bound for the normalized rough-uniform sequence or for the sum of a baseline and perturbation.

On a fixed unit class mod \(k\), for a complementary subset of band primes with product \(d\), \((d,k)=1\) and CRT counts \(P/(kd)+O(1)\) in \(J\). Writing \(\lambda=\sum_{p\in\mathcal P}1/p\), the reciprocal-product total over subsets of size \(r+1\) is at most \(\lambda^{r+1}/(r+1)!\). Bonferroni plus absolute counting of all floor errors bounds the error to \((P/k)\prod_{p\nmid k}(1-1/p)\) by \(O_r((P/k)\lambda^{r+1}+(1+|\mathcal P|)^{r+1})\). Omitting primes dividing \(k\) is necessary since they cannot exclude any integer in the fixed unit row. For the total rough count use the analogous estimate without the omitted factors. Normalizing the product main terms to mass \(P\) would indeed give \(P/\varphi(k)\). Actual normalization has \(|E|\asymp P\), so it costs at most the per-class estimate plus \(O(1/k)\) times the total-count error. It does not remove the absolute error budget by default.

The uniform per-class error sufficient via summing squares is \(O(\sqrt{P/S})=O(\sqrt T\log^2 X)\), because there are \(\asymp KS\) tested unit classes in total. The reciprocal-product majorant \(T/\log^{r+1}X\) at fixed \(r\) is much larger. Paying the displayed combinatorial floor-error bound at increasing \(r\) also exceeds the target. These facts say the two-term bound does not certify the desired variance. They give no lower bound on the actual error, do not use cancellation in floor errors, and do not exclude a sharper averaged estimate. Finally, the proof on excluded lattices uses the exact vanishing of relevant \(h_k\) terms, a property not possessed by an arbitrary perturbation. It does not restore the low-denominator smoothing multiplier after masking. The baseline and perturbation estimates therefore both remain separate open steps in this construction.
