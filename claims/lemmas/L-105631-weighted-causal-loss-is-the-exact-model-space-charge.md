# L-105631 — Weighted causal loss is the exact model-space topological charge

Claim ID: `L-105631`  
Status: **PROVED EXACT TRACE/MODEL-SPACE THEOREM**  
Created: 2026-08-25  
Depends on: `L-105625`; `L-105630`; `L-106430`  
RH status: **not assumed**

## 1. Exact trace identity

Let `U` be inner on the upper half-plane and let `V=M_U` on `H^2`. Put

\[
K_U=H^2\ominus UH^2.
\]

Then

\[
VV^*=I-P_{K_U}.
\tag{L-105631.1}
\]

Let `R>=0` be trace class. More generally, it is enough that all displayed
products are trace class. Cyclicity gives

\[
\begin{aligned}
\operatorname{tr}(R-V^*RV)
&=\operatorname{tr}R-\operatorname{tr}(RVV^*)\\
&=\operatorname{tr}(RP_{K_U}).
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{tr}(R-V^*RV)
=\operatorname{tr}(P_{K_U}RP_{K_U}).
}
\tag{L-105631.2}
\]

When `R=M_r` for a decreasing profile, `L-105625` makes the left side
nonnegative. Equation (L-105631.2) identifies its exact topological consumer:
the weighted source mass of the all-pass model space.

## 2. One simple Blaschke factor

Let

\[
B_b(z)={z-b\over z-\overline b},
\qquad
b=a+iy,
\qquad y>0.
\]

Under Paley--Wiener, the one-dimensional model space has the normalized vector

\[
\boxed{
\phi_b(\xi)
=\sqrt{2y}\,e^{-y\xi}e^{-ia\xi},
\qquad \xi>0.
}
\tag{L-105631.3}
\]

Hence for a diagonal source weight `r`,

\[
\boxed{
\operatorname{tr}
\left(P_{K_{B_b}}M_rP_{K_{B_b}}\right)
=
\int_0^\infty
r(\xi)\,2y e^{-2y\xi}\,d\xi.
}
\tag{L-105631.4}
\]

A boundary-near zero is cheap only because its normalized model vector escapes
to high source frequencies. There is no unspecified conditioning constant.

If `r` is nonincreasing, the right side is nondecreasing in `y`: an exponential
random variable with rate `2y` moves stochastically toward zero as `y`
increases. Thus every factor of depth at least `eta` costs at least

\[
\boxed{
\kappa_r(\eta)
=
\int_0^\infty r(\xi)\,2\eta e^{-2\eta\xi}\,d\xi.
}
\tag{L-105631.5}
\]

## 3. Confluent factor

For a factor of multiplicity `m`, the orthonormal Laguerre basis of
`L-106430` gives

\[
\boxed{
\operatorname{tr}_{K_{B_b^m}}M_r
=
\sum_{q=0}^{m-1}
\int_0^\infty
r(\xi)
\,2y e^{-2y\xi}L_q(2y\xi)^2d\xi.
}
\tag{L-105631.6}
\]

Thus collisions and multiplicity are explicit positive weighted charges.

## 4. Arbitrary finite inner phase

For a finite Blaschke product `U` of degree `d`, choose any orthonormal basis
`e_1,...,e_d` of `K_U`. Then

\[
\boxed{
\operatorname{tr}(R-V^*RV)
=
\sum_{j=1}^d\langle Re_j,e_j\rangle.
}
\tag{L-105631.7}
\]

At `R=I`, this reduces to

\[
\operatorname{tr}(I-V^*V)=0
\]

on the domain and

\[
\operatorname{tr}(I-VV^*)=d
\]

on the range side. The distinction is essential: the weighted contraction
loss in (L-105631.2) is obtained through cyclicity and the range defect
`P_(K_U)`, not by replacing the isometry defect `I-V^*V`, which is zero.

## 5. Xi interpretation

For the safe-height Xi-prime phase `U_H` and the actual monotone profile
`r_(b,h)`, the exact loss in `L-105628` is the current-weighted mass of
`K_(U_H)`.

Consequently:

```text
critical zeros a fixed distance below the shifted boundary
  carry a fixed positive source charge;

only zeros whose shifted depth tends to zero
  can become asymptotically charge-free.
```

This matches, in exact model-space coordinates, the Jensen-disk and
zero-height/spatial-escape frontiers elsewhere in the repository.

## 6. Scope

A lower bound on the charge of each simple factor does not automatically add
over a nonorthogonal zero list; the invariant object is the complete model-
space trace. Nor does the safe-height charge prevent a zero from reaching the
boundary during base descent. The theorem identifies and localizes the charge;
it does not prove `SAFEDESC105628` or RH.
