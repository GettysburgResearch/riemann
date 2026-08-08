# R-26902 — Direct carry-window transference cancels the RH pole

Claim ID: `R-26902`  
Title: Every atomized carry window contains the zeta factor which cancels the generalized-prime pole, so same-scale carry coercivity cannot by itself control the RH-sensitive physical source  
Status: **EXACT SCOPE REFUTATION / REQUIRED PIVOT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: the atomized carry Mellin identity of PR #247; `L-26901`, `L-26903`; elementary transform algebra  
Scope: direct same-scale transference through the pure carry-window bank; boundary/commutator and lower-scale theorems remain open

## 1. Atomized carry window

For \(0<\theta<1\), define

\[
C(x,\theta)
=\lfloor x\rfloor
-\lfloor\theta x\rfloor
-\lfloor(1-\theta)x\rfloor
\in\{0,1\}
\tag{R-26902.1}
\]

and the logarithmic normalized carry window

\[
\boxed{
H_\theta(u)
=e^{-u/2}C(e^u,\theta)\mathbf1_{u\ge0}.
}
\tag{R-26902.2}
\]

For integers \(n\ge1\), \(0\le j\le n\), and \(q\le n\), putting

\[
\theta=\frac jn,
\qquad
u=\log\frac nq,
\]

gives exactly

\[
C(e^\nu,\theta)=\chi_{n,q}(j).
\tag{R-26902.3}
\]

Therefore, for every coefficient sequence \(c(q)\),

\[
\boxed{
\frac1{\sqrt n}
\sum_{q\le n}c(q)\chi_{n,q}(j)
=
\sum_{q\le n}\frac{c(q)}{\sqrt q}
H_{j/n}(\log n-\log q).
}
\tag{R-26902.4}
\]

Thus a carry profile is literally a physical logarithmic-window output—but with the special window \(H_\theta\).

## 2. Exact transform and the zeta factor

The atomized carry Mellin identity is

\[
\int_1^\infty
C(x,\theta)x^{-s-2}\,dx
=
\frac{\zeta(s+1)}{s+1}
\left[1-\theta^{s+1}-(1-\theta)^{s+1}\right].
\tag{R-26902.5}
\]

Changing variables \(x=e^u\) and putting

\[
\sigma=z+\frac12
\]

gives

\[
\boxed{
\widehat H_\theta(z)
=
\frac{\zeta(\sigma)}{\sigma}
B_\theta(\sigma),
}
\tag{R-26902.6}
\]

where

\[
B_\theta(\sigma)
=1-\theta^\sigma-(1-\theta)^\sigma.
\tag{R-26902.7}
\]

Every carry window therefore has the full factor \(\zeta(\sigma)\).

In particular, at every nontrivial zero \(\rho\),

\[
\widehat H_\theta(\rho-1/2)=0.
\tag{R-26902.8}
\]

## 3. Generalized-prime source

For the opposite-parity source, write

\[
E(\sigma)
=(1-2^{-\sigma})(1-2^{-\sigma-1}),
\tag{R-26902.9}
\]

\[
\Omega_2(\sigma)=\frac{E(\sigma)}{\zeta(\sigma)},
\qquad
A_\omega(\sigma)=\frac{\zeta(\sigma)}{E(\sigma)}.
\tag{R-26902.10}
\]

The generalized-prime Dirichlet series is

\[
\mathcal L_\omega(\sigma)
=-\frac{A_\omega'}{A_\omega}(\sigma)
=-\frac{\zeta'}{\zeta}(\sigma)
+\frac{E'}E(\sigma).
\tag{R-26902.11}
\]

It has the required inverse-zeta pole at every zero of \(\zeta\).

But multiplying by the carry window gives

\[
\begin{aligned}
\widehat H_\theta(z)\mathcal L_\omega(\sigma)
&=
\frac{B_\theta(\sigma)}{\sigma}
\left[
-\zeta'(\sigma)
+\zeta(\sigma)\frac{E'}E(\sigma)
\right].
\end{aligned}
\tag{R-26902.12}
\]

The right side is holomorphic at every nontrivial zeta zero, including a multiple zero. The pole has been canceled exactly by the zeta factor in the carry window.

Hence the direct carry-profile signal

\[
\sum_q\frac{\Lambda_\omega(q)}{\sqrt q}
H_\theta(x-\log q)
\]

is **not** an RH-sensitive prime-Hardy output.

## 4. The compact opposite-parity carry wavelet

Apply the source \(\Omega_2\) to the carry window. Its transform is

\[
\boxed{
\widehat Z_\theta(z)
=\Omega_2(\sigma)\widehat H_\theta(z)
=
\frac{E(\sigma)}{\sigma}B_\theta(\sigma).
}
\tag{R-26902.13}
\]

All zeta factors cancel. This is the transform counterpart of the compact pointwise wavelet in `L-26901`.

Likewise the positive-inverse logarithmic signal has transform

\[
\begin{aligned}
-A_\omega'(\sigma)\widehat Z_\theta(z)
&=
\frac{B_\theta(\sigma)}{\sigma}
\left[
-\zeta'(\sigma)
+\zeta(\sigma)\frac{E'}E(\sigma)
\right],
\end{aligned}
\tag{R-26902.14}
\]

which is again holomorphic at every nontrivial zero.

Thus the exact identity

```text
generalized-prime carry profile
= positive-inverse compact-wavelet synthesis
```

is a pole-canceling identity. It is excellent finite algebra, but it cannot be used as a pole-preserving Hardy coercivity theorem.

## 5. Refuted shortcut

The following implication is false in the intended RH-sensitive sense:

```text
uniform carry-window or carry-Gram bound
-> same-scale bound for the RH-sensitive generalized-prime physical block.
```

Every pure carry analysis window vanishes at the putative off-line pole. Finite linear combinations of such windows retain the common zeta factor. A same-scale reverse frame inequality from a zeta-safe physical window to the pure carry bank is impossible on any vertical strip containing a zeta zero.

Equivalently, a hypothetical off-line pole is a common null frequency of the direct carry-window bank.

This is the carry analogue of the rank-one bulk parity/carry obstruction in `R-23007`.

## 6. What survives

This refutation does **not** invalidate:

- the pointwise carry identities;
- the factor-five localization;
- the carry Schur reserve;
- the positive inverse/generalized-prime synthesis;
- the moment tower;
- a boundary or commutator transference;
- a lower-scale digital recurrence;
- Bottom-Charge Positivity;
- RH.

It changes the final theorem.

A valid completion must obtain strictness from data not contained in the pure carry-window span, such as:

1. the finite endpoint/boundary commutator;
2. the \(m=1\) source coordinate of `L-26904`;
3. the exact digital forcing atoms;
4. the parity-paired physical channel before the carry zeta factor is introduced;
5. an explicit lower-scale recurrence retaining the fixed-ratio Mertens mode.

## 7. Corrected `F5TC` target

The remaining theorem must be a **boundary-commutator Factor-Five Transition Certificate**, not a direct bulk Gram equivalence.

It may use carry features to control the transverse transition sector, but it must separately transport the RH-bearing boundary coordinate through the independent-frequency physical block. The final Schur reserve must be written before the common zeta factor cancels.

A certificate which produces only

\[
G_{\rm phys}\preceq C S^*G_{\rm carry}S
\]

with \(S\) built solely from atomized carry windows fails at every zeta zero.

## 8. Review mutations

A proposed completion must fail if one:

```text
removes the zeta factor from H_theta by assertion;
uses the compact Z_theta window as an RH-sensitive source;
infers pole exclusion from bounded carry profiles alone;
claims a reverse bulk frame inequality across a zeta zero;
omits the physical boundary/commutator channel;
omits the m=1 source;
uses only the carry Schur reserve as the final physical reserve.
```

## 9. Exact boundary

Refuted:

- direct same-scale physical-to-carry coercivity through the pure carry-window bank;
- treating generalized-prime carry profiles as zeta-safe prime-Hardy windows;
- using the compact carry wavelet alone as an RH-sensitive output.

Still open:

- a boundary-commutator physical transition theorem;
- a bottom-charge or digital lower-scale recurrence;
- RH.
