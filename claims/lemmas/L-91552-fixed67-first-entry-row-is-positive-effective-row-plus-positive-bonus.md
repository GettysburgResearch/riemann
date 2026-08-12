# L-91552 — The fixed-`67` first-entry row is an effective positive row plus a positive dilation bonus

Claim ID: `L-91552`  
Status: **DIRECTED-EXACT FIXED-SCALE NORMALIZATION AUDIT**  
Created: 2026-08-13  
Depends on: `L-91344`, `L-91345`, `L-91547`, candidate composition `T-91551`  
RH status: **unproved**

## 1. Exact `P_61` component row

Let

\[
 P_{61}=\prod_{q\le61}q
\]

and, for real `x>=1` and integer `j>=2`, define

\[
 \boxed{
 \mathcal A_j(x)
 =\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{x/d}(j),
 }
\tag{L-91552.1}
\]

with causal zero extension.  This is the exact finite-Euler component row of
`L-91344`.

Fix the contraction prime

\[
 p=67,
 \qquad r=67^{-1/2},
\]

and write

\[
 2\le j\le y<67,
 \qquad x=67y.
\]

The raw `P_61` plus one-prime row is

\[
 \boxed{
 \mathscr R^{(61)}_{67,y}(j)
 =\mathcal A_j(x)-r\mathcal A_j(y).
 }
\tag{L-91552.2}
\]

Equivalently,

\[
 \mathscr R^{(61)}_{67,y}(j)
 =\sum_{d\mid P_{67}}\frac{\mu(d)}{\sqrt d}Q_{x/d}(j),
 \qquad P_{67}=67P_{61},
\tag{L-91552.3}
\]

by splitting divisors according as they contain `67`.

## 2. Effective row plus normalization bonus

Pure algebra gives

\[
 \boxed{
 \mathscr R^{(61)}_{67,y}(j)
 =(1-r)\mathcal A_j(x)
  +r\bigl[\mathcal A_j(x)-\mathcal A_j(y)\bigr].
 }
\tag{L-91552.4}
\]

The first summand has the natural survival/effective coefficient `1-r`.  The
second summand is the complete row-level normalization discrepancy between the
raw Euler splice and that effective row.

The load-bearing sign question is therefore whether the parent row and the
scale-dilation difference are both nonnegative.  On the complete fixed-`67`
window they are uniformly positive.

## 3. Directed-exact uniform bounds

The companion checker proves simultaneously, for every real

\[
 2\le j\le y<67,
 \qquad x=67y,
\]

that

\[
 \boxed{
 \mathcal A_j(x)>\frac1{100},
 }
\tag{L-91552.5}
\]

\[
 \boxed{
 \mathcal A_j(x)-\mathcal A_j(y)>\frac1{100},
 }
\tag{L-91552.6}
\]

and

\[
 \boxed{
 \mathscr R^{(61)}_{67,y}(j)>\frac3{250}.
 }
\tag{L-91552.7}
\]

Consequently the raw arithmetic row is a positive effective row plus a
positive current-generation dilation bonus.  No endpoint port is needed to
repair this inherited component row.

The smallest directed lower endpoints are

```text
parent row A_j(67y):
  0.012407770154759505... at j=66, x=4422;

dilation bonus A_j(67y)-A_j(y):
  0.010539196481300355... at j=66, x=4489;

raw P_67 row:
  0.012214088105776916... at j=66, x=4489.
```

The endpoint `x=4489` represents the right limit `y->67-`.

## 4. Why the replay is exhaustive

Retain the exact three-sector component formula

\[
 Q_Y(j)
 =A_j\ell_Y(j)+B_j\ell_Y(j+1)
  +C_j\sum_{m\ge j+2}\ell_Y(m),
\]

where

\[
 A_j=\frac{j+1}{j-1},
 \qquad
 B_j=-\frac{(j+1)(j-2)}{j(j-1)},
 \qquad
 C_j=\frac2{j(j-1)}.
\]

Writing

\[
 c_j(m)=
 \begin{cases}
 0,&m<j,\\
 A_j,&m=j,\\
 B_j,&m=j+1,\\
 C_j,&m\ge j+2,
 \end{cases}
\]

and

\[
 b_j(k)
 =\sum_{\substack{e\mid P_{61}\\e\mid k}}
  \mu(e)c_j(k/e),
\tag{L-91552.8}
\]

one obtains

\[
 \boxed{
 \mathcal A_j(x)
 =\sum_{k\le x}\frac{b_j(k)}{\sqrt k}\log(x/k).
 }
\tag{L-91552.9}
\]

Similarly,

\[
 \mathcal A_j(x/67)
 =\sum_{67k\le x}
  \frac{b_j(k)}{\sqrt k}\log(x/(67k)).
\tag{L-91552.10}
\]

Every breakpoint is therefore an integer.  On each activation cell `[N,N+1]`
each tested function is of the form

\[
 C\log x-D
\]

with constant exact algebraic coefficients, so its minimum is at an endpoint.
The domain is

\[
 67j\le x<67^2,
 \qquad2\le j\le66.
\]

The checker exhausts all `143,715` cells and all three quantities at both
endpoints, giving `862,290` directed endpoint inequalities.

Square roots are enclosed by integer-square bounds at denominator `10^35`.
Logarithms are enclosed by the positive atanh series after dyadic reduction,
with a rigorous geometric tail after `90` terms.  All arithmetic is outward
rounded with integers; no floating-point sign decision enters the proof.

Retained verdict:

```text
PASS_FIXED67_FIRST_ENTRY_ROW_AUDIT
```

## 5. Meaning for the candidate factor-54 chain

This theorem independently checks the component-row compatibility of the raw
small-prime packet with the fixed scale-`67` geometry used by `L-91547`:

```text
P_61 arithmetic packet;
fixed contraction prime 67;
complete real child interval 1<=y<67;
every inherited row 2<=j<=y;
raw row = positive effective row + positive bonus.
```

Together with `L-91345`, no target, score, or inherited-row separator exists on
this fixed-scale slice.

It does **not** independently reconstruct the complete candidate proof.  The
merged Hall producer, affine physical lift, one-use endpoint-port/collar ledger,
literal native loss recurrence, and finite base must still be rebuilt from
definitions before `T-91551` can be promoted.

```text
fixed-67 parent effective row                    DIRECTED EXACT POSITIVE
fixed-67 dilation/normalization bonus            DIRECTED EXACT POSITIVE
fixed-67 raw P_67 inherited row                  DIRECTED EXACT POSITIVE
fixed-67 target/score scalar packet              CLOSED BY L-91345
complete physical reset reconstruction           OPEN REVIEW
candidate T-91551                                WRITTEN / REVIEW REQUIRED
Riemann Hypothesis                               UNPROVEN
```
