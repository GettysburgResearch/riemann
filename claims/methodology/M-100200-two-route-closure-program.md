# M-100200 — Hostile next-step program for the two terminal routes

## Route A: PCRP100200

1. Freeze the exact outside-core decomposition before any phase averaging.
2. Use the priority-Hasse flow only for edge boundaries.
3. Retain every cube-root residual with its outside-core parity.
4. Partition roots by first differing prime and by a fixed product-ratio shell.
5. Apply the phase factor \(1-p^{i\gamma}\) before equal products collapse.
6. Prove a support-shifted Cauchy/Carleson estimate for the root packet.
7. A generic \(L^2\) bound without the physical half-order shift is insufficient.

Two concrete attacks:

```text
A1. node-split phase flow:
    pair opposite root parities across one-prime Hasse edges and use the
    exact Cauchy edge energy.

A2. first-owner near-collision:
    retain the native Littlewood-Paley owner, remove far-product pairs
    exactly, and estimate only the compact multiplicative near-collision Gram.
```

## Route B: BVD100210

1. Keep the extra notch; without its true half-order zero, Type I has a
   square-root main term.
2. Use \(U=X^{1/3}\) or optimize \(U\) only after retaining the exact
   \(a_U*a_U*\mu\) source.
3. Decompose \(r,s\) into product-ratio boxes.
4. Preserve the signs in \(a_U\); source-blind Hilbert or large-sieve norms
   reproduce the known square-root barrier.
5. Exploit that \(m\ll X^{1/3}\) and \(r,s>X^{1/3}\).

Two concrete attacks:

```text
B1. additive-modulus dispersion:
    open the product window by a smooth Fourier integral, apply divisor
    switching to a_U, and seek cancellation in shifted congruence classes.

B2. multiplicative phase dispersion:
    Mellin-decompose the compact product kernel and combine the two a_U
    polynomials before Cauchy, retaining the reciprocal-Mobius phase.
```

## Rejection criteria

A successor is not a closure if it:

- bounds only a diagonal or an absolute coefficient sum;
- omits the phase-Hasse root residual;
- uses the un-notched \(K_0\) Type-I sum as though its half-order moment
  vanished;
- replaces \(a_U\) by a divisor bound;
- imports an estimate already equivalent to RH without proving it.
