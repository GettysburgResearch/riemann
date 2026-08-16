# R-93786 — `rounded_transc_std` is not by itself a directed inclusion contract

Refutation ID: `R-93786`  
Status: **EXACT IMPLEMENTATION FIREWALL**  
Frozen target: PR #508 at `4ae97dffd1f76ed3244b8f3028560ffa80663caf`  
RH status: **unproved**

`X-93780` uses Boost.Numeric.Interval's `rounded_transc_std<long double>` and standard `sqrt`/`log` under hardware rounding. Boost's documentation states that this policy requires the standard transcendental functions to respect the current rounding mode and warns that this is rarely the case.

Under the exact compile flags in `X-93780`, the attached targeted probe returns singleton intervals for `sqrt([2,2])`, `sqrt([3,3])`, `sqrt([67,67])`, and `sqrt([166000,166000])` on the recorded platform. Every radicand is a nonsquare integer, so its square root is irrational. A singleton finite binary floating interval is rational and cannot contain that exact value.

Therefore the stated policy does not establish the interval inclusion property. This refutes the **certificate contract**, not the Target-Lorenz tail inequality itself. A valid successor must use an inclusion-certified transcendental backend or exact precomputed primitive enclosures.

```text
FAIL_PR508_BOOST_ROUNDED_TRANSC_STD_INCLUSION_CONTRACT
7ffb59b9209d8d1db2527f363631708db9d4ed8ac89d45b793d2ee267d5ccfa8
```
