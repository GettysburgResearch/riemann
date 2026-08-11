# L-91024 — Every Cauchy storage residual is a positive mixture of causal Hardy squares

Claim ID: `L-91024`  
Status: **EXACT HARDY-SPACE FACTORIZATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91020`  
RH status: **unproved**

## 1. Positive transport representation

Retain the nonnegative densities `W_m` and scale-free storage kernels `F_m` of `L-91020`:

\[
 F_m(y)
 =(m+2)!\,y\int_0^\infty
 \frac{W_m(r)}{(y+r)^{m+3}}\,dr.
\]

For `a>0`, `r>0`, and `Re z>=0`, define

\[
 \boxed{
 \Psi_{m,a,r}(z)
 =
 \sqrt{(m+2)!W_m(r)}\,
 a^{m+2}
 \frac{z}{(z+a\sqrt r)^{m+3}}.
 }
 \tag{L-91024.1}
\]

Then, for every real `u`,

\[
 \boxed{
 F_m(u^2/a^2)
 =
 \int_0^\infty
 |\Psi_{m,a,r}(iu)|^2\,dr.
 }
 \tag{L-91024.2}
\]

### Verification

Since

\[
 |iu+a\sqrt r|^2=u^2+a^2r,
\]

the right side equals

\[
 (m+2)!a^{2m+4}u^2
 \int_0^\infty
 \frac{W_m(r)}{(u^2+a^2r)^{m+3}}\,dr,
\]

which is exactly `F_m(u^2/a^2)` after scaling the representation of `L-91020`.

Thus every cancellation order is already a source-complete continuous Gram; the isolated rational factor of `L-91020` is merely a finite spectral factor for the first nontrivial member.

## 2. Causal impulse response

Put `c=a sqrt(r)`. The elementary identity

\[
 \frac{z}{(z+c)^{m+3}}
 =
 \frac1{(z+c)^{m+2}}
 -\frac{c}{(z+c)^{m+3}}
\]

shows that the inverse Laplace transform is

\[
 \boxed{
 \psi_{m,a,r}(t)
 =
 \sqrt{(m+2)!W_m(r)}\,a^{m+2}e^{-ct}
 \left[
 \frac{t^{m+1}}{(m+1)!}
 -c\frac{t^{m+2}}{(m+2)!}
 \right]
 \mathbf1_{t\ge0}.
 }
 \tag{L-91024.3}
\]

The impulse is causal, exponentially decaying, and satisfies

\[
 \boxed{
 \int_0^\infty\psi_{m,a,r}(t)\,dt=0.
 }
 \tag{L-91024.4}
\]

The zero integral follows from the equality of the two Gamma integrals. It is the physical-space form of the numerator zero at `z=0`.

Moreover,

\[
 \Psi_{m,a,r}(z)=O(|z|^{-m-2})
 \qquad(|z|\to\infty,\ \Re z\ge0).
\]

Each higher storage order therefore gains one additional degree of high-frequency decay.

## 3. Continuous state space

Let

\[
 \mathcal H_m=L^2((0,\infty),dr).
\]

For a real spectral coordinate `u`, define

\[
 \mathbf\Psi_{m,a}(u)(r)=\Psi_{m,a,r}(iu).
\]

Then

\[
 \boxed{
 F_m(u^2/a^2)
 =\|\mathbf\Psi_{m,a}(u)\|_{\mathcal H_m}^2.
 }
 \tag{L-91024.5}
\]

For any finite critical-line packet `(u_j,c_j)`,

\[
 \sum_{j,k}c_j\overline{c_k}
 \int_0^\infty
 \Psi_{m,a,r}(iu_j)
 \overline{\Psi_{m,a,r}(iu_k)}\,dr
 =
 \int_0^\infty
 \left|\sum_jc_j\Psi_{m,a,r}(iu_j)\right|^2dr
 \ge0.
\]

Thus the entire critical-line residual matrix has an exact continuous Hardy-space Gram.

## 4. Coefficient-one scale recurrence

The normalized recurrence of `L-91020` becomes

\[
 \boxed{
 \widetilde D_a^{(m)}(u)
 =
 \widetilde D_{2a}^{(m)}(u)
 +a^{-2(m+2)}
 \|\mathbf\Psi_{m+1,a}(u)\|_{\mathcal H_{m+1}}^2.
 }
 \tag{L-91024.6}
\]

The inherited state returns with coefficient exactly one, and the innovation is one explicit causal Hardy-space output.

## 5. Consequence for the production theorem

The remaining Cauchy–Jordan theorem no longer needs to discover a spectral factor or a positive target space. Both are canonical:

```text
source space:
  divisor-splitting Stinespring flow of L-91021;

target space at order m:
  L2(dr) of the causal filters Psi_(m,a,r);

required map:
  a completed source-to-target contraction preserving vertical phases,
  logarithmic coproducts, and the coefficient-one returned state.
```

The only unresolved issue is the completed arithmetic/archimedean boundary coupling.

## 6. Boundary

```text
positive mixture representation                 EXACT
causal impulse formula                           EXACT
zero total mass                                  EXACT
continuous Hardy Gram                            EXACT
coefficient-one target recurrence                EXACT
completed source-to-Hardy intertwiner            OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```