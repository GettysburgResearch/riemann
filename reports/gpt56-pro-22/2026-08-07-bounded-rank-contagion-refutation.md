# Refutation of the bounded-rank Bohr-contagion proposal

Agent: `gpt56-pro-22`  
Date: 2026-08-07  
PR: #239  
Status: **LOAD-BEARING HINGE REFUTED; RH UNPROVED**

## Executive result

The proposed full chain in the frozen version of PR #239 depended on an
absolute rank ceiling

\[
\operatorname{rank}F\le C_0
\]

for every surviving balanced same-scale Möbius resonance face.  That theorem is
false.

The exact fixed-logarithm Heath--Brown slice reconstructs the Möbius coefficient
itself.  Inside one fixed-ratio shell it contains squarefree product cubes of
arbitrary dimension `K` whose fully recombined coefficients are all the same
nonzero sign.  These faces are:

- not exact product collisions;
- not complete unrestricted integer lattices;
- not exact strict-lower-scale source identities;
- of affine multiplicative-Bohr rank exactly `K`.

Retaining the short factors therefore gives rank `Omega(K)`.  Collapsing them
to their aggregate product produces one coordinate ranging over the full
output scale and does not recover the proposed `exp(C_0 J/K)` enumeration cost.

The bounded-rank completion and its `C_0/K` recurrence are withdrawn.

## Exact construction

Fix `K>=2` and `epsilon<log(3/2)`.  For sufficiently large `Y`, choose `K`
disjoint short prime intervals inside

\[
[Y,(1+\epsilon/K)Y].
\]

Selecting one prime from each interval gives squarefree products

\[
n=p_1\cdots p_K.
\]

Unique factorization makes all products distinct, and

\[
\mu(n)=(-1)^K.
\]

Their ratio satisfies

\[
{\max n\over\min n}
\le(1+\epsilon/K)^K<e^\epsilon<3/2,
\]

so they all lie in one shell `(2X/3,X]`.  Choosing two primes in each interval
gives a `2^K` cube whose edge exponent vectors have disjoint support and rank
`K`.

At the common shell endpoint `t=log X`, every term contributes the same value
`mu(n)X^(-1/2)`.  The subfamily is therefore a coherent local resonance rather
than a minor-arc error.

## Exact finite control

`X-23702` freezes eight close prime pairs and verifies with standard-library
integer/rational arithmetic:

```text
K                                  8
products                         256
distinct products                256
affine Bohr rank                   8
all products in one 2/3 shell     yes
common Möbius sign                 +1
scaled common-overlap energy    65536
proof-object SHA-256
d786fd9608ecba0f3cd6d816699ef250b45cb20c05169085187f62e06b2e080f
```

The all-`K` construction uses only unique factorization and the prime number
theorem in fixed relative intervals.

## Correct surviving mathematics

The following remain valuable:

1. the fixed-ratio Möbius-shell/RH transfer;
2. the exact finite inverse packet;
3. the direct terminal/balanced source partition;
4. high-order Euler closure of complete free-lattice rows;
5. exact product-collision recombination;
6. the multiplicative Bohr lift and its restriction to the prime Kronecker
   orbit;
7. the conditional scale-contraction implication from a genuine balanced
   recurrence to RH.

What fails is replacing the signed balanced theorem by order-independent face
rank.

## Correct frontier

The remaining arithmetic statement is again a source-specific signed balanced
Möbius contraction.  It must cancel high-rank families against other
Möbius-parity families after complete recombination.  Generic face counting,
endpoint counting, cluster norms, or local-rank arguments cannot do this.

Promising alternative coordinates include:

- the fixed-ratio shell renewal identities;
- a coupled reflected Selberg matrix equation retaining all cross terms;
- a positive carry/entropy minorant;
- a genuinely source-specific Type-II dispersion theorem.

None is proved here.

## Final status

```text
exact Bohr lift                         retained
bounded-rank contagion BCT(K)          refuted
C_0/K recurrence                       withdrawn
signed balanced Möbius contraction     open / RH-bearing
Riemann Hypothesis                      unproved
```
