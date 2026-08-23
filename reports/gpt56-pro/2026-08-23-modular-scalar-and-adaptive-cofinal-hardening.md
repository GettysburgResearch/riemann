# Modular scalar and adaptive cofinal hardening

Date: 2026-08-23  
Branch: `research/gpt56-pro/104510-hermite-biehler-last-defect`  
RH status: **unproved**

## Executive result

The two fixed-order `Xi''' -> Xi''` attack lanes both advanced, but each
required a binding correction.

```text
finite mixed-orbit matrix PSD       FALSE already at t=0;
fixed theta-orbit cutoff            EVENTUALLY NEGATIVE at high frequency;
complete modular scalar             EXACTLY REDUCED;
adaptive jet-matched cutoff         EXACTLY CONSTRUCTED;
global scalar sign                  OPEN.
```

## Route A — modular integration before orbit splitting

The neutral theta carrier is removed by

\[
\mathcal B=e^{u/2}\vartheta(e^{2u})-2\cosh(u/2).
\]

Then

\[
u^2\Phi(u)=\frac{u^2}{4}(D^2-1/4)\mathcal B(u),
\]

and the complete associated kernel is one explicit modular quartic after all
`y` derivatives are integrated by parts.  It also has the exact compression

\[
\mathcal K_2=x^4\mathcal H_1-2x^2\mathcal H_2+\mathcal H_3.
\]

The conclusion-facing sign is equivalent to

\[
\int_0^\infty\mathcal G_2(x)\sin(2tx)\,dx
\le A_2/(2t).
\]

This is the cleanest pen-and-paper target.  It preserves all theta cross terms
and is naturally compatible with recent work on first- and second-level
concavity of the Riemann theta kernel.  Such concavity supplies moment-side and
admissibility constraints, not the missing positive-definiteness theorem.

An unconditional central interval is already available:

\[
\mathcal L_2(t)
\ge
\mu_0\mu_2-rac{t^2}{2}(\mu_0\mu_4-\mu_2^2).
\]

A high-precision diagnostic places the resulting radius near `5.22375`; the
analytic theorem uses the exact moment expression, not that decimal.

## Binding matrix refutation

At `t=0`, with

\[
a_n=F_n(0),\qquad b_n=-F_n''(0),
\]

one has

\[
\mathcal T_{mn}(0)=\frac12(a_mb_n+a_nb_m).
\]

Every two-orbit determinant is

\[
-\frac14(a_mb_n-a_nb_m)^2.
\]

The exact orbit likelihood ratios prove `b_n/a_n` strictly decreases with the
orbit label.  Hence every finite matrix of size at least two is indefinite.
The all-ones scalar may still be positive; matrix PSD is permanently retired.

## Route B — adaptive cofinal certification

A finite theta-orbit sum has an uncancelled third right derivative at the
modular fixed point.  Its Fourier transform therefore behaves as

\[
F_N(t)=2J_Nt^{-4}+O_N(t^{-6}),
\]

and

\[
(F_N')^2-F_NF_N''
=-16J_N^2t^{-10}+O_N(t^{-12})<0
\]

at sufficiently large height.  This is an artificial truncation mode, not a
property of the complete source.

The repaired cutoff subtracts compact modular cusp functions with coefficients
exactly equal to the omitted odd theta jets.  Matching through order `2R+1`
pushes the artificial Fourier mode from `t^-4` to `t^(-2R-4)` while retaining
an exponentially small complete-source error.

The valid cofinal programme is therefore:

1. choose overlapping height intervals;
2. choose `N(T),R(T)` tending to infinity;
3. prove directed positive margins for the jet-renormalized scalar profile;
4. beat the explicit full-source comparison error;
5. preserve coverage of every height.

The preferred implementation evaluates the complete modular mother in a
central `u` region and invokes theta-orbit tails only where no fixed-point cusp
is introduced.

## Immediate research tasks

### Modular-scalar lane

1. Insert Jacobi's autonomous theta differential system into the scalar
   quartic of `L-104534`.
2. Prove a paired-lobe inequality for the tail primitive `G_2`.
3. Determine whether the strict second-level theta concavity gives a useful
   monotonicity ratio for successive sine lobes.
4. Keep the complete combination `x^4 H_1-2x^2 H_2+H_3`; do not spend the
   associated kernels separately.

### Directed-cofinal lane

1. Implement exact modular jets from the full theta differential recurrence.
2. Use the local moment interval as the first certified block.
3. Use adaptive `N,R` on consecutive height annuli.
4. Reject any schedule whose finite profile enters its proved negative
   asymptotic regime.
5. Emit directed margins, theta tails, jet corrections and interval coverage
   in one proof object.

## Scientific boundary

Neither `MSINE104570` nor `ACDM104570` is proved.  Therefore the branch has not
derived `alpha_2>=alpha_3`, and it has not proved RH.