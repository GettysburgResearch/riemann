# L-91351 — The `P_79` one-prime splice is one terminal child plus an exact arithmetic residual row

Claim ID: `L-91351`  
Status: **CORRECTED EXACT SPLIT / RAW-ROW THEOREM — FRONTIER ASSEMBLY OPEN**  
Created: 2026-08-13  
Corrected: 2026-08-13 after `R-91310`, physical repairs `L-91352/L-91353`, and causal Hall repair `L-91354`  
Depends on: terminal theorem `L-91342`; one-prime source identities; inherited-row theorem `L-91346`; causal Hall certificate `L-91354`; physical entropy repairs `L-91352/L-91353`; exact frontier theorem `SFFEP/LRPT` still open  
RH status: **unproved**

## 1. Exact finite Euler rows

Put

\[
 P=P_{79}=\prod_{q\le79}q.
\]

For an endpoint `x` and row `j>=2`, define

\[
 \boxed{
 D_P(x;j)
 =\sum_{\substack{d\mid P\\d\le x/j}}
   \frac{\mu(d)}{\sqrt d}Q_{x/d}(j).
 }
\tag{L-91351.1}
\]

Let `p>=83`, `1<=y<83`, and put `r=p^{-1/2}`.  Adjoining the Euler factor `p`
gives the exact identity

\[
 \boxed{
 D_P(py;j)
 =rD_P(y;j)+D_{Pp}(py;j),
 }
\tag{L-91351.2}
\]

where

\[
 \boxed{
 D_{Pp}(py;j)
 =D_P(py;j)-rD_P(y;j).
 }
\tag{L-91351.3}
\]

No approximation or continuum replacement occurs.

## 2. Positive inherited residual row

`L-91346` proves by a Green-bulk/finite-boundary decomposition and a directed
finite certificate that

\[
 \boxed{
 D_{Pp}(py;j)>0
 \qquad
 (p\ge83,\ 1\le y<83,\ 2\le j\le y).
 }
\tag{L-91351.4}
\]

Thus every row inherited by the contracted child has the positive exact split

```text
parent inherited row
 = p^(-1/2) * terminal child row
   + positive current-generation arithmetic row.
```

Rows `j>y` have no child contribution.  They remain entirely in the current
generation.  `L-91346` does not certify their source typing or their physical
frontier realization.

## 3. Exact target and declared source-score identities

For `a>0`, define the finite scalar forcing

\[
 F_{a,P}(x)
 =\sum_{\substack{d\mid P\\d\le x}}
  \mu(d)
  \left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right).
\tag{L-91351.5}
\]

The SHARP target and declared endpoint source score are

\[
 \mathfrak T_P(x)=3F_{4/3,P}(x),
 \qquad
 \mathfrak S_P(x)=3F_{5/3,P}(x).
\tag{L-91351.6}
\]

The same Euler algebra gives

\[
 \boxed{
 \mathfrak T_P(py)
 =r\mathfrak T_P(y)+\mathfrak T_{Pp}(py),
 }
\tag{L-91351.7}
\]

\[
 \boxed{
 \mathfrak S_P(py)
 =r\mathfrak S_P(y)+\mathfrak S_{Pp}(py).
 }
\tag{L-91351.8}
\]

The true causal Hall theorem `L-91354` and the large-prefix theorem prove

\[
 \boxed{
 \mathfrak T_{Pp}(py)>0,
 \qquad
 \mathfrak S_{Pp}(py)>0.
 }
\tag{L-91351.9}
\]

For the finite gate `L-91354` retains the parent cutoff `d<=py` and certifies the
strict margins

\[
 \mathcal H_{4,t}^{(8)}(p,y)>\frac74,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>\frac32.
 \tag{L-91351.10}
\]

The historical `L-91350.2` formula and its `X-91127` certificate are superseded.

These target and score values are scalar ledgers of the same Euler residual.
They are not automatically the literal entropy score of its component row.

## 4. Exact correction to the first-moment claim

Let

\[
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d.
\]

The exact identity

\[
 \boxed{
 \mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)
 =\sqrt{py}\left[A_P(py)-\frac1pA_P(y)\right]
 }
\tag{L-91351.11}
\]

is valid.  The former conclusion that its right side is uniformly positive is
false.  `R-91310` proves at `(p,y)=(83,1)` that

\[
 A_P(83)-\frac1{83}A_P(1)
 =-
 \frac{223590076836035175208867029720}
 {8902150522975861711854133933093}<0.
\tag{L-91351.12}
\]

The active sign-threshold prefix bound cannot be promoted to all real endpoints
`x>=83`.

Accordingly:

```text
residual target positive                         retained;
residual declared source score positive          retained;
declared score exceeds target                    refuted and removed.
```

## 5. Terminal child typing

The child endpoint satisfies `1<=y<83`.  At its exact frozen source,
`L-91342` converts the terminal `P_79` packet `D_P(y)` into a positive source/row
object which is intended to be

```text
target exact;
score superordinate;
coefficientwise nonnegative in every finite row.
```

Multiplication by `r=p^-1/2` preserves these properties if the source theorem is
valid in the exact row normalization used here.  The coefficient `r` must remain
visible in every later recurrence and cannot be replaced by a hidden hazard
normalization.

## 6. Literal physical entropy of the residual row

Let

\[
 \mathcal E_{P,p}(py)
 =\sum_{j\ge2}D_{Pp}(py;j)G_j
\tag{L-91351.13}
\]

be the score actually represented by the exact residual component row.
`L-91352` computes it as a positive von Mangoldt convolution and proves

\[
 \boxed{
 \mathcal E_{P,p}(py)>rac43\sqrt{py}.
 }
\tag{L-91351.14}
\]

The same theorem gives

\[
 \boxed{
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
 }
\tag{L-91351.15}
\]

Hence

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}>0.
 }
\tag{L-91351.16}
\]

The independent elementary theorem `L-91353/X-91311` proves, without the
imported Chebyshev bound,

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)>\frac{86}{9},
 \qquad
 \mathcal E_{P,p}(py)-\mathfrak S_{Pp}(py)>\frac{86}{9}.
 }
\tag{L-91351.17}
\]

These are physical raw-row statements, not source-label comparisons.

## 7. Open physical assembly

All current-generation rows must be summed before the single endpoint
quantization.  To convert the exact split into a loss recurrence, one must prove
`SFFEP/LRPT` in the same row normalization:

1. export one source-labelled Hall flow from the true causal capacities of
   `L-91354`;
2. realize every noninherited frontier row `j>y` and every target-null row bonus;
3. retain the literal child coefficient `r`;
4. prove score superordination and normalized-row positivity for the same flow;
5. apply ordinary and radix-four physical maps without duplicating target,
   collar or endpoint port;
6. produce actual scalar target weights summing to at most one.

The exact nested identity embedding and finite-support terminal-debt telescope on
PR `#424` are promising downstream consumers once this live provenance packet
exists.  They do not construct it.

## 8. Corrected consequence

The one-prime arithmetic splice has the exact algebraic form

\[
 \boxed{
 \text{parent row}
 =p^{-1/2}\,\text{terminal child row}
  +\text{current arithmetic residual row}.
 }
\tag{L-91351.18}
\]

The inherited coefficient is at most `1/sqrt(83)`.  The raw current row has
strictly favorable literal entropy by two independent proofs, and the true
causal target/score Hall signs are strictly positive.

What is not yet proved is that one source-faithful positive frontier assembly
simultaneously realizes those ledgers and yields the scalar subprobability
recurrence.  This file therefore supplies an exact split and strong budgets,
not a completed factor-54 theorem.

## 9. Proof boundary

```text
exact Euler row split                         EXACT
positive inherited residual row               INDEPENDENT REPLAY PASSED
exact target and declared-score split          EXACT
true causal residual target/score Hall signs   PROVED / L-91354
strict declared score-over-target surplus      REFUTED / NOT USED
literal residual-row entropy formula           EXACT
uniform physical entropy surplus               PROVED / TWO ROUTES
terminal child positive typing                 SOURCE-PINNED REVIEW REQUIRED
source-labelled Hall flow export               OPEN
noninherited current frontier assembly          OPEN / SFFEP-LRPT
full factor-54 recurrence                      UNPROVEN
Riemann Hypothesis                             UNPROVEN
```
