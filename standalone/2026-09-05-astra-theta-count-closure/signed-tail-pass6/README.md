# Signed prime-tail theorem and the first complete dyadic source stage

**RH and the all-rank arithmetic matrix inequality remain unproved.**
This pass contains proposed complete analytic component proofs and a finite
rational interval certificate. Independent mathematical/code review remains
pending; no external novelty or priority claim is made.

Base: PR #790 @ bce97be9727dea9968db7517738edc966d2cc86b.
Everything is add-only under signed-tail-pass6/. Earlier manuscripts and
canonical/formal files are unchanged.

## Main analytic result: an actual signed prime-tail inequality

Let B=17/4 and

    g_N(t)=(t^2+1/4)^2/(t^2+B)^(2N+2),
    ghat_N(l)=integral_R g_N(t)exp(-ilt)dt.

For EVERY integer cutoff X>=2, let L be the least integer with X<=2^L.
Then, for EVERY integer N>=4096(L+1)^3,

    sum_(n>X) Lambda(n)/sqrt(n) ghat_N(log n)
      < -(1/(128N)) (4/17)^(2N+2) <0.

The full von Mangoldt weights and all prime powers are retained. The sum is
absolutely convergent at each fixed N. This is a signed infinite arithmetic
estimate, not an absolute-value bound or a finite prime experiment. Its
proof uses the unconditional explicit formula and the parent's elementary
source budget h(0)<1/2. No PNT, zero prefix, simplicity, RH, or previous
high heat-derivative positivity theorem is needed.

The important limitation: these filters concentrate at a known empty low
spectral region. This completed inequality does NOT control arbitrary
cross terms of the all-rank source matrix.

## Why the direct finite-cutoff positivity proof fails

The literal finite-prime truncation retains continuous spectral density

    W_X(t)=Omega(t)-2 sum_(n<=X)Lambda(n)n^(-1/2)cos(t log n).

At zero this density is strictly negative for every finite X. The associated
exponentially damped heat-Hankel operator has infinitely many negative
(and positive) eigenvalues. An explicit two-term exponential-polynomial
test proves negativity already by order O((log X)^3). The omitted primes
supply the signed compensation quantified above. This is a theorem about
the actual cutoff operation, NOT a counterexample to RH or to a differently
compensated approximation scheme.

## First full prescribed dyadic matrix: positive, not merely constructed

The complete ten-dimensional space V_(1,4) of heat-hankel-pass5 is certified:

    exp(-p t), t exp(-p t),    p=1,2,4,8,16.

An independent integer/rational interval implementation reconstructs h and
its first three Taylor derivatives at all five points. All ten interval
LDL pivots are strictly positive; the last lies between
4.584342053795e-48 and 4.584342053796e-48 in the RAW basis metric.
These are not eigenvalue bounds. No zeros enter the source computation.
Euler--Maclaurin/Cauchy remainder bounds retain the entire unevaluated tail.

Read PROOF.md, then CERTIFICATE.md. The latter states the elementary
outward-rounding and analytic error contracts. No compiled library of
floating-point special functions participates in acceptance.

## Execution

    python interval_source.py --check certificate.json
    python -O interval_source.py --check certificate.json
    python verify.py --check result.json
    python -O verify.py --check result.json
    python verify.py --refusals
    sha256sum -c SHA256SUMS

448 finite controls (including ten actual-source pivot signs) pass in each
mode with equal reconstructed outputs. Five deliberate result/type/sign
corruptions are refused in each mode. Independent 160-digit differentiation
agrees with all twenty source jets but is only a diagnostic. The analytic
proofs are not machine-formalized. See VALIDATION.md for the full boundary.

The failed global step is preserved in PROOF.md Section 6: neither finite
cutoff positivity (false) nor the first certified Schur block supplies the
unbounded Schur-complement sign. No all-rank completion is claimed.
