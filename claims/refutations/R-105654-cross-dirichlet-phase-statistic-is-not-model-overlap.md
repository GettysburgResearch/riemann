# R-105654 — The cross-Dirichlet phase statistic is not the model-space overlap

Claim ID: `R-105654`  
Status: **PROVED EXACT COUNTEREXAMPLE; SIBLING EQUALITY CORRECTED**  
Created: 2026-08-27  
Depends on: `L-106506`, `L-106512`, corrected sibling `L-106514`  
RH status: **not assumed**

## 1. The two quantities

For finite upper-half-plane inner functions `B_+` and `B_-`, let

\[
\mathcal O(B_+,B_-)
=
\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}})
\]

be the positive canonical-correlation overlap, and let

\[
\Delta(B_+,B_-)
=
\frac{1}{2\pi i}
\int_{\mathbb R}\frac{B_+'(t)}{B_-(t)}\,dt
\]

be the cross-Dirichlet scalar.  The adverse all-pass charge is exactly

\[
\|H_{B_+/B_-}\|_{\mathcal S_2}^2
=
\deg B_- - \mathcal O(B_+,B_-).
\]

The former sibling formulation identified `Delta` with `mathcal O`.  That is
false, already in rank one and dramatically in a two-factor rational packet.

## 2. Rank-one strict separator

Take

\[
B_-(z)=\frac{z-i}{z+i},
\qquad
B_+(z)=\frac{z-1-i}{z-1+i}.
\]

The normalized model vectors have squared overlap

\[
\mathcal O=\frac45,
\]

so

\[
\|H_{B_+/B_-}\|_{\mathcal S_2}^2=\frac15.
\]

But

\[
\Delta
=
\frac{B_+'(i)}{B_-'(i)}
=
\frac{12}{25}-\frac{16}{25}i.
\]

The denominator phase statistic is therefore

\[
1-\operatorname{Re}\Delta=\frac{13}{25}\ne\frac15.
\]

Thus the phase statistic is an upper majorant, not the exact adverse charge.

## 3. Exact two-factor rational separator

Take

\[
B_-(z)
=
\frac{(z-i)(z-2i)}{(z+i)(z+2i)},
\qquad
B_+(z)
=
\frac{(z-3i)(z-4i)}{(z+3i)(z+4i)}.
\]

For depths `d=(1,2)` define the rational Cauchy matrices

\[
G_s=
\left[\frac1{d_i+d_j+s}\right]_{i,j=1}^2.
\]

The exact canonical overlap is

\[
\boxed{
\mathcal O
=
\operatorname{tr}(G_0^{-1}G_2G_4^{-1}G_2)
=
\frac{147}{100}.
}
\]

The cross-Dirichlet scalar is instead

\[
\boxed{
\Delta
=
\sum_{B_-(c)=0}\frac{B_+'(c)}{B_-'(c)}
=
\frac{49}{60}.
}
\]

Hence

\[
\frac{147}{100}\ne\frac{49}{60}.
\]

The true adverse charge is

\[
\boxed{
\|H_{B_+/B_-}\|_{\mathcal S_2}^2
=
2-\frac{147}{100}
=
\frac{53}{100},
}
\]

whereas the old phase-equality formula would give

\[
2-\frac{49}{60}=\frac{71}{60}.
\]

Likewise the outer Dirichlet difference is

\[
\|B_+-B_-\|_{\mathcal D}^2
=
4-2\frac{49}{60}
=
\frac{71}{30},
\]

which strictly overpays the sum of the two oriented Hankel charges.

## 4. Correct implication

The corrected sibling theorem proves

\[
\operatorname{Re}\Delta
\le |\Delta|
\le \mathcal O,
\]

and therefore

\[
\|H_{B_+/B_-}\|_{\mathcal S_2}^2
\le
\frac1{4\pi}
\int\beta_-'(t)|1-B_+(t)/B_-(t)|^2dt.
\]

Thus the positive denominator phase mean remains a valid sufficient majorant,
but it is generally stronger than the canonical-correlation gate.

## 5. Binding consequence for this branch

Any exact closure of `D0PHASE105650` must use the positive model overlap

\[
\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}})
\]

or an inequality that controls it.  It may not replace that overlap by the
cross-Dirichlet scalar.  The corrected Cauchy-translation trace inequality is
recorded in `T-105655`.

RH remains unproved.
