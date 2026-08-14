# L-91387 — The target-Lorenz row gate is a finite-cell certificate or an exact separator

Claim ID: `L-91387`  
Status: **PROVED FAIL-CLOSED REDUCTION; LIVE CELL SIGNS NOT ALL CERTIFIED HERE**  
Created: 2026-08-14  
Depends on: `L-91386`, `L-91682`, `L-91684`, and the Green boundary reduction `L-91383`  
RH status: **unproved**

## 1. Remaining target-Lorenz gate

For

\[
P_{61}=\prod_{q\le61}q,\qquad
p\ge67,\qquad
1\le y<67,
\]

let \(E,O\) be the positive even and odd causal source measures. Let \(U^*\) be
the leftmost even target submeasure with

\[
T(U^*)=T(O).
\]

By `L-91386`, this submeasure is simultaneously the most favorable possible
choice for every component row and for score. The exact remaining signs are

\[
\boxed{
\mathfrak L_j(p,y)
=
R_j(U^*)-R_j(O)\ge0,
\qquad 2\le j\le66.
}
\tag{L-91387.1}
\]

If one sign fails, the corresponding row is an exact separator for the full
declared stopped-leaf LP.

## 2. Finite cutoff set

`L-91682` proves that every target-Lorenz cutoff lies below \(2000\). There are
exactly `185` possible even \(P_{61}\) cutoff nodes in that range.

For a fixed cutoff \(c\), write

\[
\rho_j(d)=\frac{K_R^{(j)}(d)}{K_T(d)}.
\]

Then the exact row difference is

\[
\begin{aligned}
\mathfrak L_j(p,y)={}&
\sum_{\substack{e<c\\\mu(e)=1}}
K_T(e)\,[\rho_j(e)-\rho_j(c)]\\
&-
\sum_{\substack{o<c\\\mu(o)=-1}}
K_T(o)\,[\rho_j(o)-\rho_j(c)]\\
&+
\sum_{\substack{o>c\\\mu(o)=-1}}
K_T(o)\,[\rho_j(c)-\rho_j(o)].
\end{aligned}
\tag{L-91387.2}
\]

The last line is termwise nonnegative.

## 3. Summation-by-parts form

Let

\[
D_T(t)=
T\bigl(E\cap[1,t]\bigr)
-
T\bigl(O\cap[1,t]\bigr)
\]

with the fractional cutoff convention at \(c\). Since \(\rho_j\) is
nonincreasing, finite Abel summation gives

\[
\boxed{
\mathfrak L_j(p,y)
=
\sum_t D_T(t)\,
\bigl[\rho_j(t)-\rho_j(t^+)\bigr]
+\text{explicit terminal term}.
}
\tag{L-91387.3}
\]

Every profile drop is nonnegative. This shows why the stopped-leaf Hall
counterexample is not decisive for the Lorenz producer: full Hall requires
\(D_T(t)\ge0\) at every threshold, whereas (L-91387.3) needs only a positive
weighted integral of the signed prefixes.

## 4. Activation-cell certificate

The complete \((p,y)\)-space is partitioned by:

```text
child activations y=d;
parent activations py=d;
row activations py/d=j,j+1,...;
target cutoff inequalities at one of 185 even nodes.
```

On one such cell:

* the active source sets are fixed;
* every \(Q_{py/d}(j)\) and \(Q_{y/d}(j)\) is affine in the relevant logarithms;
* the partial cutoff coefficient is an explicit quotient of target sums;
* (L-91387.2) is an explicit real-analytic expression in
  \(r=p^{-1/2}\), \(s=\sqrt y\), and finitely many logarithms.

A proof object for a cell consists of:

1. directed rational boxes for every square root and logarithm;
2. the cutoff-basis inequalities;
3. a directed positive lower bound for all \(\mathfrak L_j\); or
4. an exact rational/interval negative upper bound for one row.

Case 3 certifies the live producer on the cell. Case 4 is a mathematical Farkas
separator for the declared generator cone.

## 5. Large-prime tail

`L-91383` writes each shell row as a positive Green bulk plus a finite
Kantorovich boundary packet. This supplies the appropriate analytic tail
strategy:

```text
prove a uniform positive lower bound beyond one effective p_0;
certify the compact p-corridor by activation cells;
never assert universal shell positivity, which is native-row hard.
```

The exact global shell firewall `R-91314` remains binding. Only the finite
target-Lorenz combination (L-91387.2), with nonzero native slack, is to be
certified.

## 6. Reconnaissance boundary

A broad numerical scan performed during construction found no negative
target-Lorenz row gate on:

```text
all rows 2..66;
all integer y=1..66;
all primes p<=1000;
and 1000 additional random continuous (p,y) samples through p<=5000.
```

The smallest observed integer-grid value was positive and occurred near the
first active cell. This is evidence for the campaign, not a proof, and is not
used by any theorem.

```text
leftmost optimizer              PROVED
cutoff set below 2000           DIRECTED EXACT / L-91682
summation-by-parts gate         EXACT
finite-cell primal/Farkas form  EXACT
all live cell signs             OPEN
Riemann Hypothesis              UNPROVED
```
