# L-102724 — The quadratic boundary is an exact compact activation/current bridge

Claim ID: `L-102724`  
Status: **PROVED EXACT DISTRIBUTIONAL COMPOSITION**  
Created: 2026-08-22  
Depends on: `L-102722--L-102723`; PR #697 `L-101101`  
RH status: **not assumed**

Retain the tangent source `Sigma_tau` of `L-102722`. Put

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
W_3(y)=16y\mathbf1_{y\ge1}.
\]

Define the tangent fields

\[
Q_\tau(X)=
\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}T(X/n)^2,
\]

\[
H_\tau(X)=
\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}T(X/n),
\]

\[
Q_{\tau,3}(X)=
\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}W_3(X/n),
\]

and the activation measure

\[
\mathcal A_\tau
=
\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}
\delta_{\log n}.
\]

All identities below are logarithmic distribution identities.

## 1. Two exact boundary equations

The active SHARP carrier satisfies

\[
\boxed{(D-1)T^2=\delta_0+3T.}
\tag{L-102724.1}
\]

Indeed `T^2` jumps from zero to one at the activation point and, away from the jump,

\[
(D-1)T^2=3T.
\]

The boundary shift `z=3` gives `W_3(y)=16y1_(y>=1)`, so

\[
\boxed{(D-1)W_3=16\delta_0.}
\tag{L-102724.2}
\]

After source translation and finite Fubini,

\[
\boxed{(D-1)Q_\tau=\mathcal A_\tau+3H_\tau,}
\tag{L-102724.3}
\]

\[
\boxed{(D-1)Q_{\tau,3}=16\mathcal A_\tau.}
\tag{L-102724.4}
\]

Subtracting gives

\[
\boxed{
(D-1)(Q_{\tau,3}-Q_\tau)
=3(5\mathcal A_\tau-H_\tau).
}
\tag{L-102724.5}
\]

Thus the fixed five-to-one activation/current combination is not an auxiliary guess: it is the exact boundary divergence of two members of the monotone shifted-quadratic disk.

## 2. Compact dyadic projection

Let

\[
P_2=(I-\sqrt2S_2)(I-S_2)^2,
\qquad
(Jf)(X)=\int_1^Xf(t)\frac{dt}{t}.
\]

Write

\[
a_\tau=J\mathcal A_\tau,
\qquad
G_\tau=JP_2H_\tau.
\]

The operators `J`, `P_2`, `D`, and all multiplicative source shifts commute on the zero-extended finite-horizon domain. Applying `JP_2` to (L-102724.5) yields

\[
\boxed{
JP_2(D-1)(Q_{\tau,3}-Q_\tau)
=3\bigl(5P_2a_\tau-G_\tau\bigr).
}
\tag{L-102724.6}
\]

The right side is exactly one compact activation/wavelet current on the fixed source. It retains all moving-completion atoms because they are part of `Sigma_tau`.

## 3. Relation to the S-lemma row

At each unfiltered scale, `L-102723` gives the fixed inequality

\[
5a_\tau(X)-H_\tau(X)
\ge-\frac54Q_\tau(X).
\tag{L-102724.7}
\]

Equation (L-102724.6) identifies the exact compact projection of the same coordinate. No inequality is asserted after `P_2`: the filter is signed and is not cone preserving. The missing theorem is therefore not another source identity, but preservation of a subpower one-sided projection after exact carrier recombination and physical collapse.