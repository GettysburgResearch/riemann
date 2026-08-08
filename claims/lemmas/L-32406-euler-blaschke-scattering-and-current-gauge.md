# L-32406 — Euler–Blaschke scattering realizes the neutral principal return exactly

Claim ID: `L-32406`  
Title: The critical Euler–Blaschke factor is a causal unitary first-order scattering filter, and the main-pole-killing logarithmic current differs from its all-pass image by one explicit deterministic gauge  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/HILBERT-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`; the atomized carry multiplier `N_theta` of PR #302  
Scope: exact neutral-mode realization; no arithmetic energy bound or RH conclusion

## 1. Critical-coordinate form of the Euler–Blaschke factor

Fix

\[
 Q=2^d,
 \qquad
 L=\log Q,
 \qquad
 a=Q^{-1/2}\in(0,1),
 \qquad
 b=\sqrt{1-a^2}.
\]

Put

\[
 s=\frac12+z.
\]

The normalized factor of `L-32404` becomes

\[
\begin{aligned}
 \phi_Q(z)
 &:=\Phi_Q(1/2+z)\\
 &=Q^{-1/2}
   \frac{1-Q^{1/2-z}}{1-Q^{-1/2-z}}\\
 &=\boxed{
   \frac{a-e^{-Lz}}{1-ae^{-Lz}}}.
\end{aligned}
 \tag{L-32406.1}
\]

Thus `phi_Q` is the standard scalar Blaschke/all-pass transfer function in the delay variable

\[
 w=e^{-Lz}.
\]

On the boundary `Re z=0`,

\[
 \boxed{|\phi_Q(it)|=1,}
 \tag{L-32406.2}
\]

while `|phi_Q(z)|<1` for `Re z>0` by `L-32404`.

Its causal expansion is

\[
 \boxed{
 \phi_Q(z)
 =a-(1-a^2)
   \sum_{r\ge1}a^{r-1}e^{-rLz}.
 }
 \tag{L-32406.3}
\]

## 2. Exact unitary state-space realization

Let `H` be any real or complex Hilbert space and let a causal input

\[
 u:[0,\infty)\to H
\]

be locally square integrable. Decompose time into `L`-slabs. For

\[
 0\le\tau<L,
 \qquad
 u_k(\tau)=u(\tau+kL),
\]

define the state and output recursively by

\[
 \boxed{
 \begin{pmatrix}
 x_{k+1}(\tau)\\
 y_k(\tau)
 \end{pmatrix}
 =
 \begin{pmatrix}
 a&b\\
 -b&a
 \end{pmatrix}
 \begin{pmatrix}
 x_k(\tau)\\
 u_k(\tau)
 \end{pmatrix},
 \qquad x_0=0.
 }
 \tag{L-32406.4}
\]

The `2 x 2` matrix is orthogonal/unitary. Hence pointwise in `tau`,

\[
 \boxed{
 \|x_{k+1}\|_H^2+\|y_k\|_H^2
 =\|x_k\|_H^2+\|u_k\|_H^2.
 }
 \tag{L-32406.5}
\]

Solving the state recursion gives

\[
 x_k
 =b\sum_{r=1}^{k}a^{r-1}u_{k-r},
 \tag{L-32406.6}
\]

and therefore

\[
 y_k
 =a u_k-(1-a^2)
   \sum_{r=1}^{k}a^{r-1}u_{k-r}.
 \tag{L-32406.7}
\]

Comparing with (L-32406.3), the output is exactly

\[
 \boxed{y=\phi_Q(D)u.}
 \tag{L-32406.8}
\]

No spectral approximation is involved.

Integrating (L-32406.5) over `tau` and summing `0<=k<K` gives the exact finite-prefix energy law

\[
 \boxed{
 \sum_{k=0}^{K-1}\|u_k\|_{L^2(0,L;H)}^2
 =
 \sum_{k=0}^{K-1}\|y_k\|_{L^2(0,L;H)}^2
 +\|x_K\|_{L^2(0,L;H)}^2.
 }
 \tag{L-32406.9}
\]

Thus the difference between the principal input energy and its all-pass filtered energy is one explicit nonnegative terminal scattering state. This is the exact coefficient-one neutral channel; it is not a guessed contraction constant.

## 3. The logarithmic-current gauge identity

Retain

\[
 N_\theta(s)
 =\frac{1-\theta^s-(1-\theta)^s}{s}
\]

and define the ordinary atomized logarithmic current

\[
 \boxed{
 U_\theta(z)
 =-\frac{\zeta'}\zeta(s)N_\theta(s),
 \qquad s=\frac12+z.
 }
 \tag{L-32406.10}
\]

For the `Q`-source let

\[
 L_Q=-\frac{A_Q'}{A_Q}
 =-\frac{\zeta'}\zeta+\frac{E_Q'}{E_Q}
\]

and normalize its physical current by

\[
 \boxed{
 V_{Q,\theta}(z)
 =Q^{-1/2}E_Q(s)L_Q(s)N_\theta(s).
 }
 \tag{L-32406.11}
\]

Since

\[
 E_Q(s)=\sqrt Q\,\phi_Q(z),
\]

direct differentiation gives

\[
 \boxed{
 V_{Q,\theta}(z)
 =\phi_Q(z)U_\theta(z)
  +\phi_Q'(z)N_\theta(s).
 }
 \tag{L-32406.12}
\]

The second term contains no zeta factor and no prime coefficient. It is a completely explicit deterministic gauge.

## 4. The gauge is a bounded causal forcing

Differentiating (L-32406.1),

\[
 \boxed{
 \phi_Q'(z)
 =L(1-a^2)
   \frac{e^{-Lz}}{(1-ae^{-Lz})^2}
 =L(1-a^2)
   \sum_{r\ge1}r a^{r-1}e^{-rLz}.
 }
 \tag{L-32406.13}
\]

The inverse Laplace transform of `N_theta(s)` is the atomized carry kernel

\[
 H_\theta(t)=e^{-t/2}C(e^t,\theta)\mathbf1_{t\ge0},
\]

so

\[
 |H_\theta(t)|\le e^{-t/2}
\]

uniformly in `theta`. In particular,

\[
 \|H_\theta\|_2\le1.
 \tag{L-32406.14}
\]

The delay kernel in (L-32406.13) has `l^1` mass

\[
\begin{aligned}
 L(1-a^2)\sum_{r\ge1}r a^{r-1}
 &=L\frac{1-a^2}{(1-a)^2}\\
 &=L\frac{1+a}{1-a}.
\end{aligned}
\]

Young's inequality therefore gives the uniform deterministic bound

\[
 \boxed{
 \|\phi_Q' N_\theta\|_{L^2(0,\infty)}
 \le
 L\frac{1+a}{1-a}.
 }
 \tag{L-32406.15}
\]

For `Q=4`, `a=1/2`, so the right side is simply

\[
 \boxed{3\log4.}
 \tag{L-32406.16}
\]

The same bound holds after integrating the carry-position variable over any interval of length at most one.

## 5. Consequence for the neutral recurrence architecture

Equation (L-32406.12) and the exact scattering law (L-32406.9) separate the proof state into

```text
main-pole-killing Q-current V_Q:
    arithmetic / Selberg object;

explicit gauge phi_Q' N_theta:
    uniformly bounded deterministic forcing;

principal ordinary current U:
    returned through one unitary all-pass state x_K.
```

Thus a valid global proof does not need to invent an abstract coefficient-one principal return. The return is the concrete state (L-32406.6), and all nonprincipal local-Euler dressing is explicit.

In particular, if a source-bound reflected argument controls the `Q=4` current on each block by a polynomial forcing plus the incoming scattering state, then (L-32406.9) produces exactly the coefficient-one delayed architecture required by the neutral-mode firewall.

## 6. Proof boundary

Closed exactly here:

1. critical-coordinate Blaschke form;
2. causal expansion;
3. unitary state-space realization;
4. exact finite-prefix energy conservation;
5. exact ordinary-current / Q-current gauge identity;
6. a uniform `L^2` bound for the deterministic gauge.

Open:

1. an arithmetic reflected estimate for the `Q=4` current;
2. absorption of that current by the `Q=4` Selberg reserve of `L-32405` in the complete independent-frequency block;
3. the resulting global neutral recurrence;
4. RH.
