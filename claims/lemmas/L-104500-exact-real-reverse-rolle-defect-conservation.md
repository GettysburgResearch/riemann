# L-104500 — Exact real reverse-Rolle edge identity and defect conservation

Claim ID: `L-104500`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
RH status: **not assumed**

## 1. Exact interval identity

Let `f` be real analytic on a neighbourhood of `[a,b]`.  Assume:

1. `f(a)f(b) != 0`;
2. every zero of `f'` in `(a,b)` is simple;
3. `f` and `f'` have no common zero in `[a,b]`.

Write the critical points as

\[
a<c_1<\cdots<c_m<b
\]

and put `c_0=a`, `c_(m+1)=b`.

Since `f` is strictly monotone on every interval `(c_j,c_(j+1))`, that
interval contains exactly one real zero of `f` if and only if the two endpoint
values have opposite signs.  Hence

\[
\boxed{
N_\mathbb R(f;(a,b))
=
\sum_{j=0}^{m}
\mathbf1_{\{f(c_j)f(c_{j+1})<0\}}.
}
\tag{L-104500.1}
\]

This adjacent-critical-value identity is the primitive reverse-Rolle theorem.
It is exact and has no asymptotic or density hypothesis.

## 2. Wrong extrema and the factor two

For `1<=j<=m`, define

\[
e_j
=
\mathbf1_{\{f(c_j)f''(c_j)>0\}}
=
\mathbf1_{\{\mathcal L_f(c_j)<0\}},
\]

where

\[
\mathcal L_f=f'^2-ff''.
\]

Thus `e_j=1` precisely for a positive local minimum or a negative local
maximum.

Consecutive simple critical points have opposite extremum type.  Monotonicity
between them gives

\[
\boxed{
\mathbf1_{\{f(c_j)f(c_{j+1})<0\}}
=1-e_j-e_{j+1}
\qquad(1\le j<m).
}
\tag{L-104500.2}
\]

In particular, two wrong extrema cannot be adjacent.

Define the endpoint defects

\[
B_-
=1-e_1-
 \mathbf1_{\{f(a)f(c_1)<0\}},
\]

\[
B_+
=1-e_m-
 \mathbf1_{\{f(c_m)f(b)<0\}}.
\]

Each belongs to `{0,1}`.  Summing (L-104500.2) and the two boundary edges gives

\[
\boxed{
N_\mathbb R(f;(a,b))
=m+1-2E(f;(a,b))-B_--B_+,
}
\tag{L-104500.3}
\]

where

\[
E(f;(a,b))=\sum_{j=1}^{m}e_j.
\]

If `m=0`, (L-104500.1) remains the controlling statement and says that a
monotone interval contains one zero exactly when its endpoint signs differ.

## 3. Global polynomial conservation law

Let `p` be a real polynomial of degree `n`.  Assume that all real zeros of
`p'` are simple and none is a zero of `p`.  Let `N_nr(p)` count nonreal zeros
with multiplicity.

Taking `a -> -infinity` and `b -> +infinity`, both endpoint defects vanish.
If `m=N_R(p')`, then

\[
N_\mathbb R(p)=m+1-2E(p).
\]

Since

\[
N_{\rm nr}(p)=n-N_\mathbb R(p),
\qquad
N_{\rm nr}(p')=(n-1)-m,
\]

one obtains the exact conservation law

\[
\boxed{
N_{\rm nr}(p)-N_{\rm nr}(p')=2E(p).
}
\tag{L-104500.4}
\]

Iterating,

\[
\boxed{
N_{\rm nr}(p)
=N_{\rm nr}(p^{(r)})
 +2\sum_{j=0}^{r-1}E(p^{(j)}).
}
\tag{L-104500.5}
\]

Taking `r=n-1` gives

\[
\boxed{
N_{\rm nr}(p)
=2\sum_{j=0}^{n-2}E(p^{(j)}).
}
\tag{L-104500.6}
\]

Thus every nonreal conjugate pair is paid exactly once by one wrong extremum
somewhere in the derivative ladder.

## 4. Regular-level form

For any real `lambda` which is not a critical value of `p`, the same theorem
applies to `p-lambda`:

\[
N_{\rm nr}(p-\lambda)-N_{\rm nr}(p')
=2E(p-\lambda).
\]

This is the stable formulation when the zero level itself contains a multiple
or critical event.  No assertion is made here that multiplicity conventions
may be ignored without such a regularization.

## Significance

Equation (L-104500.4) is an exact converse-Rolle conservation law.  It does not
say that derivative real-rootedness forces parent real-rootedness.  It says
precisely what is missing: each wrong extremum creates one conjugate pair of
nonreal parent zeros.

For Xi, the finite-interval analogue must additionally retain the two endpoint
defects and the complex boundary winding.  That extension is `L-104501`.
