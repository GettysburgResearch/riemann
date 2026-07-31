# M-15603 — Phase-aware terminal-prime visible-block pipeline

Claim ID: `M-15603`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-pro-09-e`  
Created: 2026-07-31  
Dependencies: `L-15610`--`L-15612`, `T-15603`; PRs #163, #165, #168, #169

## Objective

Produce one proof-grade level of the visible Schur margin

\[
 \beta_a
 =\sigma_a^2-\theta_a-\omega_a-\omega_a^2/h_a>0,
\]

where `theta_a` is the complete centered terminal-prime Hankel norm and not an
absolute prime coefficient sum.

## 1. Freeze the profile packet

Record exact rational or directed representations of

```text
profiles phi_1,...,phi_m,
profile Gram G_V,
support width R,
endpoint scaling a,
Laplace vectors v_minus,v_plus,
Hankel convolution matrix C(u).
```

The first production packet should contain:

1. the explicit zero-free dyadic-convolution window of PR #165;
2. one independent phase/profile direction;
3. optional certified-zero notch factors, each with exact zero-ball attenuation
   and support cost.

A scalar profile alone is discovery data. The proof packet must control the
complete Hermitian norm.

## 2. Complete prime manifest

The endpoint formula uses only:

```text
fixed prefix:    log n <= R,
terminal window: 0 <= 2a-log n <= 2R.
```

Emit every prime power in both windows, with no overlap or omission. For every
terminal term, enclose

```text
Lambda(n)/sqrt(n),
u_n=2a-log n,
C(u_n).
```

Accumulate the matrix

\[
 P_a^{term}=2\sum c_nC(u_n)
\]

with directed complex/rational balls.

## 3. Center before taking norms

Compute

\[
 E_a=P_a^{term}-2e^av^-(v^-)^*.
\]

Then add the exact finite polar remainder

\[
 2(v^-(v^+)^*+v^+(v^-)^*)-2e^{-a}v^+(v^+)^*.
\]

The producer must verify the identity of `L-15610` in two independent algebraic
orders. Never subtract the terminal and polar terms only after converting them
to scalar absolute budgets.

## 4. Same-end local-Weyl floor

For the actual profile subspace, certify

\[
 \|f'\|\le M_a\|f\|
\]

or the concentration-packet bound

\[
 M_a\le\Omega_a/\eta_a.
\]

Insert one explicit Riemann--von Mangoldt remainder constant into `L-15612` and
obtain a directed local floor

\[
 \sigma_a^2
 \le\log R_a-4b
 -C_{A,b}(1+M_a)\log R_a/R_a
\]

with every remaining local/prefix term included in the safe direction.

## 5. Terminal norm certificate

Choose rational `theta_a>=0` and verify

\[
 \theta_a^2G_V-E_aG_V^{-1}E_a\succeq0
\]

by exact/directed LDL, or use an independently certified projected-deficit
operator bound.

Report separately:

```text
raw terminal norm,
centered terminal norm theta_a,
local floor sigma_a^2,
visible--ambient radius omega_a,
ambient complement h_a,
beta_a.
```

## 6. Three-block composition

Pass `beta_a`, the radical block, all corrected cross maps, and the assembly
radius to the exact triangular checker of PR #169. The decisive finite output is

```text
F_a=-(e_a+kappa_a+delta_a).
```

No individual eigenvector or principal angle is required.

## 7. Cofinal schedules

Two schedules are proof-relevant.

### Direct matrix schedule

Prove symbolically that

```text
theta_a + omega_a + omega_a^2/h_a
  < sigma_a^2
```

for all sufficiently large supports and that the radical-row loss tends to zero.

### Notched schedule

Select certified simple critical-line zero balls, multiply the universal window
by safe line-notch factors, and prove:

```text
known-line contribution -> 0,
trivial/pole contribution directed,
remaining terminal matrix norm below the local moat.
```

Every filter zero must be proved to lie only on the safe boundary lines of the
open counterexample strip.

## 8. Fail-closed rules

Reject a production artifact if any of the following occurs:

- a missing prime-power interval or duplicate term;
- midpoint phase reduction without an outward enclosure;
- raw terminal and centered forms use different profile hashes;
- the pole-cancellation identity does not overlap;
- a scalar phase is substituted for the full matrix norm;
- the local-Weyl graph constant is inferred only from dimension;
- a fixed finite zero frame is used without a complete residual bound;
- a final interval touches zero;
- the Suzuki/Fourier normalization is not independently bound.

## 9. Immediate computation handoff

Use the complete prime-power streaming backend already developed for the
carrier route, but replace the carrier phases by the compact terminal window.
The first ladder should use modest profile dimensions `m=1,2,4,8` and supports
where the terminal window fits in the existing prime manifest. Preserve every
centered matrix, not only its lowest floating eigenvalue.

A strict positive `beta_a` closes one finite visible block. A cofinal symbolic
bound remains necessary for RH.