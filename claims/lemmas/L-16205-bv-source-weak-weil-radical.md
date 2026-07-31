# L-16205 — Compact BV sources with the two cancellations give exact weak Weil-radical vectors

Claim ID: `L-16205`  
Status: **PROVED MELLIN/ZERO-SIDE EXTENSION; FORM-CLOSURE GATE EXPLICIT**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Primary source input: Connes--Consani arXiv:2106.01715, Lemma 6.1 and equation (1.1)

## 1. Purpose

The published radical statement is formulated for the codimension-two Schwartz
space

```text
S_0^ev={f even Schwartz: f(0)=0, integral f=0}.
```

The repaired prolate source of `T-16201`, extended by zero outside its finite
interval, is compactly supported and of bounded variation but is not Schwartz
at the support endpoints. This lemma proves that the decisive Mellin-zero and
weak Weil-radical conclusion survives in exactly that regularity class.

## 2. Source assumptions

Let `f` be an even function on the real line whose restriction to `(0,infinity)`
fulfills:

1. `f` has bounded variation;
2. `f` has compact support, or more generally rapid decay;
3. `f(x)=O(x^2)` as `x->0`;
4. `integral_0^infinity f(x)dx=0`.

Define

```text
E(f)(u)=u^(1/2) sum_(n>=1) f(nu),
u>0.                                                       (L-16205.1)
```

Connes--Consani Lemma 6.1 implies that this is pointwise well defined,
`O(u^(1/2))` at zero, and rapidly decreasing at infinity. In particular,

```text
E(f) belongs to L1(R_+^*,d*u) intersect L2(R_+^*,d*u).   (L-16205.2)
```

## 3. Exact Mellin factorization

Use the multiplicative Fourier convention

```text
ghat(z)=integral_0^infinity g(u)u^(-iz)d*u.              (L-16205.3)
```

Put

```text
M_f(z)=integral_0^infinity f(x)x^(-1/2-iz)dx.            (L-16205.4)
```

Then, throughout the half-strip

```text
Im z>-1/2,
```

one has the holomorphic identity

```text
boxed:
widehat(E(f))(z)
 =zeta(1/2-iz) M_f(z).                                   (L-16205.5)
```

## 4. Pole cancellation

The source Mellin transform is holomorphic at least for

```text
Im z>-5/2
```

under the `O(x^2)` assumption. The only pole of the zeta factor in this region
occurs at

```text
z=i/2,
```

and

```text
M_f(i/2)=integral_0^infinity f(x)dx=0.                   (L-16205.6)
```

Thus the pole is removable. The product in (L-16205.5) is holomorphic on the
whole region required for every nontrivial-zero parameter.

## 5. Vanishing at every nontrivial zero

Let

```text
rho=1/2+is
```

be a nontrivial zero of zeta. Then `|Im s|<1/2`. The functional equation and
complex conjugation give

```text
zeta(1/2-is)=zeta(1-rho)=0,

zeta(1/2-i conjugate(s))=zeta(conjugate(rho))=0.          (L-16205.7)
```

Hence

```text
boxed:
widehat(E(f))(s)=0,
widehat(E(f))(conjugate(s))=0                             (L-16205.8)
```

for every nontrivial zero parameter `s`, including off-critical zeros.

## 6. Weak Weil-radical consequence

For test functions `g` for which the zero-side formula

```text
QW(h,g)
 =sum_(1/2+is in Z)
   conjugate(hhat(conjugate(s))) ghat(s)                 (L-16205.9)
```

is valid, every summand vanishes when `h=E(f)`. Therefore

```text
boxed:
QW(E(f),g)=0.                                             (L-16205.10)
```

Likewise `QW(g,E(f))=0` by Hermitian symmetry. Thus `E(f)` belongs to the exact
**weak radical** of the Weil distribution against its test-function domain.

## 7. Proof of the Mellin identity

For `Im z>1/2`, absolute convergence permits Tonelli and the substitution
`x=nu`:

```text
widehat(E(f))(z)
 =sum_(n>=1) integral_0^infinity
    u^(1/2) f(nu)u^(-iz)d*u

 =sum_(n>=1)n^(-1/2+iz)
    integral_0^infinity f(x)x^(-1/2-iz)dx

 =zeta(1/2-iz)M_f(z).                                    (L-16205.11)
```

Lemma 6.1 gives `E(f)(u)=O(u^(1/2))` at zero and rapid decay at infinity, so
its Mellin transform is holomorphic for `Im z>-1/2`. The right side is also
holomorphic there after the cancellation (L-16205.6). Analytic continuation
from `Im z>1/2` proves (L-16205.5). Equations (L-16205.7)--(L-16205.10) follow
immediately. QED.

## 8. Application to the exact-radical prolate repair

The source `p_rad` of `T-16201` is a finite linear combination of even smooth
prolate modes on `[-lambda,lambda]`, extended by zero. It is compactly
supported and of bounded variation. The exact constraints prove

```text
p_rad(0)=0,
integral p_rad=0.
```

Even smoothness near zero then gives `p_rad(x)=O(x^2)`. Hence `L-16205`
applies:

```text
boxed:
E(p_rad) is an exact weak Weil-radical vector.             (L-16205.12)
```

This closes the source-regularity uncertainty in `T-16201` at the zero-side
distributional level.

## 9. Remaining form-domain gate

`L-16205` does not by itself assert that every sharp support projection of
`E(p_rad)`, every omitted tail, and every CCM Fourier basis vector belong to one
common closed form domain on which all four pairings used in `L-16203` may be
expanded without approximation.

A complete production transfer needs one of:

1. a continuity theorem extending `QW(E(p_rad),.)=0` from smooth test functions
   to the finite CCM form domain;
2. smooth cutoff approximants with graph/form convergence and a relative error
   smaller than the mode-8 scale;
3. a direct explicit-formula definition of every source/tail pairing proving
   the radical-tail factorization by passage to the limit.

This is now a form-closure question, not a failure of exact zeta-zero
cancellation.
