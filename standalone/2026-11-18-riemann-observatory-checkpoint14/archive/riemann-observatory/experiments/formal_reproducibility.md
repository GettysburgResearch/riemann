# Formal and finite-certificate reproduction

## Offline finite checks

From the archive root:

```
python experiments/code/independent_kernel_cells.py
python experiments/code/independent_kernel_cells_second_third.py
python experiments/code/cosine_window_energy_check.py
bash experiments/code/replay_839_reference.sh
```

The first uses Python's exact Fraction arithmetic and takes about90s here. Its analytic derivation and independent parent review are in `audits/adversarial_reviews/kernel_cell_reconstruction_round2.md`. The second checks both remaining kernel tables in about210s. The third checks a closed cosine integral and final rational constant. The fourth compiles the author's unmodified C++23 reference checker (g++14.2 here) and takes about7min. It checks the local inequality on all boxes through that implementation; it is not a new independently written search algorithm. All required data and the MIT-licensed reference code are bundled with provenance and license files. No PDFs are required or redistributed.

Observed outputs are in `experiments/results/independent_kernel_cells.json`, `cosine_window_energy_check.json` and `839_reference_rerun.json`. These remain separate claims: table soundness, constant arithmetic and execution of the original search code. The zeta theorem additionally requires mathematical search soundness and analytic transfer.

## Pinned Lean artifacts

To reproduce static source checks, obtain these exact checkouts:

```
git clone --branch v1.0 https://github.com/anthropics/zeta-23-lean.git AF
git -C AF checkout 3635e74826a4c1fcece7d1cd2b6fa75e43a00510
git clone --branch v1 https://github.com/kristianmk/839.git K839
git -C K839 checkout 0e961ea199b425010843bc8044676d4ad29fe031
python experiments/code/formal_round2_scan.py AF
python experiments/code/formal_839_scan.py K839
python experiments/code/formal_row_check.py AF
```

Static token scanning is not a Lean parser or axiom-dependency query. Challenge files deliberately contain placeholder proofs; the Solution modules are the proof targets. Counting definitions and exact theorem types must be read separately from any proof success claim.

Install elan, then use the toolchain selected by `AF/lean-toolchain`, pinned4.33.0-rc2. In AF run:

```
lake exe cache get
LEAN_NUM_THREADS=4 lake --no-cache build Zeta23.LinAlg.RankTrace
lake env lean /absolute/path/to/experiments/code/FormalRound2Axioms.lean
```

The official Mathlib cache endpoint returned CONNECT403 in this execution, so the scoped target is being built from source. A complete source build may take a substantial time; completed dependencies are reusable. The next step after the scoped build is `lake --no-cache build Solution.Multiplicity` followed by `lake env lean comparator/PrintAxioms/Multiplicity.lean`. Do not label either step successful until its actual exit and output are recorded. External comparator/nanoda replay is a further independent task and was not executed here.

For K839, use its documented upstream `anthropics/formal-math` commit `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844`, subdirectory `zeta23`, and apply its exact14-file patch. The full upstream subtree was retrieved and Git-blob-verified in this execution; the patch applies cleanly and counting definitions remain unchanged. Its three `native_decide` runs are expensive and require the disclosed additional compiler/runtime trust. No local K839 Lean build is claimed.

## Preserving evidence

Toolchains, package caches and source PDFs are excluded from the downloadable archive. Pinned URLs, Git/sha hashes, exact inputs, original-license files, scripts and scoped outcomes are included. A manifest checksum proves file identity/self-consistency; it does not prove mathematical correctness. See `audits/formal_artifact_round2.md` for the exact boundary of each claim.

The second/third checker shares exact trig enclosures and takes about210s here. All three offline data folders carry separate source hashes and MIT licenses. The independent search skeptic tests can be replayed with `python experiments/code/839_search_skeptic_checks.py`; they supplement its written general proof and do not rerun the60-million-box search.


The finite boundary exploration is reproducible offline:

```
python experiments/code/839_boundary_advocate.py
python experiments/code/839_transfer_skeptic_checks.py
python experiments/code/839_transfer_error_budget.py
lean experiments/code/839_transfer_boundary_core.lean
```

The last command needs the pinned Lean toolchain but only Std, not Mathlib. Its actual successful local output is experiments/results/839_transfer_boundary_core.json. It checks finite integer data, not real interpolation, the general transfer theorem or zeta. The source literal was compared with the exact bundled JSON; the two proofs of the real interpolation/bookkeeping implications are separately documented.

The sequential main-source-build runner, experiments/code/continue_formal_main_round2.py, waits for the prior scoped process to finish and refuses to duplicate an existing build in the same checkout. It records progress and final exits in experiments/results/formal_multiplicity_build.json. Its existence or running status is not evidence that the main theorem compiled successfully.


Current-workspace safe continuation is `python experiments/code/resume_formal_safely.py`: it checks the PID, command and checkout to avoid duplicate work or unrelated reused PIDs, preserves the prior log/status, then resumes the exact target if needed. The first main attempt was interrupted with observed SIGKILL; the cause is unknown. A source-semantic inventory found bare aggregate imports, so the main build includes all Mathlib rather than the much smaller originally estimated cone. The original proof source is unchanged. Final status must come from actual exit/query output.


First-window majorant and close-pair component: `python experiments/code/839_majorant_check.py` replays42 exact closed interval checks and the source Lambda/scalar conditions in under1s. It asserts the pinned kernel binary hash and dimensions before composing with the previously validated whole-cell table. Its Fourier/Bessel justification and independent review are separate written proofs; no full theorem build is inferred.


The archive finite perturbation proof was actually checked: in the pinned AF checkout run `lake env lean /absolute/path/to/experiments/code/ObservatoryHoffmanWielandt.lean`. It needs only the already built RankTrace cone and starts no additional main build. Observed result formal_hoffman_wielandt.json records exit0, exact source hash and standard axiom queries for the sorted-eigenvalue squared displacement and Lipschitz empirical-test square bound. The clipped-polynomial construction and asymptotic moment transfers remain separately reviewed ordinary mathematics.

The fourth attempt to build the exact Solution.Multiplicity target completed locally in 8,887 Lake jobs under Lean 4.33.0-rc2 at commit 3635e74826a4c1fcece7d1cd2b6fa75e43a00510. Its dedicated theorem type and axiom query also exited zero. For the 12 queried declarations and result hashes, see [the raw query result](results/formal_multiplicity_build.json) and [the compact summary](results/formal_multiplicity_summary.json). The query used the compiled Solution environment. A separate challenge-environment comparison, external independent-kernel replay, and the K839 Lean build were outside this result.

For the second and third K839 windows, run `python experiments/code/replay_839_later_windows.py --work-dir /absolute/path/to/private-work` from the archive. Use `--windows second` or `--windows third` for one window, and `--preflight-only` to run the exact input and integer-bound checks without launching a search. The wrapper builds the unmodified C++23 source with the matching eight- or seven-point compile definition, checks frozen hashes and reuses the closed-cell results already in the archive. It records separate heartbeat and final result JSONs in `experiments/results` by default. Use a fresh result directory via `--result-dir` for a separate replay. Preserve any stopped run's checkpoint and its private stdout/stderr before retrying the same window with a separate work and result directory. The verifier restarts its search from its root box on a new run. [Search audit](../audits/839_later_window_search_formal62.md)

A separately staged checkpoint adapter lets the later-window C++ search retain progress across executor interruptions. Run `python experiments/code/run_839_checkpoint_replay.py --work-dir /absolute/path/to/private-work --result-dir /absolute/path/to/results`. Keep the same work directory and its per-window search checkpoint files when restarting. The same command resumes from the latest durable node boundary, reloading the pinned inputs; it also preserves earlier heartbeat and log files in the private work directory. A directory lock prevents simultaneous workers for that work or result directory. To run one window, add `--windows third` or `--windows second`. Keep trusted private checkpoint files separate from the archive. Report files have the names `839_reference_second_checkpoint_replay.json` and `839_reference_third_checkpoint_replay.json`, distinct from the unmodified reruns. [Checkpoint design and scope](../audits/839_later_window_search_formal62.md)

The pinned Palomar Lewko (39/17) density source also built locally. Use the pinned package and toolchain from its semantic audit. For the current workspace, the bounded stage runner is `python experiments/code/palomar39_formal62_runner.py build --build-seconds 7200 --base sources/palomar_formal62 --status experiments/results/formal62_palomar39_build.json`. It rechecks the pins and consumes the prepared downloaded official dependency artifacts. The completed results include local type and axiom output for the global uniform density and middle large-value declarations. [Palomar replay audit](../audits/palomar_density_replay_feasibility_formal62.md) · [Completed result](results/formal62_palomar39_build.json)
