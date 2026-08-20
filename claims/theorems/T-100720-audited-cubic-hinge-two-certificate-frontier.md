# T-100720 — Audited cubic hinge, rough-prefix coarea, and adaptive two-certificate frontier

Claim ID: `T-100720`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; TWO COMPLEMENTARY COLLAR ESTIMATES OPEN**  
Created: 2026-08-21  
Initial mathematical freeze: PR #691 at `be9a4168fa0df971a2fc63176f07ce3beee6c3d4`  
Audited live base: PR #695 at `7b61f6b1998aefa185d0e5beff18e5a456451299`  
RH status: **unproved**

This successor starts from the audited double-owner coboundary route, after the
unsupported divisor-renewal arrows on PR #691 were withdrawn.  It does not use
those arrows.  Its conclusion-facing future certificate is assigned to the
completed-minus-transition coboundary and balanced homotopy of PR #695.

## 1. Exact physical/arithmetic dictionary

For `t=sqrt(y)`,

\[
\Psi(t^2)
=384\int_0^1(t-s)_+(1-s)ds
=192t-64+64(1-t)_+^3.
\]

Every double-owner interval therefore splits exactly into

\[
H_{p,q;\mathcal P}(t)
=M_{p,q;\mathcal P}(t)
+64\Delta_p\Delta_qE_{\mathcal P}(1-t)_+^3,
\]

where `M>=0` is the full deep carrier.

The derivative is the positive coarea

\[
H'_{p,q;\mathcal P}(t)
=384\int_0^1(1-s)
 \mathcal B_{p,q;\mathcal P}((t/s)^2)ds,
\]

with

\[
\begin{aligned}
\mathcal B_{p,q;\mathcal P}(x)
={}&A_{\mathcal P}(x)
-p^{-1/2}A_{\mathcal P}(x/p)\\
&-q^{-1/2}A_{\mathcal P}(x/q)
+(pq)^{-1/2}A_{\mathcal P}(x/(pq)),
\end{aligned}
\]

and

\[
A_{\mathcal P}(x)
=\sum_{d\le x,\,P^+(d)\subseteq\mathcal P}{\mu(d)\over d}.
\]

Thus the physical long collar is exactly a smoothed compensated reciprocal-
Möbius prefix on the finite interior prime semigroup.

## 2. Unconditional bounds and enlarged positive region

Tao's elementary semigroup theorem gives

\[
|A_{\mathcal P}(x)|\le1,
\]

hence a derivative bound uniform in the number and length of the interior
prime interval.

The centered collar has an exact step-source third derivative with coefficients
`d^-2` and endpoint factors `p^-3/2,q^-3/2`.  Its total variation is bounded by
the convergent prime `3/2` Euler product, and the exact joint min--max average
of that variation is uniformly bounded.

A sharper level-pairing argument proves pointwise positivity whenever

\[
\sum_{p<\ell<q}{1\over\ell}+p^{-1/2}+q^{-1/2}<1.
\]

Consequently, for every fixed `A<e`, all sufficiently large intervals

\[
q\le p^A
\]

are nonnegative at every scale. Only genuinely supercritical intervals

\[
\log q\ge(e-o(1))\log p
\]

can remain in the negative matrix.

## 3. Adaptive left/right certificate gate

For one interval define

\[
\mathcal L(t)
={1\over2}\int_0^t(t-u)^2|\widetilde H'''(u)|du,
\]

\[
\mathcal R(t)
={1\over2}\int_t^\infty(u-t)^2|\widetilde H'''(u)|du.
\]

Taylor expansion from the activation origin and from the completed deep end
gives

\[
H(t)_-\le\min\{\mathcal L(t),\mathcal R(t)\}.
\]

The raw integral of `mathcal L` over all later scales is power-sized and is
refuted in `R-100721`.  The corrected gate partitions each occurrence-time pair
according to which certificate is smaller.

Let `pi_ij=r_i r_j L_i R_j` be the audited joint min--max coefficient and put

\[
\mathscr A_k(t)
=\sum_{i<j}\pi_{ij}1_{\mathcal L_{ij}\le\mathcal R_{ij}}
 \mathcal L_{ij}(t),
\]

\[
\mathscr D_k(t)
=\sum_{i<j}\pi_{ij}1_{\mathcal R_{ij}<\mathcal L_{ij}}
 \mathcal R_{ij}(t).
\]

Then

\[
(F_k(t^2))_-\le\mathscr A_k(t)+\mathscr D_k(t).
\]

Define

```text
APCC100723:
  subpower logarithmic integral of the adaptive activation-side certificate;

DPCC100723:
  subpower logarithmic integral of the adaptive deep-side certificate.
```

Finite-cutoff exhaustion and the centered-cubic Mellin--Landau detector give

\[
\boxed{
\mathrm{APCC100723}\wedge\mathrm{DPCC100723}
\Longrightarrow RH.
}
\]

## 4. Assignment to the audited live routes

```text
APCC100723:
  compensated finite prefixes;
  actual activation endpoints;
  first-owner / finite-prefix geometry.

DPCC100723:
  future product boundaries;
  PR #695 mixed-coboundary rectangle telescope;
  completed-minus-transition balanced homotopy.
```

The future side does not invoke the withdrawn divisor-restriction renewal from
PR #691.

## 5. Exact boundary

```text
cubic hinge representation                    PROVED EXACT
carrier/collar separation                     PROVED EXACT
compensated rough-prefix coarea                PROVED EXACT
uniform semigroup-prefix derivative bound      PROVED
summable third-variation source                PROVED EXACT
pointwise positivity q<=p^A for every A<e      PROVED ASYMPTOTICALLY
finite-cutoff exhaustion                       PROVED
adaptive left/right Taylor gate                PROVED EXACT
regularity-only shortcut                       REFUTED
unrestricted left-certificate integral         REFUTED
APCC100723                                     OPEN / RH-BEARING
DPCC100723                                     OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
