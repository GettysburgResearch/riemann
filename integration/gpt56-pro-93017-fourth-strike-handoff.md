# GPT-5.6 Pro handoff: bottom-free Cycle Debt and scalar Q4

Date: 2026-08-15  
Target: draft PR #474  
Branch: `agent/91701-q4-cycle-debt-control`  
Frozen parent: `0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b`

**The Riemann Hypothesis remains unproved.**

## What this packet adds

Cycle Debt is rewritten in the triangular carry basis. For the critical target,
its exact asymmetric dual becomes

```text
N_X = max <ell_X,psi>
      subject to -W <= A psi <= 0.
```

The split `2=1+1` forces `-1 <= psi(2) <= 0`, so the bottom coordinate is
nonpositive in the objective. At `X=2Y` this gives

```text
N_(2Y) <= (1/2) N_Y + B_(2Y)
```

with no additive logarithmic bottom payment. The remaining theorem is
One-sided Parity Borrowing (`OPB`): `B_(2Y) <= polylog(Y)`.

For Q4, the endpoint mean

```text
M(N) = C(N) - (2/N) sum_(j<N) C(j)
```

has an exact finite backward inverse with one boundary term. The actual compact
Q4 prefix satisfies `C_circ(N)=o(N)` by the prime number theorem, so

```text
C_circ(N)
 = M_circ(N)
   - 2(N+1) sum_(k>=N) M_circ(k)/((k+1)(k+2)).
```

Thus a square-root/polylog bound for the single mean reconstructs every prefix,
every complete endpoint row, and the full PIG energy without a separate
major-arc theorem. Conversely, the existing variance identity gives
`|M_circ(N)|^2 <= N P_circ(N)`. Hence, subject to independent review of the
frozen Mellin consumer,

```text
RH
<=> |M_circ(N)| <= sqrt(N) log^A N for some fixed A
<=> P_circ(N) <= log^B N for some fixed B.
```

The scale-four source bridge is exact:

```text
A4(s) = (1-4^(1-s))/((1-4^(-s)) zeta(s)),
sum c_circ(n)n^(-s) = (1-4^(1-s)) A4'(s)/A4(s),
c_circ * a4 = -(epsilon-4 delta_4) * (a4 log).
```

This is a source dictionary, not yet a positive or capacity-faithful transfer.

## Live overlap

PR #483 at `87bd7ad2127f98b6141b4c03355556f2b95f6404` supplies the complete
prime-base Q4 Gram and First-Hermite coherence. This packet does not duplicate
its claims. The latest visible factor-67 work is intentionally not imported.

## Exact replays

```text
PASS_X_93017_CYCLE_DEBT_CARRY_DISCREPANCY
PASS_X_93018_Q4_HARDY_LOGDERIVATIVE
```

The checks use exact rational arithmetic and formal prime-log coefficient maps.
They do not run broad LP, prime, or zero scans and do not prove OPB, the Q4 mean
bound, or RH.

## Review order

1. `L-93017`, then `X-93017`.
2. `R-93020` before any infinite Hardy inversion.
3. `L-93018`, `T-93011`, then `X-93018`.
4. `L-93019` and `O-93017`.
5. Source lock, report, and content ledger.

## Exact open gates

```text
Cycle Debt: OPB, B_(2Y) <= polylog(Y).
Q4: M_circ(N) = O(sqrt(N) log^A N).
Cross route: a capacity-faithful logarithmic-derivative transfer.
RH: UNPROVEN.
```
