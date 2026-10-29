# Coupled prefix and completed-theta large sieve

**Status.** This is a source-qualified mixed-moment estimate for a dyadic dual slice. It uses the October 5 completed-theta coefficient and cube decomposition, de Faveri Θ₆, the original finite-ray reciprocity and physical Poisson/profile interface. The source analytic proofs and physical calibration are not independently established here. It does not prove the full source inverse moment or an individual zero-free region.

Use the notation and original zero masks of [the stratified tail note](../2026-10-29-squarepart-stratified-tail/README.md). Let \(A_b(H)\) be the quadratic Möbius/angular prefix, and \(T_{bk}(X;f)\) the normalized completed-theta sum, with fixed \(k,f\) and good sixth-free row \(b\). The following couples the two actual polynomials rather than separately bounding their moments:
\[
 \sum_{Nb\asymp B}|A_b(H)T_{bk}(X;f)|^2
 \ll (BHKFX)^\epsilon H\,\Theta_6(B,H^3X).\tag{1}
\]
The same bound holds for the log-scale derivative of the common theta profile. All constants depend on fixed source/profile parameters and the fixed number field.

To see (1), first fix the source theta cube index q; the source supplies a squarefree n-polynomial of norm scale at most \(X/(Nq)^3\), normalized coefficient squared mass \(\ll (Nq)^{-2}(BHX)^\epsilon\), and a row multiplier \(\chi_q(bk)^3\) of modulus at most one. The cube-index contributions sum harmonically, hence cost \(X^\epsilon\) after row-space Minkowski. For each q, combine the squarefree prefix index h and theta index n into \(m=h^3n\). Every prime valuation of m belongs to \(\{0,1,3,4\}\), so m is sixth-free and h,n are uniquely recoverable even when they overlap. Thus the new coefficient squared mass is \(\ll H(Nq)^{-2}(BHX)^\epsilon\), and its norm length is \(\ll H^3X\). The exact identity \(\chi_h(bk)^3\chi_n(bk)=\chi_m(bk)\) retains every zero. The fixed k,f masks and angular factor \(\mu(h)\bar\alpha(h)^3\xi(h)^3\) are common column coefficients; finite ray phases are separated before applying the source sieve. The source q factor stays a row contraction, not an illicit common coefficient. Applying Θ₆ to m and summing q proves (1).

Abel summation with \(X=D/H^3\) gives, up to logarithms,
\[
 \sum_b|P_{b,>C}(D;f)|^2\ll (BDKF)^\epsilon\frac{\Theta_6(B,D)}C.\tag{2}
\]
This can be minimized **at each cube scale** against the Hölder integrands of the stratified note, before the integration and dyadic maximum. The masks and bounded e-dependent b-row multipliers remain intact.

For a standalone consequence, put \(A=B^2K^2F/D\), \(\Theta=\Theta_6(B,D)\). The physical divisor e has \(D_e=D/Ne\), \(F_e=FNe\), exterior squared weight \((Ne)^{-1}\). The short and tail estimates give
\[
 (Ne)^{-1}BK+A(Ne)C^3+(Ne)^{-1}\Theta/C.
\]
In the admissible interior choose \(C=(\Theta/(A(Ne)^2))^{1/4}\), gaining \((Ne)^{-1/2}A^{1/4}\Theta^{3/4}\). If this C is below 1, use the direct sieve bound \((Ne)^{-1}\Theta\): it is at most \(A^{1/4}\Theta^{3/4}\), separately for \(A\ge\Theta\) and \(A<\Theta\). If C exceeds \(D_e^{1/3}\), use the full short sum, whose non-BK part is at most \(AD\), and the cutoff inequality implies \(AD\le A^{1/4}\Theta^{3/4}\). Divisor Minkowski therefore gives
\[
 \sum_b|P_b|^2\ll (BDKF)^\epsilon\bigl(BK+A^{1/4}\Theta^{3/4}\bigr).\tag{3}
\]
The large-e cutoff and empty bounded endpoint scales are treated as in the earlier physical ledger.

Alone, (3) does **not** improve the reviewed stratified p=6 slice: maximizing its four Θ faces on the small-divisor core yields \(b\le631/700\) at exponent \(21/20\), and \(b\le204251321/218750000\) at exponent \(19949123/18750000\). At the p=6 bottleneck, however, the scale-wise tail from (2) is smaller, so combining it with the existing Hölder bound before the Abel integral can improve the partial slice. A complete continuous-core certificate for that combination is not asserted here.

**Independent review.** High_match and Other_families independently checked the h³n collapse, all zero masks, the q-sum and both cutoff endpoint cases; Other_families also checked the standalone exact scalar thresholds. The source/profile identification and the unproved scale-wise mixture retain the qualifications above.
