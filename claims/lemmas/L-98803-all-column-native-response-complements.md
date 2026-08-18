# L-98803 — The two-sort realization has one nonnegative native complement in every column

Claim ID: `L-98803`
Status: **CONDITIONAL ON THE OPEN L-98802 LIVE COMMON-PARENT INTERFACE**
Depends on: `L-98802`; frozen `L-91733`; terminal omission; positive radix-four inverse
RH status: **not assumed**

## 1. Ideal equality before finite realization

At every compact root fibre, `L-98800` realizes the exact signed component row
as residual-source row plus Hall bonus.  `L-98801` is an exact causal identity.
Positive endpoint integration and the common linear kernel therefore preserve,
before finite-realization error, the native row identity

\[
\boxed{
 \Omega_X
 =\Xi(d_{X,\rm ideal}^{\rm cur})
 +\sum_b\beta_bU_b\Omega_{Y_b}.
}
\]

The bonus is current-owned.  Every full child capacity is reserved once.

## 2. Retained-cell mismatch for every `q`

Let `E_X^I` be the cumulative adjacent-cell correction built only from retained
cells.  Frozen `L-91733` gives, for every physical `q>=2`,

\[
 |v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\qquad
 |\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K}.
\]

Together with the B-spline collar,

\[
\boxed{
 |\mathcal D_4v_q(C_X-E_X^I)|
 <\frac{971}{4q\sqrt K}.
}
\]

This includes the formerly missed range `2<=q<K` and introduces no cutoff atom.
Partial retained subcells are charged by their exact signed Stieltjes
comparison and are dominated by the same adjacent total-variation bound.

## 3. One thinning closes the nonterminal range

For `2<=q<=X/4`,

\[
 \Omega_X(q)>\frac4{3\sqrt q},
\]

and the frozen exact comparison gives

\[
 \frac{|\mathcal D_4v_q(C_X-E_X^I)|}{\Omega_X(q)}
 <\frac{129}{\sqrt K}.
\]

With

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130},
\]

one has exactly

\[
 \tau_K\left(1+\frac{129}{\sqrt K}\right)
 =\frac{\sqrt K+129}{\sqrt K+130}<1.
\]

Thus, after reserving all children, the realized current and child uses leave
strict detail slack

\[
\boxed{
 r_X(q)>\frac{\Omega_X(q)}{\sqrt K+130}>0
 \qquad(2\le q\le X/4),
}
\]

before an arbitrarily smaller knot-refinement charge.

## 4. Terminal range and omissions

The top source is removed before the quantizer.  Its response reserve is more
than `5033 X^(-3/2)`, while the complete terminal mismatch/collar overfill is
less than `4452 X^(-3/2)`.  Hence

\[
\boxed{581X^{-3/2}>0}
\]

remains.  Above the retained support, triangularity gives zero response.

## 5. Exact native slack identity

After the actual child rows `d_{Y_b}` are substituted, define

\[
 d_X=d_X^{\rm cur}+\sum_b\beta_bU_bd_{Y_b}.
\]

Then one and the same row gives the `q` and `4q` responses, and

\[
\boxed{
 s_X^{(4)}=\Omega_X-\Xi(d_X)\ge0.
}
\]

Moreover the reserved-capacity decomposition is

\[
\boxed{
 s_X^{(4)}
 =r_X+
  \sum_b\beta_bU_b
  [\Omega_{Y_b}-\Xi(d_{Y_b})].
}
\]

Positive radix-four inversion gives

\[
 s_X^{\rm ord}(q)
 =\sum_{h\ge0}2^hs_X^{(4)}(4^hq)\ge0,
\]

so ordinary and detail feasibility belong to the same physical row.

## 6. Port specialization

The preferred construction uses the zero-port specialization.  If the narrow
uncoloured root port is retained, it is current-only, formed once after all
Hall labels are summed, and has no child coordinate.
