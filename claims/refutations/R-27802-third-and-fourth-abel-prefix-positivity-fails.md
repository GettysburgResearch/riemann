# R-27802 — Fixed finite Abel-order producer positivity fails beyond the original scan

Claim ID: `R-27802`  
Title: The third and fourth cumulative producer kernels have exact negative rows, so TACP-I and the fixed-order Abel programme are withdrawn  
Status: **EXACT REFUTATION / SCOPE CORRECTION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Frozen target: PR #279 at `07061d5d76b2cef7b5d9e5748352290a89f914e5`  
Scope: refutes the all-scale kernel sign asserted as `TACP-I`; it does not refute positivity of the actual critical producer

## 1. Exact cumulative targets

For Abel order `r>=1`, endpoint `Q`, and columns `2<=q<=Q`, put

\[
w_Q^{(r)}(q)=\binom{Q-q+r-1}{r-1}.
\]

Apply the exact multiple-Möbius transform and the frozen half-binary/half-ternary descending recurrence of `L-23811`. Denote the resulting coefficient by `A_Q^{(r)}(n)`.

The earlier branch had already certified

```text
order 1: generic kernel witness        K_8(3,4)=-1
order 2: X=60,Q=59,n=11                A=-13/16
```

but finite reconnaissance through `Q,n<=80` found no order-three failure.

## 2. Exact order-three counterexample

At

\[
X=Q=520,\qquad n=15,
\]

integer Möbius inversion followed by exact dyadic `Fraction` recurrence gives

\[
\boxed{A_{520}^{(3)}(15)=-\frac{91}{256}<0.}
\]

Therefore the proposed theorem

```text
S_X(n,Q)>=0 for every X,n,Q
```

is false. The failure occurs in the interior cumulative kernel, not merely in the source zero-extension collar.

## 3. Exact order-four counterexample

The next cumulative order also fails. At

\[
X=Q=8000,\qquad n=23,
\]

one obtains exactly

\[
\boxed{A_{8000}^{(4)}(23)
=-\frac{1168054960769}{4096}<0.}
\]

Thus increasing the fixed Abel order once more does not repair the mechanism.

## 4. Disposition

```text
complete monotonicity of q^(-1/2)log(X/q)    RETAINED
finite Abel summation identities              RETAINED
TACP-I all-scale third-prefix positivity      REFUTED
TACP-B as a completion of TACP-I              MOOT
T-27801 as a full conditional proposal        WITHDRAWN
actual critical producer positivity           OPEN / NOT DISPROVED
```

The exact lesson is global: no proof should take a sign after any presently tested fixed number of source-independent cumulative integrations. The higher generations must be recombined through the full fragmentation ancestry before a sign is taken.

## 5. Replacement direction

The durable replacement is the size-biased fragmentation-spine formulation:

```text
complete Möbius node source
-> conservative Markov ancestry
-> first-entrance recombination of every higher generation
-> one finite-ratio transition source
-> nonnegative exact balanced flow
-> sharp prime ramp
-> RH.
```

This is developed on the successor research branch rather than being retrofitted into the failed TACP theorem.

## 6. Mandatory mutations

Every future producer proof must reproduce all four exact failures:

```text
K_8(3,4)                              = -1
A_59^(2)(11)                          = -13/16
A_520^(3)(15)                         = -91/256
A_8000^(4)(23)                        = -1168054960769/4096
```

A theorem implying any of these quantities is nonnegative has again replaced the critical source by a false ambient positivity surrogate.
