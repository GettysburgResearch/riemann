# Research report — Finite harmonic sectors and the positive-energy endpoint

Date: 2026-08-12  
Status: **continued full unconditional proposal; RH remains unproved**

## Executive result

The previous endpoint asked for an entangled sector-changing optical operator. The present pass separates that into:

1. an unconditional representation-theoretic construction; and
2. one remaining positive-energy projection.

The critical Jordan inverse has only finitely many non-square-summable prime harmonics. On the cofinal sequence \(\omega_j=2^{-j-3}\), exactly one harmonic changes sector. After extracting it, the complete higher-harmonic inverse is an ordinary vacuum-sector product.

Although fixed critical product sectors are disjoint under translation, their orbit forms a canonical direct-integral Hilbert bundle with a strongly continuous translation group. Thus representation change and covariance are not RH-bearing.

For the completed boundary quotient \(\Theta=\mathfrak A/B\) and outer vector \(r\),

\[
\|P_-(\Theta r)\|^2
=
\|P_{K_B}(\mathfrak A r)\|^2.
\]

The negative-energy content is exactly the crossed-zero model port. The corrected proposal is therefore to construct the source-defined neutral section and prove this one projection vanishes.

## Main formulas

At the critical line,

\[
\log D_{p,\omega}(z)
=
-\sum_{k\ge1}
\frac{
p^{-k(1/2-\omega)}
-
p^{-k(1/2+\omega)}
}{k}z^k.
\]

The \(k\)-th charge is square summable across primes exactly when

\[
k(1-2\omega)>1.
\]

Hence

\[
K_\omega
=
\left\lfloor(1-2\omega)^{-1}\right\rfloor.
\]

The extracted remainder satisfies

\[
\sum_p\|R_{p,K_\omega}-1\|_{H^2}^2<\infty.
\]

For the orbit bundle,

\[
U_{t,a}
=
\bigotimes_pR_{p,a}
:
\mathcal H_t\to\mathcal H_{t+a}
\]

exists because it maps each local reference vector exactly.

Finally,

\[
P_-(\Theta r)
=
\bar B P_{K_B}(\mathfrak A r).
\]

## Corrected scientific boundary

```text
sector structure and translation covariance      solved;
number of divergent prime harmonics              solved;
higher-harmonic Fock remainder                   solved;
zero-port/negative-energy identification         solved;
source-defined first-charge neutralization       open;
positive-energy projection vanishing             open / RH-bearing;
RH                                                unproved.
```

This is a narrower and more falsifiable endpoint than a generic “sector-changing wave operator.”
