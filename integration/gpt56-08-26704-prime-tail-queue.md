# Integration handoff — prime-tail queue transport

Date: 2026-08-08  
Source PR: #271  
Relevant branches: #248, #254, #265, #269, #270

## Exact construction

For the ordered ordinary-prime residual `r_i`, define

```text
C_i=(C_(i-1)+r_i)_+.
```

The nonnegative blocks

```text
C_i 1_(p_i<m<=p_(i+1))
```

repair every old prime row. The final boundary charge is

```text
Q_X=max_k (sum_(j=k)^N r_j)_+,
```

and is minimal among all upward nonnegative prime-dipole transports.

The objective ledger is

```text
P_X >= J_P(b)-Q_X log X.
```

## Fixed-ratio theorem

For the parabolic seed, every positive maximizing tail begins at `o(X)`. This follows from the strict continuum tail majorization of PR #265 plus a uniform prime Riemann-sum transfer and the certified outer sign of PR #248.

## Integration notes

### PR #254

This is an explicit positivity-preserving constraint-dipole flow. The signed transport problem has a one-dimensional ordered-prime quotient whose exact debt is `Q_X`.

### PR #265

The continuum tail theorem now has a finite prime consequence at every fixed ratio. The remaining step is quantitative transfer in the shrinking-ratio regime, not another continuum sign theorem.

### PR #269

The preferred next proof is a half-scale recurrence for `Q_X` or a dyadic signed queue dominating it. The exact even-column isometry supplies the lower-scale block; the odd-column leakage must retain all three dyadic valuation layers.

### PR #270

The queue intervals are the simplest layer-cake contact dipoles. A Green-Skorokhod proof should seek to show that their unmatched boundary charge satisfies a half-scale recurrence.

## Status

```text
queue construction and min-cut       PROPOSED COMPLETE
fixed-ratio localization             PROPOSED COMPLETE
shrinking-ratio queue theorem        OPEN
RH                                    UNPROVED
```