# L-102001 — The balanced Vaughan remainder is an exact large-divisor Hankel form

Claim ID: `L-102001`
Status: **PROVED EXACT ARITHMETIC IDENTITY**
Created: 2026-08-21
Audited: 2026-08-21
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

where `K` is a fixed kernel supported in `[1,C]` for some finite `C>=1`.
Every sum below is therefore finite at each endpoint.

For every \(n>U\), the full Möbius divisor sum vanishes, so

\[
\boxed{a_U(n)=\sum_{d\mid n,\ d>U}\mu(d).}
\tag{L-102001.2}
\]

Insert (L-102001.2) twice into (L-102001.1), write \(r=du\),
\(s=ev\), and interchange finite sums. Since

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

## Exact parabolic localization

Specialize to the conclusion-facing choice

\[
U=\lfloor X^{1/3}\rfloor.
\]

If one term in (L-102001.3) is nonzero, then one term in
\(\mathcal L_K(X/(de))\) is nonzero. Since `supp K subset [1,C]`,

\[
1\le \frac{X}{det}\le C
\]

for some integer `t>=1`; in particular

\[
de\le X.
\tag{L-102001.5}
\]

If \(d\le e\), then \(d>\lfloor X^{1/3}\rfloor\), hence
\(d>X^{1/3}\), and therefore

\[
\boxed{
e\le\frac Xd<d^2.
}
\tag{L-102001.6}
\]

Thus every active ordered pair lies, exactly and with no finite-floor
exception, in the divisor-parabolic region

\[
\boxed{\max(d,e)<\min(d,e)^2.}
\tag{L-102001.7}
\]

This is the same exponent-two geometry contained in the stronger actual-prime
interval theorem `L-100615`. It is not by itself a lifting from composite
divisors to prime-owner intervals.

## Correct gcd reparameterization

On nonzero Möbius support write

\[
d=ga,\qquad e=gb,\qquad g=(d,e),\qquad(a,b)=1.
\]

Because `d` and `e` are squarefree, `g`, `a`, and `b` are pairwise coprime and
squarefree. Equivalently,

\[
\mu^2(gab)=1.
\]

Then

\[
\boxed{\mu(ga)\mu(gb)=\mu(a)\mu(b).}
\tag{L-102001.8}
\]

Consequently the exact gcd form is

\[
\boxed{
\mathcal B_U(X)
=\sum_{\substack{g,a,b\ge1\\\mu^2(gab)=1\\ga>U,\ gb>U}}
\frac{\mu(a)\mu(b)}{g\sqrt{ab}}
\mathcal L_K\!\left(\frac{X}{g^2ab}\right).
}
\tag{L-102001.9}
\]

The squarefreeness condition in (L-102001.9) is load-bearing. Omitting it
would introduce spurious terms such as a nonsquarefree `g` whose original
Möbius coefficient is zero.

This is an exact reparameterization, not a decomposition into independent
`g` and `(a,b)` sums. The cutoff constraints and the physical kernel remain
coupled.