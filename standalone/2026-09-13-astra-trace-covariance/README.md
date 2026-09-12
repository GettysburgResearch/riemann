# Direct trace covariance: the diagonal is now explicit

**PROPOSED component mathematics. RH and the native covariance upper bound remain
OPEN.** This is an additive continuation of PR866 at
`cb05d3052611bd1804459887e84fdec3cb7064af`. No earlier result is promoted.

Start with [PROOF.md](PROOF.md). The same DG26 source is retained:

- `m(x)=sum_{n<=x, odd}mu(n)/n`;
- `Kf(t)=integral_0^1 m(t/u)f(u)du/u`, for `1<t<3`;
- `phi_j=sqrt(4j+3)P_(2j+1)` and `S_N=sum_{j<N}||Kphi_j||^2`.

## New completed calculation

Put `psi_j(x)=integral_x^1 phi_j(u)du/u`. Exactly, at EVERY degree,

    integral_0^1 psi_j(x)^2 dx=1/(j+1).

The native arithmetic diagonal

    D_N=sum_{j<N}sum_{n>=3, odd}mu(n)^2/n^2
                         integral_1^3 psi_j(t/n)^2dt

therefore satisfies

    D_N=(4log3/pi^2) H_N+C_*+O(N^(-1/5)).

The proof supplies the explicit error and an exact expression for C_* using
only gamma, log2, log3, pi and Z'(2)/Z(2), with Z(s)=(1-2^-s)zeta(s).
No zeta-zero or RH input occurs in this diagonal theorem. In particular the
positive diagonal block increment has a finite limit.

This is NOT the different all-integer Newton collision diagonal studied in
#848/#875/#869, whose order is log^4. It is the direct diagonal of our original
odd-source trace.

## What prevents the claimed full proof

There is an exact source-ordered covariance C_N with `S_N=D_N+C_N`. It is a
limit of complete finite double sums; no cross terms have been dropped. For
EVERY fixed N the positive and negative termwise covariance sums both diverge
like a positive constant times `(log R)^2` as the source cutoff R grows.
Their jointly truncated difference converges. An absolute-value estimate, or
separate infinite positive/negative sums, therefore cannot close the argument.

An exact random-prime-sign comparison has expected trace D_N and almost-sure
trace O_delta(log(2N)[loglog(4N)]^(1+delta)) for every delta>0. The literal Mobius source is the SINGLE all-negative
prime configuration. The probabilistic conclusion does not control that
point and is not an RH theorem. The proof retains this distinction explicitly.

The exact remaining task is a native upper bound on C_N, or on its dyadic
increments, mild enough to force S_N=N^o(1). No such upper bound is obtained.
The new results finish the diagonal calculation and specify its signed
complement; they do not prove that complement is small.

## Bounded native certificates

The checker gives outward enclosures, not fitted values or exact eigenvalues:

| N | S_N | D_N | C_N=S_N-D_N |
|---:|---:|---:|---:|
| 1 | (2.386649,2.386650) | (0.465941,0.465942) | (1.920707,1.920708) |
| 4 | (3.561925,3.561926) | (0.950850,0.950853) | (2.611072,2.611075) |
| 16 | (3.884868,3.884869) | (1.530808,1.530840) | (2.354028,2.354061) |

It also certifies C_2>C_1, rejecting nonincreasing covariance from the start.
Later decreases in this finite table do not justify a general upper bound.

## Reproduce

```bash
P=standalone/2026-09-13-astra-trace-covariance
python -B "$P/check.py" --check "$P/results.json" --self-test
python -O -B "$P/check.py" --check "$P/results.json" --self-test
python -OO -B "$P/check.py" --check "$P/results.json" --self-test
```

See [SOURCES_AND_VALIDATION.md](SOURCES_AND_VALIDATION.md) for exact source pins,
reading scope, complete-tail conventions, development failures, and what the
finite checker does not prove. Same-author cross-checks are not independent
mathematical review. The manifests authenticate this packet only, not the
whole repository or other research branches.
