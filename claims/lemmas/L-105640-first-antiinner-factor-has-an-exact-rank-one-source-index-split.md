# L-105640 — The first anti-inner derivative factor has an exact rank-one source/index split

Claim ID: `L-105640`  
Status: **PROVED EXACT HARDY/MODEL-SPACE THEOREM; XI DESCENT NOT CLAIMED**  
Created: 2026-08-25  
Depends on: `L-105627--L-105631`; sibling `L-106415`, `L-106430--L-106431`  
RH status: **not assumed**

## 1. Inner/anti-inner factorization of the shifted derivative phase

Let

\[
D_H(z)=\Xi'(z+iH),
\qquad
U_H(z)={D_H^{\#}(z)\over D_H(z)},
\qquad H>0,
\]

with common real factors cancelled.  On every finite regular canonical-product
truncation, and hence in the standard cofinal Cartwright limit, write

\[
\boxed{
U_H=\omega_H e^{i\tau_H z}{A_H\over B_H},
}
\tag{L-105640.1}
\]

where `A_H` and `B_H` are inner Blaschke products with no common factor.  The
zeros of `B_H` are exactly

\[
b_\rho=\rho-iH\in\mathbb C_+
\]

coming from zeros `rho` of `Xi'` with `Im rho>H`.  The zeros of `A_H` are the
reflections of the zeros of `D_H` in the lower half-plane.  The positive Xi
Laplace moments orient the exponential factor with `tau_H>=0`; it is therefore
part of the inner numerator.

Thus

```text
H >= beta_1:       B_H=1 and U_H is inner;
H below beta_1:    every crossed Xi-prime zero contributes one anti-inner
                   denominator factor.
```

All statements below are purely Hardy-space algebra once (L-105640.1) has
been installed.

## 2. Exact signed de Branges–Rovnyak kernel

For a meromorphic unimodular function `Theta`, put

\[
K_\Theta(z,w)
={1-\Theta(z)\overline{\Theta(w)}
 \over -i(z-\overline w)}.
\]

If `U=A/B` with coprime inner `A,B`, direct multiplication gives

\[
\boxed{
B(z)\overline{B(w)}K_U(z,w)
=K_A(z,w)-K_B(z,w).
}
\tag{L-105640.2}

Hence the complete failure of the Schur/Pick kernel is not an unspecified
boundary remainder.  It is the negative model-space kernel of the anti-inner
denominator, modulo the positive kernel of the surviving inner numerator.

## 3. A first simple crossing is rank one

Suppose one simple zero crosses first.  Write

\[
b=\alpha+i\delta,
\qquad \delta>0,
\]

and

\[
B_b(z)={z-b\over z-\overline b}.
\]

Then

\[
\boxed{
K_{B_b}(z,w)
={2\delta
 \over (z-\overline b)(\overline w-b)}
=k_b(z)\overline{k_b(w)},
}
\tag{L-105640.3}

where

\[
k_b(z)={\sqrt{2\delta}\over z-\overline b}
\]

is the normalized upper-half-plane model vector, up to the fixed Hardy
normalization.  For every compact set away from the crossing point,

\[
K_{B_b}(z,w)=O(\delta),
\]

and

\[
\boxed{
\lim_{\delta\downarrow0}{K_{B_{\alpha+i\delta}}(z,w)\over\delta}
={2\over(z-\alpha)(\overline w-\alpha)}.
}
\tag{L-105640.4]

Thus the static kernel defect vanishes at first contact, but its transverse
spectral-flow derivative is a nonzero rank-one boundary flux.

## 4. Exact Hankel charge in an inner background

Let `A` be the inner numerator present immediately before the crossing and
put

\[
U=\overline{B_b}\,A
\]

on the boundary.  Since `A` is analytic,

\[
H_U=H_{\overline{B_b}}M_A.
\]

The Hankel operator `H_(overline{B_b})` is the rank-one partial isometry with
initial projection `P_(K_(B_b))`.  Reproducing gives

\[
M_A^*k_b=\overline{A(b)}k_b.
\]

Consequently

\[
\boxed{
H_U^*H_U
=|A(b)|^2P_{k_b}.
}
\tag{L-105640.5

The inner background therefore attenuates the first adverse charge only by the
literal pseudohyperbolic factor `|A(b)|^2`; no untyped conditioning constant
appears.

## 5. Paley–Wiener source/index conservation

Under the Paley–Wiener transform, the normalized model vector is

\[
\boxed{
\phi_b(\xi)
=\sqrt{2\delta}\,e^{-\delta\xi}e^{-i\alpha\xi},
\qquad \xi>0.
}
\tag{L-105640.6

Let `P_L` be the hard source-frequency projection to `[0,L]`.  Then

\[
\|P_L\phi_b\|^2=1-e^{-2\delta L},
\qquad
\|P_L^\perp\phi_b\|^2=e^{-2\delta L}.
\]

Combining with (L-105640.5) gives the exact split

\[
\boxed{
\|H_UP_L\|_{\mathcal S_2}^2
=|A(b)|^2(1-e^{-2\delta L}),
}
\tag{L-105640.7

\[
\boxed{
\|H_UP_L^\perp\|_{\mathcal S_2}^2
=|A(b)|^2e^{-2\delta L},
}
\tag{L-105640.8

and therefore

\[
\boxed{
\|H_UP_L\|_{\mathcal S_2}^2
+
\|H_UP_L^\perp\|_{\mathcal S_2}^2
=|A(b)|^2.
}
\tag{L-105640.9

This is the exact source/index conservation law at the first anti-inner
crossing.

## 6. Three scaling regimes

The relevant dimensionless parameter is

\[
c=\delta L.
\]

Then

```text
c -> 0:        the source frame sees o(1) of the new charge and the endpoint /
               signed-complement ledger sees almost all of it;

c -> c_0:      the charge splits in the fixed proportions
               1-exp(-2c_0) and exp(-2c_0);

c -> infinity: the source frame sees the complete adverse charge and the
               endpoint complement vanishes.
```

In particular, a cofinal source bank must have bandwidth of order at least
`1/delta` to see a zero which has penetrated only depth `delta` below the
moving boundary.

## 7. Scope

The theorem does not exclude the crossing.  It proves that the source-energy
and endpoint-index programmes are not competing approximations: at first
contact they are two exact pieces of one conserved rank-one charge.  A fixed
band cannot prove safe descent by source energy alone, while an adaptive band
must retain the complementary endpoint term.  Multiple and confluent crossings
are represented by the corresponding finite model-space sampling matrix and
Laguerre blocks of `L-106415/L-106430`.  RH remains unproved.
