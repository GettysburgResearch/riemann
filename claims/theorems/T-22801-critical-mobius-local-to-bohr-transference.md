# T-22801 — Critical Möbius local-to-Bohr transference

Claim ID: `T-22801`  
Title: The complete analytic-totient packet has physical critical energy bounded by its positive Jordan Bohr energy up to a subpower factor  
Status: **REJECTED AS STATED — UNIFORM OPERATOR STEP REFUTED BY R-22802**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Corrected: 2026-08-07  
Issue: #228

## Original target

For the completed packet `mathscr C_D` and the exact Jordan Bohr energy `mathcal B_D`, the desired estimate is

\[
\boxed{
\int_{D/2}^{D}|\mathscr C_D(x)|^2dx
\ll_\varepsilon
D^{1+\varepsilon}(1+\mathcal B_D).}
\tag{T-22801.1}
\]

Together with `mathcal B_D<<D`, this would give the critical analytic-totient second moment and RH through `T-9506`.

## Refuted proof step

The first version attempted to prove (T-22801.1) through a uniform cluster operator bound

\[
\|\widetilde{\mathcal R}_{D,1}\|_{2\to2}^2
\ll_\varepsilon D^\varepsilon.
\tag{T-22801.2}
\]

`R-22802` gives an exact counterargument. For any fixed positive cell index `k`, the numerator `a=1` contributes an entry at least one for a positive proportion of the denominators `q`. Hence that row has Euclidean norm `gg sqrt(D)`, and the operator norm cannot be subpower. Modifying any fixed finite set of low rows does not repair the claim.

Therefore the determinant and divisor-Hilbert argument in the frozen first version does not prove (T-22801.1).

## What remains plausible

The counterexample uses arbitrary vectors in the divisor-coordinate space. The actual vectors are highly special:

\[
U_q(D)=\sum_{q\mid d\le D}\frac{\mu(d)}d,
\qquad
V_q(D)=\sum_{q\mid d\le D}\frac{\mu(d)}{d^2}.
\]

The exact finite data continue to suggest the scalar estimate

\[
\boxed{
\int_{D/2}^{D}|\mathscr C_D(x)|^2dx
\ll_\varepsilon
D^{1+\varepsilon}(1+\mathcal B_D),}
\tag{T-22801.3}
\]

but a valid proof must exploit the Möbius signs and the coupling of `U_q,V_q` to the completed endpoint channel **before** Cauchy–Schwarz. A uniform operator theorem cannot supply that cancellation.

The repaired open statement is recorded separately as `T-22803`.

## Status boundary

```text
exact completed packet algebra       retained
exact Jordan Bohr factorization      retained
small-D exact regression             retained
uniform cluster operator proof       refuted
scalar Möbius contraction            open
proposed RH proof T-22802             gap/blocked
RH                                   unproved
```

The original proof remains visible in Git history for review, but it must not be cited as a valid theorem.