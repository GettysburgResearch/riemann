# Selberg height to shallow fifth-companion correlation

## Result of the closure attempt

The attempted proof of the full endpoint targets did not establish ninety
percent. It did close the complete macroscopic endpoint-height and deep
model-space parts of those targets.

The live fifth-endpoint all-pass symbol is

\[
U_{5,\lambda}
 =\frac{(\Xi-i\lambda\Xi')
        (\Xi^{(5)}+i\lambda\Xi^{(6)})}
       {(Ξ+i\lambda\Xi')
        (\Xi^{(5)}-i\lambda\Xi^{(6)})}.
\]

Its winding is `R_0-R_5`, independently of the positive shift on every
regular window.

## Unconditional zero-height input

Functional-equation symmetry gives

\[
\sum_{T<\gamma\le2T}
 \left|\beta-\frac12\right|
 =2\int_{1/2}^{1}N(\sigma;T,2T)\,d\sigma.
\]

Selberg's uniform density theorem therefore yields

\[
\sum_{T<\gamma\le2T}
 \left|\beta-\frac12\right|
 =O(T)=o(N(T,2T)).
\]

For finite polynomial truncations, differentiator compression and Ky Fan's
principle prove that upper zero-height mass cannot increase under
differentiation. The matrix determinant lemma gives the analogous
finite-alpha companion bounds.

## Window-adapted shift

Since the endpoint winding is independent of `lambda>0`, choose `lambda_T`
separately on each regular dyadic window. Rouché continuity then identifies
the two denominator companion zero multisets with the Xi and fifth-derivative
zero multisets, including multiplicities and common-factor reduction.

The Xi height is `o(N)`. Every fifth-derivative zero lies in
`|Im z|<=1/2`, and the pinned theorem

\[
R_5/N>997/1000-o(1)
\]

gives

\[
\sum_{D_{5,\lambda_T}^{\rm red}(a+iy)=0}y
 \le(3/4000+o(1))N.
\]

This proves the formerly open endpoint-localization row.

## Orthogonal deep/shallow split

Factor the denominator inner function at height `eta`:

\[
B_-=B_{\le\eta}B_{>\eta}.
\]

The model-space identity

\[
K_{B_-}
 =K_{B_{\le\eta}}
  \oplus B_{\le\eta}K_{B_{>\eta}}
\]

is orthogonal. Therefore the all-pass Hankel charge splits with no cross term,
and every deep direction costs at most one:

\[
\mathcal C_{>\eta}
 \le {3\over4000\eta}N+o(N).
\]

At `eta=1/100`, the deep contribution is at most `3/40 N`. Since the
fifth-endpoint allowance above ninety percent is `97/1000`, the sole remaining
statement is

```text
SHALLOWCORR106591:
  the confluent numerator/denominator canonical-correlation defect on
  denominator companion zeros of height <= 1/100 is < 11/500 N.
```

This one statement implies more than ninety percent.

## Why the final statement is genuinely microscopic

For `c>1`, the functions

\[
F_n(z)=c+\cos(nz)
\]

have a positive even Fourier source, no parent real zeros, and a completely
real-rooted fifth derivative. Their zero count in a fixed real interval is
`Theta(n)`, while total vertical height is `O(1)`. Thus a power-sized
population of topological defects can live at vanishing height.

Accordingly the remaining theorem cannot follow from zero-density first
moments, source positivity, a thin zero strip, or high-derivative
real-rootedness alone. It must use an Xi-specific microscopic correlation,
near-line repulsion, arithmetic source estimate, or equivalent oriented phase
mean.

## Status

```text
Selberg horizontal first moment                    PROVED
finite derivative/companion height majorization    PROVED
window-adapted cofinal endpoint height              PROVED
all deep charge above height .01                    PAID <= 3/40 N
SHALLOWCORR106591                                  OPEN / 90%-BEARING
ninety percent                                     UNPROVED
density one / RH                                   UNPROVED
```