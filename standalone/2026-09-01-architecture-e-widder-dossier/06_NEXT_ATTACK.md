# Next attack: close the fixed-centre heat / theta–Darboux gate

Status: **RESEARCH PROGRAMME; THE E–WIDDER SOURCE INEQUALITY IS PROVED THROUGH ORDER `4.71*10^12`; ITS UNBOUNDED-ORDER FORM AND RH REMAIN OPEN.**

The branch no longer needs another order-by-order Widder calculation.  The
latest exact identities reduce the unbounded problem to two source-local gates
that are adjoint views of the same invariant ladder:

1. complete monotonicity of one fixed-centre zero heat trace;
2. nonnegativity of one theta–Darboux exterior integral against a strictly
   totally-positive Pascal/Bessel propagator.

The purpose of this note is to organize the next proof around those gates and
prevent a return to finite-order scanning.

## 1. The fixed-centre heat gate

Let

\[
 K(t)=e^{-t/4}\sum_\rho e^{-t\gamma_\rho^2}
 =2\sum_a e^{-at},
 \qquad a=-\rho(\rho-1).
\]

Then

\[
 q(u)=\int_0^\infty e^{-ut}K(t)\,dt
\]

and

\[
 \mathcal W_k(u)
 =\int_0^\infty
 t^{2k-1}e^{-ut}(-1)^kK^{(k)}(t)\,dt.
\]

Consequently

\[
 \boxed{
 \mathrm{RH}
 \iff K\text{ is completely monotone on }(0,\infty).
 }
 \tag{HCM}
\]

The explicit source is

\[
 \begin{aligned}
 K(t)={}&2\\
 &+\frac{e^{-t/4}}{2\pi}
 \int_{\mathbb R}e^{-t\tau^2}
 \left[
  \Re\psi\left(\frac14+\frac{i\tau}{2}\right)-\log\pi
 \right]d\tau\\
 &-\frac{e^{-t/4}}{\sqrt{\pi t}}
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.
 \end{aligned}
 \tag{1.1}
\]

Every term is absolutely convergent for `t>0`.  The movable cosine phase of
the general First-Hermite formula has disappeared.  The problem is now the
complete-monotonicity sign of one nonoscillatory gamma-plus-prime heat source.

### Heat target `HCM_source`

Prove directly from (1.1) that

\[
 \boxed{
 (-1)^mD_t^mK(t)\ge0
 \qquad(m\ge0,\ t>0).
 }
 \tag{1.2}
\]

A proof immediately gives every E–Widder inequality through the positive
Laplace moment above.

## 2. The theta–Darboux gate

Let

\[
 b_n(\tau)
 =[u^n]\cosh\left(\tau\sqrt{u+\frac14}\right),
 \qquad
 L=D_\tau^2-\frac14.
\]

The actual invariant coefficients satisfy

\[
 c_n=2\int_0^\infty\Phi(\tau)b_n(\tau)d\tau,
 \qquad
 Lb_n=b_{n-1}.
\]

The kernel `(tau,n)->b_n(tau)` is strictly totally positive of infinite
order.  For increasing row and column sets `I=(i_p)`, `J=(j_q)` with
`j_1>=i_r`, put

\[
 h_p=i_p-i_1,
 \qquad
 n_q=j_q-i_1.
\]

The exact Andreief factorization is

\[
 \boxed{
 \begin{aligned}
 \det[c_{j_q-i_p}]
 ={}&2^r\int_{0<\tau_1<\cdots<\tau_r}
 \det[(L^{h_p}\Phi)(\tau_\ell)]_{p,\ell}\\
 &\qquad\qquad\cdot
 \det[b_{n_q}(\tau_\ell)]_{q,\ell}
 \,d\boldsymbol\tau.
 \end{aligned}
 }
 \tag{2.1}
\]

The second determinant is strictly positive.  All arithmetic sign is in one
actual theta–Darboux exterior current.

### Weighted theta–Darboux gate `TDA`

Prove the right side of (2.1) is nonnegative for every admissible index
packet.

This target is deliberately weaker than pointwise positivity of

\[
 \det[(L^{h_p}\Phi)(\tau_\ell)].
\]

No pointwise theorem is assumed.  Strict total positivity of `b_n` permits a
variation-diminishing proof in which the theta determinant changes sign but
its ordered pairing has the required orientation.

## 3. Why the two gates are the same ladder

The coefficient-side identity is obtained by moving powers of

\[
 L=D_\tau^2-\frac14
\]

from `b_n` onto the theta source.  The heat-side identity moves invariant
powers from the Euler-safe logarithmic derivative into heat time.  Both are
adjoint expressions of multiplication by the invariant coordinate

\[
 u=s(s-1).
\]

The desired intertwiner should have the schematic form

\[
 \boxed{
 \text{theta--Darboux exterior current}
 \longrightarrow
 \text{positive combination of }(-1)^mK^{(m)}(t).
 }
 \tag{3.1}
\]

A positive version of (3.1) would settle both `TDA` and `HCM_source`, and
therefore the quasi-free, Toeplitz, Stieltjes and E–Widder formulations at
once.

## 4. First theorem-sized objective: sign variation, not pointwise sign

For consecutive order `r`, define

\[
 \mathcal T_r(\boldsymbol\tau)
 =\det[(L^i\Phi)(\tau_j)]_{i,j=0}^{r-1}
\]

on the ordered chamber

\[
 0<\tau_1<\cdots<\tau_r.
\]

The next theorem should determine the number and orientation of sign chambers
of `mathcal T_r` and prove that the strictly TP kernel

\[
 \det[b_{k+j}(\tau_\ell)]
\]

integrates them with nonnegative total mass.

A useful sufficient theorem would be:

> **Ordered variation theorem `OVT(r)`.**  The cumulative integral of
> `mathcal T_r` over every lower ideal of the ordered chamber has the
> orientation required by all increasing Pascal/Bessel test determinants.

This is a multidimensional analogue of a signed measure having nonnegative
moments against a Chebyshev system.  It is weaker than pointwise positivity
and exactly matched to (2.1).

## 5. Darboux factorization lane

The source atom

\[
 e^{\tau/2-\pi m^2e^{2\tau}}
\]

is acted on by

\[
 L=(D_\tau-1/2)(D_\tau+1/2).
\]

Writing `y=pi m^2e^(2 tau)`, the iterates have the form

\[
 L^h\left(e^{\tau/2-y}\right)
 =e^{\tau/2-y}P_h(y),
\]

where

\[
 P_{h+1}=B(B+1)P_h,
 \qquad
 B=2y(D_y-1),
 \qquad
 P_0=1.
\]

The observed first polynomials have simple positive interlacing zeros.  The
proof task is to derive a Rodrigues/Darboux theorem for the entire sequence
and use it before summing the theta atoms.  A valid theorem must keep the
common lattice label and ordered source packet; termwise positivity followed
by an arbitrary positive sum is not enough.

The immediate analytic subtargets are:

1. prove real-rootedness and strict interlacing of every `P_h`;
2. identify the sign-regular kernel `(h,y)->P_h(y)e^(-y)`;
3. combine it with total positivity of the Laplace kernel
   `exp(-pi m^2 exp(2 tau))` through a discrete/continuous Cauchy–Binet
   formula;
4. derive the chamber orientation needed by `OVT(r)`.

## 6. Heat-source square-completion lane

Differentiate the nonoscillatory prime term in (1.1) only after the entire
source is assembled.  In the natural variable

\[
 y=\frac{(\log n)^2}{4t},
\]

each heat derivative is a Gaussian times a generalized Laguerre/Hermite
polynomial.  The gamma integral has the same heat scale.

The target is a source identity of the form

\[
 (-1)^mK^{(m)}(t)
 =\int_\Omega |V_{m,t}(\omega)|^2d\nu(\omega)
\]

or a conservative two-channel difference in which the entire gamma reserve
and prime sum are completed before squaring.  An absolute envelope for the
prime polynomial is forbidden: it destroys the cancellation at the
constant-four/terminal scale.

## 7. Quasi-free projective lane

The one-scale count law is an explicit positive mixture of quasi-free
Bernoulli fibres.  A finite exterior closure at degree `N` is equivalent to
matching every Toeplitz/Schur coefficient through that degree.

The useful finite theorem is therefore not merely real-rootedness of one
truncation.  It is:

> construct positive contractions `K_v^(N)` whose exterior traces match all
> theta-source minors through rank `N`, with a trace-norm bound independent of
> `N`, and prove projective consistency.

A compactness limit would then supply the single contraction required by the
quasi-free gate.

The theta–Darboux formula (2.1) provides the exact exterior data that these
finite contractions must realize.

## 8. Boundary and reciprocal completion

Formula (2.1) covers minors whose coefficient indices are all nonnegative.
Minors crossing the one-sided boundary must be handled with the exact
reciprocal rectangle identity

\[
 D^A_{r,k}=D^{1/A(-z)}_{k,r}.
\]

The intended composition is:

```text
positive-index chamber -> theta--Darboux/Andreief;
boundary-crossing chamber -> reciprocal bosonic coordinate;
large shift -> imported cubic wedge;
low order -> verified-height sector;
broad central cone -> OVT/TDA.
```

No region may be promoted by overlap unless the exact index conventions are
checked.

## 9. Large unconditional regions already available

The branch retains:

- strict E–Widder/source inequalities for every `u>0` through order
  `4.71*10^12`;
- the full two-parameter Widder cone through the matching rectangle;
- all Toeplitz orders through `9.42*10^12` at every shift from the verified
  zero-sector theorem;
- the imported centred cubic wedge at `k>=10^18r^3`;
- resummed radial positivity up to a terminal annulus of width below
  `2.78e-26`.

These are base regions and consistency checks.  They do not replace the
height-free source mechanism.

## 10. Computation worth doing

Useful work:

- exact symbolic generation and factorization of the Darboux polynomials
  `P_h`;
- rigorous sign-chamber enclosures for low exterior ranks, used to conjecture
  `OVT(r)`;
- exact Cauchy–Binet decompositions over lattice labels and polynomial degree;
- search for a positive heat/theta intertwiner;
- directed checks of a proposed uniform identity, not broad minor scans;
- construction of finite projectively consistent contractions.

Work to avoid:

- the literal next Widder derivative;
- a larger unstructured zero scan;
- pointwise positivity assumed from positive source;
- replacing a mixture of determinants by a determinant of an average;
- modewise `PF_infinity` followed by positive summation;
- absolute prime envelopes;
- extrapolating any finite cone to all order.

## 11. End-to-end completion protocol

A successful continuation should deliver one chain:

```text
actual theta source Phi
-> theta--Darboux exterior current
-> variation-diminishing Andreief sign / fixed-centre heat square
-> all coefficient and Widder signs
-> one positive trace-class contraction
-> q is Stieltjes
-> invariant zeros are negative real
-> RH.
```

The first load-bearing theorem is now `OVT/TDA` or its positive heat
intertwiner.  That is where the new formulation offers genuine leverage over
the original RH-equivalent inequality.
