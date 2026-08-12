# L-91711 — The dyadic Clark innovations form an orthogonal first-chaos ledger

Claim ID: `L-91711`  
Status: **PROVED EXACT POSITIVE HILBERT/Fock LEDGER**  
Created: 2026-08-13  
Depends on: `L-91710`; the standard compound-Poisson Fock construction  
RH status: **unproved**

## 1. One-generation source

For the positive innovation measure `nu_j` of `L-91710`, put

\[
\mathfrak h_j=L^2((0,\infty),\nu_j)
\]

and define the carrier defect vector

\[
g_{j,t}(u)=e^{-itu}-1.
\]

Then

\[
\boxed{
\langle g_{j,t},g_{j,s}\rangle_{\mathfrak h_j}
=
\mathscr D_j(t,s),
}
\tag{L-91711.1}
\]

where `D_j` is the polarized kernel of `L-91710.8`. In particular,

\[
\|g_{j,t}\|^2
=
2\Re\ell_{2^ja,\sigma+2^{j+1}a}(t).
\tag{L-91711.2}
\]

## 2. Orthogonal all-generation ledger

Define

\[
\boxed{
\mathfrak H_{a,\sigma}^{\rm dyad}
=
\bigoplus_{j\ge0}\mathfrak h_j.
}
\tag{L-91711.3}
\]

For every finite radial truncation the vector

\[
G_t=igoplus_jg_{j,t}
\]

satisfies

\[
\boxed{
\langle G_t,G_s\rangle
=
\sum_j\mathscr D_j(t,s).
}
\tag{L-91711.4}
\]

Thus radial generations are orthogonal first-chaos innovations. No
cross-generation norm is counted twice.

## 3. Coherent-state completion

Let `Gamma_s(h_j)` be symmetric Fock space and let `Exp(v)` denote the
exponential vector. The normalized coherent phase

\[
\eta_{j,t}
=
\exp\!\left(-\frac12\|g_{j,t}\|^2\right)
\operatorname{Exp}(g_{j,t})
\]

has overlap

\[
\langle\eta_{j,t},\eta_{j,s}\rangle
=
\exp\!\left[
\mathscr D_j(t,s)
-\frac12\mathscr D_j(t,t)
-\frac12\mathscr D_j(s,s)
\right].
\]

The tensor product over generations is the coefficient-one compound-Poisson
product system associated with the safe zeta Euler source.

## 4. Entropy ledger

On a single carrier,

\[
\boxed{
-2\log|M_{2^Ja,\sigma}(t)|
=
-2\log|M_{a,\sigma}(t)|
+
\sum_{j=0}^{J-1}\|g_{j,t}\|^2.
}
\tag{L-91711.5}
\]

Equivalently, each generation contributes one nonnegative Clark entropy and
the returned state carries the coefficient-one remainder.

This is the source-side analogue of the additive annular Green telescope.

## 5. Scope

The theorem constructs the arithmetic source and its exact radial
orthogonality. It does not identify a particular source generation with the
critical, stable, or hyperbolic model outputs. That identification is the
remaining conclusion-producing theorem.
