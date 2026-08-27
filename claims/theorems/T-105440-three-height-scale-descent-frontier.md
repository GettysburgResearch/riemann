# T-105440 — Three-height scale descent is a single scalar RH frontier

Claim ID: `T-105440`  
Status: **EXACT EQUIVALENCE AND UNCONDITIONAL COARSE ENDPOINT; FINE-SCALE DESCENT OPEN**  
Created: 2026-08-24  
Depends on: `T-105430`, `L-105435--L-105437`  
RH status: **unproved**

## 1. The microscope field

For

\[
m_r(z)={\Xi^{(r)}(z)\over\Xi^{(r+1)}(z)},
\]

define

\[
\mathcal P_r(a,h)
=-{3\over2}\Im m_r(a+ih)
+{6\over5}\Im m_r(a+2ih)
-{3\over10}\Im m_r(a+3ih).
\tag{T-105440.1}
\]

The complete microscope gate is

```text
THM105440(r) — three-height microscope

For every real a and every h>0:

1. all three denominator values Xi^(r+1)(a+jih), j=1,2,3, are nonzero;
2. P_r(a,h)<=0.
```

## 2. The gate contains critical-point reality

If `Xi^(r+1)` had a zero

\[
z_0=a_0+iy_0
\]

in the upper half-plane, then choosing

\[
h=y_0/j
\]

for any `j in {1,2,3}` places a pole in one of the three sampled ratios. Thus
the finiteness clause of `THM105440(r)` excludes every nonreal critical point.
Reflection excludes the lower half-plane.

On the resulting real-critical stratum, `L-105435` gives

\[
\rho_c
=\lim_{h\downarrow0}h\mathcal P_r(c,h).
\]

Therefore the sign clause gives every critical residue nonpositive.

Conversely, complete critical-point reality and nonpositive residues imply the
Pick representation of `L-105432--L-105433`, and the positive microscope
kernel then gives `mathcal P_r<=0` at every scale.

Hence

\[
\boxed{
\mathrm{THM105440}(r)
\Longleftrightarrow
\mathrm{CRVH105330}(\Xi^{(r)})
\Longleftrightarrow
\Xi^{(r)}\text{ is real-rooted}.}
\tag{T-105440.2}

At `r=0`,

\[
\boxed{
\mathrm{THM105440}(0)
\Longleftrightarrow
\mathrm{RH}.}
\tag{T-105440.3}

## 3. Unconditional coarse-scale endpoint

`L-105430` makes every sampled ratio holomorphic once `h` is sufficiently
large. `L-105436` then proves, for every fixed `r`,

\[
\boxed{
\mathcal P_r(a,h)<0
\qquad
(a\in\mathbb R,\ h\ge H_r^*).
}
\tag{T-105440.4}

Thus the complete microscope gate is unconditionally true on a terminal
half-line of scales.

## 4. First-obstruction dichotomy

Run `h` downward from the coarse region. The first possible failure has exactly
one of two forms.

### A. Pole obstruction

For some `a,h,j`,

\[
\Xi^{(r+1)}(a+jih)=0.
\]

This is a nonreal critical point.

### B. Sign-contact obstruction

All three ratios remain holomorphic, but

\[
\sup_a\mathcal P_r(a,h)=0
\]

for the first time, followed by a positive fine-scale value. In the limit
`h downarrow 0`, such a positive spike becomes a positive real critical
residue.

There is no third obstruction. The former determinant, source-capacity,
boundary-Loewner and outer-phase failures all project to A or B.

## 5. Exact scale equation

On the real-critical measure stratum,

\[
\mathcal P_r(\cdot,h)=\Omega_h*\mu_r,
\qquad
\mu_r=\sum_c\rho_c\delta_c.
\]

`L-105437` gives

\[
\boxed{
\partial_h\mathcal P_r
=-|D|\mathcal R_h\mathcal P_r,
}
\tag{T-105440.5}
\]

where the multiplier of `mathcal R_h` is

\[
{(1-t)(5-3t)\over t^2-4t+5},
\qquad t=e^{-h|\xi|}.
\]

The forward direction in `h` is dissipative. The conclusion-facing direction
from coarse to fine is backward and therefore anti-diffusive. This explains
why an abstract maximum principle does not close the theorem.

## 6. The single source-specific target

Define

```text
MSD105440 — Xi microscope scale descent

For r=0, the coarse solution P_0(a,h)<0 extends to every h>0 without either
(A) a pole obstruction or (B) a sign-contact obstruction.
```

Then

\[
\boxed{
\mathrm{MSD105440}
\Longrightarrow
\mathrm{THM105440}(0)
\Longrightarrow
\mathrm{RH}.}
\tag{T-105440.6}

The same target at higher derivative orders supplies a scalar reverse-Rolle
coordinate.

## 7. Available producer structure

The field is not arbitrary. It is a fixed combination of the oriented shifted
ratio

\[
{\xi'-\alpha\xi\over\xi'+\alpha\xi}.
\]

The independent oriented-ratio/one-sided-Hardy programme supplies:

```text
functional-equation folding to one safe line;
a reciprocal Dirichlet source with power-saving omitted tail;
one global sign for every real tangent chaos;
a strict one-sided translation phase gap.
```

Those facts now have one precise consumer: prevent the first pole or sign
contact in the scale evolution.

## 8. Exact frontier

```text
three-height microscope <-> complete critical sign  PROVED EXACT / REVIEW
coarse-scale microscope negativity                  PROVED UNCONDITIONALLY / REVIEW
nonlocal scale equation                             PROVED EXACT
first-obstruction pole/sign dichotomy                PROVED EXACT
MSD105440 Xi-specific backward scale control         OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVEN
```
