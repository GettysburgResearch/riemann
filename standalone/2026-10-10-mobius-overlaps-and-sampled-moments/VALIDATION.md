# Validation and finite scope

The four released programs were inspected and executed from their final packet paths under Python **3.12.14**, both normally and with `-O`. All eight runs exited successfully. Each normal/optimized pair produced byte-identical JSON, also identical to the released result file. The root replay receipt is [results/release_replay.json](results/release_replay.json).

There are **392,318 explicit finite acceptance predicates** across the four diagnostics. Every gate raises an explicit exception on failure; optimization does not remove acceptance conditions. All arithmetic is exact integer, rational, or integer-pair cyclotomic arithmetic. No floating-point error contract is involved.

## Coverage by program

| Program | Predicates | What is actually covered |
| --- | ---: | --- |
| [Quadratic masks](checks/check_quadratic_masks.py) | 35,737 | Actual selected prime ideals of norms 7 and 13; six units; 81 square factorizations; 1,944 literal square-part identities including overlapping square base/remainder; 30,940 incidence identities in degrees 1–4; finite dyadic switches inside and outside the physical range; exact degree-three exponent endpoints |
| [Möbius overlaps](checks/check_mobius_overlaps.py) | 31,955 | Primitive sextic residue symbols at norms 7 and 13; designated forward coefficients through local exponent two in stated degrees 2, 3, 4, 6; mixed positive/inverse correction and mask-prime exceptions; 144 specified two-prime tuples over all 91 simultaneous residues; exact affine cutoff certificates |
| [Scale sampling](checks/check_scale_sampling.py) | 21,950 | Exact complex polynomials represented by pairs of rationals; 28 nonuniform retained-set/order panels; integrated polynomial energies at p=2; 107 finite-grid panels including endpoint reuse; factorial bounds and explicit countermodels to omitted hypotheses |
| [Reflected blocks](checks/check_reflected_blocks.py) | 302,676 | Actual selected prime ideals of norms 7, 13, 19, 31; all 65,536 k/g/e/n tuples in the stated 16-ideal panel; literal moving-mask and gcd identities; 160,000 divisor-phase factorizations; complete 91-by-91 two-prime residue pairs; exact six-term powers and local row valuations 1–30 |

The two-prime CRT panels cover the selected quotient fields, not every residue in the larger ring quotient by the rational integer 91. The finite ideal-mask panels are not all rows below an arbitrary height. The reports list their actual coverage and limits explicitly.

The overlap and sampling reports bind the exact associated proof bytes. The other two reports bind their checker source bytes, with their proof associations recorded in [PROVENANCE.json](PROVENANCE.json). A content hash authenticates which file was used; it does not prove its mathematics. The source lock separately verifies the local repository-source bytes against the Git blobs returned at the exact GitHub commits.

## Negative controls

The diagnostics explicitly retain examples where replacing a principal character power at a nonunit by one gives the wrong answer. The reflected checker also detects deletion of the moving row mask and replacement of a squared product by its radical. The overlap checker distinguishes vanished unmasked one-axis correction terms from the nonzero one-axis terms at an excluded prime.

The sampling checker includes a complex polynomial for which no real mean-value point supplies the complex secant, a clustered-node instability, an unobserved-gap example despite positive total retained measure, and a smooth constant row multiplied by a discontinuous row-entry indicator. These countermodels diagnose invalid omissions of hypotheses. They do not contradict the remainder-inclusive interpolation theorem, and the finite gap example is explicitly only a piecewise polynomial with the stated finite regularity.

The exact exponent comparisons use `Fraction`. When a report checks both endpoints of an affine expression, affinity supplies the conclusion on that displayed interval. These algebraic certificates do not establish the analytic inequality to which the exponents are later applied. The valuation panel stops at 30; the infinite local tails and strict endpoint exclusions are proved in the mathematical note, not extrapolated from that panel.

## Replay from this packet directory

The following driver executes the released checkers in both modes in a fresh temporary directory and compares every result with the published JSON. It uses explicit exceptions rather than assertions.

```sh
python - <<'PY'
from pathlib import Path
import json, subprocess, sys, tempfile

p = Path.cwd()
jobs = [
    ("quadratic", "checks/check_quadratic_masks.py", [],
     "--output", "results/quadratic_masks.json", 35737),
    ("overlap", "checks/check_mobius_overlaps.py",
     ["--note", str(p / "MOBIUS_OVERLAP_TAILS.md")],
     "--json", "results/mobius_overlaps.json", 31955),
    ("sampling", "checks/check_scale_sampling.py",
     ["--note", str(p / "SAMPLED_MOMENT_CRITERION.md")],
     "--output", "results/scale_sampling.json", 21950),
    ("theta", "checks/check_reflected_blocks.py", [],
     "--output", "results/reflected_blocks.json", 302676),
]
with tempfile.TemporaryDirectory(prefix="riemann-moment-replay-") as temp:
    for name, script, args, flag, reference, count in jobs:
        expected = (p / reference).read_bytes()
        for optimized in (False, True):
            output = Path(temp) / (name + str(optimized) + ".json")
            command = [sys.executable] + (["-O"] if optimized else [])
            command += [str(p / script)] + args + [flag, str(output)]
            run = subprocess.run(command, capture_output=True, text=True)
            if run.returncode:
                raise RuntimeError(name + ": " + run.stderr)
            actual = output.read_bytes()
            if actual != expected:
                raise RuntimeError(name + ": published-result mismatch")
            report = json.loads(actual)
            total = report.get("total_checks", report.get("total_predicates"))
            if report.get("status") != "PASS" or total != count:
                raise RuntimeError(name + ": coverage/result mismatch")
        print(name, count, "PASS in both modes; published bytes match")
PY
```

All programs use only the Python standard library. Their results have no absolute output paths, timestamps, or optimization-mode field, so exact renamed copies reproduce the same JSON. Pass the displayed `--note` arguments for the relocated overlap and sampling programs. The recorded overlap note hash is part of the default acceptance contract; the replay above does not override it.

## What was not verified by computation

None of the programs proves a quadratic, cubic or sextic large sieve; uniform Möbius cancellation; the reciprocal-L premise; infinite Euler-product convergence; theta automorphy or all-cusp reflection; an infinite moment estimate; or a zero-free theorem. The sampling polynomial panels do not certify every measurable retained set or the infinite convolution. Those statements have analytic proofs in the four notes and the explicitly assumed source interfaces.

No fresh upstream Lean build, proof-assistant verification, external human peer review, or promotion to the repository's integrated results is claimed. Review roles and proof scopes are recorded separately in [REVIEW.md](REVIEW.md). The final publication checks verify the actual Git tree and returned file bytes; those transport checks are not mathematical acceptance.

