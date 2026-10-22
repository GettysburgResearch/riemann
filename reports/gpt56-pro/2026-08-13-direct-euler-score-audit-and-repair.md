# Direct Euler factor-54 score and causal-Hall audit

Date: 2026-08-13  
Reviewed main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Review branch: `review/gpt56-pro/91304-direct-row-score-audit`  
Verdict: **one advertised scalar surplus is exactly false; two independent physical component-entropy arguments repair the raw-row score interface; the noncausal finite Hall checker is superseded by an 18.18-million-inequality causal certificate; live flow provenance and the finite-frontier loss recurrence remain unproved; RH remains unproved**

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

A second independent review finding was also correct: the old low-prefix Hall
formula omitted the parent cutoff `d<=py`.  That sign gate has now been repaired
with the true causal kernel.

## Exact scalar counterexample

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

The active-demand threshold theorem cannot be promoted to every real endpoint
`x>=83`.  This exact counterexample is retained in `R-91310` and replayed
independently by both `X-91130` and `X-91310`.

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

## Independent elementary entropy confirmation

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

Since `p^(-1/2)<1/9`, this yields

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

## Exact causal Hall repair

The historical `L-91350.2` replaced the parent kernel by the complete formal
prefix through `t+8`.  When

\[
 t\le py<t+8,
\]

this inserted positive capacities at `e>py` that were absent from the causal
parent.

`L-91354/X-91312` restores the exact parent and child cutoffs.  For fixed `p`
and `t`, the true Hall margin is affine in `sqrt(y)` between child activations
`y=d` and parent activations `y=e/p`.  The replay evaluates both sides of every
activation.

Once `p>=max(83,t+8)`, the parent prefix is complete.  Exact reciprocal-prefix
positivity and exact child-margin positivity prove monotonicity in `p`, reducing
the infinite tail to one boundary per threshold.

The complete census is

```text
P_79 sign thresholds:                 385
finite prime plus tail cases:       91,090
child-margin directed checks:       78,540
causal Hall directed checks:    18,102,064
all directed inequalities:      18,180,604
```

It proves

\[
 \boxed{
 \mathcal H_{4,t}^{(8)}(p,y)>\frac74,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>\frac32.
 }
\]

The global score minimum occurs at

\[
 t=79,
 \qquad p=83,
 \qquad y\to(85/83)^-,
\]

immediately before the omitted parent capacity at `py=85` activates.  This is
precisely the real cell missed by the old formula.

Retained verdict:

```text
PASS_P79_CAUSAL_LOW_PREFIX_HALL
```

The old `L-91350/X-91127` claim is marked superseded rather than silently reused.

## What the repairs do and do not establish

Two arithmetic interfaces are now closed:

```text
exact Euler residual row
  -> literal component entropy
  -> entropy strictly exceeds target and declared score;

true causal target/score capacities
  -> strict finite Hall inequalities.
```

It does **not** follow merely from separate Hall feasibility that one common
source-labelled flow has the needed score, row bonuses and scalar branch
weights.  Nor does raw entropy automatically survive an arbitrary later collar
or quantizer.

The exact remaining theorem is the source-faithful frontier statement
`SFFEP/LRPT` isolated in `T-91304` and `O-91312`.  It must:

1. export one canonical target Hall flow from the causal capacities;
2. prove score superordination for that same flow;
3. prove every normalized component-row bonus for that same flow;
4. retain the literal child coefficient `p^(-1/2)`;
5. realize every noninherited row `j>y` and every target-null bonus;
6. respect ordinary and radix-four integer capacities;
7. produce actual scalar target weights summing to at most one;
8. charge collar and endpoint port once after branch summation.

## Proof-residency and independent-review boundary

The frozen main tree contains the final direct-row composition but not several
ancestors named under their historical paths, including the finite producer
packets and `T-91302`.  A future proof claim must consolidate these ancestors or
supply an exact path-plus-SHA manifest.

Of the four concrete objections in review PR `#431`, the causal Hall objection
is now closed.  Three remain:

```text
hidden hazard score is not automatically the score of an r-scaled child;
pointwise source fractions are not automatically signed-loss weights;
noninherited frontier rows are not covered by L-91346.
```

The entropy and Hall theorems supply strong positive budgets for attacking these
joints.  They do not silently discharge them.

## Replay

```bash
cd experiments/X-91130-direct-euler-score-interface
python3 verify.py
sha256sum -c SHA256SUMS

cd ../X-91310-p79-first-cell-score-gap
python3 verify.py

cd ../X-91311-p79-literal-entropy-domination
python3 verify.py

cd ../X-91312-p79-causal-low-prefix-hall
python3 verify.py
```

Retained results:

```text
PASS_DIRECT_EULER_SCORE_INTERFACE_AUDIT_AND_REPAIR
PASS_P79_FIRST_CELL_SCORE_REFUTATION_AND_ENTROPY_REPAIR
PASS_P79_LITERAL_ENTROPY_DOMINATION
PASS_P79_CAUSAL_LOW_PREFIX_HALL
```

## Final boundary

```text
false real-prefix scalar surplus                 REFUTED EXACTLY
literal direct-row entropy                       COMPUTED EXACTLY
uniform raw-row physical score moat              PROVED BY TWO ROUTES
old noncausal Hall formula                       SUPERSEDED
true causal finite Hall signs                    PROVED EXACT/DIRECTED
source-labelled Hall flow/row provenance         OPEN / LRPT
finite-frontier entropy preservation             OPEN / SFFEP
scalar branch-loss homogeneity                   OPEN
full factor-54 recurrence                        UNPROVEN / EXPLICIT GAP
Riemann Hypothesis                               UNPROVEN
```
