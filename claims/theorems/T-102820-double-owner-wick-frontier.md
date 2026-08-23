# T-102820 — The hard Wick packet begins at one canonical unordered prime pair

Claim ID: `T-102820`  
Status: **MAJOR UNCONDITIONAL OWNER REDUCTION; RH UNPROVED**  
Created: 2026-08-23  
Base: PR #719  
RH status: **unproved**

`T-102800--T-102810` removed the root and complete first chaos from the fixed
completion-defect source.  `L-102746--L-102749` now identify the exact owner
geometry of the surviving current.

## 1. Canonical pair owner

For

\[
 L=\sum_\ell p_\ell^{-1/2}e^{-i\vartheta_\ell}U_\ell,
\]

the hard source is

\[
 e^{-L}-I+L
 =\int_0^1(1-t)L^2e^{-tL}\,dt.
\]

Every squarefree occurrence containing \(k\ge2\) labelled primes is divided
equally among its \(\binom{k}{2}\) actual unordered prime pairs.  Each pair
owns the fraction

\[
 \binom{k}{2}^{-1}
\]

of the same signed coefficient.

Prime-square terms from the diagonal of \(L^2\) have activity \(p^{-1}\) and
belong to the already-closed polylogarithmic ledger.

## 2. Closed pair costs

On a horizon \(Y\):

```text
free unordered-pair energy
  = O((log log Y)^2);

same-occurrence pair-owner collapse
  = O((log Y)^2);

same-product factor-pair collapse
  = Y^o(1);

root, first chaos and repeated-label diagonals
  = removed or polylogarithmic.
```

Thus the hard source may be treated as one root-free, distinct-pair field
without paying a power loss before physical observation.

## 3. Exact remaining current

Let \(\mathcal O_*\) denote the carrier-centered fixed outer-ray observation.
Modulo the closed diagonal term,

\[
 \mathcal J_{\rm pair}(X)
 =2\int_0^1(1-t)
 \sum_{i<j}
 \mathcal O_*[RSx_ix_je^{-tL}](X)\,dt.
\]

After collapsing every equal product, the sole unproved operator correlates
**different integer products carrying different unordered owner pairs** inside
the fixed ratio-eight observation window.

Define

```text
DPWNC102749:
  after exact carrier, source-region and gauge recombination, the
  distinct-product, different-unordered-pair restriction of J_pair has
  subpower logarithmic negative mass at the fixed outer ray.
```

Then

\[
 \boxed{
 \mathrm{DPWNC}_{102749}
 \Longrightarrow
 \mathrm{WNC}_{102743}
 \Longrightarrow
 \mathrm{OER}_{102780}
 \Longrightarrow
 \mathrm{AR\!-\!DEFECT}_{102600}
 \Longrightarrow
 \mathrm{RH}.
 }
\]

## Binding restriction firewall

`R-102728` proves that bounded free pair energy does not control a physical
one-parameter restriction for arbitrary clustered logarithmic frequencies.
A successful proof must use the literal prime-product geometry, source signs
or pair-owner transport.  No source-blind Fock-to-physical contraction is
assumed.

## Exact boundary

```text
second-order Duhamel identity                 PROVED EXACT
canonical equal-pair owner                    PROVED EXACT
prime-square pair diagonal                    PROVED POLYLOG
free pair energy                              PROVED POLYLOG
same-occurrence pair collapse                 PROVED POLYLOG
same-product factor-pair collapse             PROVED SUBPOWER
distinct-product cross-pair restriction       OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
