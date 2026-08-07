# T-25301 — Signed constraint-dipole transport implies RH

Claim ID: `T-25301`  
Title: A subpolynomial-cost signed adjacent-flow repair of the parabolic carry seed proves the Riemann Hypothesis  
Status: **PROPOSED COMPLETE CONDITIONAL CHAIN — TRANSPORT OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #253  
Dependencies: `L-25301`; PR #248 `L-24501`, `L-24502`, `T-24501`; square-screw/Landau transfer on PRs #202/#218

## 1. Hypothesis

Assume that for every `epsilon>0` and all sufficiently large `X` there is a
flow `F_X` satisfying

\[
b_{F_X}(m)\ge0,
\tag{T-25301.1}
\]

\[
v_q(b_{F_X})\le q^{-1/2}\log(X/q)
\qquad(q=p^a\le X),
\tag{T-25301.2}
\]

and

\[
J_X(b_X^{(0)})-J_X(b_{F_X})
\le C_\epsilon X^\epsilon.
\tag{T-25301.3}
\]

By `L-25301`, (T-25301.3) is exactly the signed adjacent-flow transport cost.

## 2. Prime-ramp lower bound

The exact von-Mangoldt dual identity of `L-24501` gives, for every feasible
nonnegative `b`,

\[
\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\ge J_X(b).
\tag{T-25301.4}
\]

The parabolic seed satisfies

\[
J_X(b_X^{(0)})
\ge
4\sqrt X-6\log X+O(1).
\tag{T-25301.5}
\]

Therefore (T-25301.1)--(T-25301.3) imply

\[
\boxed{
\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\ge
4\sqrt X-X^{o(1)}.
}
\tag{T-25301.6}
\]

## 3. Square-screw transfer

At `X=N^2`, the exact square-screw identity has the form

\[
\Psi(2\log N)
=
4(N+N^{-1}-2)
-
\sum_{q\le N^2}
\frac{\Lambda(q)}{\sqrt q}
\log\frac{N^2}{q}
+
O(\log N).
\tag{T-25301.7}
\]

Equation (T-25301.6) gives

\[
\Psi(2\log N)\le N^{o(1)}.
\tag{T-25301.8}
\]

The unconditional derivative budget propagates the same upper exponent
between adjacent square samples. The sign-oriented Landau continuation theorem
for the zeta screw function then excludes every pole corresponding to a zero
with real part greater than `1/2`.

Functional-equation symmetry places every nontrivial zero on the critical line:

\[
\boxed{\mathrm{RH}.}
\tag{T-25301.9}
\]

## 4. Scope correction

The monotone cover hypothesis formerly proposed in `L-24502` cannot replace
(T-25301.1)--(T-25301.3): `R-25301` proves that it necessarily costs
`Omega(sqrt(X))`.

Thus the parabolic route now has one honest hinge:

\[
\boxed{
\text{signed constraint-dipole transport with subpolynomial objective cost}.
}
\]

This theorem is not proved here.

## 5. Exact status

```text
parabolic seed and objective                 inherited proposed exact
monotone Divisibility Cover                  refuted
constraint-dipole structure                  proposed complete
signed transport => prime-ramp lower bound   proposed complete
prime-ramp lower bound => RH                 inherited proposed transfer
signed transport                             open / RH-bearing
Riemann Hypothesis                           unproved
```
