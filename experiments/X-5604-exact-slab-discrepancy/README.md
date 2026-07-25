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

## Result so far

```text
a = 75347258181331 / 2^4  = 4709203636333.1875
b = 37673629090985 / 2^3  = 4709203636373.125
PR #71 ordinate T = 20225875608341108140435/2^32 strictly inside

N(a) = 19743642385928        (ball radius 0)
N(b) = 19743642386100        (ball radius 0)
N(a,b) = 172                 21.0 s at 192 bits
```

Unconditional.  `N_0` — and therefore `D` — is **not** yet computed; see
`O-5608` for what may and may not be concluded, and for two independent
confirmations this produced along the way (`N(a)` matches `turing.py`'s
independently derived `c_est` exactly, and `|Z| = |zeta(1/2+it)|` certifies the
`259.778` anomaly to `1e-15`).

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
slab_discrepancy.py   the predicate, with fail-closed gates
run_window.sh         the 40-unit window around the PR #71 ordinate
run_gap.sh            a tight slab inside the large gap (slow; see above)
results/              certificates and logs
```

## Run

```bash
pip install python-flint          # 0.9.0 exposes arb_zeta_nzeros, acb_dirichlet_zeta_zeros
python3 slab_discrepancy.py --a 75347258181331/16 --b 37673629090985/8 \
    --target 20225875608341108140435/4294967296 --prec 192 \
    --out results/window-pr71.json
```

`--list-zeros` additionally enumerates the critical-line zeros and computes `D`.
Expect it to be slow at index `~2e13`.

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
