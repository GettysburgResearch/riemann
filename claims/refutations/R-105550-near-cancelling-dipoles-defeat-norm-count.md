# R-105550 — Near-cancelling Blaschke dipoles defeat norm-only counting

Claim ID: `R-105550`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24

For real `0<a,b<1`, let

\[
B_a(z)=\frac{z-a}{1-az},
\qquad
u_{a,b}=B_a/B_b.
\]

When `a!=b`, the quotient has one reduced denominator zero, so

\[
\operatorname{rank}H_{u_{a,b}}=1.
\]

The only interior pole is `b`.  Its anti-analytic part is

\[
\frac{C}{z-b},
\qquad
C=\frac{(b-a)(1-b^2)}{1-ab}.
\]

Therefore the negative Fourier coefficients are `C b^(m-1)` and

\[
\boxed{
\|H_{u_{a,b}}\|_{\rm HS}^2
=\left(\frac{a-b}{1-ab}\right)^2.
}
\tag{R-105550.1}
\]

As `b->a`, the rank remains one while the Hilbert--Schmidt norm tends to zero.
Taking direct sums gives arbitrarily large bad rank with arbitrarily small
energy per mode.

Consequences:

```text
small companion Hankel norm        does not bound bad companion count;
small safe-line source energy       does not control a partial index;
small-delta Cayley linearization     cannot prove a zero count by norm alone.
```

Any valid norm-to-count argument must pay a separation/conditioning input such
as `L-105552`, or estimate the winding/partial index directly.
