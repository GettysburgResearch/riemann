# O-15103 — The Jensen-polynomial counterexample window is closed through degree `9 x 10^24`

Claim ID: `O-15103`  
Status: **LITERATURE AUDIT; CONCLUSION VALID, CITATION CHAIN CORRECTED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: Griffin--Ono--Rolen--Zagier (2019); Griffin--Ono--Rolen--Thorner--Tripp--Wagner (2022); Platt--Trudgian (2021)  
Scope: audit of `O-16002` on PR #173  
Related counterexample candidates: excludes a computational search range

## 1. Valid conclusion

Let `J^{d,n}` be the Jensen polynomials of the Taylor coefficients of the Riemann xi function in the normalization of the cited papers.

The following statements are supported by the primary sources.

1. Griffin--Ono--Rolen--Zagier prove hyperbolicity for
   
   \[
   1\le d\le8,
   \qquad n\ge0.
   \]

2. Griffin--Ono--Rolen--Thorner--Tripp--Wagner prove the effective implication
   
   \[
   RH_0(T)
   \quad\Longrightarrow\quad
   J^{d,n}\text{ hyperbolic for every }n\ge0
   \text{ and }d\le\lfloor T\rfloor^2.
   \tag{O-15103.1}
   \]

3. Platt--Trudgian rigorously verify `RH_0(T)` through
   
   \[
   T=3{,}000{,}175{,}332{,}800.
   \]

Consequently

\[
 \boxed{
 J^{d,n}\text{ is hyperbolic for every }n\ge0
 \text{ and every }d\le9\times10^{24}.}
 \tag{O-15103.2}
\]

Indeed

\[
 9\times10^{24}<T^2.
\]

Thus a search for a nonhyperbolic Riemann-xi Jensen polynomial in this degree range cannot produce an RH counterexample if the cited theorem and verified-zero computation are accepted.

## 2. Citation correction

The 2022 paper's printed Corollary 1.3 uses the then-cited verification height

\[
 T=3.06\times10^{10}
\]

and therefore states only

\[
 d\le9.36\times10^{20}.
\]

The stronger `9 x 10^24` conclusion is not literally Corollary 1.3 as printed. It is the immediate updated application of **Theorem 1.2** to the later Platt--Trudgian height.

Accordingly, `O-16002` has the right mathematical conclusion but should cite:

```text
2022 Theorem 1.2 + Platt--Trudgian 3e12 verification,
```

rather than attributing the updated number directly to Corollary 1.3.

## 3. Precise scope

The conclusion closes a computational counterexample search only through the stated degree. It does not prove hyperbolicity for all degrees; that remains equivalent to RH.

The phrase “any apparent violation is an arithmetic bug or a falsification of Platt--Trudgian” is rhetorically too narrow. Other possibilities include:

- a normalization mismatch in the Jensen coefficients;
- an implementation error in transporting the theorem;
- an error in the 2022 theorem or its hypotheses.

The proof-facing statement should simply be that such a violation contradicts the cited theorem chain and must not be promoted without independently auditing every interface.

## 4. Normalization warning

The papers use a specific normalized Taylor sequence `gamma(n)`. The radical source in `L-15101` has transform `Xi/4`; this constant scaling does not change Jensen roots when propagated consistently, but factorial, even-index, and variable-rescaling conventions do matter.

A production checker must reconstruct the exact literature normalization before applying (O-15103.2).

## 5. Strategic conclusion

The PR #173 recommendation is sound: do not spend computational effort searching the standard Riemann-xi Jensen family below degree `9 x 10^24`. Preserve the exact Hermite/Bézoutian hyperbolicity checker for other finite polynomials and for normalization audits.