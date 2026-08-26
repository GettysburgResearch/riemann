# L-102862 — Owner/core overlaps form a polylogarithmic common-factor renewal

Claim ID: `L-102862`  
Status: **PROVED EXACT SOURCE-RENEWAL REDUCTION**  
Created: 2026-08-24  
Depends on: `L-102831`, `L-102860`; `L-102733`  
RH status: **not assumed**

Let

\[
N=pq\,a^2,
\qquad
M=rs\,b^2
\]

be two four-distinct-owner products. An owner/core overlap is a prime in

\[
\mathcal O(N,M)
=
\bigl(\{p,q\}\cap\operatorname{supp}b\bigr)
\cup
\bigl(\{r,s\}\cap\operatorname{supp}a\bigr).
\]

If `ell` belongs to this set, then its valuations in `N` and `M` are `1` and
`2` in some order. Hence one common copy may be extracted:

\[
N=\ell N_1,
\qquad
M=\ell M_1,
\]

and for the fixed log-translation observation

\[
\boxed{
\langle v_N,v_M\rangle
={1\over\ell}\langle v_{N_1},v_{M_1}\rangle.
}
\tag{L-102862.1}

After extraction, `ell` has odd valuation in exactly one reduced product and
zero valuation in the other. Thus this particular common owner/core incidence
cannot recur.

## 1. Exact renewal

Apply the largest-two gauge again to the reduced source occurrence. Positive
homogeneity and subadditivity of the centered radial/outer cost give

\[
\boxed{
E_{\rm overlap}(Y;\mathcal P)
\le
C\sum_{\ell\in\mathcal P}{1\over\ell}
E(Y/\ell;\mathcal P\setminus\{\ell\})
+Y^{o(1)}.
}
\tag{L-102862.2}

The terminal term contains only squared/repeated-label, equal-product and
same-pair regions already closed on PR #719. Each renewal step removes one
literal common incidence and lowers the physical scale.

## 2. Path mass

Iterating (L-102862.2) produces distinct-prime paths. Their total weight is
bounded by

\[
\sum_{S\subseteq\mathcal P}{C^{|S|}\over\prod_{\ell\in S}\ell}
=
\prod_{\ell\in\mathcal P}\left(1+{C\over\ell}\right)
\ll_C(\log(2Y))^C.
\tag{L-102862.3}

Therefore

\[
\boxed{
E_{\rm clean}(Y)=Y^{o(1)}
\Longrightarrow
E_{\rm full}(Y)=Y^{o(1)}.
}
\tag{L-102862.4}

## Clean direct sector

The conclusion-bearing dispersion theorem may henceforth assume

\[
\boxed{
\{p,q\}\cap\operatorname{supp}b=\varnothing,
\qquad
\{r,s\}\cap\operatorname{supp}a=\varnothing.
}
\tag{L-102862.5}

In this clean sector every owner prime divides exactly one physical product,
so balanced phase directions may be chosen without an orientation ambiguity.