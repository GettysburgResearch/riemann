# R-106123 — A fixed-core large sieve does not pay the global least-prime conductor family

Claim ID: `R-106123`  
Programme aliases: `LFAM1.CORE_CONDUCTOR_DIMENSION_FIREWALL`, `LFAM2.VARYING_MODULUS_TRACE_GAP`, `STRESS.NEAR_PRIME_SELF_AUDIT`  
Status: **PROVED EXACT GLOBAL-SUMMATION FIREWALL; THE GLOBAL CLOSURE CLAIM OF THE FIRST `L-106123` IS RETRACTED**  
Created: 2026-08-25  
Depends on: `L-106120--L-106123`; `R-102840`, `R-106071`, `R-106110`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The local two-dimensional additive large-sieve estimate in the first
`L-106123` is correct.  Its promotion to a global near-prime-core closure is
not.

## 1. Valid local theorem

For fixed reduced cores `c,d`, least primes `ell=P^-(c)`, `rho=P^-(d)`, and
arbitrary Hilbert coefficients on owner products `P<<d`, `Q<<c`, one has

\[
 \sum_{h\ ({\rm mod}\ \ell)}
 \sum_{k\ ({\rm mod}\ \rho)}
 \left\|
 \sum_{P,Q}a_{P,Q}
 e_\ell(-hQd^2)e_\rho(kPc^2)
 \right\|^2
 \ll CD\sum_{P,Q}\|a_{P,Q}\|^2
\tag{R-106123.1}
\]

on `c~C`, `d~D`.  For the literal source coefficients this pays one fixed
core fibre after its source-dual weight is inserted.

## 2. First false promotion

The first `L-106123` then counted the number of cores inside one fixed
`(ell,rho,C,D)` block and observed that

\[
 {C\over\ell}{D\over\rho}=X^{o(1)}
\]

makes that individual block inexpensive.  It omitted the positive sum over
all possible least-prime conductor pairs `(ell,rho)`.

There can be power-many such blocks even when every block contains exactly one
core pair.

## 3. Exact counterfixture

Take reduced cores which are themselves prime:

\[
 c=\ell\in[C,2C),
 \qquad
 d=\rho\in[D,2D).
\]

Then for every conductor pair

\[
 {C\over\ell}{D\over\rho}\asymp1.
\]

Thus each individual block satisfies the proposed near-prime condition with
maximum margin.  Nevertheless the number of conductor pairs is

\[
 \pi(2C)-\pi(C)
 \quad\times\quad
 \pi(2D)-\pi(D),
\]

which is power-sized.

The fixed-core bound (R-106123.1) may cost a constant for each pair.  Summing
those positive constants over all `(ell,rho)` is not subpower.  The reciprocal
source-dual mass used to dominate the original coherent current does not
bound the positive moment itself.

This is the same structural distinction as the earlier firewalls:

```text
local fibre estimate                        valid;
positive sum of all fibres                   separate theorem;
coherent source before squaring              not interchangeable with either.
```

## 4. Correct weighted expression

Keeping the least-prime weights rather than replacing them by `ell<=c` and
`rho<=d`, the local bound contributes on the scale

\[
 {\ell\rho\over CD}
\]

per fixed core pair, before the remaining owner/core incidence factors.  A
block with about

\[
 {C\over\ell}{D\over\rho}
\]

core pairs can therefore still contribute at least its conductor-family
multiplicity after a source-blind Cauchy step.  No pointwise condition on one
block controls the global sum over conductors.

## 5. Binding consequence

```text
fixed-core two-dimensional additive large sieve       RETAINED
literal local source normalization                     RETAINED
first L-106123 global near-prime closure               RETRACTED
first BTRC106123 rough-cofactor-only frontier           RETRACTED
T-106120 bilateral tensor moment                       RETAINED / OPEN
BTPP/BTPN/BTNN                                         RETAINED / OPEN
```

The corrected remaining issue is a **varying-conductor family moment** across
`ell` and `rho`, not merely rough-cofactor multiplicity inside one conductor
block.

A valid repair must use at least one of:

```text
large sieve or trace formula across the conductor family itself;
a source-faithful conductor amplifier before squaring;
Frobenius/monodromy cancellation across varying irreducible conductors;
a signed principal-channel theorem which does not replace the coherent source
by a positive sum of local fibres.
```

## Scope

This refutation does not alter the bilateral source partition, tensor Gauss
identity, source-dual conditional implication, atomic diagonal, prime-Wick
factorization, or function-field prime-shell theorem.  It prevents the local
large sieve from being mislabeled as global closure.
