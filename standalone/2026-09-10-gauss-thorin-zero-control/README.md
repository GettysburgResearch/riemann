# GZC26: local complex-zero control from positive Gauss–Thorin defects

**Proposed component mathematics and finite directed certificates. Independent review required. RH is not proved.**

This add-only continuation of PR #851 uses the exact source in the preceding GTP26 packet. It supplies a positive real-integral upper bound for the complete complex Mellin error, a fully bounded log-Laplace evaluator, and strict Rouche predicates on three complete disks.

| Target | Exact rational centre | Radius | Result submitted for review |
|---|---|---|---|
| Raw third seed F_3 | `0.471003433 + 14.138525882 i` | `1e-6` | one simple off-critical zero |
| Reflected third seed A_3 | `1/2 + 14.138974966 i` | `1e-6` | one simple critical-line zero |
| Literal xi, transferred from A_10 | `1/2 + 14.134725 i` | `1e-5` | one simple critical-line zero |

The first result refutes **unsymmetrized** seed zero safety, not RH or the parent's reflected-seed target. The last is a new certificate through this source construction for a familiar low zero, not discovery of a new zero, a height record, or a census below that height. Exact line membership comes from reflection and a complete count of one; it is not a small floating real part.

Start with [PROOF.md](PROOF.md), especially (10)–(15), (18)–(25), and the scope discussion in Section 7. [SOURCES.json](SOURCES.json) gives exact provenance; [VALIDATION.md](VALIDATION.md) records execution and its limits.

## Reproduce

Python standard library only, from an intact extracted packet:

```sh
python -I -S -B check.py --check results.json --self-test
python -I -S -B -O check.py --check results.json --self-test
python -I -S -B tests.py
python -I -S -B -O tests.py
```

Each full check first authenticates the exact file inventory and hashes, regenerates the source polynomials and Gaussian nodes/weights, reconstructs the entire directed receipt, and checks all three strict disk inequalities. `--self-test` refuses eight changed receipts through the same acceptance function; it does not launch eight complete checker processes. The separate seven-method suite tests elementary arithmetic, gamma recurrence, an independent Bernoulli formula for source moments, malformed primitive brackets, and modulus bounds.

`--emit PATH` is a producer command, not an acceptance receipt. `--authenticate-only` checks bytes and inventory only, not mathematical predicates. No float, zeta package, downloaded zero table, or external numerical service enters acceptance. Integer dyadic intervals use 288 fractional bits and explicit analytic remainders. The code is not a proof assistant and has not received independent review.

## What remains missing

The new bounds protect isolated zeros and certify local counts. They do not exclude off-line zeros elsewhere or establish no-collision/zero-confinement at unbounded order and height. The all-order reflected-seed programme is still open. Main, accepted scientific status, previous research files, and formal sources are unchanged.
