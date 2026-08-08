# L-30701 — The outer stopped boundary has an exact nonnegative central-step realization

Claim ID: `L-30701`  
Title: The critical stopped boundary is positive and decreasing on its complete outer transition band, hence that band is realized exactly by nonnegative central carry rows  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #307  
Dependencies: `R-30701`; the exact central carry pattern  
Scope: one outer band; lower-band leakage remains coupled and is not estimated here

## 1. The positive tail function

On the range

\[
\frac{X}{3}<q\le\frac{X+1}{2},
\]

only the first positive term occurs in the finite stopped sum. Put

\[
A(q)
=(2q-1)^{-1/2}-(\mathcal Cp)(q).
\]

As in `R-30701`,

\[
\boxed{
A(q)=\sum_{r\ge1}
\left[
((2r+1)q)^{-1/2}
-((2r+2)q-1)^{-1/2}
\right].
}
\tag{L-30701.1}
\]

Every summand is positive.

## 2. Every pair is decreasing

Fix an integer `a>=3` and define

\[
g_a(q)=(aq)^{-1/2}-((a+1)q-1)^{-1/2}.
\]

Then

\[
g_a'(q)
=\frac12\left[
-\frac1{\sqrt a\,q^{3/2}}
+\frac{a+1}{((a+1)q-1)^{3/2}}
\right].
\]

It is enough to prove

\[
1-\frac1{(a+1)q}>
\left(\frac a{a+1}\right)^{1/3}.
\tag{L-30701.2}
\]

For `q>=4`,

\[
1-\frac1{(a+1)q}
\ge1-\frac1{4(a+1)}.
\]

Concavity of `x^(1/3)` gives

\[
\left(1-\frac1{a+1}\right)^{1/3}
\le1-\frac1{3(a+1)}.
\]

The first right-hand side is strictly larger than the second. Therefore

\[
\boxed{g_a'(q)<0\qquad(q\ge4).}
\tag{L-30701.3}
\]

Termwise monotone convergence in (L-30701.1) now gives

\[
\boxed{A(q)>0\quad\text{and}\quad A'(q)<0.}
\tag{L-30701.4}
\]

## 3. Monotonicity of the complete outer boundary

For `q>X/3`,

\[
P_X(q)
=\log\frac{X}{2q-1}\,A(q).
\tag{L-30701.5}
\]

Both factors are positive and decreasing for

\[
4\le q\le\frac{X+1}{2}.
\]

Hence

\[
\boxed{
P_X(q)>0,
\qquad
P_X(q)-P_X(q+1)\ge0
}
\tag{L-30701.6}
\]

throughout that integer range.

## 4. Exact central-step flow

Put

\[
N=\left\lfloor\frac{X+1}{2}\right\rfloor,
\qquad
L=\left\lceil\frac{3X}{8}\right\rceil,
\]

and extend `P_X(N+1)=0`. Define

\[
d_n=P_X(n)-P_X(n+1)
\qquad(L\le n\le N).
\tag{L-30701.7}
\]

By (L-30701.6),

\[
d_n\ge0.
\]

Let

\[
h_n=[n,\lfloor n/2\rfloor]
\]

be the central balanced split. If

\[
L\le q\le n\le N,
\]

then `q>n/2`, so both children are smaller than `q` and

\[
\boxed{\chi_{h_n}(q)=1.}
\tag{L-30701.8}
\]

Therefore the nonnegative flow

\[
\boxed{
\mathcal F_X^{\rm out}
=\sum_{n=L}^{N}d_nh_n
}
\tag{L-30701.9}
\]

has exact load

\[
\begin{aligned}
\operatorname{load}_q(\mathcal F_X^{\rm out})
&=\sum_{n=q}^{N}d_n\\
&=P_X(q)
\end{aligned}
\]

for every `L<=q<=N`. Thus

\[
\boxed{
\operatorname{load}_q(\mathcal F_X^{\rm out})=P_X(q)
\qquad(L\le q\le N).
}
\tag{L-30701.10}
\]

The complete macroscopic band which forced the linear atomic norm is therefore
not expensive in carry geometry: it is paid with zero negative capacity.

## 5. Leakage and exact scope

The same positive rows have nontrivial loads below `L`. Define the remaining
source

\[
R_X(q)
=P_X(q)-\operatorname{load}_q(\mathcal F_X^{\rm out}).
\tag{L-30701.11}
\]

Then

\[
\boxed{R_X(q)=0\qquad(q\ge L).}
\tag{L-30701.12}
\]

No assertion is made that `R_X` is positive or that repeating the same central
construction contracts its debt. In fact the central-row transition mutation
on the live review graph shows that central steps alone can amplify lower-band
variation.

The theorem closes exactly one issue:

```text
linear ordinary divisor-source norm
is not
linear optimized carry debt.
```

## 6. Proof boundary

Proved exactly:

1. positivity and monotonicity of the full outer boundary;
2. an explicit nonnegative balanced flow for that band;
3. strict support descent of the leakage.

Open:

1. cycle optimization of the lower leakage;
2. an all-generation subpower debt theorem;
3. RH.
