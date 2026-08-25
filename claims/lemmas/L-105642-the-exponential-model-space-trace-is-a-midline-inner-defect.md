# L-105642 — The exponential model-space trace is an exact midline inner defect

Claim ID: `L-105642`  
Status: **PROVED EXACT FINITE MODEL-SPACE TRACE THEOREM**  
Created: 2026-08-25  
Depends on: `L-105630--L-105631`; standard upper-half-plane model-space theory  
RH status: **not assumed**

## 1. Paley–Wiener normalization

Use the unitary Paley–Wiener map

\[
F(z)={1\over\sqrt{2\pi}}
\int_0^\infty f(\xi)e^{iz\xi}\,d\xi
\]

from `L^2(0,infinity)` onto `H^2(C_+)`. For `z=x+i eta`, the reproducing
vector in the frequency coordinate is

\[
\boxed{
k_z(\xi)={1\over\sqrt{2\pi}}
 e^{-i\overline z\xi},
\qquad
\|k_z\|^2={1\over4\pi\eta}.
}
\tag{L-105642.1}

Fix `H>0` and put `eta=H/2`. Fourier inversion gives the continuous resolution

\[
\boxed{
\int_{\mathbb R}|k_{x+iH/2}\rangle
\langle k_{x+iH/2}|\,dx
=M_{e^{-H\xi}}.
}
\tag{L-105642.2}

The integral is understood weakly. It follows directly because the integral
of `exp(-ix(xi-zeta))` is the delta distribution and the two Poisson damping
factors multiply to `exp(-H xi)` on the diagonal.

## 2. Exact finite inner trace

Let `B` be a finite Blaschke product in the upper half-plane and let

\[
K_B=H^2\ominus BH^2.
\]

The model-space reproducing kernel satisfies

\[
\boxed{
\|P_{K_B}k_z\|^2
=(1-|B(z)|^2)\|k_z\|^2.
}
\tag{L-105642.3}

Compressing (L-105642.2) to the finite-dimensional space `K_B`, taking the
trace, and using (L-105642.1)--(L-105642.3) yields

\[
\boxed{
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
={1\over2\pi H}
\int_{\mathbb R}
\left(1-|B(x+iH/2)|^2\right)dx.
}
\tag{L-105642.4}

This is an exact identity. The continuum multiplication operator need not be
trace class on the whole Hardy space; only its finite model-space compression
is traced.

## 3. One zero has an exact depth price

For

\[
b=a+iy,
\qquad y>0,
\qquad
B_b(z)={z-b\over z-\overline b},
\]

one has

\[
1-|B_b(x+i\eta)|^2
={4\eta y\over(x-a)^2+(\eta+y)^2}.
\tag{L-105642.5}

Taking `eta=H/2` in (L-105642.4) gives

\[
\boxed{
\operatorname{tr}_{K_{B_b}}M_{e^{-H\xi}}
={2y\over H+2y}.
}
\tag{L-105642.6}

This agrees with the direct Paley–Wiener model vector

\[
\phi_b(\xi)=\sqrt{2y}e^{-y\xi}e^{-ia\xi},
\]

because

\[
\int_0^\infty e^{-H\xi}|\phi_b(\xi)|^2d\xi
={2y\over H+2y}.
\]

The charge is independent of the horizontal position `a` and depends only on
the zero depth `y` below the shifted boundary.

## 4. A finite zero packet

Let

\[
B=\prod_{j=1}^m B_{b_j}
\]

with multiplicities repeated. Since `0<=|B_(b_j)(z)|^2<=1`,

\[
1-|B(z)|^2
=1-\prod_j|B_{b_j}(z)|^2
\le
\sum_j\left(1-|B_{b_j}(z)|^2\right).
\]

Therefore

\[
\boxed{
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
\le
\sum_{j=1}^m{2y_j\over H+2y_j}
\le
{2\over H}\sum_{j=1}^m y_j.
}
\tag{L-105642.7}

The first inequality preserves the complete model-space geometry while giving
a source-independent upper price. The second converts it to a linear depth
budget.

## 5. Layer-cake form

Let

\[
N_B(t)=\#\{j:y_j>t\}
\]

with multiplicity. Then

\[
\sum_jy_j=\int_0^\infty N_B(t)\,dt,
\]

so

\[
\boxed{
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
\le
{2\over H}
\int_0^\infty N_B(t)\,dt.
}
\tag{L-105642.8}

Thus an exponential source metric prices a zero packet by the area under its
vertical-depth counting function.

## 6. Meaning and scope

Equation (L-105642.4) identifies the exponential source charge with a literal
midline defect of the inner function. It is compatible with the signed
Paley–Wiener/model-space ledgers on sibling PR #731, but it is not an
unweighted degree theorem.

A boundary-near Blaschke factor has degree one while its charge
`2y/(H+2y)` tends to zero with `y`. Therefore small weighted charge cannot by
itself exclude a topological zero. That firewall is recorded separately in
`R-105640`.