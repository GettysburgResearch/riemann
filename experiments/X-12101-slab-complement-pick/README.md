# X-12101 — Slab-complement cross-height Pick checker

This experiment implements L-12101/L-12102 with exact rational arithmetic.

## What it checks

Given:

- exact slab endpoints;
- an exact complete slab-zero count;
- disjoint certified critical-line zero bins saturating that count;
- exact sample points in `Re(s)>1/2`;
- directed complex rectangles for `F=xi'/xi`;
- an exact Gaussian-rational vector with exact zero sum;

the checker reconstructs

```text
ordinary Pick score
quadratic weighted full-zero score
complete in-slab weighted contribution
slab-complement residual
```

and classifies the final interval.

It evaluates no special function and certifies no zero count. Those are named
logical gates.

## Commands

```bash
python verify_slab_complement.py \
  certificates/synthetic-strict-separation.json

python verify_slab_complement.py \
  certificates/synthetic-line-zero-control.json

python -m unittest discover -s tests -v
python -m compileall -q verify_slab_complement.py tests

# Discovery only: floating eigensolve -> exact zero-sum dyadic vector
python rank_midpoint.py certificates/synthetic-strict-separation.json \
  --bits 40 --output results/synthetic-midpoint-nomination.json
```

## Exact strict separation

The strict-separation synthetic packet has

```text
ordinary Pick:
  7450901935000 / 47129216977 > 0

slab-complement residual:
  -2956250 / 33337 < 0
```

so the new localizer succeeds where ordinary Pick passivity is strictly
positive.

The positive control has residual

```text
40377630000 / 22251597721 > 0.
```

## Fail-closed behavior

The tests reject:

- nonzero vector sum;
- incomplete slab count;
- overlapping bins;
- bins touching slab endpoints;
- Boolean multiplicities;
- blocking gates;
- false claimed endpoints.

A deliberately widened primitive rectangle returns
`UNRESOLVED_ZERO_TOUCH`.

## Discovery-only ranker

`rank_midpoint.py` constructs the midpoint slab-complement matrix, projects to
the zero-sum subspace, freezes its minimum direction to Gaussian dyadics, and
repairs the vector sum exactly. It never classifies a proof sign.

For an in-slab zero it subtracts

```text
g(gamma) r(gamma) r(gamma)*,
r_i(gamma) = 1/(z_i-i gamma),
```

which is the matrix whose quadratic form is
`g(gamma)|Phi_v(gamma)|^2`.

On the synthetic packet the corrected ranker nominates a 40-bit vector with
midpoint eigenvalue

```text
-9.748735152294984.
```

Independent X-12101 replay of that frozen vector gives the exact strict
residual

```text
-2553805375103012404546942922875
--------------------------------
 261962740315203803181668630528
```

which is approximately `-9.748735152297513`.

The first discovery-only draft used the conjugate rank-one orientation. The
exact checker was unaffected. The ranker, theorem matrix notation, frozen
vector, and derived digests were corrected before any Riemann-data nomination.

Production use requires NumPy only in this untrusted discovery layer. The
exact checker remains standard-library-only.

## Proof boundary

Exact here:

- rational parsing;
- Gaussian-rational contraction;
- zero-sum verification;
- slab/bin completeness arithmetic;
- rectangular reciprocal enclosures;
- quadratic-weight intervals;
- strict sign and moat.

External:

- D-3201/L-3201/L-3202;
- primitive directed `F` rectangles;
- total slab count and endpoint gates;
- every critical-line zero bin;
- independent numerical reproduction.

No actual Riemann-xi negative is included.
