# L-91422 — The Brownian Stein variability current is exactly the native Beta–Jacobi direction plus a nonnegative-weight boundary port

Claim ID: `L-91422`  
Status: **PROVED EXACT CURRENT DECOMPOSITION; ONE SOURCE-SPECIFIC GREEN DOMINATION REMAINS OPEN**  
Created: 2026-08-12  
Depends on: `L-91106/L-91107`, `L-91302`, `L-91310`, `L-91319`  
RH status: **unproved**

## 1. Reflection observable and Stein identity

Fix a completed tilt \(P_u\), and let \(\tau_u\ge0\) be its canonical Stein kernel. For independent \(Z_1,Z_2\sim P_u\), put

\[
S=Z_1+Z_2,\qquad
\Delta=Z_1-Z_2.
\]

For an exponential polynomial \(F\), retain

\[
\mathcal A_F(S,\Delta)
=
\int_{-S/2}^{S/2}
\overline{F(x+\Delta/2)}F(x-\Delta/2)\,dx.
\tag{L-91422.1}
\]

Write

\[
\tau_1=\tau_u(Z_1),\qquad
\tau_2=\tau_u(Z_2).
\]

The product Stein identity gives

\[
\operatorname{Cov}^{(2)}_u(\mathcal A_F,S)
=
\mathbb E_u^{(2)}
\left[
\tau_1\partial_1\mathcal A_F+
\tau_2\partial_2\mathcal A_F
\right].
\tag{L-91422.2}
\]

## 2. Sum and difference currents

Define

\[
D_+\mathcal A_F
=(\partial_1+\partial_2)\mathcal A_F
=2\partial_S\mathcal A_F,
\tag{L-91422.3}
\]

\[
D_-\mathcal A_F
=(\partial_1-\partial_2)\mathcal A_F
=2\partial_\Delta\mathcal A_F.
\tag{L-91422.4}
\]

Then

\[
\boxed{
\operatorname{Cov}^{(2)}_u(\mathcal A_F,S)
=
\frac12\mathbb E
\left[
(\tau_1+\tau_2)D_+\mathcal A_F
+
(\tau_1-\tau_2)D_-\mathcal A_F
\right].
}
\tag{L-91422.5}
\]

The sum derivative is the exact endpoint port

\[
\boxed{
D_+\mathcal A_F
=
\overline{F(Z_1)}F(Z_2)
+
\overline{F(-Z_2)}F(-Z_1).
}
\tag{L-91422.6}
\]

The difference derivative is the complete carrier-interference current.

## 3. Alignment with the native Beta direction

`L-91302` identifies the Gamma–Beta tangent direction

\[
\mathcal D_\beta
=
\partial_\Delta-\tanh\Delta\,\partial_S.
\tag{L-91422.7}
\]

Since

\[
D_-\mathcal A_F
=
2\mathcal D_\beta\mathcal A_F
+
\tanh\Delta\,D_+\mathcal A_F,
\tag{L-91422.8}
\]

equation (L-91422.5) becomes

\[
\boxed{
\begin{aligned}
\operatorname{Cov}^{(2)}_u(\mathcal A_F,S)
={}&
\mathbb E\left[
(\tau_1-\tau_2)
\mathcal D_\beta\mathcal A_F
\right]\\
&+\frac12\mathbb E\left[
c_{\tau,u}(Z_1,Z_2)
D_+\mathcal A_F
\right],
\end{aligned}
}
\tag{L-91422.9}
\]

where

\[
\boxed{
c_{\tau,u}
=
\tau_1+\tau_2+
(\tau_1-\tau_2)\tanh\Delta
}
\tag{L-91422.10}
\]

has the manifestly positive form

\[
\boxed{
c_{\tau,u}
=
(1+\tanh\Delta)\tau_1+
(1-\tanh\Delta)\tau_2
\ge0.
}
\tag{L-91422.11}
\]

Thus the entire non-Gaussian Stein variability defect is not an arbitrary two-variable current. It lies exactly in the one positive Beta–Jacobi direction already present in the source, plus an endpoint port carrying a nonnegative scalar weight.

## 4. Exact characteristic potential

At fixed Gamma reservoir \(A>0\), the BPY coordinates obey

\[
S_A(\Delta)
=
\log A-\log\cosh\Delta+\log\frac{\pi}{2}.
\tag{L-91422.12}
\]

Therefore differentiation at fixed \(A\) is precisely

\[
\frac d{d\Delta}\Big|_A
=
\partial_\Delta-\tanh\Delta\,\partial_S
=
\mathcal D_\beta.
\tag{L-91422.13}
\]

Let \(T_u'=\tau_u\), and define the explicit current potential

\[
\boxed{
\begin{aligned}
\mathcal P_u(A,\Delta)
=
\int_0^\Delta
\Bigg[
&\tau_u\left(\frac{S_A(v)+v}{2}\right)\\
-&\tau_u\left(\frac{S_A(v)-v}{2}\right)
\Bigg]\,dv.
\end{aligned}
}
\tag{L-91422.14}
\]

Then

\[
\boxed{
\mathcal D_\beta\mathcal P_u
=
\tau_u(Z_1)-\tau_u(Z_2).
}
\tag{L-91422.15}
\]

So the first term of (L-91422.9) is an explicit cross energy along a single characteristic direction:

\[
\mathbb E[
(\mathcal D_\beta\mathcal P_u)
(\mathcal D_\beta\mathcal A_F)
].
\tag{L-91422.16}
\]

## 5. Relation to the native carré du champ

The conditional Beta form of `L-91302` is

\[
\Gamma_\beta(G,G)
=
W_\beta(A,V)
|\mathcal D_\beta G|^2,
\tag{L-91422.17}
\]

with

\[
W_\beta(A,V)
=
\frac{\cosh^4\Delta}{4A^2}
\sum_n c_n^2(1-V_n^2)\ge0.
\tag{L-91422.18}
\]

Equations (L-91422.9) and (L-91422.15) reduce the full Brownian reflection sign to one source-specific Green calculation:

> integrate the current potential (L-91422.14) by parts in the exact tilted Beta–Jacobi form, and prove that the resulting cross energy plus the boundary port in (L-91422.9) is nonnegative for every exponential polynomial \(F\).

No generic DtN existence theorem is needed. The operator and the boundary current are explicit.

## 6. What this does and does not prove

Closed:

```text
canonical Stein current decomposition             EXACT
endpoint derivative                               EXACT
alignment with native Beta direction              EXACT
nonnegative scalar boundary coefficient           EXACT
one-dimensional characteristic potential          EXACT
```

Open:

```text
tilted Beta integration-by-parts boundary ledger
theta boundary atom matching
nonnegativity for arbitrary complex F
Brownian reflection/Pick positivity
Riemann Hypothesis
```

This is a strict reduction of the route-III boundary identification, not a complete proof.
