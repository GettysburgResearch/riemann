# T-26203 — Consolidated parity/factor-five source-image proposal for RH

Claim ID: `T-26203`  
Status: `FULL CONDITIONAL PROPOSAL — one explicit physical source-image transition theorem remains open`  
Scope: canonical review spine joining the critical Euler fiber, the parity frame, the factor-five carry source, the boundary-collar firewall, and the fixed-ratio shell consumer  
Date: 2026-08-08

## Frozen external dependencies

Review this proposal against the following frozen sources:

```text
PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
         correct two-frequency physical block L-9518

PR #269  51ce086be09be6849c89aa69e22fcff2665b0c03
         omega_2 pointwise wavelet, factor-five localization,
         generalized-prime synthesis, carry Schur reserve

PR #272  05e24b18d326d1aac4fb1e1e1b1f8da033475560
         half-pole jets, B-spline interfaces, shell collar firewall
```

The native source/filter files are `L-26201`--`L-26209` on this branch.

## 1. The one arithmetic source

Let

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2
\]

and define the parity analysis channels

\[
B_+(s)=\frac{p(2^{-s})}{\zeta_{\rm odd}(s)^{-1}},
\qquad
B_-(s)=\frac{p(-2^{-s})}{\zeta_{\rm odd}(s)^{-1}},
\]

with the coefficient interpretation fixed by `L-26205`. Equivalently, both channels retain every odd-prime Möbius coefficient and differ only by `(-1)^{v_2}`.

The exact frame theorem is

\[
\boxed{
|p(z)|^2+|p(-z)|^2\ge\frac{45}{4}
\qquad\left(\frac12\le|z|\le\frac1{\sqrt2}\right).
}
\tag{T-26203.1}
\]

The exact positive Bézout reconstruction is

\[
\boxed{
U(z)p(z)+U(-z)p(-z)=1,
}
\tag{T-26203.2}
\]

where `U` has four strictly positive real coefficients. Thus the inverse-zeta source is recovered by a finite dyadic synthesis; no infinite inverse and no compact-substrip loss is used.

The fixed opposite-parity source

\[
\Omega_2(s)
=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\tag{T-26203.3}
\]

is a degree-six finite synthesis of the parity pair by `L-26207`.

## 2. The exact physical block

For a declared compact real window `H`, PR #241 gives the physical block

\[
\mathcal B_J(H)
=\frac1{(2\pi)^2}
\iint F(t)\overline{F(s)}
\Phi_J(t-s)\,dt\,ds,
\tag{T-26203.4}
\]

with two independent frequencies. Expanding it gives the complete factor-ratio normal Gram, including every translate cross term.

A one-frequency vertical integral, a scalar analytic square, or a rowwise absolute-value estimate is not a dependency of this proposal.

## 3. Positive bulk already closed

The source is assembled in the following order.

### 3.1 Complete odd-core fibers

Every complete five-tap odd-core fiber has zero half-pole-value jet. Hence every unrestricted Green derivative Gram on the complete-fiber span is a positive rank-one Gram. Fibers are completed before quotient partition, and all within-fiber cross terms are retained.

### 3.2 Positive compact Green factor

The critical Euler filter converts the carry Green kernel into a differential image of one nonnegative compact convolution window. Quotient-cell interiors have positive B-spline/Peano remainders after the exact half-pole conjugation.

### 3.3 Factor-five carry localization

For the synthesized source `omega_2`, PR #269 proves that every negative logarithmic-Kummer row is confined to

\[
\boxed{2m\le n<5m.}
\tag{T-26203.5}
\]

The inner band and the entire quotient tail `n>=5m` are nonnegative in the source-specific carry projection.

### 3.4 Uniform transition reserve

On every sufficiently large transition row, the actual generalized-prime carry feature has a strict Schur reserve. A conservative reviewed target is

\[
\boxed{
\langle F,F\rangle
-\frac{|\langle Z,F\rangle|^2}{\langle Z,Z\rangle}
\ge\frac1{60{,}000{,}000}\langle F,F\rangle.
}
\tag{T-26203.6]
\]

Finite rows below the declared threshold belong to the production boundary.

## 4. The sole new theorem — Source-Image Factor-Five Domination (`SIFD`)

A production `SIFD` object is required for every sufficiently large dyadic block. It must start from the complete parity-paired two-frequency physical source and emit one exact coupled matrix ledger with the following properties.

### 4.1 Exact finite source map

It exports a linear source map

\[
\mathcal T_m:
\mathcal H_m^{\rm phys}
\longrightarrow
\mathcal H_m^{\rm carry}
\oplus\mathcal H_m^{\rm bd}
\tag{T-26203.7}
\]

which:

- includes every complete five-tap odd-core fiber;
- performs the finite Bézout synthesis to `omega_2`;
- retains every quotient cell `2,3,4`;
- retains every physical translate cross term;
- exports the exact boundary collar and lower-block rows;
- reproduces the dyadic and `2/3` Mertens projections.

### 4.2 Physical-to-feature congruence

The complete physical transition form has an exact decomposition

\[
\boxed{
\mathcal Q_m^{\rm phys}
=
\mathcal P_m
+
\mathcal T_m^*
\begin{pmatrix}
\mathcal G_m^{\rm tr}&0\\
0&\mathcal R_m^{\rm bd}
\end{pmatrix}
\mathcal T_m,
}
\tag{T-26203.8}
\]

where `P_m>=0`, `G_m^tr` is the complete generalized-prime factor-five carry Gram, and `R_m^bd` is the complete boundary/lower-block ledger. No unidentified remainder is permitted.

### 4.3 Strict source-image reserve

After the transition source square is completed and the exact boundary routes are inserted, the production object proves

\[
\boxed{
\mathcal Q_m^{\rm phys}
\succeq
\kappa_0 m^2\mathcal E_m
-
\sum_{r=1}^{R}\theta_r(m-r)^2\mathcal E_{m-r}
-C(1+m)^A I,
}
\tag{T-26203.9]
\]

with constants independent of `m`,

\[
\kappa_0>0,
\qquad
\theta_r\ge0,
\qquad
\boxed{\sum_{r=1}^{R}\theta_r<\kappa_0.}
\tag{T-26203.10]
\]

Here `E_m` is the block energy of the synthesized `omega_2` source or an explicitly equivalent paired energy. The exact equivalence map must be included in the certificate.

This is `SIFD`.

## 5. SIFD implies the shell-energy theorem

Dropping the nonnegative physical form from the left of (T-26203.9) and taking a running maximum gives

\[
m^2E_m
\le C_1(1+m)^A
+\frac{\sum_r\theta_r}{\kappa_0}
\max_{1\le r\le R}(m-r)^2E_{m-r}.
\]

Because the displayed ratio is strictly less than one, induction yields

\[
E_m=O(m^{A-2}).
\tag{T-26203.11}
\]

In particular,

\[
E_m=e^{o(m)}.
\tag{T-26203.12}
\]

The finite synthesis and all-ratio transfer give the same block exponent for the dyadic fixed-ratio Mertens shell.

## 6. Shell energy implies RH

By `L-26209`, shell block energy gives a subpower Riesz estimate and controls the bottom-charge consumer. The Laplace/Mellin transform has an uncancelled `1/zeta` pole at every hypothetical zero with real part greater than `1/2`. Therefore

\[
\boxed{\mathrm{SIFD}\Longrightarrow\mathrm{RH}.}
\tag{T-26203.13]
\]

Functional-equation symmetry supplies the opposite half of the critical line.

## 7. Why this is the canonical consolidation

The following former hinges are now consumers or diagnostics, not separate open theorems:

```text
Greedy Slack / DCRS;
Green energy;
Bottom-Charge Positivity;
Boundary-Jet Domination;
generic balanced Type II;
full Carry Saturation.
```

`L-26209` identifies the shell, collar, Riesz, and bottom-charge sources. `SIFD` is the sole proposed producer.

The endpoint-scale positive carry frame of PR #265 and Möbius fragmentation of PR #272 remain alternative producers. They are not used as hidden assumptions.

## 8. Automatic rejection

Reject this proposal if any one of the following occurs:

1. the physical identity uses one frequency;
2. a five-tap fiber is split before its cross terms are retained;
3. the finite synthesis omits a delay or a parity channel;
4. a quotient row outside `2,3,4` carries an unaccounted negative term;
5. the physical-to-carry map has a kernel direction with nonzero target energy;
6. a boundary or collar row remains at the current scale;
7. total lower-block charge is at least the reserve;
8. a same-sign odd Möbius cube disappears;
9. the dyadic or `2/3` Mertens mutation is lost;
10. a finite numerical ladder is promoted to a uniform-in-`m` theorem.

## 9. Exact status

```text
parity analysis frame and finite synthesis       PROPOSED COMPLETE
correct two-frequency block                      IMPORTED / REVIEWED
complete-fiber half-pole nullity                 PROPOSED COMPLETE
factor-five negative-row localization            PROPOSED COMPLETE
carry-feature strict reserve                     PROPOSED COMPLETE
shell/Riesz/collar/bottom-charge triangle        PROPOSED COMPLETE
SIFD source-image congruence and charge bound    OPEN / RH-BEARING
SIFD -> shell energy -> RH                       COMPLETE CONDITIONAL CHAIN
Riemann Hypothesis                               UNPROVED
```
