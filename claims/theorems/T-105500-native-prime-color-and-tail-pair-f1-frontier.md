# T-105500 — Native prime-color and tail-pair F1 Hodge frontier

Claim ID: `T-105500`

Status: **BINDING SOURCE REPAIR AND MAJOR UNCONDITIONAL NATIVE-F1 REDUCTION; RH UNPROVED**

Created: 2026-08-27

Base: durable draft PR #730

Frozen inputs:

```text
PR #730  b3114562acbeb8c5890ef7a5fc59eed8db71d29a
PR #719  59654c02d13545d6c8c0972315db2628e9efa1f6
PR #751  98af0db6ec7f77d6333a77a3dac53c4698852f43
PR #685  4f69b7656f42dcb5ff250d13adc9f88e8d18f315
PR #715  99cc94c48bafd9b96141f7cef9f1e7aa83012747
```

## 1. Binding source disposition

Corrected PR #719 proves that the *harmonic* equal-pair Euler–Beta field has

\[
H_{\rm EB}(X)
=
-C_0\sqrt X\frac{\log\log X}{\log X}(1+o(1)),
\qquad C_0>0.
\]

Therefore `QPTI103112`, `EBD103120`, and the old completed-source
`QPTI <=> BCI <=> HMO` chain are withdrawn.

`R-105500` also proves the necessary firewall: the balanced PR #730 source has
core coefficient \(b_U\), not \(\mu\), and satisfies \(b_U(c)=0\) for
\(c\le U^2\).  The QPTI semiprime asymptotic does not automatically refute
that balanced source.  What is broken is the former source-identification
arrow and every RH implication which used it without a new proof.

The finite Chow, incidence, Hodge, resolvent, cell, and generic Gram identities
remain exact at their stated scopes.

## 2. Native compactification is a prime-color boundary gauge

At one prime,

\[
(1-\alpha x)(1-\beta x)=1-x
\]

without an \(x^2\) term forces

\[
\{\alpha,\beta\}=\{0,1\}.
\]

Thus every contraction-free ordinary squarefree compactification assigns each
prime wholly to one of two factors.  For any coloring \(\chi\),

\[
\boxed{\mu=\mu_\chi^+*\mu_\chi^-.}
\]

This factorization is coefficient-exact, has unique squarefree products, and
retains the Euler product \(1/\zeta\).  It creates no owner-pair/squared-core
completion mode.

## 3. The Vaughan trilinear is one native tail pair

Let

\[
\nu_U=\mu\,\mathbf1_{n>U},
\qquad
a_U=\varepsilon-\mu_U*\mathbf1.
\]

Then

\[
\boxed{
a_U=\mathbf1*\nu_U,
\qquad
a_U*\mu=\nu_U,
\qquad
a_U*a_U*\mu=a_U*\nu_U.
}
\]

Both factors vanish for \(n\le U\).  Their free diagonals and equal-product
multiplicities are subpower.

More generally,

\[
a_U*a_U*\mu
=
(a_U*\mu_\chi^+)*(a_U*\mu_\chi^-)
\]

for every prime-color gauge.  Natural repeated prime powers are retained as
part of the ordinary native convolution; no Wick-to-ordinary correction is
performed.

## 4. Exact cross-Hodge signature on the same \(K_1\) detector

For the positive ratio-four half-kernel \(A\),

\[
K_1=(D+\tfrac32)(D-\tfrac12)(A*_MA).
\]

Let \(F^\pm\) be the two colored tail fields observed through \(A\).  Their
ordinary cross-convolution is the literal balanced native source.  On
logarithmic coordinates define

\[
\mathcal A_\chi(x)
=
\frac14\|F^++R_xF^-\|_2^2,
\qquad
\mathcal D_\chi(x)
=
\frac14\|F^+-R_xF^-\|_2^2.
\]

Then

\[
F^+*_MF^-=\mathcal A_\chi-\mathcal D_\chi,
\qquad
\mathcal A_\chi+\mathcal D_\chi=\text{constant},
\]

and for \(K_2=DK_1\),

\[
\boxed{
\mathcal B_U^{K_2}
=
-2D(D+\tfrac32)(D-\tfrac12)\mathcal D_\chi.
}
\]

Different prime colorings change \(\mathcal D_\chi\) only by an additive
constant.  The differential Hodge current is gauge-independent.

## 5. Exact ratio-sixteen Hardy primitive

The derivative kernel is

\[
K_2(y)=
\begin{cases}
4\sqrt y-3,&1\le y<2,\\
-4(1+\sqrt2)\sqrt y+3(1+2\sqrt2),&2\le y<4,\\
2(1+2\sqrt2)\sqrt y-6(1+\sqrt2),&4\le y<8,\\
-2\sqrt y+6,&8\le y<16,\\
0,&\text{otherwise}.
\end{cases}
\]

For \(c_n=\mu(n)/\sqrt n\), put

\[
P(x)=\sum_{n\le x}c_n,
\qquad
Q(x)=\sum_{n\le x}\frac{c_n}{\sqrt n},
\qquad
W(x)=3P(x)-4\sqrt x\,Q(x),
\]

and

\[
\Delta_4=(I-S)^2(I-\sqrt2S)^2.
\]

Then

\[
\boxed{G_2(m+)=-\Delta_4W(m).}
\]

The left/right discrepancy is the matching atomic dyadic filter and has
\(M^{-1/2}\) weighted cost.

Every unit cell is affine in \(\sqrt X\), so its negative logarithmic area is
one explicit endpoint primitive.  This gives the completely discrete gate
`NATIVECELL105504`.

## 6. Correct live equivalence

On each dyadic block freeze \(U_j=\lfloor2^{j/6}\rfloor\).  After absorbing the finitely many initial blocks, the derivative
Type-I lattice is

\[
O(X^{-1/6})
\]

and has finite logarithmic mass.  The balanced row is exactly the native
tail-pair Hodge mismatch.

Therefore

\[
\boxed{
\mathrm{NATIVEF1XD}_{105504}
\Longleftrightarrow
\mathrm{NATIVECELL}_{105504}
\Longleftrightarrow
\mathrm{RH}.
}
\]

The equivalent explicit scalar is

\[
\sum_{m<Y}\mathfrak n_m
\left(
-\Delta_4W(m),
-\Delta_4W(m+1)-\Delta_{4,\rm at}c(m+1)
\right)
=
Y^{o(1)}.
\]

This estimate remains open.

## Exact status

```text
harmonic Euler–Beta QPTI/EBD producer              REFUTED
QPTI/BCI/HMO completed-source equivalence           WITHDRAWN
balanced b_U source                                 DISTINCT / NOT REFUTED BY SEMIPRIME MODE
finite Chow/Hodge/configuration identities          RETAINED EXACT
ordinary squarefree two-factor compactification     PRIME-COLOR RIGID
native Möbius prime-color factorization              PROVED EXACT
Vaughan trilinear -> tail pair                       PROVED EXACT
tail-pair source diagonals/equal products            PROVED SUBPOWER
same-K1 positive-half-kernel factorization           PROVED EXACT
cross-Hodge alignment/mismatch signature             PROVED EXACT
prime-color differential gauge flatness              PROVED EXACT
K2 explicit ratio-sixteen kernel                     PROVED EXACT
one dyadic Hardy primitive                           PROVED EXACT
atomic endpoint jump ledger                          PROVED / ABSOLUTE
cell negative-area primitive                         PROVED EXACT
derivative Type-I with U=X^(1/6)                     PROVED POWER-SMALL

NATIVEF1XD105504                                     OPEN / RH-EQUIVALENT
NATIVECELL105504                                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
