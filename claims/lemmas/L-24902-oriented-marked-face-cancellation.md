# L-24902 — Oriented marked-face cancellation

Claim ID: `L-24902`  
Title: Source-additive subdivisions cancel every unmarked internal face before norms, while a fixed-degree reflected differential word marks only a bounded number of coordinates  
Status: **PROPOSED EXACT COMBINATORIAL LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Dependencies: finite cellular incidence; the degree-two reflected Selberg word of `L-9516`  
Scope: exact incidence algebra; does not prove the reflected reserve

## 1. Source-additive oriented subdivision

Let

\[
C=\sum_{\omega\in\Omega}\epsilon_\omega[\omega],
\qquad \epsilon_\omega\in\{\pm1\},
\]

be a finite oriented source chain. A deterministic partition replaces every
cell by a finite oriented subdivision

\[
S[\omega]=\sum_{\sigma\in\Sigma(\omega)}
\epsilon_{\omega,\sigma}[\sigma].
\]

The subdivision is **source additive** when every child carries the unchanged
source coefficient of its parent and the induced orientation is the usual
boundary orientation.

For every finite cellular subdivision,

\[
\boxed{\partial SC=S\partial C.}
\tag{L-24902.1}
\]

Consequently every internal codimension-one face is incident to exactly two
children with opposite induced signs. After rows with the same source data are
recombined,

\[
\boxed{\text{every internal unmarked face cancels exactly}.}
\tag{L-24902.2}
\]

This identity is finite and coefficientwise. It must be applied before total
variation, Cauchy--Schwarz, or Gram enlargement.

## 2. Marked tensor derivations

Let the source word have coordinates `x_1,...,x_r`. A derivation of degree `d`
is a finite linear combination of tensor Leibniz terms in which at most `d`
coordinate slots carry a logarithmic or differential mark.

For example, a second derivative of a product is

\[
D^2\prod_i f_i
=
\sum_i (D^2f_i)\prod_{k\ne i}f_k
+2\sum_{i<j}(Df_i)(Df_j)
\prod_{k\ne i,j}f_k.
\tag{L-24902.3}
\]

Every term marks at most two slots.

The reflected Selberg product uses one degree-two logarithmic word on the
product source and subtracts the two one-sided degree-two words. Therefore the
complete reflected Leibniz expansion marks at most

\[
2
\]

slots in the direct product word. If the two reflected inverse coordinates are
kept as separate source fibers, a conservative ledger may charge at most two
marks on each side, hence at most four marked slots.

## 3. Marked face identity

Apply the marked derivation to the source-additive subdivision. Because the
mark is inherited with the source coefficient, every internal face whose
incident children have the same marked data still occurs with opposite signs.
Thus

\[
\boxed{
\text{a surviving internal face must contain a marked slot or an omitted
source boundary}.}
\tag{L-24902.4}
\]

An omitted source boundary is not harmless: it is a manifest error and causes
certificate rejection.

The number of internal faces may grow with `K`. This growth is only a
`K`-dependent combinatorial constant for fixed order. The exponential rate is
governed by the number of coordinates simultaneously paid on one surviving
row, not by the number of rows.

## 4. Physical boundary tokens

A production reflected packet may introduce the following additional physical
tokens:

1. left and right endpoints of the compact ratio window;
2. the output-product boundary;
3. one deterministic whole-tuple first-crossing surface;
4. a residual-support boundary `a_i b_i=V` when it genuinely intersects the
   active lattice.

Each token must be attached to an explicit source equation. A partition boundary
created only for bookkeeping is internal and must cancel by (L-24902.2).

The abstract lemma therefore gives a bounded **token vocabulary**, but it does
not by itself prove that the actual top-top source can be charged injectively to
that vocabulary. That binding is part of `RBC(K)`.

## 5. Proof-producing incidence object

For each face, the certificate exports

```text
face ID
parent cell IDs
source tuple projection
induced signs
marked coordinate set
physical-boundary token or INTERNAL
```

The checker requires:

- every `INTERNAL` face occurs exactly twice;
- the two source projections are identical;
- the signs sum to zero;
- every noninternal face has a declared physical token;
- no face pays a coordinate not present in its marked/token data.

## 6. Proof boundary

Closed exactly:

- cancellation of internal faces in a source-additive oriented subdivision;
- the bounded marked-slot count of a fixed-degree Leibniz word;
- the distinction between face count and simultaneous paid-coordinate count.

Not closed:

- the source-additive incidence binding for the full reflected top corner;
- a strict reserve after cancellation;
- an absolute charge bound for the actual packet.
