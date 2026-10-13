# Growing-prime freezing and an exact one-sided moment flux

Status: PROPOSED reviewable mathematics with complete elementary proofs. This proves a hierarchy for a partially deterministic, partially random family, not for the full native family. The final one-sided flux bound is an unproved target. No zero-free exponent is improved.

Scope: every fixed k, the full physical row set, literal zero masks, and all supported squarefree ideal columns. A synthetic arbitrary-coefficient lower example is explicitly separate from the native Möbius coefficients.

Dependencies: ideal counting; elementary sign hypercontractivity (proved in the companion note); the classical Chebyshev upper bound for primes. Only the sharpness example in Section 3 additionally uses the classical prime ideal theorem. The starting arithmetic family and moment-to-zero interface are inherited from PRs #912/#926/#930, not independently re-proved here.

## 1. The deformation

Fix K=Q(sqrt(-3)), a finite bad set S, the native phases xi_u(n)=nu(n) chi_n(u), and a smooth compact test W supported in [alpha,beta] with alpha>0. For D>=2 take X=max(2,beta D). Every relevant prime ideal has norm at most X. A moving column exclusion q is implemented literally by zeroing the corresponding local phases.

For a set B of prime ideals with Np<=X, define independent signs by

    e_p=-1 deterministically for p in B,
    e_p uniform in {-1,+1} otherwise.

Define

    P_(u,B)(D) = sum_n mu_K(n)^2 xi_u(n) W(Nn/D) e(n),
    F_(k,B)(D,H) = sum_u w_H(u) E |P_(u,B)(D)|^(2k),             (1.1)

where w_H>=0 and sum_u w_H(u)<=H. Masks can alternatively be written as (n,qS)=1 in every sum. No row, including a sixth-power row, is discarded.

If B contains all relevant primes, e(n)=mu_K(n) on squarefree n and (1.1) is exactly the original M_(2k). For smaller B, all prime signs in B agree with the actual Möbius signs; only the remaining prime signs are randomized. In contrast to a_p=(Np)^(-t), this deformation does not simply shift the L-function argument.

## 2. Unconditional diagonal size with a growing frozen range

For a frozen set B define

    E_B(X) = sum_(d squarefree, Nd<=X, p|d => p in B) (Nd)^(-1/2),
    Lambda_B(X) = sum_(p in B, Np<=X) (Np)^(-1/2).

### Theorem 2.1

For every fixed k>=1 and epsilon>0, uniformly in B, in arbitrary deterministic |b(n)|<=1 supported on Nn<=X, and in all deterministic local phases of modulus at most one,

    ||sum_n mu_K(n)^2 xi(n) b(n) e(n)||_(2k)
          <<_(K,k,epsilon) X^(1/2+epsilon) E_B(X)
          <= C X^(1/2+epsilon) exp(Lambda_B(X)).                 (2.1)

Consequently, after rescaling epsilon and absorbing a fixed ||W||_infinity,

    F_(k,B)(D,H)
        << H X^(k+epsilon) exp(2k Lambda_B(X)).                  (2.2)

The constants do not depend on B, the row, the exclusion, or the row height; this pointwise-in-row randomization theorem requires no native pointwise cancellation premise.

Proof. Uniquely write each squarefree ideal n=d r, where every prime of d lies in B and no prime of r lies in B. The polynomial is

    sum_(d supported on B) mu_K(d) xi(d)
      sum_(r squarefree, (r, product_B p)=1, Nr<=X/Nd)
          xi(r) b(d r) e(r).

The inner polynomial has uniform independent prime signs. The uniform-sign version of Lemma 2.1 in the companion note gives its squared L^(2k) norm at most

    sum_(Nr<=X/Nd) (2k-1)^omega(r) |xi(r)b(d r)|^2
           <<_(K,k,epsilon) (X/Nd)^(1+2epsilon),

using ideal counting and the fixed divisor bound. Scales between 1 and 2 are harmless. Minkowski, with no assertion of independence between different d, gives the first inequality of (2.1), because (Nd)^(-1/2-epsilon)<=(Nd)^(-1/2). Removing the norm restriction from the nonnegative squarefree sum gives the Euler product product_(p in B)(1+(Np)^(-1/2))<=exp(Lambda_B). Raise to 2k and sum the nonnegative row weights. QED.

### Corollary 2.2: freeze through (log X)^2

Take B={p: Np<=Y(X)}. If

    sqrt(Y)/log(2Y) = o(log X),                                 (2.3)

then for every fixed k and epsilon>0,

    F_(k,B)(D,H) <<_(K,k,W,epsilon) H D^(k+epsilon).              (2.4)

For an arbitrary fixed function Y satisfying (2.3), the lower cutoff for D may depend on that function as well as k and epsilon; there is no uniform rate over all little-o functions. In particular, (2.4) holds with the displayed constants for Y=(log X)^2. More generally it holds for Y=(log X)^2 (log log X)^(2-delta), for every fixed delta>0 and all sufficiently large X (with delta-dependent constants). The number of frozen primes now grows with D; they are not hidden in a fixed excluded set.

Proof of the prime budget. Prime ideals in this quadratic field have norms p or p^2, with at most two above a rational prime. The classical Chebyshev inequality pi(x)<<x/log x therefore gives pi_K(Y)<<Y/log Y. Partial summation gives Lambda_B<<sqrt(Y)/log(2Y). For Y=(log X)^2 this is O(log X/log log X)=o(log X), and (2.2) proves (2.4). Chebyshev itself follows by bounding the product of primes in (n,2n] by binom(2n,n)<=4^n and summing dyadically. No prime ideal theorem, RH, or imported 7/8 premise is needed for this upper bound. QED.

Thus there is an unconditional growing-prime entry point for the entire hierarchy. It is not the endpoint B={all p<=X}.

## 3. Why an arbitrary-coefficient extension past log-power 2 fails

This is a coefficient-class example, not a counterexample to the native moment conjecture.

### Proposition 3.1

For every fixed A>2 and Y=(log X)^A, there are deterministic arrays b_X(n), |b_X(n)|<=1, supported on squarefree ideals of norm at most X, for which the partially frozen polynomial with xi=1 has, for every realization,

    |sum_n mu_K(n)^2 b_X(n)e(n)|
                >= X^(1-1/A-o(1)).                             (3.1)

Hence no diagonal-size bound for all such arrays can hold in that frozen range.

Proof. By the prime ideal theorem there are m asymp Y/log Y good prime ideals with norm in [Y/2,Y]. Set r=floor(log X/log Y), which tends to infinity and satisfies m/r -> infinity. Consider products of r distinct such primes. Unique ideal factorization makes them distinct, and every product has norm at most Y^r<=X. Their number is

    binom(m,r) >= (m/r)^r = X^(1-1/A-o(1)).

To see the last exponent, log(m/r)=(A-1)log log X+O(1), while r=log X/(A log log X)+O(1). Set b_X(n)=mu_K(n) on these products and zero elsewhere. Every one of their primes is frozen, so b_X(n)e(n)=1. This proves (3.1). The norm lower bound (Y/2)^r=X^(1-o(1)) also shows that the mass lies near the top in exponent, but no fixed annular-test counterexample is claimed. QED.

The example deliberately changes the coefficient class. It does not assert that the true signed smooth Möbius sum violates (2.4) for A>2. It shows precisely where an extension must use arithmetic rather than a universal norm estimate. The log-power-2 scale also appears in the different, completely multiplicative initial-bias sign-change problem of Angelo--Xu; their theorem is not used to infer this proposition or any native sextic estimate.

## 4. Exact prime-by-prime return to the native moment

Order the relevant good prime ideals p_1,...,p_J by nondecreasing norm, resolving equal norms with any fixed tie-break. Let F_j denote (1.1) with the first j signs fixed to -1. Let j_0 include every prime with Np<=(log X)^2. Corollary 2.2 bounds F_(j_0) at diagonal size.

For the step that freezes p_j, fix all earlier signs to -1 and leave all later signs uniform. For any fixed later-sign realization, uniquely split the polynomial as

    P = U_(u,j) + e_(p_j) V_(u,j).                              (4.1)

U is the sum over columns not divisible by p_j. The exact cofactor polynomial in V is

    V_(u,j) = xi_u(p_j)
       sum_(m squarefree, (m,p_j q S)=1)
         xi_u(m) W(Nm/(D/Np_j)) e(m).                           (4.2)

Earlier factors of m retain their fixed minus signs and later factors retain their random signs. If p_j divides the row, V is zero. Equation (4.2) retains the moving exclusion and the same physical row range. In particular V is not replaced by an arbitrary independent array.

Put A_j=|U|^2+|V|^2 and B_j=2 Re(U conjugate(V)). These real quantities depend on the row and later signs. Define

    Delta_(k,j) = -sum_u w_H(u) E_later
           sum_(ell<=k, ell odd) binom(k,ell) A_j^(k-ell) B_j^ell.
                                                                    (4.3)

### Theorem 4.1: exact signed flux identity

    F_j-F_(j-1) = Delta_(k,j),
    M_(2k)(D,H) = F_(j_0) + sum_(j>j_0) Delta_(k,j).            (4.4)

Proof. Before freezing, the conditional moment is (|U+V|^(2k)+|U-V|^(2k))/2. Afterwards it is |U-V|^(2k). Their difference is ((A_j-B_j)^k-(A_j+B_j)^k)/2, which is exactly the odd-binomial sum (4.3). Average over later signs and rows, then telescope. This is a finite identity. It introduces no boundary, contour, norm-extension, or Jensen return loss. QED.

### The explicit fourth-moment target

For k=2 define

    J_4 = sum_(j>j_0) sum_u w_H(u) E_later
           Re(U_(u,j) conjugate(V_(u,j))) (|U_(u,j)|^2+|V_(u,j)|^2).

Then

    M_4(D,H) = F_(j_0) - 4 J_4.                                (4.5)

Therefore the ONE-SIDED bound

    J_4 >= -C_epsilon H D^(2+epsilon)                           (TARGET-4)

would give the required diagonal fourth moment. The opposite inequality J_4<=F_(j_0)/4 already follows from M_4>=0; the missing information is precisely the lower bound. TARGET-4 IS NOT PROVED. It is equivalent at this scale to the fourth-moment upper bound up to the already proved diagonal F_(j_0). It is not a mathematically weaker assertion and is not offered as evidence that the moment conjecture is true.

In the repository's native H=D^(1+theta) regime, obtaining TARGET-4 at arbitrarily small fixed theta>0, with the required tests and twist coverage, would feed the existing extraction interface for the open half-plane Re(s)>17/24. That extraction is inherited, not re-proved or made unconditional by this note.

For higher orders the corresponding sufficient target is

    sum_(j>j_0) Delta_(k,j) << H D^(k+e_k+epsilon),
                   H=D^(h_k), h_k=o(k), e_k=o(k),              (TARGET-k)

along unbounded fixed orders, with the original detector and twist quantifiers. Every moment order is fixed before D grows. TARGET-k is also unproved.

## 5. The local flux has zero complete-residue mean

For the native sextic characters the flux in (4.3), before a physical norm cutoff is imposed on the rows, has exactly zero mean over a complete residue system modulo the product of relevant primes. To see this, use CRT to change only the row component modulo p_j by a unit v with chi_(p_j)(v)=-1. The good-prime sextic character has order six, so such a unit exists. U is unchanged, V changes to -V, and every term in the odd-binomial sum changes sign. Zero row residues stay zero and contribute V=0. The residue permutation therefore pairs opposite contributions.

This is a finite complete-residue statement, compatible with the cubic-fiber symmetry in PR #930; it is not new short-row equidistribution. The actual sharp norm ball is not invariant under that CRT permutation. Establishing TARGET-4 requires a bound on the resulting incomplete-row signed correlations, not an appeal to complete-residue cancellation.

One must not replace (4.3) by a sum of absolute values, assume that each Delta is nonpositive, or declare the two polynomials independent. The exact checker exhibits both signs in actual sextic-character test polynomials. Those test columns use only the specified five prime ideals, not all columns below the numerical norm cap, and are not an asymptotic experiment.

## 6. What this changes and what it does not

This pass supplies a uniformly controlled starting portion of deterministic Möbius primes, and an exact local observable for adding every remaining prime. Unlike power damping, the return does not automatically pay D^(2kt). Unlike a prime-only face, every cofactor polynomial retains its composite Möbius companions. Unlike a positive majorant, the target asks only for the adverse signed part of the TOTAL flux.

The final estimate is still the arithmetic problem. This note proves no cancellation estimate for the large-prime flux on the physical short row range. Any subsequent claimed advance must state how much of TARGET-4 or TARGET-k it actually bounds, rather than treating (4.4) itself as a moment theorem.
