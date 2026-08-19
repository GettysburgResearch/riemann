# T-99210 — Endpoint-nested common-parent component-row RH candidate

Claim ID: `T-99210`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-19  
RH status: **not established by publication**

## 1. Frozen inputs

The candidate uses only the following conclusion-facing inputs:

```text
PR #620 @ 493e12fcba3f9b98dda7c3595bff73b256e00ca4
    compact factor-67 Hall and normalized component-row monotonicity;
    residual-only causal physical-row identity;
    exact equality endpoint-frame identity;

main / T-96000 stack at the same tree
    L-96000 fixed-row reciprocal-zeta Mellin transform;
    L-96001 row-kernel noncancellation;
    Landau one-sign theorem.
```

It does **not** use the score, all-column, radix-four capacity, prime-square,
or safe-point calibration parts of T-99020. `L-99213` corrects the finite
literal-score normalization before the theorem is stated.

## 2. Exact source theorem

For real `X>=1` and integer `j>=2`, put

\[
 c_X(j)=\sum_{n\le X/j}
        \frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\tag{T-99210.1}
\]

The frozen equality endpoint-frame identity writes the complete labelled row
`c_X` as the positive endpoint integral of compact signed `P_61` fibres,
including the exact anchored boundary block.

`L-99210` proves that every unnormalized canonical packet coordinate is
endpoint-nested. Thus each smaller-endpoint rough child is a literal
restriction of one positive vector-valued endpoint source.

`L-99211` partitions each positive compact Hall source interval into:

```text
matched current-only Hall source;
positive residual source.
```

The matched source produces the coefficientwise nonnegative row difference.
Only the residual recurses. One random-key coordinate partitions that
residual endpoint source into the exact factor-67 children and the exact causal
current. Since

\[
 \sum_i\alpha_i<67^{-1/2}<1/8,
\]

the child cylinders are disjoint. Repeating the construction gives a finite
one-owner product source because every child endpoint satisfies

\[
 Y'\le Y/67+1.
\]

Every observation on that source is a nonnegative physical component row.
Direct integration therefore gives

\[
 \boxed{c_X(j)\ge0\qquad(X\ge1,\ j\ge2).}
\tag{T-99210.2}
\]

This is the sole arithmetic producer used below.

## 3. Direct fixed-row Mellin consumer

For one fixed `j`, `L-96000` gives initially for `Re(s)>1/2`

\[
 \boxed{
 \mathcal C_j(s)
 :=\int_1^\infty c_X(j)X^{-s-1}\,dX
 =\frac{C_j}{s^2}
  +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
 }
\tag{T-99210.3}
\]

The right side meromorphically continues to `Re(s)>0` and is analytic at every
positive real `s`. Since `c_X(j)>=0`, Landau's theorem forces the defining
Mellin integral to converge throughout `Re(s)>0`.

Suppose `zeta(rho)=0` with `Re(rho)>1/2`. `L-96001` supplies a fixed sufficiently
large row `j` for which

\[
 P_j(\rho)\ne0.
\]

Then (T-99210.3) has a genuine pole at

\[
 s=\rho-1/2,
 \qquad \Re s>0,
\]

contradicting holomorphy of the defining nonnegative Mellin integral. Hence
zeta has no zero to the right of the critical line. The functional equation
excludes zeros to the left, giving the proposed conclusion

\[
 \boxed{\mathrm{RH}.}
\]

## 4. What the eureka removes

```text
native score normalization                    not used
4sqrt(X) equality-score shortcut              refuted / L-99213
ordinary and radix-four capacity              not used
finite/continuum all-column discrepancy       not used
safe-point logarithmic thinning               not used
proper-prime-power moat                        not used
samplewise integral Hall leaf                 not used
```

The route attacks one object only: positivity of every fixed component row.

## 5. Complete review graph

```text
exact endpoint-frame identity for c_X
 -> endpoint-nested complete canonical packet        L-99210
 -> literal fractional-Hall source partition         L-99211
 -> literal factor-67 random-key partition           L-99211
 -> finite positive source tree / direct integration L-99212
 -> c_X(j)>=0 for every X,j
 -> fixed-row Mellin transform                       L-96000
 -> noncancellation                                  L-96001
 -> Landau + functional equation
 -> RH candidate.
```

## 6. Scientific boundary

This is a complete proof candidate, not an accepted proof. The first
load-bearing reconstruction obligations are now sharply limited to:

1. the exact finite equality endpoint-frame identity whose output is `c_X`;
2. compact Hall feasibility and normalized component-row monotonicity;
3. same-index numerical child placement in the causal identity;
4. the fixed-row Mellin transform, large-`j` noncancellation, and Landau
   application.

No unnamed theorem is hidden between those arrows. Failure of any arrow
rejects the candidate while leaving the exact score correction and abstract
source lemmas valid at their stated scopes.

```text
common-parent source realization       PROPOSED COMPLETE
full component-row positivity          PROPOSED COMPLETE
fixed-row analytic consumer             PROPOSED COMPLETE / REVIEW
accepted proof of RH                    NO
Riemann Hypothesis                      UNPROVED PENDING REVIEW
```
