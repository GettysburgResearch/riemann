# L-105223 — A common nonzero Xi-derivative anchor and explicit fixed-order disk growth

Claim ID: `L-105223`  
Status: **PROPOSED UNCONDITIONAL THETA-KERNEL THEOREM; independent review pending**  
Created: 2026-08-23  
Depends on: the classical positive Fourier kernel of `Xi`; normalization audit in PR #723  
RH status: **not assumed**

Use the standard normalization

\[
\Xi(z)=\int_{\mathbb R}\Phi_{\rm std}(u)e^{izu}\,du,
\]

where `Phi_std` is even and positive. For `u>=0`,

\[
\Phi_{\rm std}(u)
=
\sum_{n\ge1}
\left(
4\pi^2n^4e^{9u/2}
-
6\pi n^2e^{5u/2}
\right)
e^{-\pi n^2e^{2u}}.
\tag{L-105223.1}
\]

The leading coefficient is the corrected standard normalization; it is twice
the half-normalized kernel used in the earlier draft source audited by PR #723.

## 1. One common anchor for the entire derivative ladder

For every integer `m>=0` and every `y>0`,

\[
i^{-m}\Xi^{(m)}(-iy)
=
\int_{\mathbb R}u^m\Phi_{\rm std}(u)e^{yu}\,du.
\tag{L-105223.2}
\]

Pairing `u` with `-u` gives a positive cosh integral when `m` is even and a
positive sinh integral when `m` is odd. Hence

\[
\boxed{
i^{-m}\Xi^{(m)}(-iy)>0
\qquad(m\ge0,\ y>0).
}
\tag{L-105223.3}
\]

In particular

\[
\boxed{
\Xi^{(m)}(-i)\ne0
\qquad\text{for every }m\ge0.
}
\tag{L-105223.4}
\]

Thus `-i` is a single authenticated anchor for every finite derivative family.
No moving zero census is used.

## 2. Explicit global growth envelope

For `z=x+iy`, positivity and evenness give

\[
|\Xi^{(m)}(z)|
\le
2\int_0^\infty u^m\Phi_{\rm std}(u)e^{|y|u}\,du.
\]

Since the negative term in (L-105223.1) may be discarded and

\[
u^m\le m!e^u
\qquad(u\ge0),
\]

putting

\[
q=|y|+\frac{11}{2}
\tag{L-105223.5}
\]

gives

\[
|\Xi^{(m)}(z)|
\le
8\pi^2m!\sum_{n\ge1}n^4
\int_0^\infty
e^{qu-\pi n^2e^{2u}}\,du.
\]

With `v=pi n^2e^(2u)`,

\[
\int_0^\infty e^{qu-\pi n^2e^{2u}}\,du
\le
\frac12\pi^{-q/2}n^{-q}\Gamma(q/2).
\]

Because `q>=11/2` and `4-q<=-3/2`,

\[
\boxed{
|\Xi^{(m)}(z)|
\le
4\pi^2m!\zeta(3/2)
\pi^{-q/2}\Gamma(q/2).
}
\tag{L-105223.6}
\]

The factor `4` and the shift `11/2` are load bearing and agree with the
normalization audit in the latest PR #723 continuation.

## 3. Cartan-compatible disk growth

For fixed `m`, on the disk

\[
|z+i|\le R
\]

one has `|Im z|<=R+1`. Stirling's formula in (L-105223.6), together with the
fixed positive denominator from (L-105223.4), gives

\[
\boxed{
\log
\frac{
\max_{|z+i|\le R}|\Xi^{(m)}(z)|
}{
|\Xi^{(m)}(-i)|
}
=
O_m\!\bigl(R\log(R+2)\bigr).
}
\tag{L-105223.7}
\]

This closes the common-anchor and fixed-order disk-growth inputs explicitly
left open in the PR #723 Cartan-collar handoff.

## 4. Scope

The growth theorem does not authenticate a complete derivative-event manifest,
bound an optimal selector norm, absorb the Cartan exponential loss, prove the
signed first-residue carrier, or establish RH. It removes two preliminary
analytic inputs—common nonzero anchoring and fixed-order disk growth—from the
remaining selector/absorption gate.
