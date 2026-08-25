# L-102906 — Global primewise Hodge normal form

Claim ID: `L-102906`  
Status: **PROVED EXACT GLOBAL SOURCE REDUCTION**  
Created: 2026-08-25  
Depends on: `L-102905`; `L-102903--L-102904`; squared/higher-prime-power ledgers on PR #719  
RH status: **not assumed**

Fix a finite labelled-prime horizon. The two labels whose physical prime is `67` remain distinct.

For every label `p`, choose an arbitrary real or complex complementary temperature `t_p` and write

\[
F_{p,t_p}=(1-x_p)(1+x_p)^{t_p},
\qquad
G_{p,t_p}=(1-x_p)(1+x_p)^{1-t_p}.
\]

Define

\[
\mathcal T_{\mathbf t}
=
\bigotimes_p
\left(F_{p,t_p}\otimes G_{p,t_p}\right),
\]

and the harmonic midpoint tensor

\[
\boxed{
\mathcal H
=
\bigotimes_p(M_p\otimes M_p),
\qquad
M_p=1-{x_p\over2}-{x_p^2\over2}.
}
\tag{L-102906.1}
\]

Let `Pi` be global arithmetic convolution of the two factor coordinates.

## 1. Expansion by local Hodge type

Insert `L-102905.1` at every prime. Every global term is a tensor product of local coordinates of one of three kinds:

```text
harmonic midpoint coordinate M_p tensor M_p;
flat antisymmetric coordinate Omega_p;
local remainder V_(p,t_p).
```

If a global term contains at least one `Omega_p`, then

\[
\boxed{\Pi(\text{that term})=0.}
\tag{L-102906.2}
\]

This follows because global convolution factors prime by prime and

\[
\pi_p(\Omega_p)=0.
\]

If a global term contains a `V_(p,t_p)` and no flat coordinate, then its physical source contains at least one local factor of order `x_p^2`. It therefore belongs to the squared/higher-prime-power ideal already controlled on this branch.

Consequently

\[
\boxed{
\Pi(\mathcal T_{\mathbf t})
=
\Pi(\mathcal H)
+
\mathcal G_{\ge2},
}
\tag{L-102906.3}
\]

where `G_(>=2)` is a two-sided source gauge whose every nonconstant local transfer begins at activity `p^-1 U_(p^2)`.

## 2. Polylogarithmic transfer

The local ratio between the fixed product source and the harmonic midpoint product is

\[
\frac{E_pC_p}{M_p^2}
=
1-{1\over4}x_p^2+{1\over4}x_p^3-{3\over16}x_p^4+\cdots.
\]

Both this ratio and its inverse have zero linear coefficient. Therefore, on every finite physical horizon,

\[
\boxed{
\|\mathcal G_{\ge2}\|_{\rm source}
+
\|\mathcal G_{\ge2}^{-1}\|_{\rm source}
\le
(\log(2Y))^{O(1)}.
}
\tag{L-102906.4}
\]

The same statement holds after the common mother, fixed outer detector, exact owner projections, source-owned region projections, and physical collapse wherever the established squared-core theorem applies.

## 3. Exact consequence

Every primewise temperature gauge, endpoint owner assignment, endpoint-color averaging, or complex complementary polarization has the same conclusion-facing critical representative:

\[
\boxed{\mathcal H.}
\tag{L-102906.5}
\]

All deviations are either:

```text
convolution-null;
or squared/higher-prime-power and polylogarithmic.
```

Thus the arithmetic midpoint core is not one convenient remaining gauge. It is the unique global harmonic representative after every exact flat and subcritical coordinate has been quotiented out.

This theorem does not orient its signed physical observation.
