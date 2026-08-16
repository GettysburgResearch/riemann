# L-94102 — Endpoint-blocker localization gives an explicit native `Y_4` price

Claim ID: `L-94102`  
Status: **PROVED EXACT REDUCTION AND ELEMENTARY SUFFICIENT CONDITION**  
Created: 2026-08-16  
Primary inputs: `L-94101`; the `Y_4` recurrence; the elementary Chebyshev bound `psi(x)<4 log(2) x`  
RH status: **unproved**

## 1. Blocker support

Let `s_X` be the exact final detail slack of the native endpoint-detail greedy.
Define

\[
 B_X=\max\{q\ge2:s_X(q)>0\},
 \tag{L-94102.1}
\]

with `B_X=1` if the slack vanishes identically.

By `L-94101.18`,

\[
 s_X(q)>0
 \iff
 \ell_{q+1}>0.
 \tag{L-94102.2}
\]

Thus `B_X` is both the largest unsaturated physical detail column and the
largest endpoint scale carrying a diagonal blocker loss, minus one.

If

\[
 \ell_T=0\qquad(T>B+1),
 \tag{L-94102.3}
\]

then `B_X<=B`. This is a purely finite statement about the explicit greedy
coefficient list.

## 2. Deficit is supported on the blockers

Since `0<=s_X(q)<=Omega_X(q)`, support localization gives

\[
 \boxed{
 \mathfrak D_X^{\rm ned}
 =\sum_{q\le B_X}Y_4(q)s_X(q)
 \le\sum_{q\le B_X}Y_4(q)\Omega_X(q).
 }
 \tag{L-94102.4}
\]

No source-mass or score-superordination estimate appears here; this is the exact
native dual applied to the actual physical slack.

## 3. Exact scale-four summation

For `B<=X/4`,

\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}
 \qquad(q\le B).
\]

Using

\[
 Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k),
\]

and changing variables `q=4^k m`,

\[
 \boxed{
 \sum_{q\le B}\frac{Y_4(q)}{\sqrt q}
 =
 \sum_{k\ge0}
 \sum_{m\le B/4^k}
 \frac{\Lambda(m)}{\sqrt m}.
 }
 \tag{L-94102.5}
\]

The factor `2^k` cancels `sqrt(4^k)` exactly. This identity is the reason a
support bound is much stronger than a pointwise estimate for `Y_4`.

## 4. Elementary Chebyshev price

Put

\[
 \psi(t)=\sum_{m\le t}\Lambda(m).
\]

The elementary binomial argument gives

\[
 \psi(t)<4(\log2)t.
 \tag{L-94102.6}
\]

Partial summation yields

\[
 \sum_{m\le t}\frac{\Lambda(m)}{\sqrt m}
 =\frac{\psi(t)}{\sqrt t}
 +\frac12\int_1^t\psi(u)u^{-3/2}\,du
 <8(\log2)\sqrt t.
 \tag{L-94102.7}
\]

Insert this in (L-94102.5):

\[
 \sum_{q\le B}\frac{Y_4(q)}{\sqrt q}
 <8(\log2)\sqrt B\sum_{k\ge0}2^{-k}
 =16(\log2)\sqrt B.
 \tag{L-94102.8}
\]

Since `log4=2log2`,

\[
 \boxed{
 B_X\le B\le X/4
 \Longrightarrow
 \mathfrak D_X^{\rm ned}
 <32(\log2)^2\sqrt B.
 }
 \tag{L-94102.9}
\]

## 5. A sharply localized closing theorem

Consequently the finite combinatorial statement

\[
 \boxed{
 B_X=o(\log^4X)
 }
 \tag{NEDB}
\]

implies

\[
 \mathfrak D_X^{\rm ned}=o(\log^2X).
 \tag{L-94102.10}
\]

The stronger bound `B_X=O(log^2 X)` would give

\[
 \mathfrak D_X^{\rm ned}=O(\log X).
\]

By the frozen one-sided endpoint consumer, either statement yields the proposed
implication to RH.

`NEDB` is not asserted here. It is the sole asymptotic producer left by this
architecture.

## 6. Why this frontier is different

The previous factor-67 programmes had to audit:

```text
paired Möbius source signs;
negative oriented children;
least-prime normalization;
Target-Lorenz tail certificates;
activation knots and endpoint cells;
finite/continuum comparison ownership;
child capacities and common ports.
```

The endpoint-detail compiler removes all of those interfaces. Its remaining
object is the support of an explicit one-dimensional positive greedy on a
strictly triangular matrix.

A failed `NEDB` instance is itself concrete: it supplies an endpoint `X`, a
large unsaturated column `q`, the exact blocker stage `q+1`, and the complete
primal coefficient/residual ledger. It can therefore be attacked by exact
finite exchange, total-positivity, or Farkas methods without reconstructing a
Möbius source tree.

```text
exact native-feasible row for every X             PROVED
weighted deficit support                           EXACT
Y4 support price                                   <32(log2)^2 sqrt(B)
B_X=o(log^4 X) -> endpoint producer                EXACT
NEDB                                                OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
