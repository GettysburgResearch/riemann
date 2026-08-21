# L-91348 — The shifted-eight target Hall flow gives one positive `P_79` splice packet with uniformly bounded score debt

Claim ID: `L-91348`  
Status: **PROVED EXACT COMMON TARGET/SCORE PACKET THEOREM — DEPENDENCY STACK PENDING REVIEW**  
Created: 2026-08-13  
Depends on: `L-91343`, `L-91345-p79-one-prime-splice-has-a-monotone-two-ledger-kernel-and-large-prefix-reserve.md`, `L-91347`  
RH status: **unproved at claim level**

## 1. Target Hall flow

Fix

\[
 p\ge83,
 \qquad 1\le y<83,
 \qquad P_{79}=\prod_{q\le79}q.
\]

For each active squarefree divisor `d|P_79`, let

\[
 T_d=K_\Psi(d;p,y)>0,
 \qquad
 S_d=K_S(d;p,y)>0
\]

be the one-prime target and endpoint-score atoms of `L-91345`.

Give an odd demand node `o` the neighborhood

\[
 \mathcal N(o)=\{e:\mu(e)=1,\ e\le o+8\}.
\]

`L-91347` proves every target Hall inequality for odd thresholds below `4096`.
`L-91345` proves the stronger no-upward target Hall inequality for every
threshold at least `4096`.  Hence the shifted-eight target Hall inequalities
hold at every active odd threshold.

The nested-neighborhood Hall theorem therefore gives a target-mass flow

\[
 \boxed{
 t_{o,e}\ge0,
 \qquad e\le o+8,
 }
\tag{L-91348.1}
\]

such that

\[
 \sum_e t_{o,e}=T_o
\tag{L-91348.2}
\]

for every odd source and

\[
 \sum_o t_{o,e}\le T_e
\tag{L-91348.3}
\]

for every even source.

Define the residual even coefficients

\[
 \boxed{
 \nu_e=1-\frac1{T_e}\sum_ot_{o,e}\ge0.
 }
\tag{L-91348.4}
\]

They form one positive source measure.

## 2. Exact target ledger

By (L-91348.2)--(L-91348.4),

\[
\begin{aligned}
 \sum_e\nu_eT_e
 &=\sum_eT_e-\sum_{o,e}t_{o,e}\\
 &=\sum_eT_e-\sum_oT_o.
\end{aligned}
\]

Thus

\[
 \boxed{
 \sum_e\nu_eT_e
 =\sum_{\mu(d)=1}T_d-\sum_{\mu(d)=-1}T_d.
 }
\tag{L-91348.5}
\]

The positive residual source is exactly target-exact.  No target is duplicated
and no independent target copy is assigned to a branch.

## 3. Score/target ratio

Put

\[
 \phi(v)=\frac{5v-3}{4v-3},
 \qquad v\ge1.
\]

Then

\[
 \phi'(v)=-\frac3{(4v-3)^2}<0.
\tag{L-91348.6}
\]

For `d>y`,

\[
 \frac{S_d}{T_d}=\phi\!\left(\sqrt{py/d}\right),
\]

while for `d<=y`,

\[
 \frac{S_d}{T_d}
 =\phi\!\left((1+p^{-1/2})\sqrt{py/d}\right).
\tag{L-91348.7}
\]

Consequently the score per target unit increases with the source index, with one
additional upward jump across the child-support interface.

Let

\[
 c_d=\frac{S_d}{T_d}.
\]

The score of the residual positive source differs from the signed arithmetic
score by

\[
\boxed{
 \sum_e\nu_eS_e-
 \left(\sum_eS_e-\sum_oS_o\right)
 =\sum_{o,e}t_{o,e}(c_o-c_e).
}
\tag{L-91348.8
}

Every edge with `e<=o` is favorable.  Only upward edges can create score debt.

## 4. Same-regime upward-edge bound

Suppose

\[
 o<e\le o+8
\]

and both nodes lie on the same side of the child cutoff `y`.  There is a constant
`C>0` such that the arguments in (L-91348.7) are

\[
 v_d=C/\sqrt d.
\]

Since `v_e>=1`,

\[
\begin{aligned}
 c_e-c_o
 &=\int_{v_e}^{v_o}\frac3{(4v-3)^2}\,dv\\
 &\le\frac{3(v_o-v_e)}{v_e^2}\\
 &\le\frac{12}{o\,v_e}.
\end{aligned}
\tag{L-91348.9
}

Here we used

\[
 \sqrt{e/o}-1\le\frac{e-o}{2o}\le\frac4o.
\]

The target atom at `o` satisfies

\[
 T_o\le\frac{4v_o}{\sqrt o}
 \le\frac{12v_e}{\sqrt o},
\]

because `e/o<=9`. Therefore

\[
 \boxed{
 T_o(c_e-c_o)
 \le\frac{144}{o^{3/2}}.
 }
\tag{L-91348.10
}

## 5. Interface-crossing bound

Now suppose

\[
 o\le y<e\le o+8.
\]

Write

\[
 u_o=\sqrt{py/o},
 \qquad u_e=\sqrt{py/e},
 \qquad r=p^{-1/2}.
\]

Split

\[
 \phi(u_e)-\phi((1+r)u_o)
 =\bigl[\phi(u_e)-\phi(u_o)\bigr]
  +\bigl[\phi(u_o)-\phi((1+r)u_o)\bigr].
\]

The first bracket is bounded as in Section 4, with the harmless larger constant

\[
 T_o[\phi(u_e)-\phi(u_o)]
 \le\frac{288}{o^{3/2}}.
\tag{L-91348.11
}

For the second bracket,

\[
 \phi(u_o)-\phi((1+r)u_o)
 \le\frac{3r}{u_o},
\]

and

\[
 T_o\le\frac{8u_o}{\sqrt o}.
\]

Hence

\[
 \boxed{
 T_o[\phi(u_o)-\phi((1+r)u_o)]
 \le\frac{24}{\sqrt{p o}}
 <\frac3{\sqrt o}.
 }
\tag{L-91348.12
}

Only odd integers in the interval `(y-8,y]` can cross the interface.  There are
at most eight of them, so the complete interface-jump contribution is below
`24`.

## 6. Uniform bounded score debt

For each odd node, the total outgoing target mass is exactly `T_o`.  Equations
(L-91348.10)--(L-91348.12) therefore give

\[
\begin{aligned}
 \sum_{o,e}t_{o,e}(c_e-c_o)_+
 &<288\sum_{o\ge1}o^{-3/2}+24\\
 &<288\cdot3+24\\
 &=888.
\end{aligned}
\]

Thus the convenient integer bound

\[
 \boxed{
 \sum_e\nu_eS_e
 \ge
 \sum_{\mu(d)=1}S_d-\sum_{\mu(d)=-1}S_d-900
 }
\tag{L-91348.13
}

holds uniformly for every `p>=83` and every `1<=y<83`.

The constant is deliberately crude.  Its importance is that it is independent
of the parent endpoint, the rough prime and the number of later generations.
It is an admissible bounded reset debt.

## 7. Positive rows and later rough branching

The residual source `nu` is coefficientwise positive and belongs to the native
`W_Psi/W_S/Q` kernel cone.  Therefore `L-91343` applies directly:

```text
all exact finite component rows are nonnegative;
ordinary and radix-four physical capacities are assembled positively;
later rough children form a pointwise subprobability family;
current-generation score residual dominates target residual;
all colors are summed before the one finite quantization.
```

No completed two-state matrix is multiplied, so the cascade counterexample of
`R-91304` is irrelevant.  No finite child is evaluated at a fractional physical
column.

## 8. Consequence

The `P_79` plus one-prime arithmetic splice now has one explicit positive source
packet satisfying

```text
target ledger:       exact;
score ledger:        exact up to debt <900;
finite rows:         positive through the native kernel cone;
child coefficients: subprobability;
child endpoints:    at most parent/83;
physical target:    used once.
```

Together with the existing finite collar/terminal packets, the total debt per
factor-54 generation remains bounded.

## 9. Proof boundary

```text
shifted-eight target Hall flow                 EXACT
positive residual source measure               EXACT
target exactness                               EXACT
one-prime ratio derivative                     EXACT
same-regime upward score bound                 EXACT
interface upward score bound                   EXACT
uniform score debt <900                        EXACT
positive-kernel continuation                   IMPORTED EXACT
complete factor-54 composition                 NEXT THEOREM
Riemann Hypothesis                             UNPROVED AT THIS CLAIM
```
