# L-26201 — The parabolic seed is a positive endpoint-scale frame

Claim ID: `L-26201`  
Title: The sharp parabolic carry seed is an actual nonnegative average-binomial packing, and its endpoint increments are nonnegative carry atoms  
Status: **PROPOSED COMPLETE EXACT CALCULUS / FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue family: `#245/#262`  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: PR #248 `L-24501`, `L-24502`  
Scope: finite positive carry geometry; no asymptotic slack estimate and no RH conclusion

## 1. The parabolic seed in row coordinates

For an integer endpoint `X>=2`, retain the parabolic convexified coordinate

\[
 b_X(m)
 =2\sqrt m\left[
   \log\frac Xm-2\left(1-\sqrt{\frac mX}\right)
  \right],
 \qquad 2\le m\le X,
\tag{L-26201.1}
\]

and put `b_X(m)=0` for `m>X`.  Define

\[
 A_X(m)=\frac{b_X(m)}{m-1},
 \qquad A_X(X+1)=A_X(X+2)=0,
\tag{L-26201.2}
\]

and

\[
 \boxed{
 d_X(n)
 =(n+1)\left[A_X(n)-2A_X(n+1)+A_X(n+2)\right].}
\tag{L-26201.3}
\]

By the exact double-summation identities of `L-24501`, this is the unique row
coordinate associated with `b_X`:

\[
 \sum_{n=q}^X d_X(n)\beta_{nq}=v_q(b_X),
\tag{L-26201.4}
\]

and

\[
 \sum_{n=2}^X d_X(n)G_n=J_X(b_X).
\tag{L-26201.5}
\]

The new point is that `d_X` is coefficientwise nonnegative.  Thus the parabolic
seed was already a genuine positive combination of average-binomial carry rows
before any feasibility repair.

## 2. Continuous convexity proves row positivity

Extend (L-26201.1) to real `1<x<=X` and write

\[
 f_X(x)=\frac{b_X(x)}x
 =2x^{-1/2}\log\frac Xx-4x^{-1/2}+4X^{-1/2},
\]

\[
 g(x)=\frac{x}{x-1},
 \qquad
 A_X(x)=f_X(x)g(x).
\tag{L-26201.6}
\]

The derivatives are exact:

\[
 f_X(x)\ge0,
 \qquad
 f_X'(x)=-x^{-3/2}\log\frac Xx\le0,
\tag{L-26201.7}
\]

\[
 f_X''(x)=x^{-5/2}
 \left(1+\frac32\log\frac Xx\right)>0,
\tag{L-26201.8}
\]

and

\[
 g>0,
 \qquad g'=-\frac1{(x-1)^2}<0,
 \qquad g''=\frac2{(x-1)^3}>0.
\tag{L-26201.9}
\]

Consequently

\[
 \boxed{
 A_X''=f_X''g+2f_X'g'+f_Xg''>0
 \qquad(1<x<X).}
\tag{L-26201.10}
\]

Hence every interior integer second difference in (L-26201.3) is positive.
At the right boundary, `A_X(X)=0`; therefore

\[
 d_X(X-1)=X A_X(X-1)>0,
 \qquad
 d_X(X)=0.
\]

Thus

\[
 \boxed{d_X(n)\ge0\qquad(2\le n\le X).}
\tag{L-26201.11}
\]

Combining this with `L-24502.3` gives the unconditional positive-row score

\[
 \boxed{
 \sum_n d_X(n)G_n
 \ge4\sqrt X-6\log X+4-8X^{-1/2}.}
\tag{L-26201.12}
\]

The seed fails only because some column responses `v_q(b_X)` exceed the target
`w_X(q)`; it does not fail positivity in the carry-row cone.

## 3. Endpoint increments

Embed every `d_T` in the common infinite row space by setting it equal to zero
above its endpoint.  For integers `T>=3`, define the endpoint atom

\[
 \boxed{a_T(n)=d_T(n)-d_{T-1}(n).}
\tag{L-26201.13}
\]

Then

\[
 \boxed{a_T(n)\ge0\quad\text{for every }n.}
\tag{L-26201.14}
\]

### 3.1 Interior rows

For real `Y>=x`, differentiation with respect to `log Y` gives

\[
 C_Y(x)
 :=\partial_{\log Y}A_Y(x)
 =\frac{2(\sqrt x-x/\sqrt Y)}{x-1}.
\tag{L-26201.15}
\]

A direct differentiation gives

\[
 C_Y''(x)
 =
 \frac{
  3\sqrt Yx^2+6\sqrt Yx-\sqrt Y-8x^{3/2}
 }
 {2\sqrt Yx^{3/2}(x-1)^3}.
\tag{L-26201.16}
\]

When `Y>=x`, the numerator is bounded below by

\[
 \sqrt x(3x^2+6x-1)-8x^{3/2}
 =\sqrt x(3x+1)(x-1)>0.
\tag{L-26201.17}
\]

If `n<=T-3`, then `[n,n+2]` lies below every
`Y in [T-1,T]`.  Integrating the positive discrete curvature of `C_Y` gives

\[
 a_T(n)
 =\int_{\log(T-1)}^{\log T}
   (n+1)\Delta^2 C_Y(n)\,d\log Y
 >0.
\tag{L-26201.18}
\]

### 3.2 The entering boundary row

Put `m=T-1>=3`.  On `Y in [m,m+1]`, the boundary derivative needed for row
`m-1` is

\[
 C_Y(m-1)-2C_Y(m).
\]

Its coefficient of `Y^{-1/2}` is positive, so it is minimized at `Y=m+1`.
Set

\[
 a=\sqrt{\frac m{m+1}},
 \qquad
 b=\sqrt{\frac{m-1}{m+1}}.
\]

After rationalizing `1-a` and `1-b`, positivity at the minimum is equivalent to

\[
 (m-1)b(1+a)>(m-2)a(1+b).
\tag{L-26201.19}
\]

The difference of the two sides is

\[
 b(1+a)-(m-2)(a-b),
 \qquad
 a-b=\frac1{(m+1)(a+b)}.
\]

Since `b>=1/sqrt(2)`, `a+b>=sqrt(2)`, and `(m-2)/(m+1)<1`, the difference is
strictly positive.  Hence `a_T(T-2)>0`.

Finally,

\[
 a_T(T-1)=d_T(T-1)=T A_T(T-1)>0,
\]

and all rows at or above `T` vanish.  This proves (L-26201.14), including the
small endpoint `T=3` directly.

## 4. Exact positive scale frame

The atoms telescope:

\[
 \boxed{d_X=\sum_{T=3}^X a_T.}
\tag{L-26201.20}
\]

Define their carry responses and entropy scores by

\[
 \Gamma_T(q)=\sum_n a_T(n)\beta_{nq},
 \qquad
 H_T=\sum_n a_T(n)G_n.
\tag{L-26201.21}
\]

Every quantity is nonnegative.  Moreover,

\[
 \Gamma_T(q)=0\quad(q\ge T),
 \qquad
 \Gamma_T(q)>0\quad(2\le q<T),
\tag{L-26201.22}
\]

because the row `n=q` already contributes
`a_T(q) beta_(q,q)>0`.  The diagonal scale response is exact:

\[
 \boxed{
 \Gamma_T(T-1)
 =b_T(T-1)
 =2\sqrt{T-1}\left[
   \log\frac T{T-1}
   -2\left(1-\sqrt{\frac{T-1}{T}}\right)
  \right].}
\tag{L-26201.23}
\]

The entropy also telescopes:

\[
 \boxed{
 \sum_{T=3}^XH_T
 =J_X(b_X)
 \ge4\sqrt X-O(\log X).}
\tag{L-26201.24}
\]

Thus the parabolic route has a canonical one-dimensional positive dictionary:

```text
endpoint T
-> nonnegative row atom a_T
-> strictly lower-triangular positive column response Gamma_T
-> nonnegative entropy H_T.
```

No Möbius sign, prime location, or optimization solver enters the construction.

## 5. Relation to the previous routes

- `L-24508` showed that signed `b` coordinates suffice for the direct prime-ramp
  consumer.  The present lemma is stronger on the seed side: it recovers an
  actual nonnegative carry-row object.
- PR #244's row greedy works in the complete positive row cone.  The atoms
  `a_T` define a smaller but much more structured positive **scale cone**.
- PR #246 used four outer positive bands.  Equation (L-26201.20) gives an
  all-scale positive frame whose unweighted sum already has the sharp main
  mass.
- PR #247's finite minorant asks for an arbitrary positive continuum profile.
  The endpoint atoms give a finite, source-bound positive basis for constructing
  such profiles.

## 6. Proof boundary

Established in this lemma, subject to independent review:

1. the parabolic seed is a nonnegative average-binomial carry combination;
2. the endpoint family is coefficientwise increasing;
3. every endpoint difference is a nonnegative carry atom;
4. the atom response matrix is strictly lower triangular and positive;
5. the atom entropy telescopes to the sharp parabolic score.

Not established here:

- nonnegative endpoint weights making every carry column feasible;
- a subpower slack bound;
- the prime-ramp lower bound or RH.
