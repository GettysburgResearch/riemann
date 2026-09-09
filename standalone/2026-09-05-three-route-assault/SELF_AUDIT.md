# Author self-audit and independent-review contract

This is an author self-audit, not an independent reviewer verdict. The analytic proofs require separate mathematical review. Exact finite checks do not replace that review.

## Route 1: attacks applied

**Normalization.** The full positive density `Phi=(D_tau^2-1/4)g` is distinct from the split density `g`. The former gives `F=2 int Phi cosh`; the latter gives `F=1/2+2u int g cosh`. Their two probability constructions are kept separate.

**Trace-class domain.** The rational weights decay at exponent `3/2`, strictly slower than the coefficient order permits. Choosing weights `1/n^2` without a logarithmic correction could fail to make the rank-one row square summable and was not used.

**No zero insertion.** The companion uses only source Taylor coefficients. Its nonpositivity is proved by an exact tail vector. The construction works for nonreal-rooted counterfeits and supplies no independent evidence for RH.

**Marked versus scalar.** The covariance refutation concerns matching singleton and pair data in the natural mode labels. It does not refute the scalar `TQF(v)` target of PR #785. An arbitrary classical observable of a larger positive model is not automatically a determinantal marginal; the obstruction is stated only for the marked determinant structure actually tested.

**Direct integral.** A nonzero nonatomic decomposable operator is not generally trace class. In the parent's forced-mode case the failure is immediate from an infinite-dimensional eigenvalue-one space. The exponential-log formula needs a separately specified trace formalism and is not imported as an ordinary Fredholm determinant.

## Route 2: attacks applied

**Frequency moments.** The lower bound uses averaging of the exact Abel identity before Cauchy–Schwarz. It needs only `int t^2 dnu<infinity`, not a false assertion that multiplication by `t` is bounded on `L^2(nu)`.

**Prefix quantifier.** One outer-horizon measure is retained across all inner prefixes. This prevents the moving-ensemble estimate from silently changing its observation during inversion.

**Sharp norm.** Formula (10) in the proof is verified exactly on rational panels, including rational equality cases. The assertion of sharpness is for arbitrary causal `L^2` data, not for Möbius.

**Critical limit.** The norm diverges as `sigma->0` at fixed nonzero twist. No bounded critical inverse is inferred.

**Arithmetic truth.** The positive-source countercontrol retains every deterministic identity and still has exponent one. Hence the pass reports no exponent contraction or new zero-free half-plane.

## Route 3: attacks applied

**Fourier convention.** The proof uses `exp(i z t)` and `int eta^2=1`. A transfer from a source using `2pi` must rescale explicitly. No imported numerical pair-correlation error was silently applied at a new support.

**Multiplicity.** Identical points are collapsed into positive integer weights. The dimensions of the flag count distinct support directions, while `M` counts full multiplicity. The surplus `d` records their difference.

**Complex orientation.** The source is `sum m |phi_z><phi_bar(z)|`, not a sum of positive modulus squares. Pairing first gives the factor `2(rr*-oo*)`; the full surplus contains `8h_N`.

**Independent finite formula.** The checker builds the matrix operator and separately sums the ordered pair kernel. It also reconstructs the horizontal term from a Gram Schur complement, rather than accepting a stored value.

**No hidden spectral assumption.** Strict finite `H>0` follows from independence of exponentials. It does not require RH or separation estimates.

**Screening.** The extracted term is the projected odd norm. The raw `sinh` norm can exceed it by arbitrarily large factors. The explicit sixth-order coefficient and the general monic-Legendre residual were checked independently by exact moment Grams.

**No uniform limit smuggling.** The general screening expansion is an iterated limit at fixed depth. Only the separately proved quartet path `epsilon=y^2` is used as a simultaneous one-parameter example.

**Finite versus global.** No complete xi-tail operator or arithmetic lower frame bound has been supplied. A negative direction of a truncated model only survives a specified tail error below the conditioned gap.

## Preferred independent review

First review the trace decomposition and square completion in R3.3, then the Schur identification and sharp constants in R3.4–R3.5. Next verify the actual-source covariance obstruction and nuclear convergence in Route 1. Finally check Route 2's measure/prefix quantifiers and Fourier multiplier norm. The screening note should be treated as a mandatory adversarial control for any proposed continuation.
