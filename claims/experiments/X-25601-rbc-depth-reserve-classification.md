# X-25601 — Exact RBC depth/reserve classification regression

Claim ID: `X-25601`  
Status: **EXACT SYNTHETIC ALGEBRA / NO RH VERDICT**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256

The standard-library verifier in

```text
experiments/X-25601-rbc-depth-reserve/
```

replays the nilpotent depth inverse, logarithmic derivative, source-synthesis
orientation, zero Schur reserve, cyclic color Parseval identity, meromorphic
charge controls, and far-right exponent cancellation using integers and
`fractions.Fraction` only.

Retained result:

```text
K                              4
forward-shift synthesis anchor e_(K-1)
finite tail                    1/45
aggregate Schur reserve        0
nonzero packet-kernel control  98/121
color/depth Parseval energy    11936689/1587600
meromorphic quotient rank      1
far-right physical exponent    1/2
mutation tests                 8/8 PASS
proof-object SHA-256
f9804f4155ea5f88754f6bafc8b988542f3472b9570188269d283d876092a3be
```

The checker deliberately rejects the first-row orientation for the declared
forward shift, a deleted top depth, a false positive reserve, broken Fourier
orthogonality, simultaneous deletion of the base and residual pole, an
unpaid vertical-line deweighting, rank/scale conflation, and a bad digest.

It does not evaluate the Riemann zeta function or prove the anchor shell
estimate.
