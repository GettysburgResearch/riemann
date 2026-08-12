# L-91421 — The fixed Cauchy node diagonalizes every translation and compensation port

Claim ID: `L-91421`  
Status: **PROVED EXACT ONE-NODE SOURCE REDUCTION; ANNULAR EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: corrected `L-91412`, `L-91414/L-91415` on the parity sibling branch  
RH status: **unproved**

## 1. The normalized Cauchy vector

For a fixed interior node `eta>0`, put

\[
 \boxed{
 r_\eta(t)=\sqrt{2\eta}\,e^{-\eta t}\mathbf1_{t>0}.
 }
 \tag{L-91421.1}

Then

\[
 \|r_\eta\|_{L^2(0,\infty)}=1.
 \]

For the physical backward translation

\[
 (S_uf)(t)=f(t+u),
 \qquad u>0,
\]

one has the exact eigenvector identity

\[
 \boxed{
 S_ur_\eta=e^{-\eta u}r_\eta.
 }
 \tag{L-91421.2}

## 2. Parity ports become scalars

For the endpoint pair

\[
 U(u)=S_ur_\eta,
 \qquad
 V(u)=r_\eta,
\]

the Hadamard ports are

\[
 \boxed{
 E_\eta(u)
 =\frac{1+e^{-\eta u}}{\sqrt2}r_\eta,
 \qquad
 O_\eta(u)
 =-\frac{1-e^{-\eta u}}{\sqrt2}r_\eta.
 }
 \tag{L-91421.3}

Consequently

\[
 -\langle U(u),V(u)\rangle
 -\langle V(u),U(u)\rangle
 =-2e^{-\eta u}
 \tag{L-91421.4}

and

\[
 \|O_\eta(u)\|^2-\|E_\eta(u)\|^2
 =-2e^{-\eta u}.
 \tag{L-91421.5}

Every translation port at the one-node input is therefore a scalar Laplace
weight.

In particular

\[
 \|O_\eta(u)\|\le\|E_\eta(u)\|,
 \tag{L-91421.6}

\]

so the adverse long-channel odd port is automatically dominated by its
favourable even partner on this one-dimensional subspace.

## 3. Singular short-jump compensation

On the short source `0<u<kappa`, corrected `L-91412` has

\[
 C=r_\eta,
 \qquad
 \widetilde U(u)=S_ur_\eta-r_\eta
 =(e^{-\eta u}-1)r_\eta.
 \tag{L-91421.7}

The connection vector is

\[
 \boxed{
 J_\eta
 =j_\eta r_\eta,
 \qquad
 j_\eta
 =\int_0^\kappa
  (e^{-\eta u}-1)d\mathfrak M_{\rm c}^+(u).
 }
 \tag{L-91421.8}

The integral converges because the integrand is `O(u)` and the measure is
`du/(2u)+O(du)`.

Thus the full compensated short ledger is the scalar

\[
 \boxed{
 \int_0^\kappa
  |e^{-\eta u}-1|^2d\mathfrak M_{\rm c}^+(u)
 +|1-j_\eta|^2-1-|j_\eta|^2,
 }
 \tag{L-91421.9
}

plus the explicit Nakamura-versus-translation connection of `L-91412`.
No infinite-dimensional source ambiguity remains at one node.

## 4. Safe fixed-node Green alignment

For the horizontal Xi quotient

\[
 \Theta_a(z)
 =\frac{\xi(\frac12-a+z)}
        {\xi(\frac12+a+z)},
 \qquad 0<a\le\frac12,
 \tag{L-91421.10}

choose the fixed node

\[
 \boxed{\eta=1.}
 \tag{L-91421.11}

Then

\[
 \Theta_a(1)
 =\frac{\xi(\frac32-a)}
        {\xi(\frac32+a)}.
 \tag{L-91421.12}

Put

\[
 q_a=\frac12-a\ge0.
 \tag{L-91421.13}

For `a<1/2`, the completed one-Green ratio satisfies

\[
 \boxed{
 \Theta_a(1)
 =q_a\mathcal H_{2a}(q_a)
 =\left\|
   \sqrt{q_a}e^{-q_at/2}
  \right\|_{L^2(\mu_{2a})}^2.
 }
 \tag{L-91421.14}

At `a=1/2`, this has the finite pole-aligned limit described by
`L-91318` on PR #403.  Hence the entire dyadic path of `L-91420` uses one fixed
model node and explicit safe positive Green vectors.

## 5. One-node completed Green scalar

Evaluate the exact completed source identity of `T-91402` on the Cauchy input
`r_eta`, together with its reflected and bridge components.  Denote the
resulting scalar by

\[
 \Delta_a(\eta).
 \tag{L-91421.15}

Every source integral is now a Laplace transform of the completed base measure,
and every connection term is a finite evaluation of the six safe xi jets of
`L-91407`.  Therefore

\[
 \boxed{
 \Delta_a(\eta)
 }
 \tag{L-91421.16}

is an explicit scalar assembled from

```text
xi'/xi and its first derivative at safe points;
finite rational residue coefficients;
short compensated Laplace transforms;
long and prime Laplace transforms;
compressed-delay and bridge scalars.
```

By the source identity,

\[
 \boxed{
 \Delta_a(\eta)
 =\mathbb K_a^{\rm del}(r_\eta,r_\eta).
 }
 \tag{L-91421.17}

No unknown operator square root is involved.

## 6. Relation to the annular hyperbolic port

Under the model-space ledger of `L-91313`, the same one-node scalar splits as

\[
 \Delta_a(\eta)
 =K_a^{\rm crit}(\eta,\eta)
  +K_a^{\rm st}(\eta,\eta)
  +H_a(\eta),
 \tag{L-91421.18}

with `H_a` given by `L-91420`.

Thus the full operator problem has a minimal scalar shadow:
construct the arithmetic source-to-model map at `r_eta` and prove that the
critical and stable outputs exhaust (L-91421.17).  The remaining nonnegative
quantity is exactly the annular telescope.

## 7. Exact boundary

```text
Cauchy shift eigenvector                          EXACT
all parity ports scalar at one node               EXACT
long adverse port dominated at one node           EXACT
short compensation scalarized                     EXACT
fixed eta=1 Green source path                      EXACT
one-node completed source scalar                   EXPLICIT SAFE JET
critical/stable exhaustion                         OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```