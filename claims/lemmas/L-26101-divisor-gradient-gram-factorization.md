# L-26101 — Exact divisor-gradient Gram factorization

Claim ID: `L-26101`  
Title: Adjacent carry flows are divisor-gradient Gram corrections, and highly composite collectors are exact superpositions of divisor atoms  
Status: **PROPOSED COMPLETE EXACT FINITE ALGEBRA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: PR #254 `L-25301`; PR #248 `L-24501/L-24502`  
Scope: finite elementary algebra; no asymptotic estimate and no RH claim

## 1. Divisor gradients

For integers `d>=2` and `m>=2`, define

\[
 g_d(m)=\mathbf 1_{d\mid m}-\mathbf 1_{d\mid m-1}.
 \tag{L-26101.1}
\]

The prime-power carry constraint in the second-difference coordinate is

\[
 v_q(b)=\sum_{m=2}^{X}b_m g_q(m),
 \qquad q=p^a\le X.
 \tag{L-26101.2}
\]

Thus `g_q` is the exact constraint row, not a model or a continuum approximation.

## 2. Divisor-comb flows

Let `D` be any finite set of integers at least two and let `a_d` be real amplitudes. Put

\[
 F_a(j)=\sum_{\substack{d\in D\\d\mid j}}a_d,
 \qquad 1\le j\le X,
 \tag{L-26101.3}
\]

and use the adjacent-flow correction

\[
 b_a(m)=b^{(0)}_X(m)+F_a(m-1)-F_a(m).
 \tag{L-26101.4}
\]

Then

\[
\boxed{
 F_a(m-1)-F_a(m)
 =-\sum_{d\in D}a_d g_d(m).
}
\tag{L-26101.5}
\]

Consequently, with the rectangular Gram

\[
 K_X(q,d)=\sum_{m=2}^{X}g_q(m)g_d(m),
 \tag{L-26101.6}
\]

one has the exact constraint update

\[
\boxed{
 v_q(b_a)-v_q(b^{(0)}_X)
 =-\sum_{d\in D}K_X(q,d)a_d.
}
\tag{L-26101.7}
\]

No divisor multiplicity has been bounded or discarded. A large value of `F_a(j)` at a highly composite `j` is literally the superposition of all active divisor amplitudes at `j`. This explains the collector pattern seen in the top-annulus reconnaissance without importing a heuristic notion of “highly composite efficiency.”

## 3. Prime-power square Gram

If `D` is the complete prime-power set

\[
 \mathcal Q_X=\{p^a:p^a\le X\},
\]

write `G_X=(g_q(m))` and

\[
 K_X=G_XG_X^*.
 \tag{L-26101.8}
\]

Then `K_X` is positive semidefinite and

\[
\boxed{
 v(b_a)-v(b^{(0)}_X)=-K_Xa.
}
\tag{L-26101.9}
\]

Exact product collisions in this coordinate are simply identical divisor-gradient rows. They must be compressed by keeping the strongest residual constraint; deleting one arbitrarily is not valid.

## 4. Objective identity

Put

\[
 \ell_m=\log\frac m{m-1}.
\]

The prime-power von-Mangoldt identity gives, as a formal prime-log equality,

\[
\boxed{
 \ell_m
 =\sum_{q=p^a\le X}\Lambda(q)g_q(m).
}
\tag{L-26101.10}
\]

Indeed, the right side is `log m-log(m-1)`. Therefore

\[
 J_X(b)=\sum_{m=2}^{X}b_m\ell_m
 =\sum_{q=p^a\le X}\Lambda(q)v_q(b).
 \tag{L-26101.11}
\]

For the divisor-comb correction,

\[
\boxed{
 J_X(b^{(0)}_X)-J_X(b_a)
 =\sum_{d\in D}a_d
   \sum_{q=p^a\le X}K_X(q,d)\Lambda(q).
}
\tag{L-26101.12}
\]

For direct adjacent-flow coordinates this is the already known exact formula

\[
 J_X(b^{(0)}_X)-J_X(b_F)
 =\sum_jF_j\log\frac{j^2}{j^2-1}.
 \tag{L-26101.13}
\]

Thus the small `j^{-2}` transport price and the von-Mangoldt constraint charge are two forms of one exact identity.

## 5. Annular divisor-gradient matrix

Fix one interior annulus

\[
 I_X=[\lceil\alpha X\rceil,\lfloor\beta X\rfloor],
 \qquad 0<\alpha<\beta<1.
\]

For prime powers `q` and `j in I_X`, define

\[
\boxed{
 A_X(q,j)
 =2\mathbf 1_{q\mid j}
 -\mathbf 1_{q\mid j-1}
 -\mathbf 1_{q\mid j+1}.
}
\tag{L-26101.14}
\]

If a real flow `F` is supported on `I_X`, then

\[
\boxed{
 v_q(b_F)-v_q(b^{(0)}_X)=-(A_XF)_q.
}
\tag{L-26101.15}
\]

The column formula

\[
 (A_X^*y)_j
 =2\sum_{q\mid j}y_q
 -\sum_{q\mid j-1}y_q
 -\sum_{q\mid j+1}y_q
 \tag{L-26101.16}
\]

shows exactly why minimum-norm or dual-gradient repairs concentrate at integers with many active prime-power divisors while using their neighbors as discharge channels.

## 6. Proof boundary

Proved in this file:

- the divisor-gradient/cumulative-flow identity;
- the rectangular and square Gram formulas;
- the exact objective duality;
- the annular prime-power matrix and its adjoint.

Not proved here:

- a uniform lower frame bound for the source-generated active rows;
- contraction of leakage into inactive prime-power rows;
- existence of a cofinal low-norm annular repair;
- RH.
