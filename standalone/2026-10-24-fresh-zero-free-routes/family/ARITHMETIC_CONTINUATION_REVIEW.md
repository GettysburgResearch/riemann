# Independent review of the coefficient-continuation route

Reviewer: `family_escape`, not an author of the reviewed arithmetic files.
Date: 24 October 2026.
Disposition: no material mathematical gap found at the stated scope after
the explicit irrational-parameter hypothesis was added to Lemma 3.

## Frozen source files

| File under `arithmetic/` | SHA-256 |
| --- | --- |
| `COEFFICIENT_CONTINUATION.md` | `3df080e36d31d6862d290e165adc199428289a9689fcaae98338d30c3a7e85fd` |
| `DIRECT_NATIVE_APPLICATION.md` | `97139a18592ad5374e2dc57ed782e4074a4727c44b431f0627cade39ef8262b1` |
| `FRACTIONAL_ZERO_DETECTOR.md` | `a810682100ff5812fd1d6195aabf5515501ad8c361489f9c070ffc8b1b1d4a1a` |

The files were read locally and the displayed hashes were independently
recomputed. This is an internal mathematical review, not external peer review
or formal verification. It does not independently certify the complete
OpenAI/Xu--Sang/Liu analytic source chain or PR #1014's consumer.

## 1. Coefficient continuation

The ideal degree bound follows from at most `[F:Q]` prime ideals above each
rational prime and the factorial lower bound for the product of their norms.
It gives `r_B=O(log B/log log B)` and fixed-exponential interpolation cost
`C^r_B=B^o(1)`. Squarefree support is essential to this argument.

The Hilbert-valued Chebyshev inequality is valid: scalarize by the direction
of the target value, take the real part on the real interval, and apply the
ordinary scalar extremal inequality. The squared-norm transfer correctly
spends a small exponent loss on `C^(2r_B)`.

I also independently checked the positive-measure strengthening. Greedy
spacing `delta=m/[2(r+1)]` yields `r+1` points of the measurable set. After
ordering, the `j`th Lagrange denominator is at least
`delta^r j!(r-j)!`; the sum of reciprocal factorials is `2^r/r!`. This gives
the stated `(8eM/m)^r` norm cost, including a fixed complex target. The
countable uniform-bound subsets cover the parameter set, so one has positive
measure. No interior-point or Baire conclusion is being improperly inferred
for a positive-measure set.

The Baire proof on an interval is also valid with an arbitrary, possibly
uncountable, collection of row/length/profile data: an arbitrary intersection
of the corresponding closed inequality sets remains closed. The bounds must
hold for every datum in the same collection, as stated.

Corollary 3 correctly retains the fixed-power range `A<=B^C` before absorbing
the pointwise `AB` loss into a positive `B` saving. Without that hypothesis,
its stated argument would fail; the reviewed version includes it.

The fixed-integer counterexample and interpolation weights were checked
algebraically. Bounds at all fixed integer orders need not imply the desired
continuum control. The discussion of centered moments correctly treats the
full signed real polynomial and keeps any subtraction/projection fixed in
the coefficient parameter.

## 2. Direct ordinary-squarefree endpoint

I inspected the primary source
https://arxiv.org/html/2610.17675v2, Theorem 2.2 and Corollary 2.3. Its
displayed estimate has the factor `K_row R Z^epsilon`, nonprincipal inducing
rows, a common redundant zero puncture, fixed-power length ranges, finite
profile seminorms and polynomial separated-height costs. It explicitly has
no zero-slot restriction on the two bounded nonnegative logarithmic lengths.

For the reviewed note's fixed finite ray data, `R` is fixed. Taking equal
ordinary factors gives the needed fourth moment; Cauchy gives the second
moment. The opposite character orientation is covered by conjugating the
fixed ray data, profile and norm twist, retaining the zero extension.

The squarefree sieve identity is exact. Its normalized multiplier is
`mu(d) psi_u(d^2) (Nd)^(2it)/(Nd)` and the residual scale is `D/(Nd)^2`.
There is no spurious coprimality condition on the residual column. Minkowski
may discard the outside multiplier in a positive row norm because its
modulus is at most one. The ideal harmonic sum costs only a logarithm in
this fixed field.

The principal-row qualification is necessary and correctly stated. Under
the source's fixed excluded set and sixth-power-free physical indexing,
principal induction has only bounded exceptional rows (or only the unit in
the simplest unshifted family). The note explicitly refuses to extend this
argument to moving coefficient conductors or unrestricted sixth powers.

The direct endpoint and the continuum-to-native implication are therefore
supported *relative to the imported ordinary moment*. The noninteger
coefficient estimates in Targets A and B remain assumptions. Neither the
endpoint alone nor coefficient interpolation establishes them.

## 3. Fractional and marked zero detectors

The correction `H_z` is holomorphic and nonvanishing for `Re s>1/2` when
`0<z<1`: the local linear terms cancel and the logarithms have their
canonical branches. At a zero of multiplicity `m`, an irrational coefficient
parameter gives nontrivial monodromy `exp(2 pi i m z)`.

I requested an explicit restatement of `1/2<=b<1` and irrational
`z in (0,1)` in the smoothed-sum Lemma 3. The frozen version includes it.
This matters because a rational parameter only detects multiplicities not
divisible by its denominator. The entire-L/nonprincipal finite-order scope
also correctly excludes the known poles of pure norm twists.

The Mellin smoothing need not avoid an unknown zero: it has an integer order
there, which cannot remove a noninteger local exponent. Likewise the marked
coefficient identity has singular part `(s-rho)^m log(s-rho)` times a
nonzero analytic factor. Multiplication by a nonzero entire Mellin transform
does not remove that logarithmic monodromy.

The family-density section is explicitly conditional. I checked its
derivatives, concavity, stationary-point formula, and target comparison.
At `sigma=3/4`, the optimistic density is `7/12` and the required envelope
is `23/48`, giving exactly `5/48`; concavity makes this the maximum deficit
over the stated interval. The actual source starts at `sigma>51/100` and
has only its specified physical index and height scope. Those limitations
are retained instead of silently promoting the algebraic extension to a
proved density theorem.

## 4. Boundary of the review

The packet establishes a nontrivial coefficient-transfer mechanism and a
source-dependent accessible endpoint. It does not establish a continuous
family moment, a complete slit-contour estimate, stronger joint zero/value
control, or a new zero-free boundary. The review accepts precisely that
scope. The finite checkers were not used as substitutes for the analytic
arguments reviewed here.
