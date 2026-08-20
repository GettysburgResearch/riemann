# L-102001 — The balanced Vaughan remainder is an exact large-divisor Hankel form

Claim ID: `L-102001`
Status: **PROVED EXACT ARITHMETIC IDENTITY**
Created: 2026-08-21
Depends on: PR #685 `L-100311`
RH status: **not assumed**

Retain the exact Vaughan identity of `L-100311` with

\[
\mu_U(n)=\mu(n)\mathbf1_{n\le U},\qquad
a_U=\varepsilon-\mu_U*\mathbf1,
\]

and balanced remainder

\[
\mathcal B_U(X)
=\sum_{r,s>U}\sum_{m\ge1}
\frac{a_U(r)a_U(s)\mu(m)}{\sqrt{rsm}}
K(X/(rsm)),
\tag{L-102001.1}
\]

where `K` is any fixed compact kernel for which the sum is finite at each endpoint.

For every \(n>U\), the full Möbius divisor sum vanishes, so

\[
\boxed{a_U(n)=\sum_{d\mid n,\ d>U}\mu(d).}
\tag{L-102001.2}
\]

Insert (L-102001.2) twice into (L-102001.1), write \(r=du\), \(s=ev\), and interchange finite sums. Since

\[
\sum_{uvm=t}\mu(m)=(\mathbf1*\mathbf1*\mu)(t)=1,
\]

one obtains the exact collapse

\[
\boxed{
\mathcal B_U(X)
=\sum_{d,e>U}\frac{\mu(d)\mu(e)}{\sqrt{de}}
\mathcal L_K\!\left(\frac{X}{de}\right),
}
\tag{L-102001.3}
\]

where

\[
\boxed{
\mathcal L_K(Y)=\sum_{t\ge1}\frac1{\sqrt t}K(Y/t).
}
\tag{L-102001.4}
\]

No error term, smooth approximation, or unsigned majorization is used.

## Parabolic localization

Now specialize to the conclusion-facing choice \(U=\lfloor X^{1/3}\rfloor\). Compact support forces \(de\ll X\); for the ratio-16 kernel of `L-100310`, more precisely \(X/16\le de\,t\le X\) for every active summand.

In the divisor-pair outer sum itself, if \(d\le e\) and \(de\le X\), then

\[
e\le\frac Xd<d^2
\tag{L-102001.5}
\]

because \(d>U\ge X^{1/3}-1\), and the finite floor boundary may be absorbed into a fixed low-end exception. Thus asymptotically every active ordered pair lies in the divisor-parabolic region

\[
\boxed{\max(d,e)<\min(d,e)^2.}
\tag{L-102001.6}
\]

This is the same exponent-two geometry that appears inside the stronger prime-interval positivity theorem `L-100615`.

## GCD factorization

On nonzero Möbius support write

\[
d=ga,\qquad e=gb,\qquad(a,b)=1.
\]

Squarefreeness implies \((g,a)=(g,b)=1\), and therefore

\[
\boxed{\mu(ga)\mu(gb)=\mu(a)\mu(b).}
\tag{L-102001.7}
\]

Hence the common gcd core is sign-free and enters only through the square dilation \(g^2ab\):

\[
\boxed{
\mathcal B_U(X)
=\sum_{\substack{g,a,b\\(a,b)=1\\ga,gb>U}}
\frac{\mu(a)\mu(b)}{g\sqrt{ab}}
\mathcal L_K\!\left(\frac{X}{g^2ab}\right).
}
\tag{L-102001.8}
\]

This is an exact reparameterization, not a disjoint decomposition into independent `g` and `(a,b)` sums. The cutoff constraints remain coupled and must be preserved in any subsequent estimate.