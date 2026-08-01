# L-16229 — Explicit compact radial envelope and interval-ODE production adapter

Claim ID: `L-16229`  
Status: **PROVED A-POSTERIORI ERROR THEOREM; PRODUCTION PRIMITIVE NOT YET EMITTED**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: Dunster equations (2.5)--(2.11); `L-16217`, `L-16221`, `L-16228`

## 1. Purpose

Dunster's published summary writes the radial error as
\(O(\gamma^{-1})\operatorname{env}J_0\). The paper points to Olver's explicit
theory, but does not print one numerical coefficient in the summary formula.

For the CCM proof, no hidden big-O coefficient is necessary. On the complete
stationary/Airy radial window, Dunster's exact Liouville equation gives a
Volterra estimate with the outward constant \(360\). On the pole and infinite
tail pieces, a finite interval-ODE certificate supplies the same information
without trusting a hidden asymptotic constant.

## 2. Exact Liouville equation

For order \(m=0\), Dunster's transformation gives

\[
 \frac{d^2W}{d\xi^2}
 =
 \{-\gamma^2+\psi_s(\xi)\}W,                      \tag{L-16229.1}
\]

where, with \(y=z^2\) and \(s=\sigma^2\),

\[
 \psi_s
 =
 -\frac1{(y-1)(y-s)}
 +
 \frac{
 (1-s)\{6y^2-(3+s)y-2s\}
 }{
 4(y-1)(y-s)^3
 }.                                                \tag{L-16229.2}
\]

The Liouville differential is

\[
 d\xi
 =
 \sqrt{\frac{z^2-s}{z^2-1}}\,dz.                  \tag{L-16229.3}
\]

## 3. One explicit envelope constant

On the radial rectangle used by the phase partition,

\[
 \frac54\leq y\leq4,
 \qquad
 0\leq s\leq\frac18,                              \tag{L-16229.4}
\]

the two terms in (L-16229.2) satisfy

\[
 \frac1{(y-1)(y-s)}
 \leq\frac{32}{9},                                 \tag{L-16229.5}
\]

and

\[
 \left|
 \frac{
 (1-s)\{6y^2-(3+s)y-2s\}
 }{
 4(y-1)(y-s)^3
 }\right|
 \leq
 \frac{55680}{729}.                                \tag{L-16229.6}
\]

Therefore

\[
 \boxed{|\psi_s|\leq80.}                           \tag{L-16229.7}
\]

Moreover,

\[
 \frac{d\xi}{dz}
 \leq\sqrt5<\frac94,
\]

and the radial interval has length below \(1\). Thus

\[
 \boxed{\int|\psi_s(\xi)|\,d\xi<180.}              \tag{L-16229.8}
\]

Every constant is rational and outward.

## 4. Volterra replay

Fix the left endpoint \(\xi_a\) of one compact phase piece and define the exact
free solution with matching Cauchy data,

\[
 W_0(\xi)
 =
 W(\xi_a)\cos\gamma(\xi-\xi_a)
 +
 \frac{W'(\xi_a)}{\gamma}
 \sin\gamma(\xi-\xi_a).                            \tag{L-16229.9}
\]

Variation of constants gives

\[
 W(\xi)
 =
 W_0(\xi)
 +
 \frac1\gamma
 \int_{\xi_a}^{\xi}
 \sin\gamma(\xi-u)\,
 \psi_s(u)W(u)\,du.                                \tag{L-16229.10}
\]

Put

\[
 M_a=|W(\xi_a)|+\frac{|W'(\xi_a)|}{\gamma},
 \qquad
 V=\frac1\gamma\int|\psi_s|.                       \tag{L-16229.11}
\]

Gronwall gives

\[
 |W|\leq M_ae^V,
 \qquad
 |W-W_0|\leq M_a(e^V-1).                           \tag{L-16229.12}
\]

For \(\gamma\geq360\), \(V\leq1/2\), and

\[
 e^V-1\leq2V.
\]

Consequently,

\[
 \boxed{
 |W-W_0|
 \leq
 \frac{360}{\gamma}M_a.}                           \tag{L-16229.13}
\]

Differentiating (L-16229.10) introduces no endpoint term, since the sine kernel
vanishes on the diagonal. The same calculation gives

\[
 \boxed{
 \frac{|W'-W_0'|}{\gamma}
 \leq
 \frac{360}{\gamma}M_a.}                           \tag{L-16229.14}
\]

Thus \(360/\gamma\) is a fully explicit relative envelope for both the
transformed radial function and its phase derivative on every compact piece
used in `L-16228`.

The algebraic prefactor

\[
 \{(z^2-1)(z^2-s)\}^{-1/4}
\]

and its derivatives are bounded by direct rational interval arithmetic on the
same boxes.

## 5. Pole-to-tail interval adapter

The remaining regions are handled without a hidden constant.

### A. Near the simple pole

Use Dunster's variable \(\eta=\xi^2\). The transformed equation is

\[
 \widehat W''
 =
 \left[
 -\frac{\gamma^2}{4\eta}
 -\frac1{4\eta^2}
 +\frac{\widehat\psi_s(\eta)}{\eta}
 \right]\widehat W.                                     \tag{L-16229.15}
\]

The unperturbed regular and singular solutions are

\[
 u(\eta)=\sqrt\eta J_0(\gamma\sqrt\eta),
 \qquad
 v(\eta)=\sqrt\eta Y_0(\gamma\sqrt\eta),
\]

with exact Wronskian

\[
 \boxed{\mathcal W_\eta(u,v)=\frac1\pi.}                 \tag{L-16229.16}
\]

A Frobenius interval expansion at a positive dyadic \(\eta_0\) supplies the
regular Cauchy data and a geometric tail.

### B. Finite interval

Write the exact equation as a first-order system

\[
 Y'=A(\eta)Y.
\]

For an interval approximation \(\widetilde Y\), residual

\[
 r=\widetilde Y'-A\widetilde Y,
\]

and a directed transition bound

\[
 \|\Phi(\eta,t)\|\leq K,
\]

the exact a-posteriori inequality is

\[
 \boxed{
 \|Y-\widetilde Y\|_\infty
 \leq
 K\{e_0+\ell\|r\|_\infty\}.}                            \tag{L-16229.17}
\]

The derivative companion is identical after augmenting the first-order state.

### C. Infinite tail

Choose a rational \(Z>1\). Beyond \(Z\), use the exact integration-by-parts
endpoint ledger `L-16221`, retaining all channels through \(p=4\) and charging

\[
 \zeta(4)-1
 <
 \boxed{\frac{9083}{108045}},                            \tag{L-16229.18}
\]

which follows from \(\pi<22/7\). After alias cutoff \(K\),

\[
 \boxed{
 \sum_{k>K}k^{-4}
 \leq\frac1{3K^3}.}                                     \tag{L-16229.19}
\]

## 6. Squared directed output

If a finite interval has length \(\ell\), transition bound \(K\), initial
radius \(e_0\), residual radius \(r_0\), and an independently bounded tail
energy \(t_2\), then the producer emits

\[
 \boxed{
 \varepsilon_{\rm rad}^2
 \leq
 \ell K^2(e_0+\ell r_0)^2+t_2.}                         \tag{L-16229.20}
\]

It emits the analogous quantity
\(\varepsilon_{\rm rad,1}^2\) for the frequency derivative and horizontal
strip.

These are the primitive fields checked by `X-16204`.

## 7. What has and has not been extracted

The following constants are now explicit:

```text
compact Liouville potential      80
compact variation integral      180
relative radial envelope         360/gamma
relative derivative envelope     360/gamma
stationary second-derivative     11/12
higher-alias derivative gap      1/50
fold cubic interval              [8,60/7]
Poisson p=4 zeta charge          9083/108045
post-cutoff alias tail           1/(3 K^3)
```

The source paper's unprinted big-O coefficient is no longer a logical
dependency.

## 8. Smallest production blocker

The exact remaining implementation primitive is one outward-rounded
interval-ODE artifact containing:

```text
a separation-parameter interval sigma^2;
regular Cauchy data at eta_0;
transition-matrix bounds on the finite partition;
ODE residual bounds for the normalized radial template;
frequency-derivative residual bounds;
the p=4 endpoint/tail ledger;
SHA-256 bindings to the CCM mode, support, and normalization.
```

No such production artifact has yet been emitted for a real cofinal CCM block.
Once it exists, every later wrapper inequality is rational and exact.

## 9. Proof boundary

The Volterra and a-posteriori inequalities are exact. The compact constant
\(360\) is proved above. `X-16204` currently contains a synthetic interval-ODE
primitive only; it does not constitute a production PSWF replay.
