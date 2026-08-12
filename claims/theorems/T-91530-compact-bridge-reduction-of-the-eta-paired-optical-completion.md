# T-91530 — Compact-bridge reduction of the eta-paired optical completion

Claim ID: `T-91530`  
Status: **FULL CONDITIONAL RH PROPOSAL / ETA-TAIL–BETA COMPLETION OPEN**  
Created: 2026-08-12  
Depends on: `L-91530/L-91531`, `R-91530`; `T-91405`  
RH status: **unproved**

## 1. Completed factorization after pole removal

For `0<omega<1/2`, the horizontal completed quotient is

\[
\begin{aligned}
 \frac{\xi(s-\omega)}{\xi(s+\omega)}
 ={}&
 \frac{\eta_D(s-\omega)}{\eta_D(s+\omega)}
 \frac{F_L(s-s_0)}{F_L(s-s_1)}\\
 &\times
 \pi^\omega\frac{s-\omega}{s+\omega}
 \frac{\Gamma((s-\omega)/2)}
      {\Gamma((s+\omega)/2)}.
\end{aligned}
\tag{T-91530.1}

\]

The middle factor is now an explicit positive finite-interval channel with a
full-carrier covariant unitary. The old free pole and dyadic zero no longer
appear as separate source coordinates.

## 2. Closed bridge output

Let

\[
 \mathcal H_\omega^{\rm bridge}
 =L^2([0,\log2],\mu_q)
\]

with the appropriate endpoint tilt. `L-91531` supplies an exact unitary

\[
 \mathcal U_{\omega,q}^{\rm bridge}
\]

that preserves:

```text
all carrier Grams;
all physical delay phases;
both Hardy orientations;
coherent/Fock inner products;
the two removable endpoint values.
```

Thus the bridge component of the parent `EPDOB_omega` map is complete before
any norm is taken.

## 3. Reduced Eta–Beta Optical Completion (`EBOC_omega`)

Construct a source-ordered map

\[
\boxed{
 \mathfrak V_\omega:
 \mathcal H_\omega^{\rm eta,paired}
 \widehat\otimes
 \mathcal H_\omega^{\rm beta/gamma}
 \longrightarrow
 \mathcal H_\omega^{\rm crit}
 \oplus
 \mathcal H_\omega^{\rm st}
 \oplus
 \mathcal H_\omega^{\rm hyp}
 \oplus
 \mathcal E_\omega
}
\tag{T-91530.2}

\]

at the one pole-aligned Cauchy/Green vector such that:

1. its paired eta restriction agrees with the explicit one-vector sector
   change of `L-91431`;
2. the unbounded eta multiplication is coupled to the residual beta/gamma
   factor in (T-91530.1) before the graph norm is taken;
3. the compact bridge unitary is tensored in with coefficient one;
4. the visible transfer is exactly the completed Xi quotient;
5. the source norm is exhausted by the critical and deterministic stable
   outputs:
   \[
   \boxed{
   \|\Phi_\omega^{\rm source}\|^2
   =\|k_\omega^{\rm crit}\|^2
    +\|k_\omega^{\rm st}\|^2.
   }
   \tag{T-91530.3}
   \]

This reduced theorem is `EBOC_omega`.

## 4. Consequence

`EBOC_omega`, together with the already explicit bridge unitary, gives the
parent `EPDOB_omega`. Hence the one-node hyperbolic port vanishes and

\[
 \xi(s)\ne0
 \qquad(\Re s>1/2+\omega).
\]

Proving `EBOC_(omega_j)` for one sequence `omega_j downarrow0` proves RH.

## 5. What has been removed from the open theorem

The following are no longer open:

```text
coefficient of the global pole-zero cancellation;
regularization of the free non-Hilbert pole tail;
carrier covariance of the dyadic bridge;
delay and reflection covariance of that bridge;
positive Hilbert realization of the bridge.
```

The sole representation obstacle is the noncompact paired eta tail and its
entanglement with the residual beta/gamma source.

## 6. Preferred next construction

The Mellin representation

\[
 \eta_D(s)/s=\int_Ee^{-sy}dy
\]

and the beta integral for the gamma ratio place both surviving factors in
explicit positive integral spaces. The preferred attack is a closed graph map
on their product variable in which the eta growth `e^(omega y)` is absorbed by
the beta/gamma decay before integration.

A same-space bounded eta multiplier is impossible by `R-91530`; the product
source or one-node graph norm is essential.

## 7. Exact boundary

```text
dyadic/gamma pole cancellation                    EXACT COMPACT
bridge full-carrier unitary                       EXACT
one-vector paired eta sector change               EXACT
same-space full eta carrier map                   REFUTED
eta-tail–beta/gamma graph completion              OPEN / RH-BEARING
EBOC -> EPDOB -> zero-free half-plane             EXACT CONDITIONAL
Riemann Hypothesis                                UNPROVED
```
