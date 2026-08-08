# L-26805 — RH-sensitive source change is an exact half-scale descent

Claim ID: `L-26805`  
Title: The RH-sensitive annular carry source equals the generalized-prime source minus an explicit positive-inverse proper-divisor family at scale at most one half  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26802`, `R-26802`; PR #269 `L-26903`  
Scope: exact source-change recurrence; no quantitative charge bound or RH conclusion

## 1. The two carry coefficient sequences

Retain

\[
 \omega_2*a_\omega=\varepsilon
\]

and the generalized von Mangoldt sequence

\[
 \Lambda_\omega=\omega_2*(a_\omega\log).
\]

Define the RH-sensitive coefficient sequence

\[
 \boxed{
 W=\omega_2*\Lambda_\omega.
 }
 \tag{L-26805.1}
\]

The annular physical source with coefficient `Lambda_omega` has carry image
`W` by `L-26802`.

Convolving (L-26805.1) with `a_omega` gives the exact identity

\[
 \boxed{
 a_\omega*W=\Lambda_\omega.
 }
 \tag{L-26805.2}
\]

Thus the generalized-prime carry profile of PR #269 is the positive-inverse
synthesis of the RH-sensitive profile.

## 2. Current term plus strict lower scale

Since \(a_\omega(1)=1\), equation (L-26805.2) reads coefficientwise

\[
 \boxed{
 \Lambda_\omega(n)
 =W(n)
 +\sum_{\substack{d\mid n\\d\ge2}}
 a_\omega(d)W(n/d).
 }
 \tag{L-26805.3}
\]

Equivalently,

\[
 \boxed{
 W(n)
 =\Lambda_\omega(n)
 -\sum_{\substack{d\mid n\\d\ge2}}
 a_\omega(d)W(n/d).
 }
 \tag{L-26805.4}
\]

Every destination satisfies

\[
 n/d\le n/2.
 \tag{L-26805.5}
\]

Therefore the source change has identity coefficient one on the current scale;
all other terms are strictly lower scale. There is no same-scale condition
number or infinite inversion at this stage.

## 3. Exact carry-profile recurrence

For a carry row \(N\), define

\[
 \mathcal W_N(j)
 =\sum_{q\le N}W(q)\chi_{N,q}(j),
\]

and

\[
 \mathcal P_N(j)
 =\sum_{q\le N}\Lambda_\omega(q)\chi_{N,q}(j).
\]

Substitution of (L-26805.3) gives

\[
 \boxed{
 \mathcal P_N(j)
 =\mathcal W_N(j)
 +\sum_{d=2}^{N}a_\omega(d)
  \sum_{m\le N/d}W(m)\chi_{N,dm}(j).
 }
 \tag{L-26805.6}
\]

The inner vector is the scaled carry feature of the same RH-sensitive source
on arithmetic output at most \(N/d\le N/2\).

Thus the PR #269 profile with its strict transition reserve differs from the
RH-sensitive profile only by a complete declared family of half-scale source
rows.

## 4. Exact atomic and annular form

For a coefficient set \(A\subset\mathbb N\), write

\[
 \alpha_{W,A}
 =\sum_{n\in A}\frac{W(n)}{\sqrt n}\delta_{\log n},
 \qquad
 \alpha_{\Lambda,A}
 =\sum_{n\in A}\frac{\Lambda_\omega(n)}{\sqrt n}\delta_{\log n}.
\]

For one annulus

\[
 A_M=[M,2M)\cap\mathbb N,
\]

equation (L-26805.4) becomes

\[
 \boxed{
 \alpha_{W,A_M}
 =\alpha_{\Lambda,A_M}
 -\sum_{d=2}^{2M-1}
  \frac{a_\omega(d)}{\sqrt d}
  \tau_{\log d}\,
  \alpha_{W,A_M/d},
 }
 \tag{L-26805.7}
\]

where

\[
 A_M/d
 =\{m\in\mathbb N:M\le dm<2M\}.
\]

Every set \(A_M/d\) lies below \(M\), and for \(d\ge2\) below the current
half-scale endpoint. It intersects at most two adjacent dyadic annuli.

Convolution by any compact window, including the critical parity windows of
`L-26804`, preserves (L-26805.7) exactly.

## 5. Interaction with the established carry reserve

PR #269 proves a strict source-specific carry reserve for
\(\mathcal P_N\). Equation (L-26805.6) gives the fail-closed mechanism for
using it:

```text
current RH-sensitive profile W
+ complete proper-divisor source-change family
= reserved generalized-prime profile P.
```

A production energy proof must retain every cross term between the current
\(\mathcal W_N\) vector and the lower-scale family. It may then complete the
\(\mathcal P_N\) square and route the remaining family to earlier annuli.

The exact identity does not by itself prove that the total lower-scale charge is
smaller than the reserve.

## 6. Relation to the generalized Selberg defect

`L-26803` gives a second proper-divisor half-scale family:

\[
 a_\omega(n)\log^2n-\mathcal F(n)
 =\sum_{\substack{d\mid n\\d\ge2}}
  a_\omega(d)\mathcal F(n/d).
\]

Both the source change (L-26805.4) and the Selberg defect use the same positive
inverse coefficients and the same strict divisor descent. They should be
assembled in one lower-block ledger rather than estimated independently by
absolute values.

## 7. What this closes

The apparent same-scale mismatch identified in `R-26802` is resolved exactly:

\[
 \boxed{
 \text{RH-sensitive source}
 =
 \text{reserved generalized-prime source}
 -
 \text{complete half-scale divisor family}.
 }
\]

No generic inverse theorem is required.

## 8. What remains open

A full proof still needs to establish that, after all reflected cross terms are
retained, the combined source-change, Selberg-defect, and digital boundary
families have total lower-block charge strictly below the current annular
reserve.

This quantitative statement is the corrected `ASSD` theorem.

## 9. Firewalls

Reject any use of this lemma that:

- drops one proper divisor;
- takes absolute values before completing the \(\mathcal P_N\) square;
- treats \(a_\omega(d)\) as a summable contraction kernel;
- routes the current term \(d=1\) to lower scale;
- claims that (L-26805.4) alone proves a norm contraction;
- loses the reciprocal-zeta pole of the \(W\) source.

RH remains unproved.
