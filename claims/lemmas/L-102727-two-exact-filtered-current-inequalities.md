# L-102727 — Two exact SHARP inequalities survive the signed compact filter

Claim ID: `L-102727`  
Status: **PROVED EXACT FILTERED-CURRENT THEOREM**  
Created: 2026-08-22  
Depends on: `L-102722`, `L-102724--L-102726`  
RH status: **not assumed**

Retain the completion tangent source `Sigma_tau`.  Define

\[
Q_{\tau,z}(X)
=
\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}
W_z(X/n),
\]

and write

\[
Q_\tau=Q_{\tau,0},
\qquad
H_\tau=
\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}T(X/n),
\]

\[
a_\tau=J\mathcal A_\tau,
\qquad
G_\tau=JP_2H_\tau.
\]

## 1. Tangent positivity after the signed filter

By `L-102722`,

\[
\Sigma_\tau
=
\sum_\ell r_\ell U_\ell A_{1-\tau,\ne\ell}E,
\]

which is a positive linear combination of multiplicative shifts of the native
source `E`.  `L-102726` proves that the native observations of `K_-1` and
`K_-1/2` are nonnegative at every scale.  Therefore

\[
\boxed{
P_2Q_{\tau,-1}(X)\ge0,
\qquad
P_2Q_{\tau,-1/2}(X)\ge0.
}
\tag{L-102727.1}
\]

Since `J` is positive,

\[
JP_2Q_{\tau,-1}\ge0,
\qquad
JP_2Q_{\tau,-1/2}\ge0.
\tag{L-102727.2}
\]

This is the first nontrivial cone transport through the signed compact filter.
It uses the literal native prime budget; it is not entrywise preservation of an
arbitrary positive function.

## 2. Exact current identities

For a real shift `z`, linearity gives

\[
JP_2Q_{\tau,z}
=
JP_2Q_\tau+2zG_\tau+z^2P_2a_\tau.
\tag{L-102727.3}
\]

The boundary identity of `L-102724` is

\[
P_2Q_\tau-JP_2Q_\tau
=P_2a_\tau+3G_\tau.
\tag{L-102727.4}
\]

Eliminating `JP_2Q_tau` gives

\[
\boxed{
JP_2Q_{\tau,z}
=
P_2Q_\tau+(2z-3)G_\tau+(z^2-1)P_2a_\tau.
}
\tag{L-102727.5}
\]

At the activation-zero ray `z=-1`, (L-102727.2) becomes

\[
\boxed{
P_2Q_\tau-5G_\tau\ge0.
}
\tag{L-102727.6}
\]

At `z=-1/2`, it becomes

\[
\boxed{
P_2Q_\tau-4G_\tau-\frac34P_2a_\tau\ge0.
}
\tag{L-102727.7}
\]

These are exact inequalities for the same tangent source and the same signed
compact projection.

## 3. Meaning

The general filter firewall `R-102720` remains valid.  The new theorem does
not assert full-disk cone preservation.  It proves that two specially chosen
SHARP rays survive because their filtered carriers have globally subcritical
native prime budgets.

The inequalities supply a genuine one-sided filtered control of the critical
wavelet current by the quadratic and activation channels.  A lower bound in the
opposite direction—or an exact carrier-recombined use of the single S-lemma
slack—is still required for `FLC102730`.