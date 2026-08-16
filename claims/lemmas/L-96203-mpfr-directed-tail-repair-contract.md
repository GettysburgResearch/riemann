# L-96203 — MPFR outward transcendental evaluation repairs the numerical tail contract

Claim ID: `L-96203`  
Status: **PROOF-PRODUCER CONTRACT; FULL 65-ROW ARTIFACT REQUIRED**  
Created: 2026-08-16  
Depends on: PR #508 exact event reduction, MPFR correct-rounding API  
RH status: not assumed

Let \(I=[a,b]\subset(0,\infty)\) have binary floating-point endpoints. Define
\[
\sqrt I=
[\operatorname{MPFR}_{\downarrow}(\sqrt a),
 \operatorname{MPFR}_{\uparrow}(\sqrt b)]
\]
and similarly
\[
\log I=
[\operatorname{MPFR}_{\downarrow}(\log a),
 \operatorname{MPFR}_{\uparrow}(\log b)].
\]

At precision at least 192 bits, conversion of a binary `long double` endpoint into MPFR is exact. MPFR's `RNDD` and `RNDU` modes therefore return outward-rounded long-double endpoints containing the exact transcendental image. Rational arithmetic and the remaining elementary interval operations are then propagated with directed hardware rounding.

`experiments/X-96201-mpfr-target-lorenz-hardening/rewrite_and_run.py`:

1. extracts the frozen PR #508 source with `git show`;
2. replaces every interval `sqrt` and `log` call by the MPFR wrappers;
3. compiles with `libmpfr` and `libgmp`;
4. runs rows \(2,\ldots,66\) independently;
5. aggregates the full, parent, derivative, tail-persistence, and row-66 separation gates;
6. fails unless all original strict margins survive.

This corrects the specific numerical defect from review #516. It does not by itself construct the missing actual anchored source marginal; that is a distinct source-interface obligation.
