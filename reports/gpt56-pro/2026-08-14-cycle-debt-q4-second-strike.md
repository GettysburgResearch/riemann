# Second strike: fail-closed Cycle-Debt certificates and distinct-prime Q4 correlation

Status: **PROPOSED REVIEWABLE MATHEMATICS — INDEPENDENT REVIEW REQUIRED**  
Parent PR: `#474`  
Parent head: `1ad91b5ccc5af5616c26ad6a830d6d75d8182a02`  
Branch: `agent/91701-q4-cycle-debt-control`  
Scientific verdict: **RH remains unproved.**

## 1. Purpose

The first packet on PR #474 changed both dormant routes from broad architecture
to exact finite closure interfaces:

```text
Cycle Debt:
full signed LP = two positive Markov channels + Bellman certificate;

Q4:
complete endpoint positive energy has a direct zero-safe Mellin consumer.
```

This continuation attacks the next obstruction on each route rather than adding
another equivalent criterion.

## 2. Cycle Debt — the actual irrational LP is now fail-closed

The action/source matrix is rational, but the true capacity cost

\[
 c_e=\omega_e/n
\]

contains square roots. `L-93012` proves that exact rational source masses and a
rational potential can be combined with directed rational enclosures

\[
 c_e^-\le c_e\le c_e^+
\]

to produce a rigorous bracket

\[
 D\le\mathfrak N(s)\le C^+.
\]

The complete width has the exact nonnegative decomposition

\[
\begin{aligned}
C^+-D={}&\sum_ex_e^+\Delta_f(e)
 +\sum_ex_e^-(c_e^- -\Delta_f(e))\\
&+\sum_ex_e^-(c_e^+-c_e^-).
\end{aligned}
\]

Thus a certificate cannot hide:

- positive-support Bellman error;
- negative-support Bellman error;
- unresolved irrational-capacity width.

If the gap is \(\varepsilon\), mass outside any \(\eta\)-contact set is at most
\(\varepsilon/\eta\). Near-optimal solutions are therefore forced onto the
lower and upper Bellman contact graphs quantitatively.

A minimal-support argument also proves that some exact optimum uses at most
\(\operatorname{rank}A\le X-1\) signed action columns globally. Since the
source matrix is rational, those optimal action masses are rational despite the
irrational objective. Only objective selection and certification require
square-root intervals.

This gives a concrete proof-producing campaign:

```text
exact rational source equation;
O(X) signed action columns;
rational dual potential;
directed lower/upper capacity intervals;
exact gap and contact certificate.
```

The packet does not construct these certificates for the critical Möbius source
cofinally.

## 3. Q4 — all one-prime Euler self-correlation is removed

The hard Q4 block increment has five channels

\[
 b(a)=\sum_{r=0}^4\kappa_r\Lambda(\Phi_r(a)),
 \qquad
 \kappa=(1,1,1,1,-4).
\]

`L-93013` expands both exact quadratic kernels from the weighted-Goldbach normal
form and partitions every pair according to whether its two prime powers lie on
the same prime tower or on different prime towers.

For either kernel \(W\), the complete same-prime contribution obeys

\[
 |R_W^{\rm same}(n)|
 \le256n^2\log^2(4n).
\]

The proof is elementary. For one prime and channel, the total von-Mangoldt mass
of all selected powers is at most \(\log(4n)\); the absolute channel weight is
eight; and \(\pi(4n)\le4n\).

After both kernels are inserted, the full hard energy differs from the
same-prime-stripped expression by at most

\[
 1024n^2\log^2(4n).
\]

Endpoint completion costs \(O(n^2)\), and the delayed four-adic gauge has only
\(O(n\log^2n)\) square energy. Therefore actual endpoint PIG is equivalent to
a signed normal form whose remaining quadratic pairs come from **different
primes**.

This removes unconditionally:

- equal prime powers;
- different powers of the same prime;
- residue/contracted-channel coincidences;
- every one-prime Euler self-interaction;
- the explicit power-of-two gauge at endpoint-PIG scale.

The large linear terms are deliberately kept coupled to the distinct-prime
quadratic terms. No absolute-value separation is made before the exact Q4
cancellation.

The surviving arithmetic theorem is now precisely a distinct-prime weighted
Goldbach/max-kernel correlation estimate.

## 4. Exact replays

### X-93012

```text
PASS_X_93012_CYCLE_DEBT_DIRECTED_INTERVAL_CERTIFICATE
```

Exact rational checks:

```text
5,516 gap and feasibility identities;
1,644 contact-localization checks;
411 hostile mutations detected.
```

### X-93013

```text
PASS_X_93013_Q4_PRIME_TOWER_EXTRACTION
```

Exact formal checks:

```text
114 five-channel polynomial expansions;
342 same/cross partition identities;
228 tower-envelope checks;
16,268 same-prime/different-power terms retained correctly;
114 equality-only diagonal mutations detected;
114 contracted-coefficient mutations detected.
```

The replays authenticate finite algebra and mutation sensitivity. They do not
prove the cofinal Cycle-Debt bound, the analytic Chebyshev estimate, the
remaining distinct-prime correlation bound, endpoint PIG, or RH.

## 5. New exact frontier

```text
Cycle Debt:
export rank-sparse exact source channels
+ directed capacity intervals
+ a Bellman potential
with C_X^+ = X^{o(1)}.

Q4:
control the coupled distinct-prime max-kernel
+ weighted-Goldbach expression
at n^2 polylog(n) scale.
```

These are genuinely different open theorems. The first is an adaptive finite
control/certification problem; the second is a deterministic correlation theorem
between distinct Euler factors.

## 6. Boundary

```text
directed Cycle-Debt bracket and gap identity      PROPOSED COMPLETE EXACT FINITE
contact localization and rank sparsity            PROPOSED COMPLETE EXACT FINITE
critical cofinal certificate                       OPEN / RH-BEARING

same-prime Q4 tower contribution                   PROPOSED CLOSED UNCONDITIONALLY
distinct-prime Q4 normal form                      PROPOSED COMPLETE EXACT
its n^2 polylog bound                              OPEN / RH-BEARING

Riemann Hypothesis                                 UNPROVEN
```
