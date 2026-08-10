# L-90302 — The two-state curvature determinant is one Wronskian scalar

Claim ID: `L-90302`  
Title: The determinant of the complete two-state Jordan curvature has an exact exterior-product formula, reducing polarized positivity and inertia defect to one scalar Wronskian correlation  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-90301`; PR #350 `L-34412`  
Scope: exact two-dimensional Hermitian algebra; no arithmetic sign theorem

## 1. Exterior product

For `x=(x_1,x_2), y=(y_1,y_2) in C^2`, put

\[
x\wedge y=x_1y_2-x_2y_1.
\tag{L-90302.1}
\]

Let

\[
v=V(0),\qquad a=V'(0),\qquad b=V''(0)
\]

and

\[
K=aa^*-\frac12(vb^*+bv^*).
\tag{L-90302.2}
\]

Then

\[
\boxed{
\det K
=\operatorname{Re}\!\left[(v\wedge a)\,\overline{(a\wedge b)}\right]
-\frac14|v\wedge b|^2.
}
\tag{L-90302.3}
\]

### Proof

Both sides are invariant under unitary change of coordinates.  By continuity it suffices to take `v != 0` and rotate so that

\[
v=(r,0),\qquad r>0.
\]

Write `a=(x,y)` and `b=(p,q)`.  Then

\[
K=
\begin{pmatrix}
|x|^2-r\operatorname{Re}p & x\bar y-r\bar q/2\\
y\bar x-rq/2 & |y|^2
\end{pmatrix}.
\]

Direct expansion gives

\[
\det K
=r\operatorname{Re}(x\bar y q)
-r|y|^2\operatorname{Re}p
-\frac{r^2|q|^2}{4}.
\]

But

\[
v\wedge a=ry,
\quad
a\wedge b=xq-yp,
\quad
v\wedge b=rq,
\]

which is exactly (L-90302.3).

## 2. Exact scalar defect

The scalar curvature is

\[
t=\operatorname{tr}K
=\|a\|^2-\operatorname{Re}\langle v,b\rangle.
\tag{L-90302.4}
\]

For a `2 x 2` Hermitian matrix,

\[
\|K\|_F^2-t^2=-2\det K.
\]

Therefore, when `t>=0`, the excess entering `L-90301` is exactly

\[
\boxed{
\begin{aligned}
e
&=(-2\det K)_+\\
&=\Bigl[
\frac12|v\wedge b|^2
-2\operatorname{Re}\bigl((v\wedge a)\overline{(a\wedge b)}\bigr)
\Bigr]_+.
\end{aligned}}
\tag{L-90302.5}
\]

Thus the entire failure of polarized PSD is one scalar comparison among three Wronskians.

## 3. Source-row coordinates

For the source-bound row path used throughout the Q4/Jordan work, write

\[
v=(1,Y),\qquad a=(P,Q),\qquad b=(S,T),
\tag{L-90302.6}
\]

with real untwisted row coordinates.  Then

\[
v\wedge a=Q-YP,
\]

\[
v\wedge b=T-YS,
\]

\[
a\wedge b=PT-QS.
\]

Hence

\[
\boxed{
\det K
=(Q-YP)(PT-QS)-\frac14(T-YS)^2.
}
\tag{L-90302.7}
\]

At independent frequencies the same formula holds with the Hermitian real part in (L-90302.3).

The trace is the familiar source-complete augmented curvature

\[
\boxed{
t=P^2-S+Q^2-YT.}
\tag{L-90302.8}
\]

This gives a completely explicit replacement for the phrase

```text
prove the polarized 2 x 2 arithmetic matrix is PSD.
```

One may instead prove a one-sided estimate for the single scalar (L-90302.7), with the quantitative tolerance supplied by `L-90301`.

## 4. Common-carrier factorization

Suppose the two-state path factors as

\[
V(\tau)=F(\tau)p(\tau),
\]

where `F` is one scalar arithmetic carrier and `p=(p_1,p_2)` is a finite filter/state vector.  Put

\[
\alpha=F'/F,\qquad \beta=F''/F,
\]

and

\[
w_0=p\wedge p',\qquad
w_1=p\wedge p'',\qquad
w_2=p'\wedge p''.
\]

Then exactly

\[
\boxed{V\wedge V'=F^2w_0,}
\tag{L-90302.9}
\]

\[
\boxed{V\wedge V''=F^2(2\alpha w_0+w_1),}
\tag{L-90302.10}
\]

and

\[
\boxed{
V'\wedge V''
=F^2[(2\alpha^2-\beta)w_0+\alpha w_1+w_2].
}
\tag{L-90302.11}
\]

So after the complete source/filter recombination, the determinant defect separates into:

1. finite filter Wronskians `w_0,w_1,w_2`;
2. the scalar logarithmic jets `alpha,beta` of the common arithmetic carrier.

This is tailored to the existing Q2/Q4 state factorizations on PR #350.  The full matrix does not need to be expanded coefficient by coefficient before the source structure is used.

## 5. Why this is a genuine simplification

The previous frontier asked for a matrix inequality.  In state dimension two:

```text
scalar curvature t               already controlled cofinally;
full PSD                          equivalent to det K >= 0;
inertia-tolerant synthesis       only needs (-det K)_+/t controlled;
det K                            one explicit Wronskian scalar.
```

The determinant formula also makes clear why a large RH-sensitive first current need not create a comparably large negative eigenvalue: the determinant measures a correlated source/current Wronskian, while the trace contains the large positive current square.

## 6. Proof boundary

Closed exactly:

1. the complex two-state determinant identity;
2. the explicit source-row formula;
3. the common-carrier/filter factorization;
4. the reduction of negative spectral mass to one Wronskian scalar together with `L-90301`.

Open:

1. source-specific control of the negative Wronskian defect in the live Q4 ledger;
2. the delayed recurrence;
3. RH.