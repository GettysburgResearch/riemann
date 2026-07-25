# X-3904 — Cross-height complex Pick packets

Experiment ID: `X-3904`  
Agent: `gpt56-04-d`  
Issue: #39, parallel continuation  
Status: rigorous finite Arb scan pending workflow result  
Date: 2026-07-25

## Question

Do exact Pick vectors using several different ordinates expose nonpassivity that every same-height real-vector scan necessarily discards?

Under RH, L-3202 makes

```text
K_jk = (F(s_j)+conj(F(s_k))) / (s_j+conj(s_k)-1),
F = xi'/xi,
```

positive semidefinite for arbitrary points in `Re(s)>1/2`. Existing X-3902/X-3903 production contractions used one common ordinate and real vectors; their final functional therefore used only `Re F`.

L-3905 constructs exact Gaussian-rational vectors on nodes

```text
z_j = x_j + i y_j
```

and contracts

```text
v*Kv = 2 Re sum_j a_j F(s_j)
```

with exact complex coefficients. Both real and imaginary primitive rectangles contribute.

## Exact modeled-pair property

For a rational model displacement `d=delta^2`, the L-3905 vector satisfies

```text
sum conjugate(v_j) z_j/(z_j^2-d) = 0
sum conjugate(v_j)    1/(z_j^2-d) = -1
```

and the modeled reflected off-line pair contributes exactly

```text
-2*d
```

before normalization. Additional nodes cancel distant-zero moments. This modeled score only proposes a vector; the direct complete Arb interval decides the sign.

## Finite search domain

The committed scan uses four exact dyadic center ordinates near the two active carrier basins:

```text
4709203636353.6309
4709203636353.6409
3157430112465.8695095
3157430112425.8695095
```

Each decimal is replaced by its nearest declared `2^-32` dyadic and is recorded exactly in the certificate.

The packet family contains:

- three-node windows at horizontal scales `2^-20` through `2^-14`;
- model positions `1/4`, `1/2`, and `3/4` across the first horizontal gap;
- symmetric vertical offsets `(-2 delta,0,+2 delta)`;
- asymmetric fan offsets `(0,-2 delta,+4 delta)`;
- five-node packets at scales `2^-20` through `2^-16`;
- center-alternating and fan vertical patterns;
- exact moment and pole-overlap checks before every Arb call.

After point deduplication this gives:

```text
exact primitive points  428
exact packet channels   208
```

The scan runs at 160 and 224 bits. The higher-precision interval for every fixed channel must lie inside its 160-bit interval.

## Files

- `cross_height.py` — exact `Q(i)` arithmetic and L-3905 construction;
- `verify_cross_height_certificate.py` — standard-library exact rectangle contraction;
- `cross_height_scan.py` — exact finite manifest plus Arb execution;
- `compare_cross_height.py` — precision-ladder nesting check;
- `tests/` — exact pair, Gram, mutation, and finite-zero-model controls.

The primitive producer is inherited from X-3902 / draft PR #56. It evaluates each point by two completed-`xi` assemblies with Python-FLINT/Arb and requires the zeta denominator ball to exclude zero.

## Reproduction

From the repository root:

```bash
python -m pip install python-flint
export PYTHONPATH="$PWD/experiments/X-3902-arb-xi-passivity:$PWD/experiments/X-3904-cross-height-pick"

python -m unittest discover \
  -s experiments/X-3904-cross-height-pick/tests -v

python experiments/X-3904-cross-height-pick/cross_height_scan.py \
  --precision-bits 160 \
  --certificate experiments/X-3904-cross-height-pick/results/p160-certificate.json \
  --verification experiments/X-3904-cross-height-pick/results/p160-verification.json \
  --summary experiments/X-3904-cross-height-pick/results/p160-summary.json

python experiments/X-3904-cross-height-pick/cross_height_scan.py \
  --precision-bits 224 \
  --certificate experiments/X-3904-cross-height-pick/results/p224-certificate.json \
  --verification experiments/X-3904-cross-height-pick/results/p224-verification.json \
  --summary experiments/X-3904-cross-height-pick/results/p224-summary.json

python experiments/X-3904-cross-height-pick/compare_cross_height.py \
  experiments/X-3904-cross-height-pick/results/p160-verification.json \
  experiments/X-3904-cross-height-pick/results/p224-verification.json \
  --output experiments/X-3904-cross-height-pick/results/precision-ladder.json
```

## Promotion boundary

A channel whose directed upper endpoint is negative is a rigorous finite nomination under the proposed D-3201/L-3202/L-3905 interface. Before candidate allocation it must be:

1. reproduced with a separately audited directed implementation or library;
2. checked against the completed-`xi` normalization and canonical-product convention;
3. replayed from exact points and the exact Gaussian-rational vector;
4. shown not to depend on a malformed or zero-containing primitive denominator.

A modeled negative, floating eigenvalue, midpoint score, or interval touching zero is never a candidate. A wholly nonnegative finite result says nothing outside the declared packet family.
