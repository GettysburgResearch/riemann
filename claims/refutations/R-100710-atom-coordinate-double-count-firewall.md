# R-100710 — Atom coordinates must not pay the Euler activity twice

Claim ID: `R-100710`  
Status: **BINDING NORMALIZATION CORRECTION; `L-100710` WITHDRAWN AS WRITTEN**  
Created: 2026-08-21  
RH status: **unproved**

The file `L-100710` defined the full critical source atom

\[
w_{m,X}(n)
=n^{-(m+1)/2}
\kappa_{m,m-1}(\sqrt{n/X}).
\]

In these coordinates, adjoining a prime `p` is already represented by

\[
w(n)\longmapsto w(np).
\]

The factor `p^{-(m+1)/2}` inside `w(np)` includes the native
`p^{-1/2}` Euler activity together with the kernel scaling. Therefore the
formula

\[
p^{-1/2}w(np)-p^{-1}w(np^2)
\]

pays the activity a second time and is not the atom-coordinate image of

\[
R_p=p^{-1/2}U_p-p^{-1}U_{p^2}.
\]

The correct atom-coordinate transition is

\[
\boxed{w(np)-w(np^2).}
\]

Accordingly, `L-100710` is withdrawn as written and may not be cited. Its local
positivity conclusion survives only in the corrected form proved in
`L-100711`; its claimed extra future-prime exponent does not survive.

This is the same representation firewall that has recurred elsewhere in the
project:

```text
endpoint-kernel coordinates: coefficient p^(-1/2) is explicit;
full source-atom coordinates: coefficient is already inside w(np).
```

A proof must choose one representation and remain in it through every owner
comparison.