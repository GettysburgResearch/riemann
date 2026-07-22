# O-1501 — Nicolas defect remains positive through the primes below 10^10

Claim ID: O-1501  
Title: Empirical Nicolas primorial defect through `p<=10^10`  
Status: EMPIRICAL  
Authoring agent: `gpt56-02-c`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-0304 Nicolas criterion; L-0322 primorial recurrence  
Scope: long-double scan of the first 455,052,511 primes  
Related counterexample candidates: none

## Statement

A restartable segmented-prime scan processed every prime through `10^10`.
At the final prime

\[
 p_k=9{,}999{,}999{,}967,
 \qquad k=455{,}052{,}511,
\]

the ordinary long-double logarithmic Nicolas defect

\[
 d_k=\log\!\prod_{j\le k}\frac{p_j}{p_j-1}
 -\gamma-\log\log\!\left(\sum_{j\le k}\log p_j\right)
\]

was approximately

\[
 d_k=8.52461732729062\times10^{-7}>0.
\]

Equivalently, the observed normalized ratio was about
`1.0000008524620961`. No floating sign failure occurred. The stored recurrence
also reported no upward step in the defect after `k=2` at the working
precision.

This is an empirical finite negative result only. It is not a certified range
and it does not imply RH.

## Definitions

For `N_k=prod_{j<=k}p_j`, Nicolas's inequality is

\[
 \frac{N_k}{\varphi(N_k)}>e^\gamma\log\log N_k.
\]

Since `log N_k=theta(p_k)=sum_{j<=k}log p_j`, taking logarithms gives the defect
above. A nonpositive certified defect at one `k>=2` would be a finite RH
counterexample through T-0304.

## Motivation

The Nicolas route is one-dimensional and exact in its prime indexing. It is a
useful independent counterexample reconnaissance path and a check against
spectral finite-Weil anomalies.

## Computational record

The scan used exact integer segmented sieving and long-double accumulation of
`theta`, `log(p/(p-1))`, Euler's constant, and the final logarithms. Checkpoints
were taken at each billion. The defect decreased from approximately
`2.980305e-6` at `10^9` to `8.524617e-7` at `10^10`.

Full compact values are in
`experiments/X-1501-nicolas-stream/results/scan-through-1e10.json`.

## Analytic domain audit

All logarithms are real. The domain begins at `k=2`. No complex branch,
analytic continuation, contour, or zero computation is used.

## Dependency audit

- T-0304 supplies the imported equivalence to RH.
- L-0322 supplies the primorial recurrence.
- The numerical observation depends on the C++ standard library long-double
  implementation and exactness of the segmented sieve.

## Gap audit

- Long-double rounding is not outward and does not certify the sign.
- The stored Euler constant is a decimal literal, not an independently proved interval.
- A prime omission would corrupt both sides of the recurrence.
- “No upward step” is an observed property of this finite run, not a theorem.
- A positive finite range cannot prove RH or rule out a later failure.

## Adversarial tests

- A one-shot scan to `10^6` was compared with a split-and-resume scan.
- `pi(10^6)=78,498` and the last prime `999,983` were recovered.
- Independent 80-digit Python sums agreed with the long-double endpoint within
  the documented floating error.

## Remaining uncertainty

The final margin is about `8.5e-7`, much larger than the small control-run
floating discrepancy but not rigorously enclosed. The first failure, if RH is
false, has no practical upper bound from the imported criterion.

## Suggested next attack

Add a proof-producing block certificate: exact prime counts and block hashes,
independent primality verification at boundaries, interval sums for `theta` and
`log(1-1/p)`, and an interval enclosure for Euler's constant. Continue only if
checkpoint certificates remain compact enough for independent reproduction.
