# L-12102 — Certified slab-complement Pick positivity

Claim ID: L-12102  
Title: Complete critical-line zero bins turn the quadratic Pick contraction into an RH-nonnegative slab-complement matrix  
Status: PROPOSED  
Authoring agent: `gpt56-06-f`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: L-12101; proof-grade slab count and zero-bin certificates  
Scope: finite RH-disproof certificates from arbitrary-height `xi'/xi` values and complete zero slabs  
Related counterexample candidates: none

## Statement

Retain the notation of L-12101. Let \(a<b\) be exact real numbers and suppose
the following unconditional data have been certified:

1. neither endpoint ordinate is a nontrivial zero;
2. the slab \(a<\operatorname{Im}\rho<b\) contains exactly \(m\) nontrivial
   zeros counted with multiplicity;
3. pairwise disjoint closed rational intervals

   \[
    I_r=[A_r,B_r]\subset(a,b)
   \]

   contain at least \(m_r\) actual critical-line zeros counted with
   multiplicity;
4. the multiplicities saturate the slab count:

   \[
    \sum_r m_r=m. \tag{1}
   \]

Then every zero in the slab is one of the certified critical-line zeros in the
bins. No RH assumption is used in this completeness statement.

For an exact zero-sum vector \(v\), define

\[
 Q_{[a,b]}(v)
 =
 2\operatorname{Re}\sum_i c_iF(s_i)
 -
 \sum_{\substack{\gamma:\\a<\gamma<b}}
 g_{a,b}(\gamma)|\Phi_v(\gamma)|^2, \tag{2}
\]

where \(c_i\), \(g_{a,b}\), and \(\Phi_v\) are from L-12101 and the second sum
uses the actual certified in-slab critical-line zeros with multiplicity.

Under RH,

\[
 \boxed{
 Q_{[a,b]}(v)
 =
 \sum_{\gamma\notin(a,b)}
 g_{a,b}(\gamma)|\Phi_v(\gamma)|^2
 \ge0.
 } \tag{3}
\]

Consequently, exact rational/dyadic point and vector data, proof-grade
rectangles for every \(F(s_i)\), and directed interval evaluation of every
in-slab term form a finite RH-disproof certificate whenever the final interval
for \(Q_{[a,b]}(v)\) has upper endpoint strictly below zero.

## Matrix form

Let

\[
 h(\gamma)_i=\frac1{\overline{z_i}+i\gamma}.
\]

The full weighted matrix \(M^{[a,b]}\) is defined in L-12101. Define the exact
slab-complement matrix

\[
 M^{\rm out}_{[a,b]}
 =
 M^{[a,b]}
 -
 \sum_{\substack{\gamma:\\a<\gamma<b}}
 g_{a,b}(\gamma)\,h(\gamma)h(\gamma)^*. \tag{4}
\]

Under RH,

\[
 v^*M^{\rm out}_{[a,b]}v\ge0
 \qquad
 \text{for every }v\in{\bf 1}^{\perp}. \tag{5}
\]

Thus the certificate family includes:

- one exact frozen-vector contraction;
- an exact finite PSD Gram portfolio on the zero-sum subspace;
- a whole-matrix positive closure;
- a negative eigenvector nomination followed by exact Gaussian-rational replay.

The interval checker need not serialize an interval eigensystem. It may
contract one frozen vector against primitive \(F\) rectangles and zero bins.

## Proof

By (1) and the endpoint-zero gates, the certified line-zero bins account for
all zeros in the open slab. Assume RH. Then every nontrivial zero is on the
critical line, so L-12101 gives

\[
 2\operatorname{Re}\sum_i c_iF(s_i)
 =
 \sum_{\gamma}g_{a,b}(\gamma)|\Phi_v(\gamma)|^2.
\]

Subtract the complete in-slab terms. What remains is the sum over
\(\gamma\notin(a,b)\). For those ordinates,

\[
 g_{a,b}(\gamma)=(\gamma-a)(\gamma-b)\ge0.
\]

Every modulus square is nonnegative, proving (3). The matrix statement is the
same decomposition before contraction. ∎

## Proof-grade interval semantics

For a bin \(I=[A,B]\), exact rectangular arithmetic encloses

\[
 \Phi_v(I)
 =
 \sum_i
 \frac{\overline{v_i}}
 {z_i-iI}. \tag{6}
\]

It also encloses the quadratic weight

\[
 g_{a,b}(I).
\]

Because \(I\subset(a,b)\), the weight interval is nonpositive. An interval for

\[
 g_{a,b}(I)|\Phi_v(I)|^2
\]

contains the contribution of each zero in the bin. Multiplication by the
certified lower count \(m_r\) encloses their total because every one of those
zeros lies in the same bin. Summing over bins and subtracting from the finite
\(F\)-contraction gives a rigorous enclosure of (2).

The proof object must retain the **joint bin interval**. Replacing one
\(\gamma\) by independent copies inside the reciprocal factors and the
quadratic weight is allowed only as an outward overapproximation.

## Strict separation from ordinary Pick passivity

The exact synthetic model in X-12101 uses

\[
 [a,b]=[-1,1],
\]

one certified critical-line zero at \(\gamma=0\), one reflected off-line pair
at horizontal displacement \(1/2\), points

\[
 \left(
 \frac15-\frac i2,\,
 \frac15+\frac i2,\,
 \frac25-\frac i2,\,
 \frac25+\frac i2
 \right),
\]

and

\[
 v=(-2,2,-1,1).
\]

The ordinary Pick form is strictly positive:

\[
 v^*Kv
 =
 \frac{7450901935000}{47129216977}>0. \tag{7}
\]

The weighted full-zero contraction is

\[
 -\frac{8286764476250}{47129216977},
\]

and the certified in-slab line-zero contribution is

\[
 -\frac{123210000}{1413721}.
\]

The slab-complement residual is

\[
 \boxed{
 Q_{[-1,1]}(v)
 =
 -\frac{2956250}{33337}<0.
 } \tag{8}
\]

Thus the new finite witness can be negative on data for which ordinary Pick
passivity is strictly positive.

This is an exact synthetic zero model, not a Riemann-\(\xi\) evaluation.

## Relationship to current repository closures

The theorem is not blocked by the finite closures already obtained:

- PR #67 closes a same-height real-value feature cone; (2) uses arbitrary
  heights, imaginary \(F\) components, and complete zero-location data.
- PRs #71/#80 replay ordinary Pick directions; (2) changes the spectral
  measure by a signed support polynomial and exact slab removal.
- PR #110 localizes one-height direct-\(\xi\) residuals by squared distance;
  (2) is an absolute-ordinate, cross-height matrix localizer.
- PRs #116/#117 close bounded-degree horizontal response cones on one table;
  (2) couples multiple ordinates through a zero-sum complex packet.

## Analytic-domain audit

- Every \(F\)-sample lies in \(\operatorname{Re}s>1/2\).
- Slab endpoints are certified zero-free.
- Every bin lies strictly inside the slab and bins are pairwise disjoint.
- The exact slab count and the bin multiplicities use compatible endpoint
  conventions.
- The vector sum vanishes exactly.
- Completeness is unconditional. RH is used only after completeness, to identify
  every remaining zero with a critical-line ordinate.

## Dependency audit

- L-12101 supplies the finite quadratic contraction.
- A Platt/Turing count, argument-principle count, or equivalent proof supplies
  the exact slab multiplicity.
- Saturated Hardy-\(Z\) sign chains such as PR #108 can supply complete
  one-zero bins.
- D-3201/L-3201/L-3202 remain parent analytic gates.

## Gap audit

- Lower zero counts without saturation are insufficient for (3): an unremoved
  in-slab zero has a negative weight and cannot be discarded.
- A total count without ordinate bins is sufficient only after a separate
  count-dual enclosure of the complete in-slab weighted sum.
- A negative midpoint is not a certificate.
- A final negative still requires independent \(F\) and zero-table
  reproduction and review of the parent normalization.

## Adversarial tests

1. Delete one bin while retaining the exact slab count; require rejection.
2. Overlap two bins; require rejection.
3. Let a bin touch a slab endpoint; require rejection.
4. Change one vector coordinate so that \(\sum v_i\ne0\); require rejection.
5. Widen one primitive rectangle until zero is touched; require `UNRESOLVED`.
6. Mutate one \(\alpha_{ij}\) sign in an independent implementation.
7. Compare the synthetic residual with direct finite-zero summation.

## Suggested next attack

Use the 172-bin saturated PR #71 slab from PR #108 and the 520-point complex
\(F\) table from PR #56. Build the residual matrix on 16--32 point
cross-height clouds, project to the exact zero-sum subspace, and optimize the
ratio of negative midpoint to complete directed radius before freezing any
Gaussian-dyadic finalist.
