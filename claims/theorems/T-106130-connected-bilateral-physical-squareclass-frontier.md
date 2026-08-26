# T-106130 — Connected bilateral physical-squareclass frontier

Claim ID: `T-106130`  
Programme aliases: `LFAM1.CONNECTED_BILATERAL_REPAIR`, `LFAM2.KUMMER_MOBIUS_PRINCIPAL_EXTRACTION`, `STRESS.COPRIME_BOOLEAN_CONNECTED_TRACE`  
Status: **CONSOLIDATED MINIMAL PRINCIPAL FRONTIER; ONE CONNECTED OFF-ATOMIC ESTIMATE OPEN**  
Created: 2026-08-25  
Depends on: parent `T-102990`; retained `L-106120`; binding corrections `R-106122--R-106124`, `R-106131`; `L-106190`  
Parent scientific source: PR #719 head `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The bilateral Kummer construction correctly places both physical source sides
inside one two-modulus family before any square. The complete positive frame
is nevertheless too large at atomic scope: `R-106124` and binding `R-106131`
prove that every atom is repeated `(ell-1)(rho-1)` times.

The minimal repair is the exact connected Kummer--Möbius combination. It
cancels that family dimension before estimation and returns the principal
physical member with coefficient one.

## 1. Literal bilateral fibres

After the inherited common-square extraction and all closed source strata, a
live fibre has

\[
 N=Pg^2c^2,
 \qquad M=Qg^2d^2,
 \qquad c,d>1,
 \qquad (c,d)=1,
\]

with canonical phase primes

\[
 \ell=P^-(c),
 \qquad \rho=P^-(d),
 \qquad \ell\ne\rho.
\]

Fix all linear source labels other than the complete atoms in this fibre:
common core, least primes, owner quadratic classes, shell, carrier,
marked-prime, Boolean representation and renewal data, and the Mellin
parameter `t`.

Write the remaining atom amplitudes as

\[
 z_\omega(t)={\gamma_\omega(t)\over g^2cd\sqrt{PQ}},
 \qquad |\gamma_\omega(t)|\le X^{o(1)}.
\tag{T-106130.1}
\]

Attach the physical Kummer coordinates

\[
 x_\omega=Qd^2\pmod\ell,
 \qquad y_\omega=Pc^2\pmod\rho.
\tag{T-106130.2}
\]

No owner-only replacement is made.

## 2. Principal and collision ledgers

For one fibre put

\[
 T_f(t)=\left|\sum_\omega z_\omega(t)\right|^2,
 \qquad D_f(t)=\sum_\omega|z_\omega(t)|^2.
\]

Define

\[
\begin{aligned}
 C_{\ell,f}(t)&=\sum_{x_\omega=x_{\omega'}}
 z_\omega\overline{z_{\omega'}},\\
 C_{\rho,f}(t)&=\sum_{y_\omega=y_{\omega'}}
 z_\omega\overline{z_{\omega'}},\\
 C_{\ell\rho,f}(t)&=\sum_{\substack{x_\omega=x_{\omega'}\\
 y_\omega=y_{\omega'}}}z_\omega\overline{z_{\omega'}}.
\end{aligned}
\tag{T-106130.3}
\]

Let `E_(11,f)` be the complete two-nonzero-phase energy. `L-106190` gives
coefficientwise

\[
\boxed{
 T_f=E_{11,f}+\ell C_{\ell,f}+\rho C_{\rho,f}
 -\ell\rho C_{\ell\rho,f}.
}
\tag{T-106130.4}
\]

The complete even-character tensor frame is exactly `E_(11,f)`. The other
three terms are the one-coordinate and joint physical-squareclass collision
ledgers. Their signed inclusion--exclusion is mandatory.

## 3. Atomic-free connected current

Put

\[
\begin{aligned}
 E_{11,f}^{\circ}&=E_{11,f}-(\ell-1)(\rho-1)D_f,\\
 C_{\ell,f}^{\circ}&=C_{\ell,f}-D_f,\\
 C_{\rho,f}^{\circ}&=C_{\rho,f}-D_f,\\
 C_{\ell\rho,f}^{\circ}&=C_{\ell\rho,f}-D_f.
\end{aligned}
\]

Then

\[
\boxed{
 T_f-D_f=E_{11,f}^{\circ}+\ell C_{\ell,f}^{\circ}
 +\rho C_{\rho,f}^{\circ}-\ell\rho C_{\ell\rho,f}^{\circ}.
}
\tag{T-106130.5}
\]

Every atomic coefficient has cancelled. This connected current retains the
cancellations between principal, mixed and double collision channels which the
positive `BTPP/BTPN/BTNN` split discarded.

## 4. Minimal source-dual principal moment

Define

\[
\boxed{
 \mathfrak M_{\rm CK}(Y)
 ={1\over2\pi}\sum_f g_f^2\ell_f\rho_f
 \int_{\mathbb R}|\widehat\kappa(t)|^2T_f(t)\,dt.
}
\tag{T-106130.6}
\]

Unlike the full positive tensor frame, this moment contains each principal
source atom once. The reciprocal source mass satisfies

\[
 \sum_g{1\over g^2}\sum_{\ell\ne\rho}{1\over\ell\rho}
 \ll(\log\log(3Y))^2.
\]

The retained source-dual Cauchy/Mellin--Plancherel argument gives

\[
\boxed{
 \|\mathcal C_{\rm BCI}\|_{L^2(dX/X)}^2
 \ll(\log\log(3Y))^{O(1)}\mathfrak M_{\rm CK}(Y).
}
\tag{T-106130.7}
\]

## 5. The genuine atomic diagonal is paid

The atomic part of (T-106130.6) is `g^2 ell rho D_f`. Using
(T-106130.1), `ell<=c` and `rho<=d`, its summand is

\[
 \ll X^{o(1)}{\ell\rho\over g^2c^2d^2PQ}
 \le X^{o(1)}{1\over g^2cdPQ}.
\]

The source sums, shell multiplicities and compact Mellin norm are
polylogarithmic or summable. Hence

\[
\boxed{
 \mathfrak M_{\rm CK}^{\rm atomic}(Y)=Y^{o(1)}.
}
\tag{T-106130.8}
\]

## 6. Exact remaining theorem

Define

```text
CBKM106130:
  after all inherited carrier, Boolean, equal-product, repeated-label,
  shared-incidence and common-factor recombinations, the positive part of the
  complete source-dual connected off-atomic ledger

    sum_f g_f^2 * ell_f * rho_f * integral |kappa_hat(t)|^2
      [ E_11,f^circ
        + ell_f C_ell,f^circ
        + rho_f C_rho,f^circ
        - ell_f rho_f C_ellrho,f^circ ] dt

  is Y^(o(1)).
```

Because the bracket equals `T_f-D_f`, (T-106130.8) gives

\[
\boxed{
 \mathrm{CBKM}_{106130}
 \Longrightarrow\mathfrak M_{\rm CK}(Y)=Y^{o(1)}
 \Longrightarrow\mathrm{BCI}_{102990}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-106130.9}
\]

`CBKM106130` remains open.

## 7. Relation to the other live repairs

This theorem is the least-assumptive principal frontier:

```text
T-106130 / CBKM106130:
  estimate the minimal connected principal current directly.

T-106140 / WCADD106140 AND WCKUM106140:
  retain the complete family and recover the principal current as the
  difference of two separately normal-ordered signed traces.

T-106150 / WKSFSC106150, SFSC106150, REFSIG106150:
  compress the canonical source to one same-half-source Wick/ordinary
  reflection current and attack its one-sided mass.
```

The exact identity of `T-106140` and its paid principal diagonal imply

\[
 \mathrm{WCADD}_{106140}\wedge\mathrm{WCKUM}_{106140}
 \Longrightarrow\mathfrak M_{\rm CK}(Y)=Y^{o(1)},
\tag{T-106130.10}
\]

because its nonnegative principal moment carries the extra factors
`c_ell c_rho>1` and therefore dominates (T-106130.6). This proves the
principal conclusion; it does not assert that either family gate separately
proves `CBKM106130`.

`T-106150` supplies an independent source-faithful implication to
`BCI102990`. No equivalence between its gates and `CBKM106130` is claimed. All
remain open.

## 8. Why this is a real repair

The former three-gate positive programme required separate upper bounds for
principal--principal, mixed and double-nonprincipal moments. Its atomic
baseline already had power-sized frame multiplicity.

The connected frontier instead permits

\[
 (\ell-1)(\rho-1)+\ell+\rho-\ell\rho=1
\]

before any estimate. A valid large sieve, trace formula or geometric argument
may use cancellation between the one-coordinate and joint collision strata;
it must not replace them by four positive absolute values.

## 9. Function-field export target

Define

```text
FFCK106130:
  construct the connected trace function attached to the two Kummer maps

      (P,c) -> P*c^2,
      (Q,d) -> Q*d^2,

  apply the inclusion--exclusion of L-106190 before taking conductor-family
  absolute values; remove diagonal and geometrically constant constituents;
  prove square-root cancellation for the connected off-atomic trace; identify
  the number-field hybrid large-sieve or relative trace theorem reproducing
  that cancellation.
```

The function-field prime-shell theorem `L-106130` is a local input. The new
object is its connected two-conductor assembly.

## Current boundary

```text
bilateral source partition and double phases          PROVED EXACT
physical-squareclass Kummer coordinates               PROVED EXACT
complete positive tensor frame                        PROVED EXACT BUT OVERSTRONG
paid atomic diagonal of complete frame                RETRACTED
connected Kummer--Möbius inversion L-106190           PROVED EXACT
minimal principal source-dual moment                  PROVED EXACT
atomic diagonal of minimal moment                     PROVED SUBPOWER
CBKM106130 connected off-atomic estimate              OPEN / RH-BEARING
WCADD106140 / WCKUM106140                             OPEN / RH-BEARING
WKSFSC106150 / SFSC106150 / REFSIG106150              OPEN / RH-BEARING
BCI102990                                              OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
