# Integration patch — `gpt56-03-i` positive-anchor Christoffel ladder

This append-only file is intended for the repository integrator. It does not
modify concurrent global registries.

## Proposed claim registrations

| ID | Kind | Title | Status | Dependencies |
|---|---|---|---|---|
| `L-12101` | lemma | Positive-anchor one-moment transform and two-sided Schur gate | `PROPOSED` | L-9308, L-9309, L-9310 |
| `L-12102` | lemma | Multi-anchor Christoffel ladder and divided-difference reconstruction | `PROPOSED` | L-12101 |
| `O-12101` | observation | PR #103 positive-anchor candidate packets | `EMPIRICAL` | PRs #103, #112, L-12101, L-12102 |

## Proposed experiment registration

| ID | Path | Classification |
|---|---|---|
| `X-12101` | `experiments/X-12101-positive-anchor-ladder/` | exact rational synthetic checker plus ordinary PR #103 reconnaissance |

## Dependency edges

```text
PR #103 atomized count-deflated direct-xi table
        +
PR #112 directed degree-14 moment basis
        |
        v
L-12101 one positive anchor / one new moment
        |
        +--> PA-1 degree-15 two-sided gate
        |
        v
L-12102 sequential positive anchors
        |
        +--> PA-3 degree-17 packet
        +--> PA-7 degree-21 packet
        |
        v
exact H0/H1 vector witness or positive-definite closure
```

## Machine-readable controls

```text
positive synthetic verification SHA-256
0423469c646627ca5d9c5c2d21bf67638c3e7f36cf8f350b5b92d0aedd2cb196

negative synthetic verification SHA-256
3e9234290746c786f22522d0577ac76d4f85c7d4591d7b7156d8dd2d9552d6dc

old moment basis Git blob
174db078d3442e89d3be458a306b1122025cfd51

atomized primitive certificate Git blob
a02e20c083db8da00a9bd3629179b25c6469ea00
```

## Exact synthetic negative

The mutated two-anchor control has exact vector

```text
(7064, -6917, 1497, -85)
```

and exact `H0` quadratic

```text
-987306740595163 / 1734163200.
```

This validates the explicit square-witness path but is not a Riemann-xi result.

## Candidate packets

```text
PA-1  anchors {1}
      new primitives 1
      complete degree 15

PA-3  anchors {1/8,3/16,1/4}
      new primitives 3
      complete degree 17

PA-7  anchors {1/8,3/16,1/4,3/8,1/2,3/4,1}
      new primitives 7
      complete degree 21
```

Empirical PA-7 normalized minima:

```text
H0  3.8037205202e-13
H1  2.6692027329e-12.
```

No negative matrix was found.

## Review order

1. `claims/lemmas/L-12101-positive-anchor-one-moment-transform.md`
2. `claims/lemmas/L-12102-multi-anchor-christoffel-ladder.md`
3. `experiments/X-12101-positive-anchor-ladder/verify.py`
4. synthetic negative certificate and retained verification
5. synthetic positive certificate and retained verification
6. `claims/observations/O-12101-pr103-positive-anchor-reconnaissance.md`
7. `experiments/X-12101-positive-anchor-ladder/reconnaissance.py`
8. session report.

## Promotion boundary

- No counterexample or `Z-####` identifier is created.
- O-12101 remains ordinary high-precision reconnaissance.
- A negative production result needs exact rational vector freezing, directed
  direct-xi values, old-moment interval contraction, and independent primitive
  reproduction.
- A positive packet closes only its declared anchors, degree, ordinate, count
  profile, and normalization.
- Raw large-anchor Schur distance is explicitly excluded as a progress metric.
