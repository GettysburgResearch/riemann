# T-91304 — The direct Euler residual row closes the factor-54 resolution proposal

Claim ID: `T-91304`  
Status: **PROPOSED COMPLETE RH PROOF COMPOSITION — INDEPENDENT ADVERSARIAL REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: conditional consumer `T-91302`; finite producer `L-91110/L-91114/L-91115` and corrected terminal packet; terminal projection `L-91342`; least-prime substochastic typing `L-91336/L-91337`; direct splice `L-91346/L-91351`; finite Hall proof `L-91345/L-91350`; first-moment certificate `X-91128`; mandatory firewalls `R-91102`, `R-91303`–`R-91309`  
RH status: **proposed, not accepted or independently verified**

## 1. Architecture and firewalls

The proof uses neither a positive inverse of the rough renewal nor a product of
one-prime completed state matrices.  It does not feed the full parent source to
every prime branch and does not infer row typing from a scalar Hall residual.

The arithmetic source is decomposed by exact least rough prime.  Every source
atom occurs in one branch.  All current-generation rows are summed before the
single finite endpoint quantization.

## 2. Current finite layer

For every sufficiently large endpoint `X`, the resident finite producer gives:

```text
nonnegative endpoint and component-row weights;
ordinary and radix-four feasibility on the outer factor-54 window;
the finite/continuum mismatch paid once;
the positive B-spline collar paid once;
the complete terminal annulus paid once;
absolute bounded score debt.
```

The false exact finite/Volterra seed identity remains excluded by `R-91102`.
The fractional terminal repair uses exact endpoint atoms rather than an
integer-column derivative at a real child column.

## 3. Exact least-prime decomposition

The positive four-state/hidden-hazard source construction assigns each
unprocessed squarefree source atom to its unique least rough prime `p>=83`.
The pointwise branch coefficients are nonnegative and substochastic:

\[
 \boxed{
 \sum_b\theta_b(n)\le1.
 }
\tag{T-91304.1
}

No parent source, endpoint port or target column is copied across branches.
The child endpoint after the least-prime transition is

\[
 1\le y<83
\]

in the normalized reset coordinate.

## 4. Direct one-prime row splice

For a branch with least prime `p`, put `r=p^{-1/2}`.  `L-91351` proves the exact
typed identities

\[
 \boxed{
 D_P(py)=rD_P(y)+D_{Pp}(py),
 }
\tag{T-91304.2
}

\[
 \boxed{
 \mathfrak T_P(py)
 =r\mathfrak T_P(y)+\mathfrak T_{Pp}(py),
 }
\tag{T-91304.3
}

\[
 \boxed{
 \mathfrak S_P(py)
 =r\mathfrak S_P(y)+\mathfrak S_{Pp}(py).
 }
\tag{T-91304.4
}

Here:

1. `D_(Pp)(py)` is the actual finite arithmetic residual row, not an abstract
   Hall source;
2. every inherited component of that row is nonnegative by `L-91346`;
3. every noninherited row remains in the already paid current-generation
   frontier;
4. the residual target is positive by the complete `P_79` Hall theorem;
5. the residual score is positive and satisfies
   \[
   \boxed{
   \mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)
   >\frac{58}{2075}\sqrt{py}.
   }
   \tag{T-91304.5
   }
   \]

Thus the current residual creates no positive signed score loss.

## 5. Terminal child

The child endpoint satisfies `y<83`.  `L-91342` gives one positive terminal
source/row representation that is target exact and score superordinate.  Scaling
it by

\[
 r\le83^{-1/2}<1
\]

preserves those properties.

Consequently every least-prime branch has the exact form

```text
one positive terminal child, coefficient r<1;
one positive current arithmetic residual row;
positive residual target;
residual score at least residual target.
```

No completed two-state cascade is formed.

## 6. Physical capacity and one-use assembly

The row identities in (T-91304.2) are exact before carry evaluation.  Applying
the nonnegative ordinary and radix-four response maps gives the exact target
split in every physical column.  All branches are summed in the parent row
coordinate before the single quantizer and safety factor are applied.

Because the least-prime source partition is disjoint, the same physical target
and the same finite collar are each charged once.

## 7. Score recurrence

Let `mathfrak L_X` be the endpoint-score loss of the conditional consumer.  The
current arithmetic residual is favorable by (T-91304.5); the inherited terminal
child carries coefficient `r<1`; every local finite correction has bounded cost.
Summing over the substochastic least-prime partition gives

\[
 \boxed{
 \mathfrak L_X
 \le
 \sum_b\theta_b\mathfrak L_{X_b}+C,
 \qquad
 \sum_b\theta_b\le1,
 \qquad
 X_b\le c_0X+C_0,
 }
\tag{T-91304.6
}

with absolute constants `C,C_0`.

There is no branchwise factor proportional to the number of rough primes.  The
source partition and finite boundary packets are homogeneous, so all branch
charges sum inside the one constant `C`.

## 8. Iteration

Each child endpoint contracts by more than the factor-54 threshold; in the
one-prime coordinate the contraction is at least `83`.  The depth is
`O(log X)`.  Substochasticity prevents total branch mass from increasing.
Iterating (T-91304.6) yields

\[
 \boxed{
 \mathfrak L_X=O(\log X)=o(\log^2X).
 }
\tag{T-91304.7
}

The endpoint-score criterion in `T-91302` then implies the Riemann Hypothesis.

## 9. Review boundary

This is a complete proof proposal, not an accepted proof.  A hostile reviewer
must independently verify, at exact frozen commits:

1. the `L-91346` inherited-row certificate and its Green boundary estimates;
2. the corrected `X-91127` Hall certificate;
3. the `P_79` first-moment prefix bounds in `X-91128`;
4. the exact typing of frontier rows versus inherited rows in (T-91304.2);
5. least-prime substochastic source provenance;
6. one-use physical sum-before-quantize assembly;
7. the sign and normalization of the endpoint-score consumer `T-91302`.

Until those interfaces pass independent review, the status is:

```text
finite producer                         PROPOSED CLOSED
P79 terminal child                      PROPOSED CLOSED
P79 one-prime residual row              PROPOSED CLOSED
residual target/score ledgers           PROPOSED CLOSED
substochastic recurrence                PROPOSED CLOSED
Riemann Hypothesis                      PROPOSED / REVIEW REQUIRED
```
