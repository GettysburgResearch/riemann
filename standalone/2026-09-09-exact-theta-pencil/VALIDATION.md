# Executed checks and limitations

The manuscript is a paper derivation. The accompanying program checks bounded
algebra used in it; it is not an independent proof of its differential domains,
its infinite theta identities, its complete characteristic set, or RH.

## Primitive and finite scope

`check.py` uses Python integers and `fractions.Fraction` only. Its six groups
contain 93 bounded cases: 36 polynomial differential-expression factorizations,
27 Wronskian identities, 12 real/imaginary energy identities, 12 self-reciprocal
heat-weight/normalization identities, five hyperbolic multiplier identities,
and one explicitly synthetic scalar sign control. The variables in the heat
controls represent exact algebraic values of exponentials; they are not claimed
numerical evaluations of specified d or eta. No actual xi zero is computed.

The producer mode `--emit` reconstructs JSON without authenticating a packet.
It is not an acceptance command. Acceptance uses `--check result.json`, checks
exact types, reconstructs the mathematical output, and verifies the exact
regular-file inventory and seven SHA256 entries. No acceptance uses `assert`.
There is no claim that hashing proves mathematics.

## Commands

The following commands are run after sealing the delivery:

    python -I -B check.py --check result.json
    python -I -B -O check.py --check result.json

Both must return zero and identical JSON. The delivery receipt outside the
packet records the actual run hashes. A separate temporary-copy harness checks
four altered inputs in EACH mode: a resealed false RH status, a resealed Boolean
alias for an integer count, a resealed duplicate JSON key, and changed proof
bytes without updating the manifest. A pristine copy is checked first in each
mode. These are deliberately limited protocol checks, not an audited hardened
release framework.

An add-only patch is applied in a temporary Git repository with an unrelated
sentinel. Its resulting packet bytes are compared to the frozen directory and
both acceptance modes are replayed. The clean ZIP extraction is separately
checked. These small repositories are not full Riemann checkouts, remote CI,
Lean/Comparator builds, or tests of another contributor's producer.

## Prior and external sources

The prior gamma manuscript's locally supplied 21,088 bytes have Git blob
7cf1d52a811cf9be0cbe18407f6384bf460afb02, matching its deposited source. No prior
code suite or numerical campaign was rerun. The new pencil proof does not rely
on the parent's spurious-zero theorem.

DLMF normalization/modular identities and the relevant Csordas PDF sections
were inspected. The latter's normalization uses a different variable and a
half-line kernel; this note derives its own full-line normalization explicitly.
A 35-digit mpmath scratch computation was used only to notice/check the factor
two convention. It is NOT interval arithmetic, not a retained certificate, and
not used to prove any statement. No numerical potential spectrum, theta contour,
nonreal xi zero, or new native sign range is claimed.

The source lock states reading depth; it is not an exhaustive repository audit
or independent acceptance of earlier author work. External supersymmetric-potential
prior art was inspected only at abstract level; no claim of novelty or detailed
comparison to that paper is made. All original files and branches are preserved.
