# Exact reciprocal-xi probability, with the stronger sign still open

**Proposed component proofs; independent review required. Not an RH proof.**

This continuation constructs a driftless self-decomposable subordinator with

    E exp(-s S_tau) = [xi(1/2)/xi(1/2+sqrt(s))]^tau,
    s>=0, tau>=0.

The probability law is exact. It is NOT the original theta law, NOT an Ising
magnetization, and NOT asserted to be a generalized gamma convolution.

The key source result, with all high zeros retained, is

    H(t)=sum_(Im rho>0) exp(-t*((rho-1/2)/i)^2),
    H(t) > exp(-225t)/2,
    -H'(t) > 98 exp(-225t),             EVERY t>0.

Its proof uses the classical zero strip, a whole-source Jensen bound, one
freshly certified real zero in (14,15), and the PUBLISHED Platt--Trudgian theorem
only for completeness/centrality of zeros through height30. That external
computation is not rerun. The unverified high tail is bounded analytically;
it is never assumed real. PROOF Section4 gives an exact all-prime-power formula
for the same H, including the entire archimedean term and a prime-tail bound.

Consequences at every order:

    q_n=(-1)^(n+1) kappa_(2n)(w)/[2(2n-1)!] > 1/(2*225^n),
    ((i+j)! q_(i+j+1)) >0,
    ((i+j+1)! q_(i+j+2)) >0.

The factorials are essential. The native target ((q_(i+j+2))) remains OPEN.
Its positivity cannot be obtained by dividing the proved matrices entrywise
by factorials. The actual missing statement is complete monotonicity of H,
equivalently the Stieltjes property of the exact reciprocal logarithmic derivative.
PROOF Section7 supplies the full implication to RH and a synthetic integer-
residue counterexample to treating positive/decreasing as completely monotone.

## Reproduce

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

Every accepting run recomputes three complete theta-integral enclosures, not a
list of zeta zeros. The external low-height completeness theorem and the infinite
analysis are not machine-verified by this code. `--emit` is producer mode only;
`--mesh 2048` is an independent mesh of the same arithmetic implementation;
`--controls` runs just finite algebra and does not claim the native sign replay.

Read PROOF.md and REVIEW.md before interpreting result.json. SOURCES.json and
VALIDATION.md distinguish exact sources, imported facts, new calculation and
unperformed review. No previous source file or canonical status is changed.
