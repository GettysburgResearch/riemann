# L-90602 — First-order Brownian truncation error and the displacement of each fixed xi zero

Claim ID: `L-90602`  
Status: **PROPOSED COMPLETE ASYMPTOTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-21705`, `L-34001`; elementary moment expansion  
Scope: fixed-compact asymptotics and fixed-zero displacement; no uniform-in-height zero theorem

## 1. Statement

Let

\[
 S_N=\sum_{n=1}^N\frac{\Gamma_{2,n}}{n^2},
 \qquad
 m_N(s)=\pi^{-s/2}\mathbb E[S_N^{s/2}],
\]

and let

\[
 S_\infty=S_N+R_N,
 \qquad
 R_N=\sum_{n>N}\frac{\Gamma_{2,n}}{n^2},
\]

with `R_N` independent of `S_N`. By the Brownian identity,

\[
 \pi^{-s/2}\mathbb E[S_\infty^{s/2}]=2\xi(s).
\]

### Theorem

Uniformly on every compact set `K subset C`,

\[
 \boxed{
 m_N(s)
 =2\xi(s)-\frac{2s}{\pi N}\xi(s-2)+O_K(N^{-2}).
 }
 \tag{L-90602.1}
\]

Let `rho` be a simple zero of `xi`. The unique zero `s_N` of `m_N` near `rho` then satisfies

\[
 \boxed{
 s_N
 =\rho+\frac{\rho\,\xi(\rho-2)}{\pi\xi'(\rho)}\frac1N
 +O_\rho(N^{-2}).
 }
 \tag{L-90602.2}
\]

In the `z=s/2` coordinate of PR #343,

\[
 \boxed{
 z_N
 =\frac\rho2+\frac{\rho\,\xi(\rho-2)}{2\pi\xi'(\rho)}\frac1N
 +O_\rho(N^{-2}).
 }
 \tag{L-90602.3}
\]

At a nontrivial zeta zero, elementary gamma cancellation simplifies the displacement coefficient to

\[
 \boxed{
 \frac{\rho\,\xi(\rho-2)}{2\pi\xi'(\rho)}
 =\frac{(\rho-3)\zeta(\rho-2)}{(\rho-1)\zeta'(\rho)}.
 }
 \tag{L-90602.4}
\]

The theorem is deliberately fixed-height. It explains why finite approximant zeros near any one xi zero converge at rate `1/N`, but it does not control the runaway high-frequency zeros of `L-90601`.

## 2. Tail moments

Put `u=s/2`. The tail has

\[
 \mu_{1,N}:=\mathbb E R_N
 =2\sum_{n>N}n^{-2}
 =\frac2N+O(N^{-2}),
 \tag{L-90602.5}
\]

and

\[
 \mathbb E R_N^2
 =(\mathbb E R_N)^2+2\sum_{n>N}n^{-4}
 =O(N^{-2}).
 \tag{L-90602.6}
\]

For a fixed compact set of `u`, choose a fixed number of the first gamma summands large enough that all negative moments appearing below are integrable. Since `S_N` dominates that fixed positive gamma convolution, the relevant negative moments are bounded uniformly in `N`.

Taylor's formula on the positive half-line gives

\[
 (S_N+R_N)^u
 =S_N^u+uR_NS_N^{u-1}+O_K\!\left(R_N^2\,\mathcal M_N\right),
 \tag{L-90602.7}
\]

where `E M_N=O_K(1)` uniformly. Taking expectations and using independence,

\[
 \mathbb E[S_\infty^u]-\mathbb E[S_N^u]
 =u\mu_{1,N}\mathbb E[S_N^{u-1}]+O_K(N^{-2}).
 \tag{L-90602.8}
\]

The same first-order estimate one exponent lower gives

\[
 \mathbb E[S_N^{u-1}]
 =\mathbb E[S_\infty^{u-1}]+O_K(N^{-1}).
 \tag{L-90602.9}
\]

Substituting (L-90602.5) and (L-90602.9) into (L-90602.8),

\[
 \mathbb E[S_N^u]
 =\mathbb E[S_\infty^u]
 -\frac{2u}{N}\mathbb E[S_\infty^{u-1}]
 +O_K(N^{-2}).
 \tag{L-90602.10}
\]

Now

\[
 \pi^{-u}\mathbb E[S_\infty^u]=2\xi(s),
 \qquad
 \pi^{-u}\mathbb E[S_\infty^{u-1}]
 =\frac2\pi\xi(s-2),
 \tag{L-90602.11}
\]

which proves (L-90602.1).

## 3. Root displacement

Let

\[
 m_N(s)=2\xi(s)+N^{-1}E_1(s)+O(N^{-2}),
 \qquad
 E_1(s)=-\frac{2s}{\pi}\xi(s-2).
\]

At a simple zero `rho`, the analytic implicit-function/Rouché expansion gives

\[
 s_N-\rho
 =-\frac{E_1(\rho)}{2\xi'(\rho)}\frac1N+O_\rho(N^{-2}),
\]

which is (L-90602.2). Dividing by two gives (L-90602.3).

Finally, from

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and `Gamma(rho/2-1)/Gamma(rho/2)=2/(rho-2)`, one obtains at a zeta zero

\[
 \frac{\rho\xi(\rho-2)}{2\pi\xi'(\rho)}
 =\frac{(\rho-3)\zeta(\rho-2)}{(\rho-1)\zeta'(\rho)},
\]

proving (L-90602.4).

## 4. Exact continuum cancellation behind the scale `1/N`

The coefficient weight of `L-34003` has the bulk asymptotic

\[
 C_{N,\lfloor x\sqrt N\rfloor}\sim4e^{-2x^2}.
\]

Inserting `n=sqrt(N)x` into the numerator and retaining the leading continuum term gives

\[
 \int_0^\infty e^{-2x^2}x^{-2z}
 \left(z-\frac12+2x^2\right)dx.
 \tag{L-90602.12}
\]

This integral vanishes identically by the gamma recurrence:

\[
 \boxed{
 \int_0^\infty e^{-2x^2}x^{-2z}
 \left(z-\frac12+2x^2\right)dx=0.
 }
 \tag{L-90602.13}
\]

Thus the Brownian numerator is a quadrature error after its leading continuum mass cancels. Formula (L-90602.1) identifies the first surviving correction exactly.

## 5. Proof boundary

Closed here:

- the complete fixed-compact `1/N` truncation expansion;
- the displacement of every fixed simple xi zero;
- the zeta-ratio simplification;
- the leading continuum cancellation.

Not closed:

- uniform control as the zero height grows with `N`;
- any half-plane stability theorem;
- RH.

`L-90601` shows that such a uniform theorem is in fact false for the raw finite Brownian factors.
