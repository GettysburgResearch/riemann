# L-32412 — Euler–Blaschke model-space kernel and finite-horizon Gram

Claim ID: `L-32412`  
Title: The critical Euler–Blaschke source is an exact one-state unitary scattering system, and its complete independent-frequency defect is one explicit positive model-space kernel  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/OPERATOR LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-11  
Dependencies: `L-32404`; elementary Hardy-space and state-space algebra  
Scope: exact local-Euler source accounting on scalar or Hilbert-valued logarithmic slabs; no arithmetic energy estimate or RH conclusion

## 1. The critical inner factor

Fix

\[
Q>1,
\qquad
L=\log Q,
\qquad
a=Q^{-1/2},
\qquad
b=\sqrt{1-a^2}.
\]

In the shifted variable

\[
s=\frac12+z,
\]

the normalized Euler–Blaschke factor of `L-32404` is

\[
\boxed{
\phi_Q(z)
=Q^{-1/2}E_Q\!\left(\frac12+z\right)
=\frac{a-e^{-Lz}}{1-ae^{-Lz}}.
}
\tag{L-32412.1}
\]

It is analytic in `Re z>0`, has modulus one on `Re z=0`, and has modulus strictly below one in the open right half-plane.

## 2. Exact de Branges--Rovnyak kernel

For `Re z>0` and `Re w>0`, direct algebra gives

\[
\begin{aligned}
1-\phi_Q(z)\overline{\phi_Q(w)}
&=\frac{(1-a^2)
 [1-e^{-L(z+\bar w)}]}
 {(1-ae^{-Lz})(1-ae^{-L\bar w})}.
\end{aligned}
\tag{L-32412.2}
\]

Since

\[
\frac{1-e^{-L(z+\bar w)}}{z+\bar w}
=\int_0^L e^{-tz}e^{-t\bar w}\,dt,
\]

one obtains the exact kernel factorization

\[
\boxed{
\begin{aligned}
K_Q(z,w)
&:=\frac{1-\phi_Q(z)\overline{\phi_Q(w)}}{z+\bar w}\\
&=(1-a^2)
\int_0^L
\frac{e^{-tz}}{1-ae^{-Lz}}
\overline{
\frac{e^{-tw}}{1-ae^{-Lw}}
}\,dt.
\end{aligned}}
\tag{L-32412.3}
\]

Therefore `K_Q` is positive semidefinite. More explicitly, for arbitrary points `z_1,...,z_m` in the right half-plane and scalars `v_1,...,v_m`,

\[
\boxed{
\sum_{r,s}v_r\overline{v_s}K_Q(z_r,z_s)
=(1-a^2)\int_0^L
\left|
\sum_r v_r\frac{e^{-tz_r}}{1-ae^{-Lz_r}}
\right|^2dt
\ge0.
}
\tag{L-32412.4}
\]

Thus the independent-frequency defect of the local Euler factor is not an unspecified positive kernel: it is one explicit rank-continuous Gram over a single logarithmic slab.

## 3. Exact one-state unitary colligation

Let `H` be any real or complex Hilbert space and let `(u_m)_(m>=0)` be an `H`-valued sequence. Define the state and output recursively by

\[
\boxed{
\begin{aligned}
x_{m+1}&=a x_m+b u_m,\\
y_m&=-b x_m+a u_m.
\end{aligned}}
\tag{L-32412.5}
\]

The colligation matrix

\[
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
\]

is unitary. Hence, at every step,

\[
\boxed{
\|x_{m+1}\|_H^2+\|y_m\|_H^2
=\|x_m\|_H^2+\|u_m\|_H^2.
}
\tag{L-32412.6}
\]

Summing from `m=0` to `M-1` gives the complete finite-horizon identity

\[
\boxed{
\sum_{m=0}^{M-1}\|u_m\|_H^2+\|x_0\|_H^2
=
\sum_{m=0}^{M-1}\|y_m\|_H^2+\|x_M\|_H^2.
}
\tag{L-32412.7}
\]

No cross term has been discarded or estimated.

With zero incoming state and delay variable `w`, the transfer function of (L-32412.5) is

\[
\frac{Y(w)}{U(w)}
=\frac{a-w}{1-aw}.
\tag{L-32412.8}
\]

Taking

\[
w=e^{-Lz}
\]

recovers exactly `phi_Q(z)`.

## 4. Exact critical source-delay normal form

The local source comb of `L-32404` is

\[
e_Q(1)=1,
\qquad
e_Q(Q^r)=-(Q-1)\quad(r\ge1).
\]

At square-root normalization, one delay by `Q^r` carries the factor `Q^{-r/2}=a^r`. Therefore its causal scale-transfer series is

\[
\begin{aligned}
H_Q(w)
&=1-(Q-1)\sum_{r\ge1}a^r w^r\\
&=\frac{1-\sqrt Q\,w}{1-a w}\\
&=\boxed{\sqrt Q\,\frac{a-w}{1-aw}}
=\sqrt Q\,\phi_Q(w).
\end{aligned}
\tag{L-32412.9}
\]

Let `U_m` denote any square-root-normalized unsourced centered-interval field on the logarithmic scales

\[
X_m=Q^mX_0.
\]

Let `V_m` be the field after convolution by the complete local source `e_Q`. Then, coefficientwise and before any norm,

\[
\boxed{
V_m
=U_m-(Q-1)\sum_{r\ge1}Q^{-r/2}U_{m-r},
}
\tag{L-32412.10}
\]

with the causal convention `U_k=0` before the initial scale. Equivalently,

\[
\boxed{
\frac{V}{\sqrt Q}=\phi_Q(S)U,
}
\tag{L-32412.11}
\]

where `S` is one backward logarithmic-scale delay.

For `Q=4`,

\[
\boxed{
\frac{V_m}{2}
=U_m-\frac32U_{m-1}-\frac34U_{m-2}-\frac38U_{m-3}-\cdots,
}
\tag{L-32412.12}
\]

or, in first-order state form, the recursion (L-32412.5) with `a=1/2` and `b=sqrt(3)/2`.

## 5. Complete independent-frequency accounting

Take `H` in Section 3 to be any finite physical carry-position space or any finite direct sum of such spaces. The identity (L-32412.7) then holds for the entire normal Gram, including every cross-coordinate term.

Equivalently, for independent frequencies `z,w`, the source insertion changes the Cauchy/Hardy kernel by exactly the positive model-space term (L-32412.3). Therefore the local Euler source admits the fail-closed decomposition

```text
incoming independent-frequency Gram
=
source-filtered outgoing Gram
+ one positive slab model-space Gram
+ incoming state Gram
- outgoing state Gram.
```

There is no generic Cauchy--Schwarz loss and no possibility of spending the same local-Euler reserve twice: the terminal state is the unique unpaid coordinate in the unitary colligation.

## 6. Application to the Q=4 RH source

For the `Q=4` generalized-prime centered-interval input and the correctly typed physical output of `L-32407`, (L-32412.10)--(L-32412.12) identify the coefficient-one critical return explicitly.

Combined with `L-32411`, the current architecture is now:

```text
balanced Q=4 physical row
    -> asymptotically negligible fraction of its Selberg reserve;

local Euler source/filter
    -> exact unitary all-pass scattering;

complete source cross terms
    -> one explicit positive model-space Gram;

unpaid current-scale coordinate
    -> the single terminal scattering state.
```

This is precisely the accounting shape required by a coefficient-one delayed recurrence. The arithmetic theorem proving that the complete reflected Selberg reserve pays every nonterminal component is still separate.

## 7. Scope firewall

The unitary identity does **not** make the principal source small. Globally,

\[
|\phi_Q(it)|=1,
\]

so the filter preserves critical-line energy. It also cannot by itself exclude an off-line pole.

The valid conclusion is only:

\[
\boxed{
\text{local-Euler source accounting is exact and lossless, with one state.}
}
\]

A claim that (L-32412.7) alone proves a subexponential energy bound is rejected.

## 8. Proof boundary

Closed exactly here:

1. the independent-frequency model-space kernel;
2. its positive integral factorization;
3. a Hilbert-valued unitary colligation;
4. exact finite-horizon energy conservation;
5. the complete critical source-delay normal form;
6. one-state no-double-spend accounting.

Open:

1. source-complete reflected Selberg reserve accounting;
2. the resulting coefficient-one delayed block recurrence;
3. RH.
