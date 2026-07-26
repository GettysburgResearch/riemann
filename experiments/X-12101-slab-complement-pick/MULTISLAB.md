# X-12102 — Polynomial multi-slab Pick checker

`verify_multislab.py` implements L-12103 using the exact primitive arithmetic
from X-12101.

## The proof object

For `m` disjoint complete zero slabs, define

```text
P(gamma)=product_r (gamma-a_r)(gamma-b_r).
```

The exact Gaussian-rational packet must satisfy

```text
sum_i conj(v_i) w_i^k = 0,
k=0,...,m-1,
```

where all ordinates are translated by one exact origin. The checker
reconstructs

```text
2 Re sum_i c_i F(s_i)
-
sum_(all zeros in all slabs)
  P(gamma)|Phi_v(gamma)|^2.
```

Under RH this is the sum over the complement of the slabs, where `P>=0`.

## Commands

```bash
python verify_multislab.py \
  certificates/synthetic-multislab-separation.json

python verify_multislab.py \
  certificates/synthetic-multislab-control.json

python -m unittest discover -s tests -v
```

## Two-slab strict separation

```text
slabs                  (-2,-1), (1,2)
certified line zeros   -3/2, +3/2
off-line pair          delta=1/2, gamma=0
points                  1/5-i, 1/5+i, 2/5-i, 2/5+i
vector                  (1,-1,-1,1)
moments                 k=0 and k=1 exactly zero
```

Exact scores:

```text
ordinary Pick
  +79110061027840000/142332226998051841

polynomial weighted full score
  -246687826844000000/142332226998051841

complete in-slab contribution
  -655200000/479391721

multi-slab complement residual
  -108800000/296901721
```

The exact critical-line control has residual

```text
+22500/142129.
```

## Fail-closed controls

The multi-slab tests reject:

- a nonvanishing higher packet moment;
- overlapping slabs;
- incomplete count saturation in one slab;
- a zero bin assigned to the wrong slab;
- primitive widening that prevents a strict sign.

They also verify exact translation invariance: shifting every slab, zero,
point ordinate, and the declared origin by the same rational leaves the
residual unchanged.

## Production ranking

Higher degree is not automatically better. For each proposed slab family,
record:

```text
negative midpoint
complete directed radius
moment-conditioning cost
zero-table cost
primitive F reuse fraction
```

Only filters with improved rigorous moat-to-radius ratio should be escalated.
The PR #105 320-zero sidecar is the first source for two- and three-slab
experiments on existing PR #56 primitive values.
