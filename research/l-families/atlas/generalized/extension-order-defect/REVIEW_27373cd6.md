# Independent review of finite source-cut homology

Exact freeze: `27373cd629b20c4388c4a8e6731cdb6208750145`.
Reviewed file: `FINITE_CUTOFF_HOMOLOGICAL_CLASSIFICATION.md`, Git blob
`c9c1e693e99e9524afb3888522b5acb5927cf277`.
The current LF-normalized bytes reproduce that blob. This is an independent
proof-only review by the Segre/source lane, not the note's author. I reread
the entire frozen note after the earlier draft review. No scientific job,
new test suite or numerical verification is claimed or required by it.

No mathematical blocker was found. The finite positive grading and split
characteristic-zero C3 hypotheses are explicit. The homogeneous parameter
argument is valid: parameters in A^G and P^G are regular on A and P,
tensoring over the field preserves injections, and Reynolds exactness
passes each invariant parameter quotient to C. The same argument for the
independent actions gives the parameter sequence on B'. Both localized
depths are therefore4+dim(S).

The exact predecessor quotient gives the minimal generator count
1+8[r1+r2+binom(r1+1,2)+binom(r2+1,2)]. Trivial variables disappear in
that residue quotient. For a nontrivial S, the two independent faithful
C3 actions give generic rank3, while the generator count is at least17.
Thus the localized module is not free. Auslander--Buchsbaum together with
equal depths then rules out finite projective dimension. For wholly
trivial S, C=B' instead, with rank1 and projective dimension0.

The actual finite even-cut substitution r1=r2=k_N gives
1+8k_N(k_N+3), and the pinned degree-two standard constituent ensures
k_N>=1 for N>=2. This uses the normalization/minimal-generator packet
`03b1a04df3427a09781cdf4d43a9326671a2e566` and the actual C6 source at
`d4fcbe331751e1e506cc2f38864c0c1580df92e8`; it is not a fit to sampled
Hilbert coefficients.

The limits are correct: no depth claim for the infinite non-Noetherian
algebra, no whole-base periodic resolution from a relative matrix
factorization, no universal absence of branch divisors, and no analytic
determinant-frame or convergence improvement. The abstract homological
arguments are classical; the statement is their application to the
authenticated finite source cuts and their own invariant bases.
