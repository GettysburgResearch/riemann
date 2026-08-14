# L-91688 — The `P_19` odd-row prefix closes Target-Lorenz through quotient twenty-two

Claim ID: `L-91688`  
Status: **PROVED DIRECTED / EXACT CELL REDUCTION**  
Created: 2026-08-14  
Depends on: exact activation-cell formula for `Q_Y(j)`; `L-91682`, `L-91685`  
Replay: `X-91685-target-lorenz-vector-primal-dual/verify_quotient22.py`  
RH status: **unproved**

## 1. Directed row theorem

For

\[
 4\le j\le66,
 \qquad
 \max(67,5j)\le x\le22j,
\]

one has

\[
\boxed{
 Q_x(j)
 -\sum_{d\in\{2,3,5,7,11,13,17,19\}}
  \frac1{\sqrt d}Q_{x/d}(j)>0.
}
\tag{L-91688.1}
\]

The set in (L-91688.1) is exactly the set of squarefree `P_61` divisors with
negative Möbius sign below `23`. There is no three-prime odd divisor below
`30`.

## 2. Why the continuum is finite

On an activation cell

\[
 N\le Y<N+1,
\]

write

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N}.
\]

For each integer divisor `d`, the walls of `Q_(x/d)(j)` occur at

\[
 x=dn,
 \qquad n\in\mathbb Z.
\]

Every wall is an integer. Between consecutive integers every activation index
is fixed and the left side of (L-91688.1) is

\[
 A\log x+B.
\]

It is monotone on that cell, and `Q` is continuous across activation walls.
It is therefore enough to check the integer endpoints.

The directed replay checks `37,303` endpoints with 100-digit `Decimal`
square-root and logarithm evaluations enclosed by an outward interval padded by
`10^-78` after every operation. The least certified lower endpoint is

\[
 0.0001614750920097278923\ldots
\]

at

\[
 (j,x)=(66,1452)=(66,22\cdot66).
\]

## 3. Target-Lorenz consequence

Let

\[
 x=py,
 \qquad p\ge67,
 \qquad1\le y<67,
 \qquad x\le22j.
\]

Then

\[
 y=\frac{x}{p}\le\frac{22j}{67}<j,
\]

so every child row is inactive. The active odd row sources are precisely a
subset of

\[
 \{2,3,5,7,11,13,17,19\}.
\]

Let `T_1` be the target of the leftmost even atom and `O_T` the total odd
target demand.

If `O_T<=T_1`, the Target-Lorenz removal uses `O_T/T_1` of atom `1`. The
row-per-target order of `L-91682` gives

\[
 \frac{O_T}{T_1}R_1
 \ge
 \sum_{\mu(o)=-1}R_o.
\tag{L-91688.2}
\]

If `O_T>T_1`, the Target-Lorenz removal uses all of atom `1`, and
(L-91688.1) gives

\[
 R_1>\sum_{\mu(o)=-1}R_o.
\tag{L-91688.3}
\]

All additional used even rows are nonnegative. Hence in both cases

\[
\boxed{
 R_j(U)-O_R^{(j)}>0
 \qquad(py\le22j).
}
\tag{L-91688.4}
\]

Rows `j=2,3` are vacuous in this range because `py>=67>22j`.

Combining with the previous low-quotient lemmas, the entire exact row gate is
now closed through quotient twenty-two.

## 4. Scope

The theorem deliberately uses a stronger certificate than the full
Target-Lorenz margin: atom `1` alone dominates all active odd rows. This
certificate eventually fails, while the full Target-Lorenz producer may still
succeed by using later even atoms.

## 5. Exact boundary

```text
activation-cell reduction                         EXACT
37,303 directed endpoint signs                    PROVED
Target-Lorenz row gate for py/j<=22               PROVED
atom-1-only certificate near quotient 23          NOT VALID GLOBALLY
full Target-Lorenz row family above quotient 22   OPEN / ARITHMETIC
Riemann Hypothesis                                UNPROVEN
```
