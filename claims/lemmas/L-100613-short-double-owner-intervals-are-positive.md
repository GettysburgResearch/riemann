# L-100613 — Every ratio-eight double-owner cubic interval is positive

Claim ID: `L-100613`  
Status: **PROVED UNCONDITIONAL ALL-SCALE INTERVAL THEOREM — AUDITED FOR THE DUPLICATED 67 LABEL**  
Created: 2026-08-20  
Audited: 2026-08-21  
Depends on: `L-100612`; the labelled-prime level-pairing method  
RH status: **not assumed**

Let `Psi` be the cubic critical kernel, and for endpoint labels with prime
values `p<q` put

\[
K_{p,q}(y)=(I-U_p)(I-U_q)\Psi(y).
\tag{L-100613.1}
\]

By `L-100612`, `K_(p,q)(y)>=0` for every `y>0`.

## 1. A universal interior-label Harnack bound

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
\boxed{g(u-c)\le\frac43g(u).}
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

Applying (L-100613.3) with `c=log ell` proves, for every labelled prime
`ell>=2`,

\[
\boxed{
ell^{-1/2}K_{p,q}(y/\ell)
\le
\frac4{3\ell}K_{p,q}(y).}
\tag{L-100613.5}
\]

This estimate is source-normalized: the factor `ell^(-1/2)` is the literal
native Möbius activity of the interior label.

## 2. Labelled prime-harmonic mass in a ratio-eight interval

Assume

\[
67\le p<q\le8p.
\]

For distinct prime values, every prime at least five is congruent to `1` or
`-1` modulo six. Monotone integral comparison on the two progressions gives

\[
\sum_{p<\ell<q\atop \ell\ {m prime\ value}}\frac1\ell
\le
\frac2p+\frac13\log8.
\tag{L-100613.6}
\]

There is one additional labelled-prime possibility which the original
statement omitted. The duplicate-67 source contains two distinct coordinates
of prime value `67`. If the lower endpoint is the first copy, the second copy
may lie in the ordered interior even though its prime value equals `p`. This
adds at most `1/p` to the labelled reciprocal mass. Hence, uniformly over all
ordered endpoint labels,

\[
\sum_{p<_{\rm label}\ell<_{\rm label}q}\frac1\ell
\le
\frac3p+\frac13\log8.
\tag{L-100613.7}
\]

Using `p>=67` and `log2<7/10`,

\[
\frac43
\sum_{p<_{\rm label}\ell<_{\rm label}q}\frac1\ell
<
\frac4{67}+\frac49\frac{21}{10}
=
\frac4{67}+\frac{14}{15}
=
\frac{998}{1005}<1.
\tag{L-100613.8}
\]

Thus the strict contraction survives the duplicated label.

## 3. Complete interior Euler positivity

Let the interior labelled primes be

\[
p<_{\rm label}\ell_1<_{\rm label}\cdots<_{\rm label}\ell_m<_{\rm label}q
\]

and define

\[
\mathcal I_{p,q}(y)
=
\prod_{r=1}^{m}(I-\ell_r^{-1/2}U_{\ell_r})K_{p,q}(y).
\tag{L-100613.9}
\]

At fixed `y`, let `M_d(y)` be the total unsigned weight of Euler level `d` in
(L-100613.9). Removing one selected interior label and using (L-100613.5)
gives

\[
dM_d(y)
\le
\Sigma_{p,q}M_{d-1}(y),
\qquad
\Sigma_{p,q}
=
\frac43\sum_{p<_{\rm label}\ell<_{\rm label}q}\frac1\ell
<1.
\tag{L-100613.10}
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
\prod_{p<_{\rm label}\ell<_{\rm label}q}
(I-\ell^{-1/2}U_\ell)
(I-U_p)(I-U_q)\Psi(y)
\ge0}
\tag{L-100613.11}
\]

for every `y>0`, every ordered pair of actual endpoint labels whose prime
values satisfy `67<=p<q<=8p`, and the exact finite interior label multiset. The
inequality is strict whenever the endpoint kernel is nonzero.

When the two endpoints are the two copies of `67`, the interior is empty and
`L-100612` applies directly.

## Matrix consequence

The entire short-interval region of the audited implication matrix is closed:

```text
empty/adjacent intervals                  positive by L-100612;
all distinct-value endpoint ratios <=8    positive by this theorem;
duplicated-67 orderings                    included by the audited label budget;
only genuinely wider endpoint intervals   remain in the arithmetic frontier.
```

No finite scan, source-blind collapse, or RH-scale estimate enters this
result.