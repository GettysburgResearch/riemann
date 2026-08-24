# L-105603 — The Xi differential microscope is the reciprocal-source Hardy multiplier

Claim ID: `L-105603`  
Status: **PROVED EXACT SAFE-LINE DICTIONARY; PHYSICAL ONE-SIDED TRANSFER OPEN**  
Created: 2026-08-24  
Depends on: `L-105331`, `L-105340--L-105343`, `L-105420--L-105422`, `L-105444`  
RH status: **not assumed**

## 1. Reflected safe-line coordinate

Put

\[
F_r(z)=\Xi^{(r)}(z),
\qquad
m_r(z)={F_r(z)\over F_{r+1}(z)}.
\]

For

\[
z=a+i(b+h),
\qquad b\ge0,\ h>0,
\]
use the reflected Riemann coordinate

\[
\boxed{
s^*=1-\left({1\over2}+iz\right)
={1\over2}+b+h-ia.
}
\tag{L-105603.1}
\]

Let

\[
\mathcal L_r(s)
={\xi^{(r+1)}(s)\over\xi^{(r)}(s)},
\qquad
q_r(s)={1\over\mathcal L_r(s)}
={\xi^{(r)}(s)\over\xi^{(r+1)}(s)}.
\tag{L-105603.2}
\]

Differentiating the functional equation gives

\[
\boxed{
m_r(z)=i q_r(s^*).}
\tag{L-105603.3}
\]

Since `ds^*/dz=-i`, one also has

\[
\boxed{m_r'(z)=q_r'(s^*).}
\tag{L-105603.4}
\]

## 2. Exact differential-microscope formula

The base-height differential field of `L-105444` is

\[
\mathcal C_{r,b}(a,h)
={1\over2}
\left[h\Re m_r'(z)-\Im m_r(z)\right].
\]

Equations (L-105603.3)--(L-105603.4) give

\[
\boxed{
-2\mathcal C_{r,b}(a,h)
=
\Re\left[q_r(s^*)-h q_r'(s^*)\right].
}
\tag{L-105603.5}
\]

Thus the RH-equivalent differential microscope is one explicit first-order
Hardy multiplier applied to the reciprocal logarithmic-derivative source.
There is no remaining selected critical point or matrix packet in this
coordinate.

## 3. Frozen reciprocal Dirichlet source

At rung zero, separate the slowly varying completed-zeta carrier from the
arithmetic Dirichlet series as in `L-105331`:

\[
\mathcal L(s)=L-A(s),
\qquad
A(s)=\sum_{n\ge2}\Lambda(n)n^{-s}.
\tag{L-105603.6}
\]

For fixed real `L>0`, write

\[
\boxed{
{1\over L-A(s)}
=\sum_{n\ge1}b_L(n)n^{-s}.
}
\tag{L-105603.7}
\]

The resolvent expansion of `L-105420` gives

\[
\boxed{b_L(n)\ge0.}
\tag{L-105603.8}
\]

Termwise differentiation yields the exact frozen identity

\[
\boxed{
q_L(s)-h q_L'(s)
=\sum_{n\ge1}
 b_L(n)(1+h\log n)n^{-s}.
}
\tag{L-105603.9}
\]

At

\[
s=\sigma-ia,
\]
its real part is

\[
\boxed{
\sum_{n\ge1}
 b_L(n)(1+h\log n)n^{-\sigma}
\cos(a\log n).
}
\tag{L-105603.10}
\]

The coefficient source is nonnegative; only the physical translation phases
remain signed.

## 4. Base descent is the exact arithmetic frequency amplifier

Lowering the base by `delta` replaces

\[
\sigma\mapsto\sigma-\delta.
\]

Hence each frequency `log n` is multiplied by

\[
\boxed{n^\delta=e^{\delta\log n}.}
\tag{L-105603.11}
\]

This is exactly the backward-Poisson multiplier `e^(delta|D|)` of
`L-105601`, evaluated on the positive arithmetic spectrum

\[
|\xi|=\log n.
\]

The anti-diffusive Xi base descent and the amplification of reciprocal
Dirichlet frequencies are the same operation.

## 5. One-sided Hardy phase reserve

Let `S_x` denote right translation by `x` in a one-sided interval/frame of
length `L_frame`. `L-105422` proves for nonnegative coefficients `a_n` that

\[
\boxed{
A I-\Re\left(e^{i\theta}
 \sum_na_nS_{\log n}\right)
\succeq
\Gamma_{L_{\rm frame}}(a)I,
}
\tag{L-105603.12}
\]

where

\[
\boxed{
\Gamma_{L_{\rm frame}}(a)
\ge
{2\over9L_{\rm frame}^2}
\sum_na_n
\min\{(\log n)^2,L_{\rm frame}^2\}.
}
\tag{L-105603.13}
\]

Apply this with the literal source weights

\[
\boxed{
a_n=b_L(n)(1+h\log n)n^{-\sigma}.}
\tag{L-105603.14}
\]

Then the one-sided translation model has a strict positive reserve before
physical collapse. The same weighted second frequency moment is the phase
variance in `L-105600` and the source energy in the all-pass shell programme.

## 6. Exact statement-to-use map

The remaining transfer theorem is now sharply typed.

```text
DMPXFER105603 — differential-microscope physical transfer

For the actual completed-zeta reciprocal source, realize the frozen positive
operator in a source-owned smooth one-sided frame and prove that

  archimedean drift,
  carrier freezing,
  pole and seam terms,
  horizontal endpoints,
  taper conditioning,
  truncation,
  and the two-trace physical identification

are jointly smaller than the explicit reserve Gamma.
```

If `DMPXFER105603` holds uniformly for every base in `[0,1/2]`, then
(L-105603.5) gives

\[
\mathcal C_{0,b}(a,h)\le0
\qquad(a\in\mathbb R,\ h>0).
\]

By the zero-height variational theorem `T-105444`, this implies RH.

The independent one-sided-Hardy programme has already proved the source sign,
the strict pre-collapse phase gap, reciprocal-tail control and functional-
equation folding. It has not proved this complete physical transfer.

## 7. Relation to height-shell energy

Differentiating the oriented shifted ratio in its deformation parameter gives
the same reciprocal source `q_r`. Integrating its phase velocity along a
height-shell boundary produces the all-pass shell map of `L-105602`.
Therefore:

```text
pointwise differential microscope = one-point phase velocity;
height-shell all-pass energy       = integrated phase velocity/winding;
one-sided Hardy reserve            = pre-collapse positive source energy.
```

These are three consumers of the same reciprocal-source coefficient family.

## 8. Scope

The safe-line and frozen-source formulas are exact. Positivity of the frozen
coefficients does not imply pointwise positivity after physical phase
collapse. No claim is made that the error ledger is below `Gamma`, that
`DMPXFER105603` holds, or that RH is proved.
