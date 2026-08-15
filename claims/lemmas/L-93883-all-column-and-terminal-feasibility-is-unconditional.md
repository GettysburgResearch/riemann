# L-93883 — The hybrid row satisfies every ordinary and radix-four capacity

Claim ID: `L-93883`  
Status: **PROPOSED COMPLETE ALL-COLUMN ESTIMATE**  
Depends on: exact retained-cell error, martingale collar, fixed top omission  
RH status: **unproved at this claim**

## 1. Retained-cell adjacent error

For `n` in the retained cell set, put

\[
\varepsilon_X(n)
=
d_X^\star(n)-\int_n^{n+1}d_X^\star(t)\,dt.
\]

The factor-67 derivative calculation gives

\[
\boxed{
|\varepsilon_X(n)|<\frac{19}{2}n^{-3/2}.
}
\tag{L-93883.1}
\]

For every ordinary physical column `q>=2`,

\[
v_q(E_X^I)
=
\sum_{\substack{j\ge1\\jq\in\mathcal I_X}}
\varepsilon_X(jq).
\tag{L-93883.2}
\]

With `M_q=ceil(K/q)` and `\sum_{j>=M}j^{-3/2}<3M^{-1/2}`,

\[
\boxed{
|v_q(E_X^I)|
<
\frac{57}{2q\sqrt K}.
}
\tag{L-93883.3}
\]

Applying this at `q` and `4q` gives

\[
\boxed{
|\mathcal D_4v_q(E_X^I)|
<
\frac{171}{4q\sqrt K}.
}
\tag{L-93883.4}
\]

This includes `q<K`.

## 2. Intrinsic bulk collar

The B-spline width-three collar obeys

\[
\boxed{
|\mathcal D_4v_q(C_X)|
<
\frac{200}{q\sqrt K}.
}
\tag{L-93883.5}
\]

The anchored identity block produces no quantization collar.

Combining (L-93883.4) and (L-93883.5),

\[
\boxed{
|\mathcal D_4v_q(C_X-E_X^I)|
<
\frac{971}{4q\sqrt K}.
}
\tag{L-93883.6}
\]

## 3. Nonterminal columns

For `2<=q<=X/4`, the native detail is

\[
\Omega_X(q)=\frac{\log4}{\sqrt q}
>\frac4{3\sqrt q}.
\]

Therefore

\[
\frac{|\mathcal D_4v_q(C_X-E_X^I)|}{\Omega_X(q)}
<
\frac{129}{\sqrt K}.
\tag{L-93883.7}
\]

After the common thinning,

\[
\tau_K\left(1+\frac{129}{\sqrt K}\right)
=
\frac{\sqrt K+129}{\sqrt K+130}<1.
\]

Thus

\[
\boxed{
\Xi(d_X)(q)<\Omega_X(q)
\qquad(2\le q\le X/4).
}
\tag{L-93883.8}
\]

## 4. Terminal annulus

The terminal bulk/collar overfill is bounded by

\[
512\sqrt{67}\,X^{-3/2}
<
4224X^{-3/2},
\]

and the finite mismatch contributes below

\[
228X^{-3/2}.
\]

Hence the total possible terminal overfill is below

\[
\boxed{4452X^{-3/2}.}
\tag{L-93883.9}
\]

The source-owned fixed top omission removes more than

\[
\boxed{5033X^{-3/2}}
\tag{L-93883.10}
\]

from every terminal column that can overfill. The remaining margin is at least

\[
581X^{-3/2}>0.
\]

Above retained support, triangularity gives zero response.

Consequently,

\[
\boxed{
\Xi(d_X)(q)\le\Omega_X(q)
\quad(q\ge2).
}
\tag{L-93883.11}
\]

## 5. Ordinary feasibility

The recurrence

\[
C(q)=\Xi(q)+2C(4q)
\]

has the finite positive inverse

\[
C(q)=\sum_{r\ge0}2^r\Xi(4^rq).
\]

Applying it to the row and native vectors yields

\[
\boxed{
C_{d_X}(q)\le w_X(q)
\quad(q\ge2).
}
\tag{L-93883.12}
\]

## 6. Quantifier audit

The proof is uniform for every integer `X>=10^12`. It covers:

```text
small columns q<K;
bulk nonterminal columns;
activation boundaries;
terminal columns;
columns above support.
```

No asymptotic sign is used in a finite column inequality.

## 7. Boundary

```text
all ordinary columns                       FEASIBLE
all radix-four columns                     FEASIBLE
small-q range                              INCLUDED
terminal reserve                           EXPLICIT MARGIN 581
positive row                               L-93882
native cost                                L-93884
```
