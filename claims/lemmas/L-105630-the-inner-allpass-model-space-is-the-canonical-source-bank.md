# L-105630 — The inner all-pass model space is the canonical source-owned zero-count bank

Claim ID: `L-105630`  
Status: **PROVED EXACT HARDY/MODEL-SPACE THEOREM**  
Created: 2026-08-25  
Depends on: `L-105290`; `L-105625`; `L-105629`  
RH status: **not assumed**

## 1. Inner all-pass Hankel operator

Let `U` be an inner function in the upper half-plane and let

\[
H_{\overline U}
=P_-M_{\overline U}|_{H^2(\mathbb C_+)}.
\tag{L-105630.1}
\]

Put

\[
\boxed{
K_U=H^2\ominus UH^2.
}
\tag{L-105630.2}
\]

Then

\[
\boxed{\ker H_{\overline U}=UH^2.}
\tag{L-105630.3}
\]

Indeed, `H_(bar U)f=0` iff `bar U f` belongs to `H^2`, which is equivalent to
`f` belonging to `UH^2`.

If `f in K_U`, then for every `g in H^2`,

\[
\langle\overline Uf,g\rangle
=\langle f,Ug\rangle=0.
\]

Hence `bar U f` lies in the negative Hardy space, and

\[
\boxed{
H_{\overline U}f=\overline Uf,
\qquad
\|H_{\overline U}f\|=\|f\|.
}
\tag{L-105630.4}
\]

Thus `H_(bar U)` is a partial isometry whose initial space is exactly `K_U`.
The model space is the canonical all-pass Hankel bank; no auxiliary source
basis is required.

## 2. Finite Blaschke degree

If `U` is a finite Blaschke product of degree `d`, then

\[
\boxed{\dim K_U=d}
\tag{L-105630.5}
\]

with multiplicity. This follows successively from

\[
K_{UV}=K_U\oplus U K_V
\]

and the one-dimensional model space of one Blaschke factor.

The Hankel Hilbert--Schmidt charge is therefore exact:

\[
\boxed{
\|H_{\overline U}\|_{\mathcal S_2}^2=d
=\operatorname{wind}U.
}
\tag{L-105630.6}
\]

with the orientation chosen so that the inner degree is positive. This is the
model-space form of the sharp finite result in `L-105290`.

## 3. Source contraction on the complete bank

Suppose `R>=0` and multiplication by `U` obeys

\[
M_U^*RM_U\preceq R.
\tag{L-105630.7}
\]

Let

\[
W:K_U\hookrightarrow H^2
\]

be the canonical inclusion. `L-105629` gives

\[
\boxed{
W^*M_U^*RM_UW
\preceq
W^*R W.
}
\tag{L-105630.8}
\]

Hence the contraction holds on the **entire** all-pass Hankel initial space,
not only on a hand-selected finite frame. If `U` is finite Blaschke, this is a
finite source-owned bank of dimension exactly equal to its zero-count degree.

After whitening by

\[
G_U=W^*RW,
\]

the normalized physical action has norm at most one on the support of `G_U`.
No Frobenius approximation to an auxiliary Gram is needed at this exact model-
space scope.

## 4. Xi safe-height specialization

For the base Xi derivative all-pass `U_H` of `L-105627` and the monotone
current--Turan weight of `L-105628`, multiplication by `U_H` satisfies the
weighted contraction. Therefore its complete model bank `K_(U_H)` inherits
that contraction.

For a finite canonical-product truncation `U_(H,T)` containing a finite
multiset of reflected denominator zeros, one has

\[
\boxed{
\dim K_{U_{H,T}}
=\#\{\text{retained denominator zeros, with multiplicity}\}.
}
\tag{L-105630.9}
\]

This supplies an exact source-owned finite bank for the all-pass zero count.
Changing the zero truncation changes only the explicit omitted Blaschke and
endpoint ledger; it does not create an unknown denominator Gram.

## 5. What remains

The model-space theorem closes the abstract bank-identification part of
`BANKID105629`. The unresolved Xi interfaces are now:

```text
cofinal entire-window regularization of the canonical-product truncation;
matching the model-space degree to the precise reverse-Rolle/shell count;
common-zero and boundary confluent factors;
the one surviving horizontal/vertical endpoint charge;
descent below the unknown beta_0, where U_H can cease to be inner.
```

Call the finite/cofinal ledger `ENDIDX105630`.

## 6. Scope

The model-space dimension counts the inner all-pass degree, not automatically
the parent Xi zero count in a finite rectangle. The latter requires the
argument-principle endpoint identity. Infinite meromorphic inner functions may
have infinite-dimensional model spaces; finite sections must be defined by a
source-locked canonical truncation. `ENDIDX105630`, `SAFEDESC105628` and RH
remain open.
