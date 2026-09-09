# Three-route RH assault — second pass

**All three routes remain active.** This pass continues PR #793; it does not open a replacement PR or narrow the programme.

Status: PROPOSED MATHEMATICS, complete proofs and bounded certificates supplied; independent mathematical review required. **RH remains unproved.**

Parent: `7275b956b278051504da4befeb3b37924f83fd58`, branch `research/astra/20260905-three-route-assault`, repository `GettysburgResearch/riemann` (formerly `gfreund123/riemann`). The entire first-pass packet and its manifest are preserved unchanged. Everything here is additive under `pass2/`.

## 1. What changed mathematically

| Route | New result | Exact remaining problem |
|---|---|---|
| 1 — theta/positive determinant | Actual source-only positive completions through degrees two and three have **minimal ranks 15 and 32**. Arbitrary coefficient-convergent positive finite matrices suffice for closure; compatible compressions are unnecessary. | Produce such positive completions/approximants at unbounded order from the actual source. |
| 2 — signed Mobius energy | One causal damped norm removes maximal-prefix bookkeeping; its entire diagonal is explicit and finite at every positive damping. Any single off-line zero forces a quantified, multiplicity-sensitive blow-up. | Bound the complete signed off-diagonal above, uniformly in the time horizon, for every positive damping. |
| 3 — individual-zero Hilbert witness | A new trace-class Hardy/resolvent model retains an isolated pair against the **entire infinite zero background**, with exact Blaschke screening and a finite-height/finite-time negative-witness budget. | Prove arithmetic positivity of this particular source-defined operator. No additional unproved cofinal capture premise remains for this model. |

These are not three new proofs of RH. The constructive finite xi result, the causal arithmetic identity, and the complete capture theorem have different scopes. They must not be composed by identifying their operators or metrics without a theorem.

## 2. Route 1: a real source object, not a fitted zero spectrum

Read [R1_XI_MINIMAL_RANK.md](R1_XI_MINIMAL_RANK.md) and [R1_COMPACTNESS.md](R1_COMPACTNESS.md).

For

    f(u)=xi((1+sqrt(1+4u))/2)/xi(1),
    log f(u)=p1*u-p2*u^2/2+p3*u^3/3+...,

Euler--Maclaurin enclosures of the Stieltjes constants, pi, and zeta(3) determine p1,p2,p3 without zero data. A Cauchy inequality proves rank at least 15 for degree-two matching, and a two-value positive spectrum attains it.

A sharp cubic-moment bound excludes every rank at most 31 for degree-three matching. A unique root of a source-defined cubic, enclosed between the exact rationals 0.00056 and 0.00057, supplies a positive rank-32 completion. The entries are exact source constants and algebraic operations, not rounded numerical eigenvalues. Fifteen rational interval signs certify the construction and its minimality.

The companion compactness theorem proves that unbounded compatible matrices are NOT required. Coefficient convergence plus a trace bound gives

    f(u)=exp(gamma*u) product_j(1+u*lambda_j),

and the actual xi positive-axis growth forces gamma=0. The pure-escape example (1+u/n)^n is retained to prevent an invalid trace-compactness argument. A separate finite sector certificate makes approximation errors and source tails explicit; no new sector certificate is claimed as executed.

## 3. Route 2: causality is part of the arithmetic theorem

Read [R2_CAUSAL_ENERGY.md](R2_CAUSAL_ENERGY.md).

For the literal 67-free Mobius source on the fixed frequency interval [1,2], the new norm is

    J_sigma = integral_0^infty exp(-2sigma*x)
                integral_1^2 |sum_(n<=exp x) mu_67(n)n^(-1/2-it)|^2 dt dx.

The diagonal equals

    zeta(1+2sigma)/[2sigma*zeta(2+4sigma)*(1+67^(-1-2sigma))].

Finiteness of J_sigma for every positive sigma is the RH endpoint. Only an upper bound on the FULL signed off-diagonal is needed; absolute off-diagonal summation is stronger than necessary.

For a zero rho of multiplicity m and displacement delta=Re(rho)-1/2>0,

    liminf_(epsilon->0+) epsilon^(2m-1) J_(delta+epsilon)
       >= positive explicit constant depending on rho and m.

No rightmost-zero, simplicity, or linear-independence assumption enters. Infinity is allowed in the statement. A precise anti-causal counterexample shows why a finite reciprocal-zeta vertical integral alone cannot substitute for the causal norm. **No new signed Mobius power saving is proved.**

## 4. Route 3: complete capture in a deliberately changed metric

Read [R3_HARDY_CAPTURE.md](R3_HARDY_CAPTURE.md).

For fixed a,b>1/2, use the actual source operator with kernel

    2a exp(-a(t+u)) W_b(t-u),

where W_b is independently specified by a safe Laplace transform of xi'/xi, hence gamma factors and an absolutely convergent prime series. Its zero representation is used to prove trace-class convergence and analyze a hypothetical defect, not to prescribe a real spectrum.

The exact Cauchy/Blaschke Schur matrix of an omitted conjugate pair remains positive definite after projection off the complete infinite background. An explicit vector has finite-prefix Rayleigh quotient -d_T with d_T tending to a strictly positive target-dependent value. The omitted-zero error is O(log T/T); time truncation has an exponential bound. The strict budget

    R(T)+2(M_T+R(T))*exp(-(a-1/2)*L) < d_T

therefore holds for some finite T,L for every hypothetical pair. It yields a compactly supported negative test for the full operator. No uniform spacing or global frame bound is assumed.

This does NOT contradict first-pass compact-band screening: the new proof annihilates a finite background, controls the weighted remainder, and pays truncation. Nor does it transfer the first-pass surplus constants or compact-support BGST/Lamzouri estimates into the new metric. **Positivity of the gamma-plus-prime operator remains open.**

## 5. Reproduce

From this directory, using Python 3 and only its standard library:

```bash
python source_certificate.py
python -O source_certificate.py
python verify.py
python -O verify.py
python verify.py --tests
python -O verify.py --tests
sha256sum -c SHA256SUMS
```

Recorded results: **640 distinct finite controls**, including the 15 actual-xi interval signs, and **13 unit/rejection tests**, passing in both interpreter modes. The unit suite includes rerunning the controls; those executions are not additional distinct controls. The predecessor's 447 controls and 17 tests were also rerun in both modes after authenticating its local files against the remote manifest.

`RESULTS.json` and `XI_SOURCE_CERTIFICATE.json` are freshly reconstructed by the checkers, not accepted merely because their stored flags say PASS. Analytic theorems, infinite limits, source-identification proofs, and external mathematical inputs are not machine-proved by these fixtures.

Read [SOURCES_AND_VALIDATION.md](SOURCES_AND_VALIDATION.md) for the self-audit, primary-source boundary, exact parent receipt, and exclusions.

## 6. Next work, with all three routes retained

Route 1 should extend source-defined positive moment completion beyond degree three, using the escape-free compactness theorem as the endpoint. Route 2 should attack the explicit signed off-diagonal rather than a causality-free boundary integral. Route 3 should attack the source quadratic form itself, since its individual-zero capture and tail budget are now supplied for this metric.

A higher finite rank, another exact reparameterization, or a new positivity criterion is not automatically an RH advance. Each continuation must identify a genuinely new positive construction or signed arithmetic estimate and retain the demonstrated counterexamples.
