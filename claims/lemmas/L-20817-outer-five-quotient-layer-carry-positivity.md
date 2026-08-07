# L-20817 — Outer-five-quotient-layer carry positivity

Claim ID: `L-20817`  
Title: The canonical carry-saturation coefficients are nonnegative throughout the complete outer region `5n>X`  
Status: `PROPOSED — COMPLETE ELEMENTARY PROOF`  
Authoring agent: `gpt56-03-y`  
Created: 2026-08-07  
Dependencies: `R-20805`; `L-20816`  
Scope: rigorous partial closure of the Carry Saturation Lemma

## 1. Exact adjoint formula

Fix an integer cutoff `X>=2` and retain

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

Define

\[
 u_m=\sum_{k\le X/m}\mu(k)w_X(mk),
 \qquad u_{X+1}=0.
\]

`R-20805` gives

\[
 C_j={j u_j+\sum_{m=j+1}^Xu_m\over j(j-1)},
 \qquad
 c_X(j)=(j+1)(C_j-C_{j+1}).
\]

A direct subtraction yields the useful exact formula

\[
\boxed{
 c_X(j)=
 { (j+1)[j u_j-(j-2)u_{j+1}]
   +2\sum_{m=j+2}^Xu_m
  \over j(j-1)}.}
\tag{L-20817.1}
\]

Consequently, if the tail

\[
 u_j,u_{j+1},\ldots,u_X
\]

is nonnegative and nonincreasing, then `c_X(j)>=0`.

Indeed,

\[
 j u_j-(j-2)u_{j+1}
 =j(u_j-u_{j+1})+2u_{j+1}\ge0,
\]

and every term in (L-20817.1) is nonnegative.

## 2. Explicit Möbius tails before the fifth quotient

Write

\[
 y={X\over m},
 \qquad L=\log y.
\]

For `m>X/5`, only the Möbius values

\[
 \mu(1)=1,
 \qquad \mu(2)=\mu(3)=-1,
 \qquad \mu(4)=0
\]

can enter. Therefore

\[
 u_m=m^{-1/2}[A(y)L+B(y)],
\tag{L-20817.2}
\]

where the constants on the three quotient regions are

\[
(A,B)=
\begin{cases}
(1,0),&1\le y<2,\\[1mm]
(1-2^{-1/2},\ 2^{-1/2}\log2),&2\le y<3,\\[1mm]
(1-2^{-1/2}-3^{-1/2},\
  2^{-1/2}\log2+3^{-1/2}\log3),&3\le y<5.
\end{cases}
\tag{L-20817.3}
\]

The formula is continuous at `y=2,3,4`: a newly admitted Möbius term has
`log(y/k)=0` at its admission point, and `mu(4)=0`.

## 3. Positivity and monotonicity

For a fixed pair `(A,B)`, put

\[
 f(m)=m^{-1/2}[A\log(X/m)+B].
\]

Then

\[
 f'(m)=-m^{-3/2}
 \left[A+{1\over2}(A\log(X/m)+B)\right].
\tag{L-20817.4}
\]

On the first two regions, both the value and the bracket in (L-20817.4) are
immediately positive.

On `3<=y<5`, set

\[
 A_*=1-2^{-1/2}-3^{-1/2}<0,
 \qquad
 B_*=2^{-1/2}\log2+3^{-1/2}\log3.
\]

Because `A_*<0`, both required expressions are minimized at `y=5`. Direct
outward elementary enclosures give

\[
 A_*\log5+B_*>0.666,
\]

and

\[
 A_*+{1\over2}(A_*\log5+B_*)>0.048.
\tag{L-20817.5}
\]

For example, these bounds follow from rational enclosures

```text
1.4142 < sqrt(2) < 1.4143,
1.7320 < sqrt(3) < 1.7330,
0.6931 < log(2) < 0.6932,
1.0986 < log(3) < 1.0987,
1.6094 < log(5) < 1.6095.
```

Thus `u_m>0` and `u_m` decreases as `m` increases throughout the complete
region `m>X/5`.

## 4. Partial Carry Saturation Theorem

For every integer `X>=2` and every integer `j` satisfying

\[
\boxed{5j>X,}
\]

the tail beginning at `j` is nonnegative and nonincreasing. Equation
(L-20817.1) therefore proves

\[
\boxed{c_X(j)\ge0\qquad(5j>X).}
\tag{L-20817.6}
\]

This closes the first four quotient intervals, equivalently the entire outer
four-fifths of the coefficient index range, without numerical computation and
without any hypothesis about zeta zeros.

## 5. Exact stopping point of this induction

The same monotone-tail proof does not pass automatically into the next region.
When `5<=y<6`, the new term `mu(5)=-1` changes the logarithmic coefficient to

\[
 A_5=1-2^{-1/2}-3^{-1/2}-5^{-1/2},
\]

and the bracket in (L-20817.4) is negative on that region. The sequence `u_m`
need not remain monotone, although the fully averaged coefficient `c_X(j)` is
still positive in all retained reconnaissance.

Thus (L-20817.6) is a genuine theorem, but it is not a proof of complete carry
saturation.

## 6. Proof boundary

Closed:

- the exact coefficient formula (L-20817.1);
- positivity and monotonicity of the Möbius-adjoint tail for `5m>X`;
- coefficient positivity for every `5j>X`.

Open:

- coefficient positivity in the inner region `5j<=X`;
- a replacement invariant strong enough to survive the first Möbius sign-change
  layer.

No RH conclusion is claimed from this partial result alone.
