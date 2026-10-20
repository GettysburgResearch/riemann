# Independent review of the quadratic/sextic absorption pair

Date: 2026-10-20. Reviewer: Type-I subagent, independently of its author.

Reviewed file: ../mixed/QUADRATIC_PAIR_ABSORPTION.md.
SHA256: 1d14351a92904ef438e9dfcd8e0090ee2181c3c8a97742e243dd5ee628b02a86.

**Verdict:** no outstanding issue found in the stated deduction from the
source cusp reflection, cubic large sieve and exact divisor identity.
This reviews the written deduction, not every upstream source theorem.

The primitive transform sends \(\eta_j=\xi_S\chi_S^j\) to
\(\overline{\eta_j\chi_S}=\xi_S\chi_S^{-j-1}\). Thus the pair is
exactly \(j=0,2\), with both characters primitive by their coprime
quadratic and cubic orders. The two Gauss factors at \(S\) contribute
\(H\), and the moving modulus contributes \(H^{-2s}\), giving the
claimed \(H^{1-2s}\). There is no missing square root or conductor.

The four ramified profiles remain sufficient. The quadratic character
is one at \(\omega\); its value at \(-1\) is only a common scalar in
the exceptional minor. The three-step ramified ratio gains
\(\eta_j(\lambda)^3=\xi_S(\lambda)\), a unit sign. The cube Euler
factor is therefore precisely the twisted one (Q2). All extracted
divisors divide \(r\), preserving coprimality with \(S\).

Squaring and summing the reflection gives (Q9), including
\(H^{4\delta}\). For the three terms in \(F_\delta\), partial summation
of the weight \((Nk)^{-2\delta}\) is legitimate because their row
powers are \(1,1/2-\delta,1-\delta\), all strictly larger than
\(2\delta\) when \(0<\delta<1/6\). It contributes
\(R^{-2\delta}F_\delta(R,H)\), up to a fixed constant.

The finite-cutoff supremum in Section 3 is finite with a height order
independent of the conductor cutoffs. With
\(Y=C_0R^{1/2+\theta}H(1+|t|)^2\), the relative remainder is bounded by
\(C C_0^{-4\delta}R^{\eta-4\delta\theta}\). Choosing
\(\eta<4\delta\theta\) and then \(C_0\) large makes this a contraction
for every \(R\ge1\). Hence no separate small-\(R\) argument introduces
an uncontrolled \(H\)-dependent constant. The original-sum losses can
be allocated within the final \((RH)^\epsilon\).

The reflected exponents in (Q5), both Type-I bounds (Q12)--(Q13),
and the normalized terminal exponents (Q14)--(Q15) were independently
recomputed. The conditional result explicitly requires the actual
quadratic-twisted angular Hecke reciprocal; a hypothesis only for the
untwisted character would not suffice. The comparison at \(U=KL\)
correctly shows that the bound \(K^2L^p\) remains above \(KL\) in the
adverse short-prime range. No improved numerical zero-free boundary
follows from this pointwise-conductor result.
