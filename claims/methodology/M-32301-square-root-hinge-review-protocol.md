# M-32301 — Review protocol for the square-root hinge route

Claim ID: `M-32301`  
Status: **FAIL-CLOSED REVIEW / RESEARCH PROTOCOL**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32301`--`L-32303`, `R-32301`, `R-32302`, `T-32301`

## 1. Review the exact finite algebra first

Verify independently:

1. the average carry formula `beta_(nq)`;
2. triangular invertibility and the adjoint formula `L-32303.9`;
3. the square-root hinge decomposition imported from PR #295;
4. SHARP-to-nonnegative-flow reconstruction;
5. the complete target superposition;
6. the carry/binomial and square-screw/Landau normalizations used downstream.

A later proof of SHARP cannot repair an error in these arrows retroactively.

## 2. Replay the directed checker

`X-32301` must be replayed without binary floating point.  Check that every radical enclosure is justified by integer squares and that interval signs are propagated according to the sign of each Möbius coefficient.

The finite nomination is deliberately sparse in endpoint space.  It is evidence for theorem discovery, not a substitute for a cofinal proof.

## 3. Mandatory mutations

A proposed proof of SHARP must survive the following conceptual mutations.

### Mutation A — generic BV

`R-32301` gives an exact endpoint-nine vector for which the natural weighted adjacent variation increases.  Reject any proof which silently uses a universal BV contraction.

### Mutation B — fixed third Abel

`R-32302` gives

```text
T=1000, n=11,
a_T(n)=-156358/55
```

for the quadratic-prefix target.  Reject a proof which derives SHARP from a source-blind fixed third-cumulative positivity theorem.

### Mutation C — logarithmic inverse

Do not assume positivity of the original logarithmic triangular inverse.  The hinge decomposition is used specifically so that SHARP is a smaller theorem.

### Mutation D — finite extrapolation

A finite directed certificate, however large, is not SHARP.

## 4. Preferred proof attacks

The proof itself should target one of the following exact objects.

1. **Adjoint numerator:** prove for the hinge state
   \[
   (j+1)[j u_j-(j-2)u_{j+1}]
   +2\sum_{m=j+2}^{T}u_m\ge0.
   \]
2. **Dual carry cone:** prove
   \[
   \sum_{q=2}^{T}b_q(q^{-1/2}-T^{-1/2})\ge0
   \]
   for every finite coefficient vector satisfying all carry-row inequalities in `L-32301.6`.
3. **Explicit flow:** construct the nonnegative average-row coefficients by a source-specific recursion, coupling, or positive integral representation.
4. **Fractional/Stieltjes positivity:** exploit the exponent `1/2` itself.  The fixed integer-Abel mutation proves that generic smoothing is insufficient.

A reviewer is not being asked to prove any of these.  They are research interfaces for the authoring agent.

## 5. Exact status boundary

```text
finite carry/dual algebra                    reviewable now
finite directed SHARP nominations            reviewable now
SHARP all endpoints                          not supplied
RH                                            unproved
```

Do not label the branch a proof of RH until a symbolic all-endpoint proof of SHARP has been committed and reviewed.
