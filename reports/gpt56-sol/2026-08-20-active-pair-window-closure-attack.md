# Active-pair / ratio-67 window closure attack

Base: PR #659 `83c17b32a99ac9e1aa5aec3168535550eb286636`  
Branch: `research/gpt56-sol/99810-reversible-network-bellman`  
RH status: **unproved**

## Executive result

The attempt to close the remaining owner-Carleson/min-cut gate produced a sharper structural reduction.

The normalized zero-free SHARP box potential has the form

```text
0                                           below activation;
8+(-8-3u)e^(-u/2)                           in the collar;
8(1-67^-1/2)-3 log(67)e^(-u/2)              in the deep region.
```

Weighted rough Euler shifts act triangularly on this three-dimensional basis. This yields:

- exact positivity of every active weighted two-prime Euler block;
- exact annihilation of the nonconstant half-order modes in any uniform regime;
- exact positivity of every fully active top-collar `k`-prime cube;
- exact silence of inactive rough primes;
- exact identification of the only remaining many-prime collar slope with a ratio-67 Möbius window.

The last identity is

\[
c_P(u)=-3\sum_{e^u/67<n\le e^u}\mu(n)
\]

on the active squarefree rough source (with the finite decorated source understood at the canonical scope).

## Hostile corrections retained

The pass explicitly rejected the following tempting but invalid implications:

1. polylog labelled Littlewood--Paley energy -> physical scalar by Cauchy--Schwarz;
2. endpoint moment cancellation -> Poisson off-diagonal cancellation;
3. positive local network energy -> source orientation;
4. uniform unweighted Cheeger at activation boundary;
5. parent-only Kraft injection across all future primes;
6. unweighted global submodularity of the box kernel;
7. pairwise positivity -> many-prime positivity without a composition theorem.

A draft transition-pattern argument was corrected before use; the formal `(2,2,1,0)` pattern occurs only as a pre-activation left limit and is not a live active cube.

## Current shortest path

```text
ratio-67 Möbius-window one-sided negative-mass estimate
    -> compact zero-safe box negative mass = X^o(1)
    -> PR #653 one-sided Mellin/Landau theorem
    -> RH.
```

No unconditional proof of the final window estimate was found in this pass. Any source-blind `L2` estimate strong enough to imply it would already encode RH-scale cancellation and is not imported.
