# L-99613 — Every SHARP boundary power at least two is globally positive

Claim ID: `L-99613`  
Status: **PROVED UNCONDITIONAL ALL-REAL, ALL-SCALE POSITIVITY THEOREM**  
Created: 2026-08-20  
Depends on: PR #653 `L-99271`; elementary Euler products  
RH status: **not assumed**

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For a real `m>=1`, put

\[
\mathfrak H^{[m]}(x)
=\sum_{n\le x}{\beta(n)\over\sqrt n}T(x/n)^m.
\tag{L-99613.1}
\]

Then

\[
\boxed{
\mathfrak H^{[m]}(x)>0
\qquad(x\ge1,\ m\ge2).
}
\tag{L-99613.2}
\]

Thus an entire continuum of supercritical SHARP powers is positive.  The
quadratic endpoint `m=2` is the load-bearing threshold proved below; every
larger real power inherits the same labelled-level contraction.

## 1. A labelled native Euler cube

Let `mathcal L` contain one labelled copy of every prime except `67`, and two
labelled copies of `67`. For a finite subset `A` of labels, let

\[
n_A=\prod_{\ell\in A}p_\ell,
\qquad
w_m(A;x)=n_A^{-1/2}T(x/n_A)^m,
\]

with the convention that the weight is zero when `n_A>x`.

The two copies of `67` reproduce the local coefficients `(1,-2,1)`, while every
other prime contributes `(1,-1)`. Hence, exactly,

\[
\boxed{
\mathfrak H^{[m]}(x)
=\sum_{A\subset\mathcal L}(-1)^{|A|}w_m(A;x),
}
\tag{L-99613.3}
\]

where only finitely many subsets are active at fixed `x`. Every native source
coefficient occurs once; no contracted child or unrestricted reservoir is used.

## 2. Removing one labelled prime

Suppose `ell in A`, put `q=p_ell`, `B=A\setminus{ell}`, and `Y=x/n_B`.
If `A` is active then `Y>=q`, and

\[
T(Y)-\sqrt q\,T(Y/q)=3(\sqrt q-1)>0.
\]

Therefore

\[
\boxed{
{w_m(A;x)\over w_m(B;x)}
=q^{-1/2}\left({T(Y/q)\over T(Y)}\right)^m
<q^{-(m+1)/2}.
}
\tag{L-99613.4}
\]

## 3. Exact quadratic threshold and all powers `m>=2`

For real `m>=2`, let

\[
M_k^{(m)}(x)=\sum_{|A|=k}w_m(A;x)\ge0.
\]

Because `q^{-(m+1)/2}<=q^{-3/2}`, the quadratic labelled-prime sum controls
every such `m`.  To simplify notation write `M_k=M_k^(m)` below.

Double-counting every labelled removal and using (L-99613.4) gives

\[
\boxed{
kM_k(x)<S_2M_{k-1}(x),}
\tag{L-99613.5}
\]

where

\[
S_2=
\sum_{q\ {\rm prime}}q^{-3/2}+67^{-3/2}.
\tag{L-99613.6}
\]

The extra term is the second labelled copy of `67`.

We now prove `S_2<1` without numerical transcendental acceptance. Since

\[
\sum_q q^{-3/2}<\log\zeta(3/2)
\]

and `-log(1-u)>u`,

\[
S_2
<\log\!\left({\zeta(3/2)\over1-67^{-3/2}}\right).
\tag{L-99613.7}
\]

Convexity of `t^{-3/2}` on the unit intervals centered at the integers gives

\[
\zeta(3/2)
<1+\int_{3/2}^{\infty}t^{-3/2}dt
=1+2\sqrt{2/3}
<{8\over3},

where the last inequality follows from `2/3<25/36`.
\]

Also `sqrt(67)>8`, so `67^{-3/2}<1/536`, and hence

\[
{\zeta(3/2)\over1-67^{-3/2}}
<{8\over3}{536\over535}
={4288\over1605}.
\]

Finally

\[
e>1+1+{1\over2}+{1\over6}+{1\over24}+{1\over120}
={163\over60}.
\]

and

\[
{163\over60}-{4288\over1605}={289\over6420}>0.
\]

Thus the ratio in (L-99613.7) is below `e`, proving

\[
\boxed{S_2<1.}
\tag{L-99613.8}
\]

For every `j>=0`, (L-99613.5) now gives

\[
M_{2j+1}< {S_2\over2j+1}M_{2j}<M_{2j}.
\]

Pairing consecutive parity levels in the finite alternating sum yields

\[
\mathfrak H^{[m]}(x)
=(M_0-M_1)+(M_2-M_3)+\cdots>0.
\]

This proves (L-99613.2) for every real `m>=2`.

## 4. Independent cubic incoming-column strengthening

For completeness, the stronger pointwise owner ratio at `m=3` gives

\[
{T(Y/d)^3\over\sqrt d\,T(Y)^3}<d^{-2}.
\]

The complete incoming owner-column mass is therefore bounded by

\[
\rho_3
=\log\!\left({\zeta(2)\over1-67^{-2}}\right)<{1\over2}.
\]

The exact rational proof uses

\[
{\zeta(2)\over1-67^{-2}}
<{242\over147}{4489\over4488}
={49379\over29988}<\sqrt{19/7}<\sqrt e,
\]

where

\[
{19\over7}-\left({49379\over29988}\right)^2
={2617607\over899280144}>0.
\]

Thus the unit cubic source strictly dominates the complete nonunit source,
giving an independent stronger proof at `m=3`.

## 5. Significance

The continuum theorem for every `m>=2` is a genuine global result immediately adjacent to the
RH-sensitive linear transform. `R-99611` proves that the gap between powers two
and one is nevertheless structural: the labelled prime mass is finite and
subunit at exponent `3/2`, but becomes the divergent prime-harmonic mass at the
critical linear exponent one.
