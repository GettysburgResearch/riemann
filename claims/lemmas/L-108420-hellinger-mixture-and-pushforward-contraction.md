# L-108420 — Squared Hellinger debt contracts under physical pushforward and positive source gluing

Claim ID: `L-108420`  
Status: **PROVED EXACT FINITE MEASURE THEOREM**  
Created: 2026-08-31  
Depends on: none  
RH/GRH status: **not assumed**

For nonnegative finite measures `mu,nu` on a finite set, use the unnormalized
squared Hellinger distance

\[
H^2(\mu,\nu)
=
\sum_x
\left(\sqrt{\mu(x)}-\sqrt{\nu(x)}\right)^2.
\tag{L-108420.1}
\]

## 1. Positive mixture subadditivity

Let

\[
\mu=\sum_{a\in A}\mu_a,
\qquad
\nu=\sum_{a\in A}\nu_a
\]

with every summand nonnegative. Pointwise, Cauchy gives

\[
\sum_a\sqrt{\mu_a(x)\nu_a(x)}
\le
\sqrt{\mu(x)\nu(x)}.
\]

Therefore

\[
\boxed{
H^2\!\left(\sum_a\mu_a,\sum_a\nu_a\right)
\le
\sum_aH^2(\mu_a,\nu_a).
}
\tag{L-108420.2}
\]

No disjointness of the images is required.

## 2. Deterministic physical pushforward is contractive

Let `pi:Omega->S` be any map. Applying the same inequality on every fibre
`pi^{-1}(s)` gives

\[
\boxed{
H^2(\pi_*\mu,\pi_*\nu)
\le
H^2(\mu,\nu).
}
\tag{L-108420.3}
\]

Thus source-level occupancy comparison may be performed before owner/cofactor
residue collapse and before physical squareclass multiplication.

## 3. Weighted mixture form

Assume each pair has the same mass `N_a` and write

\[
H^2(\mu_a,\nu_a)
=N_a\eta_a,
\qquad
N=\sum_aN_a,
\qquad
w_a={N_a\over N}.
\]

Then

\[
\boxed{
{H^2(\mu,\nu)\over N}
\le
\sum_aw_a\eta_a.
}
\tag{L-108420.4}
\]

Combining with `L-108400`, the positive-trace payment of the complete mixture
is at most

\[
\boxed{
2N
\sqrt{\sum_aw_a\eta_a}.
}
\tag{L-108420.5}
\]

This is an RMS gluing law. It is stronger than paying
`sum_a 2 N_a sqrt(eta_a)` whenever the rectangle defects are uneven.

## 4. Source boundary

Equations (L-108420.2)--(L-108420.5) require nonnegative measures. They may be
applied to occupancy multiplicities and positive trace measures after the
source-authorized history grouping. They may not be applied directly to the
signed principal/Kummer current before its exact recombination.

## Scope

The theorem closes the abstract positive-measure gluing problem. It does not
estimate the one-sided arithmetic character energies of the source pieces.
