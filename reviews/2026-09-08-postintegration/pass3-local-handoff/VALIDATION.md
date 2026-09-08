# Executed evidence and exact limitations

## Complete reviewer-written numerical/control run

From this directory:

```sh
python3 -I -S -B independent_checks.py --output /tmp/riemann-pass3-normal.json
python3 -I -S -B -O independent_checks.py --output /tmp/riemann-pass3-optimized.json
cmp /tmp/riemann-pass3-normal.json /tmp/riemann-pass3-optimized.json
```

Both full runs completed. The retained `evidence/independent-normal.json` and `evidence/independent-optimized.json` agree byte-for-byte. No author module, zeta oracle, floating acceptance, quadrature package, or external network is used by this checker.

| Group | Accepting assertions | Scope |
|---|---:|---|
| Primitive interval contracts | 73 | Exact rational arithmetic; directed elementary log/pi/gamma constructions and domain controls |
| Prime capacities | 8 | Complete 63-mode sums for each of two P=13 reservoirs; root residual signs at both endpoints |
| Rational product spectra | 74 | Synthetic rational-rate product bases, root Green and killed Poisson controls |
| ANT profile cells | 4,095 | Exact cell integration through 4096; these are coverage units, not independent theorems |
| Profile enclosure | 3 | Full finite integral plus the stated analytic infinite-tail bound |
| Native source identities | 454 | Finite Möbius norm/projection/work and complete prime-power graph identities |
| Tail variations | 217 | Three zero jets, diagonal norm and physical lower intervals for bounded Y |
| Finite algebra | 31 | Lyapunov and Laurent-residue/normalization identities, elementary bootstrap controls |
| Scalar certificates | 11 | HT constants/range budgets, actual unshifted m=2 sign, two PR trials, actual N=3 work |
| **Total** | **4,966** | Different units are not combined into a theorem count |

Numerical primitives use Fractions and 160-bit outward dyadics. Logs use a range-reduced atanh series with a complete positive remainder; pi uses Machin arctangent remainders. Gamma is bounded from a harmonic sum and elementary upper/lower inequalities. The large rational endpoints, not the printed decimals, implement acceptance. The P=13 results use actual logarithmic prime rates; the separate rational-rate spectral controls are explicitly synthetic.

The profile tail is `10000/(3*4096^3)`. The p4 trial uses an independently bounded sum over every future period and deliberately gives a wider interval than the source's particular enclosure. It still proves the stated coarse trial bracket; it is not an optimal minimum.

## What has not been run or established

No complete author package, source-lock checker, full author CLI/rejection suite, native Windows run, whole Riemann checkout, remote CI, Lean/compiler/axiom audit, high-zero census or broad prime campaign was executed. The original source manuscripts were read through exact GitHub refs; FILES.tsv records connector-reported blob identities. That is not a local authentication of every file on those branches.

In particular, RN's four optimized two-jet minima, RC's three balance-only minima in the controlling published review, the older CD/FR trials, SSQ's finite prime prefixes and MW's 65,536-event campaign are not newly replayed. WP/IE's earlier reviewed numerical subsets are not rerun here, and their original whole-package obligations are not removed by preservation.

The finite checks do not prove the infinite analytic conclusions: Landau bootstrap, all-scale regularity, capacity asymptotics, countable self-adjoint domains, source-space statements and imported classical results remain paper-level review at their stated hypotheses. A successful synthetic example is not an arithmetic upper bound.

The delivery packaging check is recorded separately in EXECUTION.json. It checks that an add-only patch preserves prior-review sentinels and reproduces this local payload, not that a repository integration or full-checkout validator passed.
