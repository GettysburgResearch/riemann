# Independent review: norm-profile Jacobi transfer

Date: 25 October 2026. Reviewer: `native_bootstrap`, independent of the author.

## Exact object and verdict

Reviewed file: `third-pass/fractional/JACOBI_NORM_TRANSFER.md`.

Reviewed SHA256:
`b8eb20ac49897174dbb502da30fce92a1b4d4a1816082911b69d661df1956567`.

**Verdict: PASS as an exact transfer and a paid, unsuccessful application
of the imported ordinary moment.** It proves no native inverse saving.
The ordinary-moment application remains restricted to the explicitly
qualified nonprincipal-inducing row subfamily.

The initial bytes had SHA256
`6963e435d2398d3f1bda99a1b745b5e2f8e7bd8c6070bb183444614f4fdcd358`.
Root requested explicit handling of `x=0,-1` and lattice covolume. The
author repaired those points. I read the repaired passages and checked
the final hash rather than applying this verdict to the old bytes.

## Exact source scope checked

I freshly read the relevant portions of the pinned OpenAI TeX source,
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, blob
`268c4e3206d460c617d3d2129742a72b831b3def`:

* The pairing `e(zy)` with measure `(2/sqrt(3)) dx dy` makes the
  Eisenstein lattice self-dual with covolume one.
* Sextic characters retain their zero extensions even when an exponent
  is divisible by six.
* The no-slot case of `lem:plain` uses only nonprincipality of the
  inducing character, has effective width `M=m+q`, and places no
  restriction on the bounded plain lengths. The stronger exclusion of
  the finite ray-character group belongs to the positive-slot case and
  is not required here.

The full imported fourth-moment theorem was not independently reproved.

## Reconstruction

At a good prime the cubic character is nonprincipal. The map
`x -> x/(x+1)` sends the complement of `-1` bijectively to the complement
of `1`; the zero at `x=-1` is retained. The local sum is therefore `-1`.
CRT gives the exact squarefree ideal coefficient `mu(n)` for either
orientation. The unit-ideal case gives one.

For the radial Schwartz partition, a sufficiently small radial Fourier
bump, followed by inverse transform and absolute square, supplies a
nonnegative radial function whose Fourier support still lies inside
the shortest nonzero dual vector. With the stated covolume, Poisson
summation gives constant one. On each residue class modulo `n`, the
sum of `phi(x/n)` is one. Radiality makes its weight exactly
`Phi(q_x/q_n)` without an angular factor or a missing power of `q_n`.
This proves the completion identity and the normalized actual-row
identity (5).

For `x=0,-1`, the numerator is zero, so no moving radical or conductor
is defined. The final file excludes these points from every source
application. Only the unit column can survive, and only at bounded
annular `D`; its second moment is directly `O(U)`. This repair is
sufficient.

For the other points,
`N rad(x(x+1)) <= q_x q_(x+1) << (1+q_x)^2`. Since `a_x` is a square,
its contribution to the cube of the inducing sextic character is
trivial; natural deleted factors do not change that primitive inducing
character. Thus the author's stated sufficient nonprincipal subfamily
is valid. It is not silently enlarged to all physical rows.

The squarefree adapter is the exact identity
`mu^2(n)=sum_(d^2|n)mu(d)`. Its normalized coefficients have size `1/Nd`,
giving logarithmic total mass by Minkowski. Applying the no-slot fourth
moment at width `U R_x` and then Cauchy over `O(U)` original rows yields
the row norm `U^(1/2+epsilon) R_x^(1/4)`, with the displayed profile
decay. The family `W(s)Phi(y/s)` has the uniform fixed-order derivatives
needed in this invocation.

Restricting `q_x<=D^2` keeps the moving-width range bounded when
`D<=U^C`. The absolute tail for `q_x>D^2` is indeed
`O(U^(1/2)D^(5/2-K))`. Summing the retained norm bound by lattice
counting costs `D^(3/2)`, and squaring gives `U D^3`, as stated.

Finally, I checked the positive sign in the finite transform of (9)
against the source's negative Fourier kernel. Its prefactor is `X/q_n`.
At `X=q_n`, radiality makes every nonzero dual frequency fall outside
the chosen support. For shorter completion the nonzero frequencies
remain. Finite Parseval gives exactly
`q_n product_(p|n)(q_p-2)`, because two residue classes are removed at
each good prime. This does not license discarding those coefficients.

## Remaining gap and limitations

No further correction is required at this hash. A stronger joint
estimate involving the transformed cubic kernel, original rows, and
all masks would be new input; the ordinary moment does not cover those
additive transforms. The result remains an exact identity followed by
a bound worse than the trivial native estimate, on a qualified
subfamily. No full-family inverse theorem or strip improvement is
approved by this review.

## What ran

Full authored-file reading, source-scope inspection, independent
coefficient and normalization derivations, and local SHA256 computation.
No finite character experiment was used as evidence for an all-scale
bound.
