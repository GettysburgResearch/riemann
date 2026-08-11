# R-90603 — Untwisted finite stability is not the correct Brownian design target

Claim ID: `R-90603`  
Status: **GENERAL METHOD-CLASS FIREWALL**  
Created: 2026-08-11  
Depends on: `L-90605`, `L-90601`, `L-90603`, `L-90604`

The old finite Brownian programmes asked whether one distinguished approximant was zero-free in the RH-facing half-plane. `L-90605` shows that this is not the invariant question.

For a finite Dirichlet producer, vertical translation explores its complete multiplicative Bohr hull. If any hull member has one zero in the target domain, the untwisted approximant has actual zeros there with positive lower vertical density.

Therefore the following inference is invalid:

```text
untwisted finite scans + local convergence + exact symmetry
-> global finite stability.
```

A replacement producer must prove the much stronger statement

```text
every completely multiplicative unimodular twist
of its leading finite Dirichlet polynomial is zero-free.
```

For the current raw, Nörlund, and Green Brownian producers this complete-hull condition fails by the selected-prime polygon theorem. Functional-equation symmetrisation does not repair it because the reflected Gamma term vanishes in the right half-plane vertical limit.

This firewall does not apply to a genuinely infinite canonical system whose vertical limits are not finite multiplicative tori, nor does it rule out a height-dependent `N=N(T)` theorem with quantitative control varying with `N`. RH remains unproved.
