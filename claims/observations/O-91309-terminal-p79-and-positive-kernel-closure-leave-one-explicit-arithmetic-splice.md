# O-91309 — The terminal `P_79` projection and positive-kernel recursion leave one explicit arithmetic splice

Claim ID: `O-91309`  
Status: **CURRENT ROUTE HANDOFF / NO RH CLAIM**  
Created: 2026-08-12  
Depends on: `L-91342/L-91343`; the corrected DAG `O-91308`  
RH status: **unproved**

## 1. Two newly closed interfaces

`L-91342` closes the terminal finite source projection after absorbing all primes
through `79`.  On

\[
 1\le x<83,
\]

the signed `P_79` packet has one positive representation which is
simultaneously:

```text
target-exact;
score-superordinate;
coefficientwise nonnegative in every exact finite row.
```

The no-upward target-Hall margin is greater than `7/100`, and every normalized
component profile `Q_Y(j)/(4 sqrt(Y)-3)` is strictly increasing through the
terminal window.

`L-91343` closes every later operation **after** a packet has entered the
positive kernel cone.  Any pointwise subprobability rough split gives:

```text
an exact one-use target partition;
a coefficient-one score partition with positive local surplus;
a coefficientwise positive decomposition of every finite row;
children contracted by at least factor 83;
one sum-before-quantize physical assembly.
```

Thus neither terminal projection nor positive-kernel all-generation branching
is open any longer.

## 2. Exact first open arrow

Let

\[
 P_{79}=\prod_{p\le79}p.
\]

For a new rough prime `p>=83`, a terminal child parameter `1<=y<83`, and an
exact finite row `j>=2`, define the one-prime arithmetic splice

\[
\boxed{
\begin{aligned}
 \mathscr R_{p,y}(j)={}&
 \sum_{\substack{d\mid P_{79}\\d\le py/j}}
  \frac{\mu(d)}{\sqrt d}Q_{py/d}(j)\\
 &-\frac1{\sqrt p}
 \sum_{\substack{d\mid P_{79}\\d\le y/j}}
  \frac{\mu(d)}{\sqrt d}Q_{y/d}(j).
\end{aligned}}
\tag{O-91309.1}
\]

This is the exact row produced by the finite small-prime block followed by one
new rough Euler factor, in the one-prime-per-reset range.  There are analogous
ordinary/radix-four target and endpoint-score coordinates obtained by applying
the corresponding linear functionals.

The first open theorem is:

> **`P_79` One-Prime Positive Splice.** For every `p>=83` and `1<=y<83`,
> construct from the packet (O-91309.1) one positive source/row measure which is
> target-exact, score-superordinate and compatible with the single global
> endpoint port, with the child contribution passed at coefficient at most one.

A proof feeds the output into `L-91343`, then `L-91329/T-91302`, and closes the
factor-54 route.  A strict negative row, target, or score-separation witness
refutes this route at its first open arrow.

## 3. Why this is genuinely narrower than the old gate

The old statement asked for an unspecified all-generation source-faithful
projection.  The current statement has:

```text
one finite small-prime block P_79;
one rough prime parameter p>=83;
one bounded child window 1<=y<83;
one explicit positive component family Q;
one already constructed bounded common port.
```

All multiprime composition after a successful splice is handled by the positive
kernel recursion.  No scalar tensorization, fractional finite column, raw
four-state contraction, or independent branch use of the parent source is
allowed.

## 4. Surviving firewalls

Any proof of the one-prime splice must respect:

```text
finite equality seed != continuum Volterra seed       R-91102
one-prime scalar endpoint ports do not tensorize       R-91303
integer finite feasibility cannot be used at Q/m       R-91304
full parent source cannot feed every prime branch       R-91305
lower-triangular hidden lift is not raw-l1 contractive R-91306
isolated hazard return cannot preserve both ledgers     R-91307
```

The positive-kernel theorem `L-91343` applies only after the signed arithmetic
packet has crossed the one-prime splice.

## 5. Current proof boundary

```text
terminal P_79 source-to-row projection              CLOSED
positive-kernel target/score/row branching          CLOSED
factor-83 child contraction                         CLOSED
one-use physical sum-before-quantize assembly       CLOSED
P_79 plus one rough-prime positive splice           OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```