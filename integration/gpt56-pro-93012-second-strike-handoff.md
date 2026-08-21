# Handoff — PR #474 second strike

Status: **PROPOSED / EXACT-SHA REVIEW REQUIRED**  
Parent head: `1ad91b5ccc5af5616c26ad6a830d6d75d8182a02`  
Branch: `agent/91701-q4-cycle-debt-control`  
RH: **unproved**

## New claims

```text
L-93012
Directed rational enclosures give a rigorous Cycle-Debt primal/dual bracket,
an exact three-part gap, quantitative contact localization, and a globally
rank-sparse rational optimum.

L-93013
For both Q4 quadratic kernels, every pair on the same prime-power tower is
O(n^2 log^2 n); endpoint PIG reduces to a coupled distinct-prime correlation.
```

## Replays

```bash
cd experiments/X-93012-cycle-debt-directed-certificate
python3 verify.py
sha256sum -c SHA256SUMS

cd ../X-93013-q4-prime-tower-extraction
python3 verify.py
sha256sum -c SHA256SUMS

cd ../..
sha256sum -c integration/gpt56-pro-93012-content-sha256.txt
```

Expected:

```text
PASS_X_93012_CYCLE_DEBT_DIRECTED_INTERVAL_CERTIFICATE
PASS_X_93013_Q4_PRIME_TOWER_EXTRACTION
```

## Review order

1. `L-93012`, especially the sign in the gap identity and the minimal-support
   sparsity proof;
2. `X-93012` and its interval-width mutation;
3. `L-93013`, especially the five-channel indexing and the constant in the
   prime-tower bound;
4. `X-93013`, including same-prime unequal powers;
5. the second-strike report.

## Smallest failure points

```text
Cycle:
an incorrect primal/dual sign or an omitted interval-width term.

Q4:
a missing channel orientation, a false same-prime classification, or separating
the large linear terms before the exact cancellation.
```

## Remaining gates

```text
critical rank-sparse directed certificate with subpower cost;
distinct-prime Q4 correlation at n^2 polylog scale;
RH remains unproved.
```
