# Attack on all remaining Riemann fronts

Date: 2026-08-11  
Status: **new exact reductions and firewalls; RH unproved**

## Executive result

The live graph has converged to one scalar sign problem in several disguises.

- The corrected odd Weil operator of PR #368 admits a full fermionic Lenard expansion.  Every exterior coefficient is the pairing of `m^{tensor k}` with a manifestly nonnegative determinant kernel.
- PR #379's first-Hermite zero-heat scalar is the minimal linear member.  PR #378's safe-Euler derivative hierarchy is its Gamma/Stieltjes moment transform, not an independent mechanism.
- Any hypothetical negative eigenvalue has an explicit finite Hankel degree and heat-time witness, but no fixed finite complexity can detect all shallow negative directions.
- The Brownian finite producers remain globally dead by PR #376, but their compact-height expansion is now available through `N^-3` and to all fixed orders algorithmically.
- The reviewed Q4 gap can be bypassed at the criterion level: one central filtered-Chebyshev energy is directly equivalent to RH.  The required polynomial energy estimate remains open and RH-equivalent.

No sign theorem closing any of these criteria was obtained.

## I. Odd Fredholm hierarchy becomes a scalar fermion gas

For

```text
B=M_(1/(c^2+tau^2)) K_a,
A=B* M_m B,
L=BB*=M_r K_(2a) M_r,
```

one has

```text
tr(wedge^k A)
 =1/k! <m^(tensor k), det[L(tau_i,tau_j)]>.
```

The determinant has the exact square representation

```text
det K_(2a)(tau_i,tau_j)
 =(2/pi)^k/k! int exp(-2a sum x_j)
                  det[sin(tau_i x_j)]^2 dx.
```

This is the source-complete exterior-algebra completion sought after Claude's finite rank–trace theorem.  It trades noncommutative prime words for a nonnegative exclusion kernel, but the signed activity remains the full zeta distribution `m`.

## II. Complexity is necessarily adaptive

Four exact finite models show:

```text
first K exterior coefficients positive   does not imply PSD;
bounded t Fredholm positivity             does not imply PSD;
bounded beta heat sign                    does not imply PSD;
one fixed shifted-Hankel order            does not imply PSD.
```

For a genuine negative eigenvalue `-eta`, however, the Chebyshev selector yields a failing Hankel matrix once

```text
d > arcosh sqrt(M_+/eta) / arcosh(1+2eta/R_+),
```

and the relative heat trace becomes positive by

```text
beta=2 eta^-1 log(1+M_+/eta).
```

These strict witnesses are trace-norm stable, so Gaussian prime cutoffs and Galerkin sections inherit them with explicit error budgets.

## III. First-Hermite is the minimal heat/resolvent scalar

The PR #378 kernel satisfies

```text
lim_(y->0) y^-2 R_(k,y)(z)
 =-2(k+2)! z^2/(1-z^2)^(k+3)
 =-2 int_0^infinity q^(k+2)e^-q z^2 e^(qz^2)dq.
```

Thus derivative order `k` merely concentrates a Gamma distribution at heat time `q~k`.  The first-Hermite inequality of PR #379 is the minimal remaining scalar.

Two unconditional dents are available:

1. for sufficiently small `q`, the gamma term dominates the exponentially suppressed first prime, uniformly in `x`;
2. for every fixed `q`, the archimedean logarithmic drift dominates the bounded prime contribution for `|x|>=X(q)`.

The unbounded large-heat direction remains exactly where a terminal off-line pair would appear.

## IV. Brownian route after the Bohr refutation

The exact tail-moment inversion gives

```text
m_N(s)=2xi(s)
 -(2s/piN)xi(s-2)
 +N^-2[s/pi xi(s-2)+s(s-2)/pi^2 xi(s-4)]
 +N^-3[-s/(3pi)xi(s-2)
       -7s(s-2)/(6pi^2)xi(s-4)
       -s(s-2)(s-4)/(3pi^3)xi(s-6)]
 +O_K(N^-4).
```

The reciprocal moment exponential generating function gives every fixed order.  This is useful for a height-dependent diagonal scheme and for certified displacement jets, but it cannot restore global finite-N zero-freeness.

## V. Direct central Q4 criterion

Define

```text
F4(x)=E(4x)-2E(2x)-4E(x)+8E(x/2),
E=psi-x.
```

Its Mellin multiplier is

```text
M4(s)=(4^s-4)(1-2^(1-s)),
```

which has no zero in `1/2<Re(s)<1`.  Therefore

```text
RH
<=> int_(e^J)^(e^(J+1)) |F4(x)|^2/x^2 dx <= polynomial(J).
```

This direct Mellin argument does not rely on the incomplete integrated Q4 recurrence flagged by PR #371.  It supplies a correct central target, not its proof.

## Route priority

1. **First-Hermite prime inequality.** It is linear, countable, has finite negative witnesses, and subsumes the terminal heat/resolvent families.
2. **Fermionic Lenard determinants.** Use them only if determinant repulsion gives arithmetic positivity unavailable to the linear scalar.
3. **Central Q4 block energy.** A source-specific annular correlation theorem here would prove RH directly.
4. **Brownian diagonal scheme.** Retain for compact-height approximation, not global finite real-rootedness.

The upstream Claude result itself explicitly stops at proportions and a bandwidth-one ceiling.  The present packet changes consumers but does not supply the missing all-scale arithmetic cancellation.
