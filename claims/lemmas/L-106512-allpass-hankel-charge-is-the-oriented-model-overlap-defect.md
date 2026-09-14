# L-106512 — All-pass Hankel charge is the oriented model-overlap defect

Claim ID: `L-106512`  
Status: **PROVED EXACT FOR FINITE REDUCED INNER QUOTIENTS**  
Created: 2026-08-25  
Depends on: `L-106505`; finite inner Toeplitz identities  
RH status: **not assumed**

Let

\[
U=\omega B_+\overline{B_-}
\]

be reduced, with

\[
P_+=P_{K_{B_+}},
\qquad
P_-=P_{K_{B_-}},
\qquad
m_\pm=\deg B_\pm.
\]

## 1. Exact oriented charge

Analyticity gives

\[
H_U=\omega H_{\overline{B_-}}T_{B_+},
\qquad
H_{\overline{B_-}}^*H_{\overline{B_-}}=P_-.
\]

Since

\[
T_{B_+}T_{B_+}^*=I-P_+,
\]

cyclicity yields

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=\operatorname{tr}\left(P_-(I-P_+)\right)
=m_- -\operatorname{tr}(P_-P_+).
}
\tag{L-106512.1}

Thus every numerator model direction overlapping the denominator bad model is
removed before the adverse charge is counted.  Pure favorable inner degree is
free, as it must be.

The Fredholm index satisfies

\[
-\operatorname{wind}U=m_--m_+.
\]

Because `tr(P_-P_+)<=m_+`, (L-106512.1) recovers

\[
\boxed{
-\operatorname{wind}U
\le\|H_U\|_{\mathcal S_2}^2.
}
\tag{L-106512.2)

The excess over the index is exactly the failure of the two model spaces to
align within their matched dimensions.

## 2. Explicit Cauchy matrix

Let `E_-,E_+` synthesize normalized reproducing kernels at the upper zeros of
`B_-,B_+`, and put

\[
G_-=E_-^*E_-,
\qquad
G_+=E_+^*E_+,
\qquad
C=E_-^*E_+.
\]

Then

\[
\boxed{
\operatorname{tr}(P_-P_+)
=\left\|G_-^{-1/2}CG_+^{-1/2}\right\|_{\mathrm F}^2.
}
\tag{L-106512.3)

Hence

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=m_-
-\left\|G_-^{-1/2}CG_+^{-1/2}\right\|_{\mathrm F}^2.
}
\tag{L-106512.4)

The confluent statement uses derivative kernels and the same formula.

## 3. Relation to outer Dirichlet domination

`L-106507` gives the valid but stronger estimate

\[
\|H_U\|_{\mathcal S_2}^2
\le\|B_+-B_-\|_{\mathcal D}^2.
\]

Equation (L-106512.1) is the sharp oriented quantity.  It should be preferred
whenever favorable numerator degree is macroscopically large.
