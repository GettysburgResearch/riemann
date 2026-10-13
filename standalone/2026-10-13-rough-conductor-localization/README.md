# Rough-conductor localization of the generalized moment

Status: **proposed, not independently reviewed**. The full physical fourth
moment, generalized moment hierarchy and RH remain unproved.

This continuation is based on PR #931 at
`c77671d71dcf22a08833a6d7f86a6f15a2eba84f`. It adds an elementary native
sector bound and replaces the previous fully independent benchmark by a
reference that retains every physical divisibility mask and every
small-prime phase. No earlier proof or integrated status is edited.

## Main result

For every fixed k and epsilon>0, columns of norm at most X, and the complete
Hermitian tuple sector whose residual sextic conductor has all prime-ideal
norms at most `(log X)^2`, the **absolute tuple accounting** is

    O_{k,epsilon}(X^(k+epsilon)) per row,
    O_{k,epsilon}(H X^(k+epsilon)) over all 0<Nu<=H.

The result allows arbitrary bounded squarefree column coefficients,
additional tuple selectors, moving exclusions, nonunit zeros and all rows.
There is no additional bound on the total conductor norm. More generally,
the cutoff can be `(log X)^(2+o(1))`.

The proof uses a finite cyclic-phase projection and a positive Rankin
Euler majorant. The random phases are a device for representing a literal
native tuple sector, not a replacement for the physical row distribution.
The positive accounting bound itself follows directly by counting.

For a retained-prime cutoff `(log X)^A`, the uniform exponent is
`2k max(1/2,1-1/A)`. A separate construction shows sharpness for A>2 when
retained phases are unrestricted. The realizing row can be very large:
this is not a lower bound at the target physical height.

## What remains

The exact native moment is the controlled block-diagonal contribution plus
the real interference between distinct rough Kummer classes. Only the
upper side of this remainder remains to be bounded. The straightforward
Cauchy estimate loses a full power X^k, so it does not close the argument.
No new full-moment exponent or zero-free boundary is claimed.

## Read and reproduce

- [Complete proof, sharpness and remaining estimate](PROOF.md).
- [Sources, overlap and dependency limits](SOURCES.md).
- [What was actually checked](VALIDATION.md).
- [Exact standard-library diagnostic](checks/check_rough_projection.py).
- [Saved exact output](results/exact.json).

Run:

```sh
python checks/check_rough_projection.py > /tmp/rough-normal.json
python -O checks/check_rough_projection.py > /tmp/rough-optimized.json
cmp /tmp/rough-normal.json /tmp/rough-optimized.json
cmp /tmp/rough-normal.json results/exact.json
python checks/verify_manifest.py
```

The checker uses exact integer/cyclotomic arithmetic and rational numbers.
Its 4937 predicates include three independent finite formulations of the
projection, genuine split/conjugate/inert prime-ideal characters, literal
zero masks and four negative controls. These counts include elementary
setup predicates; they are not independent asymptotic cases.

The native experiments use the hard column window D<=Nn<=2D, nu=1,
excluded primes over 2 and 3, and every nonzero element row Nu<=H=D.
They are diagnostic finite examples, not simulations substituted for proof.
