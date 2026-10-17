# Fourth moments and the selected detector: independent interface audit

Read the complete relevant proofs at #965 d58e3282a9379b6ae165681bc2e21e4f9fd18c26,
#966 8d94494698ee447711a53dec922986586418e398, and #968
14f544fb4293ffb59942ff8d345ab9d6da67025c. Their exact source commits are recorded in LATEST_REVIEW.md. This pass checked the primary DF and BGL
interfaces; it does not certify the entire CT reflection construction or
the resulting proposed all-field boundaries.

## The suspected row/column mismatch is absent

Fresh primary source: https://arxiv.org/html/2610.04045v1 . Definition (1.2)
uses n-th-power-free ideals for BOTH indices of Theta_n, explicitly
distinguished from squarefree ideals in Xi_n. Theorem 1.1 gives exactly
K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6) for n=6. Section 2.3 specifies
the fixed generator choices and original zeros on nonunits. Section 2.5
gives primitive conductor c_a a^star, with c_a dividing a fixed ideal.
For sixth-free a, a^star=rad(a). These facts support the stated complete
AFE and the full-norm-indexed moment application.

The identity chi_a(c d^6)=chi_a(c)1_((a,d)=1), with c sixth-free, is exact.
The factors c and d may share primes. Fixing d before the row norm and
retaining the mask by positivity is legitimate. The coefficient l2 mass
contributes (Nd)^(-6+epsilon), so the root masses sum absolutely over d.
No extra powerful-row count or squarefree-column substitution is needed.
The complete AFE separation still requires its stated smooth weights,
both dual sums, conductor factors, and fixed local types; the written
arguments retain them. No fatal flaw was found in this component.

Fresh BGL source: https://arxiv.org/pdf/1112.1650 , Section 5, (5.1) and
(5.3)--(5.5), including the full pre-Cauchy detector and complete columns.
DF Section 9 explicitly applies that detector to the flat family. Keeping
the exceptional-row indicator before the first mean supports #966's
selected Holder step; the shared ordinate supremum remains outside the
positive sum. This is a count of exceptional characters, without silently
equating it to a sharper total-zero count.

## Mixed higher-moment consequence and its limits

For fixed positive integers r,k, the same complete-column argument proves
moments U^(kappa_r+epsilon) for L^(2r), where

    kappa_r=max(1,r/2,5/6+r/6,1/3+5r/12),

and K(U,A^k) times an arbitrarily small power for the central mollifier's
2k-th moment. Put A=U^a, B=U^b, q=2sigma-1 and

    m_k(a)=max(1,ka,5/6+ka/3,1/3+5ka/6).

Holder on the selected set of size R, with the counting factor retained,
gives

    sum_E |L M_A|
      <= R^(1-1/(2r)-1/(2k))
         U^(kappa_r/(2r)+m_k(a)/(2k)+epsilon)

up to fixed polynomial height factors. Solving the detector inequality
therefore contributes the first exponent

    [k kappa_r+r m_k(a)-rk q b]/(r+k).

The other detector exponents remain

    (1-q)b, 1-q a,
    1/3+(5/6-q)v, 5/6+(1/3-q)v,  v in {a,b}.

This is a component deduction, not a new estimate for inverse-L moments.
The separate exploratory calculations were floating-point only and are
not part of this packet's replay. Across their
tested active middle range, higher mollifier moments and direct LM
powering did not improve #966's L^4/M_A^2 selection. This finite numerical
observation is not a universal optimality theorem. At sigma=3/4 the
optimized direct LM second-moment estimate gives 13/18, worse than 43/60.

There is a genuine but small high-sigma opportunity: choosing r=4,k=1 at
sigma=24/25, a=2050/1163 and b=2625/1163 gives g=210/1163. Each displayed
exponent is at most g, with the first expression, (1-q)b and the
v=a instance of 1/3+(5/6-q)v equal to g. It improves the analogous
fourth-moment choice 643/3528, but changes no active middle-class
bottleneck of the current Dedekind composition. This was recorded rather
than promoted as progress toward the critical line.
