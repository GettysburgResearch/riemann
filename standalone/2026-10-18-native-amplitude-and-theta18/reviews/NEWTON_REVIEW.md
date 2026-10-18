# Scoped independent review of the low-product Newton amplitude theorem

Reviewer: a separate research agent in the same session (`latest_dedekind`).
This is an independent read of the component proof and checker, not an external
referee report, formal verification or audit of the full repository.

## Reviewed snapshot and result

| File | SHA-256 |
| --- | --- |
| `newton/PROOF.md` | `9f79dd54fb7e8ff26723c1bc8853c4a220d852b32c8b900c71ba9d9e15b6e6c1` |
| `newton/check_amplitude.py` | `fa7d06cd7d3657761079f7bfe3b77099ba7be97086b09183520bd9f5b1071220` |
| Fresh normal and optimized replay reports | `c1ae6f048bd895b84526a84004647061a02a54625492d744151b87a7c926a067` |

**No blocking mathematical defect was found in the stated component theorem.**
The proof establishes a complete low-product amplitude error, not a bound for
the remaining high-product amplitude or the required coarse-energy recurrence.
That distinction is correctly maintained throughout the proof.

## Exact native reconstruction

I independently expanded `mu*(delta-1*g_Y)^2`. Its last two factors vanish below
Y+1, which proves the complete coefficient identity strictly below `(Y+1)^2`.
The first excluded coefficient can have defect `mu(Y+1)^2`; the proof does not
extend across that endpoint. Weighted partial summation gives the stated finite
harmonic convolution with ALL products through Y squared.

The two finite product identities give exactly the displayed logarithmic balance
`2 M_Y B_Y+M_Y^2 log(Y^2/k)`. In particular the gamma coefficient and the constant
from mu(1) have the stated signs. Products above the output k are correctly
retained: their harmonic number is zero but their renormalized remainder is
not. Deleting them would break the balanced identity. The filtered difference
is therefore exactly the complete low-product remainder, before any estimate.

## Infinite kernel argument

I checked the elementary harmonic expansion, including the integer values
`psi(k/d)=1/2-{k/d}` and the constant `3/t^2` remainder. The trapezoidal-tail
bound and each of the three subsequent errors are sufficient for that constant.

The finite Fourier coefficient of the centered period is
`1/[d(1-exp(-2*pi*i*a/d))]`. After reduced-denominator grouping its coefficient
is exactly `Z_q/(1-exp(-2*pi*i*a/q))`, with `Z_q=sum_(q|d)c(d)/d`. The zero
frequency is `Z_1/2`, as required by the nonzero integer-grid mean. Equal
rational frequencies are combined before applying spacing; no false separation
between two representations of the same rational number enters the proof.

The bounds `|Z_q|<=d_2(q)(1+log D)^2/q` and
`sum_(q<=D)d_2(q)^2<=D(1+log D)^3` give the stated full coefficient mass.
The pointwise divisor inequality `d_2(n)^2<=d_4(n)` is valid prime by prime.
Circular spacing by `D^-2`, geometric summation and the elementary Schur bound
then give the full Gram estimate including all off-diagonal terms. The location
of the output interval does not matter. No imported arithmetic large-sieve
estimate is required.

Restoring the harmonic error gives, before simplification,

`D L^7/K + 2 D^3 L^8/K^2 + 18 D^4 L^2/K^3`, with `L=1+log D`.

For `D<=K`, this is bounded by the displayed constant 21 times
`L^8(D/K+D^3/K^2)`. Setting `D=floor(K^rho)` with `1/2<rho<2/3` gives the
negative exponent `2-3rho`. The dyadic summation and the bound
`1+log K<=2(1+log(Y+1))` yield precisely the displayed admissible constant
`10752/(1-2^(-(2-3rho)))`. The shortened final annulus is covered by the full
positive norm estimate, so no endpoint strip or intermediate annulus is lost.

## Transfer and scope

Orthogonal projection is contractive, so the difference of the square roots
of the two coarse energies is at most the amplitude error norm. The resulting
`(1+eta)` inequality correctly retains the mixed term. An additive energy
error alone would not follow; the proof explicitly avoids that assertion.
The harmonic antiderivative for each complete block was also checked directly
by interchanging its finite sums.

The result controls a strict enlargement of the range available from absolute
summation: arbitrary divisor-bounded coefficients permit low-product powers
below 2/3 instead of below 1/2. It uses cancellation in the periodic harmonic
kernel. It does not exploit new Möbius-sign cancellation, and the controlled
ordered-pair sector remains a small fraction of the full native pair set.
Neither the logarithmic balance state nor the remaining high-product quadratic
form has been bounded by the desired subquadratic energy recurrence.

## Fresh finite replay

I read the complete checker and independently ran both modes, writing reports
outside the author's Newton directory:

```bash
python3 research_pass2/newton/check_amplitude.py --output research_pass2/critical/NEWTON_REPLAY.json
python3 -O research_pass2/newton/check_amplitude.py --output research_pass2/critical/NEWTON_REPLAY_OPTIMIZED.json
```

Both passed **10,364 explicit checks**. Their bytes agree with one another and
with the author's reports at the reviewed snapshot. The checker independently
constructs the native prefix and comparison Möbius array, uses exact formal
logarithmic coefficients, and checks reduced-period identities by rational
Möbius inversion. Its 27 negative-control predicates have the narrower meaning
declared in its validation note; I do not relabel them as separately launched
corrupted-process tests.

This replay authenticates the declared finite identities and coverage. It does
not prove the infinite harmonic or spacing inequalities by experiment. Those
were checked as written mathematical arguments above. No remote CI, second
transcendental implementation, full upstream source audit or RH conclusion is
claimed. The author's files were not modified by this review.
