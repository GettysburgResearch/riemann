# Direct Euler factor-54 score audit and physical-entropy repair

Date: 2026-08-13  
Reviewed main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Review branch: `review/gpt56-pro/91304-direct-row-score-audit`  
Verdict: **one advertised scalar surplus is exactly false; two independent physical component-entropy arguments repair the raw-row score interface; the finite-frontier assembly and loss recurrence remain unproved; RH remains unproved**

## Executive finding

The direct-row proposal correctly identified an exact Euler row split, but
`L-91351` then used an invalid extension of a Hall-threshold prefix bound.  At

```text
p=83,
y=1,
x=83,
```

the exact coefficient of `sqrt(83)` in residual declared score minus residual
target is negative.  Thus the sentence “the current arithmetic residual has
source score larger than target” is false.

This does not refute the direct-row architecture.  It reveals that the proof was
using the wrong score.  The native loss is governed by the literal entropy of
the exact component row, not by its declared source-score label.

## Exact counterexample

For `P=P_79`,

\[
 A_P(83)
 =-
 \frac{1401629533229069216211617003}
 {107254825578022430263302818471}.
\]

Hence

\[
 A_P(83)-\frac1{83}A_P(1)
 =-
 \frac{223590076836035175208867029720}
 {8902150522975861711854133933093}<0.
\]

The active-demand threshold theorem in `L-91345` cannot be promoted to every
real endpoint `x>=83`.  This exact counterexample is retained in `R-91310` and
replayed independently by both `X-91130` and `X-91310`.

## Primary physical repair

Let

\[
 \mathcal E_P(x)=\sum_jD_P(x;j)G_j
\]

be the actual component-row entropy.  Exact Möbius convolution gives

\[
 \mathcal E_P(x)
 =\sum_{ab\le x,(a,P)=1}
  \frac{\Lambda(b)}{\sqrt{ab}}
  \log\frac{x}{ab},
\]

which is coefficientwise positive.

For the one-prime residual,

\[
 \mathcal E_{P,p}(py)
 =\mathcal E_P(py)-p^{-1/2}\mathcal E_P(y),
\]

every summand remains positive.  Keeping only `a=1` reduces the problem to the
von Mangoldt ramp

\[
 R(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
\]

The formally proved estimate `psi(x)>=0.9x` for `x>=41` yields a uniform
derivative moat.  It reduces the complete two-parameter corridor

```text
p>=83,
1<=y<83
```

to the single base point `(83,1)`.  Nine explicit prime-power terms certify

\[
 R(83)-\frac43\sqrt{83}>rac{41}{50}.
\]

Therefore

\[
 \mathcal E_{P,p}(py)>rac43\sqrt{py}.
\]

Meanwhile positive Euler monotonicity and the fully active `P_30` block give

\[
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
\]

Thus the exact raw row has the explicit physical target margin

\[
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}.
\]

This is `L-91352/X-91130`.

## Independent elementary confirmation

`L-91353/X-91311` proves the same raw-row sign without the imported Chebyshev
bound.  It combines:

```text
all 4,194,304 P_79 activation states;
all real endpoint cells 83<=x<=10,000;
an elementary central-binomial lower bound for psi;
a trivial prime-power upper bound for psi-theta;
a compact child-corridor bound.
```

The certificate proves

\[
 \mathcal E_P(x)-\mathfrak T_P(x)>18,
 \qquad
 \mathcal E_P(x)-\mathfrak S_P(x)>18
 \qquad(x\ge83),
\]

and

\[
 \mathcal E_P(y)-\mathfrak T_P(y)<76,
 \qquad
 \mathcal E_P(y)-\mathfrak S_P(y)<76
 \qquad(1\le y<83).
\]

Since `p^(-1/2)<1/9`, this yields the independent residual moat

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)>\frac{86}{9},
 \qquad
 \mathcal E_{P,p}(py)-\mathfrak S_{Pp}(py)>\frac{86}{9}.
 }
\]

The independent certificate returns

```text
PASS_P79_LITERAL_ENTROPY_DOMINATION
```

and records the exact finite extrema and analytic tail constants.

## What the repair does and does not establish

The arithmetic score joint is now repaired at the raw-row level:

```text
exact Euler residual row
  -> literal component entropy
  -> entropy strictly exceeds target and declared score.
```

It does **not** follow merely from this that a later positive packing, collar or
quantizer realizes the same entropy.  The exact remaining theorem is the
source-faithful finite-frontier entropy-preservation statement `SFFEP` isolated
in the corrected `T-91304`.

`SFFEP` must simultaneously provide:

1. exact nonnegative realization of every noninherited row `j>y`;
2. ordinary and radix-four capacity feasibility at every integer column;
3. target exactness with no duplication;
4. literal entropy loss bounded by one absolute homogeneous debt;
5. actual scalar branch weights summing to at most one;
6. one-use collar and endpoint-port accounting after branch summation.

## Proof-residency and independent-review boundary

The frozen main tree contains the final direct-row composition but not several
ancestors named under their historical paths, including the finite producer
packets and `T-91302`.  A future proof claim must consolidate these ancestors or
supply an exact path-plus-SHA manifest.

The independent review PR `#431` also retains four live obstructions:

```text
L-91350.2 omits a parent causal support cutoff;
hidden hazard score is not automatically the score of an r-scaled child;
pointwise source fractions are not automatically signed-loss weights;
noninherited frontier rows are not covered by L-91346.
```

The raw entropy theorem supplies a strong positive budget for attacking these
joints.  It does not silently discharge them.

## Replay

```bash
cd experiments/X-91130-direct-euler-score-interface
python3 verify.py
sha256sum -c SHA256SUMS

cd ../X-91310-p79-first-cell-score-gap
python3 verify.py

cd ../X-91311-p79-literal-entropy-domination
python3 verify.py
```

Retained results:

```text
PASS_DIRECT_EULER_SCORE_INTERFACE_AUDIT_AND_REPAIR
PASS_P79_FIRST_CELL_SCORE_REFUTATION_AND_ENTROPY_REPAIR
PASS_P79_LITERAL_ENTROPY_DOMINATION
```

## Final boundary

```text
false real-prefix scalar surplus                 REFUTED EXACTLY
literal direct-row entropy                       COMPUTED EXACTLY
positive von Mangoldt convolution                PROVED EXACTLY
uniform raw-row physical score moat              PROVED BY TWO ROUTES
finite-frontier entropy preservation             OPEN / SFFEP
scalar branch-loss homogeneity                   OPEN
full factor-54 recurrence                        UNPROVEN / EXPLICIT GAP
Riemann Hypothesis                               UNPROVEN
```
