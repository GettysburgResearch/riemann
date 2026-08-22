# L-104510 — Exact Hermite–Biehler half-plane index for a real polynomial

Claim ID: `L-104510`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
RH status: **not assumed**

Let `p` be a real polynomial of degree `n`, assume `gcd(p,p')=1`, and let
`lambda>0`. Define

\[
E_{\lambda,p}(z)=p(z)-i\lambda p'(z).
\tag{L-104510.1}
\]

The polynomial has no real zero because `p` and `p'` do not vanish
simultaneously.

Let `N_+`, `N_-` denote the numbers of zeros of `E_(lambda,p)` in the upper
and lower half-planes, counted with multiplicity. Let `r=N_R(p)` be the number
of real zeros of `p`.

## Cauchy-index computation

On the real axis the imaginary-to-real ratio is

\[
\frac{\Im E_{\lambda,p}(x)}{\Re E_{\lambda,p}(x)}
=-\lambda\frac{p'(x)}{p(x)}.
\]

At every simple real zero `rho` of `p`,

\[
-\lambda\frac{p'(x)}{p(x)}
=
-\frac{\lambda}{x-\rho}+O(1),
\]

so the ratio jumps from `+infinity` to `-infinity`. Each real zero contributes
one to the Cauchy index. The generalized Hermite–Biehler argument-principle
formula therefore gives

\[
\boxed{N_+-N_-=r.}
\tag{L-104510.2}
\]

Since `N_++N_-=n`,

\[
\boxed{
N_-(E_{\lambda,p})
=\frac{n-r}{2}
=\frac{N_{\rm nr}(p)}{2}.
}
\tag{L-104510.3}
\]

Thus every nonreal conjugate pair of `p` is exactly one lower-half-plane zero
of the companion.

Because

\[
E_{\lambda,p}'=E_{\lambda,p'},
\tag{L-104510.4}
\]

the factor-two conservation law becomes the one-unit index law

\[
\boxed{
N_-(E_{\lambda,p})-N_-(E_{\lambda,p'})
=E(p),
}
\tag{L-104510.5}
\]

where `E(p)` is the number of wrong extrema of `p`.

## Multiple roots

For a non-squarefree polynomial, apply (L-104510.3) to `p-epsilon` at regular
real `epsilon` and pass to the limit. The open lower-half-plane count remains
the number of nonreal conjugate pairs; common real zeros may remain on the
boundary.

## Xi criterion

For a real entire function of genus at most one, the same Cauchy-index theorem
holds in the weak Hermite–Biehler class under canonical-product exhaustion.
In particular, for every `lambda>0`,

\[
\boxed{
\mathrm{RH}
\iff
\Xi(z)-i\lambda\Xi'(z)
\text{ has no zero in }\Im z<0.
}
\tag{L-104510.6}
\]

The weak formulation permits boundary zeros caused by multiple real zeros of
`Xi`; it does not assume their simplicity.

Equation (L-104510.6) is a detector, not a proof of its zero-freeness.
