# T-21702 — Critical-line convolution factorization and positive variance defect

Claim ID: `T-21702`  
Title: The completed Riemann distribution factors through the line-zero annihilator exactly under RH, and every off-line quartet contributes positively to one scalar variance gap  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — finite-product algebra and canonical-product reduction supplied; RH is not claimed proved**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Source dependencies: the centered Hadamard product for `xi`; the positive completed-Riemann density of Nakamura, *Bernoulli* 21 (2015); a classical zero-free rectangle below the first nontrivial zero  
Scope: a probability and trace form of the prime-annihilator endpoint

## 1. The completed Riemann probability law

Normalize

\[
 \Xi(t)={\xi(1/2+it)\over\xi(1/2)},
 \qquad \Xi(0)=1.
 \tag{T-21702.1}
\]

The theta-kernel representation gives a symmetric probability measure
`mu_Xi` whose characteristic function is `Xi`.  In particular,

\[
 V_\Xi:=\operatorname{Var}(\mu_\Xi)
 =-\Xi''(0)
 ={\xi''(1/2)\over\xi(1/2)}.
 \tag{T-21702.2}
\]

The last equality differentiates with respect to the real characteristic
variable `t`.

## 2. Multiplicity-weighted line-zero products

Let `Gamma_L` be the set of distinct positive critical-line ordinates and let
`m_gamma` be the multiplicity of the zero at `1/2+i gamma`.  Put

\[
 S_L=\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}<\infty
 \tag{T-21702.3}
\]

and define the canonical line factor

\[
 \boxed{
 E_L(t)=
 \prod_{\gamma\in\Gamma_L}
 \left(1-{t^2\over\gamma^2}\right)^{m_\gamma}.}
 \tag{T-21702.4}
\]

The product converges locally uniformly because of (T-21702.3).

For every occurrence of `gamma`, introduce two centered probability densities.
The first is uniform:

\[
 u_\gamma(x)={\gamma\over2\pi}
 \mathbf1_{[-\pi/\gamma,\pi/\gamma]}(x),
 \tag{T-21702.5}
\]

with characteristic function

\[
 U_\gamma(t)=
 {\sin(\pi t/\gamma)\over\pi t/\gamma}.
 \tag{T-21702.6}
\]

The second is the cosine bell

\[
 c_\gamma(x)={\gamma\over2\pi}
 \bigl(1+\cos(\gamma x)\bigr)
 \mathbf1_{[-\pi/\gamma,\pi/\gamma]}(x),
 \tag{T-21702.7}
\]

whose characteristic function is

\[
 \boxed{
 C_\gamma(t)=
 {\sin(\pi t/\gamma)
  \over(\pi t/\gamma)(1-t^2/\gamma^2)}.}
 \tag{T-21702.8}
\]

The apparent values at `t=+-gamma` are removable.  Direct integration proves
(T-21702.8), and therefore

\[
 \boxed{U_\gamma(t)=
 \left(1-{t^2\over\gamma^2}\right)C_\gamma(t).}
 \tag{T-21702.9}
\]

Take `m_gamma` independent copies at each ordinate.  Since

\[
 \operatorname{Var}(u_\gamma)={\pi^2\over3\gamma^2},
 \qquad
 \operatorname{Var}(c_\gamma)=
 {\pi^2/3-2\over\gamma^2},
 \tag{T-21702.10}
\]

the corresponding infinite random sums converge almost surely and in `L2`.
Let their laws be `mu_U` and `mu_C`, with characteristic functions `U_L` and
`C_L`.  Passing to the normal limits in (T-21702.9) gives

\[
 \boxed{U_L(t)=E_L(t)C_L(t).}
 \tag{T-21702.11}
\]

Here `mu_U` is the multiplicity-weighted version of the centered uniform
annihilator law in `T-21701`.

## 3. Exact residual factorization

The centered Hadamard product, grouped by the functional-equation and
conjugation symmetries, gives

\[
 \boxed{\Xi(t)=E_L(t)E_N(t),}
 \tag{T-21702.12}
\]

where `E_N` is the normalized canonical product over the nonreal zeros of the
entire function `t -> xi(1/2+it)`, equivalently over off-critical zeta quartets.
It is entire and satisfies `E_N(0)=1`.

Combining (T-21702.11) and (T-21702.12) yields the unconditional entire identity

\[
 \boxed{
 \Xi(t)C_L(t)=U_L(t)E_N(t).}
 \tag{T-21702.13}
\]

Therefore the following are equivalent:

1. RH;
2. `E_N` is identically one;
3. the characteristic functions satisfy
   \[
    \Xi(t)C_L(t)=U_L(t)\quad(t\in\mathbb R);
   \]
4. the probability measures satisfy the convolution identity
   \[
    \boxed{\mu_\Xi*\mu_C=\mu_U.}
    \tag{T-21702.14}
   \]

The implication from (3) to RH uses the fact that `U_L/E_L=C_L` has already
removed exactly the real zeros with their multiplicities; any off-line zero is
a zero of `E_N` and prevents `E_N` from being constant.

Thus the prime annihilator has a purely probabilistic endpoint: prove that the
completed Riemann law, convolved with the explicit cosine-bell line-zero noise,
is exactly the uniform line-zero annihilator law.

## 4. Every off-line quartet has a positive second-order charge

Choose one representative of an off-line quartet in the form

\[
 \rho={1\over2}+\delta+i\gamma,
 \qquad \delta>0,
 \quad \gamma>0,
 \tag{T-21702.15}
\]

with multiplicity `m_rho`.  In the `t` variable its quartet factor is

\[
 \left(1-{t^2\over(\gamma-i\delta)^2}\right)^{m_\rho}
 \left(1-{t^2\over(\gamma+i\delta)^2}\right)^{m_\rho}.
 \tag{T-21702.16}
\]

Its contribution to `-(log Xi)''(0)` is exactly

\[
 \boxed{
 d(\delta,\gamma)
 =4m_\rho{\gamma^2-\delta^2
 \over(\gamma^2+\delta^2)^2}.}
 \tag{T-21702.17}
\]

Every nontrivial zero lies above the classical first-zero-free rectangle, while
`0<delta<1/2`; hence `gamma^2>delta^2` and (T-21702.17) is strictly positive.
Summing the locally absolutely convergent logarithmic expansion gives

\[
 \boxed{
 D_\mathrm{off}
 :=V_\Xi-2S_L
 =4\sum_{\substack{\rho=1/2+\delta+i\gamma\\
                   \delta>0,\ \gamma>0}}
 m_\rho{\gamma^2-\delta^2
 \over(\gamma^2+\delta^2)^2}
 \ge0.}
 \tag{T-21702.18}
\]

Moreover

\[
 \boxed{D_\mathrm{off}=0\iff\mathrm{RH}.}
 \tag{T-21702.19}
\]

No cancellation between distinct off-line packets is possible at this order.
This is much sharper than a generic complex-zero trace: the geometry of the
critical strip and the large positive ordinates make every quartet carry the
same sign.

## 5. The defect is exactly the annihilator variance gap

From (T-21702.10),

\[
 \operatorname{Var}(\mu_U)={\pi^2\over3}S_L,
 \qquad
 \operatorname{Var}(\mu_C)=
 \left({\pi^2\over3}-2\right)S_L.
 \tag{T-21702.20}
\]

Therefore

\[
 \boxed{
 \operatorname{Var}(\mu_\Xi*\mu_C)
 -\operatorname{Var}(\mu_U)
 =D_\mathrm{off}.}
 \tag{T-21702.21}
\]

Consequently RH is equivalent to the single scalar equality

\[
 \boxed{
 {\xi''(1/2)\over\xi(1/2)}
 =2\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}.}
 \tag{T-21702.22}
\]

The left side is an explicit second moment of Nakamura's positive completed
Riemann density.  The right side uses only actual critical-line zeros.  Under a
false RH the left side exceeds the right side by the strictly positive charge
(T-21702.18).

This is a one-number shadow of the full prime-annihilator convolution identity.
Unlike a finite determinant sign, it cannot miss an off-line quartet by phase
cancellation.

## 6. A verified-height finite bound

Suppose every zero with `0<Im rho<=H` has been certified on the critical line.
Let `N_+(T)` count all positive-ordinate nontrivial zeros with multiplicity and
assume the explicit upper bound

\[
 N_+(T)\le aT\log T+bT
 \qquad(T\ge H).
 \tag{T-21702.23}
\]

For one off-line quartet,

\[
 d(\delta,\gamma)\le{4m_\rho\over\gamma^2}.
\]

The two positive-ordinate members of the quartet contribute
`2m_rho/gamma^2` to the ordinary reciprocal-square tail.  Hence

\[
 D_\mathrm{off}
 \le2\sum_{\substack{\Im\rho>H\\\Im\rho>0}}
 {m_\rho\over(\Im\rho)^2}.
 \tag{T-21702.24}
\]

Stieltjes integration and (T-21702.23) give the fail-safe estimate

\[
 \boxed{
 0\le D_\mathrm{off}
 \le {4\,[a(\log H+1)+b]\over H}.}
 \tag{T-21702.25}
\]

Thus the published verified-height block forces the annihilator variance
identity extremely close to saturation without assuming RH above `H`.  A finite
height cannot force exact equality, because a single off-line quartet may occur
arbitrarily high.

## 7. Relation to the completed prime endpoint

`T-21701` expresses the off-line remainder as one completed prime residual.
The present theorem expresses the same obstruction as:

```text
full residual function:  E_N(t)-1,
completed prime signal:   R_infinity(x),
positive prime energy:    script E_sigma,
second-order trace:       D_off.
```

They vanish simultaneously.  A proposed proof of the prime identity must, at a
minimum, imply the scalar saturation (T-21702.22).  Conversely, because every
off-line quartet contributes positively, proving only (T-21702.22) already
proves RH; the entire function identity need not be established separately.

## 8. Proof boundary

The finite-density transforms, product identity, variance calculations, and
positive quartet formula are elementary once the centered Hadamard product and
completed-Riemann probability law are imported.

The theorem does **not** prove (T-21702.22).  That equality is the sharpened
annihilator endpoint.  Current finite zero verification proves only the explicit
near-saturation estimate (T-21702.25).
