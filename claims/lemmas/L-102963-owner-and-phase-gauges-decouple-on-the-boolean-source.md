# L-102963 — Owner and phase gauges decouple on the Boolean source

Claim ID: `L-102963`  
Status: **PROVED EXACT SOURCE/PHASE DECOUPLING THEOREM**  
Created: 2026-08-25  
Depends on: `L-102901--L-102904`; `L-102959`; `L-102962`  
RH status: **not assumed**

Retain one finite labelled Boolean source occurrence \(S\) before physical collapse.

## 1. Owner labels are an independent coordinate

The canonical equal-pair Duhamel allocation of `L-102962` is an owner-space partition whose weights sum to one. It does not alter the arithmetic convolution product represented by the occurrence.

## 2. Phase labels may be endpoint-placed independently

Let \(D(S)\subseteq S\) be any finite set determined solely by the declared source occurrence and its fixed linear region—such as literal Boolean factors, marked labels, activation labels, or a source-owned discrepancy selector.

Use the primewise flat gauge with

\[
t_p\in\{0,1\}\quad(p\in D(S)),
\qquad
t_p={1\over2}\quad(p\notin D(S)).
\]

The complementary product source is unchanged coefficientwise. The additional tensor-energy cost is

\[
\boxed{
\exp\!\left(O\!\left(\sum_{p\in D(S)}{1\over p}\right)\right),
}
\tag{L-102963.1}
\]

which is polylogarithmic on every finite horizon.

At an endpoint, each selected label has a unique factor placement. Thus no phase label is split between two factor histories.

## 3. Additive phases depend on divisibility, not owner status

Let \(p\in D(S)\) divide the physical product \(N_S\), and suppose the clean opposite product \(M\) is not divisible by \(p\). Then, regardless of whether \(p\) is an unsquared owner or a completed square-core label,

\[
\boxed{
1=-\sum_{h=1}^{p-1}e_p(h(N_S-M)).
}
\tag{L-102963.2}
\]

The identity uses only

\[
p\mid N_S,
\qquad p\nmid M.
\]

Therefore the primes used for Kummer/Ramanujan separation need not coincide with the pair-owner coordinate.

## 4. Exact compatible normal form

One may simultaneously use

```text
owner coordinate:
  the canonical symmetric equal-pair Duhamel gauge;

phase coordinate:
  source-owned Boolean/core labels placed at endpoint temperatures;

physical phase transform:
  the incidence-masked centered kernel of L-102959;

all nonempty endpoint-color variance:
  the squared/higher-prime-power ledger of L-102904.
```

This removes the minimum-owner transpose curl from any route whose phase labels are chosen sourcewise inside the Boolean core.

## Scope firewall

A phase selector depending on the *other* physical term—for example the largest prime of \(a/(a,b)\)—is not automatically a linear source region. `L-102959` proves that such masks are analytically harmless once present, but a source-exact pair-dependent selection still requires a declared incidence decomposition. The theorem decouples owner and phase gauges; it does not by itself prove the remaining coherent core incidence.