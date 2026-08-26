# L-102880 — The unrestricted stopped-prefix Type-I adverse part is power-saving

Claim ID: `L-102880`  
Status: **PROVED EXACT ONE-SIDED TYPE-I THEOREM**  
Created: 2026-08-24  
Depends on: corrected `L-102866`; `R-102868`; `L-102869`  
RH status: **not assumed**

Retain the literal finite-prime prefix

\[
M_{U,q}=
\sum_{\substack{d\le U\\P^+(d)<q}}{\mu(d)\over d},
\qquad
U=\lfloor Y^{1/6}\rfloor.
\]

The unrestricted lattice part of the stopped Type-I coordinate satisfies

\[
\boxed{
\mathcal T_{p,q}^{\rm full}(Y)
=4(\sqrt2-1)(\log2)^2 M_{U,q}^2
+O_R(Y^{-1/6}).
}
\tag{L-102880.1}
\]

The coefficient of the square is strictly positive.  Hence

\[
\boxed{
(\mathcal T_{p,q}^{\rm full}(Y))_-
\ll_R Y^{-1/6},
}
\tag{L-102880.2}
\]

uniformly in the external owners `p>q` and in the finite-prime stopping
parameter.

Integrating over one dyadic physical horizon gives

\[
\boxed{
\int_Y^{2Y}
(\mathcal T_{p,q}^{\rm full}(X/(pq)))_-
{dX\over X}
\ll_R (Y/(pq))^{-1/6},
}
\tag{L-102880.3}
\]

whenever the nonterminal support is active.  Summation over the finitely many
terminal scales is an absolute constant.

## Exact use in the conclusion ledger

The square in (L-102880.1) is a favorable Type-I reserve.  Later source
partitions may discard it when forming an upper bound for negative mass, but
may not also spend it as a positive reserve in another channel.

Thus the stopped square-core Vaughan decomposition has no open unrestricted
Type-I sign.  Its only live Type-I component is the moving smooth-boundary
current of `L-102869.6`, treated by the ordered renewal theorem `L-102881`.