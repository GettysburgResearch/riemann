# Exact finite check of the full-Gauss coefficient identity

This check verifies finite character algebra for formula (4) and the `t`-character orthogonality in `FINITE_FULL_GAUSS_OPERATOR.md`, frozen SHA256 `9d95cb27a11804cd553d7b836b3dcecaeb52bee633fbdc7cfe4893d9c59a6d8b`. It does not verify the analytic large sieve, functional equation, infinite operator bound, continued remainder, or any zero-free boundary.

## Arithmetic and finite coverage

The implementation uses the exact Eisenstein quotient ring `Z[omega]/(c)`, with `omega^2+omega+1=0`. A triangular ideal-lattice basis gives canonical residue representatives. Multiplication, reduction, exponentiation, character values, and accumulated coefficients use integer pairs throughout. No floating-point Gauss sums or tolerances occur.

The prime basis consists of a split prime above 7, its conjugate, one split prime above 13, and the inert prime 5 of norm 25. The checker covers every product of these four prime ideals with norm at most 2500: 35 moduli, maximum norm 2401. This includes the unit modulus, repeated prime powers through `7^4`, `13^3`, and norm `25^2`, and products containing both conjugate primes above 7.

For each modulus, all label exponents 0 through 5 at its active primes are tested, together with all exponents 0 through 5 at the first absent prime in the fixed basis. This external factor makes the unit multiplier `R0` nontrivial. Other label exponents are zero. The JSON and code state this exact test set; they do not claim to enumerate every sixth-power-free label.

For `t=(c,R)`, `c=mt`, `R=tR0`, the code pushes `chi_c(x)` on all units modulo `c` to `y=R0*x` modulo `m`. It checks each resulting coefficient against `Nt*chi_c(y)*conjugate(chi_c(R0))` when `rad(c)=rad(m)`. When a modulus prime disappears from `m`, it checks that every pushed coefficient is exactly zero.

For every displayed modulus `m`, all `t` exponent vectors in `{0,...,5}` on `rad(m)` are distinguished. Exact sums over all quotient-exponent classes verify the orthogonality of every ordered character pair. The computation evaluates 1555 distinct quotient classes, covering 209125 ordered pairs, of which 207570 are off diagonal.

## Recorded result

The deterministic run passed:

- 9330 label cases: 396 surviving cases and 8934 disappearing-prime cases;
- 200412 exact coefficient equalities in the surviving cases;
- 6 surviving unit-modulus cases;
- all 1555 character quotient sums and all distinct-character checks.

Three deliberately incorrect variants are rejected, with exact witnesses stored in the JSON: omitting conjugation, omitting the fiber factor `Nt`, and omitting the disappearing-prime condition.

## Reproduction and acceptance

From the workspace root, run:

```bash
python work/round3_checks/check_full_gauss_algebra.py --theorem work/round3_operator/FINITE_FULL_GAUSS_OPERATOR.md
```

If the files are moved into a publication packet, pass the theorem's actual path. `--output` may choose a separate result path. The checker authenticates the theorem's SHA256 when `--theorem` is supplied and refuses a mismatch. It records its own source hash. The default output is the JSON beside the script.

Strict acceptance is an ordinary, non-optimized Python run with exit code zero and `status: PASS`, with every exact assertion enabled. A run with Python's `-O` option is rejected. The saved JSON authenticates only this finite test set and source identity; it is not an analytic proof certificate.

The generating agent ran the checker. An independent replay is a separate review step.
