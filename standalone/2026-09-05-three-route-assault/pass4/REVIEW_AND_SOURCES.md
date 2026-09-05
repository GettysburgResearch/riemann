# Sources, proof audit, and execution boundary

## Source pins

- Continuing PR #793, parent bfb66e07f7e38306dbcb916911332a591efce917. Read the source-Hankel, reciprocal-Laguerre, and fixed-Hardy interfaces in pass3, together with the pass2 safe-source normalization.
- PR #792, 39c13367f4b3956631ea1e00fac6c3005fc32057, standalone/2026-09-05-bernstein-chebyshev-growth/cross-route-hardy-laguerre/BRIDGE.md. The arithmetic expansion and trace-class decompositions in Sections 1-2 are the operator input; safe matrix and trace identities were also examined. Its all-section positivity is explicitly open. No claim of independent acceptance of every statement in that branch is made.
- The latest #790 heat-Hankel programme was checked at PR-description level (head bce97be9727dea9968db7517738edc966d2cc86b); none of its newly stated theorems is a dependency here.

Local parent files used by the executable certificate, authenticated before loading:

    pass2/source_certificate.py
      SHA256 128df4f27cc62683a58ef74c1f374910db13b507208e00535df3e1c9a9b3c6e5
      Git blob 144875db117fced3a506fb84331d2168d05b5f06
    pass3/source_moments.py
      SHA256 1d7b36a0bfc3abca254912aaa5756fe24b7b3180aea2a1fc9edf6c51b830ce4d
      Git blob 125ba6596ff0c3869eccbed2e77955352d3a6aaf

The attached historical snapshots were unpacked locally and their exact blob identities checked against the published objects. No predecessor source was modified.

## Primary external references

1. NIST DLMF, 18.14.8, Laguerre bound at alpha=0:
   https://dlmf.nist.gov/18.14.E8
2. NIST DLMF, 18.12.13, Laguerre generating function:
   https://dlmf.nist.gov/18.12.E13
3. D. R. Johnston and A. Yang, Some explicit estimates for the error term in the prime number theorem, arXiv:2204.01980. The abstract gives an unconditional psi error bound stronger than the qualitative rate used here:
   https://arxiv.org/abs/2204.01980
   No RH-conditional error theorem is imported. No newest-bound claim or numerical use of the paper's constants is made.
4. M. Suzuki, Aspects of the screw function corresponding to the Riemann zeta-function, Journal of the London Mathematical Society (2023), DOI 10.1112/jlms.12785:
   https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12785
   Context for the established Weil/screw-function positivity framework only. The present arithmetic kernel is normalized through the pinned repository source, not copied from a different Fourier convention.

Cauchy's estimates, the compact self-adjoint min-max principle, the characteristic-function continuity theorem, compound-Poisson generating functions and elementary Stieltjes integration are standard tools. No external novelty/priority claim is made for those tools, the general RH criteria, or this packet before specialist comparison.

## New versus inherited

New deductions in this packet are the sparse all-cutoff moment obstruction with an explicit degree bound; the uniform degree-independent PNT tail comparison and compound-Poisson/Gaussian transition; the balanced all-degree error; the infinite negative index of every finite literal prime cutoff; and the quantified omitted-tail failure for subexponential reciprocal-source cutoffs. The all-n positivity of the particular full-source sparse family is a simple source-dominance corollary, not progress at the critical Hankel sign.

Inherited: the fixed actual source, positive theta coefficients, safe special values of xi, moment sufficiency theorem, reciprocal-zeta generating interface, and arithmetic Hardy kernel. The preceding minimal-rank and finite-source certificates retain their original scope; they are not being strengthened.

## Binding proof checks

- The artificial residue is at u=-2 (s=1), not at the square-root branch point u=-9/4. Cancellation in the actual completed xi must not be lost.
- Moment index j means p_(j+1). The normalized tail is 2^(j+1)(m_j(X)-m_j), not 2^j times that quantity.
- The continuous tail law is a cumulative distribution. The boundary term X k_j(X), bounded by 2, is also necessary in the PNT transfer; dropping it changes the constant.
- The compound Poisson parameter is log X; jump second moment is 10, not jump variance 6. Thus the Gaussian variance scale is 10log X.
- PT12 concerns the explicitly stated sparse family. It does not locate the first indefinite leading matrix or exclude earlier negative tests.
- The quadratic margin -1/12 is not a normalized eigenvalue bound: the sparse vector has squared norm 1+4^n.
- Full-source sparse-square positivity is not full Hankel PSD.
- The balanced germ has no artificial s=1 pole, but this does not make it positive. The actual X=2 balanced trace is certified negative.
- The kernel with FINITELY MANY PRIME ATOMS is not an exact finite-dimensional compression of the full kernel. The infinite-index statement concerns the former only.
- Infinite negative index of convergent approximants does not determine the sign of their trace-norm limit.
- The full omitted-prime cancellation is only at exp(x/2); it does not pay any exponent delta between zero and one half.
- The positive squarefree countercontrol is not actual reciprocal zeta. It proves failure of an approximation procedure, not RH's falsity.

## Actual-source interval certificate

The full m_0 and first two sparse squares are reconstructed using the source-only Euler--Maclaurin/Cauchy certificate from pass3. The finite cutoff X=2 witness can also be written directly in gamma and prime constants. Put

    G0=-(gamma_E+log pi)/2-log(2)/4,
    G1=pi^2/24+log(2)^2/4,
    G2=-zeta(3)/4-log(2)^3/4.

Then q_X=1/(u+2)+G(s(u))/d(u) gives exactly

    ell_2((1-2t)^2)=11G0/81+8G1/27+2G2/27< -1/100,
    mbal_0(2)=1/2+G0/3-1/6<0,
    D_2=(gamma_E+log pi+log(2)/2)/3>0.

Rational outward enclosures, not floating-point signs, certify these inequalities. The parent analytic remainder proofs are dependencies and still require independent mathematical review.

## Executed checks and their limits

331 distinct checks are counted once, even though they were executed in two Python modes. Eight are actual-source interval signs. Other checks are bounded formal-series identities, exact coefficient moments, finite synthetic rank-two elimination and positive residual minors, the conservative cutoff threshold, and Laguerre/residue algebra. None machine-proves the all-order analytic arguments.

Eight unit/rejection tests were run in each mode. Four corrupted saved-result inputs (a changed source enclosure, a Boolean alias, a float alias, and a duplicate JSON key) were also refused by actual checker subprocesses in each mode. REPLAY_LOG.json records those executions. This corruption count is not added to the 331 mathematical controls.

Normal and optimized full-result outputs are byte-identical. The complete result is reconstructed and type-strictly compared. SHA256SUMS covers every other file in this folder; --manifest also checks coverage. The broader old 447/640/622-control suites were not rerun; only their locked source routines needed for the new certificate were executed.

Not performed: independent mathematical referee review, formalization/Lean, a new zero census, numerical PNT verification, a broad prime search, or remote CI. The completion attempt did not obtain the RH-bearing positive sign, and no publication marker is evidence that it did.
