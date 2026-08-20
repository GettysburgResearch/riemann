# T-100210 dual-route hostile reconstruction handoff

## Frozen bases

```text
PR #672 phase-Hasse sibling:
2a351548eb7960ff8ae99f193c10e278984c5657

PR #674 minimal wavelet:
9962f7f712adc6b4ad72672ecfeace028ba79bdb

PR #675 spectral audit / branch base:
e21383e7522962182491f88301b3cbd375d6d6d0
```

## Reconstruction order

### Shared firewalls

1. Recompute the conjugation in `R-100210` and verify that the quadratic
   envelope sees `p^-1` on its leading physical mode.
2. Do not use FEAG summability as an antecedent.
3. Preserve both labelled `67` occurrences in every phase-Hasse object.

### Route A

1. Reconstruct the random-order Hasse edge formula from PR #672.
2. Expand the exact finite phase symbol.
3. Verify `L-100210.2` coefficient by coefficient.
4. Verify the Cauchy characteristic-function identity.
5. Check that the local bound is uniform in the finite active block.
6. Instantiate the outside-core sum before equal products are collapsed.
7. Prove or refute `PHCC100210` on that literal source.

Immediate falsifier: replacing the cross-core sum by the sum of local absolute
values incurs a half-order loss and does not prove the theorem.

### Route B

1. Reconstruct the three bands of `K_0` from PR #674.
2. Verify the first-order activation zero and continuity of `J_0`.
3. Differentiate `mathscr A_X` and recover `G_mu` exactly.
4. Reconstruct the centered circle Parseval identity.  The subtraction of
   `mathscr A_X(0)` is mandatory.
5. Check the factorial tail with the stated `K_X`.
6. Express every retained moment on the literal ordinary-Mobius shell.
7. Prove or refute `GMPC100212`.

Immediate falsifier: using the uncentered circle reintroduces the root term and
returns to the RH-equivalent square isolated by PR #675.

## Proposed combined attack

Apply the symmetric phase-Hasse flow to each of the first `K_X` logarithmic
moments before physical product collapse.  First-owner Jensen should remove
cross-owner interactions.  The remaining matrix is supported only on
multiplicative near-collision clusters.  The exact theorem to seek is a
subpower congestion bound for those clusters, uniform for
`1<=k<=K_X` after division by `k!`.

## Status

```text
PHCC100210   open / RH-bearing
GMPC100212   open / RH-bearing
RH           unproved
```
