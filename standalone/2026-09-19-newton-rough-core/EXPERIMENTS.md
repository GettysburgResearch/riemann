# Finite experiments and failed shortcuts

The proof in PROOF.md is the source of the all-cutoff sector bounds. These
calculations test its definitions and the complete finite source ledgers;
they do not establish an unbounded native gain.

## Directed-interval panels

Every displayed value below is a rounded presentation of a 112-bit outward
integer calculation. The authoritative lower and upper endpoints, with a
power-of-two denominator, are in `result.json`. All integer indices from
`Y+1` to `(Y+1)^2-1` are included. No product coefficient is dropped because
its index exceeds the observation endpoint.

For bank S={2,3}, the native calculations give:

| Y | B | Full annular energy F_B-F_Y | Block energy D_S | Signed cross-block C_S |
|---:|---:|---:|---:|---:|
| 5 | 35 | 0.0612974992583 | 0.0822873445890 | -0.0209898453308 |
| 15 | 255 | 0.0832644559621 | 0.4578377581436 | -0.3745733021815 |
| 31 | 1023 | 0.0990995899972 | 1.0447780323556 | -0.9456784423584 |
| 63 | 4095 | 0.1256620238712 | 1.1550874402728 | -1.0294254164017 |

These particular completions have zero annular collar, so the first column
of energies equals D_S+C_S. That simplification is NOT assumed generally.
The widths of the recorded block-energy enclosures are less than 4e-29.

### A nonzero native collar, explicitly retained

At Y=95 the clipped completion extends to 97, so m_c(96) is nonzero.
All reconstructed Newton coefficients through B=9215 equal the native ones.
The complete annular scalar ledger, evaluated without any grouped-kernel
claim at this larger Y, gives

```
T_Y                 = 0.000103852646765368...
||Q||^2             = 0.133006449772112490...
-4 <m_c,Q>          = 0.000858440897888353...
F_B-F_Y             = 0.134280301257062315...
```

The enclosures verify `F_B-F_Y=4T_Y+||Q||^2-4<m_c,Q>` and reject dropping the
collar. Grouped D_S/C_S calculations at Y=95 are present only as binary64
scouts, not accepting interval calculations.

### Coarsening does not monotonically lower the energy

At Y=31,

```
D_{2,3}       = 1.044778032355616082...
D_{2,3,5,7}   = 1.149412331150784922...
```

The two interval enclosures are disjoint in the displayed order. This rejects
an argument that continually merging prime-parity blocks must decrease their
summed energy. The theorem's upper bound is allowed to grow with the bank;
it makes no monotonicity assertion about the actual signed blocks.

### Within-squareclass off-diagonals can be positive

At Y=15 with no prime bank,

```
ordinary coalesced-product diagonal = 1.227073132476258892...
sum squareclass block energies     = 1.269256783828900487...
```

The extra within-class off-diagonal is positive. Its bound is therefore not
being obtained by silently declaring every such term negative.

### The kernel Gram matrix need not have nonnegative entries

The checker encloses the COMPLETE `sum_(k>=1) K_2(k)K_4(k)` by summing through
8192 and paying the two-sided tail `4/8192`. Its upper endpoint is negative.
Positive semidefiniteness of a Gram matrix does not imply entrywise positivity,
so prime-parity signs alone cannot decide every interaction's sign.

### A bounded fake source separates the unpaid term

For the fake prefix delta_1 through Y=15, followed by the same cap-three
completion, the actual INPUT innovation energy is 15, not the native input.
The complete finite calculation gives

```
||Q||^2          = 170.561384693732282...
D_{2,3}          =  19.476851941911524...
C_{2,3}          = 151.084532751820758...
output annulus   = 150.888238645295690...
```

The last number differs from `||Q||^2` because the fake completion has a
nonzero collar. This is a deliberate fake source, not a claim about Möbius.
PROOF.md proves an unbounded, explicit quadratic lower bound for this
cap-three family when Y>=128; the checker additionally verifies every k in
[2048,4096] for Y=128. The native divisor-inverse equations fail for the fake
input already at n=2.

## Ordinary scouts

`scout.py` uses NumPy and binary64 and was run with OPENBLAS_NUM_THREADS=1.
It records complete finite group panels for native Y=5,15,31,63,95,127 and
three declared banks; fake panels use Y=15,31,63. Every computed panel is
retained in `scout.json`. These are NOT interval certificates, independent
backends, zero computations, or all-scale evidence.

The banks were chosen before these grouped panels were evaluated, rather
than optimized to minimize one displayed cross term. No statistical p-value
or formal holdout significance is assigned. Y=63 provides a further certified
scale; Y=95/127 are larger ordinary diagnostic scales, not a proof extension.

One exploratory label originally reported a native-reference input value in
a fake-source row. It was corrected before packaging: `source_input_energy`
now measures the actual completed input. The native reference and the actual
fake output are separately named. That correction changes no theorem.
