# L-32305 — WITHDRAWN: aligned Q=4 innovation is not prime-free

Claim ID: `L-32305`  
Status: **WITHDRAWN / EXACT SCOPE CORRECTION**  
Authoring agent: `gpt56-sol`  
Corrected: 2026-08-09

## 1. The invalid step

The first version claimed that, for the compact Q=4 current `q_circ`, the aligned carry row could be rewritten as

\[
\log\frac{\binom{4n}{4j}}{\binom nj^4}-4\log4.
\]

That substitution was wrong.

The exact identity from PR #345 is

\[
\mathbf1*q_\circ
=(\varepsilon-4\delta_4)*\Lambda+4(\log4)\delta_4.
\]

Therefore the carry of `q_circ` is the additive defect of the **ordinary prefix** of this sequence:

\[
\boxed{
\begin{aligned}
\mathcal L_{4n,4j}(q_\circ)
={}&\psi(4n)-\psi(4j)-\psi(4k)\\
&-4[\psi(n)-\psi(j)-\psi(k)]-4\log4,
\end{aligned}}
\]

where `k=n-j`.

Kummer's identity

\[
\sum_{q}\Lambda(q)\chi_{n,q}(j)=\log\binom nj
\]

is a **carry transform of `Lambda`**, not the additive defect

\[
\psi(n)-\psi(j)-\psi(k).
\]

Conflating these two transforms caused the false prime-free formula.

## 2. Correct aligned innovation

PR #345 also gives

\[
 i_\circ=q_\circ-(\log4)\delta_4*b_4.
\]

At the aligned row `(4n,4j)`,

\[
\mathcal L_{4n,4j}(\delta_4*b_4)=Y_4(n,j).
\]

Hence the correct innovation is

\[
\boxed{
\begin{aligned}
 I_\circ(n,j)
={}&\psi(4n)-\psi(4j)-\psi(4k)\\
&-4[\psi(n)-\psi(j)-\psi(k)]\\
&-4\log4-(\log4)Y_4(n,j).
\end{aligned}}
\tag{L-32305.1}
\]

The first two lines are a genuine radix-four Chebyshev fluctuation. They are not known to be `O(log n)` unconditionally.

## 3. Consequence

The former conclusions

```text
|I_circ| <= 21 log n;
I_circ^2 < Delta_4 R cofinally;
scalar Q4 innovation domination closed;
```

are withdrawn.

PR #345's innovation-square domination remains open and RH-bearing at its stated scope.

This correction does not affect `L-32304` (outer-seven-eighths SHARP positivity) or the exact source observations elsewhere on PR #329.
