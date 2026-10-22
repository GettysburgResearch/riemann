# L-30502 — The complete stopped boundary has logarithmic Mersenne seminorm

Claim ID: `L-30502`  
Title: Recombining the full positive stopped-power layer cake before source inversion converts the dense boundary into one smooth shifted-central transform with logarithmic sparse dyadic variation  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #286 `L-28402`; PR #301 `L-29801`; PR #302 `L-28004`  
Scope: the complete initial critical boundary and the reciprocal-eta/Mersenne sparse functional

## 1. Complete stopped-layer recombination

Let

\[
 p(x)=x^{-1/2},
 \qquad
 p_Y(n)=n^{-1/2}\mathbf1_{n\le Y},
 \qquad
 \ell_Y=\log{Y+1\over Y}.
\]

PR #301 proves

\[
 w_X(n)=n^{-1/2}\log(X/n)\mathbf1_{n\le X}
 =\sum_{Y=1}^{X-1}\ell_Yp_Y(n).
\tag{L-30502.1}
\]

For a function on the positive half-line define the shifted central operator

\[
 (\mathscr Cf)(q)
 =\sum_{k\ge1}
 \left[f(2kq-1)-f((2k+1)q)\right],
 \qquad q\ge2,
\tag{L-30502.2}
\]

with the naturally paired convergent interpretation.

Let `mathscr Q_Y p` be the finite/infinite boundary from PR #286. By definition,

\[
 \mathscr C_Yp_Y=\mathscr Cp-\mathscr Q_Yp.
\]

Summing this identity with the positive weights `ell_Y` gives

\[
 \mathscr C_Xw_X
 =\log X\,\mathscr Cp
  -\sum_{Y=1}^{X-1}\ell_Y\mathscr Q_Yp.
\tag{L-30502.3}
\]

Define the continuous function

\[
\boxed{
 h_X(x)=x^{-1/2}\log(\min(x,X)).
}
\tag{L-30502.4}
\]

Then, on every positive integer,

\[
 w_X=\log X\,p-h_X.
\]

Applying `mathscr C` and comparing with (L-30502.3) yields the exact complete
boundary identity

\[
\boxed{
 G_X(q):=\sum_{Y=1}^{X-1}\ell_Y(\mathscr Q_Yp)(q)
 =(\mathscr Ch_X)(q).
}
\tag{L-30502.5}

Thus the full stopped endpoint bank must be recombined before a norm is taken.
Its boundary is not a collection of independent raw endpoint atoms; it is one
smooth shifted-central transform.

## 2. Derivative bounds for the recombined profile

Put `L=log X`. On `1<=x<=X`,

\[
 h_X(x)=x^{-1/2}\log x,
\]

while for `x>=X`,

\[
 h_X(x)=Lx^{-1/2}.
\]

The function is continuous at `X`. Away from `X`,

\[
\boxed{
 |h_X'(x)|\le(1+L)x^{-3/2}.
}
\tag{L-30502.6}

Set

\[
 u_X(x)=xh_X'(x).
\]

Away from `X`, direct differentiation gives

\[
\boxed{
 |u_X'(x)|\le(1+L)x^{-3/2}.
}
\tag{L-30502.7}

The only jump is

\[
 u_X(X+)-u_X(X-)=-X^{-1/2}.
\tag{L-30502.8}

## 3. Pointwise shifted-central bound

For

\[
 a=2kq-1,
 \qquad
 b=(2k+1)q,
\]

one has `b-a=q+1`. The mean-value estimate (L-30502.6) gives

\[
 |h_X(a)-h_X(b)|
 \le(q+1)(1+L)a^{-3/2}.
\]

For `q>=2`, `k>=1`,

\[
 a\ge{3\over4}(2kq).
\]

Using `q+1<=3q/2`, `zeta(3/2)<3`, and summing in `k` yields

\[
\boxed{
 |G_X(q)|\le4(1+L)q^{-1/2}.
}
\tag{L-30502.9}

No divisor-source absolute value appears.

## 4. Adjacent-difference bound

Treat `q` as a real variable between integers. At every differentiability point,

\[
\begin{aligned}
 G_X'(q)
 =\sum_{k\ge1}
 \left[
 2k h_X'(2kq-1)
 -(2k+1)h_X'((2k+1)q)
 \right].
\end{aligned}
\tag{L-30502.10}

Since

\[
 2k h_X'(a)
 ={u_X(a)+h_X'(a)\over q},
 \qquad
 (2k+1)h_X'(b)={u_X(b)\over q},
\]

one pair is bounded by

\[
 {1\over q}
 \left(|u_X(a)-u_X(b)|+|h_X'(a)|\right).
\]

Equations (L-30502.6)--(L-30502.8) give a smooth contribution at most

\[
 2(1+L)a^{-3/2}.
\]

The disjoint intervals `[2kq-1,(2k+1)q]` contain the point `X` for at most one
`k`. Its jump contribution is at most

\[
 {1\over q\sqrt X}\le q^{-3/2}
\]

whenever such a crossing occurs. Summing the smooth terms as in Section 3 gives

\[
\boxed{
 |G_X'(q)|\le8(1+L)q^{-3/2}
 \qquad(q\ge2)
}
\tag{L-30502.11}

at every differentiability point. Since `G_X` is continuous and piecewise
absolutely continuous, the same bound integrates across the finitely many
breakpoints.

Consequently

\[
\boxed{
 |G_X(q+1)-G_X(q)|
 \le8(1+L)q^{-3/2}.
}
\tag{L-30502.12}

## 5. Logarithmic Mersenne seminorm

For powers of two `P=2^r`, `r>=1`, define

\[
 \|G_X\|_{\mathcal M}
 =|G_X(2)|
  +\sum_{P=2^r}
   P\,|G_X(2P-1)-G_X(2P)|.
\tag{L-30502.13}

Terms beyond the relevant finite support may be omitted; retaining all of them
only strengthens the bound. By (L-30502.9),

\[
 |G_X(2)|<3(1+L).
\]

For `P>=2`, equations (L-30502.11)--(L-30502.12) and
`2P-1>=(3/2)P` give

\[
 P|G_X(2P-1)-G_X(2P)|
 \le5(1+L)P^{-1/2}.
\]

Finally

\[
 \sum_{r\ge1}2^{-r/2}=1+\sqrt2<{5\over2}.
\]

Therefore

\[
\boxed{
 \|G_X\|_{\mathcal M}
 \le16(1+\log X).
}
\tag{L-30502.14}

The constant `16` is deliberately nonoptimal.

## 6. Dense versus sparse boundary coordinates

`L-30501` proves simultaneously

\[
 \|\Sigma_X\|_{\rm at}\ge X/750,
\]

where `Sigma_X` is the ordinary divisor-source atomization of the same boundary.
Equation (L-30502.14) proves

\[
 \|G_X\|_{\mathcal M}=O(\log X).
\]

Thus the two coordinates have radically different sizes:

```text
ordinary divisor-source absolute norm     linear;
reciprocal-eta/Mersenne sparse seminorm    logarithmic.
```

This is the exact mechanism hidden by terminal atomization. The dense source
must be paired with the eta/Mersenne consumer, or cycle-optimized in its native
quotient coordinate, before an absolute norm is taken.

## 7. Proof boundary

Closed here:

1. exact recombination of the complete stopped-power boundary;
2. pointwise and adjacent-difference bounds;
3. the logarithmic Mersenne seminorm;
4. quantitative separation from ordinary atomic norm.

Not proved here:

1. the corresponding all-generation Mersenne estimate after every finite
   cascade stage;
2. a complete reciprocal-eta subpower theorem;
3. RH.