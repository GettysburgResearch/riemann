# A weaker all-order target is sufficient

**Status:** proved conditional implications and explicit open analytic targets. No positive exponent saving in the genuine arithmetic moment is proved in this file.

## 1. Permit a moment defect and a different row length

Retain the exact Möbius/sextic source A_u(D;W), with a fixed finite bad-prime set S, a fixed finite-order character nu, and every original row. Fix k>=1, h>0 and lambda>=0. Suppose that for every epsilon>0,

\[
 \sum_{0<Nu\le D^h}|A_u(D;W)|^{2k}
 \ll_{k,h,\lambda,\nu,S,W,\epsilon}
 D^{h+k+\lambda+\epsilon}.
\tag{1.1}
\]

The extra exponent lambda is the defect from the ideal diagonal-size moment. The estimate need not be optimal.

### Theorem 1.1. Defect-aware extraction

For every eta>0,

\[
 A_1(D;W)\ll D^{\alpha+\eta},\qquad
 \alpha=\frac12+\frac{\lambda+5h/6}{2k}.
\tag{1.2}
\]

This extends the exact prime-removal deduction of PR #910 by retaining a moment defect and allowing every fixed h>0. The source does not change when a prime is removed.

**Proof.** Put Y=D^(h/6) and let P(D) be the prime ideals outside S with Y/2<Np<=Y. The fixed-field prime ideal theorem gives J=|P(D)| asymptotic to a positive constant times Y/log Y. Only a fixed field and a fixed finite exclusion are used; no uniform theorem for a changing conductor is assumed.

Write

    T_p(x)=A_{p^6}(x;W).

With the exact zero extension, T_p is the sum defining A_1 with p-multiples omitted. Squarefreeness gives

\[
 A_1(x)=T_p(x)-\nu(p)T_p(x/Np),
 \qquad
 T_p(x)=\sum_{j\ge0}\nu(p)^j A_1(x/(Np)^j).
\tag{1.3}
\]

The second identity terminates at every x because the smooth test has compact support. Consequently

\[
 A_1(D)=\frac1J\sum_{p\in P(D)}T_p(D)
 -\frac1J\sum_{p\in P(D)}\sum_{j\ge1}\nu(p)^j A_1(D/(Np)^j).
\tag{1.4}
\]

Each prime sixth power is a distinct retained row of norm at most D^h. Hölder and (1.1) bound the first term by

\[
 \left(J^{-1}\sum_p|T_p(D)|^{2k}\right)^{1/(2k)}
 \ll D^{(k+\lambda+5h/6+\epsilon)/(2k)}(\log D)^{1/(2k)}.
\tag{1.5}
\]

Fix beta>alpha, reduce epsilon, and absorb the logarithm. This is O(D^(beta-delta)) for some delta>0. Inductively assume |A_1(x)|<=C x^beta for smaller dyadic scales above its fixed lower support threshold. All arguments on the second line of (1.4) are at most 2D/Y<D/2 once D is large. Their total is at most

\[
 \frac C J\sum_p\sum_{j\ge1}(D/(Np)^j)^\beta
 \ll_\beta C D^\beta Y^{-\beta}.
\tag{1.6}
\]

Choose the starting scale so that this is at most C D^beta/2, and then choose C to cover the bounded initial range and (1.5). This closes induction. When h>=6, some or all smaller arguments are already below the support threshold; nothing in the proof requires h<6. All constants refer to the same fixed nu,S,W, not to the moving p. Taking beta=alpha+eta proves the claim. QED.

The prime ideal theorem is the only distribution-of-primes input here. It is a classical theorem and is also explicitly used by the pinned source. The present packet does not independently reprove it.

## 2. From the cancellation exponent to nonvanishing

Assume (1.1) for every smooth compactly supported W needed below, with constants allowed to depend on W. For Re(s)>1, ordinary absolute convergence gives

\[
 \int_0^\infty A_1(D;W)D^{-s}\frac{dD}{D}
 =\frac{\widetilde W(s)}{L_K^S(s,\nu)},
 \quad
 \widetilde W(s)=\int_0^\infty W(y)y^s\frac{dy}{y}.
\tag{2.1}
\]

The sum A_1(D;W) is zero for sufficiently small D. The bound (1.2) therefore makes the integral in (2.1) holomorphic in Re(s)>alpha, using eta smaller than the distance of any given compact set from that boundary. This is local uniform convergence of the integral for a fixed W.

If L_K^S had a zero rho with Re(rho)>alpha, choose a smooth bump W supported sufficiently close to 1 that its Mellin transform at rho is nonzero. For example, make the phase of y^rho vary by less than pi/3 throughout the support and use a nonnegative nonzero bump. Then the quotient on the right of (2.1) has a pole at rho, whereas the left gives a holomorphic continuation there. This is impossible.

Thus (1.1), with the stated test coverage, gives a zero-free half-plane Re(s)>alpha. There is no assertion about the boundary line. A principal pole of L at 1 is allowed; its reciprocal has a zero, not a pole. Finitely deleted Euler factors are nonzero in Re(s)>0.

This argument does not require an implied constant uniform across all smooth tests, across all characters, or across k. It does require the actual estimate for the particular test chosen after the hypothetical zero is fixed. A computation for one cutoff does not supply that coverage.

## 3. What strength is actually necessary?

At h=1+theta for arbitrarily small fixed theta>0, the limiting exponent is

\[
 \beta_{k,\lambda}=\frac12+\frac5{12k}+\frac{\lambda}{2k}.
\tag{3.1}
\]

| Moment | Defect lambda | Limiting conditional boundary |
|---|---:|---:|
| Fourth | 0 | 17/24 |
| Fourth | 1/2 | 5/6 |
| Fourth | 2/3 | 7/8 |
| Sixth | 0 | 23/36 |
| Sixth | 1 | 29/36 |
| General 2k | lambda_k | 1/2+5/(12k)+lambda_k/(2k) |

The equalities at theta=0 mean limiting half-planes obtained by allowing arbitrary positive fixed theta and epsilon; no endpoint moment theorem at theta=0 is being assumed or asserted.

In particular, a fourth moment with **any fixed lambda<2/3** already gives a numerical boundary below 7/8. The optimal lambda=0 target is not the only useful milestone. A lambda=1/2 theorem would give 5/6, despite losing D^(1/2) relative to the ideal fourth moment.

At H near D, combining an inverse second moment with only the trivial |A_u|<=C D yields a fourth moment of order H D^3, corresponding to lambda=1. This is an illustrative consequence of that imported second moment, not an unconditional result independently reverified here. Moving from this crude fourth-moment bound to lambda<2/3 requires more than D^(1/3) saving; reaching lambda=0 requires a full D saving. This helps set a less brittle first analytic target.

## 4. An unbounded sequence with sublinear loss suffices for RH

### Theorem 4.1. Weak hierarchy criterion

Suppose the exact moment statement (1.1) holds for an unbounded sequence k_j, with fixed parameters h_j>0 and lambda_j>=0 at each order, for each target character and each needed smooth test. Assume

\[
 \frac{\lambda_j+5h_j/6}{k_j}\longrightarrow0.
\tag{4.1}
\]

Then the finite-order Hecke family over K has no nontrivial zeros to the right of 1/2. The standard quadratic norm factorization transfers this to every Dirichlet L-function, and the functional equations give their critical-line conclusions, including RH for zeta.

**Proof.** If one target had a zero with real part beta>1/2, select a finite j with (lambda_j+5h_j/6)/(2k_j)<beta-1/2. Apply Theorem 1.1 and Section 2 at that fixed order with a remaining exponent loss smaller than the strict gap. This excludes the zero. The fixed set S may depend on j, since every finite deletion preserves zeros in Re(s)>0. Constants may depend arbitrarily on the selected j. Quadratic base change gives, away from harmless fixed Euler factors,

    L_K(s,chi composed with N)=L(s,chi)L(s,chi chi_{-3}).

Away from the principal pole, a zero of either factor would be a zero of the product. Principal poles occur only at s=1, which has no Dirichlet zero by the classical nonvanishing theorem. The functional equation reflects any remaining nontrivial zero left of 1/2 to one right of 1/2 in the dual character. QED.

Thus optimal D^(k+epsilon) moments for every k are stronger than logically necessary. Bounded h_j and lambda_j=o(k_j), for example lambda_j=sqrt(k_j), suffice if their required arithmetic estimates can actually be established. Even h_j may grow sublinearly in k_j. Nothing here proves one such new sequence.

This is a global all-scale criterion. It is not a theorem about a band that narrows only at large heights, and it leaves no bounded-height exception once all its hypotheses are met.

## 5. The new fixed-source analytic target

Apply Theorem 5.2 in PROOF.md with H=D^h. It is enough to establish

\[
 \mathfrak C_k(D,D^h)\ll D^{\lambda+\epsilon},
\tag{5.1}
\]

where C_k is the fixed-S, complete-row, rectangular collision-free energy defined there. The logarithmic transfer loss is absorbed by reducing epsilon. Equations (5.1) and (1.2) make the quantitative consequences explicit.

The revised next targets are therefore:

1. For k=2, prove a rectangle estimate with lambda<2/3 before demanding lambda=0.
2. For k=3, develop the same fixed-S theorem rather than introducing a separate hierarchy of uncontrolled moving-prime masks.
3. For an unbounded sequence of orders, seek lambda_k=o(k) and h_k=o(k), not necessarily perfect diagonal size.

The missing estimate must exploit the actual sextic-row arithmetic. All algebraic collisions and their exact zero masks are already handled by the positive kernel. The kernel neither proves average independence nor justifies using an arbitrary-coefficient sieve outside its length range.

## 6. Attempted shortcuts and why they do not close the argument

**Discarding overlaps.** This loses cancellation before taking the norm. The exact forward kernel replaces it, with a proved logarithmic cost.

**Hiding the excluded primes in an implied constant.** This destroys moving-parameter uniformity. The direct fixed-S reconstruction removes the exclusion; the independent adapter in PROOF.md Section 7 also bounds its cost explicitly.

**Using only the balanced c=1 estimate.** The new reconstruction shortens coordinates separately. Rectangular test coverage is necessary and has not been inferred from an equal-scale theorem.

**Treating the whole product as arbitrary coefficients of length D^k.** This loses the factor-scale structure and pays the long-polynomial cost. The new theorem preserves the structured coefficient, but it does not supply the required cancellation at H near D.

**Using sixth-root multiplicativity as independence.** The synthetic Liouville phase model in PROOF.md violates the desired moments while satisfying that algebra. Any closure needs genuinely arithmetic information beyond the identities established here.

**Calling a positive diagonal count a moment theorem.** The off-diagonal contribution is precisely what remains. The exact computations in this packet test finite identities, not an infinite mean-square bound.
