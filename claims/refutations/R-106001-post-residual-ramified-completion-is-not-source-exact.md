# R-106001 — Ramified completion cannot be applied after residual selection

Claim ID: `R-106001`  
Status: **PROVED EXACT SOURCE-ORDER FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106000`; PR #719 through `L-102888`  
RH status: **unproved**

The principal-character restoration in `L-106000` is an identity for the full
Möbius source:

\[
(I-\ell^{-1/2}S_\ell)
\sum_{\ell\nmid n}{\mu(n)\over\sqrt n}\Phi(X/n)
=
\sum_n{\mu(n)\over\sqrt n}\Phi(X/n).
\tag{R-106001.1}
\]

It is **not** an identity for an arbitrary coefficient packet obtained after a
carrier quotient, owner selection, Vaughan split, regional restriction or
negative-part operation.

Indeed, let `r(n)` be supported only at `n=ell`, with `r(ell)=1`. Principal
character twisting kills the packet. Applying `I-ell^(-1/2)S_ell` afterwards
still gives zero, not the original packet. Thus the coefficient relation

\[
r(\ell m)=-r(m)
\]

needed by the elementary restoration need not survive an arbitrary residual
projection.

## Binding order

The only source-exact construction is:

```text
full native source
 -> character twist
 -> ramified two-scale completion
 -> complete linear carrier recombination
 -> Wick / owner / dyadic-frozen Vaughan decomposition
 -> residual selection
 -> observation or positive family moment.
```

The following order is invalid unless separately proved for the literal
residual:

```text
native source
 -> residual selection
 -> character twist
 -> ramified completion.
```

In particular, one may not define the family residual merely by twisting the
already-extracted `SLCD` or `HBCQDSP` coefficient row and then quote
`L-106000.10`.

The corrected commuting diagram is stated in `L-106004`. No previously proved
full-source Mellin identity is refuted.