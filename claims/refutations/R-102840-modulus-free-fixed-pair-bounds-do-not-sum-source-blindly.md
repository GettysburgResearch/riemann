# R-102840 — Modulus-free fixed-pair bounds do not sum coherently source-blindly

Claim ID: `R-102840`  
Status: **PROVED SOURCE-BLIND COHERENCE COUNTERMODEL**  
Created: 2026-08-24  
Depends on: `L-102863--L-102864`  
RH status: **not assumed**

The fixed-quadruple estimate in `L-102864` is dimension-free in the doubly
long regime. This does not by itself control the coherent sum over owner
quadruples.

Let `phi` be a nonzero vector in a Hilbert space and let

\[
F_j=\phi,
\qquad 1\le j\le N.
\]

Every individual packet obeys

\[
\|F_j\|^2=\|\phi\|^2.
\]

But the coherent physical sum satisfies

\[
\boxed{
\left\|\sum_{j=1}^N F_j\right\|^2
=N^2\|\phi\|^2.
}
\tag{R-102840.1}

The sum of the individual energies is only

\[
N\|\phi\|^2.
\]

Thus a uniform `O(1)` bound for each normalized owner quadruple can lose an
arbitrary factor `N` under source-blind coherent collapse.

The same fixture can be realized with distinct logarithmic shifts converging
to zero, so compact translation geometry does not remove it.

## Meaning

`L-102864` removes the explicit owner and modulus powers. The final theorem
must still use at least one of:

```text
literal semiprime-squareclass signs;
large-sieve orthogonality across owner moduli;
largest-discrepancy transport;
source-faithful cancellation between owner ranges.
```

The fixture is not arithmetic and does not refute the balanced squareclass
statement `BQSP102870`. It prevents the fixed-pair theorem from being promoted
to a global proof without a coherent-summation argument.