# Gaussian product-conductor removal: a bound for part of the actual covariance

**Status:** proposed complete component proofs; independent review pending. The high-conductor arithmetic upper bound, full higher moments, 17/24 and RH remain unproved. This is not an integrated result.

**Frozen parent:** PR #916, `f5c089e33ccce4eae4307d4f6475b9977485cb78`, branch `research/all-order-collision-removal-20261010`. All earlier files are preserved. Publication is blocked in the authoring session: the available GitHub connector exposes no writes, and terminal Git fails to resolve github.com. The packet and add-only patch are local deliverables, not an already published commit.

## What is proved here

For the predecessor's actual balanced squarefree product polynomial, use a Gaussian over the complete element-row lattice. Put sigma=1/2+delta, 0<delta<1/2, and let Q(r,s)=Nr Ns/N(gcd(r,s))^2 be the conductor of the product-column residue character.

For every fixed moment order 2k and every epsilon>0, the ABSOLUTE integrated covariance from Q(r,s)<=Q satisfies

    A_leQ(D;H) << D^epsilon * {
        H^(-2delta) Q^(1+delta), Q<=H;
        Q^(1-delta),            Q>=H.
    }

In particular Q<=H contributes only D^epsilon H^(1-delta), and the whole range

    Q <= H^(1/(1-delta))

costs at most D^epsilon H. No quasi-RH assumption or new moment estimate is used for this component bound. At the critical weight delta=0, a separate finite-horizon proof bounds Q<=H by H D^epsilon; the inverse-kernel absorption is NOT asserted to hold at that critical weight.

The proof uses primitive-character Gaussian Poisson cancellation and an exact sum over the changing common-prime masks. Omitting those masks would be wrong. A separate exact unit action decomposes the covariance into six sectors: different unit characters have zero radial correlation.

The new analytic premise can consequently be restricted to pairs with BOTH

    Q(r,s)>H^(1/(1-delta)) AND equal unit-character signatures.

That remaining signed high-conductor upper bound has NOT been proved.

## Why changing the row cutoff is legitimate

Gaussian and sharp FULL integrated moments have equivalent all-horizon power bounds. The proof compares their nonnegative energies by a layer-cake identity and enlarges the horizon when necessary. It does not majorize individual signed sharp-cutoff terms by Gaussian terms.

A suitable one-sided high-conductor bound with excess lambda would give the same conditional exponent

    1/2+delta+(lambda+5h/6)/(2k), H=D^h.

Hence the proposed fourth/sixth-moment endpoints are unchanged, not attained. Generic low-conductor removal alone cannot cover the entire support in a useful zero-free regime.

## Read and reproduce

- [PROOF.md](PROOF.md): definitions, uniform conductor theorem, primitive Gauss/Poisson proof, exact gcd-mask summation, critical finite-horizon variant, and the high-conductor remainder.
- [HORIZON_TRANSFER.md](HORIZON_TRANSFER.md): Gaussian/sharp equivalence and the precise conditional zero-free adapter.
- [VALIDATION.md](VALIDATION.md): what was run, arithmetic coverage, source boundaries and publication failure.
- [check_eisenstein_covariance.py](check_eisenstein_covariance.py): standard-library exact arithmetic, finite-field autocorrelations, full finite row-mask identities and exact scale integrals.
- [run_negative_controls.py](run_negative_controls.py): executed algebraic mutations and tampered-result refusals.

Run from this directory:

```sh
python -I -S -B check_eisenstein_covariance.py --check result.json
python -I -S -B -O check_eisenstein_covariance.py --check result.json
python -I -S -B run_negative_controls.py --check negative_controls.json
```

Normal and optimized exact arithmetic each pass 48,427 predicates with identical output. Three corrupted algebraic formulas and a tampered result are rejected in each mode. These finite tests are not an asymptotic moment proof. The finite integral tests use the explicitly declared step window 1_[1,2], not an uncomputed substitution for the smooth W_*.

## Relationship to sibling work

PR #919's metadata was read, but its full proofs were not imported or audited here. Its Hermitian full-tuple conductor and this grouped squarefree product-column conductor must not be silently identified. No claim that this cutoff dominates #919's distinct cutoff is made. The present proof is self-contained except for elementary lattice Poisson summation and ideal counting; the zero-free adapter additionally depends on the frozen #916 integrated criterion.
