# Cycle-Debt/Q4 third strike and reconciliation with PR #483

Date: 2026-08-15  
Parent branch: `agent/91701-q4-cycle-debt-control`  
Frozen parent head: `56eeaccb2b041fdf68b6e718bad85032ecbdc66a`  
Overlapping external packet: PR #483 at `87bd7ad2127f98b6141b4c03355556f2b95f6404`  
Status: new exact finite normal forms and unconditional reductions; independent review required  
Global status: **The Riemann Hypothesis remains unproved.**

## 1. Live reconciliation

The new live work that overlaps this branch is PR #483,

```text
advance: prime-block coherence for First-Hermite heat and Q4
head: 87bd7ad2127f98b6141b4c03355556f2b95f6404
```

It explicitly freezes PR #474 at `56eeaccb...` and builds a complete Q4 prime-base row decomposition on top of `T-93010`. Its useful Q4 contributions are:

1. one exact prime-base component `R_(N,p)` containing every power and every channel occurrence of `p`;
2. the positive complete-row split
   \[
   \|R_N\|^2=D_N+2\sum_{p<r}\langle R_{N,p},R_{N,r}\rangle;
   \]
3. a safe diagonal bound `D_N<=576 N^2 log^2 N`;
4. a canonical obstruction direction and quantitative prime-carrier lower bounds.

This is a genuine strengthening of the kernel-wise same-prime extraction in `L-93013`: it keeps the complete row positive before any Fourier, max-kernel, or Goldbach expansion. It does not touch Cycle Debt.

The present packet therefore does not duplicate PR #483. It freezes and extends it in two directions:

```text
Q4:
    improve the complete diagonal by one logarithm;
    remove every square-root-minor-arc cross mode;

Cycle Debt:
    recenter the full dual capacity interval;
    derive a policy-free factor-one-half dyadic recurrence;
    retain odd leakage and the commutator in one joint LP.
```

## 2. Cycle Debt: centered capacity norm

For a source `r`, let

\[
K_\omega(r)=\langle r,\mathcal G\rangle,
\qquad
\delta_\mathcal G(e)=\omega_e.
\]

The original Cycle-Debt dual is

\[
\mathfrak N_\omega(r)
=
\max\{-\langle r,F\rangle:0\le\delta F\le\omega\}.
\]

Writing

\[
H=F-\mathcal G/2
\]

makes the constraint symmetric:

\[
|\delta H(e)|\le\omega_e/2.
\]

The exact centered norm is

\[
\boxed{
\mathfrak N_\omega(r)+K_\omega(r)/2
=
\sup_{|\delta H|\le\omega/2}|\langle r,H\rangle|.
}
\]

Equivalently, the minimum weighted absolute variation is twice this support norm. In normalized size-biased coordinates the constraint is

\[
|h(n)-P_eh|\le c_e/2.
\]

Thus the two-channel primal of `L-93010` has one symmetric martingale-difference dual ball. This removes the artificial lower/upper asymmetry without weakening or strengthing the LP.
For the critical source,

\[
K_X=\sum_{q=2}^X\frac{\log(X/q)}q=O(\log^2X),
\]

so a polylogarithmic centered norm is already sufficient.

## 3. Cycle Debt: one joint dyadic parity defect

For `X=2Y`, the exact dyadic source identity of `L-27207` is

\[
r_X
=2^{-1/2}\mathcal D_2r_Y
+w_X(2)\partial T_2
+\sum_{a<Y}r_X(2a+1)\partial E_{2a}.
\]

For a higher-scale centered potential `H`, define the gauge-corrected even trace

\[
(\mathcal R_2H)(m)
=\sqrt2[H(2m)-mH(2)].
\]

The size-conservation gauge is essential for normalization and has no effect on the lower source pairing. Exactly,

\[
\langle r_X,H\rangle
=
\frac12\langle r_Y,\mathcal R_2H\rangle
+w_X(2)H(2)
+\sum_{a<Y}r_X(2a+1)[H(2a+1)-H(2a)].
\]

The bottom term is bounded by

\[
|w_X(2)H(2)|\le\frac14\log Y.
\]

The even trace differs from a lower centered dual only by the exact odd-column capacity leakage. The packet therefore defines one joint centered parity functional `P_(2Y)` in which:

- the inherited even-trace overrun;
- the signed adjacent odd commutator;

remain inside the same supremum. No pair-first cancellation is discarded.

The resulting recurrence is

\[
\boxed{
\mathfrak S_{2Y}
\le
\frac12\mathfrak S_Y
+\frac14\log Y
+\mathfrak P_{2Y}.
}
\]

A polylogarithmic bound for `P_(2Y)` gives polylogarithmic Cycle Debt and RH through the existing consumer. This new criterion is called **Centered Dyadic Parity (`CDP`)**. CDP is open.

This is the dual, policy-free counterpart of the primal paired excess in `L-27207`. It is especially suitable for fail-closed finite certification because it is a support-function comparison between two finite capacity polytopes.

## 4. Q4: improve the complete prime diagonal

For the PR #483 prime block, let

\[
A_{p,N}=\sum_{m\le N}|c_{\circ,p}(m)|.
\]

Rather than bound every `A_(p,N)` by `O(log N)` and then multiply by `pi(N)`, sum the complete tower masses first:

\[
\sum_pA_{p,N}
\le
\psi(N)+4\psi(N/4)+3\log N
\ll N.
\]

Also

\[
\max_pA_{p,N}\le8\log(2N).
\]

Hence

\[
\sum_pA_{p,N}^2
\le
(\max_pA_{p,N})\sum_pA_{p,N}
\ll N\log N.
\]

Since each row coordinate uses three prefixes,

\[
\boxed{
D_N
\le720N^2\log(2N).
}
\]

The normalized same-prime diagonal is therefore `O(log N)`. The canonical coherence consequence improves to

\[
\#\{\text{positively aligned prime bases}\}
\ge
\frac{\mathscr P_\circ(N)}{720\log(2N)}.
\]

This improves PR #483's denominator from `log^2 N` to `log N`.

## 5. Q4: remove the entire distinct-prime minor arc

For each prime block define its exact mean `M_(p,N)` and sine coordinate

\[
S_{p,N}(a)
=\sum_{m<N}c_{\circ,p}(m)
 \sin(2\pi am/N).
\]

The complete distinct-prime Gram is

\[
\frac2N\sum_{p<r}M_{p,N}M_{r,N}
+
\frac2{N^3}\sum_{a=1}^{N-1}
\frac{\sum_{p<r}S_{p,N}(a)S_{r,N}(a)}
     {\sin^2(\pi a/N)}.
\]

The elementary coefficient energy is

\[
\sum_{m<N}|c_\circ(m)|^2\le96N\log(2N).
\]

For

\[
d_N(a)=\min(a,N-a),
\qquad
K_N=\lceil\sqrt N\rceil,
\]

Parseval and the sine lower bound give

\[
\frac1{N^3}
\sum_{d_N(a)\ge K_N}
\frac{|S_N(a)|^2}{\sin^2(\pi a/N)}
\le24\log(2N).
\]

The corresponding prime-block diagonal on those modes is at most

\[
D_N/N^2\le720\log(2N).
\]

Using

\[
2\sum_{p<r}S_pS_r
=(\sum_pS_p)^2-\sum_pS_p^2
\]

therefore yields the absolute cross bound

\[
\boxed{
|\mathfrak C_{\ne p}^{\rm min}(N)|
\le744\log(2N).
}
\]

Let `C_(ne p)^maj` be the mean plus only the modes `d_N(a)<sqrt(N)`. Then

\[
\boxed{
|\mathscr P_\circ(N)-\mathfrak C_{\ne p}^{\rm maj}(N)|
\le1464\log(2N).
}
\]

Conditional on `T-93010`, RH is now equivalent to a polylogarithmic estimate for:

```text
one mean coordinate
+
fewer than 2 sqrt(N)+O(1) low additive modes
+
only correlations between different prime bases.
```

Every nonzero surviving mode has reduced additive modulus greater than `sqrt(N)`. The exact character expansion of `L-90414` therefore turns the same gate into a weighted covariance of large-additive-modulus prime sums. No claim is made that every imprimitive term has large primitive conductor.

## 6. Exact replay

### X-93014

```text
PASS_X_93014_CYCLE_DEBT_CENTERED_PARITY

48      centered/asymmetric fixture checks
48      exact dual-vertex optimum checks
48      weighted-variation checks
192     Q(sqrt(2)) dyadic pairings
192     gauge-normalized even traces
44,208  formal doubled-carry checks
384     hostile mutations detected
```

### X-93015

```text
PASS_X_93015_Q4_PRIME_MAJOR_ARC_LOCALIZATION

4,380  source coefficient checks
4,380  row reconstruction checks
80     complete Gram checks
2,484  tower diagonal checks
2,239  prime-power support checks
2,366  same-prime unequal-power terms retained
1,920  orthogonal-projection checks
144    hostile mutations detected
```

The first checker uses exact rational arithmetic, `Q(sqrt(2))`, and formal radical support. The second uses exact rational arithmetic with independent formal `log(p)` labels. Neither checker proves the remaining cofinal estimate.

## 7. Source-arithmetic correction to L-93012

During this continuation, the proof-facing certificate language in `L-93012` was re-audited. Its statement that the “critical source is rational” is false: the actual source contains square roots and logarithms inherited from

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

`R-93016` corrects this scope. The action matrix is rational, rank sparsity survives, and a basic solution is rational when the supplied source is rational. For the actual critical source, a certificate must authenticate source equality symbolically or with separately directed primitive intervals. The capacity-cost interval theorem itself survives.

## 8. Exact frontier after reconciliation

```text
Cycle Debt:
    centered dyadic parity functional P_(2Y) = polylog
    with exact source and directed capacity provenance.

Q4:
    mean + square-root-major-arc distinct-prime correlation = polylog.

Riemann Hypothesis:
    unproved.
```

The two fronts remain structurally independent. The Cycle-Debt gate is a finite adaptive transport/support-function theorem. The Q4 gate is a deterministic resonance theorem between different Euler factors in fewer than `O(sqrt N)` low additive modes.
