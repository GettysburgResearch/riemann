# L-97901 — Every fixed power-scale native rough state has a uniform positive Dickman asymptotic

Claim ID: `L-97901`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: PR #587 exact annular base theorem; `L-97900`  
RH status: **not assumed**

Let `b(Y)=F_61(Y)` be the complete grouped finite-`P_61` annular `5:3`
scalar. Use the frozen asymptotic

\[
b(Y)=a\sqrt Y+c+O(Y^{-3/2}),
\qquad
 a=12\prod_{p\le61}(1-1/p)>0,
\tag{L-97901.1}
\]

and zero-extend `b` below its support.

For a real threshold `z>=67`, define the literal native state

\[
\mathcal F(Y,z)=
\sum_{\substack{m\text{ squarefree}\\P^-(m)\ge z}}
\frac{\mu(m)}{\sqrt m}\,b(Y/m).
\tag{L-97901.2}
\]

Every source coefficient, activation and cumulative parity is the native one.

Fix `theta in (0,1)`. Uniformly for

\[
Y^\theta\le z\le Y,
\qquad
u=\frac{\log Y}{\log z}\in[1,1/\theta],
\]

one has

\[
\boxed{
\mathcal F(Y,z)
=a\sqrt Y\,\mathfrak D(\nu)+o_\theta(\sqrt Y),
}
\tag{L-97901.3}
\]

where `mathfrak D` is the positive Dickman function of `L-97900`. Consequently,
for all sufficiently large `Y`, uniformly over the same thresholds,

\[
\boxed{
\mathcal F(Y,z)
\ge \frac a2\mathfrak D(1/\theta)\sqrt Y>0.
}
\tag{L-97901.4}
\]

This removes the earlier restriction `theta>e^(-1)`: every fixed positive
power threshold is eventually safe.

## Proof

### 1. Uniform finite rough depth

If `P^-(m)>=z>=Y^theta` and `m<=Y`, then

\[
\omega(m)\le K_\theta:=\lfloor1/\theta\rfloor.
\]

Thus every sum below has uniformly bounded degree.

### 2. The non-square-root pieces are lower order

For `k>=1`, put

\[
A_k(Y,z)=
\sum_{\substack{z\le p_1<\cdots<p_k\\p_1\cdots p_k\le Y}}
(p_1\cdots p_k)^{-1/2}.
\]

The prime number theorem gives `A_1(Y,z)<<sqrt(Y)/log Y`. Inductively,

\[
kA_k(Y,z)
\le
\sum_{z\le p\le Y/z^{k-1}}p^{-1/2}A_{k-1}(Y/p,z).
\]

Since `log(Y/p)>=(k-1)theta log Y` in this range, the induction hypothesis and
Mertens' prime-harmonic bound yield

\[
\boxed{A_k(Y,z)\ll_\theta\frac{\sqrt Y}{\log Y}}
\tag{L-97901.5}
\]

uniformly for `k<=K_theta`. Therefore

\[
\sum_{m}m^{-1/2}\ll_\theta\frac{\sqrt Y}{\log Y},
\qquad
\sum_m m\ll_\theta\frac{Y^2}{\log Y},
\tag{L-97901.6}
\]

apart from the harmless unit atom.

Substituting (L-97901.1) into (L-97901.2), using (L-97901.6), and treating the
fixed compact range of `Y/m` directly gives

\[
\mathcal F(Y,z)
=a\sqrt Y\,S(Y,z)+o_\theta(\sqrt Y),
\tag{L-97901.7}
\]

where

\[
S(Y,z)=
\sum_{\substack{m\le Y\\m\text{ squarefree}\\P^-(m)\ge z}}
\frac{\mu(m)}m.
\tag{L-97901.8}
\]

Changing the upper boundary by any fixed multiplicative factor changes
`S(Y,z)` by `o_theta(1)`.

### 3. Prime-harmonic measure converges to `ds/s`

On the compact interval `[1,1/theta]`, define

\[
\nu_{Y,z}=\sum_{z\le p\le Y}\frac1p\,
\delta_{\log p/\log z}.
\]

Mertens' theorem gives, uniformly for `1<=alpha<=beta<=1/theta`,

\[
\nu_{Y,z}([\alpha,\beta])
=\log(\beta/\alpha)+o_\theta(1).
\tag{L-97901.9}
\]

Hence `nu_(Y,z)` converges weakly, uniformly in the permitted thresholds, to
`ds/s`. Repeated primes have total weight

\[
O\!\left(\sum_{p\ge z}p^{-2}\right)=o_\theta(1).
\]

For each fixed `k`, the degree-`k` part of (L-97901.8) therefore converges to

\[
\frac1{k!}
\int_{\substack{s_i\ge1\\s_1+\cdots+s_k\le\nu}}
\frac{ds_1\cdots ds_k}{s_1\cdots s_k}.
\]

Summing the finitely many degrees gives

\[
S(Y,z)=\mathfrak D(\nu)+o_\theta(1).
\tag{L-97901.10}
\]

Equations (L-97901.7), (L-97901.10), and `L-97900` prove the theorem.
