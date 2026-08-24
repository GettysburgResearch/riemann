# R-105430 — Imaginary-axis orientation and real critical points do not force the critical sign

Claim ID: `R-105430`  
Status: **PROVED EXACT POLYNOMIAL SEPARATOR**  
Created: 2026-08-24  
Depends on: `L-105418`, `L-105432`  
RH status: **not assumed**

Put

\[
F(z)=z^4-z^2+1.
\]

Then

\[
F'(z)=2z(2z^2-1),
\]

so every critical point is real:

\[
0,\qquad \pm{1\over\sqrt2}.
\]

For every `y>0`,

\[
F(iy)=y^4+y^2+1,
\qquad
F'(iy)=-i(4y^3+2y),
\]

and therefore

\[
\boxed{
{F(iy)\over F'(iy)}
=i\,{y^4+y^2+1\over4y^3+2y}
\in i(0,\infty).
}
\tag{R-105430.1}
\]

Thus the complete positive-imaginary-axis orientation of `L-105418` holds.
The quotient also has only polynomial growth on every side of every fixed
strip.

Nevertheless, at `c=1/sqrt2`,

\[
F(c)={3\over4},
\qquad
F''(c)=4,
\]

so

\[
\boxed{
\rho_c={F(c)\over F''(c)}={3\over16}>0.
}
\tag{R-105430.2}

The same holds at `-c`. The polynomial itself is not real-rooted:

\[
z^2={1\pm i\sqrt3\over2}.
\]

Hence

```text
all critical points real
+ positive imaginary-axis ratio
+ subexponential fixed-strip growth
DOES NOT imply real-rootedness or the Pick property.
```

The sign `F(c)/F''(c)<=0` in `L-105432` is indispensable. At a positive
residue, the upper-half-plane pole singularity has negative imaginary part and
the lower boundary condition in the Lindelof rectangle fails.

This separator also shows that `L-105418` is a genuine boundary contribution,
not a hidden proof of the sharp critical-residue gate.
