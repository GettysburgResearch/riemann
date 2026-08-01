# X-16206 — First source-bound directed CCM interval-ODE packet

Status: **real radial primitive emitted; complete cofinal CCM certificate not yet promoted**  
Agent: `gpt56-pro-13`  
Parent: Issue #162 / draft PR #164

## Production packet

The emitter fixes

```text
gamma = 100000,
gamma = 2*pi*lambda^2,
126 < lambda < 127,
modes = 0,4,8,12.
```

It produces four separation intervals for the infinite even Legendre-Jacobi
operator. SciPy only nominates centers. Each interval is certified by exact Arb
Sturm counts on a 65,536-dimensional principal block and a rigorous Schur bound
for the infinite tail.

For every interval the regular radial solution at

```text
z0 = 1 + 1/gamma
```

is enclosed by a 700-term Arb Taylor model in the separation parameter, with a
geometric tail. The Bessel comparison data use an Arb integral after the
endpoint-regularizing substitution `z=1+u^2`.

The largest certified pole mismatch in the scaled Cauchy state is below
`1.83e-7`.

## Directed radial fields

The primitive records:

- separation and sigma-squared intervals;
- exact infinite-Jacobi count ledgers;
- regular pole Cauchy balls;
- Liouville and Bessel Cauchy balls;
- transition bound `501/500`;
- normalized radial residual `181/100000`;
- frequency/horizontal residual `1/500`;
- radial tail energy `1/1000` beyond the retained Bessel cutoff;
- logarithmic derivative tail energy `1/10`;
- source, producer, primitive, phase, endpoint, Gram, and support-ledger digests.

The generated wrapper satisfies every rational inequality checked by the
existing `X-16204` consumer. `verify_bindings.py` additionally checks that the
consumer fields refer to the exact emitted producer, source object, primitive
object, and primitive file.

## Important proof boundary

This pass closes the missing **radial** producer for one real packet. The
profile-Gram and support-average files are explicitly classified as analytic
ledgers inherited from the existing wrapper, not as newly evaluated zeta/PSWF
production data. Consequently this is not yet a complete cofinal RH certificate.

The next production step is to replace those two ledgers by directed values for
the same source packet, then rerun this emitter on the unbounded gamma schedule
in `results/cofinal-schedule.json`.

## Replay

```bash
python emit_directed_interval_ode.py --output-dir results
python verify_bindings.py \
  --producer emit_directed_interval_ode.py \
  --primitive results/primitive.json \
  --wrapper results/wrapper-certificate.json
python ../X-16204-directed-cofinal-wrapper/verify.py \
  results/wrapper-certificate.json \
  --output results/wrapper-verification.json
```
