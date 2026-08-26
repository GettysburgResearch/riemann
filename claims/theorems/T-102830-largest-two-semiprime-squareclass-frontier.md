# T-102830 — The Wick restriction reduces to distinct semiprime squareclasses

Claim ID: `T-102830`  
Status: **MAJOR UNCONDITIONAL ARITHMETIC NORMAL-FORM ADVANCE; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

`T-102820` reduced the hard all-chaos packet to a distinct-product,
different-unordered-pair physical restriction. `L-102830--L-102834` sharpen
that restriction using arithmetic order and squareclass geometry.

## 1. Largest-two gauge

Every depth-`k` occurrence may be moved from the equal-pair owner gauge to its
two largest actual prime labels. Physical realization is unchanged, while the
labelled energy changes by at most

\[
\binom{k}{2}=O((\log Y)^2).
\]

## 2. Unique semiprime squareclass

After source-faithful completion of every smaller cofactor prime, each hard
physical product has the unique form

\[
\boxed{N=pq\,a^2,\qquad p>q>P^+(a).}
\]

The map `(p,q,a)->pq a^2` is injective. The owner pair is exactly the
squarefree kernel of the physical integer.

All different-core overlap inside one fixed pair satisfies

\[
\sum_{p>q}\|H_{p,q}\|_2^2
\ll
\log(2Y)(\log\log(3Y))^2.
\]

Thus equal products, equal pairs and same-squareclass core overlap are closed.

## 3. Exact squareclass phase lift

Independent prime signs give

\[
\chi_\varepsilon(pq a^2)=\varepsilon_p\varepsilon_q.
\]

Distinct semiprime squareclasses are orthogonal in quadratic Walsh average, so

\[
\mathbb E_\varepsilon\|\mathcal H_\varepsilon\|_2^2
=Y^{o(1)}.
\]

The literal physical field is the identity-point evaluation
`epsilon=1`. `R-102830` proves that no source-blind degree-two point-evaluation
bound is possible.

## 4. Largest discrepancy prime

For two different squareclasses `pq` and `rs`, let

\[
\ell=\max(\{p,q\}\triangle\{r,s\}).
\]

Then the corresponding completed products have opposite `ell`-adic valuation
parity. Every cross term is assigned to this unique prime. Hence the final
operator has the exact prime-indexed decomposition

\[
\mathcal C_{\rm cross}=\sum_\ell\mathcal C_\ell.
\]

Each sector is now prepared for a literal quadratic-character, additive-phase
or dispersion estimate; no arbitrary owner remains.

## 5. Exact remaining theorem

Define

```text
LDPC102834:
  after exact carrier, source-region and gauge recombination, the sum of the
  largest-discrepancy-prime semiprime-squareclass sectors has subpower
  logarithmic negative mass in the fixed ratio-eight outer observation.
```

Equivalently one may prove the identity-point squareclass estimate
`L2SC102833`. The exact conclusion chain is

\[
\boxed{
\mathrm{LDPC}_{102834}
\Longrightarrow
\mathrm{L2SC}_{102833}
\Longrightarrow
\mathrm{DPWNC}_{102749}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{RH}.
}
\]

## Exact boundary

```text
largest-two owner reallocation             PROVED EXACT/SUBPOWER
complete cofactor squaring                  PROVED EXACT
semiprime-squareclass injectivity           PROVED EXACT
same-pair core overlap                      PROVED POLYLOG
quadratic Walsh orthogonality                PROVED EXACT
largest discrepancy prime partition         PROVED EXACT
identity-point / discrepancy dispersion      OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```