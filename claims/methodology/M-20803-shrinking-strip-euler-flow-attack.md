# M-20803 — Shrinking-strip Euler-flow attack

Claim ID: `M-20803`  
Title: Attack the full prime-prefix theorem through a positive shrinking-strip moment and a centered triangular Selberg flow  
Status: `PROPOSED RESEARCH PROGRAM — T-20803/L-20810/L-20811/L-20812/L-20813 COMPLETE; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Primary theorem: `T-20803`  
Scope: direct continuation toward the full RH, not a larger finite scan

## 1. New full-problem target

`T-20802` reduced the complete zeta-screw minimum to

\[
 M_j=Q_j-A_+^*(P_j).
 \]

`T-20803` removes the log-weighted moment `Q_j` from the cofinal proof target.
Put

\[
 \omega_j=P_j^{-2},
 \qquad
 \mathcal P_j(\omega_j)
 =\sum_{q\le q_j}{\Lambda(q)\over q^{1/2+\omega_j}}.
 \]

Then RH is equivalent to the eventual inequality

\[
 \boxed{
 {P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 \ge
 A_+^*(P_j)-{\log^2(q_j/2)\over8P_j}.}
 \tag{M-20803.1}
\]

The tolerance tends to zero. The left side contains only two positive finite
prime sums and samples the finite von Mangoldt polynomial on the canonically
shrinking line

\[
 \Re s={1\over2}+P_j^{-2}.
 \]

This is the preferred battlefield.

## 2. Exact cumulant replacement

The original entropy-scale inequality used

\[
 Q_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q}.
 \]

The new statistic is the logarithmic ratio of `P_j` and one nearby positive
moment. The exact difference is

\[
 Q_j-{P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 ={P_j\over\omega_j}\int_0^{\omega_j}
 (\omega_j-u)\operatorname{Var}_{j,u}(\log q)du.
 \tag{M-20803.2}
\]

Thus no information has been hidden in an uncontrolled Taylor expansion. The
entire replacement error is a positive cumulant with a deterministic vanishing
upper bound.

This also supplies an exact scalar bridge to the Hardy/minimum-phase program:
the prime data are moved an explicit positive distance to the right of the
critical line before any estimate is attempted.

## 3. The finite Euler flow is wholly positive

`L-20812` first writes the local truncated Euler flow as

\[
 -\partial_uP_{p,K}
 =P_{p,K}^2+(\log p)P_{p,K}-E_{p,K},
 \qquad E_{p,K}\ge0.
 \tag{M-20803.3}
\]

`L-20813` then closes the apparent cutoff-defect problem exactly:

\[
 \boxed{
 P_{p,K}^2-E_{p,K}
 = (\log p)^2
   \sum_{\ell=2}^K(\ell-1)p^{-\ell(1/2+u)}
 \ge0.}
 \tag{M-20803.4}
\]

Thus

\[
 \boxed{
 -\partial_uP_{p,K}
 =(\log p)P_{p,K}
 +(\log p)^2
  \sum_{\ell=2}^K(\ell-1)p^{-\ell(1/2+u)}.}
 \tag{M-20803.5}
\]

At cutoff `X=q_j`, define

\[
 \mathcal B_j(u)
 =\sum_{p\le X}(\log p)P_{p,K_p(X)}(u)
 \tag{M-20803.6}
\]

and

\[
 \mathcal C_j(u)
 =\sum_{\substack{p^\ell\le X\\\ell\ge2}}
 { (\Lambda*\Lambda)(p^\ell)
  \over p^{\ell(1/2+u)}}.
 \tag{M-20803.7}
\]

Both are positive, and the shifted statistic is exactly

\[
 \boxed{
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\mathcal B_j(u)+\mathcal C_j(u)
  \over\mathcal P_j(u)}du.}
 \tag{M-20803.8}
\]

The first-omitted-power defect is no longer an open gate. It is exactly the
part of the local collision square lying outside the retained exponent
triangle. The trusted arithmetic flow has no internal negative channel.

## 4. The remaining comparison

The full theorem is now

\[
 \boxed{
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\mathcal B_j(u)+\mathcal C_j(u)
  \over\mathcal P_j(u)}du
 \ge A_+^*(P_j)-\eta_j,
 \qquad
 \eta_j={\log^2(q_j/2)\over8P_j}.}
 \tag{M-20803.9}
\]

The arithmetic side is positive; the difficulty is its constant-scale
comparison with the nonlinear archimedean barrier.

At `u=0`, the diagonal Selberg channel has the unconditional centering

\[
 \mathcal C_j(0)
 ={1\over8}\log^2X+C_{\rm diag}+o(1),
 \qquad X=q_j.
 \tag{M-20803.10}
\]

The square layer supplies the only divergent term; every higher power layer is
absolutely summable. This makes the next target much narrower:

```text
subtract the explicit square-layer and archimedean constants jointly;
retain the base-prime drift and actual endpoint mass in one expression;
factor the resulting o(1)-centered remainder.
```

## 5. Four serious completion mechanisms

### A. Centered triangular Selberg factorization

Use (M-20803.10) to remove the complete diagonal higher-power asymptotic before
any inequality is taken. Seek an exact identity

\[
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\mathcal B_j+\mathcal C_j\over\mathcal P_j}du
 -A_+^*(P_j)+\eta_j
 =\mathcal Q_j^{\rm pos}+\mathcal R_j,
 \tag{M-20803.11}
\]

with `mathcal Q_j^pos>=0` and `mathcal R_j>=0` or `mathcal R_j=o(1)` with a
one-sided sign. The likely missing square is not the already-closed local
collision square; it must couple distinct base primes or the prime flow to the
archimedean channel.

### B. Gibbs-entropy chain rule

`L-20811` gives

\[
 M_j=2P_j(\mathcal K_j-D_{\rm KL}(\pi_j\|\rho_j))
 \tag{M-20803.12}
\]

and splits the entropy into

\[
 D_{\rm KL}(\Pi\|R)
 +\sum_p\Pi_pD_{\rm KL}(g_p\|u_p).
 \tag{M-20803.13}
\]

The power cost is explicit; the true arithmetic term is the base-prime
marginal. A viable entropy proof should compare that marginal with the smooth
curvature law while retaining `o(P^-1)` entropy slack. A fixed Rényi order is
ruled out because it loses `Theta(P_j)`; the order must approach one at the
shrinking-strip scale.

### C. Selberg/reflection bridge

`L-15415` converts the reflected quadratic logarithmic-derivative energy into a
positive Selberg coefficient stream plus one derivative and one archimedean
term. `L-19810/L-19811` isolate off-line zeros as positive anti-causal Poisson
energy.

The high-value bridge is now

\[
 \text{centered positive flow in (M-20803.9)}
 \quad\longleftrightarrow\quad
 \text{anti-causal strip energy}.
 \tag{M-20803.14}
\]

A proof that the centered finite Euler flow exhausts the positive Hardy energy
would close the minimum-phase theorem and RH simultaneously.

### D. Prime-curvature block transport

The original exact recurrence remains useful:

\[
 M_b=M_{a-1}
 +\sum_{r=a}^bw_r\tau_r
 -\int_{P_{a-1}}^{P_b}\chi(p)dp.
 \tag{M-20803.15}
\]

The shifted statistic gives a stable positive lower surrogate for the incoming
and outgoing reserve. A cofinal block proof may combine the exact total block
transport moment, positive triangular flow, maximum internal drawdown, and the
deterministic tilt allowance.

## 6. Shortcuts now ruled out

### Fixed right line

For every fixed `alpha>1`, the Rényi lower bound misses `Q_j` by
`c_alpha P_j`. Better constants on a fixed line cannot reach the RH reserve.

### Prime-only replacement

Higher prime powers carry the complete triangular convolution and the explicit
power entropy. Dropping them changes the constant-scale sign.

### Completed local Euler factors

For `K=1`, the completed-factor collision square is entirely outside the finite
prefix. Completing every local factor without the retained-power triangle
manufactures a false positive reserve.

### Separate PNT bounds

The pole-sized main terms cancel before the final sign. Bounding prime and
archimedean channels separately leaves an error vastly larger than the target.

## 7. Production protocol

A proof-producing block should emit:

```text
complete prime-power manifest
P_j and omega_j=P_j^-2
positive shifted sum mathcal P_j(omega_j)
exact tilt-variance defect or Hoeffding upper
Fenchel entropy barrier and O(P^-5) correction
base-prime drift mathcal B_j
positive triangular/diagonal Selberg channel mathcal C_j
square-layer centered constant and tail
exact block transport and maximum internal drawdown
final directed shifted margin
```

Every transcendental quantity should have two independent producers. The
positive shifted sum should be accumulated through `expm1/log1p` forms to avoid
losing the `P^-2` displacement in subtraction.

## 8. What would finish the theorem

The clean endpoint is

\[
 \boxed{
 \exists J_0\ \forall j\ge J_0:
 {P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 -A_+^*(P_j)+{\log^2(q_j/2)\over8P_j}
 \ge0.}
 \tag{M-20803.16}
\]

By `T-20803`, this is equivalent to RH.

The preferred proof is a centered positive decomposition of
`mathcal B_j+mathcal C_j` after the square layer and archimedean barrier are
assembled jointly. The alternative is a direct strip-reflection identity
proving the same inequality from Hardy energy.

## 9. Honest status

The logarithmic moment has been replaced by a positive shrinking-strip sum; the
replacement error is exact; and the apparent finite-Euler negative channel has
been removed by an exact triangular convolution identity. The remaining
positive arithmetic-versus-archimedean comparison has not been proved.
No RH resolution is claimed in this file.