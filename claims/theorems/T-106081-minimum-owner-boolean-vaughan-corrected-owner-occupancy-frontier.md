# T-106081 — Minimum-owner Boolean Vaughan corrected owner-occupancy frontier

Claim ID: `T-106081`  
Programme aliases: `LFAM1.MINIMUM_OWNER_SELECTOR_MOMENT`, `STRESS.LONG_CORE_OWNER_OCCUPANCY`, `LFAM2.BOOLEAN_KUMMER_ASSEMBLY_FRONTIER`  
Status: **EXACT CORRECTED REDUCTION; SOURCE-TIED OWNER ASSEMBLY OPEN**  
Created: 2026-08-25  
Depends on: `L-106080--L-106081`; `R-106080`; parent `L-102880`, `L-102887--L-102888`; `T-106030`; `T-106071`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The self-reconstruction of `T-106080` retains the new Boolean source
coordinate and the minimum-owner geometry, but rejects the attempted direct
application of `L-102883`.

This theorem records the exact conclusion-facing object which remains.

## 1. Retained source reduction

For each deterministic owner pair

\[
P_i=\lambda_i\Lambda_i,
\qquad
\lambda_i<\Lambda_i,
\]

the completed balanced source consists of atoms

\[
n_i=P_i a_i^2,
\qquad
\mu^2(a_i)=1,
\qquad
(a_i,P_i)=1,
\]

with coefficient

\[
\alpha_i
=
\frac{\gamma_i}{a_i\sqrt{\lambda_i\Lambda_i}}.
\]

The Boolean balanced coefficient forces at least two distinct core primes.
The minimum-owner rule gives

\[
\lambda_i^2\le a_i.
\]

After the linear block projection

\[
B\le a_i<2B,
\qquad
L\le\lambda_i<2L,
\]

every nonempty block satisfies

\[
L^2<2B.
\]

The fixed-owner Boolean Type-I row is power-saving, and the parent terminal,
repeated-label, equal-product and finite-Euler rows remain closed.

## 2. Exact selector-tied phase packet

Let \(I_\ell\) denote the source atoms in the block whose distinguished owner
is \(\ell\), and put

\[
\beta_i=\ell\alpha_i
=
\frac{\gamma_i}{a_i}\sqrt{\frac{\ell}{\Lambda_i}}
\qquad(i\in I_\ell).
\]

For distinct phase owners \(\ell,\rho\), define

\[
\mathcal A_{\ell\to\rho;k}
=
\sum_{i\in I_\ell}
\beta_i e_\rho(k n_i)v_i,
\qquad 1\le k<\rho.
\tag{T-106081.1}
\]

The phase modulo \(\ell\) is constant on \(I_\ell\), because
\(\ell\mid n_i\). Expanding the two nonzero Ramanujan identities gives the
exact clean cross-owner Gram

\[
\boxed{
\mathcal G_{B,L}^{\rm clean}
=
\sum_{\substack{\ell,\rho\in\mathcal P_L\\\ell\ne\rho}}
\frac1{\ell\rho}
\sum_{h=1}^{\ell-1}
\sum_{k=1}^{\rho-1}
\left\langle
\mathcal A_{\ell\to\rho;k},
\mathcal A_{\rho\to\ell;h}
\right\rangle .
}
\tag{T-106081.2}
\]

All co-owner, Boolean representation, carrier, shell, marked-prime and overlap
labels are retained inside \(v_i\); none is declared orthogonal after physical
observation.

Cauchy reduces (T-106081.2) to the positive source-tied moment

\[
\boxed{
\begin{aligned}
\mathfrak P_{B,L}
={}&
\sum_{\substack{\ell,\rho\in\mathcal P_L\\\ell\ne\rho}}
\frac{\ell-1}{\ell\rho}
\sum_{k=1}^{\rho-1}
\left\|
\mathcal A_{\ell\to\rho;k}
\right\|^2.
\end{aligned}
}
\tag{T-106081.3}
\]

This is a mixed owner-squareclass phase moment: inside
\(\mathcal A_{\ell\to\rho;k}\),

\[
e_\rho(k n_i)
=
e_\rho(k\ell\Lambda_i a_i^2),
\]

and the varying co-owner \(\Lambda_i\) cannot be removed by a common
permutation of \(k\).

## 3. Correct open theorem

Define

```text
MOBOSM106081:
  after exact carrier, Wick, Boolean-Vaughan, owner, shell, marked-67,
  shared-owner and owner/core-overlap recombination, the dyadic sum of the
  selector-tied positive moments

      sum_(B,L: L^2<2B)  P_(B,L)

  is X^(o(1)), with every literal source weight used exactly once.
```

Equivalently, a reviewer may prove the source-tied bilinear form
\(\mathcal G_{B,L}^{\rm clean}\) directly without passing through Cauchy.

The relation \(L^2<2B\) is available throughout `MOBOSM106081`; hence the
remaining difficulty is no longer a distinguished-conductor/core mismatch.
It is coherent aggregation over the varying co-owner squareclasses and
source-tied owner selectors.

Under the Gauss--Mellin transform, the same target is a restricted long-core
version of the principal and nonprincipal owner-conductor moment in
`T-106030`. In the scale-matched residue coordinate, it is the long-core
owner-crowding component of `HQORO106071`.

## 4. Implication graph

Let `BSFTI106081` denote transport of the fixed-owner Boolean Type-I estimate
through the frozen parent owner ledger. The self-reconstruction finds no new
power loss in this transport, but keeps it explicit for independent review.

Then

\[
\boxed{
\mathrm{BSFTI}_{106081}
\wedge
\mathrm{MOBOSM}_{106081}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106081.4}
\]

The final two arrows are the frozen parent Volterra/Mellin consumer.

## 5. Current status

```text
Boolean Vaughan identity                         PROVED EXACT
balanced Boolean core has two primes             PROVED EXACT
squarefree fixed-owner Type-I                     PROVED POWER-SAVING
minimum-owner rule                                PROVED EXACT
lambda^2 <= a and L^2 < 2B                        PROVED EXACT
abstract same-family centered identity            PROVED EXACT
BSFTI106081 global parent-ledger transport        REVIEWABLE / NOT NEWLY CLOSED
MOBOSM106081 source-tied owner moment              OPEN / RH-BEARING
T-106080 direct L-102883 adapter                   RETRACTED BY R-106080
Riemann Hypothesis                                UNPROVED
```
