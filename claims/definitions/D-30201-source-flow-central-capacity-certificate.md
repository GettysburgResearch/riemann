# D-30201 — Source-flow central-capacity certificate

Claim ID: `D-30201`  
Title: A fail-closed finite certificate for binding Hausdorff boundary sources to actual central edges in the eta–Pascal cascade  
Status: **DEFINITION / PRODUCTION INTERFACE — NO EXISTENCE THEOREM CLAIMED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #301 at `1855957a18b7ea43229cde626178920f7a538951`  
Dependencies: `L-30201`, `L-30202`; PR #272 cycle basis and DCD consumer

## 1. Why a new certificate is required

The corrected eta pairing proves two facts:

```text
A_k>=B_k>=0;
A_k C_k can be replaced by (A_k-B_k)C_k+B_k S_k.
```

It does not prove that the already constructed lower-scale flow contains the
central edge `C_k` with coefficient `A_k`. A source coefficient, a divisor atom,
and a flow-edge coefficient are different mathematical types.

The certificate below makes the missing type conversion explicit.

## 2. Frozen source manifest

Fix an endpoint `X`, cascade depth `a`, stopped-power layer `(s,Y)`, derivative
jet, cutoff cell, and common destination label `v`.

The finite boundary ledger must export:

1. a list of paired common-tail indices `k`;
2. exact coefficients `A_k(v),B_k(v)`;
3. a list of unmatched collar atoms;
4. the residual coefficient sequence
   \[
   R_k(v)=A_k(v)-B_k(v);
   \]
5. a positive moment representation or exact finite-difference proof placing
   `R(v)` in the Hausdorff cone.

Every occurrence is duplicate free. Equal arithmetic destinations are combined
before signs or norms are taken.

## 3. Frozen lower-flow manifest

Let `d_a` be the actual finite flow entering the transition. The certificate
must export every edge of `d_a`, including its sign, source label, parent,
children, and coefficient.

For each paired source entry, declare one actual central edge

\[
 C_k(v)=[4k,2k]\otimes v
\]

in `d_a` with available coefficient `c_k(v)`. No aggregate source mass may be
substituted for this edge coefficient.

Define the capacity deficit

\[
\boxed{
 \delta_k(v)=[A_k(v)-c_k(v)]_+.
}
\tag{D-30201.1}

## 4. Exact replacement ledger

For the paid amount

\[
 t_k(v)=\min\{A_k(v),c_k(v)\},
\]

replace

\[
 t_k(v) C_k(v)
\]

by

\[
 [t_k(v)-B_k(v)]_+ C_k(v)
 +\min\{t_k(v),B_k(v)\}S_k(v),
\]

and emit every uncovered source coefficient separately.

The preferred zero-defect case is

\[
 c_k(v)\ge A_k(v),
\]

when the exact replacement is

\[
 A_k(v)C_k(v)
 \longmapsto
 R_k(v)C_k(v)+B_k(v)S_k(v).
\tag{D-30201.2}

The checker must verify the complete carry vector of the **difference** between
new and old edges, not only the coefficient inequalities.

## 5. Residual routing

Every residual central edge `R_k(v)C_k(v)` is assigned to exactly one declared
next-generation source label. The routing must verify:

```text
same coefficient;
same arithmetic destination;
strict lower endpoint or next cascade depth;
Hausdorff source type preserved;
no source returned to the analytic bulk type.
```

`L-30202` supplies the Hausdorff part once the coefficient binding is correct.

## 6. Collar and bottom rows

Every unmatched shifted-even or odd cutoff atom is listed individually. It is
routed to one of:

```text
explicit finite collar forcing;
a genuinely present included central edge;
a lower endpoint;
a bottom charge with exact objective ledger.
```

The phrase “finite collar” is not a destination. The certificate must emit its
coefficient, edge/source representation, scale, and cost.

## 7. Quantitative defect

Let `omega(e)` be the exact capacity weight of PR #272. Define the source-flow
capacity debt

\[
\boxed{
 \mathfrak C_a(X)
 =\sum_{v,k}\omega(C_k(v))\delta_k(v)
  +\text{unmatched collar debt}
  +\text{negative-edge debt after replacement}.
}
\tag{D-30201.3}

A zero-defect certificate has `mathfrak C_a(X)=0`. For the RH deduction it is
enough to prove uniformly over the `O(log X)` cascade depths that

\[
\boxed{
 \mathfrak C_a(X)\le C\log^A(2X).
}
\tag{D-30201.4}

because this enters only as inhomogeneous forcing in the triangular recurrence.

## 8. Automatic rejection conditions

Reject a certificate if it contains any of the following:

1. a formal divisor source used as an edge coefficient;
2. an incoming central edge not present in the flow manifest;
3. one central coefficient spent twice;
4. a standalone use of `(A-B)C+B S` for the signed source `A e_(2k)-B e_(2k+1)`;
5. an unmatched odd cutoff atom hidden in a common tail;
6. a residual source without a next-generation destination;
7. a boundary source returned to the analytic bulk;
8. a capacity debt measured only in logarithmic objective units;
9. a finite scan promoted to (D-30201.4).

## 9. Proof boundary

This definition supplies a finite, machine-checkable review object. It does not
assert that certificates satisfying (D-30201.4) exist. That existence statement
is the corrected arithmetic hinge of the eta–Pascal route.