# Exact first-broken-arrow audit for PR #510 and PR #522

Frozen heads:

```text
PR #509  e01daee9cdfea35d2a7d2591f1df6c8080084119
PR #510  b596b1abae9213366aab4cf3f2c911ff8cfab725
PR #522  3e8949af3e23b8563bfbc0cf8846820cc6c66d76
PR #508  4ae97dffd1f76ed3244b8f3028560ffa80663caf
review #516 2492bd48f8e2bafacfc04fc9237c06219b8c9bf8
```

## 1. PR #510 exact stopped-path normalization failure

A literal anchored occurrence `(m,k)` has native coefficient

\[
a_{X,m,k}=(km)^{-1/2}\log(X/(km)).
\]

For `m=1`, `k=67`, `X>67`, this is

\[
a_{X,1,67}=67^{-1/2}\log(X/67)>0.
\]

`L-91881.1` then multiplies by every stopped rough factor. The unique first owner is `(d,p)=(1,67)`, so before any causal split the displayed coefficient becomes

\[
a_{X,1,67}67^{-1/2}=67^{-1}\log(X/67),
\]

not the native coefficient. A later positive partition whose weights sum to one preserves this error.

Verdict: **FALSE AS WRITTEN**.

## 2. PR #522 unresolved normalization fork

`L-91880.4` writes

\[
a_X(\omega)=a_X^{native}(n,k)\prod_{r\in h}\gamma_r(c)
\]

and asserts that all path weights over one occurrence sum back to `a_X^{native}`. For `k=67`, the imported P61 coefficient is `67^{-1/2}`.

- If included in `gamma`, it duplicates the factor already present in the literal occurrence.
- If excluded, the theorem has not included the stopping coefficient and does not identify where placement supplies it.

Verdict: **UNPROVEN / GAP**.

Two valid-looking but mutually exclusive repair conventions exist:

```text
occurrence-level:
  route the fully weighted occurrence deterministically;

packet-level:
  start before k^(-1/2) and let the paired P61 identity supply it once.
```

A successor must choose one and prove its path marginal.

## 3. Review #516 remains binding

Both siblings consume the all-parameter Target-Lorenz conclusion

\[
B_\omega=R(U_\omega)-R(O_\omega)\ge0
\]

for every tail parameter and row. Review #516 found that PR #508's `rounded_transc_std<long double>` implementation did not establish interval inclusion: its exact policy/flags returned singleton finite-binary intervals for irrational square roots.

```text
FAIL_PR508_BOOST_ROUNDED_TRANSC_STD_INCLUSION_CONTRACT
7ffb59b9209d8d1db2527f363631708db9d4ed8ac89d45b793d2ee267d5ccfa8
```

This refutes the certificate contract, not the inequality. Neither sibling replaces the backend or supplies an analytic tail proof. Their one-leaf diagnostics are not an all-parameter certificate.

Verdict: **UNPROVEN / GAP**.

## 4. Top omission is not removed from the output coupling

Both siblings use retained bulk cells through `X-W-3`, put the entire complement in the anchored source, and sum all anchored paths into the physical row. In particular `m=X-1,k=1` is anchored and has positive coefficient

\[
(X-1)^{-1/2}\log(X/(X-1))>0.
\]

Later both invoke a fixed positive top omission to obtain

\[
(5033-4452)X^{-3/2}=581X^{-3/2}>0
\]

and the native-cost ledger. Neither first splits the anchored source into output and omitted marginals. The same atom cannot be both output and unused omission.

Verdict: **UNPROVEN / GAP**.

## 5. PR #522 repository-front-door rewrite

Frozen PR #509 root README blob:

```text
f0d9e9aadfbd7b192b07e3bd0762a94e6e4da97e
```

PR #522 root README blob:

```text
f2d66e62226ab53b95be4c11e9cb578989535fd6
```

The replacement is byte-identical to PR #522's standalone packet README. It erases the repository-wide navigation and is unrelated to the mathematical repair.

Verdict: **REQUEST CHANGES / REPOSITORY HYGIENE**. Revert the root file.

## Narrow surviving results

```text
hybrid finite/Volterra source identity       VERIFIED WITH FIXES
bulk rank-one source/output marginals        VERIFIED
PR #503 type firewall                        VERIFIED
whole-packet paired P61 identity             VERIFIED
abstract typed leaf compiler                 VERIFIED CONDITIONAL
one-signature/one-quantizer formalism        VERIFIED CONDITIONAL
common q/4q then detail, including q<K       VERIFIED CONDITIONAL
Y4 and endpoint arithmetic                   VERIFIED CONDITIONAL
```

Repairs remain **PROPOSED** until separately reviewed. RH remains unproved.
