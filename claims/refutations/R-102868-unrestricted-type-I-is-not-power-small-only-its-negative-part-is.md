# R-102868 — The unrestricted Type-I term is not power-small; only its adverse part is

Claim ID: `R-102868`  
Status: **PROVED EXACT MAGNITUDE/SIGN CORRECTION**  
Created: 2026-08-24  
Depends on: corrected `L-102866`; `L-102867`  
RH status: **unproved**

Put

\[
U=\lfloor Y^{1/6}\rfloor
\]

and let the unrestricted Type-I coordinate be

\[
\mathcal T^{\rm unres}(Y)
=-\sum_{d,e\le U}{\mu(d)\mu(e)\over de}
 \sum_{m\ge1}{1\over m}
 R_L\!\left({Y\over d^2e^2m^2}\right).
\]

Corrected `L-102866` proves

\[
\sum_{m\ge1}{1\over m}R_L(Z/m^2)
=4(1-\sqrt2)(\log2)^2+O_R(Z^{-1/2}).
\]

Consequently

\[
\boxed{
\mathcal T^{\rm unres}(Y)
=4(\sqrt2-1)(\log2)^2
 \left(\sum_{d\le U}{\mu(d)\over d}\right)^2
+O_R(U^2Y^{-1/2}).
}
\tag{R-102868.1}
\]

Since `U=Y^(1/6)`, the remainder is `O_R(Y^(-1/6))`.  The displayed square is nonnegative but is not known, and is not implied by the classical zero-free region, to be `O(Y^(-1/6))`.

Thus the statement in `L-102867` that the **whole** unrestricted Type-I term is `O_R(Y^(-1/6))` is false.  The correct one-sided conclusion is

\[
\boxed{
(\mathcal T^{\rm unres}(Y))_-
=O_R(Y^{-1/6}).
}
\tag{R-102868.2}
\]

This is sufficient for every logarithmic negative-mass consumer: the non-power-small main term is favorable and must not be discarded or relabelled as error.

The derivative detector in `L-102880` has genuine zero square-lattice moment and therefore has a power-small unrestricted Type-I term in absolute value.  The two statements must not be conflated.

```text
unrestricted Type-I favorable square      PROVED EXACT
whole Type-I O(Y^(-1/6))                  FALSE
negative part O(Y^(-1/6))                 PROVED
Riemann Hypothesis                        UNPROVED
```
