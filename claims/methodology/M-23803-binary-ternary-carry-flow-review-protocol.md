# M-23803 — Adversarial review protocol for the binary–ternary carry-flow proposal

Claim ID: `M-23803`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
PR: #247

## Frozen review order

1. `L-23808-atomized-carry-entropy-and-pascal-cocycle.md`
2. `L-23810-carry-flow-divergence-and-mobius-inversion.md`
3. `X-23802-binary-ternary-flow/verify.py`
4. `L-23811-explicit-binary-ternary-signed-carry-flow.md`
5. `T-23803-binary-ternary-carry-flow-rh-proposal.md`
6. `2026-08-08-explicit-fragmentation-producer.md`
7. inherited square-screw and upper-envelope Landau transfers

## A. Divergence convention

Expand one split `n=j+(n-j)` directly.  The parent contributes `+d`, both
children contribute `-d`, and a central child is counted twice.  Verify

\[
L_q(d)=\sum_mr_m\lfloor m/q\rfloor
\]

before using Möbius inversion.  A missing child multiplicity invalidates every
later identity.

## B. Target convention at q=1

The prime-ramp target is prescribed only for `q>=2`.  The auxiliary row must be
set to

\[
w(1)=0
\]

so that size conservation is encoded.  Do not substitute the analytic formula
`q^-1/2 log(X/q)` at `q=1`.

## C. Möbius inversion

Reconstruct

\[
u_m=\sum_{k\le X/m}\mu(k)w(mk),
\qquad r_m=u_m-u_{m+1},
\]

and prove that its floor transform is exactly `w`.  This is finite inversion
over multiples, not an asymptotic Möbius estimate.

## D. Binary–ternary recurrence

For every parent, retain the two splits with coefficient `1/2` each and count
repeated children separately.  Descend from `X` to `2`, verify the node-one
closure, and compare direct carry loads against the target column by column.

The exact Fraction replay is a mutation guard only.  It does not prove the
prime-ramp rate.

## E. Prime and all-integer ledgers

Independently reconstruct

\[
\mathcal P(X)=\sum_nA_X(n)\ell_n,
\qquad
\sum_qw_X(q)=\sum_nA_X(n)c_n.
\]

The first identity must use prime-power valuations with `Lambda`; the second
uses all integer columns with coefficient one.  Confusing these two ledgers
invalidates the comparison.

## F. Sole rate theorem

Classify separately:

```text
BTF strong form:
    sum |A_X(n)| sqrt(n)=X^o(1)

BTF pairing form:
    |sum A_X(n)(ell_n-c_n)|=X^o(1)
```

The pairing form is sufficient and strictly weaker.  A proof must be cofinal
and source-specific.  Finite sign tables, finite LP saturation, or one fixed
range of positive coefficients are not evidence of the required rate.

## G. Forbidden shortcuts

Reject any proof that:

- replaces `mu` by `|mu|` before binary–ternary recombination;
- estimates every quotient layer independently and sums total variation;
- infers cofinal positivity from a finite stationary-split scan;
- imports GCF, FGCM, BCT, or BTP without proving the specialized implication;
- drops the first fixed-ratio Mertens mutation;
- reverses the prime-ramp/screw-function inequality;
- treats a finite computation as an all-`X` theorem.

## H. Completion check

Only after BTF passes should the reviewer inspect:

1. `sum_q w_X(q)=4 sqrt(X)+O(log X)`;
2. the square-cutoff normalization `X=N^2`;
3. propagation between square samples;
4. the upper-envelope orientation of Landau's theorem;
5. functional-equation symmetry.

## Required status boundary

```text
atomized carry identities              verify independently
Möbius divergence and recurrence       verify independently
exact signed saturation                verify independently
BTF rate                               accept / reject separately
conditional RH deduction               retain if the transfer passes
accepted proof of RH                    only if BTF is proved cofinally
```
