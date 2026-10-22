# T-30201 — Source-bound eta–Pascal completion of the Riemann Hypothesis

Claim ID: `T-30201`  
Title: A polylogarithmic source-flow central-capacity certificate closes the triangular eta–Pascal cascade and proves RH  
Status: **FULL CONDITIONAL RH PROPOSAL — ONE FINITE SOURCE-FLOW THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #301 at `1855957a18b7ea43229cde626178920f7a538951`  
Dependencies: PR #301 analytic contraction and stopped-power layer cake; `R-30201`, `L-30201`, `L-30202`, `D-30201`; PR #272 DCD and Cycle Debt consumer  
Scope: full Riemann Hypothesis

## 1. Corrected proof boundary

The analytic half of PR #301 supplies an exact finite stopped-power resolution
and a uniform bulk contraction

\[
\boxed{\alpha\le\frac67<1.}
\tag{T-30201.1}

The corrected eta arithmetic supplies:

```text
actual paired coefficients A_k>=B_k>=0;
exact relative central/sibling replacement;
Hausdorff invariance of the residual A_k-B_k;
strict source-mass / objective amortization theta<1.
```

What it does not supply automatically is an identification of `A_k` with an
actual central-edge coefficient in the already constructed flow. `R-30201`
shows that the displayed nonnegative edge pair is not a standalone realization
of the formal paired divisor source.

The missing statement is therefore not another sign or Mellin estimate. It is
the finite source-flow certificate `D-30201`.

## 2. Source-Flow Capacity Theorem (`SFC`)

> **SFC.** There are absolute constants `A,C` such that for every endpoint
> `X`, every cascade depth, every stopped-power layer, derivative jet, common
> destination, and finite cutoff cell, one can emit a `D-30201` certificate
> satisfying
> \[
> \boxed{
> \mathfrak C_a(X)\le C\log^A(2X).
> }
> \tag{T-30201.2}
> \]
> The certificate contains the complete incoming flow, every required central
> edge, all eta pairings, every unmatched collar atom, and every residual
> lower-scale route.

A stronger zero-defect version `mathfrak C_a(X)=0` is welcome but unnecessary.

`SFC` is finite at every endpoint. It does not quantify over an unspecified
operator or Hilbert-space completion.

## 3. Exact triangular recurrence under `SFC`

Let `A_a(X)` denote the analytic coefficient-bank norm and `D_a(X)` the complete
boundary/cycle-debt norm after depth `a`, both in the fixed norms of PR #301.
The stopped-power and shifted-Dirichlet calculations give

\[
 A_{a+1}(X)
 \le
 \frac67 A_a(X)+P_M(a,X),
\tag{T-30201.3}

where `P_M` is polynomial in `a` and `log(2X)`.

The eta source-mass and switch-cost calculation gives one absolute

\[
 \theta<1
\]

(for example the corrected conservative value `theta=9/10` from PR #301).
`L-30202` proves that every common-tail residual remains in the same Hausdorff
source cone. `SFC` pays the only missing source-to-flow and collar defects.
Therefore

\[
\boxed{
 D_{a+1}(X)
 \le
 \theta D_a(X)
 +C_0 A_a(X)
 +\mathfrak C_a(X)
 +P_M(a,X).
}
\tag{T-30201.4}

Crucially there is no `D_a` term in (T-30201.3): all residual boundary sources
remain boundary typed and every capacity deficit is charged in
`mathfrak C_a`, rather than silently returned to the analytic bank.

## 4. Solving the recurrence

Put

\[
 M=
 \begin{pmatrix}
 6/7&0\\
 C_0&\theta
 \end{pmatrix}.
\]

Its spectral radius is

\[
 \rho(M)=\max\{6/7,\theta\}<1.
\]

The central residual support descends to a bounded endpoint after `O(log X)`
generations. Iterating (T-30201.3)--(T-30201.4), using `SFC`, gives

\[
\boxed{
 A_a(X)+D_a(X)=O(\log^B(2X))
}
\tag{T-30201.5}

for one absolute `B`, uniformly through the complete finite cascade.

At the final bounded endpoint every remaining flow and collar row is included
in the fixed base table.

## 5. From the cascade to Cycle Debt

The exact central-cascade saturation and PR #272 dyadic normal form convert the
complete flow into an exact eta-balanced fragmentation flow for the critical
carry target. The total weighted negative capacity is bounded by the final
boundary/capacity ledger:

\[
\boxed{
 \mathfrak N_\eta(X)
 \ll A_M(X)+D_M(X)
 =O(\log^B(2X)).
}
\tag{T-30201.6}

This implication uses the actual edge manifest of `SFC`; a source-mass estimate
alone is not substituted for capacity debt.

Hence the Cycle Debt Theorem holds:

\[
 \mathfrak N_\eta(X)=X^{o(1)}.
\]

## 6. Full RH deduction

PR #272 proves conditionally that subpower Cycle Debt gives

\[
 \sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a}
 =4\sqrt X+X^{o(1)}.
\tag{T-30201.7}

At square endpoints, the source-pinned square-screw identity gives a
subpolynomial upper envelope. The reviewed one-sided Landau argument excludes
every zero with real part greater than `1/2`; functional-equation symmetry then
gives

\[
\boxed{\mathrm{RH}.}
\tag{T-30201.8}

Thus

\[
\boxed{
 \mathrm{SFC}
 \Longrightarrow
 \text{triangular eta--Pascal contraction}
 \Longrightarrow
 \text{Cycle Debt}
 \Longrightarrow
 \mathrm{RH}.}
\]

## 7. Why this is a full-problem attack

The proposal acts directly on the complete prime-power target and its exact
balanced fragmentation flow. It does not assume WSTS, a Mertens shell estimate,
a reflected physical LMI, or a pre-existing prime-ramp bound.

The new open theorem is strictly more concrete than the former phrase
“source typing”:

```text
input:  one finite source list and one finite lower-flow list;
output: exact central-edge matches, replacements, residual routes, collars,
        and a scalar capacity-debt interval.
```

A checker can reject one missing edge or one duplicated central coefficient.

## 8. Automatic rejection conditions

Reject a claimed proof of `SFC` or RH if it:

1. treats a divisor atom as a flow edge;
2. uses `(A-B)C+B S` as a standalone source realization;
3. does not exhibit the incoming `A C` edge;
4. spends one central coefficient twice;
5. measures an unpaid central deficit only by logarithmic objective cost;
6. omits a cutoff-parity mismatch;
7. loses the Hausdorff residual destination;
8. introduces boundary-to-analytic feedback;
9. uses a finite scan as the cofinal theorem;
10. drops the first fixed-ratio Möbius mutation or square-screw normalization.

## 9. Exact status

```text
stopped-power positive resolution             IMPORTED / PROPOSED COMPLETE
bulk analytic contraction 6/7                 IMPORTED / PROPOSED COMPLETE
relative eta-Pascal replacement               PROPOSED COMPLETE EXACT
shifted residual Hausdorff invariance          PROPOSED COMPLETE
standalone paired-source flow claim            FALSE
SFC source-flow central-capacity theorem       OPEN / RH-BEARING
SFC -> triangular contraction -> Cycle Debt    PROPOSED COMPLETE
Cycle Debt -> prime ramp -> RH                 IMPORTED CONDITIONAL
Riemann Hypothesis                             UNPROVEN
```

This is a serious full conditional proposal, not an assertion that PR #301's
missing source manifest has already been constructed.