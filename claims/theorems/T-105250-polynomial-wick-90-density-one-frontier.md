# T-105250 — The polynomial Wick hierarchy gives a 90% gate and an almost-all transfer lattice

Claim ID: `T-105250`  
Status: **EXACT MODEL/IMPLICATION THEOREM; ACTUAL-XI TRANSFER OPEN**  
Created: 2026-08-24  
Depends on: L-105250--L-105253; PR #726 L-105500  
RH status: unproved

Let `K>=1`. Suppose a source-owned actual-Xi compression `H_(K,T)` and the degree-`K` frozen model `K_(K,T)` satisfy
\[
\operatorname{tr}H_{K,T}\ge\tau_{K,T}\operatorname{tr}K_{K,T},
\qquad
\|H_{K,T}\|_{\rm HS}
\le\upsilon_{K,T}\|K_{K,T}\|_{\rm HS}.
\tag{1}
\]
Assume the exact full-signature/Cauchy-index normalization of PR #726 and `o(N)` endpoint errors.

Then
\[
\eta_{K,T}
\ge
\frac{(\tau_{K,T}/\upsilon_{K,T})^2}
     {1+2\mathcal D_K}+o(1),
\]
and hence
\[
\boxed{
\liminf_{T\to\infty}\frac{N_0(T,2T)}{N(T,2T)}
\ge
\frac{2\,\liminf(\tau_{K,T}/\upsilon_{K,T})^2}
     {1+2\mathcal D_K}-1.
}
\tag{2}
\]

## 1. Robust 90% gate

It is sufficient that
\[
\boxed{
\liminf\frac{\tau_{K,T}}{\upsilon_{K,T}}
>
\sqrt{\frac{19}{20}(1+2\mathcal D_K)}.
}
\tag{3}
\]

For `K=2`, `D_2<=1669/11698176` and the `99/101` comparison give
\[
\boxed{
\liminf\frac{N_0}{N}
\ge
\frac{4997295529}{5425779287}
=0.9210281628\ldots>0.92.
}
\tag{4}
\]
This slightly sharpens the coarser `3500/3501` arithmetic while retaining the same open Xi transfer.

Degree one is borderline at that comparison. Since
\[
\mathcal D_1\ge\frac1{16}\left(\frac1{12}+\frac1{120}\right)
=\frac{11}{1920},
\]
its `99/101` consumer is strictly below `0.9`. Thus degree two is the first square-root truncation certified to cross ninety percent at the one-percent transfer budget.

## 2. Density-one gate without a uniform-in-K theorem

For each fixed `K`, define `PWXFER_(K)` to mean that
\[
\tau_{K,T}\to1,\qquad \upsilon_{K,T}\to1
\]
and all contour/endpoint errors are `o(N)`.

If `PWXFER_(K)` holds for every fixed `K`, then
\[
\liminf\frac{N_0}{N}
\ge\frac{2}{1+2\mathcal D_K}-1
\]
for every `K`. Since `D_K->0`,
\[
\boxed{
\frac{N_0(T,2T)}{N(T,2T)}\longrightarrow1.
}
\tag{5}
\]
No uniformity in `K` is needed: first take the height limit at fixed `K`, then let `K` tend to infinity in the resulting numerical inequalities.

A diagonal transfer with `K(T)->infinity`, `tau/upsilon->1`, and uniform ledgers also proves (5). L-105251 shows polynomial conditioning costs only `O(sqrt K)`, and L-105253 proves the omitted-prime safe-line row remains negligible for very large growing degrees.

## 3. Exact remaining interface

```text
PWXFER105250(K):
  realize the degree-K source-algebra congruence in the actual smooth Xi
  compression and prove trace/HS ratio -> 1, with horizontal, archimedean,
  pole, taper, freezing and endpoint errors o(N).
```

Compared with `TRIWXFER105510`, the nilpotent-projection unit problem and the omitted-prime polynomial tail are removed:

- the square-root polynomial is a unit in every contraction Banach algebra;
- the source has an exact half-line Dirichlet-shift representation;
- the inverse condition is only `O(sqrt K)`;
- the safe-line truncation is power-saving even for growing `K`.

The actual contour/taper representation remains open. Ninety percent, density one, and RH are not established.
