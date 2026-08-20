# R-100704 — Invariant-cone shortcut is unproved and would require a forbidden rough-prefix sign promotion

Status: **AUDIT CORRECTION / METHOD FIREWALL**  
RH status: **unproved**

For the quadratic critical Peano kernel

\[
\kappa(s)=1-(1-s)_+^2,
\]

one has exactly

\[
s\kappa'(s)-\kappa(s)=-\min(s^2,1).
\tag{R-100704.1}
\]

The previous version asserted, without a complete normalization and zero-extension derivation, that applying the `t=1` completed derivative cone was *precisely* a fixed rough reciprocal Möbius prefix.  That precise identification is not proved in this branch and is withdrawn.

What remains binding is the following conditional firewall.

If a proposed invariant cone for the balanced homotopy is converted, after all physical normalizations, into eventual nonnegativity of

\[
A_z(Y)=
\sum_{\substack{n\le Y\\P^-(n)\ge z}}{\mu(n)\over n}
\]

for one fixed rough threshold `z`, then the proposal is false.  The fixed-rough-prefix Mellin transform retains the reciprocal-zeta poles up to a finite nonvanishing Euler factor, and the repository's Landau audit proves that such a prefix cannot be eventually one-signed.

Thus any future cone argument must include an exact statement-to-use derivation showing that its derivative packet is **not** this fixed rough prefix, or must preserve cancellation in the homotopy parameter, activation boundary, or double-owner rectangles.

```text
identity (R-100704.1)                         PROVED;
precise equality with fixed rough prefix      WITHDRAWN;
conditional fixed-prefix no-go                RETAINED;
local transition positivity L-100704          RETAINED AFTER NORMALIZATION REPAIR.
```
