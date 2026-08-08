# L-30504 — Dyadic decomposition of the unresolved analytic tail

Claim ID: `L-30504`  
Title: The infinite negative central tail splits exactly into a half-scale lifted tail and the odd-divisor commutator of the dyadic Cycle-Debt normal form  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30503`; PR #272 adjacent-tree identities  
Scope: exact formal/carry-load identity for the analytic tail; no quantitative debt bound

Let

\[
p_n=n^{-1/2},
\qquad
a_n=p_n-p_{n+1}>0,
\]

and let

\[
h_n=[n,\lfloor n/2\rfloor]
\]

be the central split edge. Define the positive analytic tail flow

\[
\boxed{
F_N=\sum_{n\ge N}a_nh_n.
}
\tag{L-30504.1}

The sum is interpreted through its carry loads; each fixed carry column is an absolutely convergent paired series.

Let

\[
E_r=T_{r+1}-T_r
\]

be the adjacent central-tree commutator, and let the dyadic lift satisfy

\[
L_2h_m=h_{2m}.
\]

## 1. Exact pairing of consecutive rows

PR #272 gives

\[
\boxed{
h_{2m+1}-h_{2m}=E_{2m}-E_m.}
\tag{L-30504.2}

Also

\[
\begin{aligned}
a_{2m}+a_{2m+1}
&=p_{2m}-p_{2m+2}\\
&=2^{-1/2}(p_m-p_{m+1})\\
&=2^{-1/2}a_m.
\end{aligned}
\tag{L-30504.3}

Therefore

\[
\begin{aligned}
a_{2m}h_{2m}+a_{2m+1}h_{2m+1}
={}&2^{-1/2}a_mh_{2m}\\
&+a_{2m+1}(E_{2m}-E_m).
\end{aligned}
\tag{L-30504.4}

## 2. Even-endpoint tail identity

Summing (L-30504.4) for `m>=M` gives

\[
\boxed{
F_{2M}
=2^{-1/2}L_2F_M
+\sum_{m\ge M}a_{2m+1}(E_{2m}-E_m).
}
\tag{L-30504.5}

This is an exact flow identity in every finite carry column.

For an odd starting point,

\[
\boxed{
F_{2M+1}=F_{2M}-a_{2M}h_{2M}.
}
\tag{L-30504.6}

Thus parity contributes only one explicit finite collar edge.

## 3. Divisor-source form of the commutator

The adjacent-tree identity is

\[
L_q(E_r)=\mathbf1_{q\mid r+1}.
\]

Hence the second term of (L-30504.5) has exact carry load

\[
\boxed{
\sum_{m\ge M}a_{2m+1}
\left[
\mathbf1_{q\mid 2m+1}
-\mathbf1_{q\mid m+1}
\right].
}
\tag{L-30504.7}

This is precisely an odd-column divisor commutator: the current-scale odd destination `2m+1` is paired with the strict half-scale destination `m+1` before any norm is taken.

## 4. Consequence for the PR #304 repair

`L-30503` proves that the aggregate boundary rows below `X` already have only `O(log^2 X)` negative capacity. The unresolved part is `-log(X)F_X`.

Equation (L-30504.5) shows that this tail is not a new unrelated source. It is exactly:

```text
one stable dyadic lift of the same tail at half scale
+
one odd-divisor commutator
+
one finite parity collar when X is odd.
```

This is the same algebraic state as PR #272's Dyadic Commutator Debt. A repaired proof must estimate the **paired** source (L-30504.7), not its two divisor legs separately and not the atomic norm of their difference after Möbius inversion.

## 5. Proof boundary

Closed exactly:

1. the consecutive-row pairing;
2. exact square-root dyadic scaling;
3. the even- and odd-endpoint tail formulas;
4. identification of the residual as the existing odd-divisor commutator.

Open:

1. a polylogarithmic cycle-optimized bound for the all-scale paired commutator;
2. the complete Cycle-Debt estimate;
3. RH.
