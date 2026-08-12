# T-91304 — Lossless Dyadic Cascade Descent: a full RH proposal from terminal innerness and complete detail ports

Claim ID: `T-91304`  
Status: **FULL UNCONDITIONAL PROPOSAL — NOT A PROOF; CONSERVATIVE TWO-SECTION COLLIGATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91321/L-91322`; main `L-91014`–`L-91029`; corrected `T-91303`  
RH status: **unproved**

## 1. Exact scalar cocycle

With

\[
 X(w)=\xi\!\left(\frac12+w\right),
 \qquad
 \Phi_a(w)=\frac{X(w)}{X(w+2a)},
 \tag{T-91304.1}
\]

one has

\[
 \boxed{
 \Phi_{2a}(w)
 =\Phi_a(w)\Phi_a(w+2a).
 }
 \tag{T-91304.2}
\]

A zero of horizontal depth `d` with `a<d<=2a` is exactly an internal pole of
the first factor canceled by a numerator zero of the second factor. Thus the
scalar product hides precisely the annular zero states.

## 2. Source factorization

The generalized-Jordan source has the coefficient-one interval/Fock
factorization

\[
 \mathcal U_{2a}^{\rm src}
 \cong
 \mathcal U_a^{\rm src,0}
 \widehat\otimes
 \mathcal U_a^{\rm src,1},
 \tag{T-91304.3}
\]

with the shifted second section implementing `w -> w+2a`. The completed
rational, beta/Gamma, pole, and theta channels have matching two-section
cocycles. All source spaces are positive and defined in the safe half-plane.

## 3. Required conservative two-section colligation

> **Lossless Two-Section Colligation (`LTSC_a`).**  
> Construct, from the explicit source product system, a positive-metric unitary
> colligation
> \[
> \boxed{
> U_a:
> \mathcal U_{2a}^{\rm src}
> \longrightarrow
> \mathcal Y_{2a}^{\rm scalar}
> \oplus
> \mathcal D_a^{\rm detail}
> }
> \tag{T-91304.4}
> \]
> with the following properties.
>
> 1. The scalar transfer is exactly `Phi_(2a)` on a safe open uniqueness set,
>    hence everywhere by analytic continuation.
> 2. Internally, the scalar channel is the cascade of the two fine sections in
>    (T-91304.2), with coefficient one.
> 3. The detail output is the orthogonal sum of:
>    ```text
>    causal Cauchy channel;
>    anti-causal reflected Cauchy channel;
>    one bridge state;
>    coupled Brownian/theta sum--difference reserve;
>    prime Poisson/Fock chaos complement;
>    local p=2 boundary port.
>    ```
> 4. Every intermediate zero value/jet state has the natural prime-power input
>    and Cauchy/Hardy output couplings of `L-91322`.
> 5. No indefinite metric or unrecorded same-scale signed port is allowed.
>
> On the boundary the unitary optical identity is
> \[
> \boxed{
> |\Phi_{2a}|^2+\|D_a\|^2=1,
> }
> \tag{T-91304.5}
> \]
> in the normalized scalar-input channel.

`LTSC_a` is the dynamic version of the analytic intertwiner in `O-91302`.

## 4. One descent step

Assume `Phi_(2a)` is inner in its moving half-plane. Then its boundary values
have modulus one almost everywhere. Equation (T-91304.5) gives

\[
 \|D_a(x)\|^2=0
 \qquad\text{for almost every boundary }x.
 \tag{T-91304.6}
\]

Every detail component is analytic/Hardy after the declared stable factors are
removed, so boundary uniqueness gives

\[
 \boxed{D_a\equiv0.}
 \tag{T-91304.7}
\]

Suppose an annular zero `a<d<=2a` existed. By `L-91321` it is an internal
pole--zero cancellation state of the two-section cascade. By `L-91322`, every
finite value/jet packet is controllable by prime powers and observable in the
Hardy detail outputs. Such a state would force `D_a` to be nonzero, contradicting
(T-91304.7). The weighted closure/tail condition in `LTSC_a` rules out an
infinite hidden state.

Hence no zero has depth greater than `a`; equivalently `Phi_a` is inner.

Thus

\[
 \boxed{
 \Phi_{2a}\text{ inner}+LTSC_a
 \Longrightarrow
 \Phi_a\text{ inner}.
 }
 \tag{T-91304.8}
\]

## 5. Terminal start and full descent

All nontrivial zeros have depth `<1/2`. Therefore `Phi_A` is inner for every
`A>=1/2`, unconditionally.

Given arbitrary `a>0`, choose `J` with `2^Ja>=1/2`. If

\[
 LTSC_{2^ja}
 \qquad(j=0,1,\ldots,J-1)
 \tag{T-91304.9}
\]

holds, repeated use of (T-91304.8) gives innerness of `Phi_a`.

If `LTSC_a` is constructed for every positive `a`, every horizontal quotient
is inner and the Riemann Hypothesis follows.

It is enough to construct it along one dyadic lattice cofinal at zero.

## 6. Relation to the three requested routes

### Suzuki--de Branges

The finite integrated Marchenko system is the state realization of each
section. The detail-null conclusion is canonical-system minimality; the scalar
transfer at the fine scale is then Hermite--Biehler.

### Lévy--Fock--Hardy

The two source sections are literal bosonic Fock intervals. `LTSC_a` is their
fully polarized conservative output map. This is the most direct construction
route.

### Theta/Brownian DtN

The detail norm is the Green energy of the coupled theta, `(S,Delta)` Beta,
Poisson, and local-port form. Vanishing detail means no nonzero zero-energy
interior state with zero external trace.

Thus all three routes are one lossless-cascade theorem.

## 7. What is already closed

```text
scalar completed cocycle                         EXACT
terminal large-scale innerness                   UNCONDITIONAL
annular zeros = internal pole-zero cancellations EXACT
finite packet source controllability             EXACT
finite packet Hardy observability                EXACT
global Jordan source product system              PROPOSED COMPLETE
local singularity repair by one primitive         EXACT
```

## 8. What remains

```text
positive-metric LTSC_a construction               OPEN / RH-BEARING
completed gamma/theta/Fock-to-Hardy norm identity OPEN / RH-BEARING
infinite-state closure and tail                    OPEN
Riemann Hypothesis                                UNPROVED
```

This is a full unconditional proposal, not a proof.
