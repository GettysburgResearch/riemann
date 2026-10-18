# Validation, provenance, and publication scope

## What was and was not recovered

The preceding interrupted session stated that a higher native angular even-moment, polynomial norm-phase, coupled numerator and imaginary quadratic extension packet was ready, but **no recoverable unpublished bytes, filename or branch were found** in the current runtime. A repository scan checked the newer PR list through #993. The CT theta all-moment work has already landed as proposed work in #976, while the separate native angular rational-ray all-order packet was not identified. This directory is a NEW mathematical reconstruction based on the exact native definitions and #972, not a claim that the crashed packet was byte-for-byte restored.

### Relevant previous work

- #972: original Eisenstein ideal ray cancellation, sharp angular second mean, full Gaussian tails, and moving angular hull obstruction; inherited and credited.
- #963: arbitrary-coefficient archimedean ideal geometry.
- #964: a DIFFERENT result on polynomial uniformity over additive rational norms, not a uniform polynomial-Liouville bound.
- #976: full CT theta even moments and native critical target; those are not the same angular moments as here.
- #991 and #993: fixed zero-sensitive prime/determinant criteria; neither supplies the signed principal extraction needed here.

The class-group generalization in PROOF.md assumes fixed K throughout and a unitary extension of the principal infinity-type character. The second-moment proof requires rationally saturated S containing all ramified rational primes. The rectangular divisor-bound theorem does not require rational saturation but is stated with the same common set-up for ease of comparison. There is **no uniformity in discriminant, class number, k, or divisor order**.

## Exact and finite checks actually run

From the packet directory:

    python -B check_angular.py
    python -O -B check_angular.py

Both completed and printed byte-identical RESULTS.json output. In the eight finite experiments (X,k)=(20,1),(20,2),(20,3),(40,1),(40,2),(70,1),(70,2),(100,2):

- 212 exact k-fold signed factorization identities: coefficient = ideal Liouville sign times nonnegative decomposition count;
- 212 complete rational-content and quadratic-character sign checks;
- 12,110 quadratic-form determinant/Liouville checks for ordered primitive-ray pairs;
- 168 finite angular reconstruction identities comparing the k-th power to grouped rays;
- 8 directly evaluated Gaussian angular even-moment equalities (up to floating tolerance).

The (X,k)=(20,3) case contains 4 actual overlapping-content witnesses with gcd(a,NJ)>1; it tests why the coprimality shortcut from the k=1 argument is not valid at higher order. This is a formal monoid enumeration with BOTH prime ideals over split rational primes and one inert ideal at norm p^2. Conjugate ideal phases come from explicit integer Eisenstein generators. The numeric moment tests truncate the Gaussian sum at |l|<=30 with width 4, and compare two algebraically identical finite formulations; this is NOT a certified infinite Gaussian-tail computation or an independent test of the moment upper bounds.

GitHub's stored checker blob equals the locally executed source SHA-1 **ece429535b59e247ae0e743f4366aa2471500cd0**; its results blob equals the archived local output SHA-1 **0a98122e5d858b89730bdf8a526d165cb3761b43**. The ordinary/optimized replays were identical after the determinant checks were added.

## Mathematical review limits

The analytic arguments are explicitly stated in PROOF.md rather than asserted from finite experiments. They use standard fixed-imaginary-quadratic ideal lattice counting, periodicity of the nonprincipal quadratic character, divisor bounds, Poisson's Gaussian identity and a separated-phase Schur bound. The all-order theorem is a geometric/divisor-majorant result; the k=1 theorem uses actual rational-content signed cancellation. Polynomial phase uniformity in the all-order theorem follows only from taking absolute coefficients; it DOES NOT prove the stronger sign cancellation hypothesized in the interrupted work.

The lower exponent-optimality example uses the prime number theorem for rational primes splitting in K=Q(sqrt(-3)), an unconditional standard input. It does not produce a fixed-principal upper bound.

**No separate mathematical agent or human referee, formal proof assistant, remote CI run, primary-source rebuild, or independent analytic proof verification is claimed.** A finite checker cannot certify the infinite inequalities. Important review order: (1) the classwise phase separation including h_K>1; (2) squarefree chi-factor at every split/inert prime; (3) uniform full-Gaussian band cross terms; (4) the k-fold Liouville coefficient identity with shared prime factors; (5) principal extraction loss.

No modification to `main`, no integration of the claimed RH-critical estimate, and no mathematical priority claim are made.
