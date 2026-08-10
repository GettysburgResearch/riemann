# Powered Euler / Anthropic Zeta23 fusion

Date: 2026-08-10  
Status: **two new exact source/spectral theorems; RH unproved**

## 1. External advance and resident continuation

PR #361 imports the Anthropic/Claude Zeta23 theorem: an unconditional
`0.6725...` simple/on-line zero proportion with a formalized `2/3` core. PRs
#363 and #364 turn an individual off-line pair into an exact negative spectral
block and then remove finite-packet and complete-zero-side interpolation
collapse.

The remaining issue is arithmetic: a complete lower floor or subexponential
bound for the admissible test family.

## 2. Blaschke--Krylov finite-packet theorem

For a half-plane inner delay `phi`, the open channel bank

```text
1, phi, ..., phi^(k-1)
```

has a quantitatively deep reflected-pair block, but scalar inner multiplication
is exactly J-unitary and supplies no free gain.

The correct result is interpolation noncollapse. For every fixed finite packet,
a generic inner coordinate gives a bounded target-pair Schur cost. In the
rational eight-point replay the cost decreases from about `25821.7` to the exact
limit

```text
9800/81 = 120.987654...
```

This removes finite local zero-conditioning as an independent obstruction.

## 3. Powered root-of-unity Euler frame

Let

```text
a(s)=4^(1-s),
F_(omega,k)(s)=(1-omega a(s))^k.
```

After averaging over `M>2 max(k,floor(log_4 n))` roots of unity:

- the critical current frame is exactly normalized by
  `C_k(4)=sum_j binom(k,j)^2 4^j`;
- a reflected off-line pair has eigenvalues
  `m(1 +/- R_k(q))`;
- `R_k(q)>1` off the line and obeys an explicit exponential lower bound;
- every active four-adic generalized-prime level occupies a separate phase;
- the complete averaged Selberg--Kummer reserve is exactly the ordinary reserve
  plus positive local squares;
- the difference between the separate-system current and the genuine ordinary
  pole current is a deterministic physical gauge with only `O(k^2)` normalized
  energy.

This repairs the scalar-power failure on PR #325: the local levels are separated
before the Hermitian square rather than stacked in one source.

## 4. Exact new frontier

The complete zero-side escape is now removed by the Gaussian terminal theorem on
PR #364. The powered phase bank leaves one explicit arithmetic growth problem:

```text
normalized independent-frequency reflected source block
   <= exp(o(k)) + polynomial deterministic gauge.
```

Such a bound would contradict the exponential off-line eigenvalue and prove RH.
It is not proved here. Row-reserve positivity alone cannot be substituted for
this complete block estimate.

## 5. Exact replay

```text
PASS_EXACT_BLASCHKE_KRYLOV_FINITE_NONCOLLAPSE
sha256 5a44578b2e2fa87f8f64a37f9505d4b16d1bc2c91e0908ded086213740cb131a

PASS_EXACT_ROOT_UNITY_POWERED_EULER_FRAME
sha256 a669e5ebcba888612596519e41aebba3f34a5f89482c7fb02790d78949b71130
```

## Boundary

```text
Anthropic 0.6725 theorem                      imported
complete zero-side negative direction         proposed complete on PR #364
finite packet Gram collapse                    removed
powered phase off-line exponential depth       proposed complete
powered phase averaged row reserve              proposed complete
polynomial physical gauge                       proposed complete
complete reflected arithmetic growth bound      open / RH-bearing
Riemann Hypothesis                              unproved
```
