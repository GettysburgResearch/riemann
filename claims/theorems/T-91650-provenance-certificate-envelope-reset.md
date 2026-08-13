# T-91650 — Provenance-certificate envelope reset

Claim ID: `T-91650`  
Status: **PROVED CONDITIONAL CONSUMER**  
Created: 2026-08-13  
Depends on: `L-91650`, `L-91652`, `L-91653`, `L-91654`, `L-91656`, `L-91406`  
RH status: **conditional on the finite producer and root bridge**

Let `widehat C_X` be the free certificate cone of `L-91652`, with additive
mass `mhat` and pulled-back deficit `widehat Delta`.

Assume every mass-one certificate at endpoint `X` admits a reset with:

```text
current certificate mass at most 1;
recursive child mass at most rho<1;
child endpoints at most X/67;
current positive deficit at most C.
```

For the provenance-causal coefficients, `rho<1/8` by `L-91650`.

Define

\[
\Lambda(X)=
\sup_{Y\le X,\ \widehat m(C)=1}
[\widehat\Delta_Y(C)]_+.
\]

Positive homogeneity and subadditivity give

\[
\boxed{
\Lambda(X)\le C+\rho\Lambda(X/67).
}
\]

Iteration yields

\[
\boxed{
\Lambda(X)\le\frac{C}{1-\rho}<\frac{8C}{7}.
}
\]

Thus every certificate of bounded mass has `O(1)` deficit. If the root theorem
bounds the RH-sensitive endpoint scalar by that deficit plus one absolute root
charge, the resident endpoint criterion implies RH.

This theorem is a consumer. `T-91651` records the concrete proposed producer and
its independent-review boundary.