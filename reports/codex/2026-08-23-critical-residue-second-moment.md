# Critical-residue second-moment descent

## Executive result

The post-freeze Xi reverse–Rolle programme isolates a residue-coherence
condition. Its first moment had been rewritten as a complete-root variance,
while its second moment remained a collection of local contour residues.

T-105100 supplies the exact finite-polynomial second-moment ledger:

\[
\sum_{p'(c)=0}\left(\frac{p(c)}{p''(c)}\right)^2
+
\sum_{p''(d)=0}\frac{p(d)^2}{p'(d)p'''(d)}
=
\frac{(6n^2-18n+13)V_2^2
-3n(n-1)(n-2)V_4}
{n^4(n-1)^3}.
\]

The identity follows from the residues and Laurent expansion of
\(p^2/(p'p'')\).

## Why it matters

For a real polynomial, the real critical-residue second moment is now exactly
the root ledger minus:

1. the algebraic contribution of nonreal critical points;
2. the cross-residue contribution at second-derivative zeros.

This replaces one opaque \(M_2\) statistic by an explicit complete-root term
and two named debts. It also exposes a necessary firewall: the debts are not
automatically favorable.

The identity is global over all critical points of the finite polynomial. The
Xi moment in RCMV104530 is truncated at height T. A separate localization
theorem with exterior residues, boundary terms, and an explicit order of
truncation/height limits is therefore the first continuation gate.

For \(p=x^4-2x^2+2\), every zero of \(p'\) is real, yet

\[
M_{2,\mathbb R}=\frac9{32}
>\frac{37}{432}=\mathcal K_4(p)
\]

because the second-level debt equals \(-169/864\). Root moments alone therefore
do not upper-bound the coherence denominator.

## Verification

The standard-library replay uses exact rational arithmetic. It covers:

- one complete cubic critical ladder;
- one asymmetric complete quartic critical ladder;
- translation invariance;
- incomplete-coverage rejection;
- the exact quartic debt firewall;
- an exact nonreal-critical correction fixture;
- load-bearing content hashes;
- fail-closed Xi/RH scope flags.

No heavy computation was run.

## Remaining frontier

The next useful theorem is not another global finite identity. It is a
height-localized contour ledger. After that come a two-parameter
canonical-product limit and quantitative control of the off-real correction
and second-level cross-residue debt. Until those are proved, RCMV104530 and RH
remain open.
