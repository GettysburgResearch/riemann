# T-100601 — Double-owner implication matrix for the terminal signed arithmetic

Status: **PROVED EXACT DECOMPOSITION + REGIONAL ASSIGNMENT; TERMINAL ESTIMATES OPEN**
RH status: **UNPROVEN**

The exact double-owner decomposition `L-100605` turns the native Euler source into blocks indexed by endpoint primes `(p_i,p_j)`:

\[
\mathcal D_{i,i}=-r_iU_i,
\qquad
\mathcal D_{i,j}=r_ir_jU_iU_j\prod_{i<h<j}(I-r_hU_h),\quad i<j.
\]

After projection through the fixed ratio-eight minimal wavelet, every active block satisfies

\[
X/8\le p_i p_j m\le X,
\]
where every prime factor of `m` lies strictly between the endpoint primes.

This gives a genuine implication matrix by endpoint geometry.

## Region I — diagonal singleton blocks

`i=j` contains no interior Euler product. The contribution is one explicit one-prime wavelet term. It is a finite Type-I object and does not contain the previous future/cofactor sign ambiguity.

## Region II — short endpoint interval

If

\[
p_j/p_i\le8,
\]
the interior primes all lie in a single multiplicative-width-eight interval. The compact support of `K_0` and largest-prime ownership constrain `m`; there is no independent long future profile. This region is assigned to the existing compact-shell / finite-band machinery of PRs #674, #688, and the exact activation-band decompositions in PR #665.

## Region III — long endpoint interval

If

\[
p_j/p_i>8,
\]
there is room between the endpoints. Apply finite Euler squaring only to interior primes in a cutoff range, leaving both endpoint owners untouched. By

\[
(I-r_qU_q)(I+r_qU_q)=I-q^{-1}U_{q^2},
\]
the squared interior prime contributes critical owner mass `1/q^2` rather than `1/q`. The remaining unsquared interior is confined to endpoint collars and may be handled separately.

## Region IV — divisor-restricted interior

For every divisor label exposed in Regions II–III, PR #671 `L-99961` turns all subsequent dilation structure into a positive renewal with subpower Mellin mass. Thus after the divisor sign is exposed, no hidden future-prime sign remains.

## Matrix closure target

The original middle problem

```text
source-faithful producer -> one global critical signed estimate
```

is refined to

```text
native source
 -> exact double-owner blocks
 -> {singleton, short interval, long interval}
 -> region-specific compact / squaring / positive-renewal tools
 -> one residual endpoint-collar packet
 -> compact wavelet or negative-mass detector
 -> RH.
```

The new terminal theorem `DOEC100601` is the subpower logarithmic bound after summing the three region estimates and their shared endpoint-collar residual.

This statement is stronger as an integration framework than either one-sided owner decomposition alone, because each block has finite explicit endpoint geometry and no unbounded past/future profile on both sides simultaneously.

RH remains unproved.