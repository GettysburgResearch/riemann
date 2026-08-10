# O-90302 — The imported quartic \(\xi'\) window is numerically saturated

Claim ID: `O-90302`  
Status: **EMPIRICAL FREDHOLM RECONNAISSANCE — NOT A CERTIFICATE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: the imported \(\xi'\) scalar-window functional and `X-90301`  
Scope: numerical direction-setting only

## 1. Functional

For zeros of \(\xi'\), the imported two-trace ratio at \(\lambda=1\) is

\[
c(v)=\frac{(\int v)^2}
 {\int v^2+\iint D_1(|s-t|)v(s)v(t)\,ds\,dt},
\qquad |s|,|t|\le\frac12,
\]

where

\[
D_1(r)=r-4r^2+
\sum_{k\ge0}
\frac{2\,4^{k+1}k!}{(2k+2)!}r^{2k+3}.
\]

The unconstrained optimizer solves the Fredholm equation

\[
v(s)+\int_{-1/2}^{1/2}D_1(|s-t|)v(t)\,dt=\text{constant}.
\tag{O-90302.1}
\]

If the solution remains positive, it is also the optimizer under the required constraint \(v\ge0\).

## 2. Nyström replay

`X-90301` applies Gauss--Legendre Nyström discretization and solves the positive-definite linear system for the constant right-hand side. The sampled optimizer is positive at every tested order.

| quadrature order | simple/on-line constant | distinct constant | sampled min of optimizer |
|---:|---:|---:|---:|
| 40  | 0.868823454 | 0.934411727 | 0.643454 |
| 80  | 0.868687569 | 0.934343784 | 0.641985 |
| 160 | 0.868653090 | 0.934326545 | 0.641612 |
| 320 | 0.868644407 | 0.934322204 | positive |
| 640 | 0.868642228 | 0.934321114 | positive |

The upstream rigorously certified quartic values are

\[
0.868640,
\qquad
0.934320.
\]

The numerical optimum appears to be only a few parts in \(10^6\) larger. Thus additional scalar polynomial-window optimization for \(\xi'\) is very unlikely to produce a meaningful headline gain.

## 3. Consequence for research allocation

The high-value fronts are not:

- increasing the quartic degree by one or two;
- searching a larger scalar polynomial family without a proof architecture;
- adding co-lattice windows, which `L-90301` collapses exactly.

They are instead:

- a rigorous solution or enclosure of the Fredholm optimizer, if the last few digits matter;
- non-co-lattice or genuinely matrix-valued constraints;
- richer bandwidth-one certificates;
- new arithmetic input beyond the existing two-trace law.

## 4. Boundary

The table is floating-point reconnaissance. It neither proves optimality nor improves the certified upstream decimal. Any theorem-level improvement requires an outward-rounded Fredholm or polynomial certificate and an analytic window-admissibility proof.
