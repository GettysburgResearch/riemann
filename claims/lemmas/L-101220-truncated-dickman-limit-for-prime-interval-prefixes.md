# L-101220 — Prime-interval reciprocal Möbius prefixes converge to a positive truncated Dickman semigroup

Claim ID: `L-101220`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-21  
Uses: Mertens' prime-reciprocal theorem  
RH status: **not assumed**

For primes `p<q`, put

\[
A_{p,q}(x)=
\sum_{\substack{d\le x\\
                  r\mid d\Rightarrow p<r<q}}
\frac{\mu(d)}d,
\tag{L-101220.1}
\]

where the sum is over squarefree products of the interior primes. Write

\[
a_{p,q}=\frac{\log q}{\log p}.
\]

## 1. The continuum interval sieve

For `a>=1`, let

\[
d\nu_a(v)=\mathbf1_{[1,a]}(v)\frac{dv}{v}
\]

and define the finite signed convolution exponential

\[
\mathfrak m_a=
\sum_{k\ge0}\frac{(-1)^k}{k!}\nu_a^{*k}.
\tag{L-101220.2}
\]

Its total variation is at most `a`. Put

\[
F_a(u)=\mathfrak m_a([0,u]),
\qquad F_a(u)=0\quad(u<0).
\]

The Laplace transform is

\[
\int e^{-su}\,d\mathfrak m_a(u)
=
\exp\!\left(-\int_1^a e^{-sv}\frac{dv}{v}\right).
\tag{L-101220.3}
\]

For `u>0`, inverse Laplace differentiation gives

\[
\boxed{
 uF_a'(u)=F_a(u-a)-F_a(u-1).
}
\tag{L-101220.4}
\]

Equivalently,

\[
\boxed{
 uF_a(u)=
 \int_{(u-1)_+}^{u}F_a(v)\,dv
 +\int_0^{(u-a)_+}F_a(v)\,dv.
}
\tag{L-101220.5}
\]

On `0<=u<=1`, `F_a(u)=1`. If `F_a` had a first zero at `u_0>0`, the right side of (L-101220.5) would be strictly positive. Therefore

\[
\boxed{F_a(u)>0\qquad(a>=1,\ u>=0).}
\tag{L-101220.6}
\]

For `u<=a`, the upper truncation is invisible and `F_a(u)` is the ordinary Dickman function `rho(u)`. Also

\[
\lim_{u\to\infty}F_a(u)
=
\mathfrak m_a([0,\infty))
=e^{-\nu_a([1,a])}=\frac1a.
\tag{L-101220.7}
\]

## 2. Convergence of the actual prime interval

Put

\[
v_\ell=\frac{\log\ell}{\log p},
\qquad
\mathfrak m_{p,q}
=
\mathop{*}_{p<\ell<q}
\left(\delta_0-\ell^{-1}\delta_{v_\ell}\right).
\tag{L-101220.8}
\]

Then exactly

\[
A_{p,q}(p^u)=\mathfrak m_{p,q}([0,u]).
\tag{L-101220.9}
\]

Fix `A>1`. For every sequence `p_j->infinity`, `q_j<=p_j^A`, pass to a subsequence with `a_(p_j,q_j)->a in [1,A]`. Mertens' theorem gives weak convergence of

\[
\sum_{p_j<\ell<q_j}\ell^{-1}\delta_{v_\ell}
\]

to `nu_a`. Moreover

\[
\sum_{\ell>p_j}\ell^{-2}=o(1),
\]

so the even and odd positive parts of the product measure in (L-101220.8) converge separately to the even and odd convolution exponentials in (L-101220.2). Hence, at every finite `u>0`,

\[
\mathfrak m_{p_j,q_j}([0,u])\longrightarrow F_a(u).
\tag{L-101220.10}
\]

This remains true when `u=u_j` converges.

The convergence is also tight uniformly in `q<=p^A`. Indeed, the total variation is

\[
\prod_{p<\ell<q}(1+\ell^{-1})=O_A(1),
\]

and its first logarithmic moment is

\[
O_A(1)\sum_{p<\ell<q}
\frac{\log\ell}{\ell\log p}=O_A(1).
\]

Thus the absolute tail beyond `u` is `O_A(1/u)`. The full signed mass is

\[
\prod_{p<\ell<q}(1-\ell^{-1})\longrightarrow\frac1a.
\tag{L-101220.11}
\]

Consequently, if `u_j->infinity`, then

\[
A_{p_j,q_j}(p_j^{u_j})\longrightarrow\frac1a>0.
\tag{L-101220.12}
\]

Combining the bounded- and unbounded-`u` alternatives proves:

\[
\boxed{
\text{For every fixed }A>1\text{ there is }p_0(A)
\text{ such that }
A_{p,q}(x)>0
}
\]

for every pair of primes

\[
p_0(A)\le p<q\le p^A
\]

and every real `x>=1`.

This is a dynamic sieve theorem: `p` grows with the endpoint interval. It does not assert eventual positivity for any one fixed Euler tail.
