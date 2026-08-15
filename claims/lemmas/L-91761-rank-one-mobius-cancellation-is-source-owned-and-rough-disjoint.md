# L-91761 — Rank-one Möbius cancellation is source-owned and disjoint from rough first ownership

Claim ID: `L-91761`  
Status: **PROPOSED EXACT SOURCE-PARTITION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Authoring agent: `gpt56-pro`  
Depends on: `L-91760`; factor-67 positivity of `L`; first-owner theorem `L-91688`  
RH status: **unproved at this claim**

## 1. Positive and negative source masses at one endpoint

Fix `1<x<67`.  For every squarefree `k<=x`, let

\[
 a_k=\ell_x(k)>0
\]

with `ell` from `L-91760`.  Put

\[
 P_+(x)=\sum_{\substack{k\le x\\\mu(k)=1}}a_k,
 \qquad
 P_-(x)=\sum_{\substack{k\le x\\\mu(k)=-1}}a_k.
\tag{L-91761.1}
\]

Then

\[
 L(x)=P_+(x)-P_-(x)>0.
\tag{L-91761.2}
\]

The atom `k=1` gives `P_+(x)>0`.

## 2. An explicit complete-graph transport

For an odd-sign source occurrence `o` and an even-sign source occurrence `e`, define

\[
\boxed{
 t_x(o,e)=\frac{a_oa_e}{P_+(x)}.
}
\tag{L-91761.3}
\]

Then every negative occurrence is used exactly once:

\[
 \sum_e t_x(o,e)=a_o.
\tag{L-91761.4}
\]

The total amount removed from one positive occurrence is

\[
 \sum_o t_x(o,e)
 =a_e\frac{P_-(x)}{P_+(x)}<a_e.
\tag{L-91761.5}
\]

Define its residual source weight

\[
\boxed{
 r_x(e)=a_e\left(1-\frac{P_-(x)}{P_+(x)}\right)
 =a_e\frac{L(x)}{P_+(x)}>0.
}
\tag{L-91761.6}
\]

Then

\[
\boxed{
 \sum_e r_x(e)=L(x).
}
\tag{L-91761.7}
\]

## 3. Why the transport is simultaneous in every coordinate

At a fixed endpoint `s`, every Möbius colour in `L-91760` multiplies the same normalized infinitesimal packet

\[
 G_s=(g_s,p_s,\text{all linear typed observations}).
\]

Consequently one matched amount `t_x(o,e)` contributes

\[
 +t_x(o,e)G_s-t_x(o,e)G_s=0
\]

simultaneously in:

```text
seed/source coordinates;
component row;
literal score;
ordinary responses;
the q and 4q ordinary columns before radix-four subtraction;
radix-four response;
any finite additive boundary coordinate.
```

Therefore

\[
\boxed{
 \sum_{k\le x}\mu(k)a_kG_s
 =\sum_{\mu(e)=1}r_x(e)G_s
 =L(x)G_s\ge0.
}
\tag{L-91761.8}
\]

This is a literal atomwise source partition, not a coordinatewise complement.  It uses one common-feature coupling rather than a row-dependent Hall lift.

## 4. Measurability

On each quotient cell `N<=x<N+1`, the active squarefree set is fixed and every `a_k` is an algebraic function of `sqrt(x)`.  Hence `P_+`, `P_-`, `t_x`, and `r_x` are continuous on the open cell and have Borel one-sided values at the finitely many knots.

Thus the source transport may be integrated exactly against the positive endpoint measure from `L-91760`; no Hall mesh or activation collar is required.

## 5. Strict separation from rough owners

On the retained factor-67 interval, `k<x<67`.  Every prime divisor of a squarefree root colour `k` is therefore at most `61`.

The rough first-owner labels of `L-91688` begin at prime `67`.  Hence

\[
\boxed{
 \{
 \text{root colour consumed by (L-91761.3)}
 \}
 \cap
 \{
 \text{rough first-owner colour}
 \}
 =\varnothing.
}
\tag{L-91761.9}
\]

The rank-one cancellation cannot spend a rough reservoir atom or duplicate a child owner.

## 6. Compatibility with the inner source

For a rough prime `p` and an integer `u` with `pu<=x`, the scalar source weight obeys the exact same-index law

\[
\boxed{
 \ell_x(pu)=p^{-1/2}\ell_{x/p}(u).
}
\tag{L-91761.10}
\]

Thus rough multiplication changes only the source label and supplies exactly the arithmetic coefficient `p^(-1/2)` used by the same-index child functor.  No affine row-index map occurs.

Apply the first-owner rough partition before forgetting labels.  The retained outer source has no rough label by Section 5.  Every complementary rough-labelled occurrence remains in exactly one internal child colour.  Equation (L-91761.10), together with linearity of the Volterra transform and endpoint integration on each labelled slice, shows that the source equation commutes with first-owner deletion.

Thus the complete source ledger is

```text
positive retained Volterra residual;
unused positive bottom/top restrictions;
one first-owner internal colour for every rough occurrence;
finite mismatch as one current comparison datum.
```

No occurrence belongs to two entries.

## 7. Consequence

Combining `L-91760` and the present theorem gives an explicit source-derived common parent:

\[
\boxed{
 \Lambda_X^{\rm ret}
 =\int_{I_X}\frac2s
   \sum_{\mu(e)=1}r_{X/s}(e)G_s\,ds
 =\int_{I_X}\frac{2L(X/s)}sG_s\,ds.
}
\tag{L-91761.11}

Its finite component row is coefficientwise nonnegative, every source atom has one owner, and its exact signed finite/native correction is `E_X` from `L-91760`.

## 8. Boundary

```text
explicit source transport                        EXACT
all negative colours used once                   EXACT
positive residual sums to L(x)                   EXACT
simultaneous seed/row/response identity           EXACT
measurable whole-cell integration                 EXACT
root source disjoint from rough owners            EXACT
full one-shot physical realization                NEXT THEOREM
Riemann Hypothesis                                UNPROVEN
```
