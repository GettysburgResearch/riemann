# L-92110 — Projectively compatible finite passive strings glue to one global string

Claim ID: `L-92110`
Status: **EXACT COMPACTNESS THEOREM**
Created: 2026-08-14
Depends on: standard weak-* compactness of finite measures on a compact interval after one-point compactification; parent complete-Bernstein/Stieltjes normalization on PR #449
RH status: **unproved**

Let `r>0` be fixed. For each `n`, let

\[
f_n(z)=\frac{a_n}{z}+b_n+\int_{[0,\infty)}\frac{d\mu_n(s)}{z+s},
\qquad a_n,b_n\ge0,\quad \mu_n\ge0,
\]

be a generalized Stieltjes function on `C\(-infinity,0]`. Assume

\[
\boxed{f_n(r)\le M}
\]

for one constant `M` independent of `n`.

Then some subsequence converges locally uniformly on the slit plane to another generalized Stieltjes function

\[
f(z)=\frac{a}{z}+b+\int_{[0,\infty)}\frac{d\mu(s)}{z+s}.
\]

## Proof

Set

\[
d\nu_n(s)=\frac{d\mu_n(s)}{r+s}.
\]

The anchor bound gives

\[
\frac{a_n}{r}+b_n+\nu_n([0,\infty))\le M.
\]

Thus `a_n`, `b_n`, and the total masses of `nu_n` are uniformly bounded.

Compactify `[0,infinity)` to `[0,infinity]`. After passage to a subsequence,

\[
a_n\to a_0,\qquad b_n\to b_0,
\]

and `nu_n` converges weak-* to a finite positive measure `nu` on `[0,infinity]`.

For fixed `z` off the negative real axis, write

\[
\frac1{z+s}=\frac{r+s}{z+s}\frac1{r+s}.
\]

Hence

\[
f_n(z)=\frac{a_n}{z}+b_n+\int_{[0,\infty]}K_z(s)\,d\nu_n(s),
\qquad
K_z(s)=\frac{r+s}{z+s}.
\]

The compactified kernel is continuous with

\[
K_z(0)=\frac r z,
\qquad
K_z(\infty)=1.
\]

Therefore

\[
f_n(z)\to
\frac{a_0}{z}+b_0+
\int K_z(s)d\nu(s).
\]

Separate the endpoint masses:

\[
a=a_0+r\nu(\{0\}),
\qquad
b=b_0+\nu(\{\infty\}),
\]

and on `(0,infinity)` define

\[
d\mu(s)=(r+s)d\nu(s).
\]

Then the limit has generalized Stieltjes form. Uniform convergence on compact subsets follows because the family `K_z(s)` is jointly continuous and uniformly bounded when `z` ranges in a compact subset of the slit plane.

## Projective interpolation consequence

Let `Q={q_1,q_2,...}` be a countable dense safe set with `q_1=r`. Suppose for each `N` there is a generalized Stieltjes `f_N` such that

\[
|f_N(q_j)-y(q_j)|\le\varepsilon_N,
\qquad j\le N,
\qquad \varepsilon_N\to0,
\]

and `f_N(r)<=M` uniformly. Then a diagonal subsequence converges to a generalized Stieltjes function `f` with

\[
f(q_j)=y(q_j)
\]

for every `j`.

If `y` is the safe Xi admittance from PR #449, equality on the dense safe set plus analyticity identifies `f` with the actual safe admittance. Thus the only remaining producer burden is finite positive-string interpolation with one anchor bound; no extra global compactness theorem is needed.

```text
anchor-normalized compactness          EXACT
endpoint mass at 0/infinity            RETAINED
local uniform Stieltjes limit           EXACT
finite-to-countable interpolation glue  EXACT
actual finite Xi interpolation          OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```
