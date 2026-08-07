# O-26201 — The logarithmic Hall witness is the prime-ramp firewall

Claim ID: `O-26201`  
Title: The universal logarithmic dual witness turns Reflected Dyadic Hall into the original prime-ramp scalar  
Status: **EXACT SCOPE FIREWALL**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26203`; PR #248 prime-only carry reduction  
Scope: prevents the proposed Hall theorem from being mistaken for a soft combinatorial inequality

## 1. An admissible Hall witness

For every positive-defect prime and negative-slack prime, set

\[
 \alpha_p=\log p,
 \qquad
 \beta_p=\log p.
\tag{O-26201.1}
\]

For every licensed multiplicative block `(A,B)` with `A<B`,

\[
 \sum_{p\mid A}\alpha_p
 =\log A,
 \qquad
 \sum_{p\mid B}\beta_p
 =\log B,
\tag{O-26201.2}
\]

because the endpoint products are squarefree. Hence

\[
 \boxed{
 \sum_{p\mid A}\alpha_p
 <
 \sum_{p\mid B}\beta_p.}
\tag{O-26201.3}
\]

Thus the logarithmic weights are always an admissible Hall witness, independent
of the chosen source grammar.

## 2. RDH at this witness

The Reflected Dyadic Hall inequality becomes

\[
 \sum_{p:d_X(p)>0}d_X(p)\log p
 \le
 \sum_{p:d_X(p)<0}[-d_X(p)]\log p.
\tag{O-26201.4}
\]

Equivalently,

\[
 \boxed{
 \sum_{p\le X}(\log p)d_X(p)\le0.}
\tag{O-26201.5}
\]

By the exact prime-only dual identity,

\[
 \sum_{p\le X}(\log p)d_X(p)
 =
 J_{\mathbb P,X}(b_X^{(0)})
 -
 \sum_{p\le X}\frac{\log p}{\sqrt p}\log(X/p).
\tag{O-26201.6}
\]

Therefore (O-26201.5) is precisely the sharp prime-ramp inequality consumed by
the carry/square-screw route.

## 3. Consequence for review

RDH is not a generic Hall theorem that follows from the abundance of negative
slack or the combinatorics of products.  It contains the RH-bearing scalar as
one explicit extremal witness.

The proposed value of the dyadic parity-dipole route is narrower:

```text
represent this logarithmic witness, and every other Hall witness,
by one source-specific reflected Gram plus a signed digital boundary ledger.
```

A proof which invokes only abstract Hall expansion, total slack, PNT mass, or
multiplicative packing has not discharged the logarithmic witness.

The symbolic reserve identity in `T-26201.25` must specialize at
`alpha=beta=log p` to the exact prime-ramp difference (O-26201.6).  This is a
mandatory mutation and normalization test.

## 4. Proof boundary

Everything in this note is exact finite algebra.  It neither proves the
prime-ramp inequality nor RH.  It identifies the unavoidable scalar projection
inside the new source-specific proposal.
