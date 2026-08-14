# R-91675 — The atom-one odd-prefix certificate fails at quotient twenty-three

Refutation ID: `R-91675`  
Status: **PROVED DIRECTED COUNTEREXAMPLE TO A STRONGER SUFFICIENT CERTIFICATE**  
Created: 2026-08-14  
Replay: `X-91685-target-lorenz-vector-primal-dual/verify_quotient23_firewall.py`  
RH status: **unproved**

## 1. The over-strong certificate

The proof of `L-91688` uses the sufficient inequality

\[
 Q_x(j)>
 \sum_{d\in\{2,3,5,7,11,13,17,19\}}
 \frac1{\sqrt d}Q_{x/d}(j).
 \tag{R-91675.1}
\]

It says that the leftmost even atom `d=1` alone dominates every active odd row.
This is stronger than the actual Target-Lorenz row gate, which may also use
later even atoms.

## 2. Exact counterexample

At

\[
 j=44,
 \qquad x=1012=23\cdot44,
\]

the directed interval replay proves

\[
\begin{aligned}
&Q_{1012}(44)
 -\sum_{d\in\{2,3,5,7,11,13,17,19\}}
  \frac1{\sqrt d}Q_{1012/d}(44)\\
&\qquad<
 -0.0003543982654283312355<0.
\end{aligned}
 \tag{R-91675.2}
\]

The new odd source `23` has zero row exactly on its activation wall, so adding
it does not cause the sign. The atom-one reserve itself has already crossed
zero.

## 3. What is and is not refuted

This refutes only the attempt to extend `L-91688` by keeping atom `1` as the
sole used even row.

It does **not** refute the Target-Lorenz producer. At quotient twenty-three the
leftmost target removal may use later even atoms such as

```text
6, 10, 14, 15, 21, 22,
```

and `L-91685` says that the complete leftmost submeasure, not atom `1` alone, is
the exact common-source primal.

The next arithmetic theorem must therefore retain the actual target cutoff or
prove the full target-normalized determinant. A one-atom prefix proof is no
longer sufficient.

## 4. Boundary

```text
atom-one certificate through quotient 22       PROVED / L-91688
atom-one certificate at quotient 23            FALSE / EXACT WITNESS
full Target-Lorenz row margin at quotient 23   NOT REFUTED
Riemann Hypothesis                              UNPROVEN
```
