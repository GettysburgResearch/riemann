# L-93880 — The native Möbius datum has an exact positive hybrid common parent

Claim ID: `L-93880`  
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Depends on: the displayed finite Möbius formulas; `L-91760/L-91761`; the directed positivity of `L(x)` on `1<x<67`  
RH status: **unproved at this claim**

## 1. Exact finite and continuum rows

For real `X>=1`, define

\[
d_X^\star(t)=
 \sum_{k\le X/t}\frac{\mu(k)}{\sqrt{kt}}\log\frac{X}{kt},
\qquad t\ge1,
\]

\[
b_X^\star(n)=\sum_{m=n}^{\lfloor X\rfloor}d_X^\star(m),
\qquad
\overline b_X^\star(n)=\int_n^X d_X^\star(t)\,dt,
\]

and

\[
E_X=b_X^\star-\overline b_X^\star.
\]

Let `\mathcal R` be the exact finite component-row map. Put

\[
c_X=\mathcal Rb_X^\star,\qquad
\overline c_X=\mathcal R\overline b_X^\star.
\]

Then, without approximation,

\[
\boxed{c_X=\overline c_X+\mathcal R E_X.}
\tag{L-93880.1}
\]

The finite and continuum rows are not identified.

## 2. Whole-cell split

For integer `X`, put

\[
K=\left\lfloor X/67\right\rfloor+1,\qquad W=10000,
\]

and let

\[
\mathcal I_X=\{n\in\mathbb Z:K+2\le n\le X-W-3\}.
\]

Define the retained-cell defect

\[
E_X^I(n)=
\sum_{\substack{m\in\mathcal I_X\\m\ge n}}
\left(d_X^\star(m)-\int_m^{m+1}d_X^\star(t)\,dt\right).
\]

The complementary integer cells are kept as the literal anchored finite datum.
Therefore

\[
\boxed{
c_X=c_{X,\mathrm{anc}}+
     \overline c_{X,\mathrm{bulk}}+
     \mathcal R E_X^I.
}
\tag{L-93880.2}
\]

Every term is defined from disjoint cells. There is no cutoff atom.

## 3. Positive infinitesimal packet

For real `s>=1`, let

\[
g_s(m)=\left(\sqrt m-\frac m{\sqrt s}\right)\mathbf1_{m\le s},
\qquad
p_s=\mathcal R g_s.
\]

The exact Green formula gives

\[
g_s(m)\ge0,\qquad p_s(j)\ge0.
\tag{L-93880.3}
\]

For `x>=1` and squarefree `k<=x`, define

\[
\ell_x(k)=\frac1{\sqrt k}\left(2\sqrt{x/k}-1\right)>0
\]

and

\[
L(x)=\sum_{k\le x}\mu(k)\ell_x(k).
\]

Direct integration gives the one-colour identity

\[
\frac1{\sqrt k}\int_n^{X/k}t^{-1/2}\log\frac{X/k}{t}\,dt
=
\int_n^{X/k}\frac2s\,\ell_{X/s}(k)g_s(n)\,ds.
\tag{L-93880.4}
\]

Finite Fubini yields

\[
\boxed{
\overline c_{X,\mathrm{bulk}}
=
\int_{I_X}\frac{2L(X/s)}s\,p_s\,ds.
}
\tag{L-93880.5}
\]

## 4. Rank-one cancellation is atomwise

Fix `1<x<67`. Let

\[
P_+(x)=\sum_{\mu(e)=1}\ell_x(e),\qquad
P_-(x)=\sum_{\mu(o)=-1}\ell_x(o).
\]

The directed finite-cell proof gives

\[
L(x)=P_+(x)-P_-(x)>\frac{159}{500}.
\tag{L-93880.6}
\]

Define

\[
t_x(o,e)=\frac{\ell_x(o)\ell_x(e)}{P_+(x)}.
\]

Then every negative source mass is used exactly once,

\[
\sum_e t_x(o,e)=\ell_x(o),
\]

and every positive colour retains

\[
r_x(e)=\ell_x(e)\frac{L(x)}{P_+(x)}>0.
\]

Since every colour multiplies the identical typed packet `p_s`, each matched
pair cancels in source, row, score, ordinary response at `q` and `4q`, detail,
and additive boundary coordinates. Thus

\[
\boxed{
\sum_{k\le x}\mu(k)\ell_x(k)p_s
=
\sum_{\mu(e)=1}r_x(e)p_s
=
L(x)p_s\ge0.
}
\tag{L-93880.7}
\]

This is not a coordinatewise complement and uses no profile monotonicity.

## 5. Exact bulk source

The retained bulk source is therefore

\[
\boxed{
\Sigma_{X,\mathrm{bulk}}
=
\int_{I_X}\frac2s
\sum_{\mu(e)=1}r_{X/s}(e)[s,e]\otimes p_s\,ds
\ge0.
}
\tag{L-93880.8}
\]

Its observation is exactly `\overline c_{X,\mathrm{bulk}}`.

## 6. Anchored sector

The anchored complement is the literal finite Möbius source on the omitted
whole cells and rough stopping leaves. It is not approximated by the continuum
source. Its positive realization is constructed in `L-93881`.

Combining the two sectors gives the exact hybrid input marginal

\[
\boxed{
c_X=
\operatorname{Obs}(\Sigma_{X,\mathrm{bulk}})
+
\operatorname{Obs}(\Sigma_{X,\mathrm{anc}})
+
\mathcal R E_X^I.
}
\tag{L-93880.9}
\]

The first two terms are positive source-owned rows. The last term is the sole
signed finite/continuum observation.

## 7. Quantifiers and ownership

The construction holds for every integer `X` with nonempty retained interval.
All integrations are finite. Each integer cell is either anchored or bulk, not
both. Each bulk Möbius colour is matched or residual exactly once. Rough first
owners begin at prime `67`, while bulk colours satisfy `k<67`; the label sets
are disjoint.

## 8. Boundary

```text
finite/continuum identity                    EXACT
whole-cell source partition                  EXACT
bulk Volterra order swap                     EXACT
bulk source positivity                       EXACT / DIRECTED L>0
bulk Hall/profile theorem                    NOT USED
anchored positive realization                L-93881
signed defect positivity                     NOT CLAIMED
Riemann Hypothesis                           UNPROVEN
```
