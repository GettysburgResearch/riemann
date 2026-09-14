# R-106440 — Barycenter and small visible energy do not control the signed index

Claim ID: `R-106440`  
Status: **PROVED EXACT GENERIC ALL-PASS FIREWALL**  
Created: 2026-08-25  
Depends on: the confluent Laguerre tail formula in `L-106430`; `L-106444`  
RH status: **not assumed**

The exact endpoint barycenter and the small finite-band source payment are both
useful, but they do not prove `EVENST106440` in the ambient all-pass class.

Let

\[
b_y(x)={x-iy\over x+iy},
\qquad y>0,
\]

and fix integers `M>d>0`.  Put

\[
U_{M,d}(x)
 ={b_Y(x)^{M-d}\over b_\varepsilon(x)^M}.
\tag{R-106440.1}

Then

\[
\boxed{
\operatorname{wind}U_{M,d}=-d.
}
\tag{R-106440.2}

Given any fixed `c>0`, choose

\[
Y={M\varepsilon+c\over M-d}.
\tag{R-106440.3}

The signed vertical barycenter of the pole/zero divisor is then exactly `-c`,
independent of `M` and `d`.

Now take `d=floor(theta M)` with fixed `0<theta<1` and
`epsilon=M^(-2)`.  Then `Y=O(1/M)`.  For every fixed hard bandwidth `H`, the
captured low-frequency energy of a confluent cluster is the complement of

\[
\sum_{q=0}^{r-1}
\int_{2yH}^{\infty}e^{-t}L_q(t)^2\,dt.
\]

Since `L_q(0)=1`, the complete visible energy of the two clusters is `O_H(1)`
under this scaling, whereas

\[
-\operatorname{wind}U_{M,d}=d\asymp M.
\]

Equivalently, the signed unobserved tail carries `d-O_H(1)` units.  Thus one
may have simultaneously

```text
fixed signed vertical barycenter;
sublinear visible hard-band energy;
linear negative all-pass index.
```

The construction is a generic all-pass countermodel, not an Xi counterexample.
It proves that the remaining theorem must use Xi-specific companion-zero
repulsion, residue pairing, or derivative-compression geometry.  Neither the
barycenter identity nor the small visible exterior-square source can be summed
source-blindly into `EVENST106440`.