# L-91354 — Every hidden least-prime hazard contains a safe canonical child with a substochastic scalar coefficient

Claim ID: `L-91354`  
Status: **PROVED EXACT HIDDEN-SUBPACKET / SCALAR-LEDGER THEOREM — PHYSICAL RESIDUAL TYPING OPEN**  
Created: 2026-08-13  
Depends on: `L-91335/L-91336/L-91337`; PR #431 hazard obstruction  
RH status: **unproved**

## 1. Hidden hazard coefficients

Let the rough primes be ordered and put

\[
A_p=1-p^{-1},
\qquad
B_p=1-p^{-1/2}.
\]

For the branch whose least active rough prime is `p_j`, define

\[
 h_j^X=\frac1{p_j}\prod_{i<j}A_{p_i},
 \qquad
 h_j^Y=\frac1{\sqrt{p_j}}\prod_{i<j}B_{p_i}.
\tag{L-91354.1}
\]

`L-91336` proves the coordinatewise positive partition

\[
I_4=Q_\infty+\sum_jH_j,
\qquad
H_j=\operatorname{diag}(h_j^X,h_j^X,h_j^Y,h_j^Y),
\tag{L-91354.2}
\]

with

\[
\sum_jh_j^X\le1,
\qquad
\sum_jh_j^Y\le1.
\tag{L-91354.3}
\]

## 2. Canonical hidden packet

For a positive physical state `s=(L,R)^T`, the canonical hidden lift is

\[
I(s)=(L,R,L,2R)^T\ge0.
\tag{L-91354.4}
\]

Define the safe child coefficient

\[
\boxed{
\alpha_j=\min(h_j^X,h_j^Y).
}
\tag{L-91354.5}
\]

Then, coordinatewise,

\[
\boxed{
H_jI(s)-\alpha_jI(s)
=
\begin{pmatrix}
(h_j^X-\alpha_j)L\\
(h_j^X-\alpha_j)R\\
(h_j^Y-\alpha_j)L\\
2(h_j^Y-\alpha_j)R
\end{pmatrix}
\ge0.
}
\tag{L-91354.6}
\]

Thus every actual hidden hazard contains a literal scalar copy of the complete canonical packet. No comparison after signed physical observation is used.

## 3. Target and score ledgers

The positive hidden target and score functionals are

\[
m_\Psi(z)=X^++Y^-,
\qquad
m_S(z)=2X^++X^-.
\]

On a canonical packet,

\[
m_\Psi(I(s))=L+2R,
\qquad
m_S(I(s))=2L+R.
\tag{L-91354.7}
\]

Therefore the extracted child has exactly

\[
\boxed{
 m_\Psi(\alpha_jI(s))=\alpha_j(L+2R),
 \qquad
 m_S(\alpha_jI(s))=\alpha_j(2L+R).
}
\tag{L-91354.8}
\]

The residual in (L-91354.6) has nonnegative target and score because both hidden functionals have nonnegative coefficients.

For the pure reserve test used in PR #431 and the first rough prime, `h^X=p^{-1}` and `h^Y=p^{-1/2}`. Hence

\[
\boxed{\alpha=p^{-1},}
\]

not `p^{-1/2}`. The child then uses target `2/p` and score `1/p`; the unused target `2(p^{-1/2}-p^{-1})` remains positive current-generation slack. This exactly explains and repairs the review counterexample.

## 4. Substochastic scalar ledger

From (L-91354.3),

\[
\boxed{
\sum_j\alpha_j
\le\sum_jh_j^X\le1
}
\tag{L-91354.9}
\]

and likewise through the `Y` ledger. Thus the canonical children have honest scalar coefficients with total at most one.

Each child is placed at endpoint `X/p_j`; since every rough prime is at least `67`,

\[
\boxed{
X/p_j<c_0X.
}
\tag{L-91354.10}
\]

Consequently the extracted children satisfy the exact scalar and scale hypotheses of a substochastic branching consumer. The coefficients are derived from the hidden measure partition; they are not source-mass guesses.

## 5. Aggregate residual

Let

\[
\Theta=\sum_j\alpha_j.
\]

Summing (L-91354.6) together with the survival term gives the positive hidden residual

\[
\boxed{
Q_\infty I(s)+\sum_j[H_jI(s)-\alpha_jI(s)]
\ge0.
}
\tag{L-91354.11}
\]

At the level of the two positive hidden ledgers, the children consume exactly the scalar fraction `Theta`, while all unused target and score remain in the current generation.

## 6. What is repaired

The literal inference rejected by PR #431 was

```text
hidden hazard branch = p^(-1/2) times a native child + positive rest.
```

The correct statement is

```text
hidden hazard branch contains min(h_X,h_Y) times a native child;
the remainder is a positive hidden packet;
the child coefficients are substochastic.
```

This also supplies a mathematically defined scalar coefficient for each child and therefore removes the normalization ambiguity in `T-91304` at the hidden-source level.

## 7. Remaining physical theorem

The residual in (L-91354.11) is positive in hidden coordinates but is not automatically a standard endpoint packet after the signed observation `J`. To finish the route one must prove a positive physical realization, or a bounded-loss discard theorem, for these residual hidden packets in every row/detail/port coordinate.

Combined with the measure-valued consumer `T-91305`, it is sufficient to establish

\[
\mathcal V_X(\rho)
\le C\,m_X(\rho)
\]

for the residual packet class with a uniformly bounded native mass.

```text
safe canonical child inside every hazard      EXACT
pure-reserve review obstruction                REPAIRED WITH alpha=1/p
scalar child coefficients                      EXACT
sum of coefficients <=1                        EXACT
child endpoint contraction                     EXACT
positive hidden residual                       EXACT
physical residual row/capacity typing          OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
