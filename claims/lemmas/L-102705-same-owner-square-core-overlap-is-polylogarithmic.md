# L-102705 — Same-owner square-core overlap is polylogarithmic

Claim ID: `L-102705`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-22  
Depends on: `L-102704`; PR #715 common mother and squared-core completion  
RH status: **not assumed**

Fix one greatest owner prime \(p\). After square-root cofactor completion, its
physical field has the form

\[
H_p(e^u)
=
\frac1{\sqrt p}
\sum_a\frac{c_p(a)}a
\phi(u-\log p-2\log a),
\]

where \(a\) is squarefree, every prime factor of \(a\) is smaller than \(p\),
and

\[
|c_p(a)|\le1.
\]

Let \(R_\Phi\) be the common-mother autocorrelation from `L-102703` and put

\[
M_\Phi=\sup_h|R_\Phi(h)|<\infty.
\]

Then

\[
\|H_p\|_2^2
\le
\frac{M_\Phi}{p}
\sum_a\frac1a
\sum_{a/4<b<4a}\frac1b.
\]

The inner harmonic sum is bounded by an absolute constant. On a horizon
\(pa^2\le16Y\),

\[
\boxed{
\|H_p\|_2^2
\ll_\Phi
\frac{\log(2Y)}p.
}
\tag{L-102705.1}
\]

Summing the owner-diagonal energies gives

\[
\boxed{
\sum_{p\le16Y}\|H_p\|_2^2
\ll_\Phi
\log(2Y)\log\log(3Y).
}
\tag{L-102705.2}
\]

Thus every collision between two distinct square cores attached to the **same**
owner is polylogarithmic, even after taking absolute values.

Together with `L-102704`, this removes:

```text
same-product collisions;
same-owner/different-core collisions;
all squared-core physical multiplicity.
```

The remaining term is exclusively the cross-owner correlation

\[
\sum_{p\ne q}\langle H_p,H_q\rangle.
\]

Any proof of the final occupancy estimate may therefore focus on carrier-
recombined interactions between distinct greatest-owner primes.
