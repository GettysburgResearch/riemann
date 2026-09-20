# MCB31 — collective control inside the microscopic composite band

> **Repository publication scope:** this directory contains the mathematical
> documentation only. The complete nine-file executable companion is retained
> in the conversation artifact `MCB31_microscopic_covariance_packet.zip`.
> Its arithmetic-module upload was blocked by the tool; no alternate upload
> route for that module was attempted. References below to code, receipts and
> commands describe that tested local companion, not files present here.
> No executable repository replay is claimed for this documentation-only commit.

**Proposed component proofs. Independent mathematical review required.**
The native subquadratic recurrence and RH remain open. This is an add-only
continuation of #904 / strategy #902, not a new accepted mathematical baseline.
Reading parent: `d0d7ad05f9d4504e9d752518b34a9fd0609a06f7`.

## What changed

NCL29 controls pure prime powers and frequencies away from zero. This packet
estimates the opposite end: a complete smoothly selected band containing
EVERY available reduced fraction of distance at most `H/X` from an integer,
on an observation block `[X,2X)`. All denominators and internal cross terms
are included. The transition from weight one to zero over `(H/X,2H/X)` is
part of the definition; this is not a theorem for an uncharged sharp cutoff.

For a finite reciprocal-balanced source c, supported through L, let

```
x_r = sum_(n<=r)c(n)/n,
a = max(0, floor(X/(2HL))-1),
E_local = sum_(r=a+1)^(L-1) x_r^2.
```

For integers `H>=1`, `X>=8H`, `L^2<=8X`, the complete microscopic function U
satisfies on every assigned block `X<=k<=M<2X`

```
sum U(k)^2 <= 2^21 H^4 E_local^2.
```

There is no coefficient-cap assumption for this theorem and no power of X
on the right. It is a bound for the COMBINED covariance, not its diagonal.
Every value includes the full centered harmonic tail; the norm here is on
the assigned finite block, not the entire infinite future of the same mask.

For the actual native square step, scale-local short sources and a bounded
overlap argument give the stronger accounting

```
||U||^2 <= 2^23 H^4 N_H F_Y Delta_max,
F_Y = sum_(k<=Y)(sum_(n<=k)mu(n)/n)^2,
N_H = 12 + 2 ceil(log_2 H),
Delta_j = F_(y_j) - F_max(0,floor(y_j/(8H))-1),
Delta_max = max_j Delta_j.
```

This is linear in total previous energy times the largest recent input
energy. Every y_j is at most Y. The completion tail is paid by recent native
energy, and each input cell is counted a bounded number of times. No future
Mobius values are used by the short-source producer.

A further bound pays the weighted prime-power portion, so the same result
applies to the dense microscopic mixed-prime band with an additional
polylogarithmic term. Its covariance with NCL29's already controlled part
has a linear-in-F_Y budget, up to logarithms.

## The limitation is mathematical, not merely numerical

`Delta_max<=F_Y` gives exponent TWO in the worst case. No bound forcing a
native subquadratic relation between these quantities is proved. A new
analytic counterfamily attains quadratic growth within the capped nonnative
class, even with c(1)=1 and agreement with mu through five. It fails actual
divisor inversion at six. Thus the energy/calculus argument cannot simply be
sharpened generically to exponent below two.

The intermediate frequencies between order `1/X` and the earlier far-angle
window remain. A complete two-parameter bound is supplied for the full native
block, but it retains the explicit term `K^4 (X/H) H_L^9`. This is not an
RH-strength full covariance estimate. Neither that term nor any covariance
with the remaining component is declared zero.

The main new mechanism is to UNREDUCE fractions into actual product indices,
then integrate the two source differences before taking a norm. The exact
centered-mode derivative and a C^2 mask control the mixed product derivative.
See PROOF.md Sections 1-3, then the limits in Sections 4-6.

## Complete finite native panel

At Y=31, H=1, every one of the 992 new cells through B=1023 is covered.
Descriptive decimals from outward enclosures are:

| Quantity | Value |
|---|---:|
| Native F increment | 0.0990995899971780... |
| Combined microscopic energy | 0.0172795454867852... |
| Complete complementary energy | 0.0676772040867840... |
| Twice their covariance | +0.0141428404236087... |

The covariance is POSITIVE. The smaller micro sector is not an orthogonal
projection in this physical interval norm. The complement is evaluated by
exact subtraction from independently checked native Newton output, not by a
second exhaustive spectral sum. Prime-power/mixed-prime and native semiprime
subledgers are also retained in the reconstructed report.

## Reproduce the separately supplied executable companion

No package installation is needed; use Python 3.10 or newer and the standard
library. After extracting the conversation ZIP, from its packet directory:

```sh
python -S -B check.py --check-receipt receipt.json --write report.json
python -O -S -B check.py --check-receipt receipt.json
python -S -B test_check.py
python -O -S -B test_check.py
```

The full report is regenerated in that companion. Its `receipt.json`
binds its complete canonical SHA256, producer/backend hashes, coverage and
selected output intervals. A quick campaign is only a test fixture and is
explicitly different from the default full report.

The default campaign uses seven distinct block evaluations, 1,520 observation
cells and 3,033 Newton coefficient checks, counting overlaps. Largest native
endpoint: 1,023. The 12-method suites, arithmetic lineage, exact source reading,
replay boundaries and packaging checks are in VALIDATION.md and SOURCES.md.
A finite checker does not prove the infinite component estimates.

## Exact companion identity

The local executable packet contains nine files / 64,815 bytes; its Git subtree
is `865d4dbc1713143a7516b3e0798c674eb704273c`. The full report SHA256 is
`825800dd0f0759d787944daa23fe6cb31e5df7275b23a418e3d961e238c3c4d9`.
Only PROOF.md is byte-identical between this documentation directory and that
companion. The other three Markdown files add this publication boundary.
Do not claim that the executable subtree is present in this commit.
