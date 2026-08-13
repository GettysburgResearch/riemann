# T-90011 — A subquadratic complete prime-power parabolic gap is equivalent to RH

Claim ID: `T-90011` (provisional branch range)  
Title: The Riemann Hypothesis is equivalent to the deterministic parabolic entropy score matching the complete prime-power ramp to `o(log^2 X)`; no eventual sign is required  
Status: **PROPOSED COMPLETE RH-EQUIVALENCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #352 `T-90008`; `L-90020/L-90021`  
Scope: full Riemann Hypothesis; the subquadratic estimate itself remains unproved

## 1. Complete parabolic gap

Retain

\[
 F_\Lambda(X)
 =\sum_{q\le X}\Lambda(q)r_X(q).
\tag{T-90011.1}
\]

By `L-90021`, this is exactly

\[
\boxed{
 F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X),
}
\tag{T-90011.2}
\]

where

\[
 J_\Lambda(X)
 =\sum_{m=2}^Xb_X(m)\log\frac m{m-1}
\tag{T-90011.3}
\]

is the deterministic score of the nonnegative parabolic carry-row seed, and

\[
 P_\Lambda(X)
 =\sum_{q\le X}{\Lambda(q)\over\sqrt q}
  \log{X\over q}
\tag{T-90011.4}
\]

is the complete prime-power ramp.

Let

\[
 A(X)=\sum_{p\le X}(\log p)r_X(p)
\]

be the prime-only endpoint of PR #352, and put

\[
 H(X)=F_\Lambda(X)-A(X).
\tag{T-90011.5}
\]

Thus `H` is exactly the higher-prime-power residual.

## 2. Prime-square drift

`L-90020` proves unconditionally that

\[
\boxed{
 H(X)={C_{\rm pp}\over4}\log^2X+o(\log^2X),
 \qquad
 C_{\rm pp}=-1-\zeta(1/2)>0.
}
\tag{T-90011.6}

The coefficient comes from the positive prime-square occupancy source

\[
 \mathcal Q_{\rm pp}(t)\longrightarrow C_{\rm pp}.
\]

Equivalently,

\[
\boxed{
 A(X)=F_\Lambda(X)-{C_{\rm pp}\over4}\log^2X
      +o(\log^2X).
}
\tag{T-90011.7}

This identity is unconditional.

## 3. Subquadratic gap implies RH

Assume

\[
\boxed{
 F_\Lambda(X)=o(\log^2X).
}
\tag{T-90011.8}

Then (T-90011.7) gives

\[
 A(X)
 =-{C_{\rm pp}\over4}\log^2X+o(\log^2X)<0
\]

for every sufficiently large `X`.

PR #352 `T-90008` proves that eventual negativity, indeed eventual one-sidedness, of `A` implies RH. Therefore

\[
\boxed{
 F_\Lambda(X)=o(\log^2X)
 \Longrightarrow\mathrm{RH}.
}
\tag{T-90011.9}

No one-sided estimate for `F_Lambda` is used.

## 4. RH implies the subquadratic gap

Assume RH. `T-90008` gives

\[
\boxed{
 A(X)
 =-{C_{\rm pp}\over4}\log^2X+O(\log X),
}
\tag{T-90011.10}

where the critical-line zero series is absolutely and uniformly bounded after the two Riesz integrations.

Combining (T-90011.10) with the unconditional asymptotic (T-90011.6),

\[
 F_\Lambda(X)=A(X)+H(X)=o(\log^2X).
\tag{T-90011.11}
\]

Hence

\[
\boxed{
 \mathrm{RH}
 \Longrightarrow
 F_\Lambda(X)=o(\log^2X).
}
\tag{T-90011.12}

Sections 3--4 prove

\[
\boxed{
 \mathrm{RH}
 \iff
 F_\Lambda(X)=o(\log^2X)
 \iff
 J_\Lambda(X)-P_\Lambda(X)=o(\log^2X).
}
\tag{T-90011.13}

## 5. One-sided threshold versions

The full little-`o` statement is not needed for the converse. Equation (T-90011.7) shows that any fixed strict upper margin

\[
\boxed{
 \limsup_{X\to\infty}
 {F_\Lambda(X)\over\log^2X}
 <{C_{\rm pp}\over4}
}
\tag{T-90011.14}

already implies eventual negativity of `A` and hence RH.

In particular, each of the following is sufficient:

\[
 F_\Lambda(X)=O(\log^{2-\delta}X)
 \quad(\delta>0),
\tag{T-90011.15}
\]

or

\[
 F_\Lambda(X)\le0
\]

eventually.

Under RH the normalized ratio in (T-90011.14) tends to zero.

## 6. Relation to the elementary carry programme

The parabolic seed is already a nonnegative carry-row object by PR #265 `L-26201`. Its score is `J_Lambda`. The complete prime-power ramp `P_Lambda` is the exact von-Mangoldt dual value of its column responses.

Therefore the full RH problem may now be stated as:

> prove that one explicit positive parabolic packing has complete von-Mangoldt dual gap `o(log^2 X)`.

This is weaker than constructing an exactly feasible packing with polylogarithmic slack and weaker than an eventual sign theorem for the complete gap. It allows arbitrary local overfill and underfill, provided their source-matched complete-prime-power aggregate is subquadratic in logarithmic scale.

The positive renewal of `L-90021` supplies an exact finite-state coordinate for this gap. Selberg/Kummer, Green/Skorokhod, Gamma/Pascal, or endpoint-scale methods can now be judged by whether they prove (T-90011.8), rather than by whether they close a stronger intermediate cone theorem.

## 7. Proof boundary

Closed, subject to review:

1. the exact parabolic-score/prime-ramp gap identity;
2. the unconditional prime-square asymptotic separating `A` and `F_Lambda`;
3. subquadratic complete gap implies endpoint negativity and RH;
4. RH implies the subquadratic complete gap;
5. the exact equivalence (T-90011.13);
6. the weaker one-sided threshold criterion.

Open:

1. the estimate `F_Lambda=o(log^2X)`;
2. a positive-renewal or carry proof of that estimate;
3. RH.