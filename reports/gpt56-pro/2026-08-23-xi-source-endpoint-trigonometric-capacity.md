# Xi source endpoint and trigonometric capacity

Date: 2026-08-23  
Workspace: PR #729  
Scientific status: **RH unproved**

## Source-owned formulas

The source matrices in the origin capacity theorem are explicit functions of a
positive tilted Xi Fourier law. For odd derivatives, the first coefficients
are

\[
a_0=1,
\quad a_1=x/3,
\quad a_2=(5x^2-y)/30,
\quad a_3=(210x^3-77xy+3z_3)/2520.
\]

For even derivatives, after subtracting the central residue,

\[
a_0=(3-hx)/6,
\qquad
a_1=(15x-10hx^2+3hy)/360.
\]

This turns the first source signs into literal concentration inequalities of
one positive real probability law.

## Low-order sufficient thresholds

For odd derivatives, moment log-convexity shows that

\[
E[X^2]/E[X]^2\le35/27
\]

pays both ordinary and shifted order-two source matrices.

For even derivatives,

\[
E[X]E[X^{-1}]\le15/7
\]

pays both regularized order-one source pivots.

These thresholds are source-specific sufficient lanes, not sharp RH gates.

## Trigonometric exact model

For `sin(omega z)`, the tangent Mittag--Leffler measure

\[
\sum_{j\ge0}{8\over\pi^2(2j+1)^2}
\delta_{4\omega^2/[\pi^2(2j+1)^2]}
\]

is exactly the critical-residue atom measure.

For regularized `cos(omega z)`, the corresponding cotangent measure is

\[
\sum_{j\ge1}{2\over\pi^2j^2}
\delta_{\omega^2/(\pi^2j^2)}.
\]

Finite windows leave a positive tail. At full exhaustion, source and critical
capacity are equal and boundary reserve is zero.

## Unconditional high-derivative source endpoint

The positive Xi kernel admits a large real Mellin saddle. First-summand
dominance gives

\[
w_s={1\over2}\log s+O(\log\log s),
\qquad
\kappa_s={2s\over w_s}(1+O(1/w_s)).
\]

Real-line concentration yields

\[
M_{s+a}/M_s=w_s^a(1+o(1))
\]

for every fixed real `a`. Hence every fixed finite odd or even source order is
eventually strictly positive. The threshold may depend on the matrix order.

This theorem does not use the unresolved complex moving saddle. Its independent
review target is the global real-tail comparison and the treatment of fixed
negative moments near zero.

## Remaining boundary object

The high-tail source side is now positive order by order. The unresolved object
is the actual critical atom frame

\[
C_{k,\Omega}^{(a)}\preceq A_k^{(a)}.
\]

The trigonometric model saturates this inequality exactly. Xi requires a
source-specific comparison of critical locations and residue weights against
the positive source Christoffel geometry.

## Replay

```text
PASS_X_105380_XI_SOURCE_MOMENT_LAYERS
122 exact rational checks
```

The replay covers formal quotient series, determinant identities,
concentration implications and trigonometric moment coefficients. It does not
replay the analytic saddle theorem or prove a critical capacity estimate.
