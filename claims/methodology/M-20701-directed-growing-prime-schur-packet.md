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

## 1. Support schedule

Use a polynomial support schedule as the first production family:

\[
L_j=\log c_j\asymp\log N_j.
\]

This keeps the normalized line-zero nodes

\[
\mu=L\gamma/(2\pi)
\]

on the same scale as the Fourier lattice. The earlier calibration
\(N\ll\log c\) deliberately remains as a stress test but is not the preferred
growing geometry.

The schedule is a nomination. Every retained level is decided by directed
arithmetic.

## 2. Directed line frame

For each certified simple-line zero ball, produce directed intervals for

\[
s_\gamma,\qquad x_\gamma=\mu_\gamma^2.
\]

Select rows with the rational Leja pivot of `L-20702`. A frame branch is accepted
when every pivot excludes zero. Maximality is optional; if two candidates are
not separated, branch on both.

Do not form a generic inverse. Construct:

- the first-frame kernel numerator \(Q_Z\);
- the coefficient vector by residue formulas;
- the conditional second frame by evaluating \(Q_Z/P_N\);
- the metric Gram directly.

## 3. Complete prime-side source

### Prime powers

Enumerate every pair

\[
q=p^k\le c.
\]

For every entry, outward-enclose:

- \(\log p/\sqrt q\);
- \(\log q\);
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

## 4. Assemble before widening

Form

\[
A=A^{\rm pole}+A^{\rm arch}+A^{\rm pp}
\]

entrywise before any operator norm is taken. Transform once to the scaled
rational-Newton/cardinal basis.

Let \(J_Z\) span the exact first-frame kernel and let \(W_Z\) be a declared
complement. Construct

\[
A_{KK}=J_Z^*AJ_Z,
\qquad
A_{KW}=J_Z^*AW_Z,
\qquad
A_{WW}=W_Z^*AW_Z.
\]

Certify \(A_{WW}\succ0\) by directed LDL and then compute

\[
\boxed{
S_{N,c}
=A_{KK}-A_{KW}A_{WW}^{-1}A_{WK}
}
\]

by a directed block LDL or fraction-free Schur replay.

This matrix already contains the complete prime-power, polar, archimedean, and
positive-sector cross cancellation.

## 5. Selected-line decomposition as an independent replay

After the complete pivot is available, choose the conditional second frame and
form its positive Gram \(P_Y\). Define

\[
R_{Y}^{\rm corr}=S_{N,c}-P_Y.
\]

The identity

\[
P_Y+R_Y^{\rm corr}=S_{N,c}
\]

must be checked interval-wise. The selected/residual route is an independent
provenance and conditioning check; it is not the primary way to assemble the
sign.

## 6. Required endpoints

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
triangular metric inflation Lambda
assembly radius delta
final floor -Lambda*(nu-sigma^2)_+-delta
```

## 7. Independent backends

A promotion-level level requires:

1. Arb/FLINT special functions and phases;
2. an independent MPFR/MPFI or integer-series backend for the final nominated
   block;
3. a standard-library exact matrix consumer;
4. independent direct-prime and prefix-moment prime producers when feasible.

## 8. Fail-closed rules

Reject the level if:

- a Leja pivot or pole separation touches zero;
- the prime-power manifest is incomplete;
- a positive-sector LDL pivot touches zero;
- the Schur interval touches the requested floor;
- precision ladders are not nested;
- source or zero provenance hashes differ;
- the selected/residual reconstruction fails.

## 9. Cofinal acceptance

A finite level is a lower-envelope level when

\[
S_{N,c}\succeq-\epsilon G_K
\]

and the metric/assembly adapter gives the declared final floor.

The cofinal objective is an explicit unbounded list of immutable levels with

\[
\Lambda_j\epsilon_j+\delta_j\to0.
\]

No fixed verified-height tail enters this protocol.
