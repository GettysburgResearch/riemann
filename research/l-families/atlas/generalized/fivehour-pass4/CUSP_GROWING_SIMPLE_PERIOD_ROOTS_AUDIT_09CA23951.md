# Independent audit of the growing simple-period-root theorem

Status: independent exact-SHA analytic review: **PASS**.
Reviewed source: `09ca23951`, file
`CUSP_GROWING_SIMPLE_PERIOD_ROOTS.md` (including its explanatory successor
to `8204c0060`). The target theorem and its sources were not edited.
Scope: proof audit only; this note does not independently replay the
separate directed finite-inequality certificate under development.

## Sources read and verdict

I read the complete R source and the load-bearing K and L notes at the same
commit. I independently checked the complex endpoint remainder, fractional
moments, uniform eigenvalue gap, Mobius domains, matrix argument principle,
and final scale inversion. I found no actionable mathematical gap.

The smallest plausible invalidator was the all-complex-epsilon operator
estimate R4. It survives the check below. The conclusion remains exactly
as scoped: simple zeros of the full period determinant in the sub-cube-root
range, not uncancelled roots of a scalar flag quotient.

## 1. Complex Laurent remainder and moments

At `s=1-epsilon`, the second constant term is

    Lambda(1-2 epsilon) y^epsilon.

After adding `1/(2 epsilon)` and subtracting the finite part, the polar
exponential contributes

    -(exp(epsilon log y)-1-epsilon log y)/(2 epsilon).

Its absolute value is bounded by a constant times
`|epsilon| y^|epsilon| log^2 y`. The regular coefficient contributes the
same scale with at most one logarithm. The first constant term contributes
`|epsilon| y^(1+|epsilon|)(1+log y)`. This is precisely the structure in
R5; forming the Laurent difference before taking absolute values is
essential and is done in the source.

For the nonconstant Fourier series, on a fixed complex epsilon disk the
Bessel integral gives `|K_nu(x)| <= K_1(x)` after shrinking the disk if
necessary. The divisor powers are polynomial and the exponential in the
Fourier index is uniform on the whole fundamental domain. Cauchy's estimate
therefore gives an `O(|epsilon|)` analytic difference. No one-sided real
inequality has been continued to complex epsilon.

For a Petersson-unit cusp form, Parseval on `y>=1` makes each fractional
moment a positive weighted average of truncated Gamma moment ratios. Since
every Fourier index is at least one, the largest ratio is bounded by the
rate `4 pi` case. Recurrence handles integer powers and log-convexity handles
the fractional part, giving R6. Differentiating the Gamma ratio, or splitting
at `y=k`, gives R7. The compact part has bounded height. Under
`|epsilon| log k=O(1)`, `k^|epsilon|=O(1)`, so R5--R7 yield

    ||R_k(epsilon)|| <= C |epsilon| k log k.

Weighted Cauchy--Schwarz supplies the same estimate for mixed matrix
coefficients and hence the operator norm. This also supplies a common
holomorphic matrix remainder. Lemma R1 is valid as written.

## 2. Uniform spectral separation

Theorem L gives one-sided brackets with absolute width `R_1+o(1)` along
every legal sequence `j=o(k)`. This sequential statement is uniform over
`1<=j<=J_k`: otherwise choosing a worst index on a failing subsequence would
produce a contradicting legal sequence. Applying the lower bracket at `j`
and the upper bracket at `j+1` gives

    lambda_j-lambda_(j+1)
      >= (k-1)/(24 j(j+1))
         -(1/2) log((j+1)/j)-R_1-o(1).

Thus R9 holds uniformly for `J=o(sqrt(k))`, including the `J+1` endpoint.
The stronger assumption `J^3 log k=o(k)` gives both this range and
`j log k=o(k/j^2)`. In particular the relevant eigenvalues are positive
and simple. No unproved monotone motion of period eigenvalues is used.

## 3. Matrix domains and zero count

With `a(epsilon)=-1/(2 epsilon)`, the disk

    |a+lambda_j| < D j log k

excludes `a=0`, since its radius is `o(lambda_j)`. Its inverse Mobius image
is therefore one connected bounded domain, invariant under conjugation,
contained in the right half-plane and centered at `1/(2 lambda_j)`.
Uniform eigenvalue gaps make these domains disjoint. On each closure,
`|epsilon|` is comparable to `j/k`, so it lies in Lemma R1's complex disk.

On the boundary, normality of `aI+T_k` makes its singular values exactly
`|a+lambda_l|`. The adjacent-gap estimate bounds all of them below by a
fixed multiple of `D j log k`; Lemma R1 bounds the perturbation by
`C j log k`. A single sufficiently large fixed `D` therefore gives R13.
The homotopy determinant has no boundary zero. The comparison determinant
has exactly one simple zero in the domain and no pole there (epsilon zero
is outside), so the finite-dimensional argument principle preserves one
zero counting multiplicity.

Conjugation symmetry and domain invariance force this unique counted zero
to be real; count one makes it simple. The right-half-plane location makes
it positive. Finally R11 gives the reciprocal-coordinate error
`O(j log k)`. Since `lambda_j~k/(24j)` and
`j^2 log k/k=o(1)`, inversion gives `epsilon_(k,j)~12j/k` uniformly.

The `09ca23951` addition is also accurate: a known fixed-j displacement of
order `log(k)/k^2` is compatible with an `O(log k)` error after the
reciprocal-coordinate change. It is presented as consistency, not as a
new coefficient computation.

## Boundaries retained

- The proof establishes a method range, not a stopping law at cube-root
  scale.
- It counts zeros of the full completed period determinant, not a proper
  flag quotient.
- It proves simplicity only in the constructed disjoint domains.
- It does not claim RH, scalar noncancellation, or a moving compact-set
  reciprocal-Gamma limit.
- This review does not certify a separate machine fixture or finite
  inequality report; it certifies the analytic argument at exact source
  `09ca23951`.
