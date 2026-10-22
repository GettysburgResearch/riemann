# L-91033 — The boundary Jordan channel has an explicit Poisson-chaos complement

Claim ID: `L-91033`  
Status: **PROPOSED COMPLETE EXACT STINESPRING/CHAOS THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: main `L-91029`, `L-91020`, and `L-91030`  
RH status: **unproved**

## 1. Compound-Poisson anchor

Fix `a>0`, put `c_a=1+2a`, and define

\[
 \nu_a=
 \sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}
 (1-n^{-2a})n^{-c_a}\delta_{\log n}.
 \tag{L-91033.1}
\]

By main's compound-Poisson theorem and `L-91030`,

\[
 M_a(x)=\frac{Q_a(c_a+ix)}{Q_a(c_a)}
 =\exp\left\{\int(e^{-ixu}-1)d\nu_a(u)\right\}.
 \tag{L-91033.2}
\]

Let `N_a` be the Poisson random measure of intensity `nu_a` and

\[
 S_a=\int u\,N_a(du).
\]

Then

\[
 \boxed{M_a(x)=\mathbb E[e^{-ixS_a}].}
 \tag{L-91033.3}
\]

## 2. Minimal Stinespring phase vectors

For each carrier `x`, put

\[
 \eta_x(\omega)=e^{-ixS_a(\omega)}.
 \tag{L-91033.4}
\]

Then

\[
 \boxed{
 \langle\eta_x,\eta_y\rangle=M_a(x-y).
 }
 \tag{L-91033.5}
\]

For a finite carrier packet, the isometry

\[
 Ve_j=e_j\otimes\eta_{x_j}
\]

realizes the Schur correlation channel of `L-91020`:

\[
 V^*(X\otimes I)V=C_a\circ X,
 \qquad (C_a)_{jk}=M_a(x_j-x_k).
 \tag{L-91033.6}
\]

Thus the random-unitary dilation and the prime-power Fock product system are
the same environment.

## 3. Two positive cross-carrier defect kernels

The vectors

\[
 d_x=\eta_x-1
\]

have Gram kernel

\[
 \boxed{
 D_a(x,y)=1-M_a(x)-\overline{M_a(y)}+M_a(x-y)\succeq0.
 }
 \tag{L-91033.7}
\]

The centered phase vectors

\[
 c_x=\eta_x-M_a(x)
\]

have covariance kernel

\[
 \boxed{
 \Sigma_a(x,y)=M_a(x-y)-M_a(x)\overline{M_a(y)}\succeq0.
 }
 \tag{L-91033.8}
\]

These retain the polarization lost by a diagonal variance or the scalar bound
`|M_a(x)|<=1`.

## 4. One-particle defect and all-chaos resummation

Put

\[
 h_x(u)=e^{-ixu}-1\in L^2(\nu_a).
 \tag{L-91033.9}
\]

Then

\[
 \langle h_x,h_y\rangle=
 \int(e^{-ixu}-1)(e^{iyu}-1)d\nu_a(u).
 \tag{L-91033.10}
\]

The compound-Poisson covariance factors as

\[
 \boxed{
 \Sigma_a(x,y)=M_a(x)\overline{M_a(y)}
 \left[e^{\langle h_x,h_y\rangle}-1\right].
 }
 \tag{L-91033.11}
\]

Under the Poisson Fock isomorphism,

\[
 \boxed{
 \eta_x-M_a(x)=
 M_a(x)\sum_{m\ge1}\frac1{m!}I_m(h_x^{\otimes m}),
 }
 \tag{L-91033.12}
\]

and hence

\[
 \Sigma_a(x,y)=M_a(x)\overline{M_a(y)}
 \sum_{m\ge1}\frac{\langle h_x,h_y\rangle^m}{m!}.
 \tag{L-91033.13}
\]

This is the exact Wiener–Itô chaos complement of the inherited boundary
channel.

## 5. Relation to finite source ports

The first finite chaos levels explain the exact source-jet state counts:

```text
quadratic jet: one returned state plus two details;
cubic jet:     one returned state plus three details.
```

The three real Cauchy ports of `L-91022` combine into the single complex causal
Hardy channel of `L-91026/L-91031`.  The remaining task is therefore a
structured Fock-to-Hardy transfer, not the invention of additional source
states.

## 6. Conservative-colligation target

Let `H_Hardy` be the fixed-scale two-orientation output space of `L-91032`.
A complete proof of the fixed-scale criterion would follow from a positive-
metric isometry

\[
 \boxed{
 \mathcal U:
 \mathcal H_{\Gamma,\mathrm{pole}}
 \oplus\Gamma_s(L^2(\nu_a))
 \longrightarrow
 \mathcal H_{\mathrm{Hardy}}\oplus\mathcal E
 }
 \tag{L-91033.14}
\]

whose transfer kernel on carrier phase vectors is the completed screw kernel.
The auxiliary environment `E` is allowed, but no indefinite metric or
same-scale signed remainder is permitted.

All ingredients are now explicit:

```text
source: prime-power compound-Poisson Fock space;
source cross kernels: D_a and Sigma_a;
output: causal/anti-causal rational Hardy mothers;
bridge: one removable-pole vector;
reserve: completed gamma/pole channel.
```

By Kolmogorov/Douglas factorization, this colligation exists exactly when the
corresponding completed kernel domination holds.  It is a constructive form of
the remaining RH-equivalent inequality.

## 7. Boundary

Closed here, subject to independent review:

```text
explicit compound-Poisson anchor;
minimal phase-vector Stinespring dilation;
full positive cross-carrier defect kernels;
one-particle logarithmic defect;
all-order Poisson-chaos resummation;
precise completed Fock-to-Hardy colligation target.
```

Open:

```text
construction of the completed gamma/Poisson-to-Hardy isometry;
fixed-scale Lévy–Hardy Gram positivity;
RH.
```
