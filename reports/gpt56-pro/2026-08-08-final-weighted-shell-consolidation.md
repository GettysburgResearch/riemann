# Final consolidation — weighted shell-tail carry transport

Date: 2026-08-08  
Agent: `gpt56-pro`  
Canonical branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: **review-ready full proposal with one explicitly open RH-equivalent theorem**

## Executive conclusion

The live carry/Green programme has now been consolidated around the weighted
dyadic shell.  The resulting packet is substantially narrower than the earlier
Carry Sandwich, Green deformation, endpoint-scale blocker, and unweighted
prime-tail proposals.

The exact chain is

```text
parabolic seed
-> continuum shell majorization
-> weighted finite shell transport
-> summable carry-floor correction
-> one Chebyshev Stieltjes remainder
-> WSTS
-> sharp prime-ramp lower bound
-> square-screw/Landau
-> RH.
```

The first, second, third, fourth, and final conditional arrows are written
explicitly on the branch.  `WSTS` is not proved.

`T-23812` now proves the converse implication under the classical RH estimate
for `theta(x)-x`, so

```text
WSTS <=> RH.
```

This makes the status boundary unmistakable.  The proposal is ready for review
of its exact reductions and of the single source-specific arithmetic hinge, but
it is not an unconditional proof of RH.

## Why the weighted shell is canonical

The newest ordinary-prime transport work closes finite positivity and transport
geometry exactly.  However, the unweighted full prime suffix has a proposed
deterministic positive density drift of order

```text
sqrt(X)/log^2(X).
```

Accordingly an unweighted subpower prime-tail theorem cannot be the final
consumer.  The dyadic shell residual

```text
r_X(p)-1_(p<=floor(X/2)) r_(floor(X/2))(p)
```

cancels this first-order density drift before the tail maximum is formed.

The logarithmic weight is equally load bearing.  It is the exact prime-objective
coordinate and retains the fixed-ratio Mertens firewall.  The shell theorem is
therefore neither a generic PNT remainder nor an arbitrary smoothing.

## New theorem: atomwise continuum order

`L-23827` strengthens the continuum side.  If `k(u)` is the response of one
positive parabolic endpoint atom, then on

```text
1/(N+1) < u <= 1/N
```

one has

```text
k(u)=2N-S_N/sqrt(u).
```

The upper-tail discrepancy from the critical endpoint increment `u^-1/2` is
exactly

```text
K(theta)=2[(S_N+1)sqrt(theta)-N theta-1].
```

Since `S_N+1<=2 sqrt(N)`,

```text
K(theta)<=-2(sqrt(N theta)-1)^2<=0.
```

Thus every endpoint atom individually admits an ordered positive transport into
its critical target increment with nonnegative logarithmic gain.  The continuum
obstruction is absent before the endpoint atoms are summed.

The remaining difficulty is purely the finite prime/divisor sampling of this
ordered transport.

## Exact finite reduction

For the dyadic shell `Y=floor(X/2)`, `L-23825` gives

```text
s_(X,Y)(q)
 =X^(-1/2) E_c(q/X)
  +epsilon_(X,Y)(q),
```

where the floor error is absolutely summable in the `log p` norm.  Stieltjes
summation gives

```text
sum_(z<=p<=X) log(p) s_(X,Y)(p)
 =sqrt(X) H_c(z/X)
  +E_Chebyshev(X,Y;z)
  +O(log^2 X).
```

The continuum term is nonpositive and has an explicit square-root moat.  The
only uncontrolled quantity is

```text
sup_z (E_Chebyshev(X,Y;z))_+.
```

`L-23824/L-23826` turn a subpower bound for that scalar into an exact weighted
carry correction and then into the sharp prime-ramp estimate.

## Equivalence theorem

`T-23811` proves

```text
WSTS -> RH.
```

The new `T-23812` proves the converse.  Under RH,

```text
theta(t)-t=O(sqrt(t) log^2(2t)).
```

Elementary reciprocal-cell bounds give

```text
|E_c(u)|    << u^(-1/2)(1+log(1/u)),
|E_c'(u)|   << u^(-3/2)(1+log(1/u)).
```

Stieltjes integration by parts then yields uniformly in the tail endpoint

```text
E_Chebyshev(X,Y;z)=O(log^4 X).
```

Hence

```text
RH -> WSTS,
```

and the two statements are equivalent.

## What remains useful from the other branches

### Green and affine branches

They prove that physical nonnegativity is not an independent asymptotic
obstruction.  Exact Green equality, Skorokhod clipping, and the one-prime affine
lift remain useful certificate implementations.  Their open scalar is the same
prime-ramp mode now isolated by `WSTS`.

### Endpoint-scale branch

It supplies a positive endpoint dictionary and the continuum endpoint kernel.
Its blocker theorem is a possible finite producer for `WSTS`, but is not a
separate conclusion-producing theorem.

### Dyadic factor-five branch

It supplies mandatory source mutations and a source-specific carry-space reserve.
Any proposed proof of `WSTS` must retain the odd target, the two-contact source,
and the first fixed-ratio Mertens shell.  The still-open physical transference is
an optional proof mechanism, not an imported theorem.

### Squarefree collector branch

It identifies the correct response to the unweighted prime-density drift:
composite collectors can change total ordinary-prime incidence while remaining
neutral on proper prime powers.  This is a serious alternative finite mechanism
for proving the weighted shell theorem, but its all-scale collector theorem is
open.

## Review order

1. `L-23823-normalized-tail-and-fixed-ratio-shell-majorization.md`
2. `L-23827-endpoint-atom-tail-majorization.md`
3. `L-23824-zero-cost-weighted-prime-tail-transport.md`
4. `X-23821-weighted-shell-transport/verify.py`
5. `L-23825-finite-shell-profile-and-prime-sampling-remainder.md`
6. `L-23826-in-support-weighted-tail-charge-and-shell-sum.md`
7. `T-23811-weighted-shell-tail-carry-proposal.md`
8. `T-23812-weighted-shell-tail-equivalent-to-rh.md`
9. `M-23813-final-weighted-shell-review-boundary.md`
10. frozen dependencies and mutation branches in the audit TSV

## Decisive reviewer questions

1. Are the reciprocal-cell shell formulas and normalized-tail monotonicity exact?
2. Is the endpoint-atom discrepancy formula correct and continuous at every reciprocal knot?
3. Are the weighted tail-transport signs and objective conventions correct?
4. Is the carry-floor error uniformly and absolutely summable as stated?
5. Does the Stieltjes identity contain every endpoint and shell-cutoff term?
6. Is the WSTS-to-prime-ramp assembly free of an unweighted density-drift term?
7. Does `RH -> WSTS` use only the standard Chebyshev consequence of RH and the displayed profile bounds?
8. Does the square-screw/Landau consumer have the correct sign and normalization?
9. Can an unconditional argument prove the one-sided Chebyshev remainder bound without assuming an RH-equivalent input?

## Exact status

```text
continuum normalized-tail theorem          PROPOSED COMPLETE
endpoint-atom tail theorem                 PROPOSED COMPLETE
finite weighted transport                  PROPOSED COMPLETE
floor and Stieltjes reduction              PROPOSED COMPLETE
WSTS -> RH                                 PROPOSED COMPLETE CONDITIONAL
RH -> WSTS                                 PROPOSED COMPLETE
WSTS                                       OPEN / RH-BEARING
Riemann Hypothesis                         NOT PROVED
```

The packet is therefore complete as a **reviewable proposal and exact reduction**.
It is not complete as an unconditional proof of RH.
