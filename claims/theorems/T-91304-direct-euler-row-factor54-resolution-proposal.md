# T-91304 — A source-faithful frontier assembly would close the corrected direct-Euler factor-54 route

Claim ID: `T-91304`  
Status: **CORRECTED CONDITIONAL COMPOSITION — UNPROVEN / EXPLICIT GAP**  
Created: 2026-08-13  
Corrected: 2026-08-13 after `R-91310`, `L-91352/L-91353`, and the causal Hall repair `L-91354`  
Frozen main under review: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Depends on: exact Euler identities `L-91351`; inherited-row theorem `L-91346`; physical score repairs `L-91352/L-91353`; corrected causal Hall theorem `L-91354`; terminal projection, finite producer and loss consumer only at their exact source commits; mandatory firewalls `R-91102`, `R-91303`–`R-91310`, `R-91552`, and the surviving exact findings of review PR `#431`  
RH status: **unproved**

## 1. Corrected architecture

The route uses neither a positive inverse of the rough renewal nor a product of
one-prime completed state matrices.  It does not feed the full parent source to
every prime branch and does not infer row typing from a scalar Hall residual.

The arithmetic source is decomposed by exact least rough prime.  Every source
atom must occur in one branch.  All current-generation rows must be summed in
the parent coordinate before the single finite endpoint quantization.

Two score firewalls are mandatory:

```text
declared source score is not the literal entropy of the component row;
an active Hall-threshold prefix estimate cannot be extended to every real endpoint.
```

The first is `R-91552`; the second is the exact first-cell counterexample
`R-91310`.

## 2. Proof-residency boundary

At the frozen main SHA, the present file is resident but several ancestors named
by the historical composition are not resident under their cited paths,
including the finite producer packets `L-91110/L-91114/L-91115` and the
conditional consumer `T-91302`.

Therefore this theorem cannot inherit those statements by an unqualified path
reference.  Every future promotion must supply an exact path-plus-SHA manifest
or consolidate the proof-bearing ancestors into one immutable proposal branch.

The statements below are consequently split into:

```text
resident exact arithmetic identities;
resident exact/directed raw-row score and Hall theorems;
source-pinned conditional finite producer and loss consumer;
one explicit source-faithful frontier theorem still to be proved.
```

## 3. Exact direct one-prime row splice

Let

\[
 P=P_{79},
 \qquad p\ge83,
 \qquad1\le y<83,
 \qquad r=p^{-1/2}.
\]

`L-91351` proves the exact identities

\[
 \boxed{
 D_P(py)=rD_P(y)+D_{Pp}(py),
 }
 \tag{T-91304.1}
\]

\[
 \boxed{
 \mathfrak T_P(py)
 =r\mathfrak T_P(y)+\mathfrak T_{Pp}(py),
 }
 \tag{T-91304.2}
\]

\[
 \boxed{
 \mathfrak S_P(py)
 =r\mathfrak S_P(y)+\mathfrak S_{Pp}(py).
 }
 \tag{T-91304.3}
\]

Here `D_(Pp)(py)` is the actual finite arithmetic residual row.  The inherited
coordinates `2<=j<=y` are strictly positive under the exact/directed theorem
`L-91346`.  The noninherited coordinates `j>y` remain current-generation
frontier rows.

The former claim

\[
 \mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)>0
\]

is false.  At `(p,y)=(83,1)`, `R-91310` proves the opposite sign exactly.  No
corrected composition may use that scalar inequality.

## 4. Literal residual-row entropy

Let

\[
 \mathcal E_{P,p}(py)
 =\sum_{j\ge2}D_{Pp}(py;j)G_j
 \tag{T-91304.4}
\]

be the entropy actually represented by the exact residual component row.
`L-91352` proves the coefficientwise positive formula

\[
 \mathcal E_P(x)
 =\sum_{ab\le x,(a,P)=1}
  \frac{\Lambda(b)}{\sqrt{ab}}
  \log\frac{x}{ab}
 \tag{T-91304.5}
\]

and the uniform physical inequalities

\[
 \boxed{
 \mathcal E_{P,p}(py)>rac43\sqrt{py},
 }
 \tag{T-91304.6}
\]

\[
 \boxed{
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
 }
 \tag{T-91304.7}
\]

Consequently

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}>0.
 }
 \tag{T-91304.8}
\]

The independent theorem `L-91353/X-91311` avoids the imported Chebyshev bound
and proves the second raw-row certificate

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)>\frac{86}{9},
 \qquad
 \mathcal E_{P,p}(py)-\mathfrak S_{Pp}(py)>\frac{86}{9}.
 }
 \tag{T-91304.9}
\]

Thus the arithmetic score interface is repaired at the exact **raw-row** level.
This does not yet identify the score of a later packed, collared or quantized
object with (T-91304.4).

## 5. Correct causal low-prefix Hall gate

Review PR `#431` correctly observed that the historical display `L-91350.2`
dropped the parent support cutoff.  When

\[
 t\le py<t+8,
\]

formal positive sources above `py` were incorrectly inserted into the parent
capacity.

`L-91354/X-91312` restores both causal cutoffs and evaluates the left and right
states at every parent and child activation.  It proves, for every prime
`p>=83`, every real `1<=y<83`, and every active sign-demand threshold
`t<4096`,

\[
 \boxed{
 \mathcal H_{4,t}^{(8)}(p,y)>\frac74,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>\frac32.
 }
 \tag{T-91304.10}
\]

The directed replay contains `18,180,604` inequalities.  Its score minimum is
the left limit at

\[
 t=79,
 \qquad p=83,
 \qquad y=85/83,
\]

immediately before the formerly omitted parent capacity at `py=85` activates.

This closes the scalar causal Hall inequalities.  It does not export a
source-labelled flow or establish the row-provenance packet required below.

## 6. Exact remaining theorem

The first open conclusion-producing statement is the following.

> **Source-faithful finite-frontier entropy preservation (`SFFEP`).**  For every
> least-prime branch `(p,y)` in the declared reset corridor, assemble the exact
> row identity (T-91304.1) with the terminal child, every noninherited frontier
> coordinate, the finite mismatch correction, collar, common endpoint port,
> ordinary response and radix-four detail response so that:
>
> 1. the output is coefficientwise nonnegative in every exact row coordinate;
> 2. every integer physical capacity is respected;
> 3. target is represented exactly once;
> 4. the represented score is at least
>    \[
>    \mathcal E_{P,p}(py)-C_0\theta_{p,y},
>    \]
>    where `C_0` is absolute and `theta_(p,y)` is the branch's actual normalized
>    target coefficient;
> 5. the branch coefficients are scalar, nonnegative and sum to at most one;
> 6. the common collar and endpoint port are charged only after all branches are
>    summed.

The theorem must use the actual restricted branch packets.  A pointwise source
partition does not automatically produce scalar coefficients for an unrelated
worst-case signed loss functional.  Likewise, the coefficient `r=p^-1/2` in the
exact child term cannot disappear from the recurrence.

The cross-stack observation `O-91312` reduces this further to a constructive
**Live Row-Provenance Theorem (`LRPT`)**: export one causal Hall flow from the
margins (T-91304.10), retain the exact row bonuses and child coefficient, and
prove that the resulting scalar target weights are a subprobability vector.

## 7. Why `SFFEP` would yield the recurrence

Assume the source-pinned finite producer and loss consumer are valid at their
exact normalizations, and assume `SFFEP`.

The raw-row surplus (T-91304.8) pays the current arithmetic target.  The terminal
child has endpoint below the fixed reset scale and is carried with its exact
coefficient.  Homogeneity and the scalar subprobability condition in `SFFEP`
then give

\[
 \boxed{
 \mathfrak L_X
 \le
 C+
 \sum_b\omega_b\mathfrak L_{X_b},
 \qquad
 \omega_b\ge0,
 \qquad
 \sum_b\omega_b\le1,
 \qquad
 X_b\le c_0X+C_1,
 }
 \tag{T-91304.11}
\]

for absolute constants `C,C_1` and fixed `c_0<1`.

Expanding the subprobability tree gives

\[
 \mathfrak L_X=O(\log X)=o(\log^2X).
 \tag{T-91304.12}
\]

The source-pinned endpoint-score consumer would then imply RH.  This is a
conditional implication only; `SFFEP/LRPT` is not proved here.

## 8. Hostile-review findings still active

One finding of PR `#431` is now repaired:

```text
parent causal support missing from L-91350.2   CLOSED / L-91354
```

The remaining joints are:

```text
a hidden hazard score is not automatically the score of an r-scaled canonical child;
pointwise source fractions are not automatically scalar signed-loss weights;
noninherited frontier rows are not covered by L-91346;
the live source-labelled Hall flow and row bonuses have not been exported as one packet.
```

The raw-row entropy theorem and causal Hall theorem supply the correct score and
capacity budgets.  They do not silently discharge these typing and assembly
obligations.

## 9. Verification retained on this branch

```text
X-91130  exact first-cell refutation and imported-psi physical repair;
X-91310  independent first-cell target/entropy enclosure;
X-91311  4,194,304-state and all-real-cell elementary entropy proof;
X-91312  18,180,604-inequality causal Hall certificate;
X-91125  independently replayed inherited-row certificate, source-pinned.
```

No replay certifies `SFFEP/LRPT`, the complete finite producer, the branch-loss
homogeneity interface or the final loss-to-RH consumer.

## 10. Status boundary

```text
exact Euler row/target/source-score identities      PROVED
strict scalar source-score surplus                  FALSE / R-91310
literal raw-row entropy surplus                     PROVED / TWO ROUTES
inherited rows 2<=j<=y                              PROVED EXACT/DIRECTED AT SOURCE
true causal low-prefix Hall theorem                 PROVED / L-91354
source-labelled Hall flow export                    OPEN
noninherited frontier realization                   OPEN
source-faithful entropy-preserving assembly          OPEN / SFFEP-LRPT
scalar substochastic loss recurrence                 CONDITIONAL ON SFFEP-LRPT
Riemann Hypothesis                                  UNPROVEN
```
