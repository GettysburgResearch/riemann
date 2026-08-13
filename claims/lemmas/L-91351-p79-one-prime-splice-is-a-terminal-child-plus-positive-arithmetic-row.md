# L-91351 — The `P_79` one-prime splice is one terminal child plus a positive arithmetic residual row with favorable score

Claim ID: `L-91351`  
Status: **PROPOSED COMPLETE TYPED ONE-PRIME SPLICE THEOREM — FULL COMPOSITION PENDING REVIEW**  
Created: 2026-08-13  
Depends on: `L-91342`, `L-91345-p79-one-prime-splice-has-a-monotone-two-ledger-kernel-and-large-prefix-reserve.md`, `L-91346`, corrected Hall certificate `L-91350`, `X-91128`; finite frontier/collar theorems  
RH status: **unproved at claim level**

## 1. Exact finite Euler rows

Put

\[
 P=P_{79}=\prod_{q\le79}q.
\]

For an endpoint `x` and inherited row `j>=2`, define

\[
 \boxed{
 D_P(x;j)
 =\sum_{\substack{d\mid P\\d\le x/j}}
   \frac{\mu(d)}{\sqrt d}Q_{x/d}(j).
 }
\tag{L-91351.1}

Let `p>=83`, `1<=y<83`, and put `r=p^{-1/2}`.  Adjoining the Euler factor `p`
gives the exact identity

\[
 \boxed{
 D_P(py;j)
 =rD_P(y;j)+D_{Pp}(py;j),
 }
\tag{L-91351.2
}

where

\[
 \boxed{
 D_{Pp}(py;j)
 =D_P(py;j)-rD_P(y;j).
 }
\tag{L-91351.3
}

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
\tag{L-91351.4
}

Thus every row inherited by the contracted child has the positive exact split

```text
parent inherited row
 = p^(-1/2) * terminal child row
   + positive current-generation arithmetic row.
```

Rows `j>y` have no child contribution.  They remain entirely in the current
generation and are handled by the resident finite frontier, collar and terminal
packets; no inherited sign is passed through them.

## 3. Exact target and score identities

For `a>0`, define the finite scalar forcing

\[
 F_{a,P}(x)
 =\sum_{\substack{d\mid P\\d\le x}}
  \mu(d)
  \left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right).
\tag{L-91351.5
}

The SHARP target and endpoint score are

\[
 \mathfrak T_P(x)=3F_{4/3,P}(x),
 \qquad
 \mathfrak S_P(x)=3F_{5/3,P}(x).
\tag{L-91351.6
}

The same Euler algebra gives

\[
 \boxed{
 \mathfrak T_P(py)
 =r\mathfrak T_P(y)+\mathfrak T_{Pp}(py),
 }
\tag{L-91351.7
}

\[
 \boxed{
 \mathfrak S_P(py)
 =r\mathfrak S_P(y)+\mathfrak S_{Pp}(py).
 }
\tag{L-91351.8
}

The corrected finite Hall certificate `L-91350` and the large-prefix theorem
`L-91345` prove

\[
 \boxed{
 \mathfrak T_{Pp}(py)>0,
 \qquad
 \mathfrak S_{Pp}(py)>0.
 }
\tag{L-91351.9
}

These are the scalar ledgers of the same exact Euler residual as (L-91351.3).

## 4. Strict score-over-target surplus

Let

\[
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d.
\]

Since the score and target kernels differ by the square-root first moment,

\[
 \boxed{
 \mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)
 =\sqrt{py}\left[A_P(py)-\frac1pA_P(y)\right].
 }
\tag{L-91351.10
}

The `P_79` prefix theorem gives

\[
 A_P(x)>\frac1{25}
 \qquad(x\ge83).
\]

The exact finite replay `X-91128` gives

\[
 A_P(y)\le1
 \qquad(1\le y<83).
\]

Therefore

\[
 \boxed{
 \mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)
 >\left(\frac1{25}-\frac1{83}\right)\sqrt{py}
 =\frac{58}{2075}\sqrt{py}>0.
 }
\tag{L-91351.11
}

The current arithmetic residual is not merely score-feasible; it has a uniform
favorable score surplus.

## 5. Terminal child typing

The child endpoint satisfies `1<=y<83`.  `L-91342` converts the complete terminal
`P_79` packet `D_P(y)` into one positive source/row object which is

```text
target exact;
score superordinate;
coefficientwise nonnegative in every finite row.
```

Multiplication by `r=p^-1/2` preserves every property.  Thus the first term in
(L-91351.2), (L-91351.7) and (L-91351.8) is a legitimate positive terminal child
with coefficient strictly below one.

The second term is the exact nonnegative arithmetic residual row and has positive
target and still larger score by Sections 2--4.

## 6. Physical assembly

All current-generation rows are summed before the single endpoint quantization.
The resident finite mismatch, B-spline collar and terminal omission are therefore
charged once.  Applying the nonnegative ordinary and radix-four carry maps to the
positive residual row preserves feasibility.

No finite child is evaluated at a fractional physical column, and no independent
copy of the parent target or endpoint port is assigned to the prime branch.

## 7. Consequence

The `P_79` one-prime arithmetic splice required by `O-91309` has the exact typed
form

\[
 \boxed{
 \text{parent}
 =p^{-1/2}\,\text{positive terminal child}
  +\text{positive current arithmetic packet}.
 }
\tag{L-91351.12
}

The inherited coefficient is at most `1/sqrt(83)`, while the local residual has
nonpositive signed score loss because score exceeds target.

This closes the splice without multiplying the refuted completed two-state
matrices and without requiring a common Hall residual to reproduce the inherited
row.

## 8. Proof boundary

```text
exact Euler row split                         EXACT
positive inherited residual row               DIRECTED/ANALYTICALLY CERTIFIED
exact target and score split                  EXACT
positive residual target and score            CERTIFIED
strict score-over-target surplus              EXACT + FINITE PREFIX CERTIFICATE
terminal child positive typing                AVAILABLE
one-use current physical assembly             AVAILABLE
full factor-54 recurrence                     NEXT THEOREM
Riemann Hypothesis                            UNPROVED AT THIS CLAIM
```
