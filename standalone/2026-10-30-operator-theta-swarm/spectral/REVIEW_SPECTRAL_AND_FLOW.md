# Independent review of moving-anchor covariance and boundary transport

Reviewer: the theta-structure agent, independently of the spectral and transport authors.

Verdict: **the three spectral theorems and the finite transport identities pass this mathematical review at their stated scopes**. The manuscript correctly leaves the source-specific cofinal positivity/boundary-budget estimate open. No RH proof or smaller zero-free half-plane is established by these components or by the replay scripts.

## Reviewed immutable byte identities

| File | SHA-256 |
|---|---|
| `work_spectral/MOVING_ANCHOR_THEOREM.md` | `d0ef707b0155db0427edfde869f5ff6522192ed304d4bd997d17b4282088d82d` |
| `work_spectral/verify_spectral.py` | `5f982b18b9864bb648d0e8baceb51fd1217c5633ce1c81f6cc3cab335af36c19` |
| `work_root/ANCHOR_FLOW.md` | `a102e9fad7b496913abcf92b4651b07e7fcbc34ffa97c67474f58bcdb17ac09e` |
| `work_root/verify_anchor_flow.py` | `68acb088fc9d6672ce250818d77352c7d6eab28ebab574a406030b68097ee77c` |

These identities refer to the source files read in full in the parent task's scratch workspace. Renaming or copying them for publication does not alter their identities. Later changes need a new scoped review.

## 1. Moving-anchor theorem

I independently checked the following load-bearing steps.

- The coefficients of `C_a=2a*f(s_a(z))` make `T_N=Re C_a(S)` with the stated factor of two. The generalized-Li second-difference identity follows by multiplying the derivative of the logarithmic expansion by `(1-z)^2`.
- A positive finite Toeplitz matrix supplies a positive trigonometric measure and a Herglotz function matching all coefficients through degree N. Singular matrices are allowed; strict positive definiteness is unnecessary.
- The inverse Cayley map transfers that matching to Taylor order N at the real anchor `sigma_a=1/2+a`. No assertion of holomorphy of the actual `f` on the entire critical half-plane is made at this step.
- On the independently safe half-plane `Re(s)>1`, the classical real-part partial-fraction formula makes `f` positive real. Thus both Cayley transforms are bounded by one, their difference divided by two is bounded by one, and the repeated Schwarz lemma gives exactly the displayed exponent `N+1` and ratio `(s-sigma_a)/(s+sigma_a-2)`.
- At any fixed real `s_0>1`, its logarithm is `-2(s_0-1)/a+O(a^-2)` as a grows. Bounded-anchor subsequences also work. Consequently `N/a→∞`, without a logarithmic correction, is sufficient for convergence on the safe half-plane.
- A normal-family limit on `Re(s)>1/2` agrees with the safe Cayley transform. Its value at one safe point lies strictly inside the disk, so the maximum principle excludes a unit-modulus constant and permits inversion of the Cayley transform throughout the domain.
- The identity `xi'=f_tilde*xi` then extends analytically. A hypothetical zero of multiplicity m would give orders `m-1` and at least m on the two sides. This is the correct source-preserving exclusion step; the proof does not assume that a logarithmic derivative is globally holomorphic before establishing it.

No gap was found in this implication. Its imported classical inputs are the actual-xi real-part partial-fraction formula, finite trigonometric moments/Herglotz representation, Schwarz's lemma, and normal families. I checked their use and normalization; I did not independently reprove the classical xi product or every source theorem.

## 2. Unconditional large-anchor positivity

The main Toeplitz coefficient at distance n is
`a*(1+(-1)^(n+1)*q^n)/(2n)>0`. Twice the sum of these coefficients is bounded by `a*(H_N+1)`. This validates the elementary lower bound in equation (6), including its use for every `a>=100(N+1)`.

The complex Binet estimate is valid: for `Re(w)>0`, both factors `w+it` and `w-it` have modulus at least `Re(w)`, and `2*integral t/(exp(2*pi*t)-1) dt=1/12`. With `w=s/2` this gives exactly `1/(3x^2)` for the shifted digamma expression. The remainder estimate uses a deliberately loose `3/(2x)` bound; it remains valid even though combining the rational terms would sharpen it. At `x>50`, its rational majorant is below `1/19`.

For `r=N/(N+1)`, the source is analytic and uniformly bounded on the required closed disk because its image lies in `Re(s)>50`. The diagonal similarity turns `E(S)` into `E(rS)` with condition number `r^-N<e<3`. The Hardy-space compression/contraction calculus bound applies to `E(rz)`, analytic on a neighborhood of the unit disk. Taking the Hermitian part therefore incurs less than `6a/19` in operator norm, and
`a*(1/2-6/19)=7a/38>a/6` proves the claimed margin.

This proof does not use the sampled numerical eigenvalues as a premise. I found no missing infinite-prime tail: the theorem bounds the full Mangoldt series by the displayed elementary convergent sum in the safe half-plane.

## 3. Laguerre realization and completeness threshold

The upper-shift convention yields
`B=aI+2a*sum_{k>=1}S^k` and `Re B=a*1*1^*`. Differentiating `U_t^*U_t` gives the exact rank-one dissipation identity. Since the only eigenvalue of B is the positive number a, its semigroup tends to zero, even though B is nonnormal. This proves the observation map is an isometry.

Summing the generalized-Laguerre coefficients of the semigroup gives the ordinary Laguerre function `sqrt(2a)*exp(-au)*L_j(2au)`, with no missing scalar. The semigroup relation then yields the stated right-translation-of-the-argument identity and the common prime autocorrelation.

For `h_b=sqrt(2b)*exp(-bu)`, direct integration against the polynomial Laguerre expansion gives the displayed geometric coefficient. Its squared finite sum is exactly `1-| (a-b)/(a+b) |^(2(N+1))`, hence equation (16) is an equality. The span of the real exponentials is dense, and projection norms are at most one, which completes the forward strong-convergence argument.

For the converse, selecting `b=1/2` avoids the accidental zero in the projection error for every allowed `a>=1`. The bound `2*artanh(1/(2a))<=2/a` gives a fixed positive error on any subsequence with bounded `N/a`. Thus the iff threshold is correct. The manuscript appropriately distinguishes test-space completeness from source-specific uniqueness and does not pass an unbounded form through bare strong L2 convergence.

## 4. Anchor transport

I independently differentiated the Cayley map and compared coefficients. The constant coefficient is `a*g_0'=g_1`, while the n=1 equation has no `g_0` term. The finite tridiagonal matrix is skew-symmetric. Entrywise multiplication of `K^*G+GK` reproduces the coefficient derivative except for the two missing next-basis contributions at the final row and column. Their sum is exactly the displayed rank-at-most-two B, including both contributions at the final diagonal corner.

The Laguerre dilation formula was independently derived from its two elementary recurrences. In the rotating frame `U G U^*`, the internal commutator cancels, leaving precisely `U B U^*`. For decreasing anchor, integration goes backward, so the **positive** part of B is the potential loss. Equations (7)–(8) use the correct sign. The reviewed header has the corresponding corrected wording.

The eigenvalue derivative for a simple eigenvalue follows from the vanishing expectation of the internal commutator. For multiple eigenvalues, the first derivatives are the eigenvalues of the restriction of B to that eigenspace. The two boundary eigenvalues are `(N+1)/2*(g_1 ± ||r||)`; they have opposite signs whenever a non-final coordinate of r is nonzero. Thus positive trace cannot be substituted for positive semidefiniteness.

## 5. Replays actually performed

I read both scripts, then ran the original anchor-flow checker into my own review directory. It passed all 96 exact-rational matrix cases, maximum dimension 25, including the full matrix identity, trace, shared-corner mutation rejection, and rank-two spectral invariants.

I also copied the unchanged spectral script into my own directory to avoid modifying the author's output and ran it with the primary Python runtime. It passed:

- 80 exact generating-coefficient checks and 80 exact observation-coefficient checks;
- 45 exact projection-error checks, 12 exact rank-one dissipation checks, and 4 exact scalar margins;
- the ordinary floating-point safe-line Cauchy, eigenvalue, semigroup and synthetic-zero diagnostics reported by the script.

Review outputs are `FLOW_REVIEW_REPLAY.json` and `SPECTRAL_CHECKS.json` in the reviewer's work directory. The spectral floating-point results are not directed enclosures; their finite source truncation stays in `Re(s)>50` and is not promoted into a global claim. These reruns reproduce the authors' finite programs; the independent portion of this review is the mathematical reconstruction described above, not an independently implemented numerical backend.

## 6. First remaining mathematical gap

The first missing RH-bearing statement is the actual source estimate in the cofinal regime: either a nonnegative innovation/Schur-complement formula as `N/a→∞`, or the positive-part transported boundary budget in equation (8) small enough to carry the unconditional large-anchor margin down to that regime. Neither finite contractivity of each prime operator nor the low-rank shape of the boundary matrix supplies that estimate. Summing independent prime operator norm bounds is invalid at exponent 1/2, exactly as the manuscript states.

I found no earlier proof gap in the reviewed components. These results give a precise scale, an unconditional regime, and exact transport. They remain a research platform with a named open estimate, not a completed route to RH.
