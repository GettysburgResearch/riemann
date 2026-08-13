# L-91413 — The infinite completed Gamma–Beta reservoir exists and retains dimension-free coercivity

Claim ID: `L-91413`  
Status: **EXACT CONDITIONAL INFINITE-PRODUCT DIRICHLET-FORM THEOREM**  
Created: 2026-08-13  
Depends on: `L-91411`; PR #401 `L-91107`  
RH status: **unproved**

## 1. Infinite conditional reservoir

Let `(w_i)_(i>=1)` be positive and summable:

\[
A=\sum_{i\ge1}w_i<\infty.
\]

Let

\[
\rho(v)=\frac34(1-v^2)\mathbf1_{(-1,1)}(v)
\]

and let `nu=rho^(tensor infinity)` be the product reference law. Since `|v_i|<1`,

\[
D(v)=\sum_{i\ge1}w_iv_i
\]

converges absolutely and uniformly on the product cube. Define

\[
H(v)=(A^2-D(v)^2)^{1/4},
\qquad
Z=\int H\,d\nu,
\]

and

\[
\boxed{
d\mu(v)=Z^{-1}H(v)d\nu(v).
}
\tag{L-91413.1}
\]

The factor is bounded by `A^(1/2)`. It is positive `nu`-almost surely: equality `|D|=A` forces every coordinate with positive weight to equal the same endpoint `+1` or `-1`, a product-null event. Hence

\[
0<Z<\infty.
\]

This is the infinite conditioned Beta reservoir of the BPY two-copy completion.

## 2. Uniform convergence of finite completed tilts

Put

\[
A_m=\sum_{i\le m}w_i,
\qquad
D_m=\sum_{i\le m}w_iv_i,
\qquad
H_m=(A_m^2-D_m^2)^{1/4},
\]

and let

\[
R_m=A-A_m.
\]

Uniformly on the product cube,

\[
|D-D_m|\le R_m.
\]

Moreover

\[
\begin{aligned}
|(A^2-D^2)-(A_m^2-D_m^2)|
&\le (A+A_m)R_m+(|D|+|D_m|)R_m\\
&\le4AR_m.
\end{aligned}
\]

For nonnegative `x,y`,

\[
|x^{1/4}-y^{1/4}|\le|x-y|^{1/4}.
\]

Therefore

\[
\boxed{
\|H-H_m\|_\infty
\le(4AR_m)^{1/4}
\longrightarrow0.
}
\tag{L-91413.2}
\]

Writing `Z_m=int H_m dnu`, one has `Z_m->Z`, and the finite completed measures

\[
d\mu_m=Z_m^{-1}H_m\,d\nu
\]

converge to `mu` in total variation. Here `mu_m` is extended trivially over the tail coordinates.

## 3. Cylinder Dirichlet form

For a smooth cylinder function `f`, define

\[
\boxed{
\mathcal E(f,f)
=\frac14\sum_{i\ge1}
 \int(1-v_i^2)|\partial_if|^2d\mu,
}
\tag{L-91413.3
}

where the sum is finite on the cylinder core.

For `m` larger than the support of `f`, let

\[
\mathcal E_m(f,f)
=\frac14\sum_{i\le m}
 \int(1-v_i^2)|\partial_if|^2d\mu_m.
\]

Total-variation convergence and boundedness of the cylinder derivatives give

\[
\boxed{
\operatorname{Var}_{\mu_m}(f)	o\operatorname{Var}_\mu(f),
\qquad
\mathcal E_m(f,f)	o\mathcal E(f,f).
}
\tag{L-91413.4
}

The same convergence holds for bounded cylinder entropies.

## 4. Dimension-free Poincaré and logarithmic Sobolev bounds

`L-91411` proves for every finite completed reservoir

\[
\operatorname{Var}_{\mu_m}(f)
\le2\mathcal E_m(f,f).
\]

Passing to the limit in (L-91413.4),

\[
\boxed{
\operatorname{Var}_\mu(f)
\le2\mathcal E(f,f)
}
\tag{L-91413.5
}

for every smooth cylinder function.

The same Hessian lower bound `nabla^2U>=2I` gives the finite logarithmic Sobolev inequality

\[
\operatorname{Ent}_{\mu_m}(f^2)
\le4\mathcal E_m(f,f).
\]

Hence

\[
\boxed{
\operatorname{Ent}_\mu(f^2)
\le4\mathcal E(f,f)
}
\tag{L-91413.6
}

on the cylinder core.

## 5. Closability

The density `H/Z` is strictly positive almost everywhere. For each integer `r>=1`, let

\[
\Omega_r=\{v:H(v)>1/r\}.
\]

The sets increase to full `mu`-measure. On every finite-coordinate cylinder intersected with `Omega_r`, the measure `mu` is locally equivalent, with density bounded above and below, to the product Jacobi measure. The coordinate gradient is closable there.

Suppose `f_n` is cylinder, `f_n->0` in `L^2(mu)`, and the gradients are Cauchy in the norm induced by (L-91413.3). Restriction to every `Omega_r` and finite coordinate block forces the limiting gradient to vanish. Letting `r->infinity` shows that it vanishes `mu`-almost everywhere. Thus the form is closable.

Denote its Friedrichs closure again by `(E,D(E))`. Inequalities (L-91413.5)--(L-91413.6) extend by closure.

## 6. Infinite Poisson solution

Let `L` be the nonpositive self-adjoint generator associated with the closed form. Its mean-zero spectrum lies in

\[
(-\infty,-1/2].
\]

Consequently, for every mean-zero `g in L^2(mu)`, the Poisson equation

\[
-\mathcal Lh=g,
\qquad \mathbb E_\mu h=0,
\]

has the unique solution `h=(-L)^(-1)g` satisfying

\[
\boxed{
\|h\|_2\le2\|g\|_2,
\qquad
\mathcal E(h,h)
=\langle g,(-\mathcal L)^{-1}g\rangle
\le2\|g\|_2^2.
}
\tag{L-91413.7
}

The logarithmic Sobolev inequality also supplies dimension-free concentration and uniform integrability for cylinder approximants.

## 7. Application to the BPY Gamma mixture

In the BPY two-copy representation,

\[
w_n=\frac{G_n}{\pi^2n^2},
\qquad G_n\sim\Gamma(4,1).
\]

Since

\[
\mathbb E\sum_nw_n
=\frac4{\pi^2}\sum_n\frac1{n^2}<\infty,
\]

one has `sum_n w_n<infinity` almost surely. Therefore Sections 1--6 apply for almost every Gamma reservoir.

The finite completed Beta Poisson problems of `L-91409/L-91411` pass to one well-defined infinite conditional problem with the same gap and Poisson constants. The remaining Brownian/theta gate is not analytic existence, loss of coercivity, or a divergent Beta tail. It is the exact source-specific boundary identity for

\[
\mathbb E[\Gamma(h_Z,Z)\mid Z]
\]

and its coupling to the theta variance square.

This theorem is conditional on the Gamma variables. It does not assert a spectral gap in the Gamma directions or solve the fully mixed Gamma–Beta generator.

## 8. Proof boundary

```text
infinite completed Beta law                    EXACT
uniform finite-to-infinite density convergence EXACT
closed infinite Jacobi Dirichlet form          EXACT
Poincare gap at least 1/2                      EXACT
logarithmic Sobolev constant at most 4         EXACT
infinite conditional Poisson solution          EXACT
Gamma-mixture applicability almost surely      EXACT
Theta/DtN boundary-port identification         OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
