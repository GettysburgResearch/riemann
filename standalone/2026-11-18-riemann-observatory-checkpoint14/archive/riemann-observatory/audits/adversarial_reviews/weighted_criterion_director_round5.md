# Weighted closure: a verified counterexample and the corrected threshold

2026-11-17. Director adjudication after reading the complete proposer proof, two independent necessity reconstructions and the independent sufficiency audit. The director also independently derived the direct radial functional, exact Mellin values, concrete norm bound, weighted Mellin sufficiency and coefficient multiplier estimate. This is a scoped ordinary mathematical result with declared classical inputs. Historical priority is unassessed. There is no RH proof or source-wide audit.

## Exact source finding

The director visually checked the publisher's actual page26 of PAPER-E012, Gallardo–Gutiérrez–Seco2025, DOI10.1007/s11785-025-01661-2. Theorem5.5 states an **if and only if**, with alpha∈[-3,-2], 1<=a<(1-alpha)/2, between the specified weighted target closure and zero-freeness of Re(s)>(-1-alpha)/2. The inspected arXiv2206.02654v6 page21 has the same assertion.

**Verified mathematical error in that printed reverse implication:** at the allowed pair(alpha,a)=(-3,7/4), the printed half-plane is Re(s)>1 and is zero-free, but the target is outside the stated closed span. This counterexample is separate from Proposition5.1's critical endpoint; here the first-order operator is strictly above that endpoint. The earlier approximation-to-zero-free implications in Theorems2.1/3.1 are not refuted by this finding. Agreement among agents is not the evidence: the evidence is the explicit bounded functional and nonzero target value below.

## Direct separating functional in the source norm

Put t=-(alpha+1)/2, c=a-1, b=t-c>0, beta=alpha+2=1-2t, u=(1-z)^(-c), and

h_k(z)=(1-z)^(-1)Log[(1+z+...+z^(k-1))/k].

All analytic power/log branches are positive or real on the radius(0,1), with the indicated normalization at0. The coefficient estimates u_n=O((n+1)^(c-1)) and [z^n]h_k=O_k((n+1)^(-1)) show that u and every u h_k belong to D_beta; the resulting squared norm exponent is -1-2b<-1, with a harmless logarithm for the products.

For Re(s)>b define

Lambda_s(f)=[s Gamma(s)]^(-1) integral_0^1 (-logr)^(s-1)(1-r)^(c+1)[fprime(r)-a f(r)/(1-r)]dr.

The source norm is ||f||²_D_beta=Sum(n+1)^beta|f_n|². Coefficient Cauchy–Schwarz gives |f(r)|<=C||f||(1-r)^(-t) and |fprime(r)|<=C||f||(1-r)^(-t-1). Thus the boundary exponent in the absolute integral is Re(s)-b-1, which is integrable precisely in the needed strict region. Near0 the logarithmic power is integrable and the evaluations are uniformly bounded. No inverse operator, RH, numerical zero location or closure-topology substitution is used.

The product rule with a=c+1 gives

Lambda_s(u)=-1/s,
Lambda_s(u h_k)=(1-k^(1-s))zeta(s)/s.

One independent check expands the bounded remainder coefficients and uses adjacent-power differences. Another differentiates B_k=(1-z)h_k, obtaining B_kprime(r)=1/(1-r)-k r^(k-1)/(1-r^k), a function bounded at both radial endpoints. Separate geometric-series integration for Re(s)>1 followed by holomorphic continuation gives the same exact value throughout Re(s)>0. These routes check the normalization and target sign independently.

At a zeta zero rho with Re(rho)>b, Lambda_rho annihilates the entire closed generator span but takes nonzero value-1/rho on u. Hence closure implies zero-freeness in the larger half-plane Re(s)>b=t-(a-1).

For alpha=-3,a=7/4, b=1/4. Riemann–von Mangoldt gives at least one nontrivial zero and functional-equation reflection gives one with real part at least1/2. Such a zero separates the target unconditionally, while the Euler product establishes the printed Re(s)>1 premise. Theorem5.5's claimed reverse direction is therefore false in these versions.

The separation has a concrete positive lower bound. For any such rho with sigma=Re(rho)∈[1/2,1], exact Bergman evaluation sums give

dist_D_-1((1-z)^(-3/4),span{(1-z)^(-3/4)h_k})
>=|Gamma(rho)|(sigma-1/4)/(sqrt6+7/4)>0.

Indeed the derivative evaluation sum is2(1+2r²)/(1-r²)^4, and -logr>=1-r with exponent sigma-1<=0 bounds the radial integral by1/(sigma-1/4). This bound was independently checked. It is an analytic witness, not a numerical approximation to a distance.

## Accepted corrected equivalence

For the **same** target, generator span, source coefficient norm and original parameter range, the independently reconstructed correct statement is

u in closure_D_(alpha+2) span{u h_k:k>=2}
iff zeta(s) has no zeros in Re(s)>b,

where b=(1-alpha)/2-a=t-c∈(0,1].

Necessity is the direct functional. For1/2<=b<1, sufficiency follows from the Balazard–Saias estimate as reproduced in Báez-Duarte's actual math/0202141v2 Lemma2.1,p3, plus classical convexity, the completed Hadamard product and elementary Hilbert-space estimates. The original1998 lemma proof is an explicitly accepted external dependency, not newly audited in full.

Here is the shorter checked proof chain. Work in H_b=L²((0,infinity),x^(2b-1)dx). For fixed epsilon>0, the Mellin transforms of Sum_(k<=N)mu(k)k^(-epsilon){1/(kx)} converge to -zeta(s)/[s zeta(s+epsilon)] on Re(s)=b by the quoted lemma and convexity. Constants may depend on epsilon; take N→infinity first. Since every completed-function zero lies to the left of or on that line, canonical factorwise distance comparison bounds the quotient uniformly by C(1+|Im(s)|)^(epsilon/2). Choosing a fixed small epsilon0 gives an integrable squared majorant. Dominated convergence as epsilon→0 places the indicator of(0,1) in the closed fractional-part span. Cancel the exact1/x tails with a multiple of{1/x}; the constrained step functions identify the remainder span with coefficient weights comparable to n^(-1-2b).

Multiplication by u maps D_(-1-2b)=D_(alpha+2c) boundedly to D_alpha. The independently checked positive convolution matrix has bounded row and column sums, including the far triangular part; its Schur test uses b+1/2>0. Finally the strict T_a inverse transports the approximants because a-t=1-b>0 and T_a u=-u/(1-z), T_a(u h_k)=u R_k. At b=1 the sole pair(-3,1) uses the separately proved unconditional Bergman closure, rather than an invalid critical inverse. At0<b<1/2 the zero-free assertion and closure both fail by the zero count/reflection and necessity. This covers the entire original parameter range.

Consequently the RH equivalence occurs on the parameter line a=-alpha/2. The admissible region above this line has b<1/2 and the closure is impossible. Below it the closure is equivalent to a weaker zero-free half-plane b>1/2; at(-3,1) it is unconditionally true. The source's independence from a is the missing parameter dependence. This phase description is a consequence of the corrected theorem, not a new zero-free result.

## A boundary check and the arithmetic core failure

The separating functional is not silently used on Re(s)=b. Its monomial values satisfy n^(s+c)Lambda_s(z^n)→(s-1)Gamma(s+c)/[s Gamma(s)]. At that boundary and s!=1 the squared values on normalized monomials form a harmonic divergent sum, so there is no bounded extension. This independently verifies the strict threshold. The exceptional b=s=1 functional on polynomials is-f(0), not a zeta-zero witness.

At the concrete counterexample the ordinary D_-3 closure of span R_k does contain1/(1-z), by the separately established Bergman approximation and bounded T_1. The pulled-back weighted norm does not. Thus this is a failure for the special arithmetic span itself, not merely a generic observation that a multiplier is not bounded below. The old general-core open task is resolved in this parameter range by a counterexample and a corrected equivalence.

## Evidence and version limits

Proposer: gallardo_seco_weightedcore62_round5.md and gallardo_seco_corrected_threshold_weightedcore62_round5.md. Independent checks: gallardo_seco_weighted_mellin_witness62_round5.md; gallardo_seco_necessity_threshold62_round5.md; gallardo_seco_sufficiency_threshold62_round5.md. Exact primary page locations, source hashes and checked current Crossmark/arXiv snapshots are retained there. No listed correction was found in the checked official records through2026-11-17; this is not an exhaustive absence or priority claim. No contact with authors or publication occurred.
