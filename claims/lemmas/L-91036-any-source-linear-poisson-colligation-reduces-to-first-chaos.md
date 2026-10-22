# L-91036 — Any source-linear positive Poisson colligation reduces to first chaos

Claim ID: `L-91036`  
Status: **PROPOSED COMPLETE POISSON-CHAOS LINEARITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: main `L-91029`, branch `L-91030`, `L-91033`  
RH status: **unproved**

## 1. Motivation

The Guinand--Weil prime channel is linear in the von Mangoldt source.  The full
compound-Poisson Fock covariance is nonlinear in the intensity: it contains
every Wiener--Itô chaos.  A positive-metric colligation cannot use cancellation
between different chaos orders.

This lemma proves that any product-system-compatible completion of a
source-linear target is forced into the compensated first chaos.  The full
bosonic Fock space remains the natural dilation, but higher chaoses cannot be
the missing sign mechanism.

## 2. Intensity scaling

Let `nu` be a finite positive measure and let `N_r` be a Poisson random measure
with intensity `r nu`, `r>=0`.  Put

\[
 S_r=\int u\,N_r(du),
 \qquad
 \eta_x^{(r)}=e^{-ixS_r}.
 \tag{L-91036.1}
\]

For

\[
 h_x(u)=e^{-ixu}-1,
\]

the centered phase covariance is

\[
\begin{aligned}
 \Sigma_r(x,y)
 &:=\left\langle
  \eta_x^{(r)}-\mathbb E\eta_x^{(r)},
  \eta_y^{(r)}-\mathbb E\eta_y^{(r)}
 \right\rangle\\
 &=M_r(x)\overline{M_r(y)}
 \left[
  e^{r\langle h_x,h_y\rangle_{L^2(\nu)}}-1
 \right].
\end{aligned}
\tag{L-91036.2}

After removal of the harmless scalar coherent factors, its chaos expansion is

\[
 \boxed{
 e^{r\langle h_x,h_y\rangle}-1
 =\sum_{m\ge1}
  \frac{r^m}{m!}
  \langle h_x,h_y\rangle^m.
 }
 \tag{L-91036.3}
\]

Each kernel

\[
 \left(\langle h_{x_j},h_{x_k}\rangle^m\right)_{j,k}
\]

is positive semidefinite by the Schur product theorem.  It is the Gram of the
`m`-th symmetric chaos vectors `h_x^(tensor m)`.

## 3. Positive coefficient comparison

Let a product-system-compatible positive colligation assign to each intensity
`r` an output feature vector

\[
 Y_x^{(r)}=\bigoplus_{m\ge1}r^{m/2}Y_{m,x}
 \tag{L-91036.4}
\]

in mutually orthogonal chaos/output sectors.  Its kernel is

\[
 \boxed{
 K_r(x,y)
 =\sum_{m\ge1}r^m K_m(x,y),
 \qquad
 K_m(x,y)=\langle Y_{m,x},Y_{m,y}\rangle\succeq0.
 }
 \tag{L-91036.5}
\]

Assume the target is exactly source-linear:

\[
 \boxed{K_r=rK_1\quad\text{for every }r\ge0.}
 \tag{L-91036.6}
\]

Then for every finite carrier packet and every coefficient vector `c`,

\[
 0=\sum_{m\ge2}r^m c^*K_mc
 \qquad(r\ge0).
\]

Every summand is nonnegative.  Therefore

\[
 c^*K_mc=0
 \quad(m\ge2)
\]

for every `c`, and hence

\[
 \boxed{K_m=0\quad(m\ge2).}
 \tag{L-91036.7}
\]

Equivalently, every higher-chaos output vector vanishes.

## 4. First-chaos factorization

The surviving source space is

\[
 \boxed{\mathfrak h_1=L^2(\nu).}
 \tag{L-91036.8}
\]

The carrier defects are the explicit vectors

\[
 h_x(u)=e^{-ixu}-1.
 \tag{L-91036.9}
\]

Any source-linear conservative completion must therefore have the form

\[
 \boxed{
 Y_x=\mathcal C h_x
 }
 \tag{L-91036.10}
\]

for one contraction or isometry `C` from the one-particle source space into the
completed output reserve, after adjoining any separate archimedean/pole input
space.

Thus the actual CJHI problem is not

```text
full Poisson Fock -> one Hardy port.
```

It is

```text
compensated prime first chaos
+ completed archimedean first chaos
-> delayed causal/anti-causal Hardy reserve.
```

The higher Poisson chaoses provide the canonical Stinespring dilation and
independent-increment bookkeeping, but no additional positive source budget.

## 5. Application to the generalized-Jordan source

For main's positive measure

\[
 \nu_{a,\sigma}
 =\sum_{p,k}
  \frac{1-p^{-2ak}}{kp^{k\sigma}}
  \delta_{k\log p},
 \tag{L-91036.11}
\]

the one-particle vectors are

\[
 h_x(k\log p)=p^{-ikx}-1.
 \tag{L-91036.12}
\]

The carré du champ of main `L-91029` is exactly their first-chaos Gram.
Logarithmic jets multiply these vectors by powers of `k log p`; no higher
Poisson chaos is required to produce any finite source jet.

The corrected output target is the delayed two-sided Hardy family of
`L-91034`.  Therefore the conclusion-producing operator is one first-chaos
intertwiner

\[
 \boxed{
 \mathcal C_a:
 \mathcal H_{\Gamma,\mathrm{pole}}^{(1)}
 \oplus L^2(\nu_{a,\sigma})
 \longrightarrow
 \mathcal H_{\mathrm{Hardy}}^{\rm del}
 \oplus\mathcal E^{(1)}.
 }
 \tag{L-91036.13}
\]

Its transfer on every carrier/delay packet must reproduce the completed screw
kernel, with no signed remainder.

## 6. Scope of the theorem

The reduction uses two structural assumptions that a genuine source-ordered
colligation should satisfy:

1. naturality under the intensity semigroup `r -> r nu`;
2. orthogonality of the Wiener--Itô chaos grading, or an equivalent
   independent-increment product-system decomposition.

An arbitrary isometry built after fixing `r=1` need not display this grading.
Such an existential factorization would merely take a square root of the target
kernel and would not count as an explicit source construction.

The theorem does not prove that `C_a` exists.  Its existence with the required
completed transfer kernel remains RH-bearing.

## 7. Strategic consequence

The remaining search space is substantially reduced:

```text
not an infinite nonlinear Fock ansatz;
not cancellation among chaos orders;
not additional finite source ports;

but one explicit one-particle contraction
between two completely specified Hilbert spaces.
```

Suzuki's operator of `L-91035` gives the corresponding amplitude-level unitary.
The missing map is its tangent/conditional-negative-type lift.

## 8. Verification

The retained regression verifies the expansion

\[
 e^{rz}-1=rz+\frac12r^2z^2+O(r^3)
\]

at high precision and records the nonzero second-chaos coefficient for a
finite control.  The theorem itself is algebraic.

## 9. Exact boundary

```text
compound-Poisson all-chaos dilation                  EXACT
positive chaos kernels                               EXACT
source-linear target -> first-chaos reduction        PROPOSED COMPLETE
full Fock higher-chaos rescue                        CLOSED
explicit first-chaos completed contraction           OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
