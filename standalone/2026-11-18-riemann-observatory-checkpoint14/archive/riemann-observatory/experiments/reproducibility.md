# Reproducibility

Python3.12 with standard library suffices for exact rational/integer scripts. mpmath is used for supplementary high-precision computations; sympy or other imports are documented inside individual scripts. No Lean/Sage/Arb build was performed. Noζ verification computation from a cited paper was rerun.

From the archive root:

```bash
python experiments/code/lagarias_finite.py
python experiments/code/lagarias_review_fraction.py
python experiments/code/li_advocate.py
python experiments/code/li_skeptic.py
python experiments/code/toy_advocate_exact.py
python experiments/code/multiplicity_general_exact.py
python experiments/code/clustered_root_transition.py
python experiments/code/spectral_counting_barrier.py
python experiments/code/analytic_checks.py
python scripts/build_archive.py
python scripts/validate_archive.py
```

Check actual filenames in experiments/code; source hashes and results accompany scripts. Exact integer/Fraction assertions are distinguished from floating displays and random stress tests. The analytic_checks random finite-multiset tests are diagnostics, not theorem proofs. The Li skeptic high-precision paired-zero sum is nonvalidated numerical evidence; the mathematical proof is the paired-product argument. Results are deterministic where seeds or exact inputs are given.

Source PDFs/extracted text are intentionally omitted from the distributable archive. Re-fetch exact source URLs/version IDs recorded in paper records and compare source_file_hashes.jsonl. Re-fetching a mutable author URL may change bytes; retain both hashes rather than overwrite provenance.


## Later exact and scoped checks

Run commands from the archive root. Ordinary Python3 standard-library proofs/certificates include:

```sh
python experiments/code/lagarias_compact_integer.py --cells experiments/results/lagarias_compact_integer.json
python experiments/code/positive_kernel_bessel_logconcavity_skeptic_round3.py
python experiments/code/bessel_logconcavity_third_round3.py
python experiments/code/beta_smoothing_exact_checks_round3.py
python experiments/code/beta_smoothing_third_round3.py
python experiments/code/unit_circle_scalar_window_round3.py
python experiments/code/polynomial_window_third_round3.py
python experiments/code/christoffel_independent_round3.py
python experiments/code/839_boundary_advocate.py
```

Some commands write a fresh JSON result next to their archived result. The Bessel sign programs reconstruct polynomial coefficients and signs, not just read a stored PASS field. Beta finite algebra checks support, and do not replace, the analytic tail/zero/count proofs. The polynomial-window exact checks are supplemental; the twisted product rule and endpoint estimates prove the infinite family.

The independent first/second/third kernel-cell checks are more expensive and have already succeeded at the hashes/results shown in the formal audit. The first full author search requires a C++ compiler and the included licensed frozen inputs/reference code; the first unmodified search and a separately reviewed checkpoint-enabled third search have completed; exact current state of the second is in its resultJSON. The adapted search is distinguished from byte-unmodified replay. Lean source replay requires the exact pinned external repository, toolchain and Mathlib revisions. Source build logs/status record completed RankTrace and main Multiplicity builds with actual type/axiom queries, while a newer pinned39/17 density target has its own live record; caches are omitted from distribution.

Arb/FLINT runs require the pinned dependency stated in their own files. Such validated interval computations are separated from mpmath, floating exploratory searches and illustrative graphs. Original copyrighted PDFs and extracted mathematical text are not bundled; use canonical source links and recorded hashes to reproduce source inspections.


## Conrey–Li interval certificates

The shared replay used `/tmp/witness62-conrey/bin/python`. On a fresh machine:

```sh
python -m venv /tmp/conrey-li-replay
/tmp/conrey-li-replay/bin/python -m pip install 'python-flint==0.9.0'
/tmp/conrey-li-replay/bin/python experiments/code/witness62_conrey_li_deep.py
```

Compare the JSON with experiments/results/witness62_conrey_li_deep.json. The director replay matched its exact bytes. A separate implementation uses mpmath interval arithmetic at75 decimaldigits and explicit periodic-Bernoulli remainders: experiments/code/prefix_formula62_conrey_li_independent.py. It independently encloses one interior zeta witness. Finite-code certificates retain their software trust boundary and are not relabeled Lean proofs.


## Round 11 arithmetic-band figure

Run `python experiments/code/prime_band_round11_figure.py`. The PNG/SVG/PDF show exact RH-conditional asymptotic formulas for fixed power bands, evaluated for illustration with floating point. They contain no finite-height zeta samples and are not interval certificates. The JSON records the source note, exact cubic witness and plotting-code hash. The separate director replay JSON files pin the symbolic and Arb mathematical checks.

Generated compiler setup JSON caches were reversibly packed after the earlier formal replays to free workspace storage. The original source, Lean modules and private kernel data were untouched. See quality/compiler_setup_cache_packing.json and scripts/restore_packed_compiler_setup.py; only the original workspace has the private cache payloads.
