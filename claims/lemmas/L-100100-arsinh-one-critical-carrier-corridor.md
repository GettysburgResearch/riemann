# L-100100 — The critical quadratic and cubic carriers share an arsinh-one future-prime corridor

Claim ID: `L-100100`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-20  
Frozen inputs: PR #672 at `2a351548eb7960ff8ae99f193c10e278984c5657`; PR #676 at `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9`  
RH status: **not assumed**

Put

\[
\kappa(y)=
\begin{cases}
16,&0<y<1,\\
24y^{-1/2}-9y^{-1},&y\ge1,
\end{cases}
\]

and

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\]

The first is the kernel of PR #672's renormalized quadratic envelope; the
second is PR #676's positive self-reciprocal cubic critical kernel.

## 1. Exact one-prime Harnack bounds

For every prime `p` and every `y>0`,

\[
\boxed{p^{-3/2}\kappa(y/p)\le p^{-1}\kappa(y),}
\tag{L-100100.1}
\]

and

\[
\boxed{p^{-1/2}\Psi(y/p)\le p^{-1}\Psi(y).}
\tag{L-100100.2}
\]

For (L-100100.1), on `y<1` the claim is immediate; on `1<=y<p` the
right side is minimized at the relevant endpoint; on `y>=p` direct
substitution reduces the difference to `9(p-1)>=0`.

For (L-100100.2), put `a=sqrt(p)` and `t=sqrt(y)`.  On `1<=y<p` the
required difference, after division by `64`, is

\[
3t-1-\frac{3t^2}{a}+\frac{t^3}{a^2}.
\]

Its derivative is `3(1-t/a)^2`, and its value at `t=1` is
`(2a-1)(a-1)/a^2>0`.  The other two activation sectors are immediate.

When `p>y`, both carriers also satisfy

\[
p^{-\alpha}\frac{K(y/p)}{K(y)}
\le\frac32\max(1,\sqrt y)p^{-3/2},
\tag{L-100100.3}
\]

where `alpha=3/2` for `kappa` and `alpha=1/2` for `Psi`.  Hence

\[
\max(1,\sqrt y)\sum_{p>y}p^{-3/2}\ll\frac1{\log(2y)}.
\tag{L-100100.4}
\]

## 2. Euler-level contraction

Fix a least future prime `q>67`.  Expand the finite future Euler product and
let `M_r(y)` be the unsigned mass at Euler level `r`.  Double-counting label
removals and using (L-100100.1)--(L-100100.4) gives

\[
M_r(y)\le\frac{\Sigma_q(y)^r}{r!}K(y),
\tag{L-100100.5}
\]

where

\[
\Sigma_q(y)=
\sum_{q\le p\le y}\frac1p
+\frac32\max(1,\sqrt y)\sum_{p>y}p^{-3/2}.
\tag{L-100100.6}
\]

The estimates are uniform in the finite terminal prime, so the infinite future
product follows by convergence.  Pairing even and odd levels yields

\[
\boxed{
\mathcal F_q(y)\ge K(y)[1-\sinh\Sigma_q(y)].
}
\tag{L-100100.7}

Thus `Sigma_q(y)<asinh(1)` implies strict positivity for either critical
carrier.

## 3. Prime-ratio corridor

Mertens' prime reciprocal theorem and (L-100100.4) give, uniformly for fixed
`A>1` and `q<=y<=q^A`,

\[
\Sigma_q(y)\le\log A+o_{q\to\infty}(1).
\]

Since

\[
\exp(\operatorname{arsinh}1)=1+\sqrt2,
\]

we obtain

\[
\boxed{
A<1+\sqrt2
\Longrightarrow
\exists q_0(A)\ \forall q\ge q_0(A),\ q\le y\le q^A:
\mathcal F_q(y)>0.
}
\tag{L-100100.8}

This closes an unconditional hereditary future-prime terminal corridor for
both conclusion-facing carriers.  The unresolved real-variable region is the
finite low-prime block

\[
q<y^{1/(1+\sqrt2)+o(1)}.
\]
