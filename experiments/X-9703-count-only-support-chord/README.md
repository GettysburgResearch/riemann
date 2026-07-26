# X-9703 — Count-only support-gap chord witnesses

Agent: `gpt56-08`  
Issue: #93  
Status: proposed theorem, exact checker, exact synthetic separation, and ordinary four-slab reconnaissance; directed Riemann-`xi` production pending

## Breakthrough

`L-9703` eliminates the zero-location stage entirely.

Fix an exact slab `(a,b)`, an exact target `T` inside it, and the exact total
number `N` of all nontrivial zeros in that slab, counted with multiplicity. Put

```text
A = min((T-a)^2,(b-T)^2).
```

For `0<u0<u1<u2`, define

```text
L1 = log((u1+A)/(u0+A))
L2 = log((u2+A)/(u0+A))
Phi = L1*(G(u2)-G(u0)) - L2*(G(u1)-G(u0))
phi0 = L1*log(u2/u0) - L2*log(u1/u0),
G(u)=log |xi(1/2+sqrt(u)+iT)|^2.
```

Under RH,

```text
Theta = Phi - N*phi0 >= 0.
```

The total count is unconditional. Its conversion into line-zero factors occurs
only under the RH assumption in the proof by contradiction.

The proof shows that the response of one line-zero factor at squared distance
`y` is bounded below by its explicit value at `y=0`; every zero outside the
slab has `y>=A` and contributes nonnegatively.

## Trusted finite checker

```text
verify.py
```

uses only integers and `fractions.Fraction` after JSON parsing. It recomputes:

- the exact support radius `A`;
- the unique integer in the total-count interval;
- complex-rectangle modulus-square intervals;
- self-contained rational logarithm intervals;
- `L1`, `L2`, the raw chord, `phi0`, and the adjusted chord;
- every strict final sign.

It evaluates no special function and uses no floating point.

A production certificate must carry

```text
CERTIFIED_TOTAL_ZETA_ZERO_COUNT
```

and an immutable count-source digest.

## Exact synthetic separation

The model

```text
slab=(-1,1)
T=0
A=1
N=0
H(u)=u+1/2
nodes=(1,2,3)
```

has an ordinary positive Stieltjes factor at squared distance `1/2`, but that
mass lies inside a slab declared empty by the count. The checker obtains

```text
log(3/2)*log(7/3) - log(2)*log(5/3)
≈ -0.0105276223094579494570399716163543.
```

This is an exact synthetic control, not a Riemann-`xi` result.

## Four-slab reconnaissance

`recon.py` screened the four unconditional X-5604 slab targets using fifteen
rational support-scaled nodes and ordinary 80-decimal-place arithmetic.

| slab | count `N` | smallest raw chord | smallest adjusted chord |
|---|---:|---:|---:|
| PR71 | 172 | `-0.2475382644...` | `+0.6543387282...` |
| `10^13` | 4467 | `-6.3701287160...` | `+17.0524557377...` |
| `10^14` | 242 | `-0.3450271947...` | `+0.9238927601...` |
| `10^15` | 52 | `-0.0756853482...` | `+0.1969751379...` |

Across `4*455=1820` triples:

```text
raw negative rows       525
adjusted negative rows    0
```

This is an important adversarial lesson: the raw chord very often looks like a
counterexample. The exact count correction is load-bearing and reverses every
retained sign.

The ordinary screen is preserved in

```text
results/four-slab-summary.json
```

and is explicitly non-certifying.

## Reproduction

```bash
python experiments/X-9703-count-only-support-chord/verify.py \
  experiments/X-9703-count-only-support-chord/certificates/\
synthetic-empty-slab-hidden-factor.json

python -m unittest discover \
  -s experiments/X-9703-count-only-support-chord/tests -v

python experiments/X-9703-count-only-support-chord/recon.py \
  experiments/X-9703-count-only-support-chord/configs/certified-slabs.json \
  --dps 80 --prime-cutoff 10000 \
  --output experiments/X-9703-count-only-support-chord/results/recon.json
```

## Production architecture

A proof-grade run needs only:

1. `N(a)` and `N(b)` as directed total-count balls isolating integers;
2. three or more direct completed-`xi` rectangles at exact positive nodes;
3. the exact checker;
4. a 192/256-bit nesting pass.

No Hardy-`Z` evaluation, sign chain, approximate zero guide, root isolation,
individual multiplicity assignment, or count-linear-program certificate is in
the production critical path.

## Counterexample semantics

A strict negative production interval is a finite RH-disproof nomination. It
still requires:

- independent review of `L-7501` and `L-9703`;
- independent total-count reproduction;
- independent completed-`xi` production;
- exact normalization review;
- final interval nesting and an upper endpoint below zero.

No actual Riemann-`xi` negative is claimed by X-9703.