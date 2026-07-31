# R-15603 — The zero-slack Berezin symbol-capacity inequality is impossible

Claim ID: `R-15603`  
Title: A nonzero time-frequency deficit has strictly positive mass outside every finite low packet  
Status: `PROVED REFUTATION / SCOPE CORRECTION`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: Plancherel; Paley–Wiener analyticity; trace cyclicity  
Scope: the proposed final scalar inequality in `L-15620` and Issue #156  
Related counterexample candidates: none

## 1. Statement

Let `I` be a bounded interval of positive length and let

\[
 \mathcal H=L^2(I).
\]

Extend vectors by zero and use

\[
 \|f\|_2^2={1\over2\pi}\int_{\mathbb R}|\widehat f(\xi)|^2d\xi.
 \tag{R-15603.1}
\]

Let `s` be a real measurable lower symbol, let `Gamma` be real, and put

\[
 w(\xi)=(\Gamma-s(\xi))_+,
 \qquad
 D_\Gamma=P_I\mathcal F^{-1}M_w\mathcal FP_I.
 \tag{R-15603.2}
\]

Assume `w in L1(R)`. Let `A` be a lower-bounded self-adjoint operator, or a
closed lower-bounded form, satisfying

\[
 \boxed{A\succeq\Gamma I-D_\Gamma.}
 \tag{R-15603.3}
\]

Let `L subset H` be a nonzero finite-dimensional subspace, with

\[
 d=\dim L<\infty,
 \qquad
 A|_L\preceq\alpha I_L,
 \qquad
 \alpha<\Gamma.
 \tag{R-15603.4}
\]

Then the proposed capacity inequality has the **strict reverse direction**:

\[
 \boxed{
 { |I|\over2\pi}
 \int_{\mathbb R}(\Gamma-s(\xi))_+d\xi
 >d(\Gamma-\alpha).}
 \tag{R-15603.5}
\]

In particular, on the scaled Suzuki interval `I=[-1,1]`,

\[
 \boxed{
 {1\over\pi}
 \int_{\mathbb R}(\Gamma-s(\xi))_+d\xi
 >d(\Gamma-\alpha).}
 \tag{R-15603.6}
\]

Therefore the requested inequality with `<=` cannot hold at any nontrivial
finite level under the same lower-symbol and low-packet hypotheses.

## 2. Low compression forces the reverse non-strict bound

Let `P` be the orthogonal projection onto `L` and put `Q=I-P`. Compressing
(R-15603.3) to `L` and using (R-15603.4) gives

\[
 \alpha P\succeq PAP
 \succeq\Gamma P-PD_\Gamma P.
\]

Hence

\[
 \boxed{
 PD_\Gamma P\succeq(\Gamma-\alpha)P.}
 \tag{R-15603.7}
\]

Taking the finite-dimensional trace yields

\[
 \boxed{
 \operatorname{Tr}(PD_\Gamma P)
 \ge d(\Gamma-\alpha).}
 \tag{R-15603.8}
\]

Thus the packet already consumes at least the whole right side of the proposed
symbol inequality.

## 3. Every nonzero deficit localization is strictly positive

Factor

\[
 D_\Gamma=K^*K,
 \qquad
 K=M_{\sqrt w}\mathcal FP_I.
 \tag{R-15603.9}
\]

First, `w` cannot vanish almost everywhere. If it did, then `D_Gamma=0`, so
(R-15603.3) would give `A>=Gamma I`, contradicting
`A|_L<=alpha I` with `alpha<Gamma` and `L!=0`.

Therefore

\[
 E=\{\xi:w(\xi)>0\}
\]

has positive measure. For every nonzero `f in L2(I)`, the compact support of
`f` makes `widehat f` an entire function. A nonzero entire function cannot
vanish on a positive-measure subset of the real axis. Consequently

\[
 \langle D_\Gamma f,f\rangle
 ={1\over2\pi}\int_Ew(\xi)|\widehat f(\xi)|^2d\xi
 >0
 \qquad(f\ne0).
 \tag{R-15603.10}
\]

Thus

\[
 \boxed{D_\Gamma\text{ is injective and strictly positive}.}
 \tag{R-15603.11}
\]

In particular it has infinite rank, since the ambient space is infinite
dimensional.

## 4. Strict trace excess outside every finite packet

The localization operator is positive trace class and has the exact trace

\[
 \boxed{
 \operatorname{Tr}D_\Gamma
 ={ |I|\over2\pi}\int_{\mathbb R}w(\xi)d\xi.}
 \tag{R-15603.12}
\]

Choose any nonzero `q in L^perp`. Strict positivity gives

\[
 \langle D_\Gamma q,q\rangle>0,
\]

and hence

\[
 \operatorname{Tr}(QD_\Gamma Q)>0.
 \tag{R-15603.13}
\]

Using an orthonormal basis adapted to `L direct-sum L^perp`,

\[
 \operatorname{Tr}D_\Gamma
 =\operatorname{Tr}(PD_\Gamma P)
  +\operatorname{Tr}(QD_\Gamma Q).
 \tag{R-15603.14}
\]

Equations (R-15603.8), (R-15603.13), and (R-15603.14) prove
(R-15603.5). QED.

## 5. Why the Berezin clipping step became vacuous

Let an auxiliary level `G>=Gamma` define

\[
 D_G=P_I\mathcal F^{-1}(G-s)_+\mathcal FP_I,
 \qquad
 \theta=G-\Gamma.
\]

The valid Berezin inequality is

\[
 \operatorname{Tr}(D_G-\theta I)_+
 \le { |I|\over2\pi}
 \int(\Gamma-s)_+.
 \tag{R-15603.15}
\]

The left side is the trace of a **spectrally clipped operator** and can have
finite rank. The right side is the full trace of the different localization
operator `D_Gamma`, which is injective and has infinite rank whenever the
symbol deficit is nonzero.

In general,

\[
 \boxed{
 (D_G-\theta I)_+
 \ne
 P_I\mathcal F^{-1}
 \bigl((G-s)_+-\theta\bigr)_+
 \mathcal FP_I.}
 \tag{R-15603.16}
\]

The scalar identity inside the multiplier does not commute with time-frequency
compression and spectral functional calculus. The Berezin upper bound remains
correct, but replacing the operator-clipped target by its symbol integral loses
exactly the uncertainty tail that makes the latter condition impossible.

## 6. Correct nonvacuous targets

### 6.1 Operator-clipped saturation

The sharp condition from `L-15618` remains valid and potentially satisfiable:

\[
 \boxed{
 \operatorname{Tr}
 \bigl(D_G-(G-\Gamma)I\bigr)_+
 \le d(\Gamma-\alpha).}
 \tag{R-15603.17}
\]

This charges only localization eigenvalues capable of crossing the target
floor.

### 6.2 Exact packet-leverage tail

The true complement deficit is

\[
 \boxed{
 \operatorname{Tr}(QD_\Gamma Q)
 ={1\over2\pi}\int_{\mathbb R}
 w(\xi)\|Qe_\xi\|_2^2d\xi,}
 \tag{R-15603.18}
\]

where `e_xi(x)=1_I(x)e^(i xi x)`. This is the leverage-weighted deficit of
`L-15607/L-15608`. A bound on (R-15603.18), rather than on the unweighted total
trace, is geometrically aligned with the packet.

### 6.3 Vanishing positive slack

Define the necessarily positive excess

\[
 \Delta
 ={ |I|\over2\pi}\int(\Gamma-s)_+
  -d(\Gamma-\alpha)>0.
 \tag{R-15603.19}
\]

Equations (R-15603.8) and (R-15603.14) imply

\[
 \operatorname{Tr}(QD_\Gamma Q)\le\Delta.
 \tag{R-15603.20}
\]

Therefore

\[
 \boxed{
 A|_{L^\perp}\succeq(\Gamma-\Delta)I.}
 \tag{R-15603.21}
\]

A valid cofinal symbol theorem may thus seek

\[
 \boxed{
 0<\Delta_j\longrightarrow0,}
 \tag{R-15603.22}
\]

with a threshold moat `t_j<Gamma_j-Delta_j`. Exact zero slack is impossible;
vanishing positive slack is sufficient.

## 7. Consequences for the current stack

1. `L-15620.3`--`L-15620.11`, the convex trace and Berezin clipping
   inequalities, remain correct.
2. `L-15620.14`--`L-15620.19` are logically valid implications from an
   impossible premise and must not be presented as a production target.
3. The finite matrix control in `L-15618/X-15605` does not contradict this
   theorem: its positive deficit matrix is finite rank and is not a genuine
   nonzero time-frequency localization operator on `L2(I)`.
4. The active scalar routes are now the operator-clipped trace, the exact
   leverage trace tail, or a vanishing-positive-slack symbol estimate.
5. No statement here proves or disproves RH. It removes a vacuous proposed
   closure gate and prevents a false proof attempt.
