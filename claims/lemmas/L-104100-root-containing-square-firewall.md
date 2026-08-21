# L-104100: root-containing positive squares do not control their root by excess alone

Claim ID: `L-104100`  
Status: **PROVED EXACT**  
Created: 2026-08-21  
RH status: **unproved**

Let `H` be a real or complex Hilbert space, let `g in H`, and let `E>=0`.
Suppose

```text
Q = ||g||^2 + E.
```

## Statement

No bound on `E` alone implies a bound on `||g||` over the class of all such
triples.  In particular, even the strongest excess estimate `E=0` permits an
arbitrary root.

## Proof

For any prescribed `M>=0`, take `g` with `||g||=M` and take `E=0`.  Then

```text
Q=M^2,
Q-||g||^2=0.
```

Thus the excess is identically zero while the root is arbitrary.

## Implication-matrix use

Hardy-tail, divisor-GCD, Poisson and owner-square coordinates may be valuable
because they expose different nonnegative excesses.  If the complete positive
form retains the critical detector as its root term, estimating only the
excess is not a closure theorem.  A separate strict return inequality is
required.
