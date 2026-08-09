# L-34001 — Raw Brownian factor = zero-free gamma ratio times a Dirichlet-average Mellin transform

Claim ID: `L-34001`  
Title: The one-sided finite Brownian gamma truncation reduces exactly to the Mellin transform of a bounded Dirichlet average  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Issue: #340  
Dependencies: PR #296 `L-21705` only for notation and the raw convergence theorem  
Scope: exact finite probability/Mellin factorization; no all-N stability or RH conclusion

## 1. Raw Brownian gamma truncation

Let

\[
S_N=\sum_{j=1}^N\frac{\Gamma_{2,j}}{j^2},
\]

where the gamma variables are independent, shape two, unit rate. Put

\[
m_N(s)=\pi^{-s/2}\mathbb E[S_N^{s/2}].
\]

PR #296 writes

\[
\boxed{
m_N(s)=\pi^{-s/2}\Gamma(1+s/2)D_N(s),
}
\tag{L-34001.1}
\]

where `D_N` is the explicit finite Dirichlet/exponential polynomial of `L-21705`.

## 2. Beta-gamma decomposition

Let

\[
G_N=\sum_{j=1}^N\Gamma_{2,j}.
\]

Since all summands have the same unit rate,

\[
G_N\sim\Gamma(2N,1).
\]

Put

\[
W_j=\frac{\Gamma_{2,j}}{G_N}.
\]

The standard beta-gamma factorization gives

\[
(W_1,\ldots,W_N)\sim\operatorname{Dirichlet}(2,\ldots,2),
\]

and the vector `W` is independent of `G_N`.

Define the bounded Dirichlet average

\[
\boxed{
Q_N=\sum_{j=1}^N\frac{W_j}{j^2}.
}
\tag{L-34001.2}
\]

Then exactly

\[
\boxed{S_N=G_NQ_N.}
\tag{L-34001.3}
\]

Moreover

\[
\frac1{N^2}\le Q_N\le1
\]

almost surely. Therefore

\[
M_N(z):=\mathbb E[Q_N^z]
\]

is an entire function of `z`.

## 3. Exact Mellin factorization

For `Re z>-2N`, independence gives

\[
\mathbb E[S_N^z]
=\mathbb E[G_N^z]\mathbb E[Q_N^z]
=\frac{\Gamma(2N+z)}{\Gamma(2N)}M_N(z).
\]

Taking `z=s/2` and comparing with (L-34001.1) yields

\[
\boxed{
D_N(s)
=\frac{\Gamma(2N+s/2)}
       {\Gamma(2N)\Gamma(1+s/2)}
  M_N(s/2).
}
\tag{L-34001.4}
\]

Equivalently,

\[
\boxed{
D_N(2z)
=\frac{\Gamma(2N+z)}
       {\Gamma(2N)\Gamma(1+z)}
  \mathbb E[Q_N^z].
}
\tag{L-34001.5}
\]

Both sides are meromorphic/entire continuations of the same expression, so the identity extends wherever either side is defined.

The gamma ratio in (L-34001.4) has no zeros in

\[
\operatorname{Re}s>\frac12.
\]

Consequently

\[
\boxed{
D_N(s)\ne0\text{ for Re }s>1/2
\iff
M_N(z)\ne0\text{ for Re }z>1/4.
}
\tag{L-34001.6}
\]

This removes the partial-fraction and cardinal derivative coefficients from the one-sided stability problem completely.

## 4. Direct RH consequence of cofinal raw stability

PR #296 `L-21705` proves, uniformly on the closed critical strip,

\[
|m_N(s)-2\xi(s)|\le\frac{|s|}{N}.
\]

Suppose an unbounded sequence `N_k` satisfies

\[
M_{N_k}(z)\ne0
\qquad(\operatorname{Re}z>1/4).
\tag{L-34001.7}
\]

Then (L-34001.4) says `m_(N_k)` is zero-free in `Re s>1/2` inside the critical strip. If `xi` had a zero `rho` with `Re rho>1/2`, choose a small disk around `rho` contained in that half-strip and with zero-free boundary. Uniform convergence and Rouché force `m_(N_k)` to contain a zero in that disk for all sufficiently large `k`, contradiction.

Therefore

\[
\boxed{
\text{cofinal raw Dirichlet-average stability}\Longrightarrow\mathrm{RH}.
}
\tag{L-34001.8}
\]

This uses the one-sided raw truncations. It does not require the symmetrized finite approximants to be real-rooted; their known off-line finite pairs are therefore not a contradiction to this route.

## 5. Why this is a different frontier

The finite random variable `Q_N` is simply a Dirichlet average of the deterministic knots

\[
1,\frac14,\frac19,\ldots,\frac1{N^2}.
\]

Thus the full one-sided RH problem is reduced to a zero-free theorem for

\[
\boxed{
M_N(z)=\mathbb E\left[
\left(\sum_{j=1}^N\frac{W_j}{j^2}\right)^z
\right],
\quad W\sim\mathrm{Dirichlet}(2,\ldots,2).
}
\]

Possible proof mechanisms now concern one bounded positive B-spline/Dirichlet-average law: total positivity, variation diminution after logarithmic change, a canonical system, or direct Mellin geometry.

## 6. Proof boundary

Established exactly:

1. beta-gamma decomposition of `S_N`;
2. bounded Dirichlet average `Q_N`;
3. exact factorization (L-34001.4);
4. equivalence of raw half-plane stability with `M_N` zero-freeness;
5. cofinal stability implies RH.

Open:

1. zero-freeness of `M_N` in `Re z>1/4` for an unbounded sequence;
2. RH.
