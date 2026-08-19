# Reciprocal renewal after fractional-Fock downgrade

This note records the August 19 continuation after the hostile reconstruction of PR #613.

## Binding correction

The original `L-98703` centering argument is invalid: parity and the logarithmic heat do not commute with Weyl displacement. The exact compensated observable and conjugated heat are now recorded on PR #613 under the `98900` correction namespace. The proposed tunable energy estimate is therefore not available.

## New exact identity

The reciprocal-Julia inverse pair gives, for

\[
\mathcal B(x)=\sum_{n\le x}b_\diamond(n)n^{-1/2},
\qquad
\mathcal G(d)=g_\diamond(d)d^{-1/2}>0,
\]

the finite renewal equation

\[
\sum_{d\le x}\mathcal G(d)\mathcal B(x/d)=1.
\]

Hence upper overshoot above one is caused only by negative descendant values:

\[
(\mathcal B(x)-1)_+
\le\sum_{d\ge2}\mathcal G(d)\mathcal B_-(x/d).
\]

After logarithmic integration this becomes a positive renewal inequality for bad mass.

## New frontier

Combine this with PR #615's theorem that subpower logarithmic negative mass of the native scalar suffices for RH. The missing theorem is now a complementary inequality controlling negative reciprocal-Julia mass by previous upper overshoot with a contracting two-step tilted kernel.

```text
exact positive renewal                    PROVED
upper bad mass -> negative descendant mass PROVED
complementary negative-mass renewal        OPEN
subpower native scalar debt -> RH          RETAINED
Riemann Hypothesis                         UNPROVEN
```
