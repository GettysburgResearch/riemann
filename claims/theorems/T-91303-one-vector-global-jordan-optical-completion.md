# T-91303 — One-Vector Global Jordan Optical Completion

Claim ID: `T-91303`  
Status: **CORRECTED FULL UNCONDITIONAL RH PROPOSAL — NOT A PROOF; ONE MINIMAL OPTICAL IDENTITY OPEN**  
Created: 2026-08-12  
Supersedes: the overstrong local-regularization and one-coordinate claims in `T-91302`  
RH status: **unproved**

## 1. Corrections incorporated

The first hostile pass proved two exact corrections.

1. `R-91303`: the fixed phase-locked `p=2` filter leaves a nonzero
   `(x-N)^(omega-1)` singularity at every odd integer for
   `0<omega<=1/2`; it is a lossless local port, not a hard-range
   regularizer.
2. `R-91304`: the log-odds Sturm--Liouville cell realizes the two-copy
   difference
   \[
   \Delta=\operatorname{artanh}(D/A),
   \]
   not the one-copy BPY variable in the Xi impedance. The sum coordinate `S`
   and the exact half-size tilt are also load-bearing.

The surviving common-kernel equivalences of `L-91307` remain exact.

## 2. The full Pick kernel is more than RH needs

Fix `omega>0` and define

\[
 \Theta_\omega(z)
 =\frac{\xi(\frac12-\omega-iz)}
        {\xi(\frac12+\omega-iz)}.
 \tag{T-91303.1}
\]

Let `h_omega` be Suzuki's inverse-Mellin kernel and put

\[
 A_\omega(x)=\int_1^x h_\omega(y)\,dy,
 \qquad
 f_\omega(t)=e^{-t/2}A_\omega(e^t)\mathbf1_{t\ge0}.
 \tag{T-91303.2}
\]

`L-91312` gives the exact transform

\[
 \boxed{
 \widehat f_\omega(z)
 =\frac{\Theta_\omega(z)}{\frac12-iz}.
 }
 \tag{T-91303.3}
\]

The factor `r(z)=(1/2-iz)^(-1)` is outer in `H^2(C_+)`, while
`|Theta_omega|=1` on the real boundary. Therefore

\[
 \boxed{
 f_\omega\in L^2(0,\infty)
 \iff
 \Theta_\omega\text{ is meromorphic inner in }\mathbb C_+.
 }
 \tag{T-91303.4}
\]

Thus one completed vector, rather than all finite Pick matrices, is sufficient.
The full kernel `AOT_omega` of `T-91302` is a stronger possible completion but
is not the minimal proof obligation.

## 3. Positive safe source

For `u=2omega`, the completed one-Green quotient has an unconditional positive
Laplace feature

\[
 \mathcal H_u(q)
 =\frac1q\frac{\xi(1+q)}{\xi(1+u+q)}
 =\int_0^\infty e^{-qt}M_u(t)\,dt,
 \qquad M_u(t)\ge0,
 \tag{T-91303.5}
\]

on the safe real half-line. Its arithmetic component is the positive
Jordan convolution with coefficients

\[
 c_\omega(n)=\frac{J_{2\omega}(n)}{n^\omega}>0.
 \tag{T-91303.6}
\]

The corresponding prime environment is the bosonic Fock product system of
`L-91309`. The rational and beta/Gamma factors supply the completed
archimedean/pole feature.

## 4. The minimal conclusion-producing theorem

> **One-Vector Optical Theorem (`OVOT_omega`).**  
> There is a source-ordered positive-metric isometry on the completed safe
> Green/Fock core
> \[
> \mathfrak V_\omega:
> \mathcal U_\omega^{\rm Green}
> \longrightarrow
> L^2(0,\infty)\oplus
> \mathcal E_{\theta,\beta,S\Delta,{\rm Pois},2}
> \tag{T-91303.7}
> \]
> and one explicit finite-norm safe source vector `e_omega` such that
> \[
> \boxed{
> \mathfrak V_\omega e_\omega
> =f_\omega\oplus q_\omega,
> }
> \tag{T-91303.8}
> \]
> where
> \[
> q_\omega
> =q_{\theta,\omega}
>  \oplus q_{\beta,S\Delta,\omega}
>  \oplus q_{{\rm Pois},\omega}
>  \oplus q_{2,\omega}
> \tag{T-91303.9}
> \]
> is assembled from the declared positive theta, coupled sum--difference,
> Poisson/Fock, and local `p=2` gradients.
>
> Equivalently, the exact source ledger is
> \[
> \boxed{
> \|e_\omega\|_{\mathcal U_\omega^{\rm Green}}^2
> =\|f_\omega\|_{L^2(0,\infty)}^2
>  +\|q_\omega\|_{\mathcal E}^2.
> }
> \tag{T-91303.10}
> \]

The source norm on the left is finite by the unconditional one-Green
construction. Therefore `OVOT_omega` implies `f_omega in L2`, hence innerness
by (T-91303.4).

An abstract definition

\[
 q_\omega=(\|e_\omega\|^2-\|f_\omega\|^2)^{1/2}
\]

is forbidden. Every component in (T-91303.9) must be written before the target
norm is known, in prime/theta/Brownian source order.

## 5. How the three routes now divide the work

### Route I — integrated Suzuki–de Branges

`L-91311` globally deconvolves Suzuki's integer singularities through the
Dirichlet inverse of the positive Jordan source. `L-91312` then uses one Green
primitive to regularize the sole remaining endpoint singularity. Finite
integrated Hankel truncations are Hilbert--Schmidt for every `omega>0`.

The canonical system is recovered from the compatible finite systems after
`OVOT_omega` proves losslessness. The fixed `p=2` packet is retained only as a
zero-safe finite boundary port.

### Route II — fully polarized Lévy–Fock–Hardy

The positive forward Jordan convolution has an explicit bosonic Fock dilation.
Its signed global Dirichlet inverse, given in `L-91311`, is realized as the
visible transfer of `V_omega`, while the defect is stored in the four positive
auxiliary channels. Causal and anti-causal outputs are recombined before any
trace is taken.

This is the primary constructive route to (T-91303.10).

### Route III — coupled Brownian–theta DtN

The local log-odds cell supplies the `Delta` gradient. The positive bulk must
also retain

\[
 S=\frac12\log(A^2-D^2)+2C,
 \qquad
 \Delta=\operatorname{artanh}(D/A),
 \tag{T-91303.11}
\]

together with the exact half-size tilt `exp(S/2-C)`. The target is the
sum--difference boundary identity `SDDI_omega` of `R-91304`, not a one-variable
`tanh` shortcut.

Its Green energy is the `q_(beta,SDelta,omega)` term in (T-91303.9).

## 6. Completion to RH

Take

\[
 \omega_j=2^{-j-2}\downarrow0.
 \tag{T-91303.12}
\]

If `OVOT_(omega_j)` holds for every `j`, then every `Theta_(omega_j)` is
meromorphic inner. A zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
\]

would give an uncancelled upper-half-plane pole for every sufficiently small
`omega_j<delta`, apart from at most finitely many exact horizontal zero
spacings. This contradicts innerness. Functional symmetry excludes the left
half-plane.

Therefore

\[
 \boxed{
 \forall j\;OVOT_{\omega_j}
 \quad\Longrightarrow\quad
 \mathrm{RH}.
 }
 \tag{T-91303.13}
\]

## 7. Exact proof boundary

```text
one Green primitive removes all local singularities       EXACT
global Jordan arithmetic deconvolution                    EXACT
one outer vector suffices for innerness                    PROPOSED COMPLETE
fixed p=2 hard-range regularization                        REFUTED
one-copy interpretation of the log-odds cell               REFUTED
coupled S–Delta boundary coordinates                       EXACT
positive safe Green/Fock source                            PROPOSED COMPLETE
OVOT_omega source-ordered isometry/norm identity           OPEN / RH-BEARING
OVOT on omega_j -> innerness -> RH                         PROPOSED COMPLETE
Riemann Hypothesis                                         UNPROVED
```

This is the corrected full unconditional proposal. It is not a completed proof.
