# Brownian renormalization -> an exact defect companion -> a phase problem

**PROPOSED research, not a completed RH proof.** Independent mathematical review is requested for BRN26-1 through BRN26-5. The all-band phase inequality OPEN-BRN is unproved, not a routine check delegated to a reviewer.

The explicit map is `X -> (X+X')/U^2`, with U uniform on [1,2]. Starting from 1 and a mean-one exponential gives two Laplace-ordered flows converging to the exact Brownian/theta law. Its normalized Mellin transform is the whole xi function. This classical identity is credited to Biane–Pitman–Yor; the contribution is the two-flow construction, its detailed quantitative control, and extraction of a prescribed positive-law companion from their difference.

## Read the mathematics

[PROOF.md](PROOF.md) supplies definitions, complete component arguments and the exact remaining inequality.

| Result | Scope |
|---|---|
| BRN26-1 | Mean-one W2 contraction with squared factor 7/12; the classical fixed law identified exactly |
| BRN26-2 | Two-sided monotone Laplace squeeze, exact variances and complete absolute error bounds |
| BRN26-3 | Whole-plane Mellin convergence; error at most exp(-n/5) on explicit disks of radius proportional to n/log n |
| BRN26-4 | Exact finite-depth difference factorization through a positive companion law C_n |
| BRN26-5 | C_n converges to an explicit perpetuity C_*; all moments exist and define an entire companion G |
| OPEN-BRN | A strict phase inequality for Xi and the odd reflected part of G on the complete critical half-strip; NOT proved |

The key distinction from the current ferromagnetic synthesis proposal is that **the exact limit and its uniform tails are available here**. What is missing is the complex phase geometry. Neither route borrows the other's missing theorem. No bounded metric on the previous theta operator is proposed.

The naive idea that upper-seed approximants are always zero-free to the left of the critical line has numerical counterevidence. The replacement companion is defined independently by the tilted recursion in PROOF section 4, not chosen after inspecting zeros. Its early band-phase scout is encouraging only as a finite diagnostic.

## Run

Standard-library exact bounded algebra:

```sh
python -I -S -B check.py --check result.json --self-test
python -I -S -B -O check.py --check result.json --self-test
```

The checker reconstructs the finite algebra and rejects altered receipts. It does not verify the written infinite proofs, evaluate theta zeros, or prove the phase sign. [VALIDATION.md](VALIDATION.md) records executed scope and failures.

Optional, **noncertifying** NumPy/SciPy scouts:

```sh
OPENBLAS_NUM_THREADS=1 python scout.py --seed upper --step .01 --angle -1.4 --out upper-coarse.json
OPENBLAS_NUM_THREADS=1 python scout.py --seed upper --step .005 --angle -1.5 --out upper-fine.json
OPENBLAS_NUM_THREADS=1 python scout.py --seed lower --step .01 --angle -1.4 --out lower-coarse.json
OPENBLAS_NUM_THREADS=1 python companion_scout.py --step .01 --angle -1.4 --out companion-coarse.json
OPENBLAS_NUM_THREADS=1 python companion_scout.py --step .005 --angle -1.2 --out companion-fine.json
```

[SCOUTS.json](SCOUTS.json) contains selected observations, not an exhaustive search. No exact or bitwise-floating replay requirement is attached to that file.

## Review priorities and next research

Check the source scaling in (6), the chord argument in (10), both Mellin tails and expanding constants in (11), the factor of two in (18), and the independent tilted-perpetuity law in (19). These are the load-bearing component proofs.

The next research attack is on the explicit pair (24)–(25): derive a sign-controlling identity from its positive linear recursion (23), or find a reliable counterexample to OPEN-BRN before investing in a global proof. A band sign must cover every horizontal frequency and every positive height below 1/2. Sampled signs, a real-axis Wronskian alone, singular-value positivity, and ordinary moment positivity do not supply it.

## Source and publication boundaries

Base: main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. [SOURCES.json](SOURCES.json) records reading depth. This is an add-only research packet, not an integration, independent review verdict or canonical status change. The PR records its exact published head. No original source branch, main, formal library, workflow or reviewer record is edited.
