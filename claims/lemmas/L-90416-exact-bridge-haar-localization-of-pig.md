# L-90416 — Exact bridge–Haar localization of the compact-Q4 PIG Gram

Claim ID: `L-90416`  
Title: Every continuous carry field is a symmetric discrete bridge; its Haar coefficients are reflected triangular source sums, and all spatial scales at most the square-root scale are unconditionally at PIG size  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM + UNCONDITIONAL Q4 FINE-SCALE APPLICATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90411`, `L-90412`; elementary discrete Haar algebra  
Scope: the complete continuous-position carry Gram at one integer endpoint; it does not bound the mean or coarse Haar coefficients and does not prove deterministic PIG or RH

## 1. Carry fields are symmetric discrete bridges

Let `N=2^M`, let `c(1),...,c(N)` be an arbitrary complex sequence, and put

\[
 C(r)=\sum_{m\le r}c(m),\qquad C(0)=0.
\]

Define the continuous carry field

\[
 Q_{c,N}(\theta)
 =C(N)-C(\lfloor N\theta\rfloor)
       -C(\lfloor N(1-\theta)\rfloor),
 \qquad 0<\theta<1.
\tag{L-90416.1}
\]

On the open cell

\[
 \frac jN<\theta<\frac{j+1}{N},
 \qquad 0\le j<N,
\]

one has exactly

\[
 \boxed{
 R_j:=Q_{c,N}(\theta)=C(N)-C(j)-C(N-j-1).
 }
\tag{L-90416.2}
\]

Consequently

\[
 \boxed{R_{N-1-j}=R_j}
\tag{L-90416.3}
\]

and

\[
 \boxed{
 R_j-R_{j-1}=c(N-j)-c(j),
 \qquad 1\le j<N.
 }
\tag{L-90416.4}
\]

Thus the PIG field is the symmetric bridge whose discrete derivative is the source reflected about the endpoint.

The continuous energy is exactly

\[
 \boxed{
 \int_0^1|Q_{c,N}(\theta)|^2\,d\theta
 =\frac1N\sum_{j=0}^{N-1}|R_j|^2.
 }
\tag{L-90416.5}
\]

## 2. Standard Haar coefficients

For a dyadic half-length `ell=2^r`, `1<=ell<=N/2`, and a standard Haar base point

\[
 u\in\{0,2\ell,4\ell,\ldots,N-2\ell\},
\]

define

\[
 H_{u,\ell}(R)
 =\frac1{\sqrt{2\ell}}
 \left(
 \sum_{j=u}^{u+\ell-1}R_j
 -\sum_{j=u+\ell}^{u+2\ell-1}R_j
 \right).
\tag{L-90416.6}
\]

Let

\[
 w_\ell(t)=\min(t,2\ell-t),
 \qquad 1\le t<2\ell,
\]

and define the triangular source functional

\[
 T_{u,\ell}(c)
 =\sum_{t=1}^{2\ell-1}w_\ell(t)c(u+t).
\tag{L-90416.7}
\]

Summation of the bridge differences (L-90416.4) gives the exact identity

\[
 \boxed{
 H_{u,\ell}(R)
 =\frac{
 T_{u,\ell}(c)
 -T_{N-u-2\ell,\ell}(c)
 }{\sqrt{2\ell}}.
 }
\tag{L-90416.8}
\]

Equivalently,

\[
 H_{u,\ell}(R)
 =-\frac1{\sqrt{2\ell}}
 \sum_{t=1}^{2\ell-1}
 w_\ell(t)
 \bigl[R_{u+t}-R_{u+t-1}\bigr].
\tag{L-90416.9}
\]

So every Haar coefficient is the difference of two equal triangular windows, reflected about `N/2`. There is no unidentified physical-to-arithmetic map.

## 3. Exact Haar Parseval

The constant coefficient is

\[
 \overline R=\frac1N\sum_{j=0}^{N-1}R_j.
\]

Discrete Haar orthogonality and (L-90416.5) give

\[
 \boxed{
 \int_0^1|Q_{c,N}(\theta)|^2\,d\theta
 =|\overline R|^2
 +\frac1N\sum_{\ell}
  \sum_{u\equiv0\pmod{2\ell}}
  |H_{u,\ell}(R)|^2.
 }
\tag{L-90416.10}
\]

This is a spatial counterpart of the inverse-circle-Laplacian diagonalization in `L-90411`. The Fourier major arc becomes the mean plus the coarse Haar tree.

## 4. Fine Haar scales are generically easy

The triangular weights have the exact square mass

\[
 \boxed{
 \sum_{t=1}^{2\ell-1}w_\ell(t)^2
 =\frac{2\ell^3+\ell}{3}.
 }
\tag{L-90416.11}
\]

Cauchy–Schwarz in (L-90416.9) gives

\[
 |H_{u,\ell}(R)|^2
 \le
 \frac{2\ell^2+1}{6}
 \sum_{t=1}^{2\ell-1}
 |c(N-u-t)-c(u+t)|^2.
\tag{L-90416.12}
\]

At a fixed Haar scale the open intervals appearing on the right are disjoint. Hence, for every dyadic cutoff `L<=N/2`,

\[
 \boxed{
 \sum_{\substack{\ell\le L\\\ell\text{ dyadic}}}
 \sum_u |H_{u,\ell}(R)|^2
 \le
 L^2\sum_{j=1}^{N-1}|c(N-j)-c(j)|^2
 \le
 4L^2\sum_{m=1}^{N-1}|c(m)|^2.
 }
\tag{L-90416.13}
\]

The first constant is deliberately nonoptimal but uniform and elementary.

After division by `N`,

\[
 \boxed{
 \mathcal E_{\rm Haar,fine}(N;L)
 \le\frac{4L^2}{N}
       \sum_{m<N}|c(m)|^2.
 }
\tag{L-90416.14}
\]

## 5. Apply to the compact-Q4 innovation

For the actual compact innovation prefix coefficient,

\[
 c_\circ(m)
 =\Lambda(m)
 -4\mathbf1_{4\mid m}\Lambda(m/4)
 +3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r},
\tag{L-90416.15}
\]

`L-90412` proves unconditionally

\[
 \sum_{m<N}|c_\circ(m)|^2\ll N\log(2N).
\tag{L-90416.16}
\]

Take the largest dyadic `L<=sqrt(N)`. Equations (L-90416.14)--(L-90416.16) give

\[
 \boxed{
 \mathcal E_{\rm Haar,fine}(N;\sqrt N)
 \ll N\log(2N).
 }
\tag{L-90416.17}
\]

After the PIG normalization by `N`, the whole fine Haar tree contributes only

\[
 \boxed{O(\log(2N)).}
\tag{L-90416.18}
\]

This is unconditional and uses no zero-free region, prime correlation estimate, or random-sign comparison.

## 6. Exact surviving dimension

The number of standard Haar coefficients with

\[
 \ell>\sqrt N
\]

is

\[
 \sum_{\ell>\sqrt N}\frac{N}{2\ell}<\sqrt N.
\tag{L-90416.19}
\]

Therefore deterministic PIG has now been reduced in a second exact coordinate to

```text
one mean coefficient
+
fewer than sqrt(N) coarse reflected triangular prime windows.
```

This matches the dimension of the Fourier major-mode reduction but replaces global additive characters by local triangular windows.

## 7. Proof boundary

Closed exactly here:

1. cellwise bridge representation;
2. reflection and first-difference identities;
3. exact continuous/discrete energy equality;
4. exact Haar Parseval;
5. exact reflected triangular-window formula;
6. generic fine-scale energy estimate;
7. unconditional PIG-size control of every Haar scale at most `sqrt(N)`;
8. fewer than `sqrt(N)` surviving coarse coefficients.

Open:

1. the mean coefficient;
2. the coarse triangular-window square function;
3. deterministic PIG;
4. the repaired global PIG-to-pole adapter identified by PR #371;
5. RH.
