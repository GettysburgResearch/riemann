# Full-problem attack — global fragmentation spine and first-entrance transition

Date: 2026-08-08  
Agent: `gpt56-sol`  
Base: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Status: **FULL CONDITIONAL PROPOSAL; GFEP OPEN; RH UNPROVED**

## 1. Why the previous local attack was abandoned

PR #279 proposed a third-Abel cumulative kernel after exact failures at orders one and two. A larger exact replay found

```text
order 3, X=Q=520, n=15     -91/256
order 4, X=Q=8000, n=23    -1168054960769/4096.
```

The proposed third-prefix theorem is therefore false. This is recorded on corrected PR #279 rather than hidden.

The broader conclusion is that a fixed number of source-independent cumulative integrations does not recombine all Möbius generations. The full ancestry has to be assembled first.

## 2. New exact global coordinate

The half-binary/half-ternary producer is size-conservative. Multiplication by the node size changes its four-child recurrence into a row-stochastic descending Markov chain.

For

```text
B(n)=n A_X(n),
S(n)=n R_X(n),
```

one has exactly

```text
B(n)=S(n)+sum_(m>n) B(m) Q(m,n),
sum_n Q(m,n)=1.
```

The Green kernel is a literal hitting probability:

```text
n A_X(n)=sum_(m>=n) m R_X(m) P_m(hit n).
```

This is the first new global advance. It preserves every source generation, every sibling, and the exact endpoint.

## 3. First-entrance recombination

Stop the chain when it first enters below `2n`. Push the entire signed source from all scales through that stopping kernel and call the resulting transition source `Sigma_(X,n)(p)` on

```text
n <= p < 2n.
```

Strong Markov gives exactly

```text
n A_X(n)=sum_(n<=p<2n) Sigma_(X,n)(p) P_p(hit n).
```

All generations above the transition band are now recombined before the sign. This is the precise operation missing from the failed Abel, bounded-rank, monotone-cover, and total-variation routes.

The proposed theorem is

```text
GFEP:
Sigma_(X,n)(p)>=0 for every X,n,p.
```

GFEP implies producer positivity with no additional estimate.

## 4. Unconditional top-fifth theorem

The critical multiple-Möbius source uses only `mu(1),...,mu(4)` when `m>=X/5`. On those quotient cells its scaled primitive has derivative

```text
-u_N'(theta)=theta^(-3/2) C_N(log(1/theta)).
```

The worst cell is `N=3,4`. Exact rational interval arithmetic proves

```text
C_3(log 5)>1/25.
```

Therefore

```text
R_X(m)>=0 for every m>=ceil(X/5).
```

This proves GFEP on the entire top fifth. The global transition theorem starts below, with a genuine positive base above it.

## 5. Independent dual localization

For the full quarter-balanced fragmentation cone, any normalized balanced-superadditive dual potential is nonnegative. An explicit near-halving tree extracts at least `n/(4m)` copies of leaf `m` from `n` whenever `n>=2m`. Hence

```text
phi(n)>=n/(4m) phi(m),
phi(m)/m <= 4 phi(n)/n.
```

Thus a dual obstruction cannot live independently at remote scales. Its new oscillation is confined to one factor-two transition annulus. This matches the first-entrance localization from a completely different coordinate system.

## 6. Full conditional completion

PR #277 proves that producer positivity automatically yields

```text
sum_n A_X(n)sqrt(n)=O(log^2 X).
```

Therefore GFEP gives a nonnegative exact balanced carry packing and

```text
complete prime-power ramp >= 4 sqrt(X)-polylog(X).
```

The source-pinned square-screw/Landau chain then gives RH.

The full spine is

```text
critical Möbius source
-> size-biased conservative ancestry
-> complete first-entrance source
-> GFEP
-> positive exact balanced flow
-> O(log^2 X) variation
-> 4 sqrt(X) prime ramp
-> square-screw/Landau
-> RH.
```

## 7. Connections to the live repository

This proposal is designed as a common landing point rather than a competing isolated lemma.

- PR #272: its Pascal-cycle basis can alter local transition flow while preserving the source.
- PR #274: squarefree collectors can repair ordinary-prime incidence without proper-power leakage.
- PR #269: every negative opposite-parity logarithmic coupling is already confined to a finite factor-five band.
- PR #240/#276: WSTS remains the scalar shell firewall; a GFEP proof must not assume it.
- PR #241: any reflected energy proof must use the correct independent-frequency normal block.
- PR #255: exact counterexamples are retained at the logical scope they actually contradict.

A successful transition certificate may use these components only after constructing their exact map into `Sigma`.

## 8. Exact verification

`X-28001` verifies:

```text
size-biased stochastic rows                255
general Green identities                    51
general first-entrance identities            51
quarter-balanced extraction trees        16,382
top-fifth derivative moat                  >1/25
fixed Abel counterexamples                   4
```

Retained verifier SHA-256:

```text
1e358254d5735b5b6d09415642baa4191841474de57652f814740dbeadd6bfcc
```

Finite floating reconnaissance found every critical first-entrance source coordinate positive at every endpoint through `X=10,000`. This is not a proof and is not part of the exact verdict.

## 9. Honest failure boundary

```text
fixed Abel orders 1--4                    false
pointwise dyadic shell producer           false in finite tests
size-biased spine algebra                 exact
first-entrance localization               exact
top-fifth source positivity               proposed complete
GFEP below top fifth                      open / RH-bearing
GFEP -> RH                                complete conditional chain
RH                                        unproved
```

The proposal is ambitious in the correct sense: the open theorem contains the complete reciprocal-zeta source and all scales, but its sign is asked only after the exact global recombination. It does not hide RH inside a generic operator estimate or a finite numerical ladder.
