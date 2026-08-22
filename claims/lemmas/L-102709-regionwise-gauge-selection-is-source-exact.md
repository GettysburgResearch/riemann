# L-102709 — Regionwise homotopy selection is source-exact

Claim ID: `L-102709`  
Status: **PROVED EXACT COMPOSITION THEOREM**  
Created: 2026-08-22  
Depends on: `L-102706--L-102708`; PR #715 `L-102503`  
RH status: **not assumed**

Let the native-completion defect have an exact, one-use source partition

\[
E-C=\sum_{\mathcal R}P_{\mathcal R}(E-C),
\qquad
\sum_{\mathcal R}P_{\mathcal R}=I,
\]

where every `P_R` is fixed independently of the homotopy parameter and retains
its source provenance.

Examples are the source-owned regions

```text
small/squared primes;
mesoscopic Dickman corridor;
balanced coprime/Vaughan region;
activation-transfer atoms;
finite terminal packet.
```

Let `E_tau` be the Euler path of `L-102706` and `H_tau` the half-divisor path.
Both satisfy

\[
E_0=H_0=C,
\qquad
E_1=H_1=E.
\]

For each region choose independently a gauge

\[
\gamma(\mathcal R)\in\{\mathrm{Euler},\mathrm{half\!\!-divisor}\}.
\]

Then the regional current

\[
J_{\mathcal R}
=\int_0^1
P_{\mathcal R}\frac d{d\tau}
\Gamma^{\gamma(\mathcal R)}_\tau\,d\tau
\]

satisfies

\[
\boxed{J_{\mathcal R}=P_{\mathcal R}(E-C).}
\tag{L-102709.1}
\]

Consequently

\[
\boxed{
E-C=\sum_{\mathcal R}J_{\mathcal R}
}
\tag{L-102709.2}
\]

exactly, even though different regions use different homotopies.

## Intermediate switching

A region may also switch gauges at an intermediate parameter `tau_0`.  The
resulting boundary mismatch is

\[
P_{\mathcal R}(H_{\tau_0}-E_{\tau_0}).
\]

By `L-102706`, this mismatch is obtained from the Euler packet by a multiplier
whose local expansion starts at `p^(-1)`, and hence has only polylogarithmic
physical cost on every fixed horizon.

## Programme allocation

The exact admissible allocation is therefore:

```text
Euler gauge:
  moving completion atoms;
  greatest-owner cancellation;
  squared core and higher prime powers;
  activation and finite-boundary ledgers.

Half-divisor gauge:
  root-free tangent;
  ratio-four kernel factorization;
  same-product and same-owner Hilbert estimates;
  balanced distinct-product occupancy.
```

This theorem closes the source/interface question.  It does not prove the
remaining balanced cross-owner arithmetic estimate.