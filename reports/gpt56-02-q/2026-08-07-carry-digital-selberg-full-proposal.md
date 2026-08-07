# Full-problem continuation: carry Green inversion and dyadic conditional-Hankel proposal

Agent: `gpt56-02-q`  
Date: 2026-08-07  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW; RH IS NOT CLAIMED INDEPENDENTLY VERIFIED**

## 1. Why this route was chosen

The repository's latest reviews have made the common boundary unusually clear.

- The frozen Farey determinant proof is rejected.
- The undifferenced positive-Hankel `SH(L)` construction is blocked.
- High-order Euler cancellation plausibly removes terminal one-free-variable
  packets.
- The reflected endpoint proposal does not yet independently consume the
  balanced Möbius shell.
- The first critical Farey cell is an exact fixed-ratio Mertens increment.

The new route attacks that Möbius shell through the finite carry matrix rather
than through a generic Type-II operator. Its central object is the exact inverse
of a positive binomial-carry transform.

## 2. New exact finite identity

For

\[
\beta_{nq}
=\frac{\lfloor n/q\rfloor(q-1-(n\bmod q))}{n+1},
\]

one has

\[
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
=\frac{2m-n-1}{n+1}.
\]

This turns the complete floor/carry row into an affine Green row after one
Möbius contraction. It gives a closed inverse for every finite datum and, for
the prime ramp, the Möbius–Riesz coordinate

\[
u_m=m^{-1/2}
\sum_{k\le X/m}\frac{\mu(k)}{\sqrt k}
\log\frac{X/m}{k}.
\]

The identity is exact and is replayed in `X-23601`.

## 3. Continuum inverse

The scaling limit of the finite inverse is

\[
\mathfrak C(y)
=\sum_{d\le y}\frac{\mu(d)}{\sqrt d}
\left(8\sqrt{y/d}-7-\frac32\log(y/d)\right).
\]

Its Mellin transform is

\[
\int_1^\infty\mathfrak C(y)y^{-z-1}dy
=\frac{(z+1/2)(z+3/2)}
 {z^2(z-1/2)\zeta(z+1/2)}.
\]

The carry kernel has the sharp dual mass

\[
\int_1^\infty K(x)x^{-2}dx=1/2,
\]

so a nonnegative inverse profile supplies exactly the entropy constant `4`.

## 4. Unexpected dyadic connection

Let

\[
b_2(n)=\mu(n)-1_{2|n}\mu(n/2).
\]

Then

\[
\sqrt y\,\mathfrak C(y)
=\sum_{n\le y}b_2(n)H_2(y/n),
\]

where `H_2` is the dyadic Green sum of one explicit spline. This is the same
fixed-ratio shell isolated on PR #234.

The aligned source has:

\[
a_2(n)=v_2(n)+1\ge0,
\]

\[
\Lambda_2^\#(n)
=\Lambda(n)+(\log2)1_{n=2^k}\ge0,
\]

and

\[
b_2*(a_2\log^2)
=\Lambda_2^\#\log+\Lambda_2^\#*\Lambda_2^\#.
\]

Its endpoint dual satisfies

\[
\sum_{n\le N}[1-v_2(n)]=s_2(N)\ge0.
\]

Thus the aligned shell has positive Selberg forcing and positive digital
endpoint mass simultaneously.

## 5. Proposed closing theorem

`L-23603` applies finite Abel summation on the complete quotient partition
`floor(y/n)=ell`. It retains the dyadic difference before taking signs and uses
the reflected Selberg identity before Cauchy or total variation.

The proposed exact identity is

\[
\sqrt y\,\mathfrak C(y)
=\mathscr D(y)+\mathscr H(y)+\mathscr R(y),
\]

where:

- `mathscr D` is a binary-digit endpoint sum;
- `mathscr H` is a conditional-Hankel square for the zero-mass differenced
  source;
- `mathscr R` is a reflected Selberg forcing sum with nonnegative coefficients.

The reversed Green spline has alternating derivatives of the required sign.
The dyadic endpoint atoms telescope to binary digit sums, so the negative
terminal atom obstructing the old stop-loss construction is absent.

If every quotient face is present with the displayed orientation, all three
terms are nonnegative and

\[
\mathfrak C(y)\ge0.
\]

This is the sole new load-bearing claim.

## 6. Direct completion to RH

Once `mathfrak C>=0`, let `sigma_c` be the Mellin convergence abscissa. Landau's
theorem says a positive real abscissa would be a singularity on the positive
real axis. The explicit transform is regular at every positive real point,
including the removable point `z=1/2`. Hence `sigma_c<=0`, and the transform is
holomorphic throughout `Re z>0`.

A zero `rho` of zeta with `Re rho>1/2` would create an uncancelled pole at
`z=rho-1/2` in that half-plane. This is impossible. Functional-equation
symmetry gives RH.

The carry/entropy and square-screw arguments then become independent arithmetic
replays, not additional hypotheses.

## 7. Why this differs from the rejected routes

The proposal never uses:

- the false Farey step `(q,v)`;
- a generic cluster-operator norm;
- an undifferenced compact positive-Hankel adjoint;
- a scalar analytic square `H(z)^2`;
- endpoint counting in place of balanced contraction;
- a Mertens estimate as input;
- a finite positive ladder.

The exact signed source is retained through the reflected modulus square, and
the terminal sign is supplied by the digital identity rather than by deleting
endpoint atoms.

## 8. Honest boundary

This report is a full proposal, not an accepted proof.

The finite carry algebra, Möbius contraction, continuum transform, aligned
Euler data, and Landau deduction are individually explicit. The independent
review hinge is the complete quotient-layer identity in `L-23603.15`.

One omitted face or one sign-indefinite boundary distribution rejects the
proposal. The finite experiment cannot verify that cofinal identity.
