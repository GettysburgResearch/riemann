# Independent review of the controlled negative-coupling strip component

Review result: **PASS for the stated component theorems, with their proposed
repository status and their explicit all-order hypothesis retained.**

The reviewer is the theta/strip worker, independently of the author of the
negative-coupling component. The review found no blocking mathematical or
implementation defect. It does not promote the component to a proof of a new
zeta boundary: no cofinal theta construction, and no certified theta-matching
negative-coupling model, is supplied by these files.

## Exact reviewed files

| File in `../analytic/` | SHA-256 |
|---|---|
| `NEGATIVE_COUPLING_STRIP.md` | `b63af0d5f9fdf3fbe95c3d772e8e0e7a3d0cc8447c279fe82b57ccb682c959c4` |
| `check_negative_coupling.py` | `9ed5ca62e3fcb9f08e07f84b72800a754b31e182a85b3b0a588b676945d1a3bf` |
| `negative_coupling_certificate.json` | `b17fd3f29ba78b139228b159c5f2623e1846b0bd4851434269ddcfcad2b88adb` |

Changes to these files after these hashes require a new or amended review.

## Mathematical checks

The edge disk argument was checked directly. For a negative edge,
`1+r_i r_j >= c(r_i+r_j)` with `c>1` puts both radii strictly below `1/c`.
The minimum of the fractional linear modulus on the allowed disk occurs on
the negative real ray and equals the claimed rational expression. The
conversion between this radius condition and the asymmetric endpoint
`tanh` budget is exact. The equal-weight one-edge example attains the
symmetric budget and supports the stated sharpness claim for that local
constant.

The disk contraction is valid with every other variable fixed at any allowed
value. Its one-variable diagonal polynomial has nonzero constant coefficient
and no roots inside the unit disk, so the product of its two roots proves
`|D| r_1 r_2 <= |A|`. Repeated incidence contraction retains exactly the
physical spin subsets. The reciprocal identity is ordinary global spin
reversal. These steps do not discard cycles or spin configurations. Zero
observable weights have zero field and no incident negative edge under the
budget; positive-weight approximation followed by Hurwitz handles them
without assuming a strict activity inequality at the unobserved vertex.

The growth proof uses the Lee--Yang Gaussian estimate only on the
nonnegative-coupling, zero-field reference. Its correlation matrix has
nonnegative entries and is positive semidefinite. The implication
`|J_e| <= alpha_(e,i) alpha_(e,j)` follows by integrating `tanh(t) <= t`.
The subsequent bound on the total negative-interaction cost uses the
nonnegative endpoint budgets, the unit diagonal of the correlation matrix,
and its nonnegative entries. It does not assume a bound on vertex count,
degree, or total observable weight.

Both numerator and denominator comparisons in Theorem B retain the full
negative interaction. Global spin reversal permits the `cosh` lower bound
even when the biased observable is not centered. The resulting second-moment
and entire-function estimates have the signs and constants stated in the
proof. The continuous variance argument excludes the intermediate branch
and explicitly requires a connecting path. The rational theta barrier is
strict, and the source variance uses the physical Xi variable. The final
Montel/Hurwitz implication is correct under its missing cofinal construction
hypothesis; it is not an unconditional conclusion.

## Independent replay

From the directory containing `analytic/` and `audit/`, the replay command is:

```sh
python -O analytic/check_negative_coupling.py \
  --report /tmp/negative_coupling_independent.json
```

The replay passed with Python optimization enabled. Its output agrees
byte-for-byte with the recorded certificate. The checker compared incidence
contraction with complete configuration enumeration for graphs having 2, 3,
4, and 5 vertices; checked three exact rational edge budgets, including two
boundary cases; and recomputed the strict rational variance-barrier margin
`228671/22500000000`. Acceptance conditions use explicit runtime guards and
remain active under `python -O`.

These finite checks support the implementation and examples. The arbitrary
finite-graph theorem is supplied by the analytic proof reviewed above.
