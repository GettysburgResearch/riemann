# L-105450 — Every shared-owner sector is a removable common-factor renewal

Claim ID: `L-105450`

Status: **PROVED EXACT SOURCE-RENEWAL THEOREM**

Freeze the largest-two semiprime-squareclass gauge of PR #719 at

```text
2ee5c675a7a2a30ce04ad6609dc7800849bedccc.
```

A hard physical product has the unique form

\[
N=pq\,a^2,
\qquad
p>q>P^+(a).
\]

Let

\[
N=pq\,a^2,
\qquad
M=rs\,b^2
\]

have different owner pairs and suppose

\[
\{p,q\}\cap\{r,s\}=\{\ell\}.
\]

Assume first that no owner lies in the opposite square core; owner/core
incidences are removed by `L-102862`.

Because `ell` is an owner on both sides and is absent from both cores,

\[
v_\ell(N)=v_\ell(M)=1.
\]

Put

\[
N=\ell N_1,
\qquad
M=\ell M_1.
\]

Then

\[
\ell\nmid N_1M_1.
\tag{L-105450.1}
\]

For the physical translate

\[
v_n(u)=n^{-1/2}\phi(u-\log n),
\]

one has

\[
v_N=\ell^{-1/2}U_\ell v_{N_1},
\qquad
v_M=\ell^{-1/2}U_\ell v_{M_1}.
\]

Translation invariance of every fixed logarithmic block and centered outer
kernel therefore gives

\[
\boxed{
\langle v_N,v_M\rangle
=
\frac1\ell\langle v_{N_1},v_{M_1}\rangle.
}
\tag{L-105450.2}
\]

This argument does not require `ell` to be the greatest owner. In particular,
it covers

\[
\{p,q\}=\{11,5\},
\qquad
\{r,s\}=\{7,5\},
\]

where the shared owner `5` is second-largest on both sides.

## Renewal

After extracting `ell`, reapply the exact largest-two/source-region gauge to
the reduced packet. Equation (L-105450.1) prevents the same common-owner
incidence from recurring. Positive homogeneity and subadditivity of the
carrier-recombined radial cost give

\[
\boxed{
E_{\rm sh}(Y;\mathcal P)
\le
C\sum_{\ell\in\mathcal P}\frac1\ell
E(Y/\ell;\mathcal P\setminus\{\ell\})
+
Y^{o(1)}.
}
\tag{L-105450.3}
\]

The terminal term consists only of the already-closed repeated-prime,
equal-product, same-pair, owner/core-overlap and finite packets.

Every renewal history uses distinct primes. Hence its total path mass is

\[
\sum_{S\subseteq\mathcal P}
\frac{C^{|S|}}{\prod_{\ell\in S}\ell}
=
\prod_{\ell\in\mathcal P}
\left(1+\frac C\ell\right)
\ll_C(\log(2Y))^C.
\tag{L-105450.4}
\]

Therefore

\[
\boxed{
E_{\rm disjoint}(Y)=Y^{o(1)}
\Longrightarrow
E_{\rm all\ owner\ pairs}(Y)=Y^{o(1)}.
}
\tag{L-105450.5}
\]

The shared-owner part of the F1 pair-star ledger is consequently recursive,
not an independent terminal theorem. This strengthens the scope of
`L-102837`, whose displayed direct factorization treats a shared greatest
owner.
