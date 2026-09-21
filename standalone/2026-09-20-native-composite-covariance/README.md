# NCG28 — a native gain for a growing part of composite covariance

**Status:** proposed component proofs; independent mathematical review required.
**RH and the full native scale-to-scale estimate remain open.**
Date: 20 September 2026. Continuation of #904 and strategy #902.

## What changed

This pass does not just enlarge the native finite test. It supplies an
all-cutoff, SOURCE-DEPENDENT upper bound for the combined centered composite
modes in a growing denominator window. The cost is a 4/3 power of the previous
reciprocal-Mobius energy, times a fixed logarithmic factor. All mutual cross
terms inside that sector are included.

The proof uses the actual Mobius identities to control divisibility amplitudes
by the previous energy. A non-sharp elementary additive large sieve then pays
for their full covariance; an exact contractive tail transform puts the result
in the reciprocal-innovation norm actually used by the Newton recursion.

The fixed-window statement is

    sum_(k>=Y+1) |sum_(q in A) B_q Z_q(k)|^2
       <= C H_Y^4 F_Y^(4/3),
    A any subset of {2,...,floor(Y^(10/11))}.

Here F_Y=sum_(k<=Y)m(k)^2, m(k)=sum_(n<=k)mu(n)/n; B_q is the exact
short-source convolution amplitude; and Z_q is the CENTERED Ramanujan harmonic
mode. These definitions, constants, and complete proofs are in PROOF.md.

A stronger physical-scale-dependent window reaches

    q <= floor((Y^4 X^6)^(1/11))

on the dyadic physical block [X,2X). Its full tail-transformed cost is
`C H_Y^5 F_Y^(4/3)`. It reaches denominators of order Y^(16/11) toward the
end of the native annulus. It is NOT computed by simply inserting a varying
cutoff into the fixed centered-mode sum: the exact future-activation correction
must be included. The packet derives it and tests its nonzero native values.

This is not the all-mode estimate. The high-composite transformed component,
including its signed interaction with the controlled sector, remains. No
fraction of RH completion is inferred from the denominator exponent.

## Read in this order

1. PROOF.md Sections 1–2: native amplitude estimate and composite divisibility.
2. Sections 3–5: whole covariance, the exact tail map, and moving windows.
3. Section 6: the complete Newton update and the still-unproved high component.
4. VALIDATION.md and results.json: actual finite evidence and limitations.
5. SOURCES.md: attribution, exact parent sources and reading boundary.

## Run

Python 3.10+; standard library only. No package installation, compiler, GPU,
zero table or external dataset is needed for this packet.

```sh
cd standalone/2026-09-20-native-composite-covariance
python -B check.py --check results.json
python -B test_check.py
python -O -B check.py --check results.json
python -O -B test_check.py
```

The default finite corpus is Y=7,15,31,63,95. For a smaller complete test:

```sh
python -B check.py --write small.json --cutoffs 7 15
python -B check.py --check small.json --cutoffs 7 15
```

The bounded checker intentionally rejects Y outside 2,...,127 and an excessive
harmonic campaign. This limit is a resource policy, not the theorem's scope.
It streams exact harmonic enclosures and retains only requested large indices.

## Finite result to interpret correctly

At Y=95, on ALL 9,120 new reciprocal-energy cells through B=9,215, descriptive
decimals of the directed enclosures are:

| Quantity | Value |
|---|---:|
| Actual native F increment | 0.1342803012570623 |
| Moving low-composite energy | 0.0078024259056433 |
| Remaining high-composite energy | 0.1127957612613119 |
| Twice their covariance | +0.0123360949046636 |
| Completion-channel energy | 0.0004154105870615 |

The prime channel and every other mixed term are retained in results.json.
The first moving-cutoff correction is nonzero, about 0.0002928051727676.
The high component is evaluated by exact complementary algebra after the full
Newton prefix has been reconstructed and checked; it is not an independent
large-denominator spectral summation. No observed trend is extrapolated.

## Preservation and scope

The parent DSE27 packet, its original source/validation receipts, RCB26, NSR26,
main, canonical statuses, trusted formal sources and workflows are unchanged.
This packet does not rerun the parent's large 16,777,215-cell campaign.

The general Ramanujan and large-sieve tools are classical. The proposed new
research content is their source-energy composition and the precise nonlinear
window budgets, not a claim of a new general large sieve or Ramanujan theory.
A broad novelty audit and external mathematical review remain outstanding.
