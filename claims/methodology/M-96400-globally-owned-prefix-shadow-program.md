# M-96400 — A source-correct program for a global two-row prefix shadow

Claim ID: `M-96400`  
Status: **PROPOSED RESEARCH PROGRAM / OPEN**  
Created: 2026-08-17  
Depends on: `L-96400`; `R-96400`  
RH status: **unproved**

## 1. Work with the exact state, not an invented reservoir

For \(j=2,3\), retain the actual coefficients \(a_j(n)\) from `L-96400`.
Every positive occurrence has one label \((n,j)\), every negative occurrence
has one label, and its physical knot is \(\log n\).  No integer absent from
the coefficient dictionary may be introduced as capacity.

At a finite horizon \(N\), a transport certificate may decompose
\[
 \sum_{n\le N}\frac{a_j(n)}{\sqrt n}\delta_{\log n}
\]
into positive atoms, monotone pairs, and exact log-barycentric butterflies.
Every consumed positive atom must be removed from the ledger.  Such a
certificate is a valid finite proof, but extrapolation in \(N\) is not.

## 2. Prefix-state route

The exact recurrence is
\[
 c_{N+1}(j)=c_N(j)+M_j(N)\log(1+1/N).
\]
For \(N_1>N_0\),
\[
 c_{N_1}(j)
 \ge c_{N_0}(j)
 -\sum_{N=N_0}^{N_1-1}[-M_j(N)]_+
   \log(1+1/N).
\tag{M-96400.1}
\]
Therefore the sufficient global debt theorem
\[
 \sum_{N\ge N_0}[-M_j(N)]_+\log(1+1/N)
 <c_{N_0}(j)
\tag{M-96400.2}
\]
would prove eventual positivity of row \(j\).  Equation (M-96400.2) is not
claimed here; it is a precise alternative to a cross-product shadow.

## 3. Finite \(2,3\)-scale transfer route

For a squarefree core \(d\) coprime to \(6\), all row coefficients occur at
the finite scale set listed in (L-96400.8).  A possible proof may therefore
use a common owner \(d\), then couple different cores only through an explicit
large-prime first-crossing rule.

A valid induction must prove:

1. the exact set of available positive cores in every block;
2. mass domination using that set, not all integers;
3. logarithmic first-moment domination;
4. one-use ownership across overlapping \(2,3\)-scale blocks;
5. a terminal partial-block theorem.

## 4. Invariant-cone route

The sparse updates define a deterministic four-dimensional state
\[
 V_N=(c_N(2),c_N(3),M_2(N),M_3(N)).
\]
The coefficient update depends only on
\[
 \mu(N),\ \mu(N/2),\ \mu(N/3),\ \mu(N/4)
\]
and the \(2,3\)-valuation table.  A finite-facet or quadratic invariant cone
contained in
\[
 c_2\ge0,\qquad c_3\ge0
\]
would prove `TRP23` without a transport.  Any proposed cone must be checked
against every admissible squarefree-core transition, not merely sampled
values.

## 5. Acceptance rule

A future complete packet must supply one of:

* a symbolic invariant valid for every admissible transition;
* a source-complete global transport with exact rough occupancy;
* an analytic proof of the prefix debt bound;
* another unconditional theorem implying both row signs.

Until then, `TRP23` and RH remain open.
