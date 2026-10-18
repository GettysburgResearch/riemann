# Reconstruction of the global arithmetic heat-kernel inequality

Status: **internal analytic and primitive-computation review. No RH or
new zero-free strip. No novelty claim for the known positivity property.**

The coordinator read `theta/GLOBAL_HEAT_POSITIVITY.md` in full at raw
SHA256 `7e5cf58efeec38e93f3768045f4d137d284265339ed17207821a3f419cec6e9f`.
Its checker is `theta/check_heat_positive.py`, raw SHA256
`1ca301f2dd6292feb2448f53b703eb4b371996936569744a87877f6d7d078793`.
An independent fresh optimized-mode replay by the coordinator evaluated
the actual xi primitive on the entire covered contour and passed its
saved-record comparison. It used python-flint 0.9.0 from an explicit
sibling dependency directory, not a packaged derived zero table.

The global Bernoulli bounds were checked algebraically. Their cleared
denominator Taylor coefficients have exactly the displayed positive
factorizations; these are whole-half-line inequalities, not truncated
asymptotic series. The sign of E(u) changes at u=12y, so the proof uses
the correct upper or lower Bernoulli bound on each sign. The Gaussian
integrals give the stated 23/40, square-root and y/12 terms. The prime
majorant includes every integer n>=2 and therefore every prime power.
Its sum--integral estimate and endpoint monotonicity prove the inequality
on EVERY 0<y<=1/50. The directed elementary margin is not a quadrature
or a finite-y interpolation.

The spectral identity follows from the paired genus-zero product in the
squared variable and Laplace uniqueness. All off-axis contributions are
kept as complex exponentials, then bounded in modulus only for the tail.
No positivity is assigned to an unverified individual zero. Jensen gives
the number of ALL H zeros at radius r at most 2e A r^2; halving by the
actual positive/negative-height symmetry gives the stated N_+(T) bound.
The factor of two is therefore accounted for.

The contour checker encloses every point of every accepted input segment
using acb rectangular arguments. Each convex output box excludes zero
and contains both rational endpoint midpoints, so the exact curve has a
coherent homotopy to its rational polygon. Exact winding of the complete
polygon gives one zero, including multiplicity, in the full critical-strip
rectangle through height 20. The already proved small disk covers all
lower heights. Opposite actual critical-line signs then identify this one
zero as simple and on the line. The empty rectangle and orientation
controls exercise separate winding outcomes.

Stieltjes integration of the full Jensen count bounds the entire remaining
zero tail by C(400+1/4+1/y) exp(-(400-1/4)y). Dividing by the first term
uses only gamma0^2<200 and gives the displayed exp(-(799/4)y) ratio.
It decreases on y>=1/50 and is less than 2/3 at the joining point. This
pays EVERY higher zero, regardless of its location within the classical
critical strip, and proves the global sign rather than extrapolating a
finite census.

The full special-function enclosure contract and classical xi product
are imported analytic inputs. The proof is not a formal verification
of Arb or of those classical theorems. No blocking gap was found at the
stated component scope.

The coordinator's primary-source search found Polson,
*On Hilbert's 8th Problem*, arXiv:1708.02653v24, Theorem A and Sections
5--6, explicitly proving positivity of this same heat trace, together
with stronger further properties. The v26 HTML Theorem 2.1 also states
the positive/nonincreasing heat trace. Those precise primary passages
were read. Thus this packet's sign property is NOT a new discovery; the
fresh short-census proof is an independently reconstructed realization.
Neither the broad finite-derivative claims in that source nor its other
probabilistic assertions are imported as proved by our replay.

Positivity of k makes its Laplace transform completely monotone; it does
not make k itself completely monotone. The unscaled canonical Hankel
criterion and the full all-order derivative signs for k remain open.
The new upstream weighted-canonical theorem is not activated by this
global zeroth inequality or its scalar power-sum consequences.
