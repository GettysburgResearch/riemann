# L-30104 — Top-half adjacent-commutator debt is bounded

Claim ID: `L-30104`  
Title: Every parity dipole whose parent-`4k` sibling switch escapes endpoint `2Y` can be realized by the legal adjacent-tree commutator with total negative capacity debt bounded absolutely for the critical target  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27205/L-27207`; critical target `w_X(q)=q^(-1/2)log(X/q)`  
Scope: the top-half support family isolated in `R-30102`; no claim on the remaining lower-half source and no RH conclusion

## 1. Exact top-half divergence

Let

\[
X=2Y,
\qquad
w_X(q)=q^{-1/2}\log(X/q),
\qquad
2\le q\le X.
\tag{L-30104.1}
\]

Retain PR #272's Möbius divergence

\[
u_X(m)=\sum_{d\le X/m}\mu(d)w_X(md),
\qquad
r_X(m)=u_X(m)-u_X(m+1).
\tag{L-30104.2}

If

\[
Y<m<X,
\]

then `X/m<2`, so only `d=1` occurs. The same is true at `m+1`. Therefore

\[
\boxed{
 r_X(m)=w_X(m)-w_X(m+1)>0
 \qquad(Y<m<X).
}
\tag{L-30104.3}

Thus every odd-node coefficient in the top half is completely elementary; no Möbius cancellation remains there.

## 2. Capacity debt of one adjacent-tree commutator

Let

\[
E_n=T_{n+1}-T_n
\]

be the legal adjacent-tree commutator of PR #272. Its sparse recursion is

\[
E_{2m}=[2m+1,m]-[2m,m]+E_m,
\tag{L-30104.4}
\]

\[
E_{2m+1}=[2m+2,m+1]-[2m+1,m]+E_m.
\tag{L-30104.5}

For every balanced edge with parent `n`, PR #272's capacity weight obeys

\[
\omega_e\le2\sqrt n.
\tag{L-30104.6}

Put

\[
D(n)=\mathcal N_\omega(E_n),
\]

the negative capacity debt of the displayed signed commutator. Equations (L-30104.4)–(L-30104.6) give

\[
D(n)
\le2\sqrt n+D(\lfloor n/2\rfloor).
\tag{L-30104.7}

Since `E_1=[2,1]` is nonnegative, `D(1)=0`. Iterating (L-30104.7),

\[
\boxed{
D(n)
\le
C_0\sqrt n,
\qquad
C_0={2\over1-2^{-1/2}}.
}
\tag{L-30104.8}

There is no logarithmic loss: the binary scales form a geometric square-root series.

## 3. Critical first-difference bound

For the real function

\[
w_X(t)=t^{-1/2}\log(X/t),
\]

one has

\[
-w_X'(t)
=t^{-3/2}
\left(1+{1\over2}\log(X/t)\right).
\tag{L-30104.9}

When `t>=X/2`,

\[
1+{1\over2}\log(X/t)
\le
C_1:=1+{1\over2}\log2.
\tag{L-30104.10}

Hence, for `X/2<m<X`,

\[
\boxed{
0<r_X(m)
\le
C_1m^{-3/2}.
}
\tag{L-30104.11
}

The closing bracket in the equation tag is typographical only.

## 4. Complete escaped-family debt

The parent-`4k` switch of PR #301 is outside endpoint `X=2Y` precisely when

\[
k>Y/2.
\]

For this family, `m=2k+1` lies above `X/2`. Use the legal in-endpoint flow

\[
r_X(2k+1)E_{2k}
\]

instead. Since the coefficient is positive, its negative capacity debt is

\[
r_X(2k+1)D(2k).
\]

Equations (L-30104.8) and (L-30104.11) give

\[
\begin{aligned}
\sum_{Y/2<k<Y}
 r_X(2k+1)D(2k)
&\le
C_0C_1
\sum_{Y/2<k<Y}
{\sqrt{2k}\over(2k+1)^{3/2}}\\
&\le
C_0C_1
\sum_{Y/2<k<Y}{1\over2k}.
\end{aligned}
\tag{L-30104.12}

Therefore

\[
\boxed{
\sum_{Y/2<k<Y}
\mathcal N_\omega\bigl(r_X(2k+1)E_{2k}\bigr)
\le
C_2,
}
\tag{L-30104.13]

where one may take, for example,

\[
C_2=C_0C_1(1+\log2).
\]

The bound is absolute and uniform in `X`.

## 5. Consequence for the PR #301 support defect

`R-30102` proves that the nonnegative parent-`4k` sibling realization is inadmissible for the complete top half. The present theorem supplies an exact legal replacement:

```text
top-half parity dipole
-> signed adjacent-tree commutator E_(2k)
-> absolute total negative capacity debt O(1).
```

Thus the support defect does **not** regenerate an RH-sized error. It belongs to the finite/polylogarithmic collar budget.

This result is stronger than bounding each escaped commutator by `O(log X)`: the entire top-half family costs only `O(1)` in the Cycle-Debt metric.

## 6. Remaining frontier

This theorem closes only the escaped top-half family. A complete proof still needs an exact source-module construction for the lower half

\[
1\le k\le Y/2,
\]

where the parent-`4k` switch is admissible but the submitted pairing-first Euler transform is invalid by `R-30101`.

The corrected Euler-first scalar positivity theorem is `L-30103`. What remains is to bind its finite jets and exact remainder to the lower-half divisor-source/Pascal module without changing their arithmetic labels.

No RH conclusion is claimed here.
