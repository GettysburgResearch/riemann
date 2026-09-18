# 05 — Spectral synthesis and a prescribed logarithmic mollifier

Source U5/A5, full retained source stage 03. Status: proposed implications and
finite identity checks. No required asymptotic upper bound is proved. The
method lies in established Nyman--Beurling/shifted-Mobius theory [B18, B02, BCF12].

## The stronger structural question

Let Z be the CLOSED span of h_{rho,j}=partial_{conj(z)}^j h_z at right-side zeros,
for 0<=j<m_rho. Differentiating the transform identity proves

    Z subset B-perp;
    Z-perp={f in H : (T f)/zeta is holomorphic on Re s>1/2}.

The proposal is equality Z=B-perp, equivalently that analytic divisibility
implies approximability in this discrete space. It needs closure and
multiplicity-derivative kernels. The corresponding question is recorded in
Balazard [B18, Question 2]. This packet does not establish the converse or claim
an exhaustive current literature resolution. Classical NB--Baez-Duarte theory
already gives RH iff 1 belongs to B; the stronger synthesis is not needed for
that equivalence. The investigation therefore did not make synthesis a
prerequisite to constructing an explicit family.

## Fix the coefficients

For integer N>=2,

$$
c^\log_{N,n}=-\mu(n)(1-\log n/\log N),\quad
U_N=\sum_{n=2}^N c^\log_{N,n}b_n,\quad u_N=1-U_N,\quad Q_N=\|u_N\|^2.
$$

These are not the projection coefficients, and Q_N need not decrease. E_N<=Q_N.
With V_N(s)=sum_{n<=N}mu(n)(1-log n/log N)n^{-s},

    P_N(s)=V_N(s)-V_N(1), T U_N(s)=zeta(s)P_N(s), P_N(1)=0.

This is a pole-canceled version of the classical logarithmic mollifier. The
sharp result [BCF12] assumes RH AND a reciprocal-derivative hypothesis; it is
not an unconditional input here.

Define

$$
\Lambda_N(m)=\sum_{d\mid m,d\le N}\mu(d)\log(N/d),\quad
T_N^{\rm scalar}=\sum_{d\le N}\frac{\mu(d)}d\log(N/d),\quad
\Psi_N(k)=\sum_{m\le k}\Lambda_N(m).
$$

For every k,

$$
U_N(k)=\frac{\Psi_N(k)-kT_N^{\rm scalar}}{\log N},\qquad
u_N(k)=\frac{\log N+kT_N^{\rm scalar}-\Psi_N(k)}{\log N}.
$$

For k<=N, divisor inversion gives Psi_N(k)=log N+psi(k), hence

$$
u_N(k)=\frac{kT_N^{\rm scalar}-\psi(k)}{\log N}.
$$

The divisor sum Lambda_N is the
truncated von Mangoldt sum appearing in Goldston--Yildirim [GY01]. No
fixed-shift correlation theorem from that literature is silently upgraded to
the cumulative weighted estimate needed below.

The elementary identities sum_{d<=N}mu(d)floor(N/d)=1 and
sum_{d<=N}mu(d)H_{floor(N/d)}/d=1 imply |T_N^scalar|<5, using the harmonic-number
remainder. Chebyshev's elementary psi(k)<3k then gives |u_N(k)|<=8k/log N for
k<=N. Thus U_N(k)->1 at every fixed coordinate without RH.

## A simple exact cutoff

Since sum_{n=2}^N|c^log_{N,n}|<=N/log N,

$$
0\le Q_N-\sum_{k\le N^2}\frac{|u_N(k)|^2}{k(k+1)}
\le4/(\log N)^2.
$$

This uses the pointwise bound |u_N(k)|<=1+N/log N and telescoping weights.
It is specific to this prescribed family, simpler than the optimal-family
large-sieve theorem. Put

$$
R_N^{\rm arith}=\sum_{k\le N^2}
\frac{|\Psi_N(k)-kT_N^{\rm scalar}-\log N|^2}{k(k+1)}.
$$

Then R_N^arith/log^2 N <= Q_N <= (R_N^arith+4)/log^2 N.

## Length averaging: the growth-to-zero-free lemma

**Proposed component lemma, with proof:** if Q_N=O(N^{2 alpha}), alpha>=0,
for all sufficiently large N, then zeta is zero-free on Re s>1/2+alpha.

Extend U_N to real x>1 by the same logarithmic weights and set U_x=0 for
1<x<2. For N<=x<N+1,

    (log x)U_x=(log N)U_N+log(x/N)(-sum_{n=2}^N mu(n)b_n).

Since ||b_n||<=sqrt(2/n), the correction is O(N^{-1/2}) in H. Hence the assumed
integer bound gives ||U_x||=O(x^alpha). For real a>alpha the Bochner integral

$$
F_a=\int_1^\infty(\log x)U_x x^{-a-1}dx
$$

converges in H, so T F_a is holomorphic on Re s>1/2. In Re s>1, absolute
convergence and integral_n^infinity log(x/n)x^{-a-1}dx=n^{-a}/a^2 give

$$
\boxed{\mathcal T F_a(s)=\frac{\zeta(s)}{a^2}
\left(\frac1{\zeta(s+a)}-\frac1{\zeta(1+a)}\right).}
$$

The pole at s=1 is canceled by the bracket. If rho is a zero with
Re rho>1/2+alpha, choose alpha<a<Re rho-1/2 avoiding the discrete set where
zeta(rho-a)=0. At s=rho-a the right side has a genuine pole (multiplicity
retained) whereas the left side is holomorphic. This contradiction proves the
lemma. The computation initially uses reciprocal Dirichlet series only in
their half-planes of absolute convergence; no contour crossing of unaccounted
zeros is used.

Consequently Q_N=N^{o(1)} would suffice for RH. Even a bound
Q_N<<exp(C sqrt(log N)) would suffice. These upper bounds are NOT proved. This
argument needs all sufficiently large lengths, not merely a sparse good
subsequence. It is a shifted-Mobius analytic mechanism, not a new externally
accepted criterion or a proof of its hypothesis.

## How a hypothetical zero would force energy outward

For rho=1/2+delta+i gamma, delta>0, the exact relations are
< U_N,h_rho>=0 and <u_N,h_rho>=1. Meanwhile u_N tends to zero on every fixed
prefix. The kernel tail bound is

$$
\|h_\rho 1_{k>J}\|^2\le\frac{|\rho|^2}{2\delta}(J+1)^{-2\delta}.
$$

Choosing J=floor(log N), the head estimate tends to zero and Cauchy--Schwarz
gives eventually Q_N >= delta*(log N)^{2delta}/(2|rho|^2). The length-averaging
lemma separately implies

    limsup log(1+Q_N)/log N >= 2 delta.

The first is an eventual logarithmic lower bound, the second a subsequence
polynomial-growth obstruction. They are not the same assertion. Constants and
onset can depend badly on a high zero, so this is not a practical finite detector.

## The finite signed correlation that remains

Set a_N(m)=Lambda_N(m)-T_N^scalar-(log N)1_{m=1}. Finite rearrangement gives

$$
\sum_{k\le K}\frac{|\sum_{m\le k}a_N(m)|^2}{k(k+1)}
=\sum_{a,b\le K}a_N(a)a_N(b)
\left(\frac1{\max(a,b)}-\frac1{K+1}\right).
$$

A sufficient target is R_N^arith <<_epsilon (log N)^2 N^epsilon for EVERY
epsilon>0, or the single upper bound (log N)^2 exp(C sqrt(log N)). Neither is
proved. The kernel is a cumulative signed second moment, not an ordinary
uncentered second moment of Lambda_N. Independence of increments would be an
extra unproved assumption.

Taking absolute values gives only ||U_N||<=4 sqrt(2N)/log N and
Q_N<=(1+4 sqrt(2N)/log N)^2=O(N/log^2 N). The growth lemma then reaches only
the already known half-plane Re s>1. This is the elementary calculation's
boundary, not a claim that no stronger literature result exists.
