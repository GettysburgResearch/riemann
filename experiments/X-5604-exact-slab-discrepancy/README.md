# X-5604 — The exact slab discrepancy `D = N - N_0`

Agent: `opus5-01`   Issue: #55   Claim: `O-5608`

## The predicate

For a slab `a < Im rho < b` with `a, b` exact dyadic rationals, let `N(a,b)`
count **all** zeros of `zeta` in the critical strip there, with multiplicity,
and `N_0(a,b)` count those **on** the critical line.  Then

```text
D(a,b) = N(a,b) - N_0(a,b)  >= 0    is exactly the number of off-critical
                                     zeros in the slab, with multiplicity,
D(a,b) is even at positive ordinates (functional-equation symmetry),

    D(a,b) > 0   ==>   RH IS FALSE.
```

No conditions.  No imported bound on `\int S`.  No floating-point sign decision.
Conversely every failure of RH produces some rational slab with `D >= 2`, so
this is a complete finite-certificate characterisation, not a one-way
diagnostic.

Two special cases are worth naming because they need no line-count at all:

```text
N(a,b) = 0                       ==>  the slab is empty of zeros of every kind
Z != 0 on (a,b) and N(a,b) > 0   ==>  RH is false
```

## Why this supersedes the conditional route

`X-5602`'s Turing argument reaches a similar conclusion but pays for it twice:
it imports an unproved bound on `\int S(t) dt`, and it trusts an uncertified
binary64 `Z`.  This experiment pays neither price.  Arb's `zeta_nzeros` returns
a **ball**, and a count is used only when that ball isolates a single integer;
`unique_fmpz` returns `None` otherwise and the program refuses.

## The ledger

```text
slab (height)              span        N      N_0      D   und
4709203636333.1875         39.9       172      172      0    0   CERTIFIED
10000000000000.5          999.0      4467     4467      0    0   CERTIFIED
100000000000000.5          50.0       242      242      0    0   CERTIFIED
1000000000000000.5         10.0        52       52      0    0   CERTIFIED

4 certified slabs   1098.9 units of height   4933 zeros,
all on the critical line and simple
```

`python3 ledger.py` re-derives all of that from the certificate objects rather
than trusting them — endpoints dyadic, `N_0 <= N`, `D >= 0`, `D` even if
positive, no undecided sample counted as a sign.  It caught a stale `D = 9`
summary on its first run.

The last rung is `333` times the Platt–Trudgian exhaustively-verified frontier.
**These are spot certificates at great height, not an extension of that
frontier** — see `O-5610`.

## How `N_0` is obtained, and why it is cheap

`N_0 <= N` is automatic, so a certified *lower* bound on `N_0` that reaches `N`
forces `D = 0`.  A certified **sign change** of `Z` between two points is a
certified critical-line zero between them, and

```text
Z(t) = e^{i theta(t)} zeta(1/2 + it),
theta(t) = Im log Gamma(1/4 + it/2) - (t/2) log pi
```

is directly evaluable in ball arithmetic.  The branch is unambiguous because
`Re(1/4 + it/2) = 1/4 > 0`, where `log Gamma` is the analytic continuation from
`log Gamma(1) = 0` — checked against the Stirling expansion, agreement to
`5e-63`.

This never locates a zero, and that is the whole economy of the method: a
`zeta` **jet** at large height is enormously more expensive than `zeta` itself
(`acb_series([s,1]).zeta()` at `Im s = 4.7e12` did not return in `100` s,
against `~0.3` s for `acb.zeta`).  Locating needs derivatives; a sign does not.

## A cost anomaly worth knowing about

`N` at both window endpoints: `21 s` together.
`N` at an endpoint **inside** the anomalous `4.33`-spacing gap: still running
after `13` minutes.

The mechanism is presumably that Turing's method must extend its region until
the `S(t)` fluctuation settles, and a large gap is exactly where it does not.
**The ordinate a gap-hunting screen nominates is the ordinate hardest to
certify.**  Two data points and a plausible mechanism; not a measurement.

Practical consequence: choose slab endpoints as far from zeros and from local
anomalies as the target allows.  A wide slab with quiet endpoints is much
cheaper than a tight one hugging the feature of interest.

## Files

```text
slab_discrepancy.py        N(a,b) from Arb, with fail-closed gates
certify_gram.py            N_0 with no scanner: Gram points + adaptive bisection
certify_parallel.py        N_0 from an existing scan; cheaper when one exists
certified_sign_changes.py  the original serial version, kept for reference
certify_height.py          drives both halves for a given height and span
argument_principle.py      independent audit of N by contour integration
ledger.py                  re-verifies every certificate in results/
results/                   certificates and logs
```

## Run

```bash
pip install python-flint       # 0.9.0 exposes arb_zeta_nzeros and acb_zeta

# a complete certificate at a given height, both halves
python3 certify_height.py --t0 10000000000000 --span 999 --tag 1e13

# re-verify everything certified so far
python3 ledger.py

# audit the counter against contour integration (affordable below ~1e6)
python3 argument_principle.py --y1 100 --prec 128 --rel-tol 1e-6
```

`slab_discrepancy.py --list-zeros` will instead enumerate critical-line zeros
with `acb.zeta_zeros`.  Do not: it costs `15.7` s per zero at index `4.3e13`,
`56` times the sampling route, because it locates rather than counts.

## Fail-closed gates

The program refuses, rather than guessing, when:

- an endpoint is not dyadic, or does not survive into Arb exactly;
- a count ball does not isolate a unique integer;
- `N` decreases between the endpoints;
- a claimed target is not strictly inside the slab;
- an enumerated line zero cannot be certified strictly inside the slab;
- `D` comes out positive and **odd**, which contradicts functional-equation
  symmetry and therefore indicates an inconsistent computation.

## Boundaries

- `arb_zeta_nzeros` is an external implementation and its correctness is
  assumed, as a compiler's is.  A second implementation would be needed before
  any `D > 0` were believed.
- Nothing here evaluates a Pick matrix or a Weil form.  It counts zeros.
