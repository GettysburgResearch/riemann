# Support-averaged attack on the final extra-low spectral trace

Agent: `gpt56-08`  
Date: 2026-08-01  
Active branch: `agent/gpt56-pro-09-d/156-capacity-saturation`  
Primary PR: #163  
Classification: exact new abstract bridge and cofinal reduction; no RH proof

## Requested target

The target was

\[
 \operatorname{Tr}
 Q_j(\Gamma_jI-A_j)_+Q_j
 =o(\Gamma_j-t_j)
\]

along a cofinal support sequence, without returning to the already-completed
four-defect bookkeeping.

## New exact bridge

`L-15626` proves that a compression floor is sufficient even when the packet
projection does not reduce the operator. If

\[
 QAQ\succeq\gamma Q,
 \qquad\gamma>\Gamma,
\]

then

\[
 \operatorname{Tr}Q(\Gamma-A)_+Q
 \le
 {\|QAP\|_{HS}^2\over4(\gamma-\Gamma)}.
\]

With the production cross bound

\[
 PAQAP\preceq\beta^2P,
 \qquad\operatorname{rank}P=d,
\]

this becomes

\[
 \operatorname{Tr}Q(\Gamma-A)_+Q
 \le{d\beta^2\over4(\gamma-\Gamma)}.
\]

The proof expands the exact low spectral projection, solves the complement
component of each low eigenvector through `QAQ-lambda`, and uses the sharp scalar
maximum

\[
 \sup_{\lambda<\Gamma}
 {\Gamma-\lambda\over(\gamma-\lambda)^2}
 ={1\over4(\gamma-\Gamma)}.
\]

This closes a real logical gap between a form-compression floor and the spectral
functional-calculus trace.

## Support averaging

The newest radial/source work on PR #164 supplies the following architecture:

- dimension-free line-centered local Weyl scalarization;
- exact radial normalization and a uniform quadratic-log mode window;
- endpoint and Poisson-alias ledgers;
- a positive arithmetic tail-profile Gram;
- Selberg-moment control of the critical-line two-branch error;
- a Hilbert-valued large sieve in the support parameter for the reflected
  off-line cross branch.

`L-15627` packages those ingredients at the level needed by the spectral trace.
If the whitened complete-complement profile has amplitude/derivative envelope
`B_T`, the support large sieve gives

\[
 {1\over T}\int_T^{2T}\|H_R\|^2dR
 \ll {B_T^2(\log T)^3\over T}+o((\log T)^2).
\]

Therefore the subcritical condition

\[
 B_T=o\!\left(\sqrt{T/\log T}\right)
\]

selects an unbounded support sequence on which the horizontal error is
`o(log R)`. Combined with the positive profile Gram and regular local-Weyl
errors, this gives

\[
 QA_RQ\succeq c\log R\,Q.
\]

Taking `Gamma` below that floor and applying `L-15626` yields the requested
spectral-trace estimate. For the existing Gevrey near-radical packets, the
remaining cross factor `d beta^2` is superpolynomially small, so it cannot be the
blocker.

## Strongest conclusion

The target is now proved from one quantitative structural statement:

```text
The actual complete dangerous complement admits a whitened source/profile
frame with envelope B_T=o(sqrt(T/log T)).
```

A polylogarithmic frame bound would be far stronger than necessary.

## Exact blocker

The repository currently proves separately that:

1. a constructed prolate/global-anchor radical frame has polylogarithmic
   coefficient conditioning and the required radial/alias profiles;
2. generic-support density or the explicit Möbius construction gives
   qualitative/exact source surjectivity onto finite localized vectors.

It does not prove that the first frame is a frame for the **complete dangerous
complement**, nor that an arbitrary complete source right inverse has the
sub-square-root profile envelope above.

The Möbius extension theorem explains the gap. Every local vector has an exact
global-radical extension, but at every zeta zero its lower tail satisfies

\[
 \widehat t(z_\rho)=-\widehat h(z_\rho),
\]

and its tail Weil matrix equals the target Weil matrix. Existence of a right
inverse therefore does not control its proof norm.

The final theorem is a quantitative complete-source-frame conditioning bound,
not another trace identity:

\[
 \boxed{
 B_T=o\!\left(\sqrt{T/\log T}\right).}
\]

Under false RH, the persistent off-line Xi-cardinal mode forces this bound to
fail (or forces degeneration of the profile Gram/regular-error theorem). This
gives a quantitative square-root conditioning dichotomy rather than a generic
statement that the right inverse may be ill-conditioned.

## Literature audit

The recent localized screw/operator work supplies an exact finite-support
framework but leaves its large-support spectral limit conjectural. Modern PSWF
asymptotics provide the radial profile control, while Nyman--Beurling-style
results repeatedly relocate RH into a coefficient/right-inverse norm. I found no
primary-source theorem supplying the required complete-frame lower singular
value at the sub-square-root scale.

## Verdict

```text
requested spectral trace:      closed conditionally by L-15626/L-15627
new structural gain:           support averaging lowers the frame requirement
                               to o(sqrt(T/log T))
existing packet cross rates:   sufficient
complete-frame conditioning:   unproved
RH:                            not proved
```
