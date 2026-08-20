# L-101001 — Largest-prime and balanced-Vaughan terminal gates differ only by an \(L^1(dX/X)\) error

Claim ID: `L-101001`  
Status: **PROVED EXACT GATE-EQUIVALENCE THEOREM**  
Created: 2026-08-20  
Frozen inputs: PR #688 and PR #685  
RH status: **not assumed**

Let \(G_\mu(X)\) be the minimal ordinary-Möbius ratio-eight wavelet.

PR #688 gives the exact largest-prime decomposition

\[
\boxed{
G_\mu(X)=G_{\rm sm}(X)+G_{\rm rough}(X),
}
\tag{L-101001.1}
\]

where

\[
G_{\rm sm}(X)=X^{-1/6+o(1)}.
\tag{L-101001.2}
\]

PR #685 gives the exact zero-moment Vaughan decomposition

\[
\boxed{
G_\mu(X)=\mathcal T(X)+\mathcal B(X),
}
\tag{L-101001.3}
\]

where

\[
\mathcal T(X)=O(X^{-1/6}).
\tag{L-101001.4}
\]

Subtracting the two identities gives

\[
\boxed{
G_{\rm rough}(X)-\mathcal B(X)
=
\mathcal T(X)-G_{\rm sm}(X).
}
\tag{L-101001.5}
\]

The right-hand side belongs to \(L^1([2,\infty),dX/X)\).  Indeed,
(L-101001.2) implies that for some fixed \(\delta>0\),

\[
|G_{\rm sm}(X)|\ll X^{-\delta}
\]

eventually, and (L-101001.4) is integrable directly.

For real numbers \(a,b\),

\[
|a_--b_-|\le|a-b|.
\]

Consequently

\[
\boxed{
\int_2^Y(G_{\rm rough}(X))_-\frac{dX}{X}
=
Y^{o(1)}
\iff
\int_2^Y(\mathcal B(X))_-\frac{dX}{X}
=
Y^{o(1)}.
}
\tag{L-101001.6}
\]

## Matrix consequence

The apparently distinct terminal gates

```text
LPMW100410   rough largest-prime wavelet;
BVD100310    balanced Vaughan trilinear
```

are the same middle estimate modulo a harmless integrable perturbation.

Their structural leverage remains different:

```text
largest-prime form   exposes unique prime ownership and a smooth/rough split;
Vaughan form         removes all Type-I terms and exposes a balanced trilinear.
```

But they occupy one node in the implication quotient graph.  Proving both is
not a two-key closure; proving either proves the other and then RH.
