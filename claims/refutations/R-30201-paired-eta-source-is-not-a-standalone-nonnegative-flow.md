# R-30201 — A paired eta source is not realized by the displayed nonnegative edge pair

Claim ID: `R-30201`  
Title: The central/sibling replacement is an exact relative carry change, but not a standalone realization of the paired divisor source  
Status: **EXACT SCOPE-MATCHING COUNTEREXAMPLE TO `L-29807.4`; THE RELATIVE SWITCH IDENTITY SURVIVES**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #301 at `1855957a18b7ea43229cde626178920f7a538951`  
Scope: source-to-flow binding in `L-29807`; not a contradiction to the central/sibling carry identity itself

## 1. The valid local identity

At parent `4k`, write

\[
 C_k=[4k,2k],
 \qquad
 S_k=[4k,2k-1].
\]

For every carry column `q`,

\[
\boxed{
 \chi_{S_k}(q)-\chi_{C_k}(q)
 =\mathbf 1_{q\mid 2k}-\mathbf 1_{q\mid 2k+1}.
}
\tag{R-30201.1}
\]

This identity is correct and is retained.

Let

\[
 E_k(q)=\mathbf1_{q\mid2k},
 \qquad
 O_k(q)=\mathbf1_{q\mid2k+1}.
\]

For coefficients `A>=B>=0`, the edge assignment used in `L-29807` is

\[
 d_{A,B,k}=(A-B)C_k+B S_k.
\tag{R-30201.2}
\]

It is coefficientwise nonnegative. Relative to an already present central edge
`A C_k`, it satisfies exactly

\[
\boxed{
 d_{A,B,k}-A C_k
 =B(S_k-C_k),
}
\tag{R-30201.3}
\]

and its relative carry change is `B(E_k-O_k)`.

Thus `L-29807.1` is a valid **relative replacement** statement.

## 2. The standalone source claim is false

The formal paired divisor source in `L-29806` is

\[
 P_{A,B,k}=A e_{2k}-B e_{2k+1},
\]

whose carry image is

\[
 P_{A,B,k}(q)=A E_k(q)-B O_k(q).
\tag{R-30201.4}
\]

Using (R-30201.1), the carry image of (R-30201.2) is

\[
\begin{aligned}
 L_q(d_{A,B,k})
 &=(A-B)\chi_{C_k}(q)+B\chi_{S_k}(q)\\
 &=A\chi_{C_k}(q)+B(E_k(q)-O_k(q)).
\end{aligned}
\tag{R-30201.5}
\]

Therefore

\[
\boxed{
 P_{A,B,k}(q)-L_q(d_{A,B,k})
 =(A-B)E_k(q)-A\chi_{C_k}(q).
}
\tag{R-30201.6}
\]

This is not identically zero. In fact at `q=4k`,

\[
 E_k(4k)=O_k(4k)=0,
 \qquad
 \chi_{C_k}(4k)=\chi_{S_k}(4k)=1,
\]

so

\[
\boxed{
 P_{A,B,k}(4k)=0,
 \qquad
 L_{4k}(d_{A,B,k})=A.
}
\tag{R-30201.7}
\]

Every nonzero ordered pair is therefore a counterexample to the statement that
`d_(A,B,k)` by itself realizes the complete paired divisor source.

## 3. Small exact witness

Take the first eta pair

\[
 k=1,
 \qquad
 A=\frac12,
 \qquad
 B=\frac13.
\]

Then

\[
 d=\frac16[4,2]+\frac13[4,1].
\]

The source and edge loads at columns `2,3,4` are

\[
\begin{array}{c|ccc}
q&2&3&4\\ \hline
A E_1-B O_1&1/2&-1/3&0\\
L_q(d)&1/3&1/6&1/2.
\end{array}
\tag{R-30201.8}
\]

The mismatch is exact. Moreover, the formal source has a negative column at
`q=3`; no standalone coefficientwise nonnegative carry flow can realize it.

## 4. Correct logical consequence

The paired edge assignment can be used only after an exact manifest proves all
of the following:

1. an incoming central edge `A C_k` is genuinely present in the upper flow;
2. the boundary source requiring correction is exactly the relative dipole
   `B(E_k-O_k)`;
3. the residual even source is represented at the next lower endpoint rather
   than silently identified with `(A-B)C_k` at the current endpoint;
4. the all-generation residuals telescope to the exact target divergence;
5. every unmatched cutoff term is retained.

Without that manifest, equations `L-29807.4`, `L-29807.6`, and the DCD deduction
`L-29807.9` do not follow from the displayed local algebra.

## 5. Verdict boundary

```text
central/sibling carry difference                 VERIFIED
coefficientwise nonnegative relative replacement VERIFIED
standalone realization of A e_(2k)-B e_(2k+1)    FALSE
complete all-generation source-to-flow manifest  UNPROVEN
PR #301 recurrence as a completed proof           UNPROVEN
Riemann Hypothesis                                UNPROVEN
```

This counterexample does not show that the proposed cascade cannot be repaired.
It identifies the precise additional source-binding identity that a valid repair
must emit.