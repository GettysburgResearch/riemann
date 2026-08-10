# Confluent cluster renormalization for finite Weil interpolation

**Status:** `PROPOSED NATIVE THEOREM / EXACT FINITE HILBERT-SPACE ALGEBRA`

This note continues `FINITE_OFFLINE_ISOLATION.md`. The raw evaluation Gram of a packet of nearby zero coordinates becomes badly conditioned when coordinates coalesce. That degeneration is not, by itself, a new obstruction: after the canonical Newton divided-difference change of coordinates, every finite cluster converges to a positive confluent jet Gram.

The theorem identifies the genuinely invariant scale of off-line-pair capture. For a reflected pair at centered depth `y`, the unit-value cardinal cost grows like `y^(-2)`, but the depth-normalized target has a finite limit and its negative Weil value is exactly of order `y^2`. Thus the correct competition is

```text
far-tail / corrected-floor radius
versus
pair depth squared,
```

not the raw smallest eigenvalue of an unrenormalized Vandermonde-type Gram.

RH is not proved here.

## 1. The analytic evaluation kernel

Let `I` be a bounded real interval, let `v in L^1(I)` be nonnegative and positive almost everywhere on a nonempty subinterval, and fix `L>0`. Put

\[
 K(z,w)
 :=L\int_I v(u)e^{i(z-\overline w)u}\,du.
 \tag{CC1}
\]

This is the complete-critical-frame evaluation kernel used in the Zeta23 finite-isolation packet. For every finite set of distinct coordinates `Z={z_1,...,z_n}`, the matrix

\[
 K_Z=(K(z_i,z_j))_{i,j}
\]

is positive definite.

## 2. One cluster and Newton coordinates

Fix distinct complex numbers

\[
 \xi_0,\ldots,\xi_{r-1}
\]

and a cluster centre `z_0`. For `epsilon != 0` put

\[
 z_j(\epsilon)=z_0+\epsilon\xi_j.
\]

For a function `f` analytic near the cluster define the Newton divided-difference coordinates

\[
 \mathcal D_a^{\epsilon}f
 :=[z_0+\epsilon\xi_0,\ldots,z_0+\epsilon\xi_a]f,
 \qquad 0\le a<r.
 \tag{CC2}
\]

Equivalently,

\[
 \mathcal D_a^{\epsilon}f
 =\sum_{k=0}^a
 {f(z_0+\epsilon\xi_k)
  \over
  \prod_{0\le \ell\le a,\,\ell\ne k}
  \epsilon(\xi_k-\xi_\ell)}.
 \tag{CC3}
\]

Let `T_epsilon` be the lower-triangular matrix implementing `(CC3)` on the vector of point evaluations. The divided-difference Gram is

\[
 K_\epsilon^{\Delta}
 :=T_\epsilon K_{Z(\epsilon)}T_\epsilon^*.
 \tag{CC4}
\]

### Theorem 2.1 — confluent limit

As `epsilon -> 0`, entrywise and in operator norm,

\[
 \boxed{
 K_\epsilon^{\Delta}\longrightarrow J_r(z_0),
 }
 \tag{CC5}
\]

where

\[
 \boxed{
 J_r(z_0)_{ab}
 ={1\over a!b!}
 \partial_z^a\partial_{\overline w}^bK(z,w)
 \big|_{z=w=z_0}
 = {L\over a!b!}
 \int_I v(u)(iu)^a(-iu)^b e^{-2\operatorname{Im}(z_0)u}\,du.
 }
 \tag{CC6}
\]

#### Proof

For every analytic `f`, the standard confluent divided-difference limit is

\[
 [z_0+\epsilon\xi_0,\ldots,z_0+\epsilon\xi_a]f
 \longrightarrow {f^{(a)}(z_0)\over a!}.
\]

Apply this first in `z` and then anti-analytically in `w` to `K(z,w)`. Since the packet is finite, entrywise convergence implies operator-norm convergence. Differentiating `(CC1)` under the integral gives `(CC6)`. `square`

### Theorem 2.2 — the jet Gram is strictly positive

For every finite `r`,

\[
 \boxed{J_r(z_0)>0.}
 \tag{CC7}
\]

#### Proof

For `alpha in C^r`,

\[
 \alpha^*J_r(z_0)\alpha
 =L\int_I v(u)e^{-2\operatorname{Im}(z_0)u}
 \left|\sum_{a=0}^{r-1}{\alpha_a(iu)^a\over a!}\right|^2du.
 \tag{CC8}
\]

If this vanishes, the displayed polynomial vanishes on a set of positive measure and hence identically. Thus every `alpha_a=0`. `square`

Consequently there are `epsilon_0>0` and `c>0`, depending only on the fixed finite cluster data, such that

\[
 K_\epsilon^{\Delta}\ge cI
 \qquad(0<|\epsilon|<\epsilon_0).
 \tag{CC9}
\]

The raw Gram `K_{Z(epsilon)}` may have eigenvalues tending rapidly to zero; `(CC9)` shows that this is exactly the singular scaling of point-evaluation coordinates, not loss of the underlying finite jet interpolation geometry.

## 3. Several finite clusters

Let `z_1^0,...,z_q^0` be distinct centres, and at centre `z_c^0` let there be `r_c` nodes

\[
 z_{c,j}(\epsilon)=z_c^0+\epsilon\xi_{c,j}
 \qquad(0\le j<r_c).
\]

Apply the Newton transformation separately inside each cluster. The transformed Gram converges to the block confluent Gram whose rows are the functionals

\[
 f\longmapsto {f^{(a)}(z_c^0)\over a!},
 \qquad 1\le c\le q,\quad 0\le a<r_c.
 \tag{CC10}
\]

### Theorem 3.1 — finite exponential jets are independent

The multi-cluster confluent Gram is positive definite.

#### Proof

Its quadratic form is

\[
 L\int_Iv(u)
 \left|
 \,\sum_{c=1}^q e^{iz_c^0u}
       \sum_{a=0}^{r_c-1}\alpha_{c,a}{(iu)^a\over a!}
 \right|^2du.
 \tag{CC11}
\]

If it vanishes, the exponential polynomial in `(CC11)` vanishes on an interval and therefore identically. Exponential polynomials with distinct exponents and finite polynomial multiplicities are linearly independent; equivalently, they form the solution basis of a constant-coefficient ODE and have a nonsingular confluent Vandermonde Wronskian. Hence every coefficient is zero. `square`

Thus **no fixed finite collection of finite-order clusters can produce an invariant Gram collapse after canonical confluent renormalization**.

## 4. Reflected pair and the depth-normalized target

Take a reflected pair

\[
 z_-=x-iy,
 \qquad
 z_+=x+iy,
 \qquad y>0,
 \tag{CC12}
\]

of multiplicity `m`. The unit cardinal target of `FINITE_OFFLINE_ISOLATION.md` is

\[
 t^{\rm unit}=(1,-1).
\]

Define instead the depth-normalized target

\[
 \boxed{t_y=(-iy,iy)=(-iy)t^{\rm unit}.}
 \tag{CC13}
\]

In the Newton coordinates ordered as `(z_-,z_+)`,

\[
 t_y\longmapsto
 \left(-iy,{iy-(-iy)\over2iy}\right)=(-iy,1)
 \longrightarrow(0,1).
 \tag{CC14}
\]

Let nuisance coordinates be included and transformed clusterwise as in Section 3. Suppose the total confluent packet is fixed and finite. Then the minimum coefficient-norm capture cost

\[
 C_y:=t_y^*K_Z^{-1}t_y
 \tag{CC15}
\]

has a finite positive limit:

\[
 \boxed{
 C_y\longrightarrow C_{\rm jet}
 =e_{\rm der}^*J_{\rm confluent}^{-1}e_{\rm der}
 \in(0,\infty).
 }
 \tag{CC16}
\]

Since `t_y=(-iy)t_unit`,

\[
 \boxed{
 y^2 C_Z(t^{\rm unit})\longrightarrow C_{\rm jet}.
 }
 \tag{CC17}
\]

The apparent `y^(-2)` explosion of the unit cardinal cost is therefore precisely the cost of demanding an order-one jump across two points separated by `2y`; the invariant derivative target is regular.

For the reflected Weil block `(a,b) -> 2m Re(a conjugate(b))`, the target `(CC13)` gives

\[
 \boxed{
 W_{\rm pair}(t_y,t_y)
 =2m\operatorname{Re}[(-iy)\overline{(iy)}]
 =-2my^2.
 }
 \tag{CC18}
\]

Thus the negative moat and the stable capture target scale by the same natural depth square.

## 5. Depth-tail-floor capture law

Let the localized compression be

\[
 G=G_Z+E_{\rm far},
 \qquad \|E_{\rm far}\|\le\epsilon,
 \tag{CC19}
\]

and suppose an arithmetic argument supplies the corrected floor

\[
 G\ge-\delta I.
 \tag{CC20}
\]

The minimum-norm interpolant for `t_y` satisfies

\[
 c_y^*Gc_y
 \le -2my^2+\epsilon C_y,
 \qquad
 c_y^*Gc_y\ge-\delta C_y.
\]

Hence every surviving off-line pair must obey

\[
 \boxed{
 2my^2\le(\epsilon+\delta)C_y.
 }
 \tag{CC21}
\]

For a fixed finite confluent packet, `(CC16)` gives the invariant criterion

\[
 \boxed{
 \epsilon+\delta
 < {2m\over C_{\rm jet}+o(1)}y^2
 \quad\Longrightarrow\quad
 \text{a strict negative full-Weil direction}.
 }
 \tag{CC22}
\]

For the uniform control window `v=1` on `[-1/2,1/2]`, `L=1`, one has

\[
 J_2(0)=\begin{pmatrix}1&0\\0&1/12\end{pmatrix},
 \qquad C_{\rm jet}=12.
 \tag{CC23}
\]

Equivalently, the exact two-point formula

\[
 C_Z(t^{\rm unit})={2\over r_y-1},
 \qquad r_y={\sinh y\over y},
\]

gives

\[
 y^2C_Z(t^{\rm unit})\to12.
 \tag{CC24}
\]

## 6. Refined interpretation of the Gram-collapse alternative

`FINITE_OFFLINE_ISOLATION.md` showed that a vanishing corrected floor and tail can coexist with an off-line pair only if a raw local evaluation Gram becomes ill-conditioned. The present theorem refines that statement:

> Raw Gram collapse caused by any fixed finite coalescing packet is removable by the canonical divided-difference transformation. In invariant coordinates the packet converges to a strictly positive jet Gram.

Therefore a counterexample can evade a hierarchy with `epsilon_j+delta_j=o(y^2)` only through a genuinely noncompact mechanism, for example:

```text
unbounded local cluster order;
unboundedly many nuisance constraints in the active packet;
loss of localization/tail control under the confluent basis;
or failure of the corrected floor itself.
```

Finite near-collisions and finite multiplicity are not independent escape mechanisms.

This does not yet exclude unbounded local packet complexity. The classical bound

\[
 N(t+1)-N(t)\ll\log(t+3)
\]

still allows the required jet order to grow with height, and controlling that growth against the tail/floor radii is the remaining quantitative problem.

## 7. Scope boundary

Proved here:

- canonical divided-difference renormalization of every finite cluster;
- operator-norm convergence to an explicit positive jet Gram;
- positivity for arbitrary finite collections of finite-order clusters;
- exact `y^(-2)` unit-cardinal scaling for a near-line reflected pair;
- a finite depth-tail-floor capture criterion;
- elimination of finite coalescence as an invariant Gram-collapse obstruction.

Not proved here:

- a uniform lower bound as total cluster order tends to infinity;
- a quantitative tail theorem in the confluent basis at order `O(log T)`;
- a corrected-kernel floor;
- RH.
