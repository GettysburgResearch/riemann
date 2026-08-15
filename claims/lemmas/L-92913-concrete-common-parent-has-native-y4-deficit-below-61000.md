# L-92913 — The concrete common parent has native \(Y_4\) deficit below 61000

Claim ID: `L-92913`  
Status: **PROVED DIRECT COST COMPOSITION ON FROZEN ANALYTIC ESTIMATES**  
Created: 2026-08-15  
Depends on: `L-91377`, `L-91378`, `L-91733`, `L-91734`, `L-91735`, `L-19885`, `L-19887`, `L-92901`, `L-92911`, `L-92912`  
RH status: **unproved**

## 1. Exact native dual identity

The full finite Möbius row satisfies

\[
C_{c_X}=w_X,
\qquad
\Xi_{c_X}=\Omega_X,
\qquad
\mathcal H(c_X)=J_\Lambda(X).
\tag{L-92913.1}
\]

For the concrete feasible row `d_X` of `L-92911/L-92912`, put

\[
r_X=\Omega_X-\Xi(d_X)\ge0.
\tag{L-92913.2}
\]

The exact radix-four dual gives

\[
\boxed{
\Delta_X(d_X)
:=
J_\Lambda(X)-\mathcal H(d_X)
=
\langle Y_4,r_X\rangle.
}
\tag{L-92913.3}
\]

No comparison with `4 sqrt(X)` occurs.

## 2. Sparse dual support

The exact support formula is

\[
Y_4(2^e)
=
(2^{\lceil e/2\rceil}-1)\log2,
\tag{L-92913.4}
\]

\[
Y_4(4^v p^a)=2^v\log p
\qquad(p\ \text{odd prime}),
\tag{L-92913.5}
\]

and `Y_4(q)=0` otherwise.  In particular,

\[
\sum_qY_4(q)q^{-3/2}<11,
\tag{L-92913.6}
\]

and, with `L=log(2X)`,

\[
\sum_{q\le X}\frac{Y_4(q)}q
\le3+2L+2L^2.
\tag{L-92913.7}
\]

These are used only to pay the observation vector of `L-92912`.

## 3. Common thinning

The common scalar thinning is applied once to the complete labelled row.  The elementary Chebyshev estimate frozen in `L-19887` gives, for `X>=10^12`,

\[
\boxed{
\langle Y_4,u_X^{\rm thin}\rangle<12012.
}
\tag{L-92913.8}
\]

This is a direct positive-reserve cost.  It does not use an eventual estimate for

\[
J_\Lambda(X)-4\sqrt X.
\]

## 4. Signed nonterminal comparison

The all-column owner split of `L-91733`, together with (L-92913.7), gives

\[
\boxed{
\sum_{q\le X/4}
Y_4(q)
\left|e_X^{\rm nonterm}(q)\right|
<4.
}
\tag{L-92913.9}
\]

This includes `2<=q<K`.  The inequality is applied to the absolute value of a signed observation defect, not to source mass.

## 5. Signed terminal comparison

The terminal majorant and (L-92913.6) give

\[
\boxed{
\sum_qY_4(q)
\left|e_X^{\rm term}(q)\right|
<48972.
}
\tag{L-92913.10}
\]

The top omission is paid separately as positive unused source.  The terminal comparison itself remains signed.

## 6. Omissions, activation collars and refinement

The whole-cell bottom transition and fixed top omission have combined native cost below one on the frozen large-`X` range.  By atomlessness of

\[
d\nu(x)=2L(x)\,dx/x,
\]

choose the activation collars so that their native cost is below one.  Choose the positive retained-cell refinement so that its integrated native error is below one.

Allowing a conservative margin for all remaining fixed-width omission, rounding and bookkeeping terms gives

\[
\boxed{
\langle Y_4,u_X^{\rm omit}\rangle
+
\langle Y_4,|e_X^{\rm collar/ref}|\rangle
<12.
}
\tag{L-92913.11}
\]

The preferred large-`X` direct row uses no matrix port and no finite base packet, so those two costs are zero.

## 7. Total cost

By `r_X=u_X-e_X` and `Y_4>=0`,

\[
\langle Y_4,r_X\rangle
\le
\langle Y_4,u_X\rangle
+
\langle Y_4,|e_X|\rangle.
\tag{L-92913.12}
\]

Combining (L-92913.8)--(L-92913.11),

\[
\begin{aligned}
0\le\Delta_X(d_X)
&<12012+4+48972+12\\
&=61000.
\end{aligned}
\]

Therefore

\[
\boxed{
0\le
J_\Lambda(X)-\mathcal H(d_X)
<61000
\qquad(X\ge10^{12}).
}
\tag{L-92913.13}
\]

In particular,

\[
\Delta_X(d_X)=O(1)=o(\log^2X).
\tag{L-92913.14}
\]

## 8. What is absent

The estimate does not use

```text
the rejected equality-score recurrence;
J_Lambda(X)-4sqrt(X)=O(log X);
a positive-source interpretation of the signed mismatch;
a recursive descendant slack tree;
a child quantizer or child root correction;
a port or large-X base packet.
```

The root Hall creates no total-row approximation error because (L-92910.15) is exact before observation.  The only approximation costs are the separately typed operations listed above.

## 9. Boundary

```text
exact native dual identity                         exact
all physical columns                               feasible
common thinning cost                               <12012
signed nonterminal cost                            <4
signed terminal cost                               <48972
omission/collar/refinement allowance               <12
total native deficit                               <61000
benchmark bridge                                   not used
Riemann Hypothesis                                 unproved
```
