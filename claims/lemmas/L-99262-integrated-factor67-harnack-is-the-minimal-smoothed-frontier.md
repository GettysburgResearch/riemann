# L-99262 — The integrated factor-67 Harnack defect is a strictly weaker scalar closure target

Claim ID: `L-99262`  
Status: **PROVED EXACT REDUCTION; GLOBAL SIGN OPEN**  
Created: 2026-08-20  
Depends on: `L-99261`; PR #647 scalar SHARP Harnack identity  
RH status: **unproved**

Put

\[
 r=67^{-1/2},
 \qquad
 \mathfrak H_{67}(X)=W_X-rW_{X/67},
\]

with `W_y=0` for `y<1`. If

\[
 \mathfrak H_{67}(X)\ge0
\]

for all sufficiently large `X`, and `W` is nonnegative on the resulting finite
base interval, repeated division by `67` gives `W_X>=0` for every later `X`.
By `L-99261`, this implies RH.

The SHARP-kernel representation gives

\[
 \boxed{
 \mathfrak H_{67}(X)
 =\int_1^X
  H_{67}^{\rm sharp}(X/t)\kappa_*(t)\frac{dt}{t},
 }
 \tag{L-99262.1}
\]

where

\[
 H_{67}^{\rm sharp}(y)=\Psi(y)-r\Psi(y/67).
\]

Thus the pointwise scalar Harnack theorem of PR #647 implies the integrated
5:3 Harnack theorem, but the latter only asks for positivity after smoothing by
the positive row kernel.

Using the primitive prefix of `L-99261`, for `X>=67`,

\[
 \boxed{
 \mathfrak H_{67}(X)
 =\int_1^{67}C_*(t)\frac{dt}{t}
  +\int_{67}^X
   \left[C_*(t)-rC_*(t/67)\right]\frac{dt}{t}.
 }
 \tag{L-99262.2}
\]

Consequently localized negative values of the primitive Harnack defect are
allowed, provided their accumulated logarithmic mass never exhausts the finite
initial reserve. This is strictly weaker as a method target than demanding
pointwise nonnegativity of the primitive prefix or of the unsmoothed SHARP
Harnack defect.

The open closure target is:

```text
IHR67:
    mathfrak H_67(X) >= 0 eventually.
```

It is a one-dimensional scalar statement with a zero-free Mellin numerator and
no source-tree normalization ambiguity. It remains RH-bearing and is not
claimed proved here.
