# Independent component review of the fixed-shift and signed-ray proofs

Reviewer: native-amplitude agent, separate from the critical component's
proof/checker author. Date: 2026-10-18. This is agent review, not independent
human referee acceptance. No target file was edited by this reviewer.

## Exact reviewed identities

The current files were checked against `critical/HANDOFF.json` before review:

| File | SHA256 | Git blob |
|---|---|---|
| `critical/PROOF.md` | `54527c0c30700c324835f5e8f6928db64357e161193eaca0880fce10254948cc` | `e70f2b89ba847d60cf3efbbb52e64793b3c4afb5` |
| `critical/ARITHMETIC.md` | `786cb7a8c53986cb4d0cbd53695789de563ecbafd2e3e342fa2fbbf3e20fedbb` | `56f0195a8b7471fc7409c0f8f55432d9c9ec44fc` |

**Verdict: no mathematical correction found in these component statements
and proofs at their stated scopes.** Their remaining complete critical
upper estimate remains open. This review does not promote them to an RH proof.

## Single fixed shift and causal bounds

I independently reconstructed both Dirichlet convolution identities and
their inverse, retaining prime powers and common ideal factors. Critical
normalization changes a dilation coefficient to (NE)^(-h-1/2), so h>1/2
is precisely sufficient for the displayed absolute coefficient sums.
Changing variables really shortens each past horizon to T/NE; Minkowski
therefore gives the same constants for every horizon and every p, including
infinity. The exact continuum expression and all three L2 formulas were
recomputed by completing the square and Mellin Plancherel. Their constants,
the h=1 ordinary specialization, and the general h=3/2 choice check out.

For Theorem 2 I independently checked that the dyadic Cauchy estimate from
the subpower energy gives holomorphy on Re s>1/2, with the Gaussian flatness
paying the lower endpoint. At a denominator zero rho, the nonzero Gaussian
cannot remove a pole. Holomorphy forces Z(rho+h) to vanish with at least
the same multiplicity. The stipulated Z(1-h) finite and nonzero excludes a
zero at the continuum cancellation point, including a possible real-zero
chain that would collide with the numerator's pole. A finite forward chain
reaches the Euler half-plane and contradicts its absence of zeros. No
rightmost zero, simplicity, separation, shift average, or numerical zero
information is needed. The converse contour movement explicitly assumes
field RH before using reciprocal bounds, so it is not circular.

## Full Gaussian kernel and signed arithmetic

I recomputed the complete Gram kernel directly in x=log X; its Gaussian
center is (log n+log m)/2+2(c-1/2), with ratio factor exp(-log(n/m)^2/8).
The squared local Euler factor, its density (p-1)(p+2)/(p^2+p+1), and the
absolutely convergent residual series for Re s>1/2 all check. Convolution
with 1 justifies the stated error for the squared coefficient summatory
function, and partial summation supplies the logarithmic diagonal.

I independently opened the publisher's 36-page PDF of Tao's 2016 two-point
logarithmic-correlation paper and read Corollary 5, condition (8), and the
following Liouville discussion (published pages 6–7). The application to
a(p)=-1+1/p changes that prime-distance expression by at most sum_p p^-2,
uniformly in the character and permitted real twist. The fixed-offset
theorem therefore has the stated imported premise. The Gaussian smoothing
and the O_k(n^-2) kernel replacement are valid uniformly in T. They give no
rate for growing offsets, as the packet explicitly says.

For a prime power p^j in the divisibility ratio, the altered local factor
divided by the square factor at s=1 is exactly

    -(p^2-1)/(p^j(p+2)).

This calculation retains shared primes between the common scale and the
ratio. The finite set of altered Euler factors still leaves an absolutely
convergent residual Dirichlet series. Hence the fixed-ray logarithmic
asymptotic and its beta(r) constant follow. Crucially, the passage to ALL
integer-divisibility rays does not sum the ratio-dependent error constants:
the complete smoothed harmonic sum is bounded by C_c(1+log T) uniformly
in r, and r^(-1/2)exp(-log(r)^2/8) is summable. Dominated convergence after
division by log T is valid. The diagonal is counted once and the other
divisibility rays twice. The complete signed sector can be negative without
contradicting positivity of the full Gram energy.

The absolute tail bound in (13) was independently derived by u=log t and
the elementary Gaussian tail inequality; its factor 8 is correct. I read
the frozen exact interval code underlying the sign certificate. Its dyadic
rounding, atanh remainder, reduced alternating exponential enclosures,
positive reciprocal domains, signed beta accumulation and two-sided
infinite-tail enlargement have the correct directions. I did not rerun or
independently recode that finite sign certificate in this review; the root
agent performed a separate, tighter sign certification. Ordinary Gaussian
quadrature is correctly labelled as non-directed checking, not an infinite
analytic proof.

Finally the fixed coprime primitive-ratio constant beta(r)beta(s) was
recomputed. The proposed absolute double dominating series really diverges
on comparable distinct prime ratios. Thus the packet correctly refuses an
unjustified exchange of the full two-variable limit. Its positive lower
requirement on the nondivisibility complement and the remaining one-sided
critical upper bound have the right directions.

## Review boundary

This review reconstructs the written analytic and arithmetic deductions and
checks the imported theorem's applicable statement. It does not reproduce
Tao's entropy-decrement proof, prove fixed-field RH-assuming reciprocal
bounds from scratch, rerun the author's finite executable, or bound the
complete unsolved nondivisibility sector. There is no finding that either
component proves RH or an unconditional critical-power source estimate.
