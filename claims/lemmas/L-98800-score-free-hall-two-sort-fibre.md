# L-98800 — Compact Hall gives one positive two-sort fibre

Claim ID: `L-98800`
Status: **PROPOSED COMPLETE EXACT TYPE RECONSTRUCTION ON FROZEN HALL INPUTS**
Depends on: `R-98800`; frozen `L-91690`; component-profile monotonicity
RH status: **not assumed**

## 1. Source and row sorts

Fix `1<x<67`.  Let `E_x` and `O_x` be the positive and negative compact
`P_61` occurrences.  Frozen `L-91690` supplies a no-upward target flow
`t_x(o,e)>=0` satisfying

\[
\sum_e t_x(o,e)=T_x(o),\qquad
\sum_o t_x(o,e)\le T_x(e),\qquad
 t_x(o,e)>0\Rightarrow e\le o.
\]

Define residual target mass

\[
 u_x(e)=T_x(e)-\sum_o t_x(o,e)\ge0.
\]

The replacement packet category is

\[
\boxed{
 \mathsf C_x=\mathsf{Src}_x^+\oplus\mathsf{Row}_x^+.
}
\]

- `Src` carries source provenance, target mass, declared score, component rows,
  ordinary/detail responses, and may be causally split.
- `Row` carries only a finite nonnegative component-row vector with endpoint and
  Hall-edge provenance.  It has **no target coordinate, no declared-score
  coordinate, and no recursive child operation**.

## 2. Exact Hall identities

For each row profile

\[
 \rho_{x,j}(k)=A_{x,j}(k)/T_x(k),
\]

finite algebra gives

\[
\boxed{
 \sum_eT_x(e)\rho_{x,j}(e)-\sum_oT_x(o)\rho_{x,j}(o)
 =\sum_eu_x(e)\rho_{x,j}(e)+B_{x,j},
}
\]

where

\[
 B_{x,j}=\sum_{o,e}t_x(o,e)
 [\rho_{x,j}(e)-\rho_{x,j}(o)]\ge0.
\]

Target conservation is

\[
 \sum_k\mu(k)T_x(k)=\sum_eu_x(e).
\]

The score ratio is decreasing in the endpoint variable, so the residual source
satisfies the favorable inequality

\[
 \sum_eu_x(e)\frac{S_x(e)}{T_x(e)}
 \ge \sum_k\mu(k)S_x(k).
\]

No score equality is assigned to `B_x`.

## 3. Positive fibre

Define

\[
 \mu_x=\sum_eu_x(e)\,\delta_e\in\mathsf{Src}_x^+,
 \qquad
 \beta_x=(B_{x,j})_{j\ge2}\in\mathsf{Row}_x^+.
\]

Then

\[
\boxed{
 \mathfrak C_x=(\mu_x,\beta_x)\ge0
}
\]

has the exact signed compact component row under the realization

\[
 \mathcal R_x(\mu,\beta)
 =\mathcal R_x^{\rm src}(\mu)+\beta.
\]

Every matched target edge owns one term of `beta_x`; every unmatched positive
occurrence owns one atom of `mu_x`.  Neither is duplicated.

## 4. Physical positivity of the bonus

The component coefficients `B_{x,j}` are nonnegative.  The frozen component
basis has nonnegative ordinary and radix-four response kernels, hence `beta_x`
is a valid positive current-row object.  This statement uses no source or score
coordinate for the bonus.

## 5. Boundary

```text
target Hall residual             positive / exact
residual declared score          favorable inequality
Hall row bonus                   componentwise nonnegative
Hall bonus target                absent
Hall bonus declared score        absent
Hall bonus recursive child       forbidden
complete signed component row    exact after realization
RH                               unproved
```
