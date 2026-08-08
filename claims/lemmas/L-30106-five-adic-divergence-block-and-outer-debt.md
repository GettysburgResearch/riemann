# L-30106 — Five-adic divergence blocks and bounded outer debt

Claim ID: `L-30106`  
Title: The critical Möbius divergence at endpoint `5Y` is a scaled lower divergence plus four adjacent commutators per block; all blocks above the lower endpoint have nonnegative coefficients and absolute total capacity debt `O(1)`  
Status: **PROPOSED COMPLETE EXACT/elementary THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30105`; PR #272 adjacent-tree commutators and capacity weights  
Scope: exact five-adic source decomposition and complete outer-family debt; the inner factor-five source remains to be recursively paired

## 1. Critical Möbius divergence

Let

\[
X=5Y,
\qquad
w_X(q)=q^{-1/2}\log(X/q),
\]

and define

\[
u_X(m)=\sum_{d\le X/m}\mu(d)w_X(md),
\qquad
r_X(m)=u_X(m)-u_X(m+1).
\tag{L-30106.1}

For the lower endpoint `Y`, define `u_Y,r_Y` in the same way.

The target scales exactly on multiples of five:

\[
w_X(5n)=5^{-1/2}w_Y(n).
\tag{L-30106.2}

Therefore

\[
\boxed{
u_X(5a)=5^{-1/2}u_Y(a)
}
\tag{L-30106.3]

and

\[
\boxed{
\sum_{j=0}^{4}r_X(5a+j)
=5^{-1/2}r_Y(a).
}
\tag{L-30106.4]

The closing brackets in two equation tags are typographical only.

## 2. Exact block dipole decomposition

For `j=1,2,3,4`, put

\[
\boxed{
c_{a,j}
=u_X(5a+j)-u_X(5a+5)
=\sum_{\ell=j}^{4}r_X(5a+\ell).
}
\tag{L-30106.5}

Then the complete five-node block satisfies

\[
\boxed{
\begin{aligned}
\sum_{j=0}^{4}r_X(5a+j)e_{5a+j}
={}&5^{-1/2}r_Y(a)e_{5a}\\
&+\sum_{j=1}^{4}c_{a,j}
 (e_{5a+j}-e_{5a+j-1}).
\end{aligned}}
\tag{L-30106.6}

Indeed the coefficient at `5a` is

\[
5^{-1/2}r_Y(a)-c_{a,1}=r_X(5a),
\]

while the coefficient at `5a+j`, `1<=j<4`, is `c_(a,j)-c_(a,j+1)=r_X(5a+j)`, and the last coefficient is `c_(a,4)=r_X(5a+4)`.

Thus the exact node source is a five-fold lower-scale lift plus adjacent dipoles. No asymptotic estimate enters.

## 3. Legal adjacent-tree flow

PR #272 defines

\[
E_n=T_{n+1}-T_n,
\qquad
\partial E_n=e_{n+1}-e_n-e_1.
\tag{L-30106.7}

Modulo the unique root coefficient forced by the size-zero condition, equation (L-30106.6) is realized by

\[
\boxed{
5^{-1/2}\mathcal L_5 d_Y
+
\sum_{a}\sum_{j=1}^{4}c_{a,j}E_{5a+j-1},
}
\tag{L-30106.8}

where `d_Y` is any exact lower flow and `mathcal L_5` multiplies every parent and child label by five. The finite bottom block supplies the omitted root charge exactly, as in the dyadic normal form.

Every commutator in (L-30106.8) is `1/4`-balanced and legal.

## 4. Positivity of every outer coefficient

Assume

\[
a>Y/5.
\]

Then

\[
5a+j>Y=X/5
\qquad(1\le j\le4),
\]

and the complete interval `[5a+j,5a+5]` lies in the monotonicity region of `L-30105`. Hence

\[
\boxed{
c_{a,j}\ge0
\qquad(a>Y/5,\ 1\le j\le4).
}
\tag{L-30106.9}

So every outer five-adic block is a positive combination of legal adjacent-tree commutators.

## 5. Uniform derivative bound on the outer region

The quotient-cell proof of `L-30105` gives, for `Y<t<5Y`,

\[
0<-u_X'(t)
\le C_3t^{-3/2},
\tag{L-30106.10}

where `C_3` is absolute: only the fixed terms `d=1,2,3` occur and `log(X/t)<=log5`.

Consequently

\[
\boxed{
0\le c_{a,j}
\le C_3(5-j)(5a+j)^{-3/2}.
}
\tag{L-30106.11}

## 6. Absolute total outer capacity debt

Let

\[
D(n)=\mathcal N_\omega(E_n).
\]

The sparse binary recursion of PR #272 gives

\[
D(n)\le C_0\sqrt n,
\qquad
C_0={2\over1-2^{-1/2}}.
\tag{L-30106.12}

Therefore the complete outer commutator family has negative capacity debt at most

\[
\begin{aligned}
\sum_{Y/5<a<Y}
\sum_{j=1}^{4}c_{a,j}D(5a+j-1)
&\le C_4
\sum_{Y/5<a<Y}{1\over a}\\
&\le C_4(1+\log5).
\end{aligned}
\tag{L-30106.13}

Thus

\[
\boxed{
\mathcal N_\omega(Q_{\rm outer})=O(1)
}
\tag{L-30106.14]

uniformly in `X`. The closing bracket in the tag is typographical only.

This estimate includes both the parent-`4k` support-escape family of `R-30102` and the legal middle family. No nonnegative sibling capacity is assumed.

## 7. Exact location of the remaining source

If

\[
a\le {Y-4\over5},
\]

then every parent in the corresponding commutators obeys

\[
5a+j-1\le Y
\qquad(1\le j\le4).
\]

Hence the complete remaining source is already supported in the lower endpoint `Y=X/5`. Only at most four terminal block rows straddle `Y`; they form an absolute finite collar.

The five-adic decomposition therefore has the fail-closed form

```text
endpoint X=5Y source
 = 5^(-1/2) lifted critical lower source
   + in-endpoint factor-five source supported through Y
   + O(1)-debt outer commutators
   + finite bottom/cutoff collar.
```

All source rank above the lower endpoint has been eliminated exactly.

## 8. Capacity scaling of the five-fold lift

For an edge `e=[n,j]`, let `5e=[5n,5j]`. Its columns divisible by five satisfy the pointwise carry identity

\[
\chi_{5e}(5q)=\chi_e(q).
\]

Therefore

\[
\omega_{5e}
=5^{-1/2}\omega_e+\omega_{\not\equiv0(5)}(5e).
\tag{L-30106.15}

Multiplying the lifted flow by the target factor `5^(-1/2)` gives the exact main debt contribution

\[
\boxed{
{1\over5}\mathcal N_\omega(d_Y)
}
\tag{L-30106.16]

plus a nonmultiple-column leakage. The complete residual commutator family in (L-30106.8) is the source that must be paired with that leakage before absolute values. The outer portion costs only `O(1)` by (L-30106.14); the remaining paired excess is supported through `Y`.

## 9. Corrected proof frontier

This theorem closes:

1. the exact five-adic divergence block identity;
2. the lower-source scaling factor `5^(-1/2)`;
3. legal adjacent-tree realization of every block residual;
4. positivity of every coefficient above the lower endpoint;
5. an absolute `O(1)` debt bound for the complete outer family;
6. confinement of every remaining source and nonmultiple leakage to endpoint `Y=X/5`;
7. the exact factor `1/5` on the lifted lower debt.

A complete RH proof still requires the final **in-endpoint pairing theorem**:

```text
five-lift nonmultiple leakage
+
inner factor-five commutators supported through Y
-> one lower-endpoint flow state
   with no fixed positive debt amplification.
```

Unlike the frozen PR #301 hinge, this is now a finite source-supported statement at strict scale `X/5`; no common infinite tail or out-of-endpoint parent remains.

No RH conclusion is claimed in this lemma.
