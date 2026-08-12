# T-91405 — Eta-paired dyadic pole-bridge optical completion would prove RH

Claim ID: `T-91405`  
Status: **FULL CONDITIONAL RH PROPOSAL / ONE-NODE SECTOR-CHANGING COMPLETION OPEN**  
Created: 2026-08-12  
Depends on: `L-91430`, `L-91431`, `R-91408`; `L-91313/L-91330` on PR #403  
RH status: **unproved**

## 1. Exact source factor at the hard pole node

For `0<omega<1/2`, put

\[
 s_0=1-\omega.
\]

The horizontal Jordan factor has the exact representation

\[
 \frac{\zeta(s-\omega)}{\zeta(s+\omega)}
 =\frac{\eta_D(s-\omega)}{\eta_D(s+\omega)}
  \frac{1-2^{1-s-\omega}}
       {1-2^{1-s+\omega}}.
 \tag{T-91405.1}

\]

At `s=s_0`, the paired eta ratio is finite and the dyadic numerator has one
simple zero with coefficient

\[
 \zeta(1-2\omega).
 \tag{T-91405.2}

\]

This cancels the one free gamma pole of `L-91330` with coefficient one.

## 2. Positive paired source

The real paired eta values are norms in

\[
 \ell^2(\mathbb N):
 \qquad
 \eta_D(\sigma)=\|e_\sigma\|^2.
 \tag{T-91405.3}

\]

The explicit Householder unitary of `L-91431` transports the normalized safe
state `e_1` to the hard state `e_(1-2omega)`.  Its bosonic second quantization
supplies a positive representation change on the distinguished one-vector
sector.

## 3. Eta-Paired Dyadic Optical Bridge (`EPDOB_omega`)

Construct a source-ordered map

\[
 \boxed{
 \mathfrak U_\omega:
 \mathcal H_\omega^{\rm eta,safe}
 \oplus\mathbb C_{\rm dyadic}
 \oplus\mathcal H_\omega^{\rm gamma,free}
 \longrightarrow
 \mathcal H_\omega^{\rm crit}
 \oplus\mathcal H_\omega^{\rm st}
 \oplus\mathcal H_\omega^{\rm hyp}
 \oplus\mathcal E_\omega
 }
 \tag{T-91405.4}

\]

on the one pole-aligned Cauchy/Green vector such that:

1. the paired eta component is transported by the explicit unitary of
   `L-91431`;
2. the dyadic factor supplies the simple zero in (T-91405.2);
3. the free gamma endpoint supplies the opposite pole residue of `L-91330`;
4. the zero and pole cancel before the Hilbert norm is taken;
5. the visible completed transfer is the horizontal Xi quotient;
6. the source norm is exhausted by the critical and deterministic stable
   outputs:
   \[
   \boxed{
   \|\Phi_\omega^{\rm source}\|^2
   =\|k_\omega^{\rm crit}\|^2
    +\|k_\omega^{\rm st}\|^2.
   }
   \tag{T-91405.5}
   \]

No same-node auxiliary or hyperbolic norm may remain.

## 4. Consequence

By the one-node detector of `L-91313`, (T-91405.5) gives

\[
 K_\omega^{\rm hyp}(\eta,\eta)=0
\]

and therefore

\[
 \xi(s)\ne0
 \qquad
 \left(\Re s>\frac12+\omega\right).
 \tag{T-91405.6}

\]

Proving `EPDOB_(omega_j)` for one fixed sequence `omega_j downarrow0` proves
RH.

## 5. Why this route is distinct

The route does not take a critical limit of the positive Euler Fock vacuum.
That limit is disjoint by `L-91327`.  Instead it reorganizes the arithmetic
before completion:

```text
positive local Euler product sector       abandoned at the hard node;
odd/even paired eta sector                 absolutely convergent;
dyadic zero                               explicit;
free gamma pole                           explicit;
sector change                             one positive Householder at one node.
```

The construction therefore attacks the exact global pole-zero cancellation
that finite Euler products miss.

## 6. Firewall and remaining joint

`R-91408` proves that the one-vector Householder does not intertwine the whole
carrier family.  `EPDOB` is deliberately a one-node theorem.  Its remaining
joint is the explicit multiplication/Mellin map from the paired eta and gamma
source vectors to the critical and stable model outputs, with the dyadic
zero-pole cancellation performed before norms.

An arbitrary unitary mapping one source vector to a target vector is not
sufficient: every factor in (T-91405.1) and the completed gamma residue must be
retained with coefficient one.

## 7. Exact boundary

```text
eta/dyadic factorization                          EXACT
pole-node dyadic zero coefficient                 EXACT
positive paired one-vector sector change          EXACT
full carrier use of one Householder               REFUTED
completed one-node eta/gamma optical map           OPEN / RH-BEARING
EPDOB for omega_j -> RH                           EXACT CONDITIONAL
Riemann Hypothesis                                UNPROVED
```