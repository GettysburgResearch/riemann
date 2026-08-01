# X-16207 — source-derived repaired-packet moat

This experiment replaces the three placeholder fields used by the early
`DIRECTED_INTERVAL_ODE` prefix:

```text
tail_l2_sq_upper                 1
derivative_tail_l2_sq_upper      4
source fourth-derivative L1      10^100
```

with values derived from the actual `gamma=4096`, modes `0,4,8,12` repaired CCM
packet.

The producer reconstructs the directed infinite Legendre--Jacobi eigenvectors,
resolves the positive concentration defects, forms the exact two-constraint
`0/4/8` target and `4/8/12` complement, and propagates their normalized
coefficient tails through the Fourier/radial map.  It also applies the exact
Legendre derivative transform four times and uses Cauchy--Schwarz to obtain a
physical `W^{4,1}` source bound.

The compact certificate retains outward rational ceilings:

```text
radial tail L2 squared              <= 1e-4181
frequency-derivative tail L2^2      <= 1e-4174
horizontal-strip tail L2^2          <= 1e-4180
repaired packet ||f^(4)||_1         <= 45000
p=4 endpoint point charge           <= 1e-5
p=4 endpoint L2 squared charge      <= 2e-10
source-derived deterministic error  <= 1/40000
first-alias Gram                    [0.9999999, 1.0000001]
```

`verify.py` reconstructs all combinations from the two source columns and fails
closed if a downstream deterministic error is declared independently.

## Deliberate promotion barrier

The first Poisson sample is not the complete arithmetic omitted tail.  If

```text
D_full = D_first + P_self + C_cross,
P_self >= 0,
```

then

```text
D_full >= [lambda_min(D_first)-||C_cross||] I.
```

The certificate therefore has one mandatory production field:

```text
complete_arithmetic_alias.cross_error_upper.
```

It is currently `null`.  The checker consequently returns

```text
SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN
```

rather than passing a synthetic profile-Gram interval through X-16204.  A
source-directed oscillatory quadrature or finite phase ledger must supply this
single cross-alias operator bound.

## Cofinal decay

For an unbounded block sequence, choose the angular/Jacobi cutoff adaptively
until every repaired normalized radial tail is at most `gamma^-2`; the scaled
frequency derivative is then at most `gamma^-1`.  This is a diagonal
proof-producing choice because the directed coefficient tail tends to zero for
each fixed block and every exact leakage norm is positive.

For the fixed repaired mode packet, the prolate sources converge with fixed
Sobolev order to their Hermite limits.  Hence `||f^(4)||_1=O(1)` along the
cofinal sequence.  Since `lambda ~ sqrt(gamma)`, the p=4 endpoint charges obey

```text
point charge = O(gamma^-2),
L2 squared charge = O(gamma^(-7/2)).
```

Thus every replacement field in the deterministic-error ledger tends to zero.
The only unclosed cofinal datum is the complete arithmetic cross-alias operator
bound.

Run:

```bash
python verify.py certificate.json --output results/verification.json
python -m unittest discover -s tests -v
```

No RH proof is claimed.
