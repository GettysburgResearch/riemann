# L-106125 — Large phase conductors force owner-product diagonals

Claim ID: `L-106125`  
Programme aliases: `LFAM1.LARGE_CONDUCTOR_DIAGONAL`, `LFAM2.PRODUCT_COLLISION_SUPPORT`, `STRESS.NONPRINCIPAL_RANGE_LOCALIZATION`  
Status: **PROVED UNCONDITIONAL SUPPORT REDUCTION AND CLOSURE OF LARGE-CONDUCTOR NONPRINCIPAL SECTORS**  
Created: 2026-08-25  
Depends on: `L-106122`; parent same-owner/equal-pair renewals `L-102747`, `L-102832`, `L-102837`, `L-102862`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Put the two owner products in dyadic intervals

\[
 A\le P,P'<2A,
 \qquad
 B\le Q,Q'<2B.
\tag{L-106125.1}
\]

The anchor nonprincipal character is modulo `rho`; the opposite-owner
nonprincipal character is modulo `ell`.

## 1. One product-collision modulus

Suppose

\[
 P\equiv P'\pmod\rho.
\]

Since

\[
 |P-P'|<A,
\]

one has

\[
\boxed{
 \rho>A
 \quad\Longrightarrow\quad
 P=P'.
}
\tag{L-106125.2}
\]

For the negative component,

\[
 P\equiv-P'\pmod\rho
 \quad\Longrightarrow\quad
 \rho\mid P+P'.
\]

But `0<P+P'<4A`, so

\[
\boxed{
 \rho>4A
 \quad\Longrightarrow\quad
 P\not\equiv-P'\pmod\rho.
}
\tag{L-106125.3}
\]

Consequently, for

\[
 \rho>4A,
\]

the complete even-character product-collision relation reduces to literal
integer equality `P=P'`.

The same argument gives

\[
\boxed{
 \ell>4B
 \quad\Longrightarrow\quad
 Q\equiv\pm Q'\pmod\ell
 \text{ only through }Q=Q'.
}
\tag{L-106125.4}
\]

## 2. Equal owner products are inherited closed sectors

For squarefree semiprime owner products, `P=P'` identifies the same unordered
owner pair, up to the fixed labelled copies of `67`.  Cross terms with the
same owner pair and different cores are in the inherited same-owner
square-core overlap/common-factor renewal.  Repeated labels and equal physical
products are already in the diagonal ledger.

Thus the large-conductor equal-product residue in (L-106125.2)--
(L-106125.4) has subpower physical cost.

## 3. Closed mixed channels

In the principal--nonprincipal channel, the only strict collision is on the
opposite-owner side.  Therefore

\[
\boxed{
 \ell>4B
 \quad\Longrightarrow\quad
 \text{the principal--nonprincipal block is inherited closed.}
}
\tag{L-106125.5}
\]

Similarly,

\[
\boxed{
 \rho>4A
 \quad\Longrightarrow\quad
 \text{the nonprincipal--principal block is inherited closed.}
}
\tag{L-106125.6}
\]

## 4. Double nonprincipal channel

A genuinely strict double collision can occur only when

\[
\boxed{
 \rho\le4A,
 \qquad
 \ell\le4B.
}
\tag{L-106125.7}
\]

If either inequality fails, the corresponding owner products agree and that
side reduces to the inherited same-owner ledger; the remaining term is at
worst one of the already-typed mixed channels.

## 5. Correct residual gates

The nonprincipal gates of `T-106120` may therefore be sharpened to:

```text
BTPN-S106125:
  mixed strict product collisions only in the range conductor <= 4 owner
  product scale;

BTNN-S106125:
  strict double product collisions only in the simultaneous range

      rho <= 4A and ell <= 4B.
```

All complementary nonprincipal blocks are unconditionally closed.

## Meaning

The family obstruction cannot live in a conductor which is much larger than
its owner amplifier.  It is confined to the genuinely balanced
conductor/owner regime, exactly where a hybrid large sieve or trace formula is
expected to be sharp.

## Scope

The theorem does not affect the untwisted principal--principal channel.  It
does not prove the residual mixed or double nonprincipal moments in
(L-106125.7), `BCI102990`, or RH.
