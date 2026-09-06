# T-91307 — Entangled Pole-Bridge Sector-Changing Completion: corrected full RH proposal after the Julia–Wick firewalls

Claim ID: `T-91307`  
Status: **FULL UNCONDITIONAL RH PROPOSAL — NOT A PROOF; ONE ENTANGLED SECTOR-CHANGING OPTICAL THEOREM OPEN**  
Created: 2026-08-12  
Depends on: `L-91327`–`L-91330`, `R-91308/R-91309`, corrected `T-91303`, PR #402  
RH status: **unproved**

## 1. Corrections absorbed

The following facts are now exact.

1. The global Jordan inverse exists canonically as an algebraic cylinder distribution.
2. It is a Hilbert vector only for \(\Re s>1/2+\omega\), and its critical product representation is disjoint from the safe vacuum.
3. Physical prime-log translations are not implemented in the critical inverse product sector.
4. The inverse channel sends the interacting Suzuki Green vector to the free endpoint Green vector.
5. The free endpoint has one explicit unstable mode
   \[
   \frac{C_{0,\omega}}{1-\omega}e^{(1/2-\omega)t}
   \]
   for \(0<\omega\le1/2\).
6. The full forward Jordan factor cancels that mode by its exact zero at \(s=1-\omega\).
7. Finite Euler products amplify the pole bridge and do not approximate that analytic zero.
8. The unrenormalized all-generation pole-node source norm does not match the model-space source norm.

Thus the wave operator of `T-91305/T-91306` cannot be a bounded same-vacuum Fock limit, and the one-node source vector cannot be used with its old normalization.

## 2. Exact source objects

Fix \(0<\omega<1/2\).

### Prime cylinder source

Let

\[
 \mathfrak d_\omega^{\rm cyl}
 \in\mathcal P_{\rm cyl}'
 \tag{T-91307.1}
\]

be the exact all-detail inverse distribution of `L-91328`, and let \(\mathfrak c_\omega\) denote the positive forward Jordan product system with coefficients

\[
 c_\omega(n)=\frac{J_{2\omega}(n)}{n^\omega}>0.
 \tag{T-91307.2}
\]

### Archimedean endpoint

Let

\[
 F_\omega(y)=g_\omega(1/y),
 \qquad
 F_\omega^\circ(y)=F_\omega(y)-C_{0,\omega}y^{1-\omega},
 \tag{T-91307.3}
\]

and let \(b_\omega\) be the one-dimensional pole-bridge coordinate carrying

\[
 C_{0,\omega}y^{1-\omega}.
 \tag{T-91307.4}
\]

The pole-subtracted free Green vector is unconditionally in \(L^2\).

### Positive reserves

Retain the source-defined positive channels

\[
 \mathcal E_\omega
 =\mathcal E_{\theta,\omega}
 \oplus\mathcal E_{\beta,S\Delta,\omega}
 \oplus\mathcal E_{{\rm Pois},\omega}
 \oplus\mathcal E_{2,\omega}.
 \tag{T-91307.5}
\]

## 3. The visible target

Let

\[
 A_\omega(x)=\int_1^xh_\omega(y)dy
 \tag{T-91307.6}
\]

and

\[
 f_\omega(t)=e^{-t/2}A_\omega(e^t)\mathbf1_{t\ge0}.
 \tag{T-91307.7}
\]

Then

\[
 \widehat f_\omega(z)
 =\frac{\Theta_\omega(z)}{\frac12-iz},
 \qquad
 \Theta_\omega(z)
 =\frac{\xi(\frac12-\omega-iz)}
        {\xi(\frac12+\omega-iz)}.
 \tag{T-91307.8}
\]

## 4. Entangled Pole-Bridge Optical Theorem

> **`EPBOT_omega`.**  
> Construct a nuclear/rigged source core \(\mathscr S_\omega\), containing the prime cylinder algebra, the positive forward Jordan product system, the pole bridge, the pole-subtracted theta endpoint, and the coupled Brownian/local reserves, together with a closable sector-changing map
> \[
> \boxed{
> \mathscr U_\omega:
> \mathcal D_\omega\subset\mathscr S_\omega'
> \longrightarrow
> L^2(0,\infty)\oplus\mathcal E_\omega
> }
> \tag{T-91307.9}
> \]
> satisfying all of the following.
>
> 1. **Cylinder exactness.** On every finite prime cylinder it agrees with the Julia scalar/detail identities of `L-91323`–`L-91326`.
> 2. **Correct orientation.** The forward Jordan scalar channel acts before the all-detail inverse is read; deconvolution of the interacting vector returns the free endpoint as in `L-91329`.
> 3. **Pole-bridge cancellation.** The prime and archimedean amplitudes are mixed before taking norms, and the visible residue at \(s=1-\omega\) vanishes with coefficient one, reproducing
>    \[
>    C_\omega(s)G_\omega(s)
>    =\xi(s-\omega)/\xi(s+\omega).
>    \]
> 4. **No same-sector limit.** The construction is an unbounded sector-changing closure; it does not identify the critical inverse product with the safe Fock vacuum.
> 5. **Visible output.** The distinguished completed source distribution is sent to
>    \[
>    f_\omega\oplus q_\omega,
>    \qquad q_\omega\in\mathcal E_\omega.
>    \]
> 6. **Positive optical identity.** The graph form is positive and gives
>    \[
>    \boxed{
>    \|\Omega_\omega\|_{\rm ren}^2
>    =\|f_\omega\|_2^2+\|q_\omega\|^2<\infty.
>    }
>    \tag{T-91307.10}
>    \]
> 7. **Safe uniqueness.** On a nonempty safe half-plane the scalar transfer equals the completed Xi quotient, not merely its zeta factor or its boundary modulus.
> 8. **Dyadic compatibility.** The map intertwines the coefficient-one two-section cocycle.
> 9. **Translation covariance after completion.** The physical log-translation group acts strongly continuously on the Hardy output; no source-side product implementation is assumed.
> 10. **Tail closure.** Finite prime/cylinder and finite log-height cores are graph-norm dense, with an explicit cutoff-uniform bound.

The phrase *entangled before taking norms* is load-bearing. A direct sum of independently completed prime and archimedean channels does not satisfy `EPBOT_omega`.

## 5. Why `EPBOT_omega` proves the hard estimate

The optical identity gives

\[
 f_\omega\in L^2(0,\infty).
 \tag{T-91307.11}
\]

The factor \((1/2-iz)^{-1}\) is outer and \(|\Theta_\omega|=1\) on the real boundary. The one-vector theorem of PR #402 therefore yields

\[
 \Theta_\omega\text{ meromorphic inner in }\mathbb C_+.
 \tag{T-91307.12}
\]

Equivalently, the factor-four renewal energy is finite and \(\xi(s)\) has no zero in

\[
 \Re s>\frac12+\omega.
 \tag{T-91307.13}
\]

For the predetermined sequence

\[
 \omega_j=2^{-j-2}\downarrow0,
 \tag{T-91307.14}
\]

`EPBOT_(omega_j)` for every \(j\) proves RH by functional-equation symmetry.

## 6. Three constructive readings

### Suzuki–de Branges

The sector-changing graph closure is the global integrated Marchenko transform. The pole bridge is the single unstable endpoint state; the positive canonical Hamiltonian is formed only after this state has been coupled to the full Jordan tail.

### Lévy–Fock–Hardy

The safe prime factors remain exact Julia/Fock nodes, but their critical output is a different representation. `EPBOT_omega` is a wave operator between disjoint representations, not a unitary inside one incomplete tensor product.

### Theta/Brownian DtN

The pole bridge is a boundary state of the positive theta/Beta/Poisson/local form sum. The required Weyl function is obtained after Schur elimination of that bridge, so the same Green identity gives the completed Xi impedance.

## 7. Binary rejection tests

Reject a claimed proof if it:

1. places \(\mathfrak d_\omega^{\rm cyl}\) in the naive critical Fock Hilbert space;
2. implements critical translations by the primewise tensor product;
3. appends the gamma/theta channel only after the prime Hilbert completion;
4. maps the inverse directly to the interacting output without the forward Jordan factor;
5. omits the explicit pole bridge at \(s=1-\omega\);
6. infers the global analytic zero from finite Euler products;
7. rescales the pole-node source vector after seeing the target norm;
8. defines the auxiliary vector by subtracting the unknown target norm;
9. proves only local/finite-height convergence;
10. hides an indefinite or same-scale signed port.

## 8. Exact boundary

```text
all-prime inverse as cylinder distribution                    EXACT
Dirichlet-Hardy/Kakutani threshold                             EXACT
critical product translation disjointness                      EXACT
Green/Dirichlet-convolution commutation                         EXACT
free endpoint pole bridge and L2 threshold                     EXACT
finite Euler amplification of the bridge                       EXACT
old pole-node source normalization                             REFUTED
same-vacuum Julia-Wick Hilbert wave operator                   REFUTED
EPBOT_omega entangled sector-changing optical identity         OPEN / RH-BEARING
EPBOT on omega_j -> renewal L2 -> innerness -> RH              PROPOSED COMPLETE
Riemann Hypothesis                                             UNPROVED
```
