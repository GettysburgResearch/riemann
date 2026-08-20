# L-99939 — The duplicate-67 quadratic SHARP transform is globally positive

Claim ID: `L-99939`  
Status: **PROVED UNCONDITIONAL ALL-SCALE POSITIVITY THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

Define

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]

and

\[
\mathfrak H_2(x)
=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n)^2.
\]

Then

\[
\boxed{\mathfrak H_2(x)>0\qquad(x\ge1).}
\]

## Labelled Euler cube

Use one labelled copy of every prime other than `67` and two labelled copies
of `67`. For a finite subset `A` of labels put

\[
n_A=\prod_{\ell\in A}p_\ell,
\qquad
w(A;x)=n_A^{-1/2}T(x/n_A)^2,
\]

with zero weight when `n_A>x`. The two labelled copies of `67` reproduce the
local coefficients `(1,-2,1)`; every other prime contributes `(1,-1)`. Thus

\[
\mathfrak H_2(x)=\sum_A(-1)^{|A|}w(A;x).
\]

If `ell in A`, `q=p_ell`, `B=A\setminus{ell}`, and `Y=x/n_B`, then activation
of `A` gives `Y>=q`, and

\[
T(Y)-\sqrt q\,T(Y/q)=3(\sqrt q-1)>0.
\]

Hence

\[
\frac{w(A;x)}{w(B;x)}
=q^{-1/2}\left(\frac{T(Y/q)}{T(Y)}\right)^2
<q^{-3/2}.
\]

Let `M_k(x)=sum_(|A|=k) w(A;x)`. Double-counting labelled removals gives

\[
kM_k(x)<S_2M_{k-1}(x),
\]

where

\[
S_2=\sum_{p\ \mathrm{prime}}p^{-3/2}+67^{-3/2}.
\]

We prove `S_2<1` using only rational inequalities. Since

\[
\sum_{p\ \mathrm{prime}}p^{-3/2}<\log\zeta(3/2),
\]

\[
S_2<\log\!\left(\frac{\zeta(3/2)}{1-67^{-3/2}}\right).
\]

Convex midpoint comparison gives

\[
\zeta(3/2)<1+2\sqrt{2/3}<8/3,
\]

and `sqrt(67)>8` gives `67^(-3/2)<1/536`. Therefore

\[
\frac{\zeta(3/2)}{1-67^{-3/2}}
<\frac{4288}{1605}<\frac{163}{60}<e.
\]

Thus `S_2<1`. Consequently

\[
M_{2j+1}<\frac{S_2}{2j+1}M_{2j}<M_{2j}.
\]

Pairing consecutive parity levels in the finite alternating sum proves strict
positivity.
