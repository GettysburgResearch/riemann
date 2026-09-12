# RGT26 — a finite positive gamma tail with exponentially accurate xi limit

**PROPOSED component proofs; independent review required. RH and the vanishing
nonreal defect are NOT proved.** This is a separate continuation of the exact
centered gamma/finite-defect programme, not a canonical-status change.

## Main result

Replace the omitted shape-two gamma tail after N by a positive deterministic
drift and r independent gamma variables. A prescribed Gauss--Radau rule on the
positive measure `sum_(n>N) (2/n^2) delta_(1/n^2)` matches its first **2r+1
cumulants exactly**. All parameters come from finitely many even-zeta values
and algebraic equations; no zero location or fitted Fourier moment defines them.
The law is a convolution, not a probability mixture or signed correction.

The exact Stieltjes error is a high power times a positive Laplace transform.
Keeping its full remainder and the complete head characteristic function gives
a uniform, evaluated estimate. With r=floor(N/4), N>=1024, and
`R_N=N/[16 log(N+3)]`, the normalized reciprocal Fourier transform satisfies

```
sup_(|Im z|<=R_N) |F_(N,r)^(k)(z)-(Xi(z)/Xi(0))^(k)|
                                        <= k! exp(-N/4).
```

This includes ALL real frequencies and every fixed derivative order. The bound
is absolute, not relative near zeros. Large-order parameter conditioning and
bit complexity are not claimed. The code encloses actual r=1 and r=2 rules;
it does NOT numerically construct the large-order rules used in this theorem.

Every fixed new law has the analytic endpoint form required for an eventually
real/simple spectral tail. Its remaining nonreal part is finite, but neither
its size nor the weighted defect is proved to vanish. Positivity of the Radau
weights is NOT a Lee--Yang theorem. A hypothetical nonreal limiting xi zero
would also be followed by these accurate approximants.

## Read and reproduce

[PROOF.md](PROOF.md) gives the construction, uniqueness, exact error, all
constants, endpoint adapter, and full RH implication with its missing premise.
[REVIEW.md](REVIEW.md) identifies the load-bearing checks.
[SOURCES.json](SOURCES.json) fixes the source commits and reading depths.
[VALIDATION.md](VALIDATION.md) states what was run and excluded.

From this directory:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

`--emit PATH` is producer mode, not authenticated acceptance. The accepting
path authenticates all eight manifest entries and reconstructs the receipt.
It imports no prior research code and uses only integers/Fractions and outward
320-bit intervals. No numerical Fourier transform, newly computed zero, native defect integral,
parent certificate replay, formal build, or entire-repository validation is
represented by a passing bounded checker.

## Relevant concurrent work

The published finite-defect packet is #862 at
`67d5d6a5f588642f4c451fe35d2369b5ddac9346`. The overlapping endpoint/index
packet #858 at `72ccb357e774db1189e82f4f1b83459f00638c7e` includes the
centered N=5 critical-band exception; it precludes blanket stagewise reality.
The #842 ten-moment positive-pair construction is a different source problem:
its theta moments are not the gamma-tail cumulants matched here. Fixed-stage
branching high-height results likewise do not provide uniform zero control.
No overlapping proof is counted as a new independent acceptance vote.

A further source-class stress test uses the inherited #855 critical-band disk:
for a changed infinite positive gamma law, the same positive Radau construction
and exponential convergence coexist with a persistent nonreal zero. This
conditional-on-certificate theorem uses the explicit parameter eta=2^-256 and
a complete integral perturbation bound. It is not an actual xi counterexample
or a fresh defining-integral zero computation. It shows why the native
integer-square coefficients must enter a further sign argument.

Suggested separate branch: `research/astra/20260912-positive-gamma-tail-compression`,
stacked on the frozen #862 head. Preserve every predecessor file. Original
mathematical statuses and the pending integration candidate remain unchanged.
