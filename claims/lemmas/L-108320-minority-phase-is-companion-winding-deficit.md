# L-108320 — Minority endpoint phase is exactly the direct-companion winding deficit

Claim ID: `L-108320`  
Status: **PROVED EXACT FINITE-WINDOW THEOREM**  
Created: 2026-08-31  
Depends on: `L-108310`, `L-108311`  
RH status: **not assumed**

Let `K` be odd and let

\[
E_{K,\sigma,\epsilon}
=
f^{(K)}+i\sigma\epsilon f.
\]

Assume first that the zeros

\[
c_1<\cdots<c_M
\]

of `f^(K)` in the regular window are simple and not shared with `f`. Put

\[
s_j
=
\operatorname{sgn}
{f(c_j)\over f^{(K+1)}(c_j)}
\in\{+1,-1\}.
\]

Let

\[
\Delta_I\arg E_{K,\sigma,\epsilon}
\]

denote the unwrapped real-axis phase change, equivalently the integral of the
phase derivative from `L-108310.3`.

At `c_j`, the local model is

\[
f^{(K)}(x)
=f^{(K+1)}(c_j)(x-c_j)+O((x-c_j)^2).
\]

The Cauchy angle therefore gives

\[
\boxed{
\lim_{\epsilon\downarrow0}
{1\over\pi}
\Delta_I\arg E_{K,\sigma,\epsilon}
=
-\sigma\sum_{j=1}^M s_j
+
\mathcal B_{K,\sigma}(I),
}
\tag{L-108320.1}
\]

where `B` is the explicit endpoint/common-zero branch ledger. On a regular
exhaustion it is `O(1)`.

If `U_+` and `U_-` count the two residue signs, then

\[
M=U_++U_-,
\qquad
U_+-U_-=\sum_js_j.
\]

Consequently

\[
\boxed{
2\min(U_+,U_-)
=
M-\left|\sum_js_j\right|.
}
\tag{L-108320.2}
\]

Combining (L-108320.1) and (L-108320.2),

\[
\boxed{
M-2\min(U_+,U_-)
=
\lim_{\epsilon\downarrow0}
{1\over\pi}
\left|
\Delta_I\arg E_{K,+,\epsilon}
-\pi\mathcal B_{K,+}(I)
\right|.
}
\tag{L-108320.3}
\]

Thus the direct endpoint descent of `L-108311` can be written without a
minority count:

\[
\boxed{
N_{\mathbb R}(f;I)
\ge
\lim_{\epsilon\downarrow0}
{1\over\pi}
\left|
\Delta_I\arg E_{K,+,\epsilon}
-\pi\mathcal B_{K,+}(I)
\right|
-1-\mathcal E_{K,\rm reg}(I).
}
\tag{L-108320.4}
\]

The high-derivative count has been converted into the maximal possible phase
winding of one direct companion.

## Argument-principle interface

Let `Omega` be a rectangle whose lower horizontal side is the real window and
on whose boundary `E` has no zero. Then

\[
\boxed{
\Delta_I\arg E
=
2\pi N_\Omega(E)
-
\Delta_{\partial\Omega\setminus I}\arg E,
}
\tag{L-108320.5}
\]

with the induced orientation. Thus the real-axis winding may be attacked by:

```text
half-plane/strip zeros of the direct companion;
safe-line phase or prime-explicit-formula data;
vertical-side and endpoint flux.
```

Equation (L-108320.5) is an exact ledger, not a claim that any of those terms
is small.

## Multiplicities

For even tangencies and common zeros, retain the half-weights and multiplicity
charges already explicit in `L-108310` and the regularization term in
`L-108311`. No simple-zero conclusion is inferred from the winding identity.
