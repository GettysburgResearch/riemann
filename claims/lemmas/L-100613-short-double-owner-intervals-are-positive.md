# L-100613 — Every ratio-eight double-owner cubic interval is positive

Claim ID: `L-100613`  
Status: **PROVED UNCONDITIONAL ALL-SCALE INTERVAL THEOREM**  
Created: 2026-08-20  
Depends on: `L-100612`; the labelled-prime level-pairing method  
RH status: **not assumed**

Let `Psi` be the cubic critical kernel, and for endpoint primes `p<q` put

\[
K_{p,q}(y)
=
(I-U_p)(I-U_q)\Psi(y).
\tag{L-100613.1}
\]

By `L-100612`, `K_(p,q)(y)>=0` for every `y>0`.

## 1. A universal interior-prime Harnack bound

Write

\[
\phi(u)=\Psi(e^u)
\]

and

\[
g(u)=e^{-u/2}\phi''(u).
\]

The explicit cubic kernel gives

\[
g(u)=
\begin{cases}
48[4e^{u/2}-3e^u],&u\le0,\\
48,&u\ge0.
\end{cases}
\tag{L-100613.2}
\]

For every `c>=0` and every real `u`,

\[
\boxed{
g(u-c)\le\frac43g(u).}
\tag{L-100613.3}
\]

For `u>=0`, this follows from `0<=g<=64`. For `u<0`, put
`x=e^(u/2)` and `alpha=e^(-c/2)`. The ratio is

\[
\frac{g(u-c)}{g(u)}
=
\frac{\alpha(4-3\alpha x)}{4-3x}.
\]

It increases with `x in (0,1]`; at `x=1` its maximum over
`0<=alpha<=1` is `4/3`, attained at `alpha=2/3`.

Let `a=log p`, `b=log q`. The Peano representation gives

\[
K_{p,q}(e^u)
=
\int_0^a\int_0^b\phi''(u-s-t)\,dt\,ds
\]

and therefore

\[
K_{p,q}(e^u)
=
e^{u/2}
\int_0^a\int_0^b
 e^{-(s+t)/2}g(u-s-t)\,dt\,ds.
\tag{L-100613.4}
\]

Applying (L-100613.3) with `c=log ell` proves, for every `ell>=2`,

\[
\boxed{
\ell^{-1/2}K_{p,q}(y/\ell)
\le
\frac4{3\ell}K_{p,q}(y).
}
\tag{L-100613.5}
\]

This estimate is source-normalized: the factor `ell^(-1/2)` is the literal
native Möbius activity of the interior prime.

## 2. Prime-harmonic mass in a ratio-eight interval

Assume

\[
67\le p<q\le8p.
\]

Every prime between `p` and `q` is congruent to `1` or `-1` modulo `6`. For a
decreasing function, integral comparison on each arithmetic progression gives

\[
\sum_{\substack{p<\ell<q\\\ell\ {m prime}}}\frac1\ell
\le
\frac2p+\frac13\log8.
\tag{L-100613.6}
\]

Using `p>=67` and the elementary bound `log 2<7/10`,

\[
\frac43
\sum_{p<\ell<q}\frac1\ell
<
\frac8{201}+\frac49\frac{21}{10}
=
\frac{2934}{3015}
<1.
\tag{L-100613.7}
\]

## 3. Complete interior Euler positivity

Let the interior labelled primes be

\[
p<\ell_1<\cdots<\ell_m<q
\]

and define

\[
\mathcal I_{p,q}(y)
=
\prod_{r=1}^{m}(I-\ell_r^{-1/2}U_{\ell_r})K_{p,q}(y).
\tag{L-100613.8}
\]

At fixed `y`, let `M_d(y)` be the total unsigned weight of Euler level `d` in
(L-100613.8). Removing one selected interior label and using (L-100613.5)
gives

\[
dM_d(y)
\le
\Sigma_{p,q}M_{d-1}(y),
\qquad
\Sigma_{p,q}
=
\frac43\sum_{p<\ell<q}\frac1\ell
<1.
\tag{L-100613.9}
\]

Hence

\[
M_{2r+1}(y)
\le
\frac{\Sigma_{p,q}}{2r+1}M_{2r}(y)
<
M_{2r}(y).
\]

Pairing consecutive parity levels proves

\[
\boxed{
\prod_{p<\ell<q}
(I-\ell^{-1/2}U_\ell)
(I-U_p)(I-U_q)\Psi(y)
\ge0
}
\tag{L-100613.10}
\]

for every `y>0`, every pair of actual primes `67<=p<q<=8p`, and the exact
finite interior prime set. The inequality is strict whenever the endpoint
kernel is nonzero.

The repeated labelled `67` case has empty interior and is already covered by
`L-100612`.

## Matrix consequence

The entire short-interval region of `T-100611` is now closed without a finite
scan, a source-blind collapse, or an RH-scale estimate:

```text
empty/adjacent intervals          positive by L-100612;
all endpoint ratios <=8           positive by L-100613;
only endpoint ratios >8           remain in FOCR100610 / LOCR100610.
```

Thus both Schur gates may be restricted to long prime intervals, where the
source-faithful finite-squaring and positive-renewal tools of PR #691 apply.