# Fifth-residue coherence and projective-variation frontier

## Result of the attempted closure

The exact fifth-endpoint all-pass charge, shallow canonical-correlation gate,
and adaptive-scale gate remain open. A direct attempt to infer the charge from
positive Fourier source, zero-height mass, or pointwise carrier matching is
blocked by the existing `c+cos` family.

The surviving new reduction is discrete and denominator-free.

Let \(c_j\) be consecutive simple real zeros of \(\Xi^{(5)}\), and define

\[
\rho_j=\frac{\Xi(c_j)}{\Xi^{(6)}(c_j)}.
\]

Because \(\Xi^{(6)}(c_j)\) alternates sign,

\[
\rho_j\rho_{j+1}>0
\]

forces an Xi zero between \(c_j\) and \(c_{j+1}\). Thus the complete fifth-step
reverse–Rolle loss is the number of residue-sign transitions.

Two exact positive gates follow.

### Global coherence

\[
\mathfrak C_5
=
\frac{|\sum\rho_j|^2}{M\sum\rho_j^2}.
\]

At least \(\mathfrak C_5 M\) residues have one common sign, so the number of
adjacent transitions is at most \(2M(1-\mathfrak C_5)\). With the pinned
\(R_5/N>997/1000-o(1)\) input,

\[
\mathfrak C_5>\frac{1897}{1994}
\]

implies more than \(90\%\) of zeta zeros lie on the line.

The exact contour coordinate is

\[
\frac{(\Phi_1-C_1)_+^2}
     {M(B-C_2-D_2)}
>
\frac{1897}{1994},
\]

using the boundary and Bézout corrections of `L-105102`.

### Projective edge energy

\[
\mathfrak E_5
=
\sum_j
\frac{(\rho_{j+1}-\rho_j)^2}
     {\rho_j^2+\rho_{j+1}^2}.
\]

Every sign transition costs at least one unit, so

\[
\limsup\frac{\mathfrak E_5+\mathcal E_{\rm reg}}N
<
\frac{97}{1000}
\]

also implies more than \(90\%\).

## Why this is not yet the theorem

Neither residue estimate is proved for fixed derivative order five. The
high-order saddle programme proves coherence only in a growing derivative
band; the low-order contour identity retains nonreal critical, boundary and
adjacent-derivative correction terms. Count information alone does not bound
those residue weights.

The exact positive-source firewall is

\[
F(t)=c+\cos t,\qquad c>1.
\]

It has a positive even Fourier source, no real zeros, and a completely
real-rooted fifth derivative, while its fifth residues alternate signs at
every derivative zero. Therefore source positivity and high-derivative
real-rootedness cannot be promoted to either gate without an Xi-specific
correction estimate.

## Status

```text
fifth-residue sign transition = reverse-Rolle loss   PROVED EXACT
coherence threshold 1897/1994                        PROVED EXACT
projective edge allowance 97/1000                    PROVED EXACT
contour first/second moment interface                 IDENTIFIED EXACTLY
RESCOH106610 / RESEDGE106610                          OPEN
90 percent                                             UNPROVED
density one / RH                                       UNPROVED
```
