# T-105444 — One-height differential microscope frontier

Claim ID: `T-105444`  
Status: **EXACT RH-EQUIVALENT SCALAR FRONTIER; DIFFERENTIAL SIGN OPEN**  
Created: 2026-08-24  
Depends on: `T-105430--T-105443`, `L-105444`  
RH status: **unproved**

## 1. The field

For

\[
m_r={\Xi^{(r)}\over\Xi^{(r+1)}},
\]

define, at base `b>=0`,

\[
\boxed{
\mathcal C_{r,b}(a,h)
={1\over2}
\left[
 h\Re m_r'(a+i(b+h))
-
\Im m_r(a+i(b+h))
\right].
}
\tag{T-105444.1}

This is the infinitesimal limit of the unique affine-free two-height
microscope. It uses one point and one adjacent-rung ratio.

## 2. Exact criterion

Define

```text
DM105444(r,b) — differential microscope at base b

The ratio m_r is holomorphic in Im z>b and

  C_(r,b)(a,h)<=0

for every real a and h>0.
```

Then

\[
\boxed{
\mathrm{DM105444}(r,b)
\Longleftrightarrow
m_r\text{ is Pick in }\Im z>b
\Longleftrightarrow
\Xi^{(r)}\text{ has no zero in }\Im z>b.
}
\tag{T-105444.2}

The first equivalence is the monotonicity of

\[
\Im m_r(a+i(b+h))/h;
\]

the second follows from the paired zero product and the impossibility of a
Pick-function zero.

Let `beta_r` be the upper zero height. Then

\[
\boxed{
\beta_r
=
\inf\{b>=0:\mathrm{DM105444}(r,b)\}.
}
\tag{T-105444.3}

At the base rung,

\[
\boxed{
\mathrm{DM105444}(0,0)
\Longleftrightarrow
\mathrm{RH}.}
\tag{T-105444.4}

## 3. Exact residue and zero detection

At a simple real critical point,

\[
\boxed{
\lim_{h\downarrow0}h\mathcal C_{r,0}(c,h)
={\Xi^{(r)}(c)\over\Xi^{(r+2)}(c)}.
}
\tag{T-105444.5}

At a simple off-line zero `a+i beta`, immediately below its base height,

\[
\boxed{
\mathcal C_{r,b}(a,h)
={\beta-b\over2}+o(\beta-b)>0.
}
\tag{T-105444.6}

Thus one scalar field detects both positive real residues and nonreal zeros.

## 4. Unconditional endpoint

`L-105429` proves

\[
\boxed{
\mathrm{DM105444}(r,b)
\quad\text{for every }b>=1/2.
}
\tag{T-105444.7}

The critical strip is therefore the compact base-height descent interval

\[
0\le b\le1/2.
\]

## 5. One-point adjacent-rung form

Put

\[
\mathcal R_r={\Xi^{(r)}\Xi^{(r+2)}\over(\Xi^{(r+1)})^2}.
\]

Then

\[
\boxed{
2\mathcal C_{r,b}(a,h)
=h(1-\Re\mathcal R_r(z))-\Im m_r(z),
\quad z=a+i(b+h).
}
\tag{T-105444.8}

The open theorem can therefore be attacked without an all-packet determinant,
a selected critical point, or a two-height comparison.

## 6. Differential scale interpretation

On the real-critical distribution stratum,

\[
\mathcal C_r(a,h)
=
\sum_c\rho_c
{h^3\over((a-c)^2+h^2)^2}
\]

and

\[
(\partial_h+|D|)^2\mathcal C_r=0.
\]

The kernel is positive and has Fourier multiplier

\[
{\pi\over2}(1+h|\xi|)e^{-h|\xi|}.
\]

The coarse direction is dissipative. The conclusion-facing base descent from
`1/2` to `0` is the remaining unstable direction.

## 7. Relation to previous gates

```text
all critical Vandermonde determinants
all boundary Loewner packets
all source-critical Stieltjes matrices
outer oriented phase
minimal two-height microscope
```

all collapse, for the global Xi derivative class, to the differential field
in (T-105444.1). The finite-window versions remain distinct before the global
growth interfaces are inserted.

## 8. Exact frontier

```text
one-height differential localizer             PROVED EXACT
Pick/zero-height equivalence                  PROVED EXACT / REVIEW REQUIRED
critical-residue recovery                     PROVED EXACT
simple-zero crossing calibration              PROVED EXACT
unconditional base b>=1/2                    PROVED
adjacent-rung one-point consumer              PROVED EXACT
DM105444(0,0)                                OPEN / RH-EQUIVALENT
Riemann Hypothesis                            UNPROVEN
```
