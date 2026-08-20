## Purpose

Recover the unpublished critical-variation descent under a fresh namespace,
stacked on PR #664 at exact head
`14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`.

**The Riemann Hypothesis remains unproved.**

## Exact results

For

```text
beta(n)=mu(n)-1_(67|n)mu(n/67),
H_m(x)=sum_(n<=x) beta(n)n^(-1/2)(4sqrt(x/n)-3)^m,
G_2(u)=e^(-u)H_2(e^u),
```

this packet proves:

```text
H_2(x)>0 for every x>=1;

dG_2(u)
 = sum_n beta(n)n^(-3/2) delta_(log n)
   +3e^(-u)H_1(e^u)du;

3 integral_1^X (H_1(x))_- dx/x
 = integral_[0,log X] e^u d(-G_2^ac)_+(u);

G_2 has finite ordinary variation and a positive explicit limit;

subpower critical downward variation <=> RH.
```

## Binding firewall

Positive convergence and ordinary bounded variation of `G_2` do not control
its exponentially weighted downward variation. An explicit dyadic jump model
has finite ordinary variation but infinite critical weighted variation.

Thus the remaining gate is not a routine residual estimate left over from the
quadratic positivity theorem. It is exactly RH-scale cancellation.

## Replay

```bash
python3 experiments/X-99940-critical-variation/verify.py \
  --output /tmp/t99940.json
cmp /tmp/t99940.json \
  experiments/X-99940-critical-variation/results/verification.json
sha256sum -c T99940_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99940_CRITICAL_VARIATION_DESCENT
```

## Exact boundary

```text
quadratic SHARP positivity                 PROVED UNCONDITIONALLY
critical distributional descent            PROVED EXACT
ordinary BV and positive limit              PROVED EXACT
negative mass = weighted downward variation PROVED EXACT
critical subpower variation -> RH           PROVED EXACT
RH -> critical subpower variation           PROVED ON STANDARD LITTLEWOOD CRITERION
critical variation estimate                 OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
