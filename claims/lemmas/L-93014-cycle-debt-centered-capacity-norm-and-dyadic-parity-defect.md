# L-93014 - Cycle Debt has a centered capacity norm and one joint dyadic parity defect

Claim ID: `L-93014`  
Status: **PROPOSED COMPLETE EXACT FINITE NORMAL FORM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: PR #272 at `fa787eed202aef67b2a4e23a64aeedfb05f93645`, especially `L-27205` and `L-27207`; PR #474 at `56eeaccb2b041fdf68b6e718bad85032ecbdc66a`, especially `L-93010`--`L-93012`  
Scope: the exact finite Cycle-Debt LP and its critical dyadic source identity; no bound for the final parity functional and no RH conclusion

## 1. Capacity potential and the asymmetric dual

Fix an endpoint `X` and a balanced split family. For an allowed split

\[
e=(n,j),\qquad n=j+k,
\]

write

\[
\delta_F(e)=F(n)-F(j)-F(k).
\tag{L-93014.1}
\]

Retain the exact capacity potential

\[
\mathcal G_X(n)
=\sum_{q=2}^{n}\frac1{\sqrt q}
  \left\lfloor\frac nq\right\rfloor,
\qquad \mathcal G_X(1)=0.
\tag{L-93014.2}
\]

Its split defect is the capacity weight

\[
\boxed{\delta_{\mathcal G_X}(e)=\omega_e.}
\tag{L-93014.3}
\]

Let `r` be any size-conserving node divergence in the split-column range, and define

\[
K_\omega(r)=\langle r,\mathcal G_X\rangle.
\tag{L-93014.4}
\]

The exact Cycle-Debt dual of `L-27205` is

\[
\mathfrak N_\omega(r)
=
\max_F[-\langle r,F\rangle],
\qquad
0\le\delta_F(e)\le\omega_e,
\qquad F(1)=0.
\tag{L-93014.5}
\]

## 2. Center the capacity interval

Put

\[
H=F-\frac12\mathcal G_X.
\tag{L-93014.6}
\]

Then

\[
0\le\delta_F(e)\le\omega_e
\quad\Longleftrightarrow\quad
|\delta_H(e)|\le\frac12\omega_e.
\tag{L-93014.7}
\]

Define the symmetric centered capacity ball

\[
\boxed{
\mathcal B_X
=
\left\{
H:H(1)=0,\ 
|\delta_H(e)|\le\frac12\omega_e
\text{ for every allowed }e
\right\}.
}
\tag{L-93014.8}
\]

Substitution in the objective, together with the symmetry
`H in B_X iff -H in B_X`, gives the exact identity

\[
\boxed{
\mathfrak N_\omega(r)+\frac12K_\omega(r)
=
\sup_{H\in\mathcal B_X}|\langle r,H\rangle|.
}
\tag{L-93014.9}
\]

This is an equality, not an upper bound.

For every exact signed flow `d` with divergence `r`,

\[
\sum_e\omega_ed_e=K_\omega(r),
\]

so

\[
\sum_e\omega_e|d_e|
=
K_\omega(r)+2\sum_e\omega_e(-d_e)_+.
\tag{L-93014.10}
\]

Minimizing and using (L-93014.9) yields the equivalent weighted-variation duality

\[
\boxed{
\min_{\partial d=r}\sum_e\omega_e|d_e|
=
2\sup_{H\in\mathcal B_X}|\langle r,H\rangle|.
}
\tag{L-93014.11}
\]

Thus the two-channel formulation of `L-93010` and the centered support norm are
the primal and dual forms of one symmetric transport problem.

## 3. Markov form

Write

\[
h(n)=\frac{H(n)}n.
\]

For one split action, let

\[
P_eh=\frac jn h(j)+\frac kn h(k),
\qquad
c_e=\frac{\omega_e}{n}.
\]

Since

\[
\delta_H(e)=n[h(n)-P_eh],
\]

the centered ball is exactly

\[
\boxed{|h(n)-P_eh|\le\frac12c_e.}
\tag{L-93014.12}
\]

The asymmetric lower and upper Bellman obstacles of `L-93011` have become one
centered martingale-difference ball. No positivity or monotonicity of `H` is
imposed.

## 4. The critical baseline is only logarithmic squared

For the critical target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

let `r_X` be its exact multiples-Mobius divergence. Divisor switching gives

\[
\boxed{
K_X:=K_\omega(r_X)
=
\sum_{q=2}^{X}\frac{\log(X/q)}q
=
O(\log^2(2X)).
}
\tag{L-93014.13}
\]

Put

\[
\mathfrak S_X
=
\sup_{H\in\mathcal B_X}|\langle r_X,H\rangle|.
\tag{L-93014.14}
\]

Then

\[
\boxed{
\mathfrak S_X
=
\mathfrak N_\omega(r_X)+\frac12K_X.
}
\tag{L-93014.15}
\]

Consequently a polylogarithmic bound for `S_X` implies a polylogarithmic
Cycle-Debt bound. Centering removes the one-sided geometry and the fixed positive
baseline; it does not assume the RH-bearing estimate.

## 5. Exact dyadic source decomposition

Let

\[
X=2Y,\qquad \alpha=2^{-1/2}.
\]

The critical scaling is

\[
w_X(2q)=\alpha w_Y(q).
\]

By `L-27207`,

\[
\boxed{
r_X
=
\alpha\mathcal D_2r_Y
+w_X(2)\,\partial T_2
+\sum_{a=1}^{Y-1}r_X(2a+1)\,\partial E_{2a}.
}
\tag{L-93014.16}
\]

Here

\[
\partial T_2=e_2-2e_1,
\qquad
\partial E_{2a}=e_{2a+1}-e_{2a}-e_1.
\]

For `H in B_X`, define its gauge-corrected even trace on the lower endpoint by

\[
\boxed{
(\mathcal R_2H)(m)
=
\sqrt2\,[H(2m)-mH(2)].
}
\tag{L-93014.17}
\]

Then `(\mathcal R_2H)(1)=0`. Since `r_Y` conserves size,

\[
\sum_m m r_Y(m)=0,
\]

and therefore

\[
\alpha\langle\mathcal D_2r_Y,H\rangle
=
\frac12\langle r_Y,\mathcal R_2H\rangle.
\tag{L-93014.18}
\]

Define the complete odd commutator pairing

\[
\boxed{
\mathcal O_X(H)
=
\sum_{a=1}^{Y-1}
r_X(2a+1)[H(2a+1)-H(2a)].
}
\tag{L-93014.19}
\]

Pairing (L-93014.16) with `H`, before taking any separate absolute values,
gives

\[
\boxed{
\langle r_X,H\rangle
=
\frac12\langle r_Y,\mathcal R_2H\rangle
+w_X(2)H(2)
+\mathcal O_X(H).
}
\tag{L-93014.20}
\]

This is the exact centered-dual counterpart of the paired
lifted-flow/odd-commutator normal form in `L-27207`.

## 6. The bottom charge is harmless

The edge `T_2=[2,1]` has

\[
\omega_{2,1}=2^{-1/2}.
\]

Because `H in B_X` and `H(1)=0`,

\[
|H(2)|\le\frac1{2\sqrt2}.
\tag{L-93014.21}
\]

Also

\[
w_X(2)=2^{-1/2}\log(X/2),
\]

so

\[
\boxed{
|w_X(2)H(2)|
\le\frac14\log(X/2).
}
\tag{L-93014.22}
\]

The immutable bottom logarithmic charge is not the closing obstruction.

## 7. The even trace and odd capacity leakage

For a lower split `e=(n,j)`, let `2e=(2n,2j)` be its doubled split. The linear
gauge in (L-93014.17) has zero split defect, so

\[
\delta_{\mathcal R_2H}(e)
=
\sqrt2\,\delta_H(2e).
\tag{L-93014.23}
\]

The exact capacity decomposition of `L-27207` is

\[
\omega_{2e}
=
2^{-1/2}\omega_e+\omega_{\rm odd}(2e).
\tag{L-93014.24}
\]

Thus every even trace obeys

\[
\boxed{
|\delta_{\mathcal R_2H}(e)|
\le
\frac12\omega_e
+\frac1{\sqrt2}\omega_{\rm odd}(2e).
}
\tag{L-93014.25}
\]

The only reason `R_2H` need not belong to the lower centered ball is the same
odd-column leakage that appears in the primal factor-one-half contraction.

## 8. One joint parity functional

The even-trace overrun in (L-93014.25) and the odd commutator in
(L-93014.19) must not be bounded separately before their source-specific
cancellation. Define the centered dyadic parity defect by

\[
\boxed{
\begin{aligned}
\mathfrak P_X
=
\Bigg[
&\sup_{\substack{H\in\mathcal B_X\\ \sigma\in\{-1,1\}}}
\left\{
\frac{\sigma}{2}\langle r_Y,\mathcal R_2H\rangle
+\sigma\mathcal O_X(H)
\right\}\\
&-\frac12\mathfrak S_Y
\Bigg]_+.
\end{aligned}
}
\tag{L-93014.26}
\]

The supremum is one finite linear program over the complete higher-scale
centered ball. The inherited even trace and the signed odd commutator remain in
the same objective.

Taking the supremum in (L-93014.20) and using only (L-93014.22) gives

\[
\boxed{
\mathfrak S_{2Y}
\le
\frac12\mathfrak S_Y
+\frac14\log Y
+\mathfrak P_{2Y}.
}
\tag{L-93014.27}
\]

This is a genuine factor-one-half recurrence in the complete centered
Cycle-Debt norm. Its sole same-scale term is the joint parity functional.

## 9. A fail-closed closing theorem

The remaining centered theorem is:

> **Centered Dyadic Parity (`CDP`).** There are fixed constants `A,C` such that
> \[
> \mathfrak P_{2Y}\le C\log^A(2Y)
> \]
> for every sufficiently large `Y`.

If CDP holds, (L-93014.27) gives a polylogarithmic bound for `S_X` on even
endpoints. The exact unit-endpoint interpolation of `L-27208`, together with
(L-93014.13), extends it to odd endpoints. Equation (L-93014.15) then gives
polylogarithmic Cycle Debt, and the resident prime-ramp/Landau consumer gives RH.

Thus

\[
\boxed{
\mathrm{CDP}
\Longrightarrow
\text{polylog Cycle Debt}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-93014.28}
\]

CDP is not proved here.

Directed rational enclosures may certify each finite CDP instance. For the
actual critical source, source coefficients as well as capacities must be
authenticated symbolically or by outward intervals; see `R-93016`.

## 10. Proof boundary

Established exactly:

1. asymmetric Cycle-Debt dual equals a centered capacity support norm;
2. weighted total-variation duality;
3. centered Markov/Bellman form;
4. critical baseline `O(log^2 X)`;
5. gauge-corrected even trace;
6. exact half-scale/odd-commutator pairing;
7. logarithmic bottom-charge bound;
8. localization of every trace-capacity excess to odd columns;
9. the factor-one-half centered recurrence (L-93014.27).

Open:

1. the polylogarithmic CDP bound;
2. Cycle Debt;
3. RH.
