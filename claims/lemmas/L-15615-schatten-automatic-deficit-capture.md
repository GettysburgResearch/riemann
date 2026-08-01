# L-15615 — Schatten automatic deficit capture

Claim ID: `L-15615`  
Title: Low compression automatically captures every Schatten moment of a positive deficit operator  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-15612`; scalar Jensen inequality; trace cyclicity; Kato–Seiler–Simon inequality  
Scope: a dimension-aware replacement for the coarse `r=1` weighted-trace condition  
Related counterexample candidates: none

## Motivation

`L-15612` uses the ordinary trace of a positive deficit operator.  That scalar
charges every shallow deficit eigenvalue, even when each is far below the
amount `G-Gamma` that could create a low mode.  The newest plunge estimates are
naturally Schatten estimates, so the correct automatic-capture statement should
retain higher positive moments.

## Abstract theorem

Let `A` be lower-bounded self-adjoint on a Hilbert space. Let `D` be positive
and belong to the Schatten class `S_r` for some real

\[
 r\ge1.
 \tag{L-15615.1}
\]

Suppose

\[
 \boxed{A\succeq GI-D.}
 \tag{L-15615.2}
\]

Let `L` be a `d`-dimensional subspace with orthogonal projection `P`, and assume

\[
 \boxed{A|_L\preceq\alpha I_L,}
 \qquad
 \alpha<G.
 \tag{L-15615.3}
\]

Put

\[
 \kappa=G-\alpha>0,
 \qquad
 Q=I-P.
 \tag{L-15615.4}
\]

Then

\[
 \boxed{PDP|_L\succeq\kappa I_L,}
 \tag{L-15615.5}
\]

and

\[
 \boxed{
 \|QDQ\|^r
 \le
 \operatorname{Tr}(QD^rQ)
 \le
 \operatorname{Tr}D^r-d\kappa^r.}
 \tag{L-15615.6}
\]

Consequently,

\[
 \boxed{
 A|_{L^\perp}
 \succeq
 \left[
 G-\left(\operatorname{Tr}D^r-d(G-\alpha)^r\right)_+^{1/r}
 \right]I.}
 \tag{L-15615.7}
\]

### Proof

Compressing (L-15615.2) to `L` and using (L-15615.3) gives

\[
 \alpha I_L\succeq A|_L\succeq GI_L-PDP|_L,
\]

which proves (L-15615.5).

Let `e_1,...,e_d` be an orthonormal basis of `L`.  For the spectral probability
measure of `D` associated to `e_j`, scalar Jensen gives

\[
 \langle D^re_j,e_j\rangle
 \ge\langle De_j,e_j\rangle^r
 \ge\kappa^r.
 \tag{L-15615.8}
\]

Therefore

\[
\begin{aligned}
 \operatorname{Tr}(QD^rQ)
 &=\operatorname{Tr}D^r
   -\sum_{j=1}^d\langle D^re_j,e_j\rangle\\
 &\le\operatorname{Tr}D^r-d\kappa^r.
\end{aligned}
 \tag{L-15615.9}
\]

For every unit vector `w in L^perp`, scalar Jensen again gives

\[
 \langle Dw,w\rangle^r\le\langle D^rw,w\rangle.
\]

Taking the supremum and then bounding a positive operator norm by its trace
proves

\[
 \|QDQ\|^r
 \le\|QD^rQ\|
 \le\operatorname{Tr}(QD^rQ).
\]

Finally, on `L^perp`, (L-15615.2) gives

\[
 A\succeq GI-QDQ,
\]

and (L-15615.7) follows. QED.

## Scalar saturation criterion

For real numbers

\[
 t<\Gamma<G,
\]

if

\[
 A|_L\prec tI
 \tag{L-15615.10}
\]

and

\[
 \boxed{
 \operatorname{Tr}D^r-d(G-\alpha)^r
 \le(G-\Gamma)^r,}
 \tag{L-15615.11}
\]

then

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I}
 \tag{L-15615.12}
\]

and hence

\[
 \boxed{N_A(t)=N_A(\Gamma)=d.}
 \tag{L-15615.13}
\]

No principal angle between `L` and any eigenspace of `D` is required.

For `r=1`, (L-15615.11) is exactly the trace condition of `L-15612`:

\[
 \operatorname{Tr}D-d(G-\alpha)\le G-\Gamma.
\]

For `r>1`, shallow deficit modes are suppressed by their `r`-th powers.

## Exact packet-moment refinement

The lower term `d(G-alpha)^r` uses only the scalar compression endpoint.  If a
proof packet directly certifies a stronger finite lower bound

\[
 \operatorname{Tr}(PD^rP)\ge\mathcal C_r,
 \tag{L-15615.14}
\]

then one may replace `d(G-alpha)^r` throughout by `mathcal C_r`.  The exact
uncaptured moment is

\[
 \operatorname{Tr}(QD^rQ)
 =\operatorname{Tr}D^r-\operatorname{Tr}(PD^rP).
 \tag{L-15615.15}
\]

This permits a finite packet to capture deep deficit directions by more than
the minimum amount forced by low compression.

## Symbol/Schatten corollary

Let `I` be a bounded interval and

\[
 D=P_I\mathcal F^{-1}w\mathcal FP_I,
 \qquad
 w(\xi)\ge0.
 \tag{L-15615.16}
\]

Put

\[
 K=M_{\sqrt w}\mathcal FP_I.
\]

Then `D=K^*K`.  The one-dimensional Kato–Seiler–Simon inequality gives, for
`r>=1`,

\[
 \|K\|_{S_{2r}}^{2r}
 \le\frac{|I|}{2\pi}\int_{\mathbb R}w(\xi)^r\,d\xi.
\]

Since

\[
 \operatorname{Tr}D^r=\|K\|_{S_{2r}}^{2r},
\]

we obtain

\[
 \boxed{
 \operatorname{Tr}D^r
 \le\frac{|I|}{2\pi}
 \int_{\mathbb R}w(\xi)^r\,d\xi.}
 \tag{L-15615.17}
\]

For the scaled Suzuki interval `I=[-1,1]` and

\[
 w_{a,G}(\xi)=(G-s_a(\xi))_+,
\]

a sufficient scalar complement certificate is therefore

\[
 \boxed{
 \frac1\pi\int_{\mathbb R}(G-s_a(\xi))_+^r\,d\xi
 -d(G-\alpha)^r
 \le(G-\Gamma)^r.}
 \tag{L-15615.18}
\]

Every symbol lower-bound and assembly radius must be inserted before taking the
positive part.

## Why this is better matched to plunge estimates

The ordinary trace can be dominated by a very large number of eigenvalues far
below `G-Gamma`.  Such modes cannot individually violate the desired
complement floor.  Equation (L-15615.11) permits any Schatten exponent
`r>1`, and the limit `r->infinity` approaches operator-norm/threshold-index
control.

The recent one-dimensional localization results estimate singular values and
Schatten quasi-norms of off-diagonal localization operators.  Those estimates
can be combined with layer-cake majorants of the exact arithmetic deficit to
bound (L-15615.17).  This is a closer analytic match than forcing every result
through the `r=1` trace.

## Strict separation from a dimension-only argument

The theorem still requires the low-compression inequality for the **same**
operator `A`.  An unrelated `d`-dimensional source packet does not supply
(L-15615.5), and the counterexample in `R-15601` remains valid.

Conversely, once low compression is certified, deficit capture is automatic at
every Schatten order.  Relative packet rotation is irrelevant.

## Cofinal criterion

At level `j`, choose an exponent `r_j>=1`.  If

\[
 \operatorname{Tr}D_j^{r_j}
 -d_j(G_j-\alpha_j)^{r_j}
 \le(G_j-\Gamma_j)^{r_j}
 \tag{L-15615.19}
\]

and the near-radical compression/residual rates of `T-15602` hold, then exact
low-index saturation follows.  The lower floors of `T-15602` tend to zero and
RH follows.

The exponents may be fixed or may increase with support, provided every
Schatten estimate and root operation is directed and uniform.

## Proof boundary

- The abstract theorem and Kato–Seiler–Simon reduction are exact.
- A proof-grade zeta application still requires an asymptotic bound for the
  complete arithmetic `L^r` deficit and a uniformly normalized repaired source
  packet.
- A numerical singular-value decay curve is not a Schatten certificate.
- The `r=1` trace condition may be much too coarse even when an `r>1` or exact
  leverage certificate passes.
- No cofinal Suzuki-symbol moment bound is proved here, and no proof of RH is
  claimed.
