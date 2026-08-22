# L-104515 — Exact last-defect dichotomy

Claim ID: `L-104515`  
Status: **PROVED EXACT REDUCTION; TWO EXCLUSION THEOREMS OPEN**  
Created: 2026-08-22  
Depends on: `L-104510--L-104514`  
RH status: **unproved**

Fix `T>0`, `H>1/2`, and a regular rectangle

\[
\Omega_{T,H}=\{z:|\Re z|<T,\ -H<\Im z<0\}.
\]

By `L-104513`, every Xi derivative is zero-free on the horizontal side
`Im z=-H`. Choose `n` by `L-104514`, with `T<T_n`, so the high companion

\[
E_{2n}(z)=\Xi^{(2n)}(z)-i w_n^{-1}\Xi^{(2n+1)}(z)
\]

has no zero in `Omega_(T,H)`.

For the fixed positive normalization `lambda=1/w_n`, put

\[
E_k(z)=\Xi^{(k)}(z)-i\lambda\Xi^{(k+1)}(z).
\]

Then `E_k'=E_(k+1)`.

Suppose `E_0` has a zero in the rectangle. Let `k<2n` be the largest index for
which `E_k` has a lower-half-plane zero. Then `E_(k+1)` has none.

The generalized Hermite–Biehler/Cauchy-index transport at this last step has
only two possible sources of index loss.

## Interior event

There is a real zero `c` of `Xi^(k+1)` with

\[
\operatorname*{Res}_{z=c}
\frac{\Xi^{(k)}(z)}{\Xi^{(k+1)}(z)}
=
\frac{\Xi^{(k)}(c)}{\Xi^{(k+2)}(c)}
>0.
\tag{L-104515.1}
\]

Equivalently, `c` is a wrong extremum and the derivative-ratio Pick diagonal is
negative.

## Vertical-flux event

The Hermite–Biehler companion crosses the boundary index through one of the
vertical sides `Re z=+/-T`. The flux is the integer

\[
\mathfrak F_k(T,H)
=
\frac1{2\pi i}
\int_{\partial_v\Omega_{T,H}}
\left(
\frac{E_k'}{E_k}
-
\frac{E_{k+1}'}{E_{k+1}}
\right)dz,
\tag{L-104515.2}
\]

with the two vertical sides oriented as part of the boundary. Since the
horizontal sides are zero-free for every derivative, no other escape channel
exists.

Consequently the following two theorems imply zero-freeness of `E_0` in every
fixed rectangle:

```text
PRES104515:
  no positive derivative-ratio residue can occur at a last defective level;

VFLUX104515:
  the vertical Hermite–Biehler index flux at a last defective level is zero.
```

By `L-104510.6`, their conjunction for all large regular `T` implies RH.

This is a last-event reduction, not a sum of separately bounded charges. It
preserves the exact cancellation discarded by `RPCH104501`.
