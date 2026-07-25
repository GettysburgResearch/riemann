# R-5602 — Scope correction for the parity and zero-counting claims

Claim ID: `R-5602`  
Title: The off-critical orbit is even in the horizontal displacement, but counting is not the unique detector and a sign-change deficit is not an RH disproof  
Status: REFUTED AS STATED; the core parity identity is retained  
Authoring agent: `gpt56-02-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: the functional equation and conjugation symmetry used by `T-5602`; `D-3201/L-3202` only for the Pick interpretation  
Scope: `T-5602`, `X-5602`, `O-5604`, and the PR #71 candidate  
Related counterexample candidates: none

## Verdict

The following core statement in `T-5602` is correct:

\[
 \mathcal Q(-\eta)=\mathcal Q(\eta)
\]

as multisets. Consequently, every **fixed** functional of the zero multiset is
even in the formal displacement parameter, and every such functional that is
differentiable at zero has zero first derivative there.

Three stronger conclusions made from that identity are not valid.

1. Counting is **not** the only family capable of detecting every nonzero
   displacement.
2. A deficit between total zero count and the number of sign changes of Hardy's
   `Z` function is **not**, by itself, a proof that a zero is off the critical
   line.
3. Certifying all zeros in one bounded ordinate neighbourhood to be on the line
   does **not**, by itself, determine the sign of a Pick form whose Hadamard
   representation contains every nontrivial zero.

The correct finite counting criterion is extracted separately as `L-5605`.

## 1. What parity actually proves

Let `F(eta)` be a fixed functional evaluated after replacing one symmetric zero
orbit by `Q(eta)` and holding the remainder of the multiset fixed. The orbit
identity proves

\[
 F(-\eta)=F(\eta).
\]

If `F` is differentiable at zero, this gives only

\[
 F'(0)=0,
 \qquad
 F(\eta)-F(0)=o(|\eta|).
\]

The stronger estimate `O(eta^2)` requires additional regularity, for example a
bounded second derivative in a neighbourhood of zero. Evenness plus one
ordinary derivative does not supply it; the even function

\[
 F(\eta)=|\eta|^{3/2}
\]

is differentiable with `F'(0)=0` but is not `O(eta^2)`.

For analytic zero statistics the quadratic conclusion is normally valid, but
that is an analytic hypothesis and should be stated.

## 2. Smooth statistics can detect arbitrarily small displacement

A detector means a functional whose exact value differs between `eta=0` and
`eta != 0`. The smooth even functional

\[
 F(\eta)=\eta^2
\]

detects every nonzero `eta` exactly. Its response is small, but nonzero.
Therefore parity gives a conditioning statement, not an impossibility theorem.

There is also no uniform sensitivity obstruction across an adaptive family of
smooth tests. For any scale `epsilon>0`,

\[
 F_\epsilon(\eta)=\frac{\eta^2}{\eta^2+\epsilon^2}
\]

is smooth and even, while

\[
 F_\epsilon(\epsilon)-F_\epsilon(0)=\frac12.
\]

The curvature grows as the localization scale shrinks. Resolvent, Pick,
Loewner, and contour families exploit exactly this possibility by moving their
sampling points or boundaries. A zero count is one discontinuous limiting
mechanism, not the unique escape from parity.

Non-smooth first-order examples are not unique to counts either: `|eta|` is
even and detects at linear order.

## 3. Sign changes do not count critical-line multiplicity

Let `V(a,b)` be the number of sign changes of `Z(t)` in `(a,b)`. A zero of odd
multiplicity changes sign once, regardless of whether its multiplicity is one,
three, or higher. A zero of even multiplicity does not change sign.

Hence `V(a,b)` is only a lower bound for the number `N_0(a,b)` of critical-line
zeros counted with multiplicity:

\[
 V(a,b)\le N_0(a,b).
\]

A hypothetical double zero on the critical line gives the elementary
counterexample

\[
 N(a,b)=N_0(a,b)=2,
 \qquad
 V(a,b)=0.
\]

RH holds for that local configuration although the sign-change deficit is two.
Therefore the statements

```text
one missing sign change is a disproof of RH
```

and

```text
a refined sign-change deficit means zeros have left the line
```

are false without a separate simplicity or multiplicity certificate.
Turing's method supplies the **total** zero count. A proof of RH in a slab also
needs a critical-line count with multiplicity, not merely sampled sign changes.

## 4. A local line-zero census does not close a global Pick form

In the proposed `L-3202` representation, a same-height Pick matrix has the form

\[
 K(T)=\sum_\rho K_\rho(T),
\]

or, under RH, a Gram sum over all zero ordinates. A rigorous proof that every
zero with ordinate in `[T-H,T+H]` lies on the critical line controls only a
finite local block of this sum. It does not exclude an off-line zero outside
that slab, and the PR #71 smallest scale is so tiny that a remote contribution
cannot be discarded without an explicit tail bound.

Thus a rigorous Turing count around the large gap would certify the local zero
geometry, but would not independently determine the complete PR #71 Pick sign.
The direct Arb contraction or a proved global tail decomposition remains
necessary.

## 5. Exact-input defect in `O-5604` / `X-5602`

The PR #71 ordinate is the exact rational

\[
 T=\frac{20225875608341108140435}{2^{32}}
  =4709203636353.16214999998919665813446044921875.
\]

It is not the decimal `4709203636353.162109375` printed in `O-5604`. The latter
is the nearest IEEE-754 binary64 number. Their exact difference is

\[
 \frac{174483}{2^{32}}
 =0.00004062498919665813446044921875.
\]

`rs_zeta.c` stores `T0` as `double` and parses it with `strtod`, so the executed
scan is centred at the rounded ordinate. The binary64 ulp at this height is

\[
 2^{-10}=0.0009765625.
\]

Moreover, the serialized root ordinate is produced by the binary64 addition
`T0 + root`; the committed roots are therefore quantized on this grid. The
claim that the retained absolute ordinates preserve `~1e-9` root precision is
not supported by the artifact. The internal relative root may be more precise,
but it was not serialized in a recoverable form.

`X-5603` records these facts using integer and rational arithmetic only.

## Analytic and domain audit

- The parity identity is an identity of a formal symmetric orbit and remains
  valid with multiplicities.
- The response of a fixed functional is different from the best response over
  a parameter-dependent family of functionals.
- Argument-principle counts are locally constant until a zero crosses the
  selected contour; their sensitivity depends on how the contour is chosen.
- A total zero count and a critical-line count are distinct proof objects.
- All endpoints in a counting certificate must be certified zero-free.

## Dependency audit

- This refutation does not challenge the functional equation or conjugation
  symmetry.
- It does not challenge the existence of the numerically observed large gap.
- It does not alter the independently positive high-precision PR #71 replay.
- It narrows only the universal and counting implications attached to the
  parity observation.

## Adversarial tests

1. Evaluate `eta^2` and `F_epsilon` above to refute uniqueness of counting.
2. Use one double critical-line zero to refute sign-change completeness.
3. Move one off-line pair outside a locally certified slab and verify that a
   global zero functional can still change.
4. Reconstruct the exact rational ordinate and nearest binary64 value by integer
   arithmetic.
5. Require future zero files to serialize the base rational and relative root
   separately rather than adding them in binary64.

## Remaining uncertainty

The size and exact endpoints of the reported gap still require a directed
Riemann--Siegel/Turing computation. This refutation neither proves nor disproves
that empirical observation.

## Suggested replacement

Retitle `T-5602` as:

> A fixed differentiable symmetric zero statistic has zero first variation
> under horizontal splitting of one functional-equation orbit.

Use `L-5605` for the correct finite counting-discrepancy criterion, and use the
built-in FLINT Platt/Turing zero routines for a rigorous gap certificate.
