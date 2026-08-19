# L-99120 — Nilpotent two-sort row resolvent

Claim ID: `L-99120`  
Status: **PROVED EXACT ABSTRACT THEOREM**  
Created: 2026-08-19  
Frozen application base: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **not assumed**

## 1. Setup

Fix one endpoint `X`. Let `S_X` be the positive cone of finite labelled source
measures and let

\[
\mathcal R_X=\mathbb R^{J_X}
\]

be the finite physical-row space containing every live component row. Ordinary
and radix-four responses, target mass and literal score are linear functionals
of `mathcal R_X`; they are not independent source decorations.

Let

\[
\mathsf T_X:S_X\to S_X
\]

be the positive child-source operator. Assume it is **well founded**: every
child endpoint is at most `Y/67+1`. At fixed `X` there is therefore an integer
`L_X` such that

\[
\boxed{\mathsf T_X^{L_X+1}=0.}
\tag{L-99120.1}
\]

Let

\[
\mathsf J_X:S_X\to\mathcal R_X
\]

be the positive current map. It contains two disjoint sorts:

```text
source current: the positive residual-source current;
row current:    the target-free, declared-score-free Hall row bonus.
```

The child operator acts only on the source sort. The row sort has no child
coordinate and is never copied.

Finally let

\[
\mathsf E_X:S_X\to\mathcal R_X
\]

be the canonical equality-row map. Assume the local source identity holds in
the **physical row space**:

\[
\boxed{
\mathsf E_X=\mathsf J_X+\mathsf E_X\mathsf T_X.
}
\tag{L-99120.2}
\]

No declared score coordinate is used in (L-99120.2).

## 2. Exact resolvent

Since `T_X` is nilpotent,

\[
(I-\mathsf T_X)^{-1}
=I+\mathsf T_X+\cdots+\mathsf T_X^{L_X}.
\]

Iterating (L-99120.2) gives

\[
\mathsf E_X
=\mathsf J_X
  (I+\mathsf T_X+\cdots+\mathsf T_X^{L_X})
 +\mathsf E_X\mathsf T_X^{L_X+1}.
\]

The last term vanishes. Hence

\[
\boxed{
\mathsf E_X
=\mathsf J_X(I-\mathsf T_X)^{-1}.
}
\tag{L-99120.3}
\]

For a positive root source `s_X`, define

\[
\boxed{
D_X^{\rm ideal}
:=\mathsf J_X(I-\mathsf T_X)^{-1}s_X.
}
\tag{L-99120.4}
\]

Every summand is a nonnegative physical row, and therefore

\[
D_X^{\rm ideal}\ge0.
\]

By (L-99120.3),

\[
\boxed{
D_X^{\rm ideal}=\mathsf E_Xs_X
}
\tag{L-99120.5}
\]

coordinatewise in the actual physical row space.

## 3. Consequences

For every linear physical-row functional `ell`,

\[
\boxed{
\ell(D_X^{\rm ideal})=\ell(\mathsf E_Xs_X).
}
\tag{L-99120.6}
\]

This applies simultaneously to:

- every component-row coordinate;
- every ordinary response;
- every radix-four response formed after the common ordinary rows;
- target mass;
- literal physical score `mathcal H`;
- every finite boundary coordinate retained in a proof object.

The theorem is algebraic and finite at fixed `X`. A contraction estimate is not
needed for existence or exactness. A bound such as child target mass `<1/8` is
used only for uniform cost estimates and optional infinite-endpoint limiting
arguments.

## 4. Measure-valued direct integrals

The same proof applies when `S_X` is a cone of finite positive measures. The
endpoint descent still makes `T_X` nilpotent, so the inverse is a finite
polynomial. Positive direct integration commutes with every term by finite
Tonelli. Exact convex cubature may be applied **after** (L-99120.4), to the one
resolved finite-dimensional row. Applying a separate cubature or quantizer at
each generation is unnecessary and may destroy label ownership.
