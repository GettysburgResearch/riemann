# T-27801 — Third-Abel collar producer proposal for RH

Claim ID: `T-27801`  
Title: A source-specific third-Abel kernel/collar theorem would prove the binary–ternary producer positive and close the sharp carry route to RH  
Status: **FULL CONDITIONAL RH PROPOSAL — TACP OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Parent: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Dependencies: `L-27801`, `R-27801`, PR #277 `L-23814/T-23804`, inherited square-screw/Landau consumer

## 1. Why this is the selected research route

The scope audit left several stronger source-specific statements open. The binary–ternary carry producer is unusually concrete:

```text
one exact critical target w_X(q)=q^-1/2 log(X/q)
-> one exact Mobius divergence
-> one deterministic O(X) descending producer A_X(n)
-> producer positivity alone
-> O(log^2 X) weighted variation
-> sharp prime ramp
-> square-screw/Landau
-> RH.
```

PR #277 `L-23814` removes every independent asymptotic-rate obligation once `A_X>=0` is known. The full problem is therefore reduced to a sign theorem for one explicit finite transform.

`R-27801` proves that this sign cannot come from generic positivity or even from a twofold Abel integration. The new route is deliberately source-specific.

## 2. Third-Abel Collar Positivity (`TACP`)

For each endpoint `X`, let `K_X(n,q)` be the exact producer kernel and

\[
S_X(n,Q)=\sum_{q=2}^{Q}\binom{Q-q+2}{2}K_X(n,q)
\]

its third cumulative kernel.

Let

\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad w_X(q)=0\quad(q>X),
\]

and

\[
d_X(Q)=w_X(Q)-3w_X(Q+1)+3w_X(Q+2)-w_X(Q+3).
\]

The **Third-Abel Collar Positivity theorem** asks for an explicit integer collar width `L_X` and a proof that, for every sufficiently large `X` and every node `2<=n<=X`,

### TACP-I — interior kernel

\[
\boxed{
S_X(n,Q)\ge0
\quad(2\le Q\le X-L_X-1).
}
\tag{T-27801.1}
\]

### TACP-B — exact boundary collar

\[
\boxed{
\sum_{Q=X-L_X}^{X}S_X(n,Q)d_X(Q)\ge0.
}
\tag{T-27801.2}
\]

A fixed or polylogarithmic collar is the preferred production form because it makes the source-specific boundary ledger finite/local, but the logical implication to producer positivity only needs an explicit cofinal collar satisfying the two displayed conditions.

No assertion is made that `S_X` is a positive operator on arbitrary data.

## 3. Exact implication to producer positivity

`L-27801` proves the finite third-Abel identity

\[
A_X(n)=\sum_{Q=2}^{X}S_X(n,Q)d_X(Q).
\tag{T-27801.3}
\]

It also proves complete monotonicity of

\[
x^{-1/2}\log(X/x)
\]

on `(0,X]`, and therefore

\[
d_X(Q)\ge0\qquad(Q+3\le X).
\tag{T-27801.4}
\]

Under TACP-I, every term of the interior sum is nonnegative. TACP-B gives the sign of the only region where zero-extension at the endpoint destroys complete monotonicity. Hence

\[
\boxed{A_X(n)\ge0\qquad(2\le n\le X).}
\tag{T-27801.5}
\]

This step has no hidden norm or asymptotic passage: it is one finite equality plus two finite sign ledgers.

## 4. Producer positivity closes the carry theorem

PR #277 `L-23814` proves exactly that producer positivity implies

\[
\sum_{n=2}^{X}A_X(n)\sqrt n=O((\log X)^2).
\tag{T-27801.6}
\]

The binary–ternary flow then gives the complete prime-power ramp

\[
\boxed{
\mathcal P(X)
\ge4\sqrt X-O((\log X)^C)
}
\tag{T-27801.7}
\]

for a fixed absolute exponent after the inherited finite carry/entropy bookkeeping.

Equivalently, the half-moment and profit/debt firewalls of PR #277 are automatically controlled. There is no separate Möbius total-variation estimate to prove.

## 5. RH deduction

At square endpoints `X=N^2`, the source-pinned square-screw identity converts (T-27801.7) into a subpolynomial upper envelope for the screw statistic. The reviewed critical-square sampling/Landau mechanism then excludes a rightmost zeta zero with real part greater than `1/2`. Functional-equation symmetry gives

\[
\boxed{RH.}
\]

Thus

```text
TACP
-> binary–ternary producer positivity
-> BTF with O(log^2 X) variation
-> sharp prime-power ramp
-> square-screw/Landau
-> RH.
```

The final arrow chain is inherited at its existing reviewed/proposed scope; this branch does not rewrite its normalization.

## 6. Why the proposed hinge may be more tractable

The previous producer sign theorem asked directly for positivity after Möbius inversion and a recursive fragmentation operator. TACP separates that sign into two qualitatively different pieces:

1. a **universal rational combinatorial kernel theorem** about the third cumulative response of the fixed binary–ternary grammar;
2. a **small source-bound endpoint theorem** for the explicit critical weight.

The first has no logarithms, square roots, zeta values, or analytic continuation. It is an integer/Fraction sign problem and may admit induction on the binary/ternary ancestry graph.

The second is exactly where the RH-sensitive source is allowed to enter. It cannot be dropped: `R-27801` proves that the second-order source-independent version is false.

This division is the central proposed advance.

## 7. Candidate proof program for TACP-I

The third-prefix target

\[
\binom{Q-q+2}{2}1_{q\le Q}
\]

has constant positive third discrete derivative. Under Möbius inversion it becomes an explicit divisor-sum polynomial. The descending producer then acts only through the four deterministic children

```text
floor(n/2), ceil(n/2), ceil(n/3), n-ceil(n/3).
```

A proof should attempt to establish a source-free recursion

\[
S_X(n,Q)=\mathcal M(n,Q)
 +\frac12\sum_{m>n}S_X(m,Q)N(m\to n),
\tag{T-27801.8}
\]

where the third-integrated Möbius forcing `mathcal M` is grouped over complete divisor intervals before signs are taken. The target theorem is not termwise positivity of `mathcal M`; cancellation must occur before the induction is closed.

Natural exact decompositions to test are:

- quotient cells `floor(Q/d)`;
- parity/ternary residue classes of the ancestry graph;
- Pascal four-cycles already present in PR #247;
- squarefree collector moves of PR #274 as local rewrites of a negative forcing cell.

Any proof must preserve the exact `Q=59,n=11` second-prefix mutation.

## 8. Candidate proof program for TACP-B

The boundary coefficients are explicit combinations of

\[
(X-j)^{-1/2}\log\frac{X}{X-j}
\]

for small `j`. Taylor expansion has alternating controlled coefficients, but an asymptotic expansion alone is not a proof.

A production proof should emit either:

- an exact finite rational/interval enclosure for a fixed collar after factoring the common `X^{-1/2}` scale; or
- a recursive collar inequality that sends any negative endpoint contribution to earlier positive third-difference columns.

Numerical reconnaissance suggests a short collar, but no fixed width is asserted on this branch.

## 9. Exact failures retained as firewalls

A proposed completion is automatically rejected if it implies either

\[
K_8(3,4)\ge0
\]

or

\[
A_{(60-q)_+}(11)\ge0,
\]

because `R-27801/X-27801` certify the exact values

\[
-1,\qquad-13/16.
\]

Likewise, a finite positivity scan of `S_X` cannot be promoted to TACP-I.

## 10. Exact current boundary

```text
binary–ternary producer algebra             PROPOSED EXACT / inherited
producer positivity => O(log^2 X) BTF       PROPOSED EXACT / inherited
raw-kernel positivity                       FALSE
second-Abel kernel positivity               FALSE (-13/16)
critical source complete monotonicity        PROVED EXACT
third-Abel finite identity                   PROVED EXACT
third-prefix kernel through X=80             EXACT FINITE RECONNAISSANCE
TACP-I all-scale third-kernel positivity     OPEN
TACP-B endpoint collar positivity            OPEN
TACP -> producer positivity -> RH            COMPLETE CONDITIONAL PROPOSAL
Riemann Hypothesis                           UNPROVED
```

This proposal is intentionally ambitious but fail-closed: the only new unproved mathematics is displayed as TACP-I/TACP-B, not hidden inside a generic positivity theorem.
