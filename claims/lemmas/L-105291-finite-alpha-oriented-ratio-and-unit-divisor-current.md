# L-105291 — Finite-α oriented ratio and the unit-charge divisor current

Claim ID: `L-105291`  
Status: **PROVED EXACT AT FINITE MEROMORPHIC SCOPE**  
Created: 2026-08-24  
Depends on: `L-105280`; PR #726 `L-105340--L-105343`  
RH status: **not assumed**

## 1. The all-pass coordinate is the finite-shifted ratio

Write

\[
F_k(t)=\Xi^{(k)}(t)=i^k\xi^{(k)}\!\left(\frac12+it\right),
\qquad s=\frac12+it.
\]

For \(\lambda>0\), put \(\alpha=\lambda^{-1}\). The companion all-pass
function of `L-105280` is

\[
\Theta_{\lambda,k}(t)
 =\frac{F_k(t)-i\lambda F_{k+1}(t)}
        {F_k(t)+i\lambda F_{k+1}(t)}.
\]

Since \(F_{k+1}=i^{k+1}\xi^{(k+1)}\), direct cancellation gives

\[
\boxed{
\Theta_{\lambda,k}(t)
 =-\left[
 \frac{\xi^{(k+1)}(s)-\alpha\xi^{(k)}(s)}
      {\xi^{(k+1)}(s)+\alpha\xi^{(k)}(s)}
 \right]^{-1}.
}
\tag{L-105291.1}
\]

Thus the conclusion-facing all-pass symbol is the **finite-α** version of the
oriented ratio of PR #726, not merely its derivative at \(\alpha=0\).
Multiplication by \(-1\) and inversion only change the harmless orientation
convention.

The functional equation

\[
\xi^{(k)}(1-s)=(-1)^k\xi^{(k)}(s)
\]

gives

\[
\boxed{
\mathcal M_{\alpha,k}(1-s)=\mathcal M_{\alpha,k}(s)^{-1}.
}
\tag{L-105291.2}
\]

Therefore the two safe lines fold exactly at every finite \(\alpha\); no
Cauchy differentiation in the shift parameter is needed to retain winding.

## 2. Unit-charge Poisson current

Let \(U\) be a rational scalar all-pass function, normalized by
\(U(\infty)=1\), with no zero or pole on the real line. Let its upper-half-plane
divisor be

\[
\nu_U=\sum_{z\in\mathbb H}
       \operatorname{ord}_z(U)\,\delta_z,
\]

where poles have negative order. Then on the real line

\[
\boxed{
J_U(x):=\frac1{2\pi i}\frac{U'(x)}{U(x)}
 =\sum_{z=a+iy\in\mathbb H}
   \operatorname{ord}_z(U)
   \frac{y}{\pi((x-a)^2+y^2)}.
}
\tag{L-105291.3}
\]

Proof: factor \(U\) into elementary all-pass factors

\[
b_z(x)=\frac{x-z}{x-\bar z}.
\]

For one factor,

\[
\frac1{2\pi i}\frac{b_z'}{b_z}
 =\frac{y}{\pi((x-a)^2+y^2)}.
\]

Products and inverses give (L-105291.3).

Integrating the Poisson kernels yields

\[
\boxed{
\int_{\mathbb R}J_U(x)\,dx
 =\nu_U(\mathbb H)
 =\operatorname{wind}U.
}
\tag{L-105291.4}
\]

Every zero or pole is counted with **unit multiplicity charge**, independent
of its distance from the real axis. This is precisely why the current sees a
near-line Blaschke slip that ordinary \(L^2\) misses.

Poisson convolution gives the exact scale law

\[
P_h*J_U(x)
 =\sum_{z=a+iy}
   \operatorname{ord}_z(U)P_{h+y}(x-a),
\tag{L-105291.5}
\]

where \(P_y(x)=y/[\pi(x^2+y^2)]\).

## 3. Relation to the Xi Gauss-law programme

PR #729 identifies a residue-weighted six-dimensional Newton source for
\(\Xi^{(r)}/\Xi^{(r+1)}\). Equation (L-105291.3) is complementary: it is the
one-dimensional boundary current of the finite-shifted all-pass ratio and
counts the shifted divisor with unit order. The two currents must not be
identified without an explicit residue-to-order conversion.

## Scope

This theorem closes the finite-shift and source-coordinate interface. It does
not bound the unit-charge divisor current. The remaining task is a
half-derivative/Carleson estimate for the complete finite-α source, including
all Blaschke factors.
