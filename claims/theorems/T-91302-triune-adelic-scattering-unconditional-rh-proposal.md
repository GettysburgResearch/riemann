# T-91302 — Triune Adelic Scattering Completion: a full unconditional proposal through one source-ordered optical theorem

Claim ID: `T-91302`  
Status: **FULL UNCONDITIONAL PROPOSAL — NOT A PROOF; ONE SOURCE-SPECIFIC OPTICAL THEOREM OPEN**  
Created: 2026-08-12  
RH status: **unproved**  
Depends on: `L-91307`–`L-91310`; PRs #400–#402; the phase-locked adelic theta-wavelet packet; standard realization theory

## 1. Meaning of “unconditional proposal”

No step in the construction assumes RH, a zero-free half-plane, innerness of
`Theta_a`, or positivity of the target Pick kernel. Every source space,
differential form, local port, coherent vector, and boundary trace is defined
from:

```text
the completed gamma/pole factor;
the positive generalized-Jordan prime-power measure;
the bosonic Fock product system;
the BPY Gamma–Beta variables;
the supersymmetric theta Hamiltonian;
the explicit self-dual p=2 wavelet and its Riesz orbit;
the explicit causal and anti-causal Hardy factors;
one bridge direction.
```

The proposal becomes a proof only after the source-ordered optical theorem
below is established.

## 2. The three routes are one problem

For

\[
\Theta_a(z)
=
\frac{\xi(\frac12-a-iz)}
     {\xi(\frac12+a-iz)}
\tag{T-91302.1}
\]

and

\[
\ell_a(z)=\frac{1-\Theta_a(z)}{1+\Theta_a(z)},
\tag{T-91302.2}
\]

`L-91307` proves that the following target kernels differ only by explicit
diagonal congruences:

\[
K_a^\Theta(z,w)
=
\frac{
1-\Theta_a(z)\overline{\Theta_a(w)}
}{
-i(z-\bar w)
},
\tag{T-91302.3}
\]

\[
K_a^\ell(z,w)
=
\frac{
\ell_a(z)+\overline{\ell_a(w)}
}{
-i(z-\bar w)
},
\tag{T-91302.4}
\]

\[
K_a^E(z,w)
=
\frac{
E_a(z)\overline{E_a(w)}
-
E_a^\#(z)\overline{E_a^\#(w)}
}{
-2\pi i(z-\bar w)
}.
\tag{T-91302.5}
\]

Consequently:

```text
Suzuki–de Branges canonical system
= conservative Fock–Hardy colligation
= theta/Brownian Dirichlet-to-Neumann map
```

at the level of the exact positive kernel.

## 3. Common source and output spaces

Fix a rational `0<a<1/2`.

### Input

\[
\mathcal U_a
=
\mathcal H_{\Gamma/{\rm pole},a}
\oplus
\Gamma_s(\mathfrak h_a),
\tag{T-91302.6}
\]

where `h_a` and its coherent vectors are given in `L-91309`.

### Visible output

\[
\mathcal Y_a^{\rm vis}
=
H^2_+\oplus H^2_-\oplus\mathbb C_{\rm bridge}.
\tag{T-91302.7}
\]

### Positive auxiliary output

\[
\mathcal Y_a^{\rm aux}
=
\mathcal H_\theta
\oplus
\mathcal H_{\beta,a}
\oplus
\mathcal H_{{\rm Pois},a}
\oplus
\mathcal H_{2,a}.
\tag{T-91302.8}
\]

The four components carry, respectively, the theta supersymmetric gradient,
the log-odds/Gamma–Beta gradient, the Fock difference gradient, and the radial
`p=2` gradient.

## 4. The single conclusion-producing theorem

> **Adelic Optical Theorem (`AOT_a`).**  
> On the source coherent core there is an explicit map
> \[
> \mathfrak V_a:
> \mathcal U_a
> \longrightarrow
> \mathcal Y_a^{\rm vis}\oplus\mathcal Y_a^{\rm aux}
> \]
> assembled in source order from the declared local and archimedean pieces,
> such that
> \[
> \boxed{
> \langle e_{a,w},e_{a,z}\rangle_{\mathcal U_a}
> =
> \langle \mathfrak V_ae_{a,w},
>         \mathfrak V_ae_{a,z}\rangle
> }
> \tag{T-91302.9}
> \]
> and the visible scalar transfer is exactly `Theta_a`.
>
> Equivalently,
> \[
> \boxed{
> K_a^\Theta(z,w)
> =
> \langle q_{a,w},q_{a,z}\rangle_{\mathcal Y_a^{\rm aux}},
> }
> \tag{T-91302.10}
> \]
> where `q_(a,z)` is the explicitly declared
> theta/Beta/Poisson/`p=2` gradient vector.
>
> Equivalently again, the positive bulk of `L-91310` has Weyl function
> `ell_a`, and the regularized Suzuki–Marchenko construction of `L-91308`
> has terminal structure function `E_a`.

The three equivalences after (T-91302.9) are consequences of `L-91307`; they do
not create three independent unproved statements.

## 5. Route I produced from `AOT_a`

Equation (T-91302.10) gives `K_a^E >= 0`. The de Branges chain theorem
produces a positive Hamiltonian `H_a(t)>=0` with terminal structure
function `E_a`.

More constructively, the `p=2`-regularized multiplicative Hankel operator of
`L-91308` yields Fredholm tau functions and the same Hamiltonian. The finite
local factor is Schur-eliminated before the reduced determinant is read.

Thus `AOT_a` supplies the requested unconditional Suzuki–de Branges
construction.

## 6. Route II produced from `AOT_a`

Equation (T-91302.9) is a lurking isometry on a total set of Fock coherent
vectors. Its unitary extension is the fully polarized conservative colligation

\[
U_a:
\mathcal H_{\Gamma/{\rm pole},a}\oplus\Gamma_s(\mathfrak h_a)
\longrightarrow
H^2_+\oplus H^2_-\oplus\mathbb C_{\rm bridge}
\oplus\mathcal Y_a^{\rm aux}.
\tag{T-91302.11}
\]

The transfer is `Theta_a`, so the colligation optical identity gives
innerness.

Thus `AOT_a` supplies the requested Lévy–Fock–Hardy conservative system.

## 7. Route III produced from `AOT_a`

The auxiliary norm in (T-91302.10) is the Green energy of the positive form sum

\[
\mathbb H_a
=
H_\theta
\boxplus
\mathcal S_a^{(\beta)}
\boxplus
\mathcal N_{\rm Pois}
\boxplus
\mathcal D_2.
\tag{T-91302.12}
\]

The even/odd theta traces are its boundary maps, and its Weyl function is
`ell_a`. Therefore Green's identity factors `K_a^ell`.

Thus `AOT_a` supplies the requested theta/Brownian DtN identification.

## 8. Completion to RH

Take the predetermined sequence

\[
a_j=2^{-j-2},\qquad j=0,1,2,\ldots.
\tag{T-91302.13}
\]

If `AOT_(a_j)` holds for every `j`, then every `Theta_(a_j)` is
meromorphic inner. If

\[
\rho=\frac12+\delta+i\gamma,\qquad \delta>0,
\]

were an off-line zero, then for every sufficiently small `a_j<delta`, except
possibly finitely many exact horizontal zero spacings, the denominator of
`Theta_(a_j)` would have an uncancelled upper-half-plane zero. This
contradicts innerness. Functional symmetry excludes the left half as well.

Hence

\[
\boxed{
\forall j\ AOT_{a_j}
\quad\Longrightarrow\quad
{\rm RH}.
}
\tag{T-91302.14}
\]

By PR #402, the same conclusion is equivalent to finiteness of the factor-four
renewal energy for every `a_j`.

## 9. What is genuinely new in this proposal

1. The three requested routes are fused into one kernel rather than pursued as
   disconnected RH-equivalent criteria.
2. The `p=2` phase-locked source is used as a lossless local port, not as a
   generic modularity argument.
3. The Fock environment is kept fully polarized until after the Hardy cross
   channels and bridge are formed.
4. The Brownian `tanh(aZ)` coordinate is promoted to an explicit positive
   log-odds Sturm–Liouville cell.
5. The historical missing theta anticommutator square is enlarged by the exact
   Beta, Poisson, and `p=2` positive reservoirs.
6. The closing statement is one source-ordered equality of Gram kernels, not a
   qualitative demand to “find a Hilbert–Pólya operator.”

## 10. Exact proof boundary

```text
common Schur/Cayley/de Branges kernel congruences       EXACT
abstract three-realization equivalence                  STANDARD / COMPLETE
prime Jordan bosonic Fock product system                PROPOSED COMPLETE
causal + anti-causal Hardy channels and bridge          PROPOSED COMPLETE
self-dual p=2 local port and Riesz synthesis             PROPOSED COMPLETE
positive theta supersymmetric bulk                      PROPOSED COMPLETE
log-odds Sturm–Liouville cell                           EXACT
Gamma–Beta / Poisson / p=2 form sum                     CONSTRUCTED CANDIDATE
AOT_a source-ordered Gram identity                      OPEN / RH-BEARING
AOT for a_j -> innerness -> RH                          PROPOSED COMPLETE
Riemann Hypothesis                                      UNPROVED
```

This is a full unconditional proposal, not a completed proof.
