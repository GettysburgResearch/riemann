# M-105646 — Hostile review contract for critical-height majorization

Claim ID: `M-105646`  
Created: 2026-08-25  
RH status: **unproved**

A reviewer should reconstruct the following interfaces independently.

## A. Compression identity

1. Verify that the compression of `diag(rho_1,...,rho_n)` to the orthogonal
   complement of the uniform vector has characteristic polynomial `p'/n`.
2. Include repeated roots and algebraic multiplicities.

## B. Majorization

1. In a unitary Schur form of the compression, verify that the diagonal of its
   Hermitian imaginary part is exactly the vector of critical-point heights.
2. Reprove the Schur--Horn/Jensen step.
3. Reprove codimension-one Cauchy interlacing for the compression of the
   diagonal parent-height matrix.
4. Check that nonnegativity and monotonicity of the convex test function are
   used only in the final interlacing comparison.

## C. Xi statement-to-use

1. Distinguish a finite canonical packet from the complete entire Xi function.
2. Retain omitted-zero, horizontal-endpoint and canonical exponential terms in
   every cofinal limit.
3. Confirm that the theorem controls penetration moments, not the number of
   arbitrarily shallow zeros.
4. Confirm that scalar addition is not used for nonorthogonal model-space
   factors.
5. Verify the current-charge coefficient `2h/(b+h)^2` against `L-105641`.

## D. Falsifiers

The claim is falsified by any finite polynomial and level `H` for which

```text
sum_(p'(c)=0) (Im c-H)_+^q
>
sum_(p(rho)=0) (Im rho-H)_+^q
```

for one `q>=1`, or by an error in the root-compression characteristic
polynomial.  A cofinal Xi endpoint failure would not refute the finite theorem;
it would refute only its attempted transfer.
