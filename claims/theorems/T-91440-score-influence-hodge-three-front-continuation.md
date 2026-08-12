# T-91440 — Corrected three-front continuation: score normalization, prime influences, and Hahn resistance

Claim ID: `T-91440`  
Status: **RESEARCH SYNTHESIS — THREE EXACT ADVANCES, THREE EXPLICIT REMAINING THEOREMS**  
Created: 2026-08-12  
RH status: **unproved**

## I. Factor-54 front

The candidate full proof on PR #407 weights inherited endpoint-score loss by fractions of the native SHARP target source. `R-91440` gives an exact two-atom counterexample to that inference.

The corrected exact ledger is `L-91441`:

\[
 d\tau_x=q_xd\sigma_x,
 \qquad
 q_x=\frac{W_\Psi}{W_S},
\]

with score-mass child weights

\[
 \theta_b^S
 =\frac{\mathfrak S_{x/p_b}(\nu_b^{\rm in})}
        {\mathfrak S_x(\nu)},
 \qquad
 \sum_b\theta_b^S\le1,
\]

while the actual child target measures form a separate positive subpartition of the parent target.

This repairs the two-ledger algebra and preserves one-use target capacity through `L-91329/L-91340`.

The sole remaining producer theorem is now:

> Construct one positive source-linear packing functor on the whole normalized positive kernel cone, with local debt bounded uniformly per unit score mass and with the root score normalization matching the prime-ramp loss.

A scalar SHARP-mass identity does not supply this theorem.

## II. Green-removal front

For every pre-knot scalar,

\[
 B_a(\log N-)
 =B_a^{\rm FKG}(N)+\mathcal C_{a,N},
\]

and `L-91442` proves the exact positive decomposition

\[
\boxed{
 \mathcal C_{a,N}
 =\frac1{C_N}
  \sum_{p_j\le N}
   \mathbb E[\Delta_jG\Delta_jH]
 \ge0.
}
\]

Thus `R-91401` does not merely say one-sided FKG is weak. It identifies the exact missing source: a sum of prime-coordinate martingale influence energies.

The sole remaining arithmetic theorem is

\[
 \mathcal C_{a,N}
 \ge[-B_a^{\rm FKG}(N)]_+
\]

uniformly in the compact hard range. This is the correct quantitative target for a block-prime, butterfly, or polarized Hardy proof.

## III. Brownian/theta front

`L-91443` gives the exact finite Hodge completion of every Hahn edge current:

\[
 \sum_kJ_k\overline{\Delta f_k}
 =\mathcal E_N(P_J,f),
\]

\[
 \mathcal R_N(J)
 =\sum_k\frac{|J_k|^2}{c_k},
\]

and

\[
 \operatorname{Re}\sum_kJ_k\overline{\Delta f_k}
 \ge-rac12\mathcal R_N(J)-\frac12\mathcal E_N(f,f).
\]

The beta-binomial Hahn chain has spectral gap one, so also

\[
 \mathcal R_N(J)
 \le\|\operatorname{div}_\pi J\|_{L^2(\pi_N)}^2.
\]

Combining this with PR #409 reduces the finite Brownian/theta theorem to the fully quantified reserve inequality

\[
 \mathfrak R_{\theta,N}(F)
 \ge
 \frac12\mathcal R_N(J_{u,N})
 +\frac14\mathbb E[c_{\tau,u}\mathcal D_F].
\]

There is no missing finite Poisson solver, current orientation, or endpoint coefficient. The open theorem is the theta reserve itself and the resistance-norm limit.

## IV. Common positive engine

The Green influence term and the Brownian finite current are two presentations of the same object:

```text
product-coordinate martingale difference
    -> adjacent positive butterfly
    -> birth-death/Hahn edge current
    -> Jacobi carré du champ.
```

This suggests one joint production programme:

1. form the finite prime-influence current for the exact Green knot;
2. compress it into a Hahn edge network with preserved resistance;
3. test whether the theta/contact reserve supplies the sharp Hodge completion;
4. use the same certificate as the shape-uniform positive packing functor on the factor-54 cone.

## V. Exact status

```text
PR #407 SHARP-mass score coefficient            REFUTED AS WRITTEN
score-normalized two-ledger branching            EXACT
shape-uniform factor-54 packing functor           OPEN / RH-BEARING
Green knot = FKG envelope + influence energy      EXACT
quantitative prime-influence lower bound          OPEN / RH-BEARING
finite Hahn Hodge/resistance completion           EXACT
finite theta reserve inequality                   OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
