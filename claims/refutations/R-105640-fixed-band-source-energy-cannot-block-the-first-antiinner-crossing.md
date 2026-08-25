# R-105640 — Fixed-band source energy cannot block the first anti-inner crossing

Claim ID: `R-105640`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-25  
Depends on: `L-105640--L-105642`; `R-105620`; sibling `R-106430`  
RH status: **not assumed**

Let a simple zero of the shifted Xi-prime denominator cross the moving boundary
to depth `delta>0`, and let `L<infinity` be fixed.  The exact visible fraction
of its adverse model-space charge is

\[
1-e^{-2\delta L}.
\]

Therefore

\[
\boxed{
1-e^{-2\delta L}\longrightarrow0
\qquad(\delta\downarrow0),
}
\tag{R-105640.1}
\]

while the complementary signed endpoint fraction tends to one.  The same
statement holds in an arbitrary pre-existing inner background after
multiplication by the common factor `|A(b)|^2`.

Consequently no argument of the following form can prove safe descent:

```text
choose one fixed finite source band;
prove a favorable current-weighted energy inequality there;
discard the signed complement or endpoint index;
claim that the first denominator crossing is impossible.
```

At first contact the chosen band sees asymptotically none of the new topological
unit.  This failure is independent of how strong the source contraction is
inside the band.

The firewall does **not** refute an adaptive proof.  Three valid exits remain:

```text
let L grow on the reciprocal-depth scale 1/delta;
retain the exact signed endpoint complement;
work with the transverse spectral-flow derivative before delta tends to zero.
```

This is the zero-height analogue of the raw-shell firewall `R-105620`: taking a
one-sided positive quantity before retaining its compensating index loses the
conclusion-bearing charge.

The result is a proof-architecture no-go, not an Xi counterexample.  RH remains
unproved.
