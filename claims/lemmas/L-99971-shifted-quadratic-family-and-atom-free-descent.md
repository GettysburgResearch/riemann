# L-99971 — A shifted quadratic family is positive, with one atom-free critical descent

Claim ID: `L-99971`  
Status: **PROVED EXACT ALL-SCALE POSITIVITY + DISTRIBUTIONAL IDENTITY**  
Created: 2026-08-20  
RH status: **not assumed**

Let

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
 \qquad
 T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For `-1<=c<=3`, define the active shifted carrier

\[
 S_c(y)=(4\sqrt y-3+c)\mathbf1_{y\ge1}
\]

and

\[
 Q_c(X)=\sum_{n\ge1}{\beta(n)\over\sqrt n}S_c(X/n)^2.
\tag{L-99971.1}
\]

Then

\[
\boxed{Q_c(X)\ge0\qquad(X\ge1,-1\le c\le3),}
\tag{L-99971.2}
\]

with strict inequality for `X>1`.

## Proof

Use one labelled copy of every prime and a second copy of `67`.  For an active
labelled subset `A`, put

\[
 w_c(A)=n_A^{-1/2}S_c(X/n_A)^2.
\]

If a label `q` is removed from `A`, write `B=A\setminus{q}` and
`Y=X/n_B>=q`.  Since `S_c(y)>=0` on `y>=1`, and

\[
\boxed{
 S_c(Y)-\sqrt q\,S_c(Y/q)
 =(3-c)(\sqrt q-1)\ge0,
}
\tag{L-99971.3}
\]

we have

\[
 {w_c(A)\over w_c(B)}\le q^{-3/2}.
\tag{L-99971.4}
\]

The complete labelled prime sum

\[
 \sum_p p^{-3/2}+67^{-3/2}<1
\]

was proved elementarily in `L-99939/L-99930`.  The same adjacent-level
pairing therefore gives (L-99971.2).  The endpoint cases `c=-1` and `c=3`
follow by the non-strict version of (L-99971.4) and the strict total prime-mass
bound.

Writing

\[
 H_0(X)=\sum_{n\le X}{\beta(n)\over\sqrt n},
 \quad
 H_1(X)=\sum_{n\le X}{\beta(n)\over\sqrt n}T(X/n),
 \quad
 H_2(X)=\sum_{n\le X}{\beta(n)\over\sqrt n}T(X/n)^2,
\]

this gives the exact continuum of quadratic constraints

\[
\boxed{
 H_2(X)+2cH_1(X)+c^2H_0(X)\ge0
 \qquad(-1\le c\le3).
}
\tag{L-99971.5}
\]

## The activation-zero member

At `c=-1`,

\[
 S_{-1}(y)=4(\sqrt y-1)\mathbf1_{y\ge1}
\]

vanishes at activation.  Put

\[
 G_{-1}(u)=e^{-u}Q_{-1}(e^u).
\]

There are no activation atoms.  Direct differentiation on every active term,
using

\[
 y{d\over dy}\left({S_{-1}(y)^2\over y}\right)
 ={4S_{-1}(y)\over y},
\]

gives the global absolutely continuous identity

\[
\boxed{
 dG_{-1}(u)
 =4e^{-u}L_{-1}(e^u)\,du,
}
\tag{L-99971.6}
\]

where

\[
 L_{-1}(X)
 =\sum_{n\le X}{\beta(n)\over\sqrt n}S_{-1}(X/n)
 =H_1(X)-H_0(X).
\tag{L-99971.7}
\]

Moreover

\[
 \lim_{u\to\infty}G_{-1}(u)
 =16{1-67^{-3/2}\over\zeta(3/2)}>0.
\]

Thus

\[
\boxed{
 4\int_1^X(L_{-1}(x))_-{dx\over x}
 =\int_{[0,\log X]}e^u\,d(-G_{-1})_+(u).
}
\tag{L-99971.8}
\]

This removes the signed activation-atom ledger from the quadratic-to-critical
descent.  It does not make the critically weighted downward variation
automatic; ordinary bounded variation is still insufficient.

The Mellin transform of the active linear carrier is

\[
 \int_1^\infty4(\sqrt y-1)y^{-s-1}dy
 ={2\over s(s-1/2)}.
\]

Consequently subpower logarithmic negative mass of `L_-1` is itself a
zero-safe sufficient criterion for RH.  The theorem supplies a cleaner
critical observable, not its missing one-sided estimate.
