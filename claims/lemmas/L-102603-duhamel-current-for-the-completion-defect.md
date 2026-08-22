# L-102603 — The completion defect is one source-faithful Duhamel current

Claim ID: `L-102603`  
Status: **PROVED EXACT FINITE-HORIZON IDENTITY**  
Created: 2026-08-22  
Depends on: `L-102602`  
RH status: **unproved**

On a finite horizon let

\[
E=\prod_{\ell\in\mathcal L}(I-r_\ell Z_\ell)
\]

be the native labelled source and define the positive completion homotopy

\[
A_t=\prod_{\ell\in\mathcal L}(I+t r_\ell Z_\ell),
\qquad 0\le t\le1.
\]

Then

\[
A_0E=E,
\qquad
A_1E=C,
\]

where \(C\) is the squared completion.  Differentiating the finite product and
integrating gives

\[
\boxed{
E-C
=
-\int_0^1
\sum_{\ell\in\mathcal L}
r_\ell Z_\ell
A_{t,\ne\ell}E\,dt.
}
\tag{L-102603.1}
\]

This identity retains:

- every native factor;
- both labelled copies of \(67\);
- accumulated parity;
- the exact physical shift;
- the full completion coefficient;
- one source owner for each differentiated label.

Applying the common mother, CV channel, XD channel, any exact regional
projection, and physical collapse commutes with (L-102603.1).

Define

```text
AR-DEFECT102600:
  the source-faithful Duhamel current in (L-102603.1), after exact deterministic
  carrier recombination, has subpower logarithmic negative mass in the fixed
  common-mother observation.
```

By `L-102602`, `AR-DEFECT102600` is equivalent modulo a polylogarithmic error to
the original common-mother negative-mass gate and therefore implies RH through
the fixed Mellin–Landau consumer.

The identity does not prove `AR-DEFECT102600`.  It replaces two separately
named rows by one literal current on one source.
