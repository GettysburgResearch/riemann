# L-91441 — Score-normalized branching preserves both the score budget and one-use target capacity

Claim ID: `L-91441`  
Status: **EXACT TWO-LEDGER REPAIR; SHAPE-UNIFORM PACKING BOUND OPEN**  
Created: 2026-08-12  
Depends on: `L-91329`, `L-91339`, `L-91340`, `R-91440`  
RH status: **unproved**

## 1. Positive coefficient measures

For a positive finite coefficient measure `nu` at endpoint `x`, define

\[
 \mathfrak T_x(\nu)
 =\int W_\Psi(x,n)d\nu(n),
 \qquad
 \mathfrak S_x(\nu)
 =\int W_S(x,n)d\nu(n),
\tag{L-91441.1}
\]

where

\[
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
\tag{L-91441.2}
\]

Both are positive and

\[
 0<q_x(n):=\frac{W_\Psi(x,n)}{W_S(x,n)}<1.
\tag{L-91441.3}
\]

The score measure and target measure attached to `nu` are therefore

\[
 d\sigma_x=W_S(x,n)d\nu(n),
 \qquad
 d\tau_x=q_x(n)d\sigma_x.
\tag{L-91441.4}
\]

The target is a positive submeasure of the score measure, but the two measures are not proportional.

## 2. Exact one-prime split in both ledgers

Fix a rough prime `p`, put `B_p=1-p^{-1/2}`, and split `nu` into

\[
 \nu^{\rm in}=\nu|_{n\le x/p},
 \qquad
 \nu^{\rm fr}=\nu|_{x/p<n\le x}.
\]

The identities of `L-91339` give

\[
\boxed{
\begin{aligned}
 \mathfrak T_x(\nu)
 ={}&\mathfrak T_{x/p}(\nu^{\rm in})
 +4B_p\sqrt x\int_{n\le x/p}\frac{d\nu(n)}n
 +\mathfrak T_x(\nu^{\rm fr}),\\
 \mathfrak S_x(\nu)
 ={}&\mathfrak S_{x/p}(\nu^{\rm in})
 +5B_p\sqrt x\int_{n\le x/p}\frac{d\nu(n)}n
 +\mathfrak S_x(\nu^{\rm fr}).
\end{aligned}}
\tag{L-91441.5}
\]

Every term on the right is positive. Moreover the paid score exceeds the paid target by

\[
 B_p\sqrt x\int_{n\le x/p}\frac{d\nu(n)}n
 +\left[\mathfrak S_x-\mathfrak T_x\right](\nu^{\rm fr})
 \ge0.
\tag{L-91441.6}
\]

Thus the child coefficient is exactly one in both ledgers, and every current-generation term has favorable score orientation.

## 3. Parallel least-prime colors

Let

\[
 \nu=\nu_0+\sum_b\nu_b
\tag{L-91441.7}
\]

be any positive disjoint color partition, with color `b` carrying prime `p_b`. Apply (L-91441.5) to every color. Put

\[
 s_b=\mathfrak S_{x/p_b}(\nu_b^{\rm in}),
 \qquad
 t_b=\mathfrak T_{x/p_b}(\nu_b^{\rm in}),
 \qquad
 S=\mathfrak S_x(\nu).
\tag{L-91441.8}
\]

Then

\[
\boxed{
 \sum_b s_b\le S,
 \qquad
 \sum_b t_b\le\mathfrak T_x(\nu).
}
\tag{L-91441.9}
\]

If `S>0`, the correct branching weights are

\[
\boxed{
 \theta_b^{S}=\frac{s_b}{S},
 \qquad
 \sum_b\theta_b^{S}\le1.
}
\tag{L-91441.10}
\]

These are score-mass fractions. The target is not replaced by these scalar weights: the exact child target measures themselves form a positive subpartition of the parent target.

## 4. Compatibility with the finite Hall projection

`L-91340` performs the parity Hall transport in score-mass units and produces a positive coefficient measure `nu_x` satisfying

\[
 \text{finite forcing score}
 =\mathfrak S_x(\nu_x),
\tag{L-91441.11}
\]

while

\[
 \mathfrak T_x(\nu_x)
 \le \text{available signed target forcing}.
\tag{L-91441.12}
\]

The ratio monotonicity used there is exactly what is needed to keep the target subordinate while score is represented without loss. Hence the score-normalized split above is stable under the finite parity projection.

`L-91329` then transports and quantizes the **sum** of all positive target submeasures once, so the physical target is not duplicated by the score normalization.

## 5. Shape-uniform loss functional

Let `C_x` be the cone of positive kernel measures admitted by the finite source typing. For `nu in C_x`, let `D_x(nu)` be the score loss of one fixed positive, source-linear packing construction. Assume:

1. positive homogeneity:
   \[
   D_x(c\nu)=cD_x(\nu),\qquad c\ge0;
   \tag{L-91441.13}
   \]
2. the local operations in (L-91441.5), Hall transport, sum-before-quantize and finite collars give
   \[
   D_x(\nu)
   \le e(x)\mathfrak S_x(\nu)
      +\sum_bD_{x/p_b}(\nu_b^{\rm in});
   \tag{L-91441.14}
   \]
3. `e(x)\ll(1+\log\log(3x))^A` uniformly on the normalized cone.

Define the worst normalized loss

\[
 \mathcal R(x)
 =\sup_{0\ne\nu\in C_x}
  \frac{D_x(\nu)}{\mathfrak S_x(\nu)}.
\tag{L-91441.15}
\]

Using (L-91441.9),

\[
\boxed{
 \mathcal R(x)
 \le e(x)+
 \sup_{y\le x/67}\mathcal R(y).
}
\tag{L-91441.16}
\]

Indeed each child term is at most `s_b R(x/p_b)`, and `sum s_b<=S`.

Iteration gives

\[
 \mathcal R(x)
 \ll\log x\,(1+\log\log x)^A.
\tag{L-91441.17}
\]

Thus a boundedly normalized root source would have `o(log^2 x)` loss.

## 6. Exact remaining producer theorem

Equations (L-91441.1)--(L-91441.12) repair the two-ledger algebra completely. What is not supplied by a scalar source partition is the uniform hypothesis (L-91441.14): the finite packing map must be defined on the whole positive kernel cone, and its local debt must be bounded per unit **score** mass.

Therefore the corrected factor-54 conclusion-producing theorem is:

> Construct one source-linear positive packing functor on `C_x` satisfying (L-91441.14), with the root source normalization matched exactly to the prime-ramp score.

This is narrower and correctly normalized. It is not equivalent to taking the total mass of the SHARP target measure.

## 7. Boundary

```text
score/target Radon-Nikodym split                 EXACT
one-prime coefficient-one split in both ledgers EXACT
parallel score subprobability                    EXACT
parallel target subpartition                     EXACT
finite Hall source typing                        IMPORTED EXACT
sum-before-quantize one-use target               IMPORTED EXACT
shape-uniform positive packing functor           OPEN
root score normalization                         OPEN AUDIT JOINT
factor-54 RH conclusion                          CONDITIONAL
Riemann Hypothesis                               UNPROVED
```
