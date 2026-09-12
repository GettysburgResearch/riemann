# Validation of the changed-source finite-jet packet

Status: same-author exact checks supporting a proposed component proof.
They do not prove the native all-degree cumulant inequality or RH.

## Commands

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
```

Both accepting modes regenerate the complete mathematical record and check the
exact file inventory and seven SHA256 entries. They use only Python integers,
Fractions and standard-library functions. No floating arithmetic participates
in an accepting computation. `--emit` is producer-only.

## Reconstructed mathematics

- All derivative polynomials P0,...,P84, the order-42 and order-84 combinations,
  and their rational leading-term and complete Gaussian envelopes.
- The exact choice m=20, eta=1/4, R=2^324; both complete source budgets, the
  positive real and imaginary parts of c=f((R+i/4)^2), exact inverse coefficients,
  and the exact polynomial zero. No root search or theta evaluator is involved.
- Thirty-nine derivative coefficients from a separate formal exponential-
  composition calculation (three rational Q values, orders 0 through 12).
- Three finite multiplier/moment/endpoint/logarithm panels and eight exact
  Schur-completion panels, with both positive and negative remainder examples.

The bound on all Q and all theta indices is supplied by the mathematical
inequality in PROOF.md. Finite tests are not substituted for that inequality.
The negative-index conclusion uses the parent's proposed analytic theorem;
no high-degree negative theta matrix or explicit witness degree is computed.

## Changed-copy checks

The delivery harness runs one pristine copy and six altered copies in EACH
mode. Alterations are: resealed false RH status; resealed Boolean/integer alias;
resealed duplicate JSON key; resealed producer Fourier-sign change; an unsealed
changed proof; and an extra inventory file. Each must return a nonzero status.
The producer Fourier-sign change is caught by independently evaluated polynomial
identities, not merely by comparing hashes. The harness is an external delivery
check; it is not a hidden module required by the accepting checker.

## Delivery and unexecuted scope

An isolated minimal Git fixture is used to build and apply the add-only patch.
An unrelated sentinel is preserved; each new payload byte is compared. Both
accepting modes are run after the patch and after clean ZIP extraction. The
external delivery receipt records the actual commands and their outputs.
Neither fixture is a full riemann checkout or a repository-wide build.

The supplied parent proof has 23,854 bytes and was authenticated to Git blob
b5c071afbac25cc27c4382306b4e8e26debb573c. Its numerical certificate and earlier
producers were not rerun. There is no new numerical theta integral, real or
complex actual zeta zero, Ising moment match, native positive range, formal
proof, independent referee acceptance, Windows run or remote CI claim.

Initial exploratory bound sizing printed two floating approximations; those
prints are excluded from all evidence. The final checker proves the stated
powers of two by exact rational comparisons and independently verifies the
actual Gaussian-rational parameters. No exploratory script is required or
included in the accepting packet.
