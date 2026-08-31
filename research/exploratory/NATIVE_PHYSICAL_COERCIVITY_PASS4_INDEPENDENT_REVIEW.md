# Independent review of the fixed-prime physical coercivity packet

Verdict: **PASS IN THE STATED FIXED-PRIME SCOPE**.

Reviewed science commit:
`3a99132af19a7bfaf707fdc88987d2866a221934`.
Pre-computation design:
`8113cb407b6c7b2e64943b4485ead37b7ac0ccc3`.
Authoring base:
`8f01064df805624c045877655893c324a220975d`.

This is a non-author review. The science tree was read and replayed at the
exact frozen commit in a clean detached worktree. No file in the reviewed
packet was edited during review.

## Accepted statement

For the literal completed half-source at the fixed prime set `{2,3,5}`, in
the original continuous measure

\[
 d\nu(t)=|\widehat\kappa(t)|^2dt/(2\pi),
\]

the declared 64-dimensional A/C tensor observation satisfies, for every
complex `8 by 8` coefficient matrix,

\[
 2^{-153}\|M\|_F^2\le\|F_M\|_{L^2(\nu)}^2
 \le2^{27}\|M\|_F^2. \tag{R1}
\]

The source-exact change to the original monomial schedule coordinates gives
the stated bounds `2^-165` and `2^39`. The finite-horizon consequence for
every integer `H>=2^190` also follows, with the stated conservative lower
constant `2^-155` in A/C coordinates.

This is finite-dimensional coercivity at one fixed prime set. It is not a
uniform all-prime frame, a retained-gamma reconstruction, arbitrary path
attainability, or a principal-member lower bound.

## Proof audit

I checked the following load-bearing points independently.

1. The radical fields retain all infinite arithmetic aliases. Absolute
   convergence at the fixed primes identifies the closed radical expression
   with the literal double series carrying the original `1/d` equal-ratio
   weights.
2. The elementary global estimates give
   `||phi(t)||_2<=512`, `||phi'(t)||_2<=2048`,
   `nu(R)<2^9`, and `|kappahat'(t)|<54`. These imply the claimed global
   upper bound without numerical quadrature.
3. The directed finite computation encloses the complete `64 by 64`
   evaluation matrix at the preregistered nodes `1,...,64`. Its dyadic
   midpoint inverse is accepted only after the strict Neumann residual
   test. From `||V^-1||_infinity<=2^33` one obtains
   `||V^-1||_2<=8||V^-1||_infinity` and hence
   `sigma_min(V)>=2^-36`.
4. The same immutable panel proves
   `min_j |kappahat(j)|>=2^-12` from the exact piecewise antiderivative.
   With interval radius `2^-51`, the derivative bounds preserve half the
   sampling singular value and half the Fourier-kernel lower bound.
5. Integrating the resulting inequality over the 64 disjoint genuine
   intervals gives

   \[
   2^{-51}2^{-72}2^{-24}/64=2^{-153}.
   \]

   Thus no replacement of `nu` by an atomic sampling measure occurs.
6. The local coordinate matrix and its inverse have norm below two. Their
   third tensor powers and two-sided matrix congruence cost at most `2^12`
   after squaring, exactly as used in the monomial-coordinate bounds.
7. The complete coefficient tail is bounded in the unchanged physical
   norm. At `H=2^190` its norm is below `2^-78`, which safely yields the
   declared finite-horizon lower and upper constants.

## Detached replay

Runtime:
`C:/Users/gideo/OneDrive/Documents/riemann/isolated/native-xi-pass3-runtime/Scripts/python.exe`.

At detached head `3a99132af19a7bfaf707fdc88987d2866a221934`:

```text
python -m unittest discover -s tests -p test_native_physical_coercivity_pass4.py
Ran 20 tests in 50.511s -- OK
```

The author supplied a separate clean detached replay of the same commit in
both normal and optimized modes; the resident suite authenticates 25 frozen
source rows, the pinned numerical runtime, complete primitive
reconstruction, and six fully resealed hostile mutations. This review also
read the producer, all resident tests, the two proof notes, and the two
principal fixed-prime source/completion notes used by the analytic argument.

## Tuple boundary

The exact U=64 Boolean histories and displayed arithmetic constants replay.
The packet correctly leaves the native weighted aggregate `UNDETERMINED`.
The missing input is still the actual labelled regional occurrence and its
retained coefficient measure after carrier, quotient, and renewal transfers.
Neither the scalar cancellation of the 24 Boolean signs nor (R1) supplies
that information. This boundary is necessary for acceptance.

## Smallest remaining gates

- construct a source-defined observation with a lower frame bound uniform as
  the prime set grows, pricing the inverse source normalization;
- acquire one literal retained-gamma occurrence and its full coefficient
  measure before aggregation and squaring;
- connect any such source statement to the principal family norm without a
  non-admissible projection.

No RH conclusion is obtained.
