# R-96201 — The imported PR #508 transcendental interval contract is not proof-grade

Claim ID: `R-96201`  
Status: **EXACT IMPORT DISPOSITION / REVIEW #516 ADOPTED**  
Created: 2026-08-16  
Frozen target: PR #508 at `4ae97dffd1f76ed3244b8f3028560ffa80663caf`

PR #508 uses
```cpp
boost::numeric::interval_lib::rounded_transc_std<long double>
```
and treats calls to the platform `sqrt` and `log` as directed enclosures. Review #516 produced singleton intervals for irrational inputs such as \(\sqrt2\), \(\sqrt3\), and \(\sqrt{67}\). A singleton finite-binary interval cannot contain an irrational exact value.

Therefore:

```text
event reduction and algebra                 retained;
reported numerical margins                  computational evidence;
directed transcendental inclusion           false;
L-93781 as a proof-grade certificate         not imported;
T-94000 anchored producer through PR #508    unproved.
```

A valid repair must use a correctly rounded library such as MPFR with explicit downward/upward rounding at every transcendental call, then propagate the resulting endpoint intervals through the full event sweep.

`X-96201` supplies such a source transformer and workflow contract. Until its full artifact passes and the actual endpoint/source registry is reconstructed, the anchored sector remains fail-closed.
