# L-27601 — Averaged carry kernel and compact opposite-parity wavelet

Claim ID: `L-27601`  
Title: Averaging all atomized carry windows gives the canonical carry-resolvent kernel, and the `omega_2` source turns it into one explicit compact two-band wavelet  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Frozen base: PR #269 at `4c67408f1dd7cd3d6574bafbf51c50a280bc0384`  
Dependencies: PR #252 `L-24501`; PR #269 `R-26902`; elementary floor integration and Laplace transforms  
Scope: exact source/kernel algebra; no asymptotic source bound and no RH conclusion

## 1. Atomized carry windows

For real `x>=1` and `0<=theta<=1`, put

\[
 C(x,\theta)
 =\lfloor x\rfloor
  -\lfloor\theta x\rfloor
  -\lfloor(1-\theta)x\rfloor
 \in\{0,1\}.
\tag{L-27601.1}
\]

Let `N=floor(x)`. Since

\[
 \int_0^1\lfloor\theta x\rfloor\,d\theta
 =\frac{N(N-1)/2+N(x-N)}x,
\]

one obtains the exact average

\[
\boxed{
 \int_0^1C(x,\theta)\,d\theta
 =b(x)
 :=\frac{N(N+1-x)}x.
}
\tag{L-27601.2}
\]

Thus the continuum carry coefficient of PR #252 is not an auxiliary smoothing: it is literally the uniform average of all finite carry positions.

Define the logarithmically normalized averaged window

\[
\boxed{
 k(u)=e^{-u/2}b(e^u)\mathbf1_{u\ge0}.
}
\tag{L-27601.3}
\]

Equivalently,

\[
 k(u)=\int_0^1H_\theta(u)\,d\theta,
 \qquad
 H_\theta(u)=e^{-u/2}C(e^u,\theta)\mathbf1_{u\ge0}.
\tag{L-27601.4}
\]

## 2. Exact transform

Write

\[
 \sigma=z+\frac12.
\]

The atomized Mellin identity of `R-26902` gives

\[
 \widehat H_\theta(z)
 =\frac{\zeta(\sigma)}\sigma
  \left[1-\theta^\sigma-(1-\theta)^\sigma\right].
\tag{L-27601.5}
\]

Averaging in `theta` and using

\[
 \int_0^1
 [1-\theta^\sigma-(1-\theta)^\sigma]\,d\theta
 =\frac{\sigma-1}{\sigma+1}
\]

yields

\[
\boxed{
 K(z):=\widehat k(z)
 =\zeta(\sigma)
  \frac{\sigma-1}{\sigma(\sigma+1)}
 =\zeta\!\left(z+\frac12\right)
  \frac{z-\frac12}
  {(z+\frac12)(z+\frac32)}.
}
\tag{L-27601.6}
\]

This is exactly the continuum carry transform of `L-24501`.

## 3. The fixed RH-bearing source

Retain the opposite-parity coefficient

\[
 \omega_2(n)
 =\mu(n)
  -\frac32\mathbf1_{2\mid n}\mu(n/2)
  +\frac12\mathbf1_{4\mid n}\mu(n/4),
\tag{L-27601.7}
\]

and the normalized atomic measure

\[
 \beta_\omega
 =\sum_{n\ge1}\frac{\omega_2(n)}{\sqrt n}\,
   \delta_{\log n}.
\tag{L-27601.8}
\]

Its Laplace transform is

\[
 \Omega(\sigma)
 =\frac{E(\sigma)}{\zeta(\sigma)},
 \qquad
 E(\sigma)
 =(1-2^{-\sigma})(1-2^{-\sigma-1}).
\tag{L-27601.9}
\]

No zero of `E` lies in the open critical strip.

Define

\[
\boxed{
 z_\omega=\beta_\omega*k.
}
\tag{L-27601.10}
\]

Then

\[
\boxed{
 \widehat z_\omega(z)
 =E(\sigma)
  \frac{\sigma-1}{\sigma(\sigma+1)}.
}
\tag{L-27601.11}
\]

All zeta factors cancel at zeroth carry order, in agreement with `R-26902`.

## 4. Exact compact physical kernel

Put `L=log 2`. The inverse transform of

\[
 \frac{\sigma-1}{\sigma(\sigma+1)}
 =-\frac1\sigma+\frac2{\sigma+1}
\]

is

\[
 g_0(u)
 =-e^{-u/2}+2e^{-3u/2}
 \qquad(u\ge0).
\tag{L-27601.12}
\]

In the `z`-Laplace variable, multiplication by `E(sigma)` is the translation filter

\[
 (I-2^{-1/2}\tau_L)
 (I-2^{-3/2}\tau_L).
\tag{L-27601.13}
\]

Applying it to `g_0` gives the exact compact wavelet

\[
\boxed{
 z_\omega(u)
 =\begin{cases}
  2e^{-3u/2}-e^{-u/2},&0\le u<L,\\[1mm]
  \frac12e^{-u/2}-4e^{-3u/2},&L\le u<2L,\\[1mm]
  0,&u\ge2L.
 \end{cases}}
\tag{L-27601.14}
\]

The endpoint convention inherited from the causal convolution is:

```text
u=0       belongs to the first band;
u=log 2  belongs to the second band;
u=2log 2 has value zero.
```

The first band is nonnegative and the second is strictly negative. Hence the complete averaged carry source is a fixed factor-four two-band wavelet, not a growing packet.

## 5. Source-level interpretation

Equation (L-27601.10) says

```text
uniform average over every carry position
-> apply the complete opposite-parity inverse-zeta source
-> one compact physical wavelet supported on ratios [1/4,1].
```

The pure carry average is pole blind, but the compact result is the correct finite window on which the logarithmic boundary commutator acts in `L-27602`.

## 6. Exact replay target

`X-27601` verifies:

1. the exact floor-average identity (L-27601.2) on 2,079 rational controls;
2. the transform partial fraction;
3. the compact-filter coefficients on all three support intervals;
4. the finite Dirichlet inverse for `omega_2`;
5. the first and second commutator identities of `L-27602`.

## 7. Proof boundary

Closed exactly, subject to review:

- atomized-to-averaged carry identity;
- equality with the canonical carry-resolvent kernel;
- transform cancellation by `omega_2`;
- the compact two-band wavelet and endpoint convention.

Open:

- a subpower estimate for the logarithmic commutator;
- its local physical energy bound;
- RH.
