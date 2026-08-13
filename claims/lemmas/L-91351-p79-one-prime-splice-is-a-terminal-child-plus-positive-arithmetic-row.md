# L-91351 — The `P_79` one-prime splice is one terminal child plus an exact arithmetic residual row

Claim ID: `L-91351`  
Status: **CORRECTED PROPOSED COMPLETE TYPED ONE-PRIME SPLICE — FULL COMPOSITION PENDING REVIEW**  
Created: 2026-08-13  
Corrected: 2026-08-13 after exact counterexample `R-91310`  
Depends on: `L-91342`; `L-91345-p79-one-prime-splice-has-a-monotone-two-ledger-kernel-and-large-prefix-reserve.md`; `L-91346`; corrected Hall certificate `L-91350`; physical entropy repair `L-91352`; finite frontier/collar theorems  
RH status: **unproved at claim level**

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

Let `p>=83`, `1<=y<83`, and put `r=p^{-1/2}`. Adjoining the Euler factor `p`
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

Rows `j>y` have no child contribution. They remain entirely in the current
generation. Their exact realization in the same row normalization is supplied
only after the resident finite frontier, collar and terminal packets are
assembled; `L-91346` does not certify those rows.

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

The corrected finite Hall certificate `L-91350` and the large-prefix theorem
`L-91345` prove

\[
 \boxed{
 \mathfrak T_{Pp}(py)>0,
 \qquad
 \mathfrak S_{Pp}(py)>0.
 }
\tag{L-91351.9}
\]

These are scalar ledgers of the same Euler residual. They are not automatically
the literal entropy score of its component row.

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
\tag{L-91351.10}
\]

is valid. The former conclusion that its right side is uniformly positive is
false. `R-91310` proves at `(p,y)=(83,1)` that

\[
 A_P(83)-\frac1{83}A_P(1)
 =-
 \frac{223590076836035175208867029720}
 {8902150522975861711854133933093}<0.
\tag{L-91351.11}
\]

The active odd-threshold prefix bound in `L-91345` cannot be promoted to all
real endpoints `x>=83`.

Accordingly:

```text
residual target positive                         retained;
residual declared source score positive          retained;
declared score exceeds target                    refuted and removed.
```

## 5. Terminal child typing

The child endpoint satisfies `1<=y<83`. `L-91342` converts the complete terminal
`P_79` packet `D_P(y)` into one positive source/row object which is

```text
target exact;
score superordinate;
coefficientwise nonnegative in every finite row.
```

Multiplication by `r=p^-1/2` preserves every property. Thus the first term in
(L-91351.2), (L-91351.7) and (L-91351.8) is a legitimate positive terminal child
with coefficient strictly below one.

## 6. Literal physical entropy of the residual row

Let

\[
 \mathcal E_{P,p}(py)
 =\sum_{j\ge2}D_{Pp}(py;j)G_j
\tag{L-91351.12}
\]

be the score actually represented by the exact residual component row.
`L-91352` computes it as a positive von Mangoldt convolution and proves

\[
 \boxed{
 \mathcal E_{P,p}(py)>rac43\sqrt{py}.
 }
\tag{L-91351.13}
\]

The same theorem gives the source upper corridors

\[
 \boxed{
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
 }
\tag{L-91351.14}
\]

Hence the corrected favorable statement is

\[
 \boxed{
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}>0.
 }
\tag{L-91351.15}
\]

This is a physical row-entropy statement, not a source-label comparison.

## 7. Physical assembly

All current-generation rows must be summed before the single endpoint
quantization. The resident finite mismatch, B-spline collar and terminal
omission are therefore charged once. Applying the ordinary and radix-four maps
preserves feasibility after:

1. the inherited residual rows `2<=j<=y` are certified by `L-91346`;
2. the current frontier rows `j>y` are realized exactly in the row normalization
   used in (L-91351.12);
3. the bounded finite assembly debt is charged once.

No finite child is evaluated at a fractional physical column, and no independent
copy of the parent target or endpoint port is assigned to the prime branch.

## 8. Corrected consequence

The one-prime arithmetic splice has the exact form

\[
 \boxed{
 \text{parent row}
 =p^{-1/2}\,\text{terminal child row}
  +\text{current arithmetic residual row}.
 }
\tag{L-91351.16}
\]

The inherited coefficient is at most `1/sqrt(83)`. Once the exact current rows
are assembled, their literal entropy exceeds their target, so they introduce no
positive physical score loss apart from the already bounded finite correction.

This closes the scalar score-interface error without multiplying the refuted
completed two-state matrices and without requiring a Hall residual to reproduce
the inherited row.

## 9. Proof boundary

```text
exact Euler row split                         EXACT
positive inherited residual row               INDEPENDENT REPLAY PASSED
exact target and declared-score split          EXACT
positive residual target and source score      CERTIFIED
strict declared score-over-target surplus      REFUTED / NOT USED
literal residual-row entropy formula           EXACT
uniform physical entropy surplus               PROPOSED COMPLETE
terminal child positive typing                 AVAILABLE / REVIEW
one-use current physical assembly              AVAILABLE / REVIEW
full factor-54 recurrence                      CORRECTED NEXT THEOREM
Riemann Hypothesis                             UNPROVED AT THIS CLAIM
```
