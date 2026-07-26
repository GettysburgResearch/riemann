# L-9310 — Half-line SOS moment closure of every nonnegative response polynomial

Claim ID: L-9310  
Title: Two finite Hankel matrices decide the full direct-xi response-polynomial cone on a fixed node table  
Status: PROPOSED  
Authoring agent: `gpt56-01-n`  
Created: 2026-07-26  
Dependencies: L-9308; L-9309  
Scope: exact closure or separation of all polynomial responses nonnegative on `[0,infinity)`  
Related counterexample candidates: none

## Summary

L-9309 closes the subcone in which the response polynomial has nonnegative
monomial coefficients. The actual L-9308 condition is larger:

\[
P_\beta(y)\ge0\qquad(y\ge0).
\]

This lemma gives an exact finite decision procedure for that **entire** cone.
For a degree bound `d`, let

\[
\ell_k=L(\beta^{(k)}),\qquad 0\le k\le d,
\]

where `beta^(k)` is the exact L-9309 portfolio with response polynomial `y^k`.
The sequence `ell_k` is the finite moment sequence of the frozen linear
functional `L` on response polynomials.

If `d=2m`, form

\[
H_0=(\ell_{i+j})_{0\le i,j\le m},
\qquad
H_1=(\ell_{i+j+1})_{0\le i,j\le m-1}.
\]

If `d=2m+1`, form

\[
H_0=(\ell_{i+j})_{0\le i,j\le m},
\qquad
H_1=(\ell_{i+j+1})_{0\le i,j\le m}.
\]

Then

\[
\boxed{
L(P)\ge0\text{ for every real }P\ge0\text{ on }[0,\infty),\ \deg P\le d
}
\]

if and only if both Hankel matrices are positive semidefinite.

If one matrix has a negative rational direction, its square polynomial—or `y`
times its square polynomial—is already an explicit finite RH-disproof portfolio
through L-9308. If both matrices are rigorously positive for interval-valued
moments, the complete degree-bounded response cone is closed at once.

## Half-line sum-of-squares decomposition

### Proposition

Every real polynomial `P` nonnegative on `[0,infinity)` can be written

\[
\boxed{
P(y)=\sum_r a_r(y)^2+y\sum_s b_s(y)^2.
}
\]

If `deg P=2m`, one may take

\[
\deg a_r\le m,
\qquad
\deg b_s\le m-1.
\]

If `deg P=2m+1`, one may take

\[
\deg a_r\le m,
\qquad
\deg b_s\le m.
\]

### Self-contained proof

Put

\[
Q(t)=P(t^2).
\]

Then `Q` is a real polynomial nonnegative on all of `R`. Factor `Q` over the
reals. Every real root has even multiplicity. Every irreducible quadratic factor
is strictly positive and, after completing the square, is a sum of two squares
of real polynomials. The identity

\[
(A^2+B^2)(C^2+D^2)
=(AC-BD)^2+(AD+BC)^2
\]

shows that the product of two sums of two squares is again a sum of two squares.
Thus

\[
Q(t)=A(t)^2+B(t)^2
\]

for real polynomials `A,B`.

Split each polynomial into even and odd parts:

\[
A(t)=A_e(t)+A_o(t),
\qquad
B(t)=B_e(t)+B_o(t).
\]

Since `Q` is even, its odd part vanishes:

\[
A_eA_o+B_eB_o=0.
\]

Therefore

\[
Q=A_e^2+B_e^2+A_o^2+B_o^2.
\]

Write

\[
A_e(t)=a(t^2),\quad B_e(t)=c(t^2),
\]

\[
A_o(t)=t b(t^2),\quad B_o(t)=t d(t^2).
\]

Substituting `y=t^2` gives

\[
P(y)=a(y)^2+c(y)^2+y b(y)^2+y d(y)^2.
\]

The degree bounds follow directly from `deg A,deg B <= deg Q/2`. This proves the
proposition. ∎

## Moment-matrix theorem

Let `L` be any real linear functional on polynomials of degree at most `d`, and
put

\[
\ell_k=L(y^k).
\]

### Even degree `d=2m`

For

\[
a(y)=\sum_{i=0}^{m}a_i y^i,
\]

one has

\[
L(a^2)=a^T H_0 a.
\]

For

\[
b(y)=\sum_{i=0}^{m-1}b_i y^i,
\]

one has

\[
L(yb^2)=b^T H_1 b.
\]

The half-line SOS decomposition therefore implies

\[
L(P)\ge0\quad\text{for every }P\ge0,\ \deg P\le2m
\]

whenever `H0,H1` are positive semidefinite.

Conversely, if `a^T H0 a<0`, then `P=a^2` is a nonnegative polynomial with
`L(P)<0`. If `b^T H1 b<0`, then `P=y b^2` is a nonnegative polynomial with
`L(P)<0`. Thus positivity of the two matrices is necessary and sufficient.

### Odd degree `d=2m+1`

The same proof applies with `deg a,deg b<=m`, so both `H0` and `H1` have size
`m+1`.

This proves the boxed equivalence.

## Direct-xi interpretation

On a fixed direct-xi/count-deflated node table, let `L_T(beta)` be the frozen
linear residual functional from L-9308. L-9309 supplies the exact basis
portfolios `beta^(k)` satisfying

\[
P_{\beta^{(k)}}(y)=y^k.
\]

Hence

\[
\ell_k=L_T(\beta^{(k)}).
\]

A negative rational direction in either moment matrix gives an explicit
portfolio:

- `P(y)=a(y)^2` from a negative `H0` direction;
- `P(y)=y b(y)^2` from a negative `H1` direction.

The corresponding exact rational `beta` is recovered by the L-9309 inverse:

\[
\beta_i=-\frac{P(-u_i)}{\prod_{j\ne i}(u_j-u_i)}.
\]

Because `P>=0` on the half-line, L-9308 makes this a valid RH-disproof witness
if its complete directed residual upper endpoint is negative.

## Robust interval certificate

Suppose each basis value is enclosed by

\[
\ell_k\in[\underline\ell_k,\overline\ell_k].
\]

Define exact rational midpoints and radii

\[
m_k=\frac{\underline\ell_k+\overline\ell_k}{2},
\qquad
r_k=\frac{\overline\ell_k-\underline\ell_k}{2}.
\]

Let `M0,M1` be the midpoint Hankel matrices and let `R0,R1` be their entrywise
radius matrices. Fix an exact rational `delta>0`.

Assume:

1. exact rational LDL factorizations prove
   \[
   M_0-\delta I\succ0,
   \qquad
   M_1-\delta I\succ0;
   \]
2. exact row-sum bounds prove
   \[
   \varepsilon_0=\max_i\sum_j(R_0)_{ij}<\delta,
   \]
   \[
   \varepsilon_1=\max_i\sum_j(R_1)_{ij}<\delta.
   \]

For every admissible exact Hankel matrix `H=M+E`,

\[
\|E\|_2\le\|E\|_\infty\le\varepsilon.
\]

Therefore

\[
\boxed{
H_0\succeq(\delta-\varepsilon_0)I\succ0,
\qquad
H_1\succeq(\delta-\varepsilon_1)I\succ0.
}
\]

This certifies strict positivity of the entire nonzero degree-bounded half-line
cone despite shared interval uncertainty.

## PR #103 atomized-minimum certificate

For the committed 16-node, 512-bit atomized-minimum table at ordinate shift

\[
\frac{483}{1024},
\]

L-9309 gives moments `ell_0,...,ell_14`. Thus `d=14=2*7`, and the complete cone
is governed by

\[
H_0=(\ell_{i+j})_{0\le i,j\le7},
\qquad
H_1=(\ell_{i+j+1})_{0\le i,j\le6}.
\]

Use

\[
\delta=\frac1{100000}.
\]

The exact standard-library checker proves every LDL pivot of

\[
M_0-\delta I
\quad\text{and}\quad
M_1-\delta I
\]

strictly positive. The midpoint pivot approximations are:

```text
H0-delta I:
1.1658837781416847e8
2.9848195976500502e4
4.9614486983503678e1
9.2825010945945620e-1
4.0025744448133878e-2
8.0393545303811047e-3
1.1299609732479410e-2
1.4490020403269124

H1-delta I:
3.0193794005571052e7
8.8644874150896057e3
1.9442093394948421e1
4.9875931118628000e-1
3.0360098168068567e-2
1.2013127826460019e-2
6.2192032126116841e-2
```

The complete interval-box row-sum radii satisfy

\[
\varepsilon_0
<1.414035934617576\times10^{-32},
\]

\[
\varepsilon_1
<6.430285324476411\times10^{-44}.
\]

Hence

\[
\delta-\varepsilon_0
>9.9999999999999999999999999858\times10^{-6},
\]

\[
\delta-\varepsilon_1
>9.99999999999999999999999999999999999994\times10^{-6}.
\]

The canonical SHA-256 of the exact rational delta, both pivot lists, and both
row-radius bounds is

```text
7028c2688bcd8ca783e98977bd2da6247fd70bc59f4d6f78b7df7f05a5c6096b
```

Therefore:

\[
\boxed{
\text{Every nonzero real response polynomial }P\ge0\text{ on }[0,\infty),
\ \deg P\le14,
\text{ has a strictly positive directed residual on this exact table.}
}
\]

This rigorously closes the complete L-9308 response-polynomial cone available on
the 16 fixed nodes—not merely the monomial-positive subcone and not merely the
previously enumerated determinant families.

## Exact checker interface

X-9308 reads the committed L-9309 basis intervals and:

1. parses every finite decimal endpoint as an exact rational;
2. constructs both midpoint Hankel matrices and radius matrices;
3. performs exact rational LDL without pivoting on `M-delta I`;
4. requires every pivot to be strictly positive;
5. computes exact maximum row-sum radius bounds;
6. requires each radius to be strictly below `delta`;
7. hashes the complete exact rational proof object.

No floating eigensolver or SDP solver enters the trust boundary.

## Proof boundary

- The half-line SOS and moment-matrix equivalence are exact finite algebra.
- The PR #103 closure inherits the directed basis intervals and their source
  bindings from X-9307/PR #112.
- The RH interpretation inherits L-7501/L-7502/L-9308 and the atomized
  total-count conversion.
- The closure applies to degree at most 14 on this exact 16-node table and this
  exact ordinate/count profile.
- It says nothing about higher-degree response polynomials requiring additional
  horizontal nodes, other ordinates, or nonpolynomial positive responses.
- No counterexample or RH resolution is claimed.

## Suggested next attack

The PR #103 atomized minimum is now closed under every degree-14 half-line
nonnegative response polynomial. The next offensive move must change the finite
primitive table: add horizontal nodes to raise the degree, move to a distinct
large-gap ordinate, or enlarge beyond scalar logarithmic response polynomials.
Do not continue optimizing inside the closed 16-node cone.
