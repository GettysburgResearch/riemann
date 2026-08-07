# R-26701 — Scope limits of the affine boundary lift

Claim ID: `R-26701`  
Title: The affine construction isolates but does not automatically bound the RH-bearing boundary charge  
Status: **PROPOSED SCOPE CORRECTION**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26701`, `L-26702`

## 1. The construction is not itself the asymptotic theorem

`L-26701` produces a nonnegative vector for every finite endpoint, but its prime
boundary charge is
\[
C_X(a,b).
\]
Without a subpower estimate for this scalar, the objective loss
\[
C_X(a,b)\log X
\]
may be of the same size as the sharp \(4\sqrt X\) main term.

Thus
\[
\text{finite nonnegative lift}
\not\Longrightarrow
\text{RH}
\]
without ABLC.

## 2. The oversupport endpoint must avoid all old divisors

Adding a constant on the original support gives
\[
v_q(C\mathbf1_{2\le m\le X})
=
C\mathbf1_{q\mid X}.
\]
It may violate an old prime-power constraint.

The prime oversupport \(Y\in(X,2X)\) is load bearing:
\[
v_q(C\mathbf1_{2\le m\le Y})=0
\quad(q\le X).
\]

A composite \(Y\) may charge old divisors and invalidates the simple proof
ledger.

## 3. Green energy is sufficient, not necessary

The exact inequality
\[
C_X^G\le\sqrt{\mathcal G_X}
\]
does not make a Green-energy estimate automatic. A proof of
\(\mathcal G_X=X^{o(1)}\) would already resolve the prime-ramp mode.

The affine charge is weaker because it retains only the largest positive edge.
No converse from \(C_X^G\) to \(\mathcal G_X\) is claimed.

## 4. Aggregate slack does not bound the maximum edge

DCRS and Greedy Slack measure aggregate objective loss. A small aggregate debt
does not by itself control
\[
\max_m(F_X(m)-F_X(m-1))_+.
\]
A concentration of the correction on one physical edge could leave the
aggregate ledger small while making the affine charge large.

Conversely, ABLC gives the prime-ramp bound without proving either full DCRS or
GET.

## 5. Floating reconnaissance is not ABLC

The observed decrease of \(C_X^G\) through finite endpoints is discovery
evidence only. Under a false RH, the critical mode may remain invisible until
arbitrarily large scale.

No finite table, least-squares solve, or nondirected floating LP proves the
cofinal subpower statement.

## 6. The logarithmic dual ray cannot be removed

The dual of `L-26702` contains
\[
y_q=\Lambda(q)/\log X.
\]
Its objective is the normalized prime-ramp discrepancy. Therefore a proof that
bounds the boundary charge by excluding or damping this ray is circular.

A successful dipole or Green argument must control the actual logarithmic ray
together with every other monotone-additive dual witness.
