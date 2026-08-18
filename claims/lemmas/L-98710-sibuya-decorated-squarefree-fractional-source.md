# L-98710 — Fractional reciprocal Euler coefficients have an exact Sibuya-decorated squarefree source

Claim ID: `L-98710`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98700`  
RH status: **not assumed**

Fix `0<theta<1` and put

\[
a_\theta(k)=(-1)^{k-1}\binom\theta k
=\frac{\theta\,\Gamma(k-\theta)}{\Gamma(1-\theta)\Gamma(k+1)}
\qquad(k\ge1).
\]

Then

\[
a_\theta(k)>0,
\qquad
\sum_{k\ge1}a_\theta(k)z^k=1-(1-z)^\theta,
\qquad
\sum_{k\ge1}a_\theta(k)=1.
\tag{L-98710.1}
\]

For the odd Euler part

\[
B_{\theta,\mathrm{odd}}(s)=\prod_{p\text{ odd}}(1-p^{-s})^\theta
=\sum_{n\text{ odd}}b_{\theta,\mathrm{odd}}(n)n^{-s},
\]

one has the exact coefficient formula

\[
\boxed{
b_{\theta,\mathrm{odd}}(n)
=\mu(\operatorname{rad}n)
 \prod_{p^k\Vert n}a_\theta(k).
}
\tag{L-98710.2}
\]

Thus the correct positive source is not generalized-prime *letter parity* after
histories with the same integer product have been summed. It is a positive
measure on exponent-decorated squarefree supports:

```text
support       rad(n);
mark at p     k=v_p(n), with positive mass a_theta(k);
sign          mu(rad(n)).
```

For example,

\[
b_{\theta,\mathrm{odd}}(p^2)
=-a_\theta(2)
=-\frac{\theta(1-\theta)}2<0.
\tag{L-98710.3}
\]

At the generalized-prime-history level the same coefficient is the sum of an
odd one-letter history `p^2` and an even two-letter history `p,p`:

\[
-\frac\theta2+\frac{\theta^2}{2}
=-\frac{\theta(1-\theta)}2.
\]

Equation (L-98710.2) performs that cancellation before any completion is built.
It therefore supplies a canonical one-owner source space for every finite prime
cutoff.

The dyadic factor

\[
(1-2^{-s})^{2\theta}(1-2^{-s-1})^\theta
\]

is handled by three independent positive Sibuya decorations at the single
prime `2` (two with carrier `2^{-s}` and one with carrier `2^{-s-1}`). It is a
finite-prime tensor factor and does not alter the odd-prime source theorem or
any exponential rate below.
