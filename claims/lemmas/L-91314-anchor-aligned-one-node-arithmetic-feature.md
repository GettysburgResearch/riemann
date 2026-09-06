# L-91314 — The one-node detector can be aligned exactly with the canonical Jordan anchor

Claim ID: `L-91314`  
Status: **EXACT COORDINATE AND SAFE-FEATURE ALIGNMENT; NORM EXHAUSTION REMAINS OPEN**  
Created: 2026-08-12  
Depends on: `L-91313`, main `L-91014/L-91019/L-9506`  
RH status: **unproved**

## 1. Choose the aligned interior node

For `0<a<1/2`, work with

\[
 \Theta_a(z)
 =\frac{\xi(\frac12-a+z)}
        {\xi(\frac12+a+z)}
 \tag{L-91314.1}
\]

in the right half-plane. Choose

\[
 \boxed{
 \eta_a=\frac12+3a.
 }
 \tag{L-91314.2}
\]

Then

\[
 \frac12-a+\eta_a=1+2a,
 \qquad
 \frac12+a+\eta_a=1+4a,
 \tag{L-91314.3}
\]

and hence

\[
 \boxed{
 \Theta_a(\eta_a)
 =\frac{\xi(1+2a)}{\xi(1+4a)}.
 }
 \tag{L-91314.4}
\]

Both completed-zeta samples lie in the absolutely convergent Euler half-plane.

## 2. Exact Jordan anchor

Let

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}
 \tag{L-91314.5}
\]

and let

\[
 k_{a,s}
 =\sum_{n\ge1}\sqrt{q_a(n)}n^{-s}e_n,
 \qquad
 q_a(n)=\prod_{p\mid n}(1-p^{-2a}).
 \tag{L-91314.6}
\]

At

\[
 s_a=\frac12+a,
 \tag{L-91314.7}
\]

one has

\[
 \|k_{a,s_a}\|^2
 =Q_a(1+2a)
 =\frac{\zeta(1+2a)}{\zeta(1+4a)}.
 \tag{L-91314.8}
\]

Thus the unit vector

\[
 \boxed{
 \eta_a^{\rm J}
 =\frac{k_{a,\,1/2+a}}
        {\sqrt{Q_a(1+2a)}}
 }
 \tag{L-91314.9}
\]

is exactly the canonical anchor used by the positive logarithmic-jet theorem.
No arbitrary safe carrier is introduced.

## 3. Completed archimedean factor

Direct substitution in the completed Xi ratio gives

\[
 \boxed{
 \Theta_a(\eta_a)
 =\Gamma_a^{\rm anc}\,Q_a(1+2a),
 }
 \tag{L-91314.10}
\]

where

\[
 \boxed{
 \Gamma_a^{\rm anc}
 =\pi^a
 \frac{1+2a}{2(1+4a)}
 \frac{\Gamma(\frac12+a)}
      {\Gamma(\frac12+2a)}.
 }
 \tag{L-91314.11}
\]

The arithmetic and archimedean parts are therefore both explicit at the same
anchor point.

## 4. Exact one-Green feature at the aligned node

For `s=2a`, the completed positive one-Green ratio is

\[
 \mathcal H_{2a}(q)
 =\frac1q\frac{\xi(1+q)}{\xi(1+2a+q)}
 =\int_0^\infty e^{-qt}\,d\mu_{2a}(t),
 \qquad \mu_{2a}\ge0.
 \tag{L-91314.12}
\]

At the aligned value

\[
 q_a=2a,
 \tag{L-91314.13}
\]

one gets

\[
 \boxed{
 2a\,\mathcal H_{2a}(2a)
 =\Theta_a(\eta_a).
 }
 \tag{L-91314.14}
\]

Consequently the explicit safe vector

\[
 \boxed{
 \phi_a(t)=\sqrt{2a}\,e^{-at}
 \in L^2(\mu_{2a})
 }
 \tag{L-91314.15}
\]

has norm

\[
 \boxed{
 \|\phi_a\|_{L^2(\mu_{2a})}^2
 =\Theta_a(\eta_a).
 }
 \tag{L-91314.16}
\]

The logarithmic tangent vectors are simply `t^j phi_a`; their Gram entries are
absolutely convergent derivatives of `H_(2a)` at `2a`.

## 5. One-node zero-port detector at the same point

By `L-91313`,

\[
 \mathcal K_a^{\rm hyp}(\eta_a,\eta_a)
 =\frac{1-|B_a(\eta_a)|^2}
        {2\eta_a|B_a(\eta_a)|^2}.
 \tag{L-91314.17}
\]

It vanishes exactly when there is no crossed zero port at scale `a`.
Therefore the minimal arithmetic theorem can be required at the aligned node
`eta_a`, using the canonical source vector (L-91314.15) and its completed
first-chaos/tangent features.

## 6. Corrected one-node theorem

> **Anchor-Aligned Arithmetic Exhaustion (`AAAE_a`).**  
> Starting from the explicit positive one-Green feature `phi_a`, the Jordan
> anchor `eta_a^J`, and the completed gamma/pole factor
> `Gamma_a^(anc)`, construct the source-ordered boundary map and prove exact
> norm exhaustion by the critical and deterministic stable outputs at
> `z=eta_a`, with no auxiliary remainder.

Once the arithmetic source norm is identified with the model source norm,
`AAAE_a` forces (L-91314.17) to vanish and proves

\[
 \xi(s)\ne0
 \qquad(\Re s>\tfrac12+a).
 \tag{L-91314.18}
\]

For one sequence `a_j downarrow0`, `AAAE_(a_j)` proves RH.

## 7. Significance

The remaining vector is no longer abstract:

```text
model node:          eta_a = 1/2+3a;
Green parameter:     q_a   = 2a;
Jordan coherent:     k_(a,1/2+a);
unit anchor:         eta_a^J;
positive feature:    sqrt(2a) exp(-a t);
archimedean scalar:  Gamma_a^(anc).
```

The only missing object is the completed source-to-model tangent/isometry at
this one explicitly aligned state.
