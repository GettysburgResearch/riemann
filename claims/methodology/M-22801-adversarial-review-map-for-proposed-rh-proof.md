# M-22801 — Adversarial review map for the proposed RH proof

Claim ID: `M-22801`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Issue: #228

## Review objective

The proof manuscript is intentionally short downstream of one new arithmetic theorem. Review should not be diluted across the many equivalent global routes.

## Frozen proof spine

Review in this order:

1. `L-9512-parabolic-riesz-is-analytic-totient-error.md` from frozen PR #226;
2. `L-9513-bohr-energy-of-mobius-fractional-part-packet.md`;
3. `L-22801-completed-mobius-farey-packet.md`;
4. `T-22801-critical-mobius-local-to-bohr-transference.md`;
5. `T-22802-proposed-full-proof-of-rh.md`;
6. `R-22801-truncated-bohr-packet-without-endpoint-tail-is-insufficient.md`;
7. `X-22801-critical-local-bohr` only as an algebra regression.

## Verdict granularity

Reviewers should classify separately:

```text
A. exact analytic-totient identity
B. exact reduced-Farey coefficient formula
C. exact Jordan/Bohr factorization
D. determinant-kernel estimate
E. divisor-Hilbert operator bound
F. completed endpoint-row cancellation
G. finite Fourier cutoff limit
H. dyadic second-moment-to-Mellin continuation
I. zero-pole contradiction and functional-equation conclusion
```

A failure in D–G blocks the new proof. Passing A–C and H–I does not repair it.

## Mandatory adversarial checks on T-22801

### 1. Low numerator regime

The estimate must remain valid when `|a|` or `|a'|` is one. This is where generic Farey large-sieve bounds lose a power. Verify that the completed endpoint rows, not a hidden Mertens estimate, pay this regime.

### 2. Determinant zero

Check that `aq'-a'q=0` is treated only for identical reduced fractions. No distinct rational pair may be folded into the diagonal.

### 3. Adjacent cells

The Fourier transform of the majorant couples adjacent cells as well as identical cells. Verify every phase and factor in this coupling.

### 4. r=1 divisor-Hilbert endpoint

The `r=1` channel is critical and conditionally summable in several naïve rearrangements. Require finite cutoffs before every interchange and a uniform limit.

### 5. Endpoint completion

Reconstruct the two integrations by parts. Confirm that both `M_D/3` and `x^2 R_D` are included, that all boundary terms are present, and that the Möbius floor identity is used with the correct strict-cutoff convention.

### 6. Fourier regularity

The Bernoulli packet is only piecewise smooth. Verify the finite Fourier truncation, the majorant contraction, and passage to `L2` without pointwise convergence assumptions at rational discontinuities of the derivative.

### 7. No concealed RH-equivalent estimate

Search the proof of the determinant or divisor bounds for any use of:

- `M(x)=O(x^(1/2+epsilon))`;
- critical short-interval Möbius cancellation;
- a local moment estimate equivalent to RH;
- a uniform prime-Hardy compact-strip bound;
- an unproved large-sieve constant at Farey spacing `D^-2`.

Any such use is circular.

## Cross-route consistency tests

If `T-22801` passes, independently derive:

1. the compact-strip finiteness in `T-22302`;
2. the nonnegative Haar defect of `T-20201`;
3. the polygon domination of `T-21501` on PR #219;
4. the Brownian saturation equality of `T-21703`;
5. the absence of a persistent negative CCM cardinal direction.

These are consequences and normalization checks, not proof dependencies.

## Publication rule

Until this review is complete, use only:

```text
FULL PROPOSED PROOF
PENDING INDEPENDENT REVIEW
RH NOT YET VERIFIED
```

Do not rewrite the public README or claim a solved Millennium problem from this branch alone.