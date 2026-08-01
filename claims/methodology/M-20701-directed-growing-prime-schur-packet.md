# M-20701 — Directed growing-packet prime-side Schur production

Claim ID: `M-20701`  
Status: `PROPOSED PRODUCTION PROTOCOL`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01

## Objective

At growing support and packet size, certify the complete D-0001/Suzuki finite
operator without an absolute unseen-zero tail:

\[
A_{N,c}
=A_{N,c}^{\rm pole}
+A_{N,c}^{\rm arch}
+A_{N,c}^{\rm pp}.
\]

The proof object must end with the complete joint prime-side Schur pivot, not
with a frame condition number or separate residual norm.

## 1. Explicit support schedule

Use the all-integer square schedule as the first production family:

\[
\boxed{
N_M=M,
\qquad
c_M=M^2,
\qquad M=2,3,4,\ldots .
}
\]

It has

\[
L_M=\log c_M=2\log M\asymp\log N_M,
\]

so the normalized line-zero nodes

\[
\mu=L\gamma/(2\pi)
\]

remain in the polynomial-support geometry tested by `X-20704/X-20705`.

This schedule is not merely convenient. By `L-20704/T-20701`, its constant
principal coordinate is the square-screw RH statistic divided by `log M`. A
production level must therefore certify both the full joint Schur pivot and the
constant-coordinate arithmetic gate. No sparse subsequence is substituted for
the all-integer schedule without a separate sampling theorem.

The earlier calibration `N<<log c` remains a stress test but is not the preferred
growing geometry.

## 2. Directed line frame

For each certified simple-line zero ball, produce directed intervals for

\[
s_\gamma,
\qquad
x_\gamma=\mu_\gamma^2.
\]

Select rows with the rational Leja pivot of `L-20702`. A frame branch is accepted
when every pivot excludes zero. Maximality is optional; if two candidates are
not separated, branch on both.

Do not form a generic inverse. Construct:

- the first-frame kernel numerator `Q_Z`;
- the coefficient vector by residue formulas;
- the conditional second frame by evaluating `Q_Z/P_N`;
- the metric Gram directly.

## 3. Complete prime-side source

### Prime powers

Enumerate every pair

\[
q=p^k\le c.
\]

For every entry, outward-enclose:

- `log p/sqrt(q)`;
- `log q`;
- every sine and cosine phase;
- the exact diagonal or divided-difference kernel;
- pairwise accumulation.

The manifest must bind the complete duplicate-free prime-power list and its
endpoint count.

### Polar block

Evaluate the released closed rational-hyperbolic matrix in the same coefficient
basis and metric. Preserve it separately before summation.

### Archimedean block

Evaluate the digamma, trigamma, and geometric-correction formulas with Arb or a
second directed backend. Retain explicit geometric tails and precision nesting.

### Centered prime/pole replay

Before any entrywise norm is taken, independently reconstruct the exact
contraction of `L-20705`:

\[
\mathcal P_v(L)
=-{1\over L}\int_0^L
\Theta(y)K_v'\!\left(1-{y\over L}\right)dy.
\]

For the constant coordinate this must agree with

\[
\mathcal S(M)=\log M\,A_{00}(M^2)
\]

from `L-20704`. The direct prime-power matrix and the centered-discrepancy
producer are independent arithmetic assembly paths for the same quantity.

## 4. Assemble before widening

Form

\[
A=A^{\rm pole}+A^{\rm arch}+A^{\rm pp}
\]

entrywise before any operator norm is taken. Transform once to the scaled
rational-Newton/cardinal basis.

Let `J_Z` span the exact first-frame kernel and let `W_Z` be a declared
complement. Construct

\[
A_{KK}=J_Z^*AJ_Z,
\qquad
A_{KW}=J_Z^*AW_Z,
\qquad
A_{WW}=W_Z^*AW_Z.
\]

Certify

\[
A_{WW}\succ0
\]

by directed LDL and then compute

\[
\boxed{
S_{N,c}
=A_{KK}-A_{KW}A_{WW}^{-1}A_{WK}
}
\]

by a directed block LDL or fraction-free Schur replay.

This matrix already contains the complete prime-power, polar, archimedean, and
positive-sector cross cancellation. By `L-20703`, changing the first-frame
graph cannot change its exact sign.

## 5. Selected-line decomposition as an independent replay

After the complete pivot is available, choose the conditional second frame and
form its positive Gram `P_Y`. Define

\[
R_Y^{\rm corr}=S_{N,c}-P_Y.
\]

The identity

\[
P_Y+R_Y^{\rm corr}=S_{N,c}
\]

must be checked interval-wise. The selected/residual route is an independent
provenance and conditioning check; it is not the primary way to assemble the
sign.

## 6. Optional support average

A support average must be assembled from the already-centered formula
`L-20705.13`. It may be used to nominate cells or reduce directed phase
variation. It is not accepted as a pointwise level unless the certificate also
provides either:

1. a directed bound for the average negative part; or
2. a continuity radius and one strict pointwise moat selecting a support.

Positivity of the averaged matrix alone is not a support-selection theorem.
The beta square-cell average retains the RH-sensitive constant coordinate.

## 7. Required endpoints

Every retained level emits:

```text
N, c, L
prime-power manifest hash
rational-Leja row indices and pivot intervals
kernel/cardinal coefficient balls
kernel metric G_K
positive-sector LDL pivots
complete Schur matrix S_(N,c)
selected frame lower endpoint
joint corrected-residual lower endpoint
constant-coordinate square-screw replay
triangular metric inflation Lambda
assembly radius delta
final floor -Lambda*(nu-sigma^2)_+-delta
```

## 8. Independent backends

A promotion-level level requires:

1. Arb/FLINT special functions and phases;
2. an independent MPFR/MPFI or integer-series backend for the final nominated
   block;
3. a standard-library exact matrix consumer;
4. independent direct-prime and centered-discrepancy prime producers.

## 9. Fail-closed rules

Reject the level if:

- a Leja pivot or pole separation touches zero;
- the prime-power manifest is incomplete;
- a positive-sector LDL pivot touches zero;
- the Schur interval touches the requested floor;
- the square-screw principal-coordinate replay does not overlap;
- precision ladders are not nested;
- source or zero provenance hashes differ;
- the selected/residual reconstruction fails.

## 10. Cofinal acceptance

A finite level is a lower-envelope level when

\[
S_{N,c}\succeq-\epsilon G_K
\]

and the metric/assembly adapter gives the declared final floor.

The cofinal objective on the explicit square schedule is

\[
\boxed{
A_{WW,M}\succ0,
\qquad
S_{M,M^2}\succeq-\epsilon_MG_{K,M},
\qquad
\Lambda_M\epsilon_M+\delta_M\to0.
}
\]

`T-20701` proves that this objective is already RH-resolving in its constant
principal coordinate. The protocol is therefore a plan for proving the
arithmetic sign itself, not for deriving it from conditioning or a phase-blind
prime estimate.

No fixed verified-height tail enters this protocol.
