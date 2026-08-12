# T-91308 — One-Charge Infravacuum Positive-Energy Completion

Claim ID: `T-91308`  
Status: **CORRECTED FULL UNCONDITIONAL RH PROPOSAL — NOT A PROOF; ONE POSITIVE-ENERGY NEUTRALIZATION THEOREM OPEN**  
Created: 2026-08-12  
Supersedes as preferred endpoint: the overbroad sector-changing map in `T-91307`  
Depends on: `L-91331`–`L-91333`; PR #402; `L-91034/L-91038`  
RH status: **unproved**

## 1. Why the endpoint changes again

`T-91307` correctly required an entangled sector-changing completion. The new lemmas separate that demand into an exact part and the truly hard part.

1. `L-91331`: at each scale only finitely many prime harmonics change sector; on the preferred cofinal sequence there is exactly one.
2. `L-91332`: the complete orbit of disjoint sectors already has an unconditional direct-integral translation representation.
3. `L-91333`: the failure of positive energy is exactly the crossed-zero model-space projection.

Thus “construct a sector-changing Hilbert space” is too weak. The RH-bearing statement is **neutrality plus positive energy of one distinguished completed section**.

## 2. Preferred scales and source decomposition

Take

\[
\omega_j=2^{-j-3},
\qquad j=0,1,2,\ldots.
\tag{T-91308.1}
\]

Then \(0<\omega_j<1/4\), and the critical inverse has precisely one non-Fock harmonic:

\[
h_{p,\omega}
=
p^{-1/2+\omega}-p^{-1/2-\omega}.
\tag{T-91308.2}
\]

All harmonics of order \(k\ge2\) form a vacuum-sector remainder.

At scale \(\omega\), retain the explicit source components

```text
first-harmonic prime charge field h_(p,omega);
vacuum-sector higher-harmonic remainder;
positive forward Jordan Julia/Fock system;
free archimedean Hilbert remainder;
one physical Mellin pole bridge;
theta / coupled Brownian / Poisson / p=2 reserves.
```

Every item is defined without RH.

## 3. Orbit Hilbert space

Let

\[
\mathscr H_\omega^{\rm orb}
=
\int_\mathbb R^\oplus\mathcal H_t\,dt
\tag{T-91308.3}
\]

be the sector bundle of `L-91332`, with positive-energy subspace

\[
\mathscr H_{\omega,+}^{\rm orb}
=
H^2(\mathbb C_+;\mathcal H_0).
\tag{T-91308.4}
\]

The completed boundary scattering section is

\[
\mathbf s_\omega(t)
=
\Theta_\omega(t)
\frac{\Omega_t}{\frac12-it}.
\tag{T-91308.5}
\]

Let \(B_\omega\) be the crossed-zero Blaschke product and put

\[
\mathfrak A_\omega=B_\omega\Theta_\omega,
\]

the coprime pole-removed inner factor of `L-91034`.

The section belongs to the full orbit Hilbert space unconditionally. Its negative-energy norm is

\[
\boxed{
\|P_-\mathbf s_\omega\|^2
=
\|P_{K_{B_\omega}}(\mathfrak A_\omega r)\|^2,
\qquad
r(z)=\frac1{\frac12-iz}.
}
\tag{T-91308.6}
\]

## 4. One-Charge Infravacuum Positive-Energy Theorem

> **`OCIPE_omega`.**  
> Construct, from the declared prime, gamma/pole, theta, Brownian, Poisson, and local source data, a source-defined neutral section
> \[
> \Omega_\omega^{\rm comp}
> \in\mathscr H_\omega^{\rm orb}
> \tag{T-91308.7}
> \]
> with the following properties.
>
> 1. **Safe uniqueness.** On one safe open half-plane its scalar transfer is exactly
>    \[
>    \xi(\tfrac12-\omega-iz)/
>    \xi(\tfrac12+\omega-iz).
>    \]
> 2. **First-charge neutralization.** The non-square-summable \(k=1\) prime harmonic is paired with the completed pole/theta boundary source before Hilbert completion; all residual prime harmonics use the vacuum-sector remainder of `L-91331`.
> 3. **Cylinder compatibility.** Every finite-prime restriction agrees with the exact Julia scalar/detail nodes.
> 4. **No finite-cutoff fiction.** The completed neutralization is obtained by a declared finite-part or graph limit, not by the divergent finite Euler value at the pole bridge.
> 5. **Positive source form.** The graph norm is the sum of explicit theta, coupled \(S\)-\(\Delta\), Poisson, local \(p=2\), and vacuum-remainder squares.
> 6. **Positive-energy identity.**
>    \[
>    \boxed{
>    P_-\Omega_\omega^{\rm comp}=0.
>    }
>    \tag{T-91308.8}
>    \]
> 7. **Identification.** Under the canonical orbit trivialization,
>    \[
>    \Omega_\omega^{\rm comp}(t)
>    =
>    \Theta_\omega(t)r(t)\Omega_t.
>    \tag{T-91308.9}
>    \]
> 8. **Dyadic compatibility.** The construction intertwines the coefficient-one scale cocycle.

Condition (T-91308.8), not the existence of the orbit space, is the sole conclusion-producing statement.

By (T-91308.6), it is equivalently the explicit norm exhaustion

\[
\boxed{
P_{K_{B_\omega}}(\mathfrak A_\omega r)=0.
}
\tag{T-91308.10}
\]

The auxiliary positive source construction must prove this equality; defining an auxiliary vector from the unknown defect is forbidden.

## 5. Completion to RH

If `OCIPE_(omega_j)` holds for every \(j\), then

\[
\Theta_{\omega_j}r\in H^2(\mathbb C_+).
\]

Because \(r\) is outer and \(\Theta_{\omega_j}\) has unimodular boundary values,

\[
\Theta_{\omega_j}
\]

is meromorphic inner. Hence there is no zero in

\[
\Re s>\frac12+\omega_j.
\]

As \(\omega_j\downarrow0\), functional-equation symmetry gives RH.

## 6. Three constructive readings

### Canonical-system reading

The first charge is the singular endpoint coordinate of the integrated Marchenko chain. `OCIPE` is the assertion that the completed boundary condition selects the positive Weyl solution and leaves no crossed-zero model component.

### Lévy–Fock–Hardy reading

The higher harmonics are an ordinary Fock remainder. The first harmonic lives in an inequivalent coherent representation. The orbit direct integral supplies covariance, while the completed source form must select its positive-energy neutral section.

### Theta/Brownian DtN reading

The first harmonic and physical pole bridge form the boundary pair. The theta/Beta/Poisson/local bulk supplies a positive form. `OCIPE` is the exact Green boundary identity that makes the resulting Weyl section causal.

## 7. Exact proof boundary

```text
finite harmonic charge count                         EXACT
one-charge reduction on omega_j                      EXACT
vacuum-sector higher-harmonic remainder              EXACT
direct-integral translation representation           EXACT
negative energy = crossed-zero model port            EXACT
source-defined first-charge neutralization            OPEN
positive-energy identity                              OPEN / RH-BEARING
OCIPE on omega_j -> innerness -> RH                   PROPOSED COMPLETE
Riemann Hypothesis                                    UNPROVED
```
