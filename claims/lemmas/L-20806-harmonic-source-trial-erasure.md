# L-20806 — Harmonic shorting erases the chosen source trial

Claim ID: `L-20806`  
Title: The line-centered harmonic source graph and its joint perturbation residual are independent of the affine trial vector  
Status: `PROVED FINITE BLOCK THEOREM; CANONICAL GRAPH ARITHMETIC BOUND OPEN`  
Authoring agent: `gpt56-03-t`  
Created: 2026-08-01  
Dependencies: `L-18512`, `L-15633`, `L-20801`; elementary Schur complementation  
Scope: the factorially flat source packet and every other source-normalized trial  
Related counterexample candidates: none

## 1. Setup

Let a finite source space split as

\[
 \mathcal U=\mathbb C e\oplus W,
 \qquad
 \ell(e)=1,
 \qquad
 W=\ker\ell.
 \tag{L-20806.1}
\]

Let the positive line-centered comparator be

\[
 H^0=
 \begin{pmatrix}
  a&r^*\\
  r&C_0
 \end{pmatrix},
 \qquad
 C_0\succ0,
 \qquad
 H^0\succeq0.
 \tag{L-20806.2}
\]

Its source Schur value is

\[
 s_0=a-r^*C_0^{-1}r\ge0.
 \tag{L-20806.3}
\]

Every source-normalized trial is uniquely

\[
 x_w=e+w,
 \qquad w\in W.
 \tag{L-20806.4}
\]

The comparator residual of this trial is

\[
 \rho_w=P_WH^0x_w=r+C_0w.
 \tag{L-20806.5}
\]

## 2. Exact trial erasure

Short the trial by its comparator residual:

\[
 y_w=x_w-C_0^{-1}\rho_w.
 \tag{L-20806.6}
\]

Then

\[
 \boxed{
 y_w=e-C_0^{-1}r=:y_0
 }
 \tag{L-20806.7}
\]

for every `w`. In particular, the line-centered harmonic source graph is
**independent of the chosen trial vector**.

### Proof

Substitute (L-20806.5):

\[
 x_w-C_0^{-1}\rho_w
 =e+w-C_0^{-1}(r+C_0w)
 =e-C_0^{-1}r.
\]

QED.

Equivalently, if two source-normalized trials differ by `u in W`, their
comparator residuals differ by `C_0u`; exact shorting removes that difference.

The comparator identities are

\[
 P_WH^0y_0=0,
 \tag{L-20806.8}
\]

and

\[
 \langle H^0y_0,y_0\rangle=s_0.
 \tag{L-20806.9}
\]

The trial's excess comparator energy is exactly

\[
 \boxed{
 \langle H^0x_w,x_w\rangle-s_0
 =\rho_w^*C_0^{-1}\rho_w.
 }
 \tag{L-20806.10}
\]

Thus a trial may have spectacularly small values under selected response
functionals while being very far from the canonical harmonic graph in the only
metric relevant to the source Schur complement.

## 3. Exact joint perturbation identity

Let the actual block be

\[
 H=H^0+E
 =\begin{pmatrix}b&z^*\\z&C\end{pmatrix},
 \qquad C\succ0.
 \tag{L-20806.11}
\]

Since the comparator residual of `y_0` vanishes, its actual residual is exactly

\[
 \boxed{
 \rho_E=P_WHy_0=P_WEy_0.
 }
 \tag{L-20806.12}
\]

The actual source Schur value satisfies the exact identity

\[
 \boxed{
 s(H)
 =s_0+\langle Ey_0,y_0\rangle
 -\rho_E^*C^{-1}\rho_E.
 }
 \tag{L-20806.13}
\]

### Proof

The vector `y_0` is source-normalized. Every other source-normalized vector is
`y_0+u`, `u in W`. Therefore

\[
\begin{aligned}
 \langle H(y_0+u),y_0+u\rangle
 ={}&\langle Hy_0,y_0\rangle
 +2\operatorname{Re}\langle \rho_E,u\rangle
 +\langle Cu,u\rangle.
\end{aligned}
\]

The minimum occurs at `u=-C^{-1}rho_E` and equals

\[
 \langle Hy_0,y_0\rangle-\rho_E^*C^{-1}\rho_E.
\]

Now use (L-20806.9) and `H=H^0+E`. QED.

Equation (L-20806.13) is the requested one-contraction form: the perturbation
energy and inverse-metric residual must be evaluated on the same canonical
line-centered graph before either is widened.

## 4. Metric source normalization

Let `G>0`, put

\[
 q=G^{-1}\ell^*,
 \qquad
 g=\ell q,
 \qquad
 W=q^{\perp_G},
 \tag{L-20806.14}
\]

and use source coordinate `e=q/g`. Multiplying (L-20806.13) by `g` gives the
normalization used in `L-20801` and `X-18506`:

\[
 \boxed{
 {g\over\ell H^{-1}\ell^*}
 ={1\over g}
 \left[
  g^2s_0
  +\langle E\widetilde y_0,\widetilde y_0\rangle
  -\widetilde\rho_E^*C^{-1}\widetilde\rho_E
 \right],
 }
 \tag{L-20806.15}
\]

where `widetilde y_0=gy_0` and
`widetilde rho_E=g rho_E`.

Hence the factorial packet can enter the final scalar only if it supplies
information about the canonical `y_0`, or if it proves that its comparator
harmonic defect (L-20806.10) is negligible. Its raw response is not itself a
lower certificate.

## 5. Main-density erasure model

The erasure is especially transparent for the dominant metric comparator.
Assume

\[
 H^0=\alpha G,
 \qquad \alpha>0,
 \tag{L-20806.16}
\]

and take the affine normalization `ell x=g`. The source Riesz vector `q` is the
unique harmonic representative. For every `x=q+w`, `w in W`,

\[
 \boxed{
 y_0=q,
 \qquad
 \langle H^0x,x\rangle-\alpha g
 =\alpha\|w\|_G^2.
 }
 \tag{L-20806.17}
\]

Thus a high-order notch placed in an arbitrary affine trial is projected back
to the ordinary source Riesz vector under the main-density shorting.

The conclusion is stable. Suppose

\[
 H^0=\alpha G+E_0,
 \qquad
 \|G^{-1/2}E_0G^{-1/2}\|\le\eta\alpha,
 \qquad 0\le\eta<1.
 \tag{L-20806.18}
\]

Write the harmonic representative as `y_0=q+w_0`, `w_0 in W`. Stationarity on
`W` gives

\[
 \alpha Gw_0+P_WE_0(q+w_0)=0.
\]

Therefore

\[
 \boxed{
 \|w_0\|_G
 \le{\eta\over1-\eta}\sqrt g.
 }
 \tag{L-20806.19}
\]

So whenever the line-centered block is a small relative perturbation of its
main-density metric, its canonical source graph remains close to `q`, not to an
arbitrarily chosen factorial trial.

## 6. Consequence for the factorially flat packet

Let `x_M=g_Mv_{r_M}` be the packet of `L-20804`. Its exact source value,
coefficient metric, factorial response, and fixed-mode suppression remain valid.
However, in any line-centered comparison the vector entering the exact joint
Schur identity is

\[
 y_{0,M}=x_M-C_{0,M}^{-1}P_WH_M^0x_M,
 \tag{L-20806.20}
\]

and this vector is the same one obtained from every other source-normalized
trial.

Accordingly, a valid continuation must prove at least one of:

1. the canonical graph `y_(0,M)` itself inherits the factorial response bound;
2. the harmonic defect
   \[
   (P_WH_M^0x_M)^*C_{0,M}^{-1}(P_WH_M^0x_M)
   \]
   is negligible in the final source metric;
3. the complete joint quantity in (L-20806.13) is bounded directly, without
   assigning the flat packet's raw notch to `y_(0,M)`.

The first two statements are new arithmetic assertions. Neither follows from
`L-20804/L-20805`.

## 7. Production object

A proof-facing source packet should now emit, in one declared metric,

```text
H0, C0, comparator source residual,
canonical harmonic source vector y0,
actual-horizontal graph energy <E y0,y0>,
actual residual P_W E y0,
actual constrained block C,
final exact joint Schur value.
```

The trial vector may still be retained as an independent producer, but the
consumer must recompute `y0` and verify trial erasure before accepting any notch
bound.

## 8. Proof boundary

- Trial erasure and the joint perturbation identity are exact.
- The theorem does not refute the factorial packet's finite response formulas.
- It refutes only the unstated transfer from those formulas to the canonical
  line-centered graph.
- No bound for the canonical graph response or for (L-20806.13) is proved here;
  the source Weyl-function sign remains open.
