# L-106122 — The bilateral family is an exact double prime-product collision variety

Claim ID: `L-106122`  
Programme aliases: `LFAM1.DOUBLE_PRODUCT_COLLISION`, `LFAM2.BI_KUMMER_TRACE_VARIETY`, `STRESS.TWO_OWNER_WICK_FOURTH_MOMENTS`  
Status: **PROVED EXACT CHARACTER-COLLISION NORMAL FORM; STRICT COLLISIONS OPEN**  
Created: 2026-08-25  
Depends on: `L-106113`, `L-106120--L-106121`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Modulo the closed repeated-prime terms, one bilateral tensor member contains

\[
 {1\over4}
 \mathcal P_{\psi,c}(s)^2
 \mathcal P_{\chi,d}(s)^2,
\]

where `psi` is a character modulo `rho` on the anchor-owner primes and `chi`
is a character modulo `ell` on the opposite-owner primes.

Write the four anchor-owner labels in a moment expansion as

\[
 p_1,p_2,p_3,p_4
\]

and the four opposite-owner labels as

\[
 q_1,q_2,q_3,q_4.
\]

All source masks, core exclusions and dyadic shells are absorbed in the
coefficients and do not affect character orthogonality.

## 1. Double nonprincipal channel

A complete character average in both moduli gives exactly

\[
\boxed{
 p_1p_2\equiv p_3p_4\pmod\rho,
 \qquad
 q_1q_2\equiv q_3q_4\pmod\ell.
}
\tag{L-106122.1}
\]

For the even-character quotient used by the Gauss frame, each congruence is
replaced by the union of its two sign components:

\[
\boxed{
 p_1p_2\equiv\pm p_3p_4\pmod\rho,
 \qquad
 q_1q_2\equiv\pm q_3q_4\pmod\ell.
}
\tag{L-106122.2}
\]

Thus the nonprincipal--nonprincipal tensor channel is the fibre product of two
prime-product collision varieties.

## 2. Mixed channels

The principal--nonprincipal channel has only the opposite-owner collision
condition

\[
 q_1q_2\equiv\pm q_3q_4\pmod\ell,
\tag{L-106122.3}
\]

while the anchor owner polynomial remains untwisted.  The
nonprincipal--principal channel has only

\[
 p_1p_2\equiv\pm p_3p_4\pmod\rho.
\tag{L-106122.4}
\]

The principal--principal channel has no character collision constraint and is
the native untwisted two-owner Wick moment.

## 3. Literal diagonals

If

\[
 p_1p_2=p_3p_4,
 \qquad
 q_1q_2=q_3q_4
\]

as integers, unique unordered semiprime factorization puts the term in the
atomic/equal-product ledger of `L-106121` and parent `L-102747`.
Repeated labels `p_1=p_2` or `q_1=q_2` are the closed diagonal Wick
polynomials.

Shared-owner and owner/core incidences are removed before the clean tensor
packet by the inherited decreasing-prime and common-factor renewals.  Hence
the genuinely new nonprincipal--nonprincipal region is

\[
\boxed{
\begin{aligned}
&p_1p_2\equiv\pm p_3p_4\pmod\rho,
&&p_1p_2\ne p_3p_4,\\
&q_1q_2\equiv\pm q_3q_4\pmod\ell,
&&q_1q_2\ne q_3q_4,
\end{aligned}
}
\tag{L-106122.5}
\]

with all eight owner labels clean unless a separately typed renewal applies.

## 4. Exact tensor-channel gates

Define:

```text
BTPP106122:
  the off-atomic principal--principal prime-Wick tensor moment is subpower;

BTPN106122:
  the sum of the two mixed channels, after removal of equal products and
  inherited renewals, is subpower;

BTNN106122:
  the strict double product-collision moment (L-106122.5) is subpower.
```

The positive tensor decomposition gives

\[
\boxed{
 \mathrm{BTPP}_{106122}
 \wedge
 \mathrm{BTPN}_{106122}
 \wedge
 \mathrm{BTNN}_{106122}
 \Longrightarrow
 \mathfrak M_{\rm BT}(Y)=Y^{o(1)}.
}
\tag{L-106122.6}

None of the three gates is proved here.

## 5. Function-field geometry

Over `F_q[T]`, the double nonprincipal channel is the fibre product of the two
Kummer multiplication maps

\[
 (p_1,p_2,p_3,p_4)\mapsto p_1p_2/(p_3p_4),
 \qquad
 (q_1,q_2,q_3,q_4)\mapsto q_1q_2/(q_3q_4),
\]

coupled to the two source-selected Artin--Schreier phases at `ell` and `rho`.
The exact geometric task is to remove constant and diagonal constituents and
compute the monodromy of the remaining fibre product.  This is the target
`FFBT106120` in `T-106120`.

## Scope

The lemma proves the complete collision dictionary and the exact channel
split.  It does not estimate the strict collision varieties or the untwisted
principal tensor.
