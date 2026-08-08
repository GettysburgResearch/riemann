# M-28001 — Global first-entrance review protocol

Claim ID: `M-28001`  
Status: **METHODOLOGY / FAIL-CLOSED REVIEW PROTOCOL**  
Created: 2026-08-08  
Target: `L-28001`--`T-28001`

## Review objective

Audit the full chain

```text
critical Möbius divergence
-> exact sibling-coupled size-biased ancestry
-> complete first-entrance source
-> GFEP
-> nonnegative balanced flow
-> sharp prime ramp
-> RH.
```

The central rule is: **all ancestors above the transition band must be recombined before any sign or norm is taken.**

## Exact algebra gates

1. Reconstruct the multiple-Möbius divergence `R_X` at the exact endpoint.
2. Count repeated binary or ternary central children twice.
3. Verify
   ```text
   Q(m,n)=n/(2m) * child multiplicity
   ```
   and `sum_n Q(m,n)=1` exactly.
4. Verify the conservative equation for `B(n)=nA(n)`.
5. Reconstruct the hitting Green formula.
6. Reconstruct the cut/flux identity.
7. For each `n`, retain paths that first enter below `2n` but skip below `n`; they contribute zero, not an omitted positive term.
8. Verify the strong-Markov first-entrance formula.

## Source gates

- `L-28002` may use only `mu(1),...,mu(4)` on the top fifth.
- Check continuity at every reciprocal boundary.
- Reproduce the exact rational interval certificate
  ```text
  C_3(log 5)>1/25.
  ```
- Do not promote the observed negative sign below `X/5`; it is not proved.

## Dual geometry gates

For `L-28003`:

- every tree split must lie in `[1/4,3/4]`;
- the near-halving partition must create exactly a power-of-two number of near-equal blocks;
- every final block must lie in `[2m,4m]`;
- the marked-leaf count must satisfy `k>=n/(4m)`;
- no claim stronger than the factor-four normalized inequality is inherited.

## Frozen counterexamples

Every implementation must reproduce:

```text
K_8(3,4)                              = -1
A_59^(2)(11)                          = -13/16
A_520^(3)(15)                         = -91/256
A_8000^(4)(23)                        = -1168054960769/4096
```

A proof implying any of these is nonnegative has reverted to a false fixed-order smoothing theorem.

## GFEP proof-object requirements

A production object must emit, for every recursive transition family:

- exact source endpoints and Möbius quotient cells;
- exact entrance probabilities or a rational equivalent flow;
- every sibling and skipped path;
- complete transition-band source after recombination;
- lower-scale destinations;
- a strict sign or a quantitative reserve;
- the dyadic/`2/3` Mertens mutation;
- the same-sign Möbius-cube mutation.

If reflected energy is used, include the independent-frequency physical block and every cross term.

## Prohibited shortcuts

Reject:

- total variation of `R_X` before transport;
- unsigned prime or divisor covers;
- a generic positive Markov kernel claim;
- an arbitrary chain not arising from the declared sibling-coupled splits;
- a finite numerical ladder promoted to GFEP;
- assuming WSTS, BTF, producer positivity, or an RH-equivalent scalar as an auxiliary estimate.

## Status vocabulary

```text
finite stochastic/Green identity        exact
finite GFEP reconnaissance               empirical only
GFEP top fifth                           proposed proved via L-28002
GFEP below top fifth                     open
GFEP -> RH                               conditional
RH                                       unproved
```
