# L-92910 — Compact factor-67 Hall fibres give one concrete positive labelled physical row

Claim ID: `L-92910`  
Status: **PROVED EXACT COMPACT-FIBRE COMPILER ON FROZEN HALL/PROFILE INPUTS**  
Created: 2026-08-15  
Frozen inputs: `L-91112.25--.26`, `L-91362`, `L-91650`, `L-91682`, `L-91688`, `L-91690`, `L-91692`  
RH status: **unproved**

## 1. The actual finite fibre

Fix `1<=x<67`.  Only squarefree divisors of

\[
P_{61}=\prod_{p\le61}p
\]

can occur.  For every squarefree `k<=x`, put

\[
T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k},
\qquad
S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k},
\tag{L-92910.1}
\]

and, for every physical component row `j>=2`,

\[
A_{x,j}(k)=\frac1{\sqrt k}Q_{x/k}(j).
\tag{L-92910.2}
\]

The finite signed source occurrence is labelled

\[
(x,k,\operatorname{sgn}\mu(k)).
\]

Write

\[
E_x=\{e\le x:\mu(e)=1\},
\qquad
O_x=\{o\le x:\mu(o)=-1\}.
\tag{L-92910.3}
\]

No continuum or finite-realization error has yet been introduced.

## 2. Deterministic Hall transport

The directed prefix theorem of `L-91690` supplies a deterministic leftmost flow

\[
t_x(o,e)\ge0,
\qquad
t_x(o,e)>0\Longrightarrow e\le o,
\tag{L-92910.4}
\]

with

\[
\sum_e t_x(o,e)=T_x(o),
\qquad
\sum_o t_x(o,e)\le T_x(e).
\tag{L-92910.5}
\]

Put

\[
r_x(e)=T_x(e)-\sum_o t_x(o,e)\ge0,
\qquad
\nu_x(e)=\frac{r_x(e)}{T_x(e)}\in[0,1].
\tag{L-92910.6}
\]

Every positive even occurrence is divided into its residual fraction and its matched edge fractions.  Every odd occurrence is exhausted by its matched edges.  These fractions sum exactly to the original occurrence, so the Hall operation neither duplicates nor invents source.

## 3. Residual physical row

Define the positive residual row

\[
R_{x,j}
=
\sum_{e\in E_x}\nu_x(e)A_{x,j}(e)
=
\sum_e r_x(e)\rho_{x,j}(e),
\tag{L-92910.7}
\]

where

\[
\rho_{x,j}(k)
=
\frac{A_{x,j}(k)}{T_x(k)}
=
\frac{Q_{x/k}(j)}{4\sqrt{x/k}-3}.
\tag{L-92910.8}
\]

Every term in (L-92910.7) is an actual positive canonical endpoint row.  Its source label is

```text
(x, even divisor e, HALL_RESIDUAL, residual fraction nu_x(e)).
```

The residual target is exactly the signed target:

\[
\sum_e r_x(e)
=
\sum_{k\le x}\mu(k)T_x(k).
\tag{L-92910.9}
\]

The score ratio in `L-91690` gives

\[
\sum_e\nu_x(e)S_x(e)
\ge
\sum_{k\le x}\mu(k)S_x(k).
\tag{L-92910.10}
\]

This is superordination, not a false all-coordinate equality.

## 4. Hall-edge row bonus

For every used edge `(o,e)`, define

\[
B_{x,o,e;j}
=
t_x(o,e)
\bigl[\rho_{x,j}(e)-\rho_{x,j}(o)\bigr].
\tag{L-92910.11}
\]

The frozen target-normalized row theorem says that

\[
e\le o
\Longrightarrow
\rho_{x,j}(e)\ge\rho_{x,j}(o),
\tag{L-92910.12}
\]

so `B_(x,o,e;j)>=0` for every component coordinate.  Put

\[
B_{x,j}=\sum_{o,e}B_{x,o,e;j}\ge0.
\tag{L-92910.13}
\]

This bonus is not unused source.  Its provenance label is the ordered pair of the two already consumed matched fractions:

```text
(x, odd divisor o, even divisor e, HALL_EDGE,
 t_x(o,e)/T_x(o), t_x(o,e)/T_x(e)).
```

The source coordinate of the bonus is zero.  The label certifies the exact cancellation which generated its physical row, and prevents either matched fraction from appearing anywhere else.

The available declared-score reserve of the same edge is

\[
\Sigma_{x,o,e}
=
t_x(o,e)
\left[
\frac{S_x(o)}{T_x(o)}
-
\frac{S_x(e)}{T_x(e)}
\right]\ge0.
\tag{L-92910.14}
\]

Thus the Hall edge is target-null and row-positive, while the same matched source pair leaves nonnegative declared-score reserve.  No equality between this reserve and the literal entropy of the bonus row is asserted.  The literal score of the final assembled row is measured directly by the exact native `Y_4` dual in `L-92913`; no declared-score recurrence is load-bearing.

## 5. Exact physical row identity

Demand conservation gives, for every `j>=2`,

\[
\begin{aligned}
\sum_{k\le x}\mu(k)A_{x,j}(k)
&=
\sum_eT_x(e)\rho_{x,j}(e)
-\sum_oT_x(o)\rho_{x,j}(o)\\
&=
\sum_er_x(e)\rho_{x,j}(e)
+\sum_{o,e}t_x(o,e)
   [\rho_{x,j}(e)-\rho_{x,j}(o)].
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_{k\le x}\mu(k)A_{x,j}(k)
=
R_{x,j}+B_{x,j},
\qquad
R_{x,j},B_{x,j}\ge0.
}
\tag{L-92910.15}
\]

This is the concrete row which the reviewed proposals had only named abstractly.

Every ordinary response is applied after the total row in (L-92910.15) is formed.  Hence the ordinary identity is exact.  The radix-four identity is obtained by applying the ordinary identity at `q` and `4q` separately and only then subtracting.  No positivity is asserted for an isolated signed detail functional.

## 6. A concrete positive normalized fibre

The equality density is

\[
L(x)
=
2\sqrt x\sum_{n\le x}\frac{\mu(n)}n
-
\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\tag{L-92910.16}
\]

The directed compact census gives

\[
\frac{159}{500}<L(x)<\frac{183}{100}
\qquad(1\le x<67).
\tag{L-92910.17}
\]

Define the normalized physical fibre

\[
\boxed{
\mathscr H_x(j)
=
\frac{R_{x,j}+B_{x,j}}{L(x)}\ge0.
}
\tag{L-92910.18}
\]

Its residual source part is

\[
\mathscr R_x^{\rm src}
=
\frac1{L(x)}
\sum_e\nu_x(e)\,[x,e,\mathrm{residual}],
\tag{L-92910.19}
\]

while its Hall-edge part has zero source coordinate and the paired provenance of Section 4.  Equation (L-92910.18), together with (L-92910.15), is an explicit positive source/observation fibre, not an existential packet.

On every activation cell the active divisor set is fixed, the deterministic Hall map is a finite composition of addition, subtraction, `min` and division by positive target atoms, and every row profile is algebraic-logarithmic.  Thus `x -> mathscr H_x` is measurable and piecewise Lipschitz.

## 7. Rough ownership and inner colours

Attach the exact first rough owner from `L-91688` to every residual source occurrence in (L-92910.19).  Root Hall uses only divisors of `P_61`, whereas every first rough owner is at least `67`, so these labels are independent and unambiguous.

Apply the exact causal identity of `L-91650` to the residual source part only.  For the ordered rough primes, the nonnegative current and child coefficients satisfy

\[
s_k+\sum_i\lambda_i=1,
\qquad
\alpha_i=r_i\lambda_i,
\qquad
\sum_i\alpha_i<\frac18.
\tag{L-92910.20}
\]

Each residual source occurrence is therefore partitioned among

```text
surviving current;
one causal-difference current colour;
one first-owner inner child colour.
```

The coefficients sum exactly to one in the complete source and row ledger.  The Hall-edge bonuses remain current-only and are never copied to a child.

A complete label is

\[
(\text{outer cell},x,k,\text{Hall role},o,e,
 \text{first rough owner},\text{causal colour},\text{generation}).
\tag{L-92910.21}
\]

For fixed `x`, these labels are pairwise disjoint and exhaust the compact fibre.

## 8. Boundary

```text
finite P_61 source occurrence                     explicit
deterministic Hall residual                       explicit positive source
Hall row bonus                                    explicit positive physical row
bonus source type                                 zero source / paired provenance
target identity                                   exact
declared score                                    superordinate
component-row identity                            exact
ordinary response identity                        exact after total-row sum
radix-four identity                               q and 4q first, then subtract
rough first owner                                 exact
inner causal colours                              exact / coefficient mass <1/8
continuum integration and quantization            next lemma
Riemann Hypothesis                                unproved
```
