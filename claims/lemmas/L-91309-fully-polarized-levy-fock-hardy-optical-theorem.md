# L-91309 — Fully polarized Lévy–Fock–Hardy completion and the source-ordered optical theorem

Claim ID: `L-91309`  
Status: **FULL CONSTRUCTIVE COLLIGATION PROGRAMME; ONE GRAM IDENTITY OPEN**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Prime-power one-particle space

Fix `a>0`. Let

\[
\mathfrak h_a
=
L^2\!\left(
[0,a]\times\mathcal P^*,
2\Lambda(n)\,d\tau
\right),
\tag{L-91309.1}
\]

where `P*` is the set of prime powers, counted in the repository's
von-Mangoldt convention. For safe parameters `s,t`, put

\[
v_{a,s}(\tau,n)
=
\mathbf 1_{[0,a]}(\tau)n^{-s-\tau}.
\tag{L-91309.2}
\]

Then

\[
\langle v_{a,t},v_{a,s}\rangle_{\mathfrak h_a}
=
\log\frac{\zeta(s+\bar t)}{\zeta(s+\bar t+2a)}.
\tag{L-91309.3}
\]

In symmetric bosonic Fock space,

\[
\left\langle
\operatorname{Exp}(v_{a,t}),
\operatorname{Exp}(v_{a,s})
\right\rangle
=
\frac{\zeta(s+\bar t)}{\zeta(s+\bar t+2a)}.
\tag{L-91309.4}
\]

The scale cocycle is literal interval factorization:

\[
v_{a+b,s}
=
v_{a,s}\oplus v_{b,s+a}.
\tag{L-91309.5}
\]

Thus the positive generalized-Jordan source is an explicit bosonic product
system rather than an abstract positive kernel.

## 2. Full polarization

At a safe vertical line the normalized quotient is compound Poisson. Its
one-particle phase vectors retain every prime-power phase before aggregation.
The complete Wiener–Itô chaos kernel is

\[
K_{\rm Fock}(s,t)
=
\sum_{m\ge0}\frac1{m!}
\left\langle v_{a,t},v_{a,s}\right\rangle^m.
\tag{L-91309.6}
\]

No trace over the Fock environment is allowed before the causal/anti-causal
cross channels have been formed.

## 3. Hardy outputs

Let `Psi_a^+` be the causal Cauchy spectral factor retained on the parent
branch, `Psi_a^-=(Psi_a^+)^#` its reflected anti-causal channel, and `b_a` the
one bridge vector carrying the global mean-zero direction. For a carrier `x`,
let

\[
\widehat f_{a,x}^{\pm}(\lambda)
=
\lambda\Psi_a^\pm(\lambda-x).
\tag{L-91309.7}
\]

The output space is

\[
\mathcal Y_a
=
H^2_+\oplus H^2_-\oplus\mathbb C_{\rm bridge}
\oplus\mathcal Y_{a,\rm aux}.
\tag{L-91309.8}
\]

The first three summands are fixed and explicit. The auxiliary summand is the
positive theta/Brownian/`p=2` reserve of `L-91310`.

## 4. Input space

Adjoin the positive beta/Gamma and completed pole channels to the prime Fock
source:

\[
\mathcal U_a
=
\mathcal H_{\Gamma,\mathrm{pole},a}
\oplus\Gamma_s(\mathfrak h_a).
\tag{L-91309.9}
\]

The completed safe-side coherent vector `e_(a,z)` in `U_a` is the tensor product
of the explicit gamma/pole feature and `Exp(v_(a,z))`.

## 5. The source-ordered optical theorem

The required identity is the following.

> **Adelic Optical Theorem (`AOT_a`).**  
> There exist explicit auxiliary vectors `q_(a,z)` in `Y_(a,aux)`, assembled
> from the supersymmetric theta gradient, the Gamma–Beta Jacobi gradient, the
> prime Poisson difference gradient, and the radial `p=2` Riesz gradient, such
> that on the safe exponential core
> \[
> \boxed{
> \frac{
> 1-\Theta_a(z)\overline{\Theta_a(w)}
> }{
> -i(z-\bar w)
> }
> =
> \langle q_{a,w},q_{a,z}\rangle_{\mathcal Y_{a,\rm aux}}.
> }
> \tag{L-91309.10}
> \]
> Equivalently, before scalar normalization,
> \[
> K_{\rm source,a}
> =
> K_{\rm Hardy,+}
> +K_{\rm Hardy,-}
> +K_{\rm bridge}
> +K_{\rm aux},
> \qquad
> K_{\rm aux}\succeq0,
> \tag{L-91309.11}
> \]
> with every term written in source order.

Equation (L-91309.11), not an existential square root of the unknown Xi kernel,
is the proof obligation.

## 6. Lurking isometry and conservative completion

If `AOT_a` holds, equality of the Gram kernels defines an isometry on the span
of source coherent vectors:

\[
e_{a,z}
\longmapsto
f^+_{a,z}\oplus f^-_{a,z}\oplus b_{a,z}\oplus q_{a,z}.
\tag{L-91309.12}
\]

The coherent vectors are total in the bosonic Fock product system. After adding
the orthogonal defect space, (L-91309.12) extends to a unitary colligation

\[
\boxed{
U_a:
\mathcal H_{\Gamma,\mathrm{pole},a}
\oplus\Gamma_s(\mathfrak h_a)
\longrightarrow
H^2_+\oplus H^2_-\oplus
\mathbb C_{\rm bridge}\oplus\mathcal Y_{a,\rm aux}.
}
\tag{L-91309.13}
\]

The scalar transfer channel is `Theta_a`. The standard colligation optical
identity then reproduces (L-91309.10) globally and proves that `Theta_a` is
inner.

## 7. Why this route is stronger than diagonal prime positivity

The diagonal prime mass diverges in the critical normalization and cannot prove
the target by Tonelli or absolute values. The load-bearing terms are:

```text
causal / anti-causal cross polarization;
the bridge direction;
the completed gamma/pole channel;
the untraced Fock chaos;
the theta/Brownian/p=2 auxiliary reserve.
```

Removing any one of them recreates the known firewalls.

## 8. Exact remaining work

The Fock source, its product system, the Hardy factors, and the bridge are
explicit. The conclusion-producing step is to prove the source-ordered identity
(L-91309.11). `L-91310` gives a concrete positive candidate for `K_aux`;
`T-91302` explains how that same identity yields the other two requested
routes.
