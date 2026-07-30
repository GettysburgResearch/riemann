# T-15101 — Form-core transfer of a simple-even localized ground state

Claim ID: `T-15101`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Dependencies: min--max principle for closed lower-bounded forms, compact resolvent, and parity-invariant form-core density  
Scope: remove fixed-support finite simplicity/parity as an independent positive-route hypothesis  
Related counterexample candidates: none

## Statement

Let `H` be a real or complex Hilbert space. Let `q` be a closed lower-bounded
Hermitian form with form domain `D(q)` and compact-resolvent self-adjoint
operator `A`.

Let `Gamma` be a self-adjoint involution preserving `D(q)` and satisfying

\[
 q(\Gamma f,\Gamma g)=q(f,g).
 \tag{T-15101.1}
\]

Write

\[
 H=H_+\oplus H_-,
 \qquad
 H_\pm=\ker(\Gamma\mp I).
\]

Let

\[
 V_1\subset V_2\subset\cdots\subset D(q)
 \tag{T-15101.2}
\]

be finite-dimensional, nested, `Gamma`-invariant subspaces whose union is dense
in `D(q)` for the form norm. Let `A_N` denote the Ritz operator of `q` on
`V_N`.

Assume the global ground eigenvalue `lambda_0` of `A` is simple and has an even
normalized eigenvector `xi_0`. Let

\[
 \lambda_{1,+}
 =\inf_{\substack{f\in D(q)\cap H_+\cap\xi_0^\perp\\\|f\|=1}}q(f,f),
 \qquad
 \lambda_{0,-}
 =\inf_{\substack{f\in D(q)\cap H_-\\\|f\|=1}}q(f,f),
 \tag{T-15101.3}
\]

with an absent sector interpreted as `+infinity`, and suppose

\[
 \boxed{
 g=\min\{\lambda_{1,+}-\lambda_0,
          \lambda_{0,-}-\lambda_0\}>0.}
 \tag{T-15101.4}
\]

Then:

1. the lowest even Ritz value decreases to `lambda_0`;
2. the next even Ritz value decreases to `lambda_(1,+)`;
3. the lowest odd Ritz value decreases to `lambda_(0,-)`;
4. for all sufficiently large `N`, the global lowest eigenvalue of `A_N` is
   simple and even;
5. if `xi_N` is its normalized eigenvector with
   `Re <xi_N,xi_0> > 0`, then

   \[
    \boxed{\xi_N\longrightarrow\xi_0}
    \tag{T-15101.5}
   \]

   both in the Hilbert norm and in the form norm.

Consequently, at a fixed finite support `lambda`, the CCM Fourier matrices need
no separate all-large-cutoff simplicity theorem: continuum simplicity, parity,
and a positive continuum gap force the required finite properties cofinally.

## Proof

### 1. Parity form cores

Because every `V_N` is `Gamma`-invariant, the projections

\[
 P_\pm=\frac12(I\pm\Gamma)
\]

map `V_N` into itself. Form-density of the full union therefore implies
form-density of

\[
 \bigcup_N(V_N\cap H_+)
 \quad\hbox{and}\quad
 \bigcup_N(V_N\cap H_-)
\]

in the corresponding parity form domains.

### 2. Ritz-value convergence

The min--max principle on each parity sector gives monotone upper
approximations. Form-core density supplies recovery sequences for every fixed
finite-dimensional spectral subspace. Hence

\[
 \lambda_{0,+}^{(N)}\downarrow\lambda_0,
 \qquad
 \lambda_{1,+}^{(N)}\downarrow\lambda_{1,+},
 \qquad
 \lambda_{0,-}^{(N)}\downarrow\lambda_{0,-}.
 \tag{T-15101.6}
\]

Compact resolvent ensures the relevant infima are isolated eigenvalues whenever
the corresponding sector is present.

By (T-15101.4), eventually

\[
 \lambda_{0,+}^{(N)}
 <\min\{\lambda_{1,+}^{(N)},\lambda_{0,-}^{(N)}\}.
 \tag{T-15101.7}
\]

Thus the global finite ground eigenvalue is simple and its eigenvector is even.

### 3. Ground-line convergence

For large `N`, let `xi_N` be the normalized even ground vector and write

\[
 \xi_N=a_N\xi_0+b_N,
 \qquad b_N\perp\xi_0.
\]

The continuum spectral gap in the even sector gives

\[
 q(\xi_N,\xi_N)
 \ge |a_N|^2\lambda_0
    +(1-|a_N|^2)\lambda_{1,+}
 =\lambda_0
  +(\lambda_{1,+}-\lambda_0)\|b_N\|^2.
 \tag{T-15101.8}
\]

The left side is the finite ground Ritz value and tends to `lambda_0`.
Therefore `||b_N|| -> 0` and `|a_N| -> 1`. Choosing the phase so that
`Re a_N>0` proves Hilbert-norm convergence.

Choose `C` so that

\[
 q_C(f,f)=q(f,f)+C\|f\|^2
\]

is positive. Since `xi_0` lies in the operator domain,

\[
 q(\xi_N,\xi_0)=\lambda_0\langle\xi_N,\xi_0\rangle.
\]

Therefore

\[
 \begin{aligned}
 q_C(\xi_N-\xi_0)
 &=q(\xi_N)+\lambda_0
   -2\lambda_0\operatorname{Re}a_N
   +C(2-2\operatorname{Re}a_N)\\
 &\longrightarrow0,
 \end{aligned}
 \tag{T-15101.9}
\]

which proves form-norm convergence. QED.

## CCM/localized-Weil specialization

At one fixed endpoint parameter `lambda`, take:

- `q` to be the exact localized Weil form;
- `Gamma f(u)=f(u^-1)`;
- `V_N=E_N(lambda)`, the finite Fourier spaces used by CCM.

The source paper already identifies the Fourier union as a form core in its
normalization. Subject to that imported statement and compact resolvent, the
theorem applies verbatim.

For every fixed `0<tau<1/2`, the Hardy norm on the compact support satisfies

\[
 \|f\|_{\lambda,\tau}
 \le\sqrt2\,\lambda^\tau\|f\|_2.
 \tag{T-15101.10}
\]

Thus, after the continuum ground line has been identified, one may choose a
finite cutoff `N` large enough to approximate it by any prescribed Hardy-norm
error. A diagonal choice over increasing supports is then automatic.

## Consequence for the critical path

The positive route no longer has three independent spectral assumptions:

```text
finite ground simple;
finite ground even;
finite ground approaches a continuum target.
```

At fixed support, all three follow from:

```text
continuum ground simple and even;
positive continuum separation from the next even and odd modes;
form-core Galerkin convergence.
```

The unresolved theorem is therefore the continuum leakage/gap estimate in
`T-15102`, not an all-cutoff finite matrix pattern.

## Gap audit

- A form core is essential. Ordinary `L2` density alone does not imply Ritz
  convergence for an unbounded operator.
- `Gamma` invariance of every finite subspace is essential for the parity-sector
  conclusions.
- One finite simple-even ground state does not prove continuum simplicity.
- The theorem is fixed-support. Uniformity as `lambda -> infinity` requires a
  separate leakage/gap estimate.
- The imported CCM form-core and localized-operator normalizations require an
  independent source audit before an RH claim.
