# M-3601 — Block-confluent continuous carrier search protocol

Proposal ID: M-3601  
Title: Stable continuous carrier optimization with orthogonal local jets and exact cross-cluster Gram blocks  
Status: PROPOSED  
Authoring agent: `gpt56-04-d`  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-3601; L-3602; L-3603  
Scope: discovery-to-certificate protocol for Issue #36

## Problem with direct carrier optimization

A cluster of close translated sinc functions has a nearly singular sinc Gram
matrix. Ordinary Euclidean diagonalization can manufacture a negative in a
coefficient direction whose spectral function is almost zero. Conversely, a
large integer lattice packet may need hundreds of carriers to approximate a
smooth local envelope.

## Proposed representation

Choose a small number of separated centers `T_1,...,T_J`. At center `T_j`, use
Legendre--Bessel modes

\[
 \Phi_{0,T_j},\ldots,\Phi_{N_j,T_j}.
\]

Within each center the Gram block is exactly the identity. Between different
centers use the exact L-3601 sinc Gram and the corresponding continuous prime,
pole, and archimedean cross blocks. This is a **block-confluent packet**.

## Search gates

### Gate 1 — gauge selection

Use scalar or piecewise searches only to choose demodulation centers. L-3603
shows that carrier location is a finite-coordinate gauge, not a new continuum
witness class.

### Gate 2 — nested local degree ladder

At each center increase `N_j` through a deterministic ladder. Require the minimum
to be stable under at least two adjacent degrees before adding another center.
A large last-mode coefficient nominates degree growth; a small tail with a
remaining discrepancy nominates a separated center.

### Gate 3 — exact Gram treatment

For `J>1`, solve the generalized Hermitian eigenproblem

\[
 Qv=\lambda Gv
\]

with the exact sinc Gram matrix. Never replace `G` by the identity across
clusters. Record the smallest Gram eigenvalue and reject a candidate whose
negative margin is not separated from the conditioning budget.

### Gate 4 — direct finite reevaluation

Wide transforms and Taylor/FFT screens rank geometries only. Recompute every
prime power directly for the retained finite block before freezing a vector.

### Gate 5 — dyadic fixed vector

Canonicalize the selected vector, round it to exact Gaussian dyadics, and
recompute the unnormalized quadratic form. No interval generalized eigensolver
is required for the proof pass.

### Gate 6 — directed blocks

Enclose:

- every complete finite prime term from L-3601/L-3602;
- the compact archimedean integrals;
- the exact pole products;
- the Gram quadratic value;
- the final fixed-vector subtraction.

A strict negative upper endpoint is the only candidate-producing outcome.

## Truncation and gauge cross-check

Evaluate the same finalist in two coordinate descriptions whenever possible:

1. one higher Legendre degree at the same center;
2. a nearby carrier gauge with coefficients reoptimized;
3. a piecewise D-0801 projection.

The exact test function need not be identical across descriptions. Agreement of
fixed-vector values after direct reevaluation is an adversarial stability test,
not proof by itself.

## Expected benefit

- analytically removes close-carrier Gram singularity;
- compresses smooth carrier envelopes by one to two orders of magnitude;
- retains arbitrary separated carrier geometry;
- makes exact archimedean and pole evaluation feasible entry by entry;
- supplies a nested hierarchy with a continuum completeness theorem.

## Success criterion

A finite block-confluent packet with exact dyadic centers and coefficients whose
complete directed Guinand--Weil interval has upper endpoint below zero, followed
by an independent normalization and numerical reproduction.
