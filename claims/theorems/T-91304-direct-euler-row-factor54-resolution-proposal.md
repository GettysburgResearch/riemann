# T-91304 — The corrected direct Euler residual row would close the factor-54 resolution proposal

Claim ID: `T-91304`  
Status: **CORRECTED PROPOSED COMPLETE RH COMPOSITION — INDEPENDENT ADVERSARIAL REVIEW REQUIRED**  
Created: 2026-08-13  
Corrected: 2026-08-13 after exact counterexample `R-91310`  
Depends on: conditional consumer `T-91302`; finite producer `L-91110/L-91114/L-91115` and corrected terminal packet; terminal projection `L-91342`; least-prime substochastic typing `L-91336/L-91337`; direct splice `L-91346/L-91351`; physical score repair `L-91352`; finite Hall proof `L-91345/L-91350`; mandatory firewalls `R-91102`, `R-91303`–`R-91310`  
RH status: **proposed, not accepted or independently verified**

## 1. Architecture and firewalls

The proof uses neither a positive inverse of the rough renewal nor a product of
one-prime completed state matrices. It does not feed the full parent source to
every prime branch and does not infer row typing from a scalar Hall residual.

The arithmetic source is decomposed by exact least rough prime. Every source
atom occurs in one branch. All current-generation rows are summed before the
single finite endpoint quantization.

A further firewall is now mandatory:

```text
declared source score is not automatically the literal entropy score
of the positive component row.
```

`R-91310` also forbids extending an active-threshold Hall prefix estimate to the
complete real endpoint corridor.

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
\tag{T-91304.1}
\]

No parent source, endpoint port or target column is copied across branches.
The child endpoint after the least-prime transition is

\[
 1\le y<83
\]

in the normalized reset coordinate.

## 4. Direct one-prime row splice

For a branch with least prime `p`, put `r=p^{-1/2}`. `L-91351` proves the exact
identities

\[
 \boxed{
 D_P(py)=rD_P(y)+D_{Pp}(py),
 }
\tag{T-91304.2}
\]

\[
 \boxed{
 \mathfrak T_P(py)
 =r\mathfrak T_P(y)+\mathfrak T_{Pp}(py),
 }
\tag{T-91304.3}
\]

\[
 \boxed{
 \mathfrak S_P(py)
 =r\mathfrak S_P(y)+\mathfrak S_{Pp}(py).
 }
\tag{T-91304.4}
\]

Here:

1. `D_(Pp)(py)` is the actual finite arithmetic residual row, not an abstract
   Hall source;
2. every inherited component of that row is nonnegative by `L-91346`;
3. every noninherited row remains in the current-generation frontier and must be
   realized in the same exact row normalization;
4. the residual target and residual source score are separately positive.

The former assertion

\[
 \mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)>0
\]

is false. `R-91310` gives the exact counterexample `(p,y)=(83,1)`. It is not used
in this corrected composition.

## 5. Literal component-row entropy

Let

\[
 \mathcal E_{P,p}(py)
 =\sum_{j\ge2}D_{Pp}(py;j)G_j
\tag{T-91304.5}
\]

be the entropy actually represented by the exact residual component row.
`L-91352` proves the positive von Mangoldt convolution

\[
 \mathcal E_P(x)
 =\sum_{ab\le x,(a,P)=1}
  \frac{\Lambda(b)}{\sqrt{ab}}
  \log\frac{x}{ab}
\tag{T-91304.6}
\]

and, using the formally verified explicit bound `psi(x)>=0.9x` for `x>=41`,
proves uniformly for `p>=83`, `1<=y<83` that

\[
 \boxed{
 \mathcal E_{P,p}(py)>rac43\sqrt{py}.
 }
\tag{T-91304.7}
\]

Positive Euler monotonicity and the fully active `P_30` block give

\[
 \boxed{
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
 }
\tag{T-91304.8}
\]

Therefore the correct favorable-loss statement is physical and strictly
stronger than the refuted scalar sentence:

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}>0.
 }
\tag{T-91304.9}
\]

This conclusion is available only after the inherited rows and all frontier
rows are realized exactly as the row in (T-91304.5). An unrelated positive
packing with the same scalar target does not suffice.

## 6. Terminal child

The child endpoint satisfies `y<83`. `L-91342` gives one positive terminal
source/row representation that is target exact and score superordinate. Scaling
it by

\[
 r\le83^{-1/2}<1
\]

preserves those properties.

Consequently every least-prime branch has the corrected form

```text
one positive terminal child, coefficient r<1;
one exact current arithmetic residual row;
positive residual target;
literal residual-row entropy strictly larger than residual target.
```

No completed two-state cascade is formed.

## 7. Physical capacity and one-use assembly

The row identity in (T-91304.2) is exact before carry evaluation. Applying the
nonnegative ordinary and radix-four response maps gives the target split in
every physical column, provided the frontier realization is the same exact row
used in (T-91304.5). All branches are summed in the parent row coordinate before
the single quantizer and safety factor are applied.

Because the least-prime source partition is disjoint, the same physical target
and the same finite collar are each charged once.

## 8. Score recurrence

Let `mathfrak L_X` be the endpoint-score loss of the conditional consumer. The
current arithmetic residual is favorable by the physical inequality
(T-91304.9), not by its declared source score. The inherited terminal child
carries coefficient `r<1`; every local finite correction has bounded cost.
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
\tag{T-91304.10}
\]

with absolute constants `C,C_0`, provided the exact native loss is additive
under the declared row/capacity assembly.

There is no branchwise factor proportional to the number of rough primes. The
source partition and finite boundary packets are homogeneous, so all valid
branch charges sum inside the one constant `C`.

## 9. Iteration

Each child endpoint contracts beyond the factor-54 threshold; in the one-prime
coordinate the contraction is at least `83`. The depth is `O(log X)`.
Substochasticity prevents total branch mass from increasing. Iterating
(T-91304.10) yields

\[
 \boxed{
 \mathfrak L_X=O(\log X)=o(\log^2X).
 }
\tag{T-91304.11}
\]

The endpoint-score criterion in `T-91302` would then imply the Riemann
Hypothesis.

## 10. Review boundary

This remains a complete proof proposal, not an accepted proof. A hostile
reviewer must independently verify, at exact frozen commits:

1. the `L-91346` inherited-row certificate and its Green boundary estimates;
2. the exact component-entropy identity and the `L-91352` partial-summation
   normalization;
3. the imported formal Chebyshev bound used in `L-91352`;
4. the corrected `X-91127` Hall certificate;
5. the exact typing and realization of every frontier row `j>y` in
   (T-91304.2) and (T-91304.5);
6. least-prime substochastic source provenance;
7. one-use physical sum-before-quantize assembly;
8. additivity and sign normalization of the endpoint-score loss in `T-91302`.

Until those interfaces pass independent review, the status is:

```text
false scalar score-over-target surplus  REFUTED / NOT USED
physical residual-row entropy surplus   PROPOSED COMPLETE
finite producer                         PROPOSED CLOSED
P79 terminal child                      PROPOSED CLOSED
P79 one-prime residual row              PROPOSED CLOSED
substochastic recurrence                PROPOSED CLOSED CONDITIONALLY
Riemann Hypothesis                      PROPOSED / REVIEW REQUIRED
```
