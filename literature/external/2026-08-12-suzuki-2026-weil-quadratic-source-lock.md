# Suzuki 2026 localized Weil-operator source lock — 2026-08-12

## Primary source

Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:`2606.09096v1`, submitted 2026-06-08.

## Imported statements

The local packet imports only the following claims from the primary source.

1. The localized Weil form `Q_W^a` on `L^2(-a,a)` is represented by a canonical densely defined self-adjoint operator `A_a`.
2. If `G_a` is the localized continuous screw-kernel operator and `D=i d/dx` with Dirichlet domain, then
   ```text
   B_a=D* G_a D
   ```
   is symmetric and `A_a` is its Friedrichs extension (Suzuki Theorem 1.1).
3. The spectrum of `A_a` is discrete and bounded below; its lowest eigenvalue is
   ```text
   lambda_a=inf Q_W^a(v)/||v||_2^2.
   ```
4. The function `a -> lambda_a` is continuous (Suzuki Theorem 1.3).
5. `lambda_a>0` for sufficiently small `a`, with an explicit logarithmic asymptotic; if RH is false, there exists an `a` with `lambda_a<0`, and continuity forces a degenerate localized form at some intermediate scale.
6. For every `lambda<lambda_a`, the shifted form
   ```text
   Q_W^a(v)-lambda||v||_2^2
   ```
   defines a positive Hilbert norm, in which the first-order differential operator has self-adjoint extensions with real spectra.
7. The paper formulates, but does not prove, a global limiting spectral conjecture as `a -> infinity`.

## Relevance to the present branch

The delayed fixed-scale synthesis operator of `L-91034/T-91008` produces a family of vectors in the Weil form domain.  Its full Gram is

```text
(A_a^del)* Q_W A_a^del.
```

Suzuki's theorem supplies an explicit localized self-adjoint realization of the same form after support localization.  It does not supply its nonnegativity.

The shifted Hilbert construction is not a proof of the desired embedding: choosing `lambda<lambda_a` makes the form positive by definition, while the RH-bearing statement is precisely

```text
lambda_a>=0 for every a>0.
```

Thus an argument that embeds the prime output only after inserting an unknown negative spectral shift has not completed CDFHGI.

## No status transfer

The following are local and are not imported from Suzuki 2026:

- the scalar Cauchy mother and its refutation;
- the delay-fibre form-core repair;
- the Jordan Fock product system;
- the first-chaos reduction;
- the full delayed source-to-Hardy Gram factorization;
- any proof of RH.

## Exact boundary

```text
localized Weil self-adjoint operator          IMPORTED PROVED
continuity of the lowest eigenvalue            IMPORTED PROVED
positive shifted Hilbert realization           IMPORTED PROVED
unshifted lambda_a>=0 for every a               OPEN / RH-EQUIVALENT
CDFHGI source-ordered full-Gram factorization   OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```
