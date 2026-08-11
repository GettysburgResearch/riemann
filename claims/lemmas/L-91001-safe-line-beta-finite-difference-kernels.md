# L-91001 — Beta finite differences of the one-safe-line hierarchy are positive zero kernels

Claim ID: `L-91001`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-90903` and its normalized kernel expansion  
RH status: **unproved**

## 1. Normalized single-line moments

Let

\[
\mathfrak S_k(x)
=-\Re\mathcal H_k\!\left(\frac12+ix\right)
\]

be the one-safe-line scalar of `T-90903`, and normalize by

\[
\boxed{
 a_k(x)=\frac{\mathfrak S_k(x)}{(k+2)!}.
}
\tag{L-91001.1}
\]

If `u=gamma-x` for a critical-line zero and `z=rho-(1/2+ix)` for one right-side member of an off-line reflected pair, the exact zero expansion is

\[
\boxed{
\begin{aligned}
 a_k(x)
={}&\sum_{\rho=1/2+i\gamma}
 m_\rho\frac{2u^2}{(1+u^2)^{k+3}}\\
 &-4\sum_{\Re\rho>1/2}
 m_\rho\Re\frac{z^2}{(1-z^2)^{k+3}}.
\end{aligned}}
\tag{L-91001.2}
\]

Both sums converge absolutely.

## 2. Exact beta finite differences

For integers `k,m>=0`, put

\[
\boxed{
 D_{k,m}(x)
 =(-1)^m\Delta^m a_k(x)
 =\sum_{j=0}^m(-1)^j\binom mj a_{k+j}(x).
}
\tag{L-91001.3}
\]

For one complex zero coordinate `z`, the normalized kernel satisfies

\[
\boxed{
\begin{aligned}
&\sum_{j=0}^m(-1)^j\binom mj
 \left[-\frac{2z^2}{(1-z^2)^{k+j+3}}\right]\\
&\qquad=
 -2(-1)^m\frac{z^{2m+2}}{(1-z^2)^{k+m+3}}.
\end{aligned}}
\tag{L-91001.4}
\]

Therefore

\[
\boxed{
\begin{aligned}
D_{k,m}(x)
={}&\sum_{\rho=1/2+i\gamma}
 m_\rho\frac{2u^{2m+2}}{(1+u^2)^{k+m+3}}\\
&-4(-1)^m\sum_{\Re\rho>1/2}
 m_\rho\Re\frac{z^{2m+2}}{(1-z^2)^{k+m+3}}.
\end{aligned}}
\tag{L-91001.5}
\]

The critical-line kernel is manifestly nonnegative for every `k,m`.

A real target pair at depth `y` and centre `x` contributes

\[
\boxed{
 -4(-1)^m\frac{y^{2m+2}}{(1-y^2)^{k+m+3}}.
}
\tag{L-91001.6}
\]

Thus even difference order retains the negative target sign; odd order reverses it.

## 3. Hausdorff measure under RH

Assume RH and put

\[
 \lambda_u=\frac1{1+u^2}\in(0,1].
\]

Then

\[
\frac{2u^2}{(1+u^2)^{k+3}}
=2(1-\lambda_u)\lambda_u^{k+2}.
\]

Define the finite positive measure

\[
\boxed{
 \nu_x
 =\sum_{\rho=1/2+i\gamma}
 2m_\rho(1-\lambda_{\gamma-x})
 \lambda_{\gamma-x}^2\,
 \delta_{\lambda_{\gamma-x}}.
}
\tag{L-91001.7}
\]

The local zero count and the `u^-4` tail make `nu_x` finite. Equation (L-91001.2) becomes

\[
\boxed{
 a_k(x)=\int_{[0,1]}\lambda^k\,d\nu_x(\lambda),
}
\tag{L-91001.8}
\]

and (L-91001.5) becomes

\[
\boxed{
 D_{k,m}(x)
 =\int_{[0,1]}
 \lambda^k(1-\lambda)^m\,d\nu_x(\lambda)\ge0.
}
\tag{L-91001.9}
\]

Thus the normalized safe-line sequence is a Hausdorff moment sequence, not merely a nonnegative sequence.

## 4. Shifted beta-Hankel sum of squares

For each `m,d,ell>=0`, define

\[
 H_{d,\ell}^{(m)}(x)
 =\bigl(D_{\ell+i+j,m}(x)\bigr)_{0\le i,j\le d}.
\tag{L-91001.10}
\]

Under RH, for every coefficient vector `c=(c_0,...,c_d)`,

\[
\boxed{
 c^*H_{d,\ell}^{(m)}(x)c
 =\int_{[0,1]}
 \lambda^\ell(1-\lambda)^m
 \left|\sum_{j=0}^dc_j\lambda^j\right|^2
 d\nu_x(\lambda)\ge0.
}
\tag{L-91001.11}
\]

Hence every shifted beta-Hankel matrix is PSD. The two families `m=0` and `m=1`, with all shifts, are the classical Hankel/localizing matrices for moments supported on `[0,1]`. In particular, a negative coefficient `a_K=D_(K,0)` is already the negative `1 x 1` shifted Hankel matrix `H_(0,K)^(0)`.

## 5. Bernstein spectral cells

At level `N`, define

\[
\boxed{
 B_{N,j}(x)
 =\binom NjD_{j,N-j}(x),
 \qquad 0\le j\le N.
}
\tag{L-91001.12}
\]

Under RH,

\[
 B_{N,j}(x)
 =\int_{[0,1]}
 \binom Nj\lambda^j(1-\lambda)^{N-j}
 d\nu_x(\lambda)\ge0.
\tag{L-91001.13}
\]

The Bernstein partition of unity gives the exact conservation law

\[
\boxed{
 \sum_{j=0}^N B_{N,j}(x)=a_0(x).
}
\tag{L-91001.14}
\]

On the critical line the cell kernel is

\[
\boxed{
 2\binom Nj
 \frac{u^{2(N-j)+2}}{(1+u^2)^{N+3}}.
}
\tag{L-91001.15}
\]

Thus each finite level is a positive beta histogram of the transformed squared zero distance `lambda=(1+u^2)^-1`.

## 6. Exact boundary

Proposed complete here:

```text
normalized single-line zero expansion;
all beta finite-difference kernels;
RH -> Hausdorff moment representation;
all shifted beta-Hankel sum-of-squares identities;
Bernstein spectral-cell positivity and partition.
```

Still open:

```text
prime-side proof of any complete Hausdorff/Pick hierarchy;
Riemann Hypothesis.
```