# L-104518 — Corrected exterior-boundary last-defect transport

Claim ID: `L-104518`  
Status: **PROVED EXACT CORRECTION; TWO EXCLUSION THEOREMS OPEN**  
Created: 2026-08-22  
Supersedes: the vertical-only flux wording of `L-104515`  
Depends on: `L-104510--L-104517`  
RH status: **unproved**

Fix a regular lower rectangle

\[
\Omega_{T,H}
=
\{z:|\Re z|<T,\ -H<\Im z<0\}.
\]

For one fixed `lambda>0`, put

\[
E_k(z)=\Xi^{(k)}(z)-i\lambda\Xi^{(k+1)}(z),
\qquad
E_k'=E_{k+1}.
\]

Let the upper boundary be the real segment

\[
\Gamma_{\rm top}=[-T,T]
\]

and let

\[
\Gamma_{\rm ext}
=
\partial\Omega_{T,H}\setminus\Gamma_{\rm top}
\]

be the closed-boundary complement: both vertical sides together with the lower
horizontal side.

Define

\[
\mathfrak T_k(T)
=
{1\over2\pi i}
\int_{\Gamma_{\rm top}}
\left(
{E_k'\over E_k}
-
{E_{k+1}'\over E_{k+1}}
\right)dz,
\tag{L-104518.1}
\]

\[
\mathfrak X_k(T,H)
=
{1\over2\pi i}
\int_{\Gamma_{\rm ext}}
\left(
{E_k'\over E_k}
-
{E_{k+1}'\over E_{k+1}}
\right)dz.
\tag{L-104518.2}
\]

Neither summand is generally an integer.  Their sum is:

\[
\boxed{
N_{\Omega}(E_k)-N_{\Omega}(E_{k+1})
=
\mathfrak T_k(T)+\mathfrak X_k(T,H).
}
\tag{L-104518.3}
\]

This is the exact argument-principle decomposition.

## 1. Top-boundary phase and real defects

On the real segment,

\[
\frac{d}{dt}\arg E_k(t)
=
\lambda
\frac{
\Xi^{(k+1)}(t)^2
-
\Xi^{(k)}(t)\Xi^{(k+2)}(t)
}{
\Xi^{(k)}(t)^2
+\lambda^2\Xi^{(k+1)}(t)^2
}.
\tag{L-104518.4}
\]

Every positive derivative-ratio residue, equivalently every wrong extremum,
appears as a clockwise local phase event in `mathfrak T_k`.  The exact
adjacent-critical-value ledger of `L-104500` determines its integer jump after
the endpoint phases are included.

## 2. Correct last-defect dichotomy

Choose a high derivative level `r` for which `E_r` is zero-free in the
rectangle, using `L-104514` or the uniform band `L-104517`.  If `E_0` has a
lower-half-plane zero, let `k<r` be the largest index for which

\[
N_\Omega(E_k)>0,
\qquad
N_\Omega(E_{k+1})=0.
\]

Then (L-104518.3) implies that at least one of the following occurs:

1. **positive-residue/top-phase event:** the real-axis phase contains a wrong
   extremum, equivalently a positive residue of
   `Xi^(k)/Xi^(k+1)`;

2. **exterior-boundary event:** the complete exterior charge
   `mathfrak X_k(T,H)` supplies the missing positive index after the endpoint
   phase terms are included.

The lower horizontal contribution may be small or may vanish in a further
limit, but it may not be deleted merely because the segment is zero-free.

## 3. Corrected gates

The valid last-defect implication is

```text
PRES104518:
  no positive derivative-ratio residue/top-phase defect occurs at the last
  defective level;

EFLUX104518:
  the complete exterior-boundary charge cannot carry inward index at that
  level.
```

Then

\[
\boxed{
\mathrm{PRES104518}
\wedge
\mathrm{EFLUX104518}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-104518.5}
\]

`VFLUX104515` is superseded as a standalone index statement.  Any future proof
may recover a vertical-only form only after proving a separate theorem that
the lower horizontal contribution vanishes in the chosen limit.

## 4. New quantitative entry supplied by L-104517

For derivative orders in the uniform high band of `L-104517`, both gates are
vacuous on the admissible boxes because the canonical companions and Xi
derivatives are already zero-free/real-rooted there.  Thus every last defective
level lies below that band.  This is genuine compression of the cascade, but
not yet its complete closure.
