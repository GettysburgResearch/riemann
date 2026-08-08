# T-30701 — Corrected cycle-optimized boundary transference frontier

Claim ID: `T-30701`  
Title: The stopped boundary must be transferred coherently in the Pascal-cycle metric; ordinary atomic termination is false, while the complete outer band is already free  
Status: **CORRECTED CONDITIONAL FRONTIER — NO RH PROOF CLAIM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #307  
Dependencies: `R-30701`, `L-30701`, `L-30702`; PR #272 Cycle-Debt consumer  
Scope: exact disposition and sufficient replacement theorem

## 1. What has been closed

The complete first critical stopped boundary satisfies simultaneously:

\[
\sum_m\sqrt m|\sigma_X(m)|\gg X
\tag{T-30701.1}
\]

in the ordinary divisor-source coordinate, but

\[
\sum_q\frac{|P_X(q)|}{\sqrt q}=O(\log^2X)
\tag{T-30701.2}
\]

in the carry-column coordinate.

Moreover, the complete outer band

\[
\frac{3X}{8}\le q\le\frac{X+1}{2}
\]

has the explicit zero-debt nonnegative realization of `L-30701`.

Thus neither the size nor the sign of the outer boundary is the obstruction.
The obstruction is the lower-column leakage of a chosen band realization.

## 2. Why the atomic terminal theorem cannot be repaired by constants

The adjacent-tree map

\[
\Phi(\sigma)=\sum_m\sigma_mE_{m-1}
\]

is a valid exact right inverse for one ordinary divisor source. Its estimate

\[
\mathcal N_\omega(\Phi(\sigma))
\ll\sum_m\sqrt m|\sigma_m|
\]

is also valid at that scope.

Equation (T-30701.1) shows that using this map on the recombined boundary incurs
a fixed polynomial loss. No larger Euler order, changed constant, or finite
splitting of the same total source repairs the contradiction.

## 3. The corrected theorem

Let `mathcal B_X` denote the complete activated stopped boundary, with every
endpoint, arithmetic fiber, cutoff label, and common-destination recombination
retained. Let `mathcal F_eta(X)` be the full finite-dimensional space of
quarter-balanced flows with that exact carry load. Define

\[
\mathfrak D_{\rm bdry}(X)
=
\inf_{d\in\mathcal F_\eta(X)}
\sum_e\omega_e(-d_e)_+.
\tag{T-30701.3}
\]

The honest replacement theorem is:

> **Cycle-Optimized Boundary Transference (`COBT`).** There are absolute
> constants `A,C` such that
>
> \[
> \boxed{
> \mathfrak D_{\rm bdry}(X)
> \le C\log^A(2X)
> }
> \tag{T-30701.4}
> \]
>
> for every integer `X>=2`, with the same estimate after every exact
> support-halving boundary injection.

The optimization is over the complete Pascal-cycle affine space. It is not an
instruction to iterate the central split: one critical central row can create
polynomial weighted variation on the next band.

## 4. Fail-closed production form

A proof of `COBT` must emit, rather than ask a reviewer to construct:

```text
complete activated boundary manifest;
correct arithmetic fibers q_0;
canonical tree flow;
explicit fundamental-cycle coordinates;
final balanced signed flow;
exact carry-column replay;
all lower-band destinations;
weighted negative capacity;
dyadic/Mersenne and fixed-ratio mutations.
```

The proof is rejected if it:

- replaces the boundary by its ordinary divisor-source total variation;
- erases the arithmetic fiber;
- uses only central rows recursively;
- takes a positive part before cycle optimization;
- omits a cutoff activation condition;
- promotes finite LP feasibility to (T-30701.4).

## 5. Conditional consequence

PR #272 proves, conditionally on a subpower Cycle-Debt bound for the complete
critical carry source, that

\[
\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
=4\sqrt X+X^{o(1)}.
\]

The source-pinned square-screw/Landau transfer then excludes every zeta zero to
the right of the critical line. Therefore

\[
\boxed{
\mathrm{COBT}
\Longrightarrow
\text{Cycle Debt}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-30701.5}

This implication is conditional. `COBT` is not proved in this branch.

## 6. Exact status

```text
linear atomic-norm refutation                 PROVED
outer-band positive flow                      PROVED
polylog boundary column mass                  PROVED
central-steps-only contraction                NOT USED / known false
cycle-optimized boundary transference         OPEN / RH-BEARING
COBT -> RH                                    CONDITIONAL
Riemann Hypothesis                            UNPROVED
```

Reviewers of this branch are asked to verify the supplied proofs and exact
counterexamples. They are not being asked to fill `COBT` and the branch does not
represent it as completed.
