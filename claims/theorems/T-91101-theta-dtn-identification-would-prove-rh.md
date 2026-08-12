# T-91101 — A theta/Brownian Dirichlet-to-Neumann identification would prove RH

Claim ID: `T-91101`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; IDENTIFICATION OPEN**  
Created: 2026-08-11  
Depends on: PR #398; `L-91105`--`L-91108`  
RH status: **unproved**

## 1. Theta-DtN identification target

For each rational `0<a<1/2`, let

\[
 \ell_a(r)
 =\frac{\xi(\frac12+r+a)-\xi(\frac12+r-a)}
        {\xi(\frac12+r+a)+\xi(\frac12+r-a)}
\tag{T-91101.1}
\]

on the safe real half-line `r>a+1/2`.

The **Theta-DtN Identification (TDI)** is any construction of a Hilbert space `H_a`, a closed nonnegative bulk form `E_a`, and boundary solution vectors `j_a(r)` such that

\[
\boxed{
 \frac{\ell_a(r)+\ell_a(s)}{r+s}
 =\langle j_a(r),j_a(s)\rangle_{H_a}
}
\tag{T-91101.2}
\]

for all safe real `r,s`.

A boundary-triple realization of `ell_a` as the Weyl function of the supersymmetric theta bulk (L-91108.3), or a Gamma-shadow square for the Brownian form (L-91106.5) using (L-91107.9), is sufficient.

## 2. Conditional theorem

If TDI holds for every positive rational `a<1/2`, then the Riemann Hypothesis holds.

### Proof

For every finite safe rational packet, (T-91101.2) makes the matrix

\[
 H_{ij}=\frac{\ell_a(r_i)+\ell_a(r_j)}{r_i+r_j}
\]

positive semidefinite. By the exact Cayley congruence `L-91105`, the target matrix

\[
 C-DCD
\]

is positive semidefinite. PR #398 proves that positivity on the safe rational uniqueness set yields the global Schur continuation of

\[
 \Theta_{2a}(s)=\frac{\xi(s-2a)}{\xi(s)}
\]

in its moving half-plane by finite Nevanlinna--Pick interpolation, Montel compactness, and the identity theorem. An off-line zero would be an uncancelled pole for some rational `a`; therefore none exists. Functional-equation symmetry gives RH. QED.

## 3. Equivalent Brownian production theorem

By `L-91106`, TDI is equivalent to the reflection positivity

\[
\boxed{
 \mathbb E\left[
  \sinh(aS)
  \int_{-S/2}^{S/2}
   \overline{F(x+\Delta/2)}F(x-\Delta/2)dx
 \right]\ge0
}
\tag{T-91101.3}
\]

for every exponential polynomial `F`, where `S,Delta` come from two independent half-biased Brownian log ranges.

The proposed production chain is:

```text
pair the two BPY gamma sums mode by mode;
Gamma(2)+Gamma(2) -> Gamma(4) x Beta(2,2);
retain the exact half-size tilt (A^2-D^2)^(1/4);
solve the Jacobi Dirichlet problem in the beta variables;
identify its boundary flux with the interval autocorrelation in (T-91101.3);
pass to infinitely many modes with the Gamma tail retained as one reservoir.
```

PR #399's adjacent martingale butterflies are the natural finite transport basis for the fourth step.

## 4. Why this is a radical change of target

The conclusion-producing task is no longer:

```text
estimate a signed prime sum pointwise;
continue an abstract positive one-Green kernel;
prove infinitely many unrelated Hankel inequalities;
or prove a finite Brownian approximant globally real-rooted.
```

It is one exact identification:

\[
\boxed{
 \text{Xi horizontal impedance}
 =
 \text{Weyl function of an explicit positive theta/Brownian bulk}.
}
\]

Once the identity is present, positivity is inherited from `Q^*Q`; it is not separately estimated.

## 5. Proof boundary

Exact/proved in the current stack:

```text
safe Pick <-> Cayley anticommutator;
BPY impedance and two-copy reflection form;
Gamma(4)-Beta(2,2) reservoir and positive Jacobi energy;
theta Gibbs variance square;
supersymmetric theta bulk;
TDI -> RH composition.
```

Open:

```text
boundary/Jost/DtN identification TDI;
Gamma-shadow square for the Brownian interval autocorrelation;
Riemann Hypothesis.
```
