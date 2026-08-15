# PR #496 / PR #500 comparison: `q=2` normalization and hybrid repair

## Frozen inputs

```text
PR #496  96f8a6b3cc3d474217633e16d4caa490a0aae518
PR #500  d73c1e7a1a482cac31581211a84db43cc34c824e
PR #495  50f45b46cbe3c471d6e702c41c7ef178b530e1ab
```

Neither frozen head is modified.

## Finding 1: exact separator, overbroad application

The complete `P_61` rough lift differs from the native packet at `q=2` by at least `log(4)/sqrt(134)>1/9` for `X>=536`. Under the additional full-rough-lift and small-correction hypotheses, the `X=10^16` calculation gives a final excess greater than `109/1200`.

Those hypotheses were never proved for PR #496, and PR #500's retained coupling is typed through a source tree rather than an explicit full rough-lift marginal. The earlier PR-specific falsifier is therefore withdrawn.

## Finding 2: the real normalization firewall

The paired least-prime source tree is split before signed observation and equals the native endpoint source. The `P_61` rough lift is formed after native observation and equals native plus a positive rough reservoir. The operations are not interchangeable after labels are erased.

Every complete producer must identify which object it realizes. The `q=2` calculation rejects a silent rough-lift substitution.

## Hybrid construction

Use the native paired source tree, the explicit PR #500 Hall/source/physical coupling, the PR #496 two-ledger signed comparison, and actual first-generation child packets.

The stronger specialization keeps the actual children internal to the single label-blind quantizer and retains the `<60989` bound.  The modular fallback exports them before root realization, realizes each against its own capacity, and stops:

```text
one-shot cost   <60989
fallback root   <60989
fallback child  <6039/8
fallback total  493951/8 <61744
```

No standard child capacity is substituted for an actual child response, no root correction is repeated, no port is needed, and no benchmark bridge is used.

## Status

The packet is candidate complete on its frozen analytic inputs. RH remains unproved pending independent reconstruction.
