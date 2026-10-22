# L-24535 — The Möbius response of every divisor adjacent commutator is the rank-one value `-1`

Claim ID: `L-24535`  
Title: For the central bottom-mass consumer, a complete divisor-source boundary is measured only by its signed total coefficient, not by its ambient atomic or fragmentation norm  
Status: **PROPOSED COMPLETE — exact finite pairing identity**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: `L-24534`; elementary Möbius inversion  
Scope: scalar boundary adapter for `T-24508`

## 1. Complete central-tree response

Let `T_m` be the complete central fragmentation tree rooted at `m`.  For every
integer carry column `q>=2`,

\[
L_q(T_m)=\left\lfloor{m\over q}\right\rfloor.
\tag{L-24535.1}
\]

By Möbius inversion,

\[
\sum_{q=1}^{m}\mu(q)\left\lfloor{m\over q}\right\rfloor=1.
\]

The omitted `q=1` term equals `m`.  Therefore

\[
\boxed{
\sum_{q=2}^{m}\mu(q)L_q(T_m)=1-m.
}
\tag{L-24535.2}
\]

## 2. Adjacent commutator response

For

\[
E_{m-1}=T_m-T_{m-1}
\qquad(m\ge2),
\]

subtract (L-24535.2) at adjacent endpoints.  One obtains

\[
\boxed{
\sum_{q=2}^{m}\mu(q)L_q(E_{m-1})=-1.
}
\tag{L-24535.3}
\]

This agrees with the divisor-indicator form

\[
L_q(E_{m-1})=\mathbf1_{q\mid m},
\]

because

\[
\sum_{\substack{q\mid m\\q\ge2}}\mu(q)=-1
\qquad(m>1).
\]

The value is independent of `m`.

## 3. Rank-one source functional

For an arbitrary finite real divisor source `sigma_2,...,sigma_N`, put

\[
\Phi(\sigma)=\sum_{m=2}^{N}\sigma_mE_{m-1}.
\]

Then exact finite rearrangement and (L-24535.3) give

\[
\boxed{
\sum_{q=2}^{N}\mu(q)L_q(\Phi(\sigma))
 =-\sum_{m=2}^{N}\sigma_m.
}
\tag{L-24535.4}
\]

Equivalently, if

\[
g(q)=\sum_{\substack{m\le N\\q\mid m}}\sigma_m,
\]

then

\[
\boxed{
\sum_{q=2}^{N}\mu(q)g(q)
 =-\sum_{m=2}^{N}\sigma_m.
}
\tag{L-24535.5}
\]

Thus all physical source labels disappear from the Möbius scalar after the
complete divisor family is recombined.

## 4. Consequence for the terminal atomic-norm obstruction

`R-24530` shows that the stopped outer-anchor boundary has ambient norm

\[
\sum_m\sqrt m|\sigma_m|\gg X.
\]

Equation (L-24535.4) shows that this norm is irrelevant to the bottom-mass
consumer.  What matters is only

\[
\sum_m\sigma_m,
\]

with its sign and all eta/dyadic siblings retained.

This is not an automatic bound.  The outer-anchor family may still have a
macroscopic signed total if it is separated from its analytic parity partner.
The gain is exact scope:

```text
ambient terminal proof:   must bound every source atom;
Mobius scalar proof:       must bound one signed source total.
```

The latter is the quantity on which the eta boundary-comb mass and its strict
paired contraction act.

## 5. Compatibility with source integration by parts

Using the tree expansion of `L-24534`,

\[
\Phi(\sigma)
 =\sigma_NT_N+
  \sum_{m=2}^{N-1}(\sigma_m-\sigma_{m+1})T_m.
\]

Pairing with Möbius and using (L-24535.2) yields

\[
\begin{aligned}
&\sigma_N(1-N)
 +\sum_{m=2}^{N-1}
  (\sigma_m-\sigma_{m+1})(1-m)\\
&\qquad=-\sum_{m=2}^{N}\sigma_m,
\end{aligned}
\tag{L-24535.6}
\]

which is a direct summation-by-parts check of (L-24535.4).  Hence the positive
Hausdorff-tree realization and the rank-one scalar response are fully
compatible.

## 6. Unit-source firewall

The identity begins at `m=2`.  A source at the unit node is not represented by
an adjacent commutator and is not annihilated or absorbed here.  In the complete
Möbius Riesz coordinate it is precisely the explicit term

\[
\log X
\]

in `L-24533.6`.

This matches the unit-source firewall on the factor-five/bottom-charge branches:
positive logarithmic carry moments can control the transverse divisor source,
but the unit boundary must be retained in the final signed recurrence.

## 7. Correct scalar production target

A valid continuation of PR #304's boundary work for the central scalar should
therefore prove a signed identity of the form

\[
\sum_{m\ge2}\sigma_{X,m}
 =\sum_r\theta_r\mathcal D(Y_r)
  +O(\log^A X),
\]

with lower scales `Y_r<=X/2` and total coefficient below one.  No estimate of

\[
\sum_m\sqrt m|\sigma_{X,m}|
\]

is required or useful for this consumer.

## 8. Proof boundary

Proved exactly:

- complete-tree Möbius response;
- adjacent-commutator response `-1`;
- rank-one total-source formula;
- compatibility with the monotone tree layer cake.

Open:

- a strict lower-scale recurrence for the signed total source after eta/dyadic
  recombination;
- RH.
