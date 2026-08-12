# L-91740 — Positive kernel defects generate the canonical lurking isometry

Claim ID: `L-91740`  
Status: **PROVED EXACT KOLMOGOROV/DEFECT REDUCTION**  
Created: 2026-08-13  
Depends on: standard Kolmogorov decomposition of positive kernels; `L-91731`  
RH status: **unproved**

## 1. Positive kernel defect

Let `X` be a label set and let `A,C` be positive semidefinite kernels on `X`.
Assume

\[
\boxed{
R:=A-C\succeq0.
}
\tag{L-91740.1}
\]

Choose minimal Kolmogorov decompositions

\[
C(x,y)=\langle c_y,c_x\rangle_{\mathcal H_C},
\qquad
R(x,y)=\langle r_y,r_x\rangle_{\mathcal H_R}.
\]

Then

\[
A(x,y)
=
\langle c_y\oplus r_y,c_x\oplus r_x\rangle.
\tag{L-91740.2}
\]

## 2. Canonical lurking isometry

Let

\[
A(x,y)=\langle a_y,a_x\rangle_{\mathcal H_A}
\]

be any minimal Kolmogorov decomposition. The linear rule

\[
\boxed{
a_x\longmapsto c_x\oplus r_x
}
\tag{L-91740.3}
\]

preserves all finite Gram matrices and therefore extends uniquely to a unitary

\[
\boxed{
U_A:
\overline{\operatorname{span}}\{a_x:x\in X\}
\longrightarrow
\overline{\operatorname{span}}\{c_x\oplus r_x:x\in X\}.
}
\tag{L-91740.4}
\]

No arbitrary square root of a target operator is used; the residual kernel
itself is the minimal auxiliary Gram.

## 3. Equality case

If `R=0`, the source and declared output Kolmogorov spaces are canonically
unitarily equivalent on their minimal spans.

If `R` is nonzero, every source-to-output isometry must carry a residual
subspace with Gram `R`, up to unitary equivalence. Thus output allocation is
completely encoded by the kernel difference.

## 4. Application to the arithmetic/model problem

Let

\[
A_\omega
\]

be the explicit completed arithmetic source kernel of `L-91731`, and let

\[
C_\omega
=
K_\omega^{\rm crit}
+
K_\omega^{\rm st}
\]

be the declared critical-plus-stable model kernel.

A proof of

\[
\boxed{
A_\omega-C_\omega\succeq0
}
\tag{L-91740.5}
\]

automatically constructs the canonical minimal source-to-model isometry.
The residual kernel is then exactly the combined hyperbolic/auxiliary Gram
provided the common completed source lock has been established.

The open burden is therefore a kernel identity and sign, not a separate
existence theorem for an intertwining operator.
