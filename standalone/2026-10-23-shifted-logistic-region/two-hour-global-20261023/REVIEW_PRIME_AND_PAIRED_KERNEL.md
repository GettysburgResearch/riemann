# Review of the retained-prime and paired-kernel components

2026-10-23. No defect found in the scoped components below. This is
not a review of a final global constant or a human mathematical review.

## Bound files and scope

- Parent's FORD_COMBINED_PRIME_GAIN.md:
  `67df2f838807e94e01d51cd821a524b00428328ebd7a9d3ecf5ccaf490ee09d1`.
- Parent's verify_ford_prime_gain.py:
  `5170c59e8c35fe842af4e315aca8376f2fb234b49c1986a8732deb53843e2c59`.
- Its imported exact Bernstein helper:
  `059c9c069618e2d8988faea5465403bb85442e513ab580d0233822b1c7dacda6`.
- Parent's verify_paired_poisson_kernel.py:
  `63e0101e99d43aae299bbf0b0980532ad0681eb0f206f4cb5f29a8fc21de6193`.

The reviewer derived the initial Poisson comparison and suggested
investigating reflection-paired kernels, so that broad mechanism is
shared work. The parent derived the exact paired polynomial proof.
The present audit independently reconstructs its rational inequality
and checks its Bernstein certification. The prime arithmetic and
the parent's exact proof were independently reviewed here; a related
prime-retention idea had also been discussed between both authors.

## Retained-prime interface

Ford's Euler-product identity at the right line, together with the
exact Fourier transform of sech squared, gives

    -(1/2) sum_(j>=1) b_j I_right(jt)
      =sum_n Lambda(n)/(n^2-n)
          -sum_n Lambda(n)P(tlog n)/(n^2-n).

Combining the favorable second sum with the original nonnegative
Dirichlet sum gives exactly (P1) in the reviewed note, including
the factor lambda and division by w0. The exponential weight can
be discarded in the lower bound because w>=0. The global curvature
bound then gives (P2); the directions of both inequalities are correct.
Multiplication by P is valid because the exact polynomial is a sum
of two absolute squares and hence nonnegative for every phase.

I checked the integer reconstruction of its cosine coefficients,
the Chebyshev recurrence, the substitution cos x=2u-1, and the
monomial-to-Bernstein conversion. The de Casteljau halving helper
preserves exact denominators and the accepted closed subintervals
cover [0,1] without gaps. The dependence on lambda squared is
affine, so its two checked endpoints prove the full stated interval.
The logarithmic lower and upper bounds enter with the correct signs.
The false-target control is genuinely false at a tested endpoint.

## Paired-kernel primitive inequality

Reflection permits 0<=d<=1/2. Put a=1/4 and v=y^2. The desired
pointwise inequality is

    min(4,1/(d^2+v))+min(4,1/((1-d)^2+v))
       <=(29/9)[(d+a)/((d+a)^2+v)
                   +(1-d+a)/((1-d+a)^2+v)].

Outside, v=w+1/4-d^2 with w>=0 makes both radii at least1/2.
The code's primitive numerator is precisely the positive-denominator
clearing of this inequality. Every coefficient in w is nonnegative
on 0<=2d<=1 by its univariate Bernstein coefficients, which covers
the unbounded w direction.

Inside, v=t(1/4-d^2), 0<=t<=1, makes the first minimum4 and the
second reciprocal. The other cleared numerator in the code is
again exact. Its four affine half-square substitutions cover the
whole closed (2d,t) square, and each bivariate Bernstein coefficient
is nonnegative. All cleared denominators are positive. The equality
at d=0,v=1/4 and rejection of a smaller constant check the stated
sharp boundary case. Critical-line zeros can be handled by the
same inequality with half weight on the repeated horizontal pair.

This proves the primitive kernel inequality; any later weighted
Hadamard aggregation, digamma bound, and endpoint optimization are
separate interfaces and are not implicitly certified by this review.

## Replay

Both scripts passed normal and optimized execution using
`python -I -S -B` and `python -I -S -B -O`. Their printed outputs
were identical. The generated exact certificate hashes are

- FORD_PRIME_GAIN_CERTIFICATE.json:
  `106314dc47ccde399165077b29b6161432ffb692bebeebb6ac073dc905421926`.
- PAIRED_POISSON_KERNEL_CERTIFICATE.json:
  `c0e2f78922b6b14b2778dfdf4da74ffc537bc76105bb1931c6cd078ac24ec780`.

These are finite arithmetic certificates of inequalities whose
analytic reductions are explained above, not certificates of RH
or of an assembled global zero-free theorem.
