# Paired-kernel type stability: integration report

Date: 2026-08-13  
Branch base: `15edbccaeedd96cfa76783713b41715d8ad7d8e5`  
Frozen companion branch: `23aa9adc48a6c3176b799944dfbac11e665407ef`  
Verdict: **new exact recursive theorem; candidate factor-54 closure narrowed to one merged one-step audit; RH unproved**

## Executive result

The hazard branch produced by the binary return does not have to be forced back
into the single common `W_Psi/W_S` measure cone.  Carry it as its own positive
paired target/score type.

For any positive paired affine kernels, arbitrary pointwise subprobability rough
children give exact positive residuals in target, score, and every finite
component row.  Child target masses form a subprobability vector.  Even when the
residual score is smaller than the residual target, the positive local debt is
at most the residual target and hence at most one after target normalization.

This yields an actual-packet typed consumer.  It avoids the invalid
restriction-loss proportionality that invalidated an earlier proposed closure.

## Frozen binary-return checks

Writing \(r=p^{-1/2}\) and \(z=\sqrt{x/n}\), exact algebra gives

\[
T_s+T_h=4z-3,
\]

\[
S_s+S_h=5z-3+r(1-r)(z-1),
\]

and

\[
1/2\le T_s/S_s<1,\qquad 1/2\le T_h/S_h<2.
\]

Thus both outputs are uniformly positive physical types, including the limit of
large rough primes.

## Consequence

The all-generation “channel-type stability” item on the binary-return branch is
removed.  Once its one-prime target-Hall row producer has emitted the two
positive types, `L-91540` carries them recursively without changing type and
`T-91541` closes the branching score estimate.

The remaining uncertainty is concentrated in four merge interfaces:

1. exact normalization of the PR `#416` target-Hall measures against the live
   `P_61` one-prime packet;
2. exact row coefficient under affine child pushforward;
3. one-use accounting of the common observation port after target
   normalization;
4. a merged replay of all directed Hall and finite-row certificates.

This is deliberately not labeled an RH proof.

## Replay

```bash
cd experiments/X-91540-paired-kernel-typed-closure
python3 verify.py
sha256sum -c SHA256SUMS
```

Retained result:

```text
PASS_PAIRED_KERNEL_TYPED_BRANCHING
checks: 2011
```

The replay certifies symbolic algebra and exact finite diagnostics only.
