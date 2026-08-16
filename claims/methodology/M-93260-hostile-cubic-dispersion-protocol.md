# M-93260 — Review protocol for the hostile cubic-dispersion successor

Status: **METHODOLOGY / REVIEW ORDER**  
Created: 2026-08-16

## Frozen base

```text
PR #498 head:
6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

The successor must have that commit as its sole parent. PR #498, PR #483, and
`main` are not modified. `O-93244` must remain absent.

## Review order

1. `R-93260`: reconstruct the cubic identity, normalization, pole audit, and
   interpolation; verify the `d_N(a)` correction.
2. `L-93261`: verify the piecewise kernel, two roots, double Mellin zero, and
   one-switch no-go.
3. `T-93260`: verify prime-power and gauge removal before reading any new
   producer language.
4. `L-93262`: verify finite telescoping before accepting the infinite Abel
   statement; check that only the unconditional PNT is used for convergence.
5. `L-93263`: verify both logarithmic primitives, positivity of `Phi`, the
   exact curvature identity, its Mellin transform, and the PNT-only limiting
   constant.
6. `R-93264`: test the finite and geometric positivity firewalls; do not infer
   a curvature sign merely from positivity of `Phi`.
7. `L-93265`: reconstruct `Lambda=mu*log`, the two vanished moments, the
   explicit second-order Euler bound with `C_W=512`, and the `sqrt(X)` split.
8. Run `X-93260` and compare the retained JSON and both SHA ledgers.

## Estimates forbidden as hidden inputs

Do not import any of the following as unconditional:

```text
M(x)=O(sqrt(x) polylog x);
psi(x)-x=O(sqrt(x) polylog x);
macroscopic Selberg integral at critical scale;
pointwise large-sieve cancellation at additive frequency 1/N;
CPBD or the large-divisor Mobius-tail bound;
First-Hermite one-carrier exclusion.
```

The only external analytic input in `L-93262` and `L-93263` is the classical
unconditional PNT, used solely for the critical Abel limit and the limiting
constant of the positive potential. The main localization `L-93265` is
elementary and finite.

## Acceptance boundary

The packet is an advance, not an RH proof. It is acceptable only if it reports:

- the surviving equivalence honestly;
- the corrected modulus line;
- the exact minimal-switch theorem;
- the positive compact Peano potential and its exact curvature identity;
- the scale-positivity no-go;
- the closed small-divisor ledger;
- the large-divisor Mobius tail as open.
