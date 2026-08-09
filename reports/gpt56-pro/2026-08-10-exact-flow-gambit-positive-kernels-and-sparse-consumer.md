# Exact Flow Gambit continuation: positive packet kernels, genuine nonnegative-flow cuts, and the sparse producer target

Date: 2026-08-10  
Agent: `gpt56-pro`  
Proposed branch: `research/gpt56-pro/90101-nonnegative-flow-sparse-kernel`  
Primary base: Fable consolidation PR #351  
Status: two proposed-complete exact results, one finite route-selection observation; **RH remains unproved**

## Executive result

The pass found two exact advances and one important narrowing of the open target.

First, the coefficient positivity left conjectural in Fable's `T-90007` is proved by one finite Abel summation.  Every coefficient in

\[
 \Sigma_{X,n}(p)=\sum_k\mu(k)c_p(k)
\]

is the mass of an explicit positive Stieltjes/first-entrance packet.  The same statement holds for every nonnegative trace of the exit vector, in particular the at-most-three-nontrivial-site producer trace of `L-32301`.

Second, the “flow” LP in `T-90006` is audited at its exact sign scope.  Its internal throughput is free in `R^F`, so its harmonic-pixel dual is correct for **signed transshipment**.  Imposing the physically relevant constraint `y>=0` produces a different exact dual: all nonnegative superharmonic potentials.  That cone has a complete atomic decomposition into exit pixels plus internal Green charges.  Threshold cuts return, and feasibility is equivalent to simultaneous nonnegativity of the exit vector and all internal producer occupations.

Third, the exact consumer is materially less rigid than coordinatewise GFEP.  Under the stored adversarial source at `(X,n)=(2000,20)`, the bottom exit is `-0.4712` while the sparse producer remains `+0.04593`.  The corresponding tail LP also tolerates substantially more deep uncertainty.  A second witness at `(3000,25)` makes the sparse producer negative, so this is a reopened route rather than a proof.

## 1. Audit of Fable's exact-flow theorem

### 1.1 What survives unchanged

`T-90006` correctly proves that, when the far-node variable `y` is unrestricted in sign, the dual constraint is

\[
 Lh=0.
\]

The resulting cone is generated exactly by the harmonic exit pixels `H_p`, and the signed LP value is `min_p Sigma(p)`.  Nothing in the present pass disputes that theorem.

### 1.2 What the word “flow” hides

For a genuine throughput, `y` must be nonnegative.  With

\[
 s_F=S_F+Q_{FF}^{\mathsf T}y-y,
 \qquad
 s_W=S_W+Q_{FW}^{\mathsf T}y,
\]

the true feasibility problem is

\[
 y,s_F,s_W\ge0.
\]

Let `g` be the canonical descending Green occupation and `Sigma` its boundary delivery.  Since

\[
 A=I-Q_{FF}^{\mathsf T}
\]

has a finite nonnegative inverse, every feasible `y` obeys

\[
 g-y=A^{-1}s_F\ge0,
\]

and hence `g>=0` and `Sigma>=0`.  Conversely, `y=g` is feasible whenever those two vectors are nonnegative.  Thus

\[
 \boxed{NF_n\text{ feasible}\iff g\ge0\text{ and }\Sigma\ge0.}
\]

The dual cut cone is

\[
 h\ge0,\qquad Lh\ge0,
\]

not the harmonic face `Lh=0`.  Every such `h` is uniquely

\[
 h=\sum_p h(p)H_p+\sum_r(Lh)(r)K_r,
\]

where `K_r` is the internal Green potential with unit Laplacian charge at `r`.  The exact source pairing is

\[
 \langle S,h\rangle
 =\sum_p h(p)\Sigma(p)+\sum_r(Lh)(r)g(r).
\]

This is the genuine nonnegative-throughput max-flow/min-cut theorem.

### 1.3 Threshold cuts

For `h_k=1_[k,X]`,

\[
 Lh_k(m)=\mathbb P_m(Z_1<k)\ge0.
\]

Therefore thresholds are valid true-flow cuts and decompose into exit pixels plus internal Green charges.  Fable's statement that threshold indicators are not harmonic remains correct; the stronger informal reading that no threshold cut exists for a nonnegative flow is scope-inaccurate.

## 2. The positive-kernel conjecture is a theorem

Fable defines

\[
 c_p(k)=\sum_m [G_p(m)-G_p(m-1)]w_X(mk),
 \qquad G_p(m)=mE_n(m,p)\ge0.
\]

For `M=floor(X/k)`, finite Abel summation gives

\[
 c_p(k)=\sum_{m=n}^{M}G_p(m)
 [w_X(mk)-w_X((m+1)k)].
\]

The critical weight is decreasing, because

\[
 -w_X'(u)=u^{-3/2}\left(1+\frac12\log\frac Xu\right)>0.
\]

Hence every summand is nonnegative.  More precisely,

\[
 c_p(k)=\int_{kn}^{X}
 G_p(\lfloor u/k\rfloor)
 u^{-3/2}\left(1+\frac12\log\frac Xu\right)du.
\]

This gives the combinatorial object requested by the gambit: a positive path/Stieltjes packet for each squarefree layer `k`.  What remains is not the sign of an individual packet, but an exact multiplicative coupling of the alternating packet layers.

## 3. The positive kernel survives sparse recombination

For any nonnegative boundary trace `a(p)`, let

\[
 G_a=\sum_pa(p)G_p.
\]

The same Abel formula proves `c_a(k)>=0`.  Taking `a=h_n`, the hitting trace from `L-32301`, gives

\[
 G_a(m)=mh_n(m)
\]

and

\[
 nA_X(n)=\sum_k\mu(k)c_{\rm prod}(k),
 \qquad c_{\rm prod}(k)\ge0.
\]

This is the exact positive packet form for the actual producer induction step.  It preserves the bottom coordinate, the one/two ternary contacts, and the top-site recursion before taking any sign split.

## 4. The primitive-count lure and its exact renaming

The strongest numerical pattern in the new coordinates was squarefree finite-difference positivity of `k -> c_p(k)`.  The embedded skeptic identifies the full-depth version exactly.

Because

\[
 w_X(mk)=k^{-1/2}w_{X/k}(m),
\]

one has

\[
 c_p^{X,n}(k)=k^{-1/2}c_p^{X/k,n}(1)
\]

and

\[
 \boxed{
 \sum_j\mu(j)c_p^{X,n}(kj)
 =k^{-1/2}\Sigma_{X/k,n}(p).
 }
\]

Thus the would-be primitive weight at scale `k` is precisely the same GFEP coordinate at the smaller endpoint `X/k`.  A primitive-object proof would be a genuine strong-induction proof, not an automatic consequence of positive packets.  Defining the primitive measure by this Möbius transform is circular.

This exact dictionary also explains why fixed cumulative Abel positivity is not the solution: post-Fable PR #352 gives an exact fourfold cumulative counterexample at `(X,n,p)=(1000,21,21)`, while the final scalar remains positive.

## 5. Sparse-vs-pixel adversarial calibration

The finite replay uses the same deep-sign class as `T-90007`.

| `(X,n)` | minimum exit | sparse producer |
|---|---:|---:|
| `(2000,20)` | `-0.4712115867` | `+0.0459306074` |
| `(3000,25)` | `-0.8138646554` | `-0.5633436528` |

The first row proves that the stored per-pixel adversary does not automatically refute the true consumer.  The second proves that sparsity alone is insufficient.

The tail-budget LP gives the same conclusion quantitatively:

| `(X,n)` | bottom `A*` | sparse `A*` |
|---|---:|---:|
| `(2000,20)` | 2.48155 | free deep signs still positive |
| `(3000,25)` | 2.18881 | 3.57368 |
| `(3000,15)` | 1.38956 | 1.84319 |
| `(4000,20)` | 1.46051 | 2.12229 |
| `(4000,15)` | 1.32621 | 1.66255 |

The advantage is real but decays with depth in this finite sample.  No cofinal estimate is inferred.

## 6. Revised frontier

The exact-flow gambit is not dead, but its correct target is narrower than the final wording on PR #351.

The viable structural statement is:

> Build a positive primitive packet measure for the sparse producer trace, using the true multiplicative relations of `mu`, with measurable packet splitting and complete ternary/top-site recombination.

A claimed closure must not:

- use a free sign vector in place of multiplicativity;
- infer primitive positivity from `c(k)>=0` alone;
- use the circular smaller-endpoint identity as the construction;
- revert to a one-to-one coarse-chain injection killed by `L-90004`;
- prove every exit pixel when only the sparse trace is consumed;
- use a fixed finite Abel order, refuted by `R-90004`.

The strongest immediate research subproblem is to find an explicit dilation-compatible coupling for the continuous packets in `L-90101.9`.  Unlike the coarse chain algebra, this model permits mass splitting, so Fable's cardinality pigeonholes do not by themselves exclude it.  The coupling must still satisfy nontrivial cut conditions; its existence is not asserted.

## 7. Verification

Run:

```bash
python experiments/X-90101-nonnegative-flow-sparse-kernel/verify.py
```

Retained headline:

```text
PASS_X_90101_NONNEGATIVE_FLOW_SPARSE_KERNEL
```

The replay contains:

- 293 direct-vs-Abel kernel identities at 70 decimal digits;
- 2,533 individually nonnegative Abel terms;
- 12 scale and primitive-scaling identities;
- three exact rational Green/cut pairings;
- 31 exact threshold decompositions;
- two independent sparse-consumer identities;
- five tail-budget LP comparisons.

## 8. Honest status

```text
T-90007 coefficient positivity conjecture          PROVED EXACTLY
positive path/Stieltjes packet representation       PROVED EXACTLY
arbitrary nonnegative trace / sparse kernel          PROVED EXACTLY
signed-vs-nonnegative flow scope                     RESOLVED EXACTLY
true superharmonic cut cone                          CLASSIFIED EXACTLY
threshold cuts in genuine flow                       RESTORED EXACTLY
primitive-measure full transform                     IDENTIFIED AS SCALED GFEP
GFEP adversary vs sparse consumer                    SEPARATED AT ONE FINITE CASE
uniform sparse tail control                          OPEN / RH-BEARING
positive primitive packet coupling                   OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
