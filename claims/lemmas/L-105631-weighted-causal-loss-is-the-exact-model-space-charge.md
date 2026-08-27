# L-105631 — Weighted causal loss is the exact model-space charge at trace-class/finite scope

Claim ID: `L-105631`  
Status: **PROVED EXACT TRACE/MODEL-SPACE THEOREM; CONTINUUM TRACE REQUIRES REGULARIZATION**  
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

Let `R>=0` be trace class. More generally, it is enough that the two terms in
the first trace difference are trace class and cyclicity is justified. Then

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

At finite-dimensional source scope the same identity holds with every operator
compressed before taking the trace. Equation (L-105631.2) identifies the exact
topological consumer: the weighted source mass of the all-pass model space.

A bounded multiplication operator `M_r` on the continuum space
`L^2(0,infinity)` is generally **not** trace class. One may not apply
(L-105631.2) to it by subtracting two infinite traces. The continuum Xi use
must pass through a declared finite/source trace-class regularization and keep
its limiting endpoint carrier.

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

For any bounded nonnegative diagonal source weight `r`, the **finite-rank
model-space compression** is trace class and

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
increases. Thus every simple factor of depth at least `eta` has compressed
charge at least

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

Thus collisions and multiplicity are explicit positive finite-rank charges.

## 4. Arbitrary finite inner phase

For a finite Blaschke product `U` of degree `d`, choose any orthonormal basis
`e_1,...,e_d` of `K_U`. Then

\[
\boxed{
\operatorname{tr}(P_{K_U}M_rP_{K_U})
=
\sum_{j=1}^d\langle M_re_j,e_j\rangle.
}
\tag{L-105631.7}
\]

Whenever a trace-class regularization `R_T` of `M_r` is declared and
(L-105631.2) applies,

\[
\operatorname{tr}(R_T-V^*R_TV)
=
\operatorname{tr}(P_{K_U}R_TP_{K_U}).
\]

At `R=I`, the domain defect `I-V^*V` is zero while the range defect
`I-VV^*=P_(K_U)` has trace `d`. Since `I` is not trace class on the infinite
Hardy space, this is a firewall against extending (L-105631.2) by formal
subtraction.

## 5. Xi interpretation

For the safe-height Xi-prime phase `U_H` and the monotone profile `r_(b,h)`,
`L-105628` gives a form-level contraction. Every declared finite model-space
section has the explicit positive charges (L-105631.4)--(L-105631.7).
Consequently:

```text
critical zeros a fixed distance below the shifted boundary
  carry a fixed positive compressed source charge;

only zeros whose shifted depth tends to zero
  can become asymptotically charge-free.
```

Passing from these finite charges to a global trace requires exactly the
cofinal endpoint/index regularization `ENDIDX105630`. No continuum trace
identity is claimed before that step.

## 6. Scope

A lower bound on the charge of each simple factor does not automatically add
over a nonorthogonal zero list; the invariant finite object is the complete
model-space trace. The theorem identifies and localizes finite charges but does
not prove the cofinal trace limit, `SAFEDESC105628`, or RH.
