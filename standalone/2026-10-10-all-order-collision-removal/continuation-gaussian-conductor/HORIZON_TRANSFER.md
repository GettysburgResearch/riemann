# Gaussian row smoothing preserves the all-horizon exponent criterion

**Status:** proposed complete elementary adapter, plus an explicitly unproved arithmetic premise. This file does not claim a new zero-free half-plane.

## 1. The cutoff issue

The preceding packet uses the complete finite row set 0<Nu<=H. PROOF.md estimates a Gaussian row covariance. Signed individual covariance terms are not monotone under row majorization. We therefore compare the NONNEGATIVE FULL energies before splitting off any signed sector.

With the same fixed B_u(X), k, sigma, W and S as PROOF.md, define

    I_#(D;H)=integral_0^D X^(-2k sigma)
                     sum_(0<Nu<=H)|B_u(X)|^2 dX/X,
    I_G(D;H)=integral_0^D X^(-2k sigma)
                     sum_(u!=0)e^(-Nu/H)|B_u(X)|^2 dX/X.

Fix h>0 and lambda>=0. All row ranges remain fixed inside each integral.

### Proposition 1.1. Same exponent, two row cutoffs

The assertions

    for every epsilon>0, I_#(D;D^h)<<D^(h+lambda+epsilon),
    for every epsilon>0, I_G(D;D^h)<<D^(h+lambda+epsilon)

are equivalent, with constants allowed to depend on the fixed data, h, lambda and epsilon, never on D.

**Proof.** On Nu<=H, exp(-Nu/H)>=exp(-1), so I_#<=e I_G.

Conversely, Tonelli and e^(-x)=integral_x^infinity e^(-t)dt give the exact layer-cake identity

    I_G(D;H)=integral_0^infinity e^(-t) I_#(D;tH)dt.           (1.1)

For 0<t<=1, bound I_#(D;tD^h) by I_#(D;D^h). For t>=1, put D_t=t^(1/h)D. The row cutoff tD^h equals D_t^h, and the positive scale integral up to D is bounded by the one up to D_t. Therefore the assumed sharp estimate gives

    I_#(D;tD^h)<=I_#(D_t;D_t^h)
        << t^((h+lambda+epsilon)/h) D^(h+lambda+epsilon).

The exponentially weighted t integral converges. For D sufficiently large every D_t in the second range is above the common lower threshold. This proves the reverse implication. QED.

There is no appeal to a false inequality between signed sharp and Gaussian subfamilies. Nor is H=D^h replaced inside an integral by the moving cutoff X^h.

## 2. The resulting narrower sufficient condition

Use the predecessor's fixed smooth window W_*. Fix k>=2, delta in (0,1/2), h>0, and choose the fixed finite enlargement of S so that its nonidentity inverse-kernel mass q is less than one. PROOF.md holds for that same S.

For every horizon D, form the Gaussian signed remainder R_high(D;D^h) consisting of the exact product-column pairs with

    Q(r,s)>D^(h/(1-delta)),
    j(r)=j(s) modulo 6.

Suppose for every epsilon>0 and all sufficiently large D that

    R_high(D;D^h)<=C_epsilon D^(h+lambda+epsilon).             (2.1)

This is an UNPROVED ARITHMETIC HYPOTHESIS. By PROOF.md (6.2), it implies the Gaussian integrated estimate, hence by Proposition 1.1 the exact sharp-row premise of the predecessor. Its integrated kernel comparison, prime-removal identity and single-window Mellin argument then give

    L_K(s,nu)!=0 when Re(s)>alpha,
    alpha=1/2+delta+(lambda+5h/6)/(2k).                       (2.2)

The boundary is strict. Principal poles are allowed. No OpenAI quasi-RH theorem is needed for this logical implication, but the elementary proof components in the frozen predecessor are dependencies, not independently formalized inputs.

For every fixed nu, constants may depend on nu, k, h, delta and epsilon. A conclusion for all Hecke targets requires the arithmetic premise for each target. For zeta alone, the predecessor explains why the principal target over K suffices logically. A future analytic proof could still require auxiliary twists; they are not assumed available.

At arbitrarily small fixed delta, near-linear fixed h approaching one, and lambda=0, (2.2) has the limiting values 17/24 for k=2 and 23/36 for k=3. Those numbers remain CONDITIONAL. Cofinal orders with delta_k->0 and (lambda_k+h_k)/k->0 would give the critical-line conclusion. No uniform-in-k constants or height-effective shrinking band is obtained.

## 3. Boundary of this pass

The work proves an absolute upper bound for a growing, exactly defined covariance sector. It does not prove (2.1). Deleting the whole remaining conductor range with generic bounds is prevented by the length calculation PROOF.md (7.1).

The source-sensitive high-conductor signed estimate, not the fixed window, gcd zero mask, Gaussian cutoff or low-conductor range, is now the missing statement in this particular formulation.
