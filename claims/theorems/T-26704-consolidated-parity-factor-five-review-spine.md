# T-26704 — Consolidated parity/factor-five review spine for RH

Claim ID: `T-26704`  
Title: Exact positive carry geometry, dyadic source compression, and the one remaining physical source-image transition theorem  
Status: **FULL CONDITIONAL PROPOSAL — ONE EXPLICIT RH-BEARING THEOREM OPEN**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Scope: canonical review spine after the prime-density drift correction; RH is not claimed proved

## 0. Direct verdict

The repository is **not yet finished** in the unconditional sense.

The finite carry geometry, positivity restoration, source compression, quotient-tail signs, and carry-space reserve have all been reduced to exact finite statements. The prime-only queue closure has been withdrawn after a positive density-drift obstruction.

The sole proposed producer retained in this consolidation is:

> **SIFD — Source-Image Factor-Five Domination.**  
> Construct the exact bounded source map from the corrected independent-frequency physical block to the complete generalized-prime carry Gram on quotient cells `2,3,4`, retaining every parity sibling, cross term, collar, and lower-block route, and prove a strict recurrence whose total lower-block charge is smaller than the carry reserve.

Everything after SIFD is explicit. SIFD itself is open.

## 1. Frozen review inputs

Review this spine against the following commits:

```text
PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
         exact two-frequency physical block L-9518

PR #263  73e24368b62f32f31e10691ebbaf3764b544f2a3
         parity-paired Euler frame, finite Bezout synthesis,
         complete-fiber nullity, consolidated SIFD schema

PR #268  73a93663a51a1b945a2bbb2d57f2b1e3a1e1d762
         compact omega_2 carry image and bottom-charge criterion

PR #269  51ce086be09be6849c89aa69e22fcff2665b0c03
         pointwise omega_2 wavelet, factor-five localization,
         generalized-prime synthesis, strict carry reserve

PR #274  c2e1a978a0156944c26132943fa41bcf7c838fec
         proposed density-drift refutation of prime-only PTQ

PR #271  current branch
         affine lift, zero-tax positive deformation,
         queue algebra, and this corrected consolidation
```

No conclusion below should be read at a stronger status than its frozen source.

## 2. Finite positivity is no longer the obstruction

### 2.1 Affine prime-boundary lift

`L-26701` proves that every signed finite carry certificate can be made nonnegative by adding one constant block through a prime `Y in (X,2X)`. Every old response is preserved and only one new boundary charge is created.

If `C` is the maximum benchmark deficit, then

\[
P_X\ge J_X(b_X^{(0)})-C\log X.
\]

### 2.2 Exact least-charge dual

`L-26702` identifies the least such charge by finite LP duality. Its witnesses are nonnegative prime-power weights whose divisor potential is nondecreasing. The normalized von-Mangoldt ray is an admissible witness and cannot be removed.

### 2.3 Zero-tax ordinary-prime deformation

`L-26703` proves, for every sufficiently large finite endpoint, that the parabolic seed admits a nonnegative ordinary-prime-feasible correction whose objective is exactly the actual ordinary-prime ramp:

\[
J_{\mathbb P,X}(b_X^+)=P_X.
\]

This closes:

```text
existence of a positive finite object;
existence of a finite defect-to-slack deformation;
all extra objective tax caused only by positivity.
```

It does not estimate `P_X`.

## 3. Prime-only queue correction

`L-26704` retains a useful exact one-dimensional quotient of ordinary-prime transport. Its terminal queue is the maximum positive residual suffix and is the minimum exterior charge in the prime-to-prime transport cone.

The former proposal `PTQ: Q_X=X^o(1)` is not retained. `R-26702`, importing PR #274 `R-27302`, records the proposed asymptotic

\[
\mathcal Q_X
\ge
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
\]

Thus prime-to-prime transport alone cannot close the proof. The finite queue algebra remains correct; the subpower rate does not.

This correction is load bearing. A reviewer should reject any consolidation that still lists PTQ as the last open theorem.

## 4. One fixed inverse-zeta source

Define

\[
\omega_2(n)
=
\mu(n)
-rac32\mathbf1_{2\mid n}\mu(n/2)
+rac12\mathbf1_{4\mid n}\mu(n/4).
\]

Its Dirichlet series is

\[
\Omega_2(s)
=
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\]

The Euler numerator has no zero in the open counterexample strip, so every off-line zeta zero remains visible.

This source has four exact `2`-adic layers

```text
+1, -5/2, +2, -1/2,
```

and retains every same-sign odd Möbius family together with its actual parity siblings.

## 5. Exact source compression

### 5.1 Two bottom carry rows

PR #268 proves

\[
\sum_{q=2}^n\omega_2(q)\beta_{nq}
=
\begin{cases}
-5/6,&n=2,\\
-1/2,&n=3,\\
0,&n\ge4.
\end{cases}
\]

For the exact triangular carry inverse `c_X`, this gives

\[
\boxed{
5c_X(2)+3c_X(3)
=-6\sum_{q=2}^X
\frac{\omega_2(q)}{\sqrt q}\log(X/q).
}
\]

Eventual nonnegativity of this one bottom functional would imply RH by the stated Mellin/Landau argument. That sign is not proved.

### 5.2 Pointwise factor-five wavelet

PR #269 proves, before averaging,

\[
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j),
\]

where

\[
g_m=\mathbf1_{[m,2m)}-rac12\mathbf1_{[2m,4m)}.
\]

Its reflected logarithmic-Kummer coupling has no negative row outside

\[
\boxed{2m\le n<5m.}
\]

Thus all possible negative source rows lie in quotient cells `2`, `3`, and `4`.

### 5.3 Actual generalized-prime source

The inverse coefficients are explicit and positive:

\[
a_\omega(n)=2v_2(n)+2^{-v_2(n)}>0.
\]

The generalized von Mangoldt weights are nonnegative, and the actual prime carry profile is the positive synthesis

\[
P_n=
\sum_{m\le n}a_\omega(m)\log(m)Z_{n,m}.
\]

No surrogate ordinary-log source is substituted.

### 5.4 Strict carry-space reserve

For every sufficiently large transition row, the generalized-prime carry profile has a uniform Schur moat against the source wavelet. A conservative inherited value is

\[
\kappa_0=1/60{,}000{,}000.
\]

Finite smaller rows are a declared production boundary.

## 6. Exact parity analysis frame

PR #263 uses

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2
\]

and the paired channels `p(z),p(-z)`. It proves the closed-strip reserve

\[
|p(z)|^2+|p(-z)|^2\ge45/4
\]

on the declared annulus, and an exact finite Bezout reconstruction

\[
U(z)p(z)+U(-z)p(-z)=1
\]

with four positive delays.

The source `omega_2` is a finite synthesis of this parity pair. Hence the physical proof may work with a fixed two-channel frame and a finite reconstruction; no infinite Wiener inverse or growing source rank is needed.

Complete odd-core fibers are assembled before quotient partition. Their half-pole-value jet vanishes exactly, so within-fiber cross terms cannot be discarded.

## 7. Correct physical block

PR #241 proves the exact independent-frequency representation

\[
\mathcal B_J(H)
=
\frac1{(2\pi)^2}
\iint F(t)\overline{F(s)}\Phi_J(t-s)\,dt\,ds.
\]

It expands to the complete finite factor-ratio normal Gram. A one-frequency global integral is not a physical block, and no scalar analytic square may replace the reflected mixed product.

Every SIFD certificate must begin from this two-frequency matrix.

## 8. Sole open theorem — SIFD

For every sufficiently large dyadic block, emit one finite proof object containing:

### 8.1 Complete source manifest

- both parity analysis channels;
- every complete five-tap odd-core fiber;
- the finite Bezout synthesis to `omega_2`;
- all quotient cells `2`, `3`, and `4`;
- all physical translate cross terms;
- every cutoff, transition, collar, and finite-boundary row;
- the dyadic and `2/3` Mertens projections.

### 8.2 Exact physical-to-feature congruence

Construct a source map `T_m` and prove

\[
\boxed{
\mathcal L_m^{\rm phys}
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
\]

with

\[
\mathcal P_m\succeq0.
\]

Here `G_m^tr` is the complete generalized-prime factor-five carry Gram and `R_m^bd` is the complete boundary/lower-block ledger. No unidentified remainder is permitted.

### 8.3 Strict recurrence

Using the inherited carry reserve, prove

\[
\boxed{
\kappa_0m^2E_m+Q_m
\le
C(1+m)^A
+
\sum_{r=1}^{R}\theta_r(m-r)^2E_{m-r},
}
\]

where

\[
Q_m\ge0,
\qquad
\theta_r\ge0,
\qquad
\boxed{\sum_r\theta_r<\kappa_0.}
\]

The energy `E_m` must be the synthesized `omega_2` block energy or be connected to it by an exact finite map in the same proof object.

These three requirements are SIFD. They are not currently established.

## 9. Conditional conclusion

Set `F_m=m^2E_m`. SIFD gives

\[
F_m
\le
C_1(1+m)^A
+
\vartheta\max_{1\le r\le R}F_{m-r},
\qquad
\vartheta<1.
\]

Finite-step induction yields polynomial `F_m` and therefore subexponential block energy.

The finite source reconstruction and fixed-ratio transfer give the same exponential rate for the dyadic Möbius shell. Its Mellin/Laplace transform contains an uncancelled reciprocal-zeta factor. Any zero with real part greater than `1/2` would produce a pole in the resulting holomorphic half-plane. Functional-equation symmetry then gives

\[
\boxed{\mathrm{SIFD}\Longrightarrow\mathrm{RH}.}
\]

This implication is conditional on SIFD.

## 10. Automatic rejection tests

Reject the proposal if any one occurs:

1. one frequency is used in place of the mixed physical block;
2. a parity sibling or Bezout delay is missing;
3. a five-tap odd-core fiber is split before its cross terms are assembled;
4. a negative quotient row survives outside cells `2,3,4`;
5. the physical source map has a kernel direction carrying target energy;
6. the carry reserve is quoted without the actual generalized-prime source;
7. a collar or boundary term remains at current scale;
8. total lower-block charge is at least the reserve;
9. a same-sign odd Möbius cube is deleted;
10. the dyadic or `2/3` Mertens mutation is lost;
11. finite numerical matrices are promoted to a uniform theorem;
12. the refuted prime-only PTQ is used as a substitute.

## 11. Review order

1. `R-26702-prime-tail-queue-subpower-fails.md`;
2. `L-26703-positive-prime-deformation-zero-geometric-tax.md`;
3. PR #241 `L-9518`;
4. PR #263 `L-26205`--`L-26209`;
5. PR #269 `L-26901`--`L-26903`;
6. PR #268 `L-26204/T-26202` as the bottom-charge consumer;
7. this theorem's Section 8, beginning with the absent exact source map;
8. the conditional recurrence and Mellin conclusion.

## 12. Exact status

```text
finite positivity and deformation               PROPOSED COMPLETE
prime-only PTQ                                   PROPOSED REFUTED
parity frame and finite source reconstruction    PROPOSED COMPLETE
correct two-frequency block                      IMPORTED / REVIEWED
factor-five negative-row localization            PROPOSED COMPLETE
actual generalized-prime carry source             PROPOSED COMPLETE
strict carry-space reserve                       PROPOSED COMPLETE
SIFD physical source-image congruence             OPEN / RH-BEARING
SIFD strict lower-block recurrence                OPEN / RH-BEARING
SIFD -> shell energy -> RH                        COMPLETE CONDITIONAL
Riemann Hypothesis                               UNPROVED
```
