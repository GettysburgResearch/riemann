# Research report — Critical Jordan inverse sectors, the universal pole bridge, and the corrected optical target

Date: 2026-08-12  
Status: **substantial exact continuation; full unconditional proposal corrected; RH remains unproved**

## Executive result

The Julia–Wick programme has been pushed far enough to expose two previously hidden obstructions and one exact repair.

First, the all-prime signed Jordan inverse is now fully defined algebraically and its Hilbert regularity is classified exactly. It undergoes a Kakutani phase transition at

\[
 \Re s=\frac12+\omega.
\]

At the critical Xi line it belongs to a representation disjoint from the safe Fock vacuum, and its nonzero log-translates are disjoint as well. Hence no same-vacuum bounded Fock wave operator can perform the completion.

Second, exact Green/convolution commutation shows that the all-detail inverse has the opposite orientation from the first proposal: it maps the interacting Suzuki kernel back to the free archimedean endpoint.

Third, that free endpoint has one explicit unstable mode

\[
 \frac{C_{0,\omega}}{1-\omega}e^{(1/2-\omega)t},
 \qquad
 C_{0,\omega}=-4\omega\pi^{\omega-1/2}\Gamma(3/2-\omega).
\]

The full positive Jordan factor cancels this mode through its exact zero at \(s=1-\omega\). Finite Euler products do the opposite: they amplify its coefficient at rate

\[
 \log C_{\omega,P}(1-\omega)
 \sim\frac{P^{2\omega}}{2\omega\log P}.
\]

Thus the remaining construction is not an ordinary Wick limit. It must be an entangled sector-changing optical theorem that performs the global prime/archimedean pole-zero cancellation before taking Hilbert norms.

## Exact new theorems

### Product-sector threshold

For the local inverse

\[
 D_p(z)=\frac{1-a_pz}{1-b_pz},
 \qquad
 a_p=p^{-(\sigma-\omega)},\quad b_p=p^{-(\sigma+\omega)},
\]

one has

\[
 \|D_p\|_{H^2}^2
 =1+\frac{(a_p-b_p)^2}{1-b_p^2}.
\]

The normalized product vector is vacuum-equivalent exactly for \(\sigma>1/2+\omega\). At \(\sigma=1/2\), the exact translated overlap has a deficiency comparable to

\[
 p^{-1+2\omega}(1-\cos(t\log p)),
\]

whose prime sum diverges for every \(t\ne0\).

### Cylinder distribution and weighted Hardy norm

Because every local inverse has constant coefficient one, finite-prime pairings stabilize exactly on cylinder tests. This gives a canonical all-prime distribution without a limiting convention.

Its weighted Dirichlet–Hardy norm is

\[
 \prod_p\left[
 1+\frac{(p^{2\omega}-1)^2p^{-2(\sigma+\omega)}}
 {1-p^{-2(\sigma+\omega)}}
 \right],
\]

and converges exactly for \(\sigma>1/2+\omega\).

### Green commutation and orientation

For \(\mathcal JF(x)=\int_1^xF(y)dy/y\) and multiplicative convolution \(\mathcal T_a\),

\[
 \mathcal J\mathcal T_a=\mathcal T_a\mathcal J.
\]

Therefore, with \(A_\omega\) the interacting Suzuki Green primitive,

\[
 \mathcal T_{d_\omega}A_\omega=\mathcal JF_\omega.
\]

### Universal pole bridge

Suzuki's explicit endpoint kernel yields

\[
 g_\omega(x)
 =C_{0,\omega}x^{\omega-1}
 +C_{1,\omega}x^{2-\omega}+O(x^{4-\omega}).
\]

The free Green output is in \(L^2\) exactly when \(\omega>1/2\). After subtracting the single pole mode it is in \(L^2\) for the entire hard range.

In Mellin space this mode is the pole of

\[
 G_\omega(s)=\gamma(s-\omega)/\gamma(s+\omega)
\]

at \(s=1-\omega\). The forward Jordan factor

\[
 C_\omega(s)=\zeta(s-\omega)/\zeta(s+\omega)
\]

has a simple zero there, canceling it coefficient-one.

## One-node correction

The explicit all-generation pole-node source vector has norm

\[
 S_a\sim\frac1{2a},
\]

whereas the model critical-plus-stable ledger at the pole-aligned node is

\[
 T_a\sim(112+4\xi'(1)/\xi(1))a.
\]

Thus the old unrenormalized source vector cannot be the exhausted model source vector. A common analytic tangent map and nontrivial normalization remain indispensable.

## Corrected preferred theorem

`T-91307` defines `EPBOT_omega`, an unbounded sector-changing map from a rigged prime/archimedean cylinder source to the Hardy output plus positive theta/Beta/Poisson/local reserves. It must:

```text
agree with every finite Julia node;
retain the forward/inverse orientation;
mix the all-prime tail with the pole bridge before taking norms;
cancel the pole residue coefficient-one;
recover the completed Xi quotient on a safe uniqueness set;
have a positive cutoff-uniform graph identity;
intertwine the dyadic cocycle;
implement translations only after completion.
```

If this theorem is proved for one sequence \(\omega_j\downarrow0\), PR #402's outer-vector criterion gives RH.

## Honest boundary

This pass does not prove `EPBOT_omega`, the hard renewal estimate, innerness, or RH. It removes a misleading same-vacuum picture, defines the inverse distribution exactly, identifies the precise unstable mode and its exact arithmetic cancellation, and replaces the former generic renormalization request by a more rigid sector-changing optical theorem.
