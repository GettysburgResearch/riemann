# L-100723 — Left and right cubic Taylor certificates form one exact collar AND gate

Claim ID: `L-100723`  
Status: **PROVED EXACT TWO-CERTIFICATE IMPLICATION; TWO ARITHMETIC ESTIMATES OPEN**  
Created: 2026-08-21  
Depends on: `L-100720--L-100722`; PR #691 `L-100616`  
RH status: **not assumed**

Let

\[
H(t)=H_{p,q;\mathcal P}(t),
\qquad
\widetilde H(t)=H(t)-M_{p,q;\mathcal P}(t)
\]

be one literal double-owner cubic interval.  Put

\[
\boxed{
\mathcal L_{p,q;\mathcal P}(t)
={1\over2}\int_0^t(t-u)^2
 |\widetilde H'''(u)|du
}
\tag{L-100723.1}
\]

and

\[
\boxed{
\mathcal R_{p,q;\mathcal P}(t)
={1\over2}\int_t^\infty(u-t)^2
 |\widetilde H'''(u)|du.
}
\tag{L-100723.2}
\]

These are two positive certificates of the **same source-owned collar
occurrence**.

## 1. Left Taylor certificate

By `L-100720`,

\[
H(0)=H'(0)=0,
\qquad H''(0)>0,
\]

and `H'''=widetilde H'''`.  Taylor's formula with integral remainder gives

\[
H(t)={H''(0)\over2}t^2
 +{1\over2}\int_0^t(t-u)^2\widetilde H'''(u)du.
\]

The initial quadratic term is nonnegative. Therefore

\[
\boxed{H(t)_-\le\mathcal L_{p,q;\mathcal P}(t).}
\tag{L-100723.3}
\]

This is the past/activation-prefix certificate.

## 2. Right Taylor certificate

The compact centered collar and its first two derivatives vanish at infinity.
Integrating its third derivative from the right gives

\[
\widetilde H(t)
=-{1\over2}\int_t^\infty(u-t)^2
 \widetilde H'''(u)du.
\]

Since the removed carrier `M` is nonnegative,

\[
\boxed{H(t)_-\le\mathcal R_{p,q;\mathcal P}(t).}
\tag{L-100723.4}
\]

This is the future/largest-owner certificate.

Combining the two bounds pointwise,

\[
\boxed{
H(t)_-^2
\le
\mathcal L_{p,q;\mathcal P}(t)
\mathcal R_{p,q;\mathcal P}(t).
}
\tag{L-100723.5}
\]

No generic Schur factorization or unknown common contraction enters this
identity.

## 3. Joint min--max composition

For a finite labelled prime source, let

\[
\pi_{ij}=r_ir_jL_iR_j
\]

be the exact joint min--max law and define

\[
\mathscr L_k(t)=
 \sum_{i<j}\pi_{ij}\mathcal L_{ij}(t),
\qquad
\mathscr R_k(t)=
 \sum_{i<j}\pi_{ij}\mathcal R_{ij}(t).
\tag{L-100723.6}
\]

Cauchy--Schwarz on this single probability space gives

\[
\boxed{
\sum_{i<j}\pi_{ij}H_{ij}(t)_-
\le\sqrt{\mathscr L_k(t)\mathscr R_k(t)}.
}
\tag{L-100723.7}
\]

This is the concrete realization of the abstract two-certificate gate in
`L-100616.6--7`.

Define the two terminal estimates

\[
\boxed{
\mathrm{LPCC100723}(Y):
\quad
\sup_k\int_1^Y\mathscr L_k(\sqrt X){dX\over X}
=Y^{o(1)}
}
\tag{L-100723.8}
\]

and

\[
\boxed{
\mathrm{FPCC100723}(Y):
\quad
\sup_k\int_1^Y\mathscr R_k(\sqrt X){dX\over X}
=Y^{o(1)}.
}
\tag{L-100723.9}

Then Cauchy--Schwarz in `dX/X`, the exact joint hazard decomposition, finite
cutoff exhaustion, and the centered-cubic Mellin--Landau detector give

\[
\boxed{
\mathrm{LPCC100723}\ \wedge\ 
\mathrm{FPCC100723}
\Longrightarrow RH.
}
\tag{L-100723.10}

## 4. Why the conjunction has new leverage

The two statements are not duplicate norms:

```text
LPCC:
  integrates the collar from the activation origin;
  sees the p^-2 / p^-3/2 third-derivative source first;
  is adapted to first-owner and finite-prefix tools.

FPCC:
  integrates backward from the completed deep carrier;
  sees the future product boundary;
  is adapted to largest-prime squaring and positive divisor renewal.
```

Neither estimate is asserted here.  The advance is the exact pointwise
factorization of one negative collar occurrence into the two complementary
certificates already suggested by the repository's opposite owner lanes.
