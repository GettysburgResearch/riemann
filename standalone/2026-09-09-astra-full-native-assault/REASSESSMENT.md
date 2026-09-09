# Direct RH attack: selection, attempted closure, and result

Status: research attempt, not a completed RH proof or an independent review.
Date: 2026-09-09. Main observed at f99d9e3908dde4865377c75d9ca051c1f545bf4f.

## Why stop the graph sequence here

The user asked to return to the full problem. The recent graph gap and capacity
results are useful mathematics, but they do not bound the actual critical
arithmetic residual. Further refinements of arbitrary graph reservoirs would
not discharge that missing implication. This pass does not extend those graph
results and does not treat their positivity as positivity of the Weil form.

I reread the integrated approach map and its current Xi/operator statements,
checked the active research and review metadata, and read the new #803 residual
compression proof through its principal singular-value estimate. This is a
selected cross-route reassessment, not a fresh reading of every historical
proof or of all 45 post-integration packets.

## The full routes, with their first unproved step

1. **Native arithmetic synthesis.** Construct balanced finite Dirichlet
polynomials with the exact growing Mobius prefix and subpower COMPLETE physical
error. The implication to RH uses a delayed Hardy evaluation at any hypothetical
off-line zero, not a local census. #803 has source-faithful norm certification,
classical-scale cancellation, and now near-square-root spectral compression.
The compressed affine minimum is still not bounded subpower. Compression is
not a bound on the distance to the target.

2. **Critical Euler/source domain.** #804/#811/#818 construct genuine causal
objects and explicit critical discrepancy norms. Their sufficient upper bounds
remain RH-strength. The prime-power corrections and local square-cell detail
are controlled; accumulated prime error is not. A positive safe source cannot
be moved to the critical line by an unbounded exponential reweighting.

3. **Actual Xi/Weil positivity.** The integrated operator reduction accounts for
the positive infinite sector of each finite window and gives a lower Schur
certificate. What is required is the sign on an unbounded family of complete
windows, not another positive matrix of samples. The high-derivative and
companion work in #765 keeps its raw-innerness firewall: raw Xi innerness already
contains RH, and high-order real-zero geometry is not a proved zero-defect descent.

4. **Families and algebraic structures.** The programme map retains the explicit
principal-member, conductor, metric, and global-realization hypotheses. No
source-faithful family theorem with those hypotheses discharged was identified
in this pass. This is a map-level assessment, not a new audit of #766/#769/#781.

5. **Robin and critical SHARP.** The native finite/counting reductions and m>=2
SHARP positivity are distinct from their remaining unbounded or m=1 estimates.
Nothing in the graph capacity papers closes those estimates.

The useful central question is not which criterion has the fewest symbols. It is
which construction supplies a new UPPER estimate for the unmodified arithmetic
source, without using zero-freeness to justify that estimate.

## The attempted whole-problem construction

I chose to test complete finite Euler multiplicativity rather than another
norm on arbitrary graph coefficients. Expand ALL squarefree terms of the
ordinary-prime Euler product, then impose the exact prefix, balance, derivative
normalization, and centering using only later indices. PROOF.md gives the
polynomial explicitly; there is no unknown minimizer or zero-dependent choice.

This yields an admissible vector in the original residual class at every
preserved prefix. It also fixes the complete proposed implication:

    exact growing native prefix + subpower full residual -> RH.

The candidate's entire residual norm can be evaluated asymptotically. The answer is

    E(p_Y)=exp[(4+o(1))sqrt(Y)/log(Y)].

It FAILS the proposed closing estimate. A shrinking frequency interval near
pi/log Y produces the lower bound, and a complete global zeta norm gives the
matching upper bound. None of its error was reassigned to a discarded tail.

This failure is not a criticism of #803's considerably better short-support
completions: they are different polynomials. The present family was selected to
test whether retaining the whole multiplicative product could supply the missing
cancellation. It does not. In particular its very large support means it is not
in the fixed-ratio support class of #803's compression theorem.

## Can the continuum correction repair it?

It removes the principal raw-product growth, but its difficult remainder is
already the central arithmetic object in #811/#818. At Re s>1 let

    C_Y(s)=sum_(p<=Y)p^(-s)-integral_2^Y x^(-s)/log(x) dx,
    V_Y(s)=sum_(p<=Y,k>=2)p^(-ks)/k,
    C_inf(s)=sum_p p^(-s)-integral_2^infinity x^(-s)/log(x) dx,
    V_inf(s)=sum_(p,k>=2)p^(-ks)/k.

With E1(w)=integral_w^infinity exp(-t)dt/t on the positive axis and its analytic
continuation in Re w>0, define on Re s>1

    H_Y(s)=M_Y(s) exp[-E1((s-1)log Y)].

All logarithms in the next identity are defined FIRST in this safe half-plane:

    log[zeta(s) H_Y(s)] = C_inf(s)-C_Y(s)+V_inf(s)-V_Y(s).

Indeed log zeta-log M_Y^(-1) is the omitted-prime logarithm; subtracting E1
removes exactly its first-prime continuum term. The k>=2 term is locally
absolutely convergent for Re s>1/2. Analytic continuation and critical norm
control of the remaining FIRST-prime discrepancy are precisely what have not
been proved. This identity is not used to define log zeta across unknown zeros.

Thus the repair does not provide a new full proof: it brings the attempted
product construction back to the existing unpaid global prime discrepancy.
The finite completions A_X in #811 include their own entire normalization and
causal conventions. H_Y above is only an explicit safe-half-plane comparison,
not a silently substituted source in those theorems or a finite Dirichlet polynomial.

## The unresolved proposal, without a hidden conclusion

A proof from the native residual route still needs a SPECIFIED sequence of
finite balanced polynomials with exact prefix and

    E(p_Y)<=C_epsilon Y^epsilon for every epsilon>0

on an unbounded sequence. The conditional deduction is proved in PROOF.md
Section 1, but its upper-bound premise is not supplied. A proof from the actual
Xi route still needs the full arithmetic sign, not raw-innerness as an input.

I did not find an unconditional argument for either premise in this pass.
The supplied norm theorem rejects one direct candidate; it does not establish
that the central problem is now smaller, that a solution is near, or that all
other routes are blocked. I am not submitting a gapped RH proof for reviewers
to complete. This packet preserves a concrete full-problem attempt and its
mathematical outcome, rather than counting an auxiliary theorem as closure.

## Review scope

Review the original-metric candidate, every normalization, the uniform
low-frequency product asymptotic, the noncancellation of the imposed
corrections, and the full upper norm in PROOF.md. The ordinary PNT is the only
prime-distribution input. No predecessor numerical campaign was rerun, and
no new intrinsic minimum, continuum sign, or critical entropy integral was
numerically certified.
