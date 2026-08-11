# L-91031 — The boundary Jordan channel has an explicit Poisson-chaos complement

Claim ID: `L-91031`  
Status: **PROPOSED COMPLETE EXACT STINESPRING/CHAOS THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91020`, `L-91028`  
RH status: **unproved**

## 1. Compound-Poisson anchor

Fix `a>0` and put

\[
 c_a=1+2a.
\]

Let

\[
 \nu_a
 =\sum_{n\in\mathcal P^*}
 \frac{\Lambda(n)}{\log n}
 (1-n^{-2a})n^{-c_a}\delta_{\log n}.
 \tag{L-91031.1}

By `L-91028`, this is a finite positive measure and

\[
 M_a(x)
 =\frac{Q_a(c_a+ix)}{Q_a(c_a)}
 =\exp\left\{
  \int(e^{-ixu}-1)d\nu_a(u)
 \right\}.
 \tag{L-91031.2}

Let `N_a` be the Poisson random measure of intensity `nu_a` and put

\[
 S_a=\int u\,N_a(du).
\]

Then

\[
 \boxed{M_a(x)=\mathbb E[e^{-ixS_a}].}
 \tag{L-91031.3}

This is the exact random variable whose phase vectors implement the correlation
channel in `L-91020`.

## 2. Full Stinespring vectors

For each carrier `x`, define

\[
 \eta_x(\omega)=e^{-ixS_a(\omega)}
 \in L^2(\Omega_a).
 \tag{L-91031.4}

Then

\[
 \boxed{
 \langle\eta_x,\eta_y\rangle
 =M_a(x-y).
 }
 \tag{L-91031.5}

For a finite carrier set `x_1,...,x_N`, the isometry

\[
 Ve_j=e_j\otimes\eta_{x_j}
 \tag{L-91031.6}

satisfies

\[
 V^*(X\otimes I)V=C_a\circ X,
 \qquad
 (C_a)_{jk}=M_a(x_j-x_k).
 \tag{L-91031.7}

Thus the random-unitary formula of `L-91020` and the Fock product system of
`L-91028` are the same minimal Stinespring environment.

## 3. Two exact positive defect kernels

The vectors

\[
 d_x=\eta_x-1
\]

have Gram kernel

\[
 \boxed{
 D_a(x,y)
 =1-M_a(x)-\overline{M_a(y)}+M_a(x-y)
 \succeq0.
 }
 \tag{L-91031.8}

The centred random variables

\[
 c_x=\eta_x-M_a(x)
\]

have covariance kernel

\[
 \boxed{
 \Sigma_a(x,y)
 =M_a(x-y)-M_a(x)\overline{M_a(y)}
 \succeq0.
 }
 \tag{L-91031.9}

These kernels retain the cross-carrier polarization that is lost if one keeps
only `|M_a(x)|<=1` or only diagonal variances.

## 4. One-particle logarithmic defect

Put

\[
 h_x(u)=e^{-ixu}-1
 \in L^2(\nu_a).
 \tag{L-91031.10}

Then

\[
 \boxed{
 \langle h_x,h_y\rangle_{L^2(\nu_a)}
 =\int(e^{-ixu}-1)(e^{iyu}-1)d\nu_a(u).
 }
 \tag{L-91031.11}

The compound-Poisson covariance factors as

\[
 \boxed{
 \Sigma_a(x,y)
 =M_a(x)\overline{M_a(y)}
 \left[
  e^{\langle h_x,h_y\rangle}-1
 \right].
 }
 \tag{L-91031.12}

This is an exact all-chaos resummation of the one-particle positive kernel.

## 5. Wiener--Itô decomposition

Under the Poisson Fock isomorphism, the centred phase has the orthogonal
expansion

\[
 \boxed{
 \eta_x-M_a(x)
 =M_a(x)\sum_{m\ge1}\frac1{m!}
 I_m(h_x^{\otimes m}),
 }
 \tag{L-91031.13}

with the usual normalization of multiple compensated-Poisson integrals.
Consequently

\[
 \boxed{
 \Sigma_a(x,y)
 =M_a(x)\overline{M_a(y)}
 \sum_{m\ge1}\frac{
  \langle h_x,h_y\rangle^m}{m!}.
 }
 \tag{L-91031.14}

The first three nontrivial chaos levels are the intrinsic infinite-dimensional
source counterpart of the three cubic detail ports in `L-91025`.  The exact
physical residual of `L-91026` packages three real ports into one complex Hardy
channel; the remaining task is therefore a structured Fock-to-Hardy transfer,
not the invention of more source states.

## 6. A precise conservative-colligation target

Let `mathcal H_Hardy` be the two-orientation fixed-scale output space of
`L-91030`.  A complete proof of `T-91006` would follow from an isometry

\[
 \boxed{
 \mathcal U:
 \mathcal H_{\Gamma,\mathrm{pole}}
 \oplus
 \Gamma_s(L^2(\nu_a))
 \longrightarrow
 \mathcal H_{\mathrm{Hardy}}
 \oplus\mathcal E
 }
 \tag{L-91031.15}

whose transfer kernel on carrier phase vectors is `mathbb K_(a_0)`.
The auxiliary space `mathcal E` is allowed, but no indefinite metric is.

The data on both sides are now explicit:

```text
source environment: prime-power compound-Poisson Fock space;
source cross kernel: D_a or Sigma_a;
output environment: causal and anti-causal rational Hardy mothers;
output bridge: one explicit removable-pole vector;
completed reserve: gamma/pole channel.
```

By the Kolmogorov/Douglas factorization theorem, such a contractive
intertwiner exists exactly when the corresponding completed kernel domination
holds.  Thus (L-91031.15) is neither weaker nor stronger than the remaining
fixed-scale Gram sign; it is its constructive state-space form.

## 7. Boundary

Closed here, subject to independent review:

```text
exact compound-Poisson anchor variable;
minimal phase-vector Stinespring dilation;
two full positive cross-carrier defect kernels;
one-particle logarithmic defect;
all-order Poisson-chaos resummation;
precise conservative Fock-to-Hardy colligation target.
```

Still open:

```text
construction of the completed gamma/Poisson-to-Hardy isometry;
fixed-scale Levy-Hardy Gram positivity;
RH.
```
