# Integration handoff — cofinal radical-tail ratio

Stack on PR #152.

## Claim order

```text
L-14311  exact multiband complement floor       [existing parent]
L-14312  exact Riemann-radical Gaussian tail
L-14313  full-domain finite packet Hardy moat
T-14303  both cofinal tail/coercivity limits
O-14303  remaining growing low-block barrier
X-14307  exact finite source/ratio regression
```

## Review order

1. Verify the `E(h_R)` source and radical conventions against Connes--Consani.
2. Check every component of the polarized explicit-form tail estimate in
   `L-14312`, especially the `n>lambda^2` translation geometry.
3. Check that `L-14311`'s symbol inequality extends through Suzuki's closed form
   to constants and the full localized form domain.
4. Check the unitary scaling and Hardy metric conversion in `L-14313`.
5. Recompute the two one-line limits in `T-14303`.
6. Replay `X-14307` and all mutation tests.

## Do not infer

The theorem does not prove positivity of the growing low packet and does not
prove RH.  Its exact contribution is to remove the external-tail ratio from the
critical path of the block lower-floor route.
