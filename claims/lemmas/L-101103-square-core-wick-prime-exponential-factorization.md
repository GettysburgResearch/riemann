# L-101103 — Exact squared-core / Wick-renormalizer / prime-exponential factorization

Claim ID: `L-101103`  
Status: **PROVED EXACT OPERATOR AND MELLIN FACTORIZATION**  
Created: 2026-08-21  
Depends on: `L-101100--L-101102`  
RH status: **not assumed**

Let `P_Z` be a finite labelled prime set, retaining the two copies of `67` as
separate commuting labels.  Put

\[
r_p=p^{-1/2}
\]

and let `U_p` be the corresponding scale shift.  The native Euler operator is

\[
\mathcal E_Z=\prod_{p\in\mathcal P_Z}(I-r_pU_p).
\]

Define

\[
\mathcal S_Z
=
\prod_{p\in\mathcal P_Z}(I-r_p^2U_p^2),
\]

\[
\mathcal R_Z
=
\prod_{p\in\mathcal P_Z}
\frac{\exp(r_pU_p)}{I+r_pU_p},
\]

and

\[
\mathcal P_Z
=
\exp\!\left(-\sum_{p\in\mathcal P_Z}r_pU_p\right).
\]

All factors commute.  The one-label identity

\[
(1-r^2U^2)\frac{e^{rU}}{1+rU}e^{-rU}=1-rU
\]

gives

\[
\boxed{
\mathcal E_Z=\mathcal S_Z\mathcal R_Z\mathcal P_Z.
}
\tag{L-101103.1}
\]

## 1. Interpretation of the three factors

```text
S_Z:
  the literal finite squared core used in the CV completion;

R_Z:
  a zero-free Wick renormalizer whose local Taylor series starts at order r^2;

P_Z:
  the exponential of the linear prime-shift operator.
```

Thus finite squaring does not lose the original source.  It moves every
critical first-prime contribution into the single factor `P_Z`.

## 2. Polylogarithmic total-variation norm of the renormalizer

For one scalar variable,

\[
\frac{e^x}{1+x}
=
\exp\!\left(\sum_{m\ge2}\frac{(-1)^m}{m}x^m\right).
\]

If `|x|=r<1`, the coefficient `l1` norm is bounded by

\[
\exp\!\left(\sum_{m\ge2}\frac{r^m}{m}\right)
=
\frac{e^{-r}}{1-r}.
\]

Consequently, on source total variation,

\[
\log\|\mathcal R_Z\|_1
\le
\sum_{p\le Z}
[-r_p-\log(1-r_p)].
\]

Since `r_p<=2^(-1/2)` and

\[
-r-\log(1-r)
\le
\frac{r^2}{2(1-r)},
\]

Mertens' prime-reciprocal estimate yields

\[
\boxed{
\|\mathcal R_Z\|_1
\le C(\log Z)^{C_0}
=Z^{o(1)}.
}
\tag{L-101103.2}
\]

The second labelled copy of `67` changes only the absolute constant.

Thus the renormalizer is harmless at every subpower criterion in the live
matrix.

## 3. Mellin factorization

Let

\[
\mathcal P(s)=\sum_p p^{-s}
\]

be the prime zeta series in its initial half-plane.  For the ordinary Euler
source,

\[
\prod_p(1-p^{-s})
=
\left[
\prod_p(1-p^{-2s})
\frac{e^{p^{-s}}}{1+p^{-s}}
\right]
\exp[-\mathcal P(s)].
\]

Equivalently,

\[
\boxed{
\frac1{\zeta(s)}
=
\exp\!\left[-\sum_{m\ge2}{\mathcal P(ms)\over m}\right]
\exp[-\mathcal P(s)].
}
\tag{L-101103.3}
\]

The first factor is analytic and zero-free for `Re(s)>1/2`; it is the infinite
counterpart of `S_Z R_Z`.  Every open-strip reciprocal-zeta pole is therefore
carried by the prime-exponential factor `exp[-P(s)]`.

## 4. Common CV/XD frontier

The CV squared-core theorem controls `S_Z`.  Equation (L-101103.2) controls
`R_Z` with only subpower loss.  The short/long XD carrier in `L-101101` is the
first-order physical manifestation of `P_Z`.

Therefore the two requested proof programmes have one exact common unresolved
source:

\[
\boxed{
\mathcal P_Z
=
\exp\!\left(-\sum_{p\le Z}p^{-1/2}U_p\right).
}
\tag{L-101103.4}
\]

Any closure must estimate this prime-exponential packet after the literal
SHARP/wavelet observation while preserving its carrier cancellation.  No
additional many-prime parity cube remains outside this factor.
