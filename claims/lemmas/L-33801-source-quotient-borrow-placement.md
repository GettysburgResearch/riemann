# L-33801 — Source–quotient placement with one exact borrow term

Claim ID: `L-33801`  
Title: Every source-convolved physical prefix defect decomposes exactly into quotient-row defects plus one floor-borrow increment; for Q=4 this places the true pole current into lower quotient Kummer rows without source mistyping  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 corrected Q=4 physical coefficient `c_4=e_4*Lambda_4`; elementary Dirichlet convolution and floor arithmetic  
Scope: exact integer-row placement; no sign, norm, independent-frequency polarization, or RH conclusion

## 1. General prefix source identity

Let `b,g` be finite real or complex arithmetic sequences and put

\[
 c=b*g.
\]

For `N>=0` define prefix sums

\[
 A_g(N)=\sum_{m\le N}g(m),
 \qquad
 G_c(N)=\sum_{m\le N}c(m),
\]

with both prefixes zero at `N=0`.

Finite divisor switching gives exactly

\[
\boxed{
 G_c(N)=\sum_{d\le N}b(d)A_g\!\left(\left\lfloor\frac Nd\right\rfloor\right).
}
\tag{L-33801.1}
\]

Fix a split

\[
 n=j+k,
 \qquad 1\le j<n,
\]

and for every `d<=n` put

\[
 N_d=\left\lfloor\frac nd\right\rfloor,
 \quad
 J_d=\left\lfloor\frac jd\right\rfloor,
 \quad
 K_d=\left\lfloor\frac kd\right\rfloor.
\]

Then the physical prefix defect

\[
 Q_{b,g}(n,j)=G_c(n)-G_c(j)-G_c(k)
\]

has the exact source–quotient placement

\[
\boxed{
 Q_{b,g}(n,j)
 =\sum_{d\le n}b(d)
 \bigl[A_g(N_d)-A_g(J_d)-A_g(K_d)\bigr].
}
\tag{L-33801.2}
\]

No approximation or positivity assertion is involved.

## 2. The floor borrow is only zero or one

Define

\[
 \varepsilon_d
 =N_d-J_d-K_d.
\]

Since `n=j+k`, elementary floor arithmetic gives

\[
\boxed{
 \varepsilon_d
 =\chi_{n,d}(j)
 \in\{0,1\}.
}
\tag{L-33801.3}
\]

Equivalently,

\[
 K_d=N_d-J_d-\varepsilon_d.
\]

Thus every source scale has exactly two cases: an exact quotient split or one unit of floor borrow.

## 3. Kummer specialization

Assume now that

\[
 g=\mathbf1*\lambda,
\]

where `1(n)=1`. Define the ordinary carry/Kummer row associated with `lambda` by

\[
 P_\lambda(N,J)
 =\sum_{q\le N}\lambda(q)\chi_{N,q}(J).
\]

Because

\[
 P_\lambda(N,J)
 =A_g(N)-A_g(J)-A_g(N-J),
\]

equation (L-33801.3) gives, source by source,

\[
\boxed{
 A_g(N_d)-A_g(J_d)-A_g(K_d)
 =P_\lambda(N_d,J_d)
  +\varepsilon_d\,g(N_d-J_d).
}
\tag{L-33801.4}
\]

Therefore

\[
\boxed{
 Q_{b,\mathbf1*\lambda}(n,j)
 =\sum_{d\le n}b(d)
 \left[
 P_\lambda(N_d,J_d)
 +\chi_{n,d}(j)\,(\mathbf1*\lambda)(N_d-J_d)
 \right].
}
\tag{L-33801.5}
\]

This is the promised quotient-row plus borrow decomposition. The second term is not a vague endpoint error: its source scale, carry indicator, and exact arithmetic destination are written explicitly.

## 4. Q=4 true physical current

Retain the Q=4 Euler–Blaschke system

\[
 b_4=\mu*e_4,
 \qquad
 (\mathbf1*b_4)=e_4,
\]

and generalized-prime sequence `Lambda_4`. The correctly typed physical coefficient is

\[
 c_4=e_4*\Lambda_4.
\]

Associativity gives

\[
\boxed{
 c_4
 =b_4*(\mathbf1*\Lambda_4).
}
\tag{L-33801.6}
\]

Thus corrected PR #325 / PR #337 physical field

\[
 Q_4^{\rm phys}(n,j)
 =G_4(n)-G_4(j)-G_4(n-j)
\]

is exactly (L-33801.5) with `b=b_4` and `lambda=Lambda_4`:

\[
\boxed{
\begin{aligned}
 Q_4^{\rm phys}(n,j)
 =\sum_{d\le n}b_4(d)
 \Bigl[
 &P_4(N_d,J_d)\\
 &+\chi_{n,d}(j)\,H_4(N_d-J_d)
 \Bigr],
\end{aligned}
}
\tag{L-33801.7}
\]

where

\[
 H_4(m)=(\mathbf1*\Lambda_4)(m).
\]

This is an exact source placement of the pole-preserving physical current into lower quotient generalized-Kummer rows plus one explicit borrow ledger.

## 5. The borrow coefficient is elementary and positive

From the Q=4 generalized-prime formula,

\[
 \Lambda_4
 =\Lambda
 +(\log4)\sum_{r\ge1}(4^r-1)\delta_{4^r},
\]

so divisor summation yields

\[
\boxed{
 H_4(m)
 =\log m
 +(\log4)
 \sum_{1\le r\le v_4(m)}(4^r-1)
 \ge0.
}
\tag{L-33801.8}
\]

Here `v_4(m)=max{r:4^r|m}`. Hence all sign difficulty in (L-33801.7) is carried by the declared inverse-source coefficient `b_4(d)`; no additional hidden sign is introduced by the floor borrow.

## 6. Why this is a real placement advance

Several earlier failed source-to-carry steps replaced an arithmetic source label by a quotient label or silently ignored the one-unit floor mismatch. Equation (L-33801.7) does neither.

It records simultaneously:

```text
physical source scale d;
quotient parent N_d;
quotient child J_d;
carry/borrow indicator chi_(n,d)(j);
exact Kummer row P_4(N_d,J_d);
exact positive borrow coefficient H_4(N_d-J_d).
```

Thus the integer physical-current placement problem is no longer an unspecified map. Any future reserve argument can be audited source by source.

The identity does **not** remove the Möbius signs in `b_4`, and it does not by itself polarize the independent-frequency reflected block. Those are separate conclusion-producing steps.

## 7. Proof boundary

Closed exactly:

1. finite source-prefix switching;
2. zero/one quotient borrow;
3. Kummer specialization;
4. exact Q=4 physical-current placement;
5. explicit positive Q=4 borrow coefficient.

Open:

1. signed recombination of the complete `b_4(d)` source before norms;
2. independent-frequency/Hermitian polarization of the quotient ledger;
3. coefficient-one neutral recurrence;
4. RH.
