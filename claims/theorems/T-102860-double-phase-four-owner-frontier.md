# T-102860 — Four-distinct-owner dispersion has two independent nonzero phases

Claim ID: `T-102860`  
Status: **MAJOR UNCONDITIONAL TWO-MODULUS REDUCTION; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

`T-102850` reduced the direct physical restriction to two semiprime
squareclasses whose owner sets contain four distinct physical primes.
`L-102838--L-102839` show that this sector has two exact arithmetic phase
directions.

## 1. Double principal-frequency removal

Let `ell_1>ell_2` be the two largest primes among the four owners. Each divides
exactly one physical product and is absent from the other. Therefore

\[
\boxed{
1=
\sum_{h_1=1}^{\ell_1-1}
\sum_{h_2=1}^{\ell_2-1}
 e_{\ell_1}(h_1(N-M))
 e_{\ell_2}(h_2(N-M)).
}
\]

Both phase coordinates are nonzero. This holds whether the two largest owners
occur on the same product or on opposite products.

## 2. Product-modulus core energy

For one fixed residual semiprime squareclass `Q`, one square-core octave
`B<=b<2B`, and `L=ell_1 ell_2`,

\[
\boxed{
\sum_{h_1,h_2}
\|F_{h_1,h_2,Q}\|_2^2
\ll
{1\over Q}\left(1+{L\over B}\right).
}
\]

The proof uses Chinese-remainder orthogonality. A core collision must satisfy
`b'=+-b` independently modulo each of the two primes, so it lies in at most
four residue classes modulo `L`.

Thus:

```text
long core B>=ell_1 ell_2:
  double-phase energy <<1/Q;

short core B<ell_1 ell_2:
  double-phase energy <<ell_1 ell_2/(B Q).
```

## 3. Exact remaining theorem

The sole uncontrolled operation is no longer zero-frequency removal or fixed-
squareclass core energy. It is coherent summation over different residual
squareclasses and over the two-modulus owner families.

Define

```text
2QDSP102860:
  after exact carrier, source-region, gauge and shared-owner renewal, the
  coherent two-nonzero-phase sum over four-distinct-owner semiprime
  squareclasses has subpower logarithmic negative mass in the fixed
  ratio-eight outer observation.
```

Then

\[
\boxed{
\mathrm{2QDSP}_{102860}
\Longrightarrow
\mathrm{4QDSP}_{102850}
\Longrightarrow
\mathrm{QDSP}_{102840}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{RH}.
}
\]

## Exact boundary

```text
four-distinct-owner reduction              PROVED EXACT
shared-owner renewal                        PROVED POLYLOG
double nonzero-phase identity               PROVED EXACT
fixed-squareclass product-modulus energy    PROVED
coherent two-modulus squareclass sum        OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```