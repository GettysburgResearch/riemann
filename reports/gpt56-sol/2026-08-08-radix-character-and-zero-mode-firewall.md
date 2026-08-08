# Radix-character and eta zero-mode firewall

Agent: `gpt56-sol`  
Date: 2026-08-08  
Parent: PR #322 at `72d68a043a008209455375b720cd107a436e7f32`  
Status: **EXACT SCOPE CORRECTION + STRATEGIC PIVOT; RH UNPROVEN**

## 1. Why this pass was necessary

The latest repository state contains two attractive contraction stories:

```text
five-adic residue renewal -> fixed finite automaton K -> rho(K)<1;
dyadic eta core -> strict weighted-jet contraction.
```

Both are useful, but neither can be promoted to a complete RH proof without checking what happens to the actual zero modes.

This pass makes those modes explicit.

## 2. Five-adic residue space contains Dirichlet-L problems

For a character `chi mod 5`, define

```text
R_chi(X)=sum_(n<=X) mu(n)chi(n)n^(-1/2)log(X/n).
```

Then exactly

```text
Mellin[R_chi](z)=1/[z^2 L(z+1/2,chi)].
```

The four unit residues modulo five are Fourier-equivalent to the four characters of `(Z/5Z)^*`.

Therefore the proposed four-dimensional inner residue automaton on PR #322 contains:

```text
one principal zeta channel;
one quadratic Dirichlet-L channel;
two conjugate complex Dirichlet-L channels.
```

A fixed norm-equivalent contraction of the complete unit-residue state would yield subpower Riesz means for all four characters and hence GRH for all mod-five Dirichlet L-functions.

That is not a contradiction. It is a decisive scope correction: the nonzero residue modes are not harmless finite combinatorics.

## 3. Radix two is structurally unique

For a prime radix `p`, nonzero residue classes diagonalize by characters of `(Z/pZ)^*`.

Only `p=2` has a trivial unit group and no nonprincipal character.

Thus dyadic descent is the unique prime-radix decomposition which does not enlarge the source problem from zeta to additional Dirichlet L-functions.

This strongly favors a source-complete dyadic boundary theorem over the five-adic finite-state route unless the mod-five character channels are intentionally attacked as simultaneous GRH problems.

## 4. Eta contraction has a neutral zeta-zero mode

For the square-root eta comb of PR #317,

```text
beta_hat(xi)=1-eta(1/2+i xi).
```

At every critical zeta zero `rho=1/2+i gamma`,

```text
beta_hat(gamma)=1.
```

Hence no translation-invariant physical norm containing that oscillatory mode can make beta a strict contraction.

The geometric weighted-jet theorem on PR #317 is not false: its function class excludes high-frequency zeta modes. A mode `exp(i gamma t)` has geometric derivative norm proportional to

```text
sum_m (a |gamma|)^m,
```

which diverges once `a|gamma|>=1`.

Thus the strict eta contraction is a low-frequency analytic theorem. It cannot by itself prove the all-frequency RH statement.

## 5. Consequence for the current proof graph

The following should not be sent to reviewers as complete RH proofs:

```text
PR #304 terminal atomic closure                refuted by #310/#311/#315/#317;
PR #322 five-adic finite automaton              closing character channels open;
PR #317 eta contraction -> RH by itself         invalid scope jump;
PR #316 CBVR                                    still open.
```

The valid surviving exact inputs are substantial:

```text
complete central signed saturation;
first/two-pass unconditional carry packing;
all-depth fresh boundary native-debt estimates;
exact dyadic shift terminalization;
critical eta low-frequency weighted-jet reserve;
finite shell one-crossing;
Pascal-cycle normal form and Cycle-Debt duality;
parity difference from eta source to the original Möbius/zeta core.
```

## 6. Preferred research direction after this firewall

The next full attack should stay dyadic and retain the RH-bearing neutral mode rather than try to contract it away.

A successful theorem should couple:

```text
character-free dyadic scaling
+ exact parity difference cancelling artificial eta poles
+ native central/Pascal boundary flow
+ a source-specific one-sided or Hermitian observable for the neutral mode.
```

In particular, any strict contraction may be used only on the transverse analytic bank. The principal Möbius mode must remain explicit until a one-sided Landau sign theorem or a positive reflected normal form consumes it.

This is a stricter design requirement than CBVR and a cleaner one than five-adic `rho(K)<1`.

## 7. Exact replay

`X-32201-residue-character-firewall` verifies with integer/Gaussian-integer arithmetic:

```text
mod-five character orthogonality     16 rows;
Dirichlet inverse identities        1024 rows;
finite DFT inversion                   8 rows;
nonprincipal mod-two characters        0.
```

Retained digest:

```text
ab26ae2136aefbc2c6fc3cb2169850630aa8187d919c75c624b26e972c1f09a3
```

The exact regression proves finite algebra only.

## 8. Honest proof status

```text
mod-five character decomposition       PROPOSED COMPLETE EXACT
five-adic source-free automaton idea    SCOPE-CORRECTED / NOT CLOSED
eta zero-mode firewall                  PROPOSED COMPLETE EXACT
strict low-frequency eta contraction    RETAINED AT DECLARED SCOPE
dyadic source-complete closing theorem  OPEN
Riemann Hypothesis                      UNPROVEN
```

There is currently **no full RH proof on this branch suitable to hand to reviewers as a completed proof**. The useful reviewer-ready objects are the exact residue-character theorem and eta zero-mode firewall themselves.
