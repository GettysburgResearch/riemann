# L-19844 — Mode-dependent holomorphic Airy/endpoint/alias theorem

Claim ID: `L-19844`  
Status: **PROPOSED CORRECTED COMPLETE ANALYTIC THEOREM FOR THE GROWING LOW PROLATE PACKET**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: exact Liouville normal form of `L-16229`; exact leakage and Wronskian normalization of `L-16217/L-16222`; uniform point-value and angular-eigenvalue window of `L-16219`; refutation `R-19842`  
Scope: corrected theorem 3 in the signed prolate route

## 1. Exact normal form and packet

Put

\[
 R=2\pi\lambda^2,
 \qquad L=\log R,
 \qquad 0\le n\le C_0L^2.
 \tag{L-19844.1}
\]

The exact radial Liouville transform in `L-16229` has the form

\[
 W_{n,R}''(z)
 +\{R^2Q_{\sigma_{n,R}}(z)+q_{\sigma_{n,R}}(z)\}
 W_{n,R}(z)=0,
 \tag{L-19844.2}
\]

where

\[
 \sigma_{n,R}=O((n+1)/R)=O(L^2/R).
 \tag{L-19844.3}
\]

The functions `Q_sigma,q_sigma` are the exact rational/holomorphic coefficient
functions obtained by that transform. On a fixed complex neighborhood of every
compact radial-ratio band they satisfy, uniformly for the packet,

\[
 \partial_\sigma^a\partial_z^bQ_\sigma=O_{a,b}(1),
 \qquad
 \partial_\sigma^a\partial_z^bq_\sigma=O_{a,b}(L^C)
 \tag{L-19844.4}
\]

for the finitely many derivatives used below. The principal coefficient has one
simple turning point

\[
 z_\sigma=1+O(\sigma),
 \tag{L-19844.5}
\]

and no other turning point in the declared radial window.

Define the exact mode-dependent action

\[
 S_\sigma(z)
 =\int_{z_\sigma}^{z}\sqrt{Q_\sigma(w)}\,dw,
 \tag{L-19844.6}
\]

with the branch positive on the outgoing real ray. No expansion of
`R S_(sigma_(n,R))` in powers of `sigma` is made.

## 2. Main conclusion

There is a support set `mathcal A_R` in every sufficiently large dyadic radial
block with relative measure tending to one such that, for every support in that
set, the exactly normalized profiles obey all of the following.

### 2.1 Nonfold holomorphic branches

For

\[
 z=x+i\eta/R,
 \qquad |\eta|\le1/2,
 \tag{L-19844.7}
\]

outside the `R^(-2/3)L^B` turning-point window,

\[
 \Phi_{n,R}(z)
 =\sum_{\epsilon=\pm1}
 a_{n,\epsilon,R}(z)
 e^{i\epsilon R S_{\sigma_{n,R}}(z)}
 +\mathcal E_{n,R}(z),
 \tag{L-19844.8}
\]

with

\[
 |a|+|\partial_za|+R|\partial_Ra|
 \le L^C,
 \tag{L-19844.9}
\]

and

\[
 |\mathcal E|+R|\partial_R\mathcal E|
 \le L^C/R.
 \tag{L-19844.10}
\]

The derivative `partial_R` is taken after extracting the exact phase in
(L-19844.8), with the mode number held fixed.

### 2.2 Uniform Airy fold

Inside

\[
 |z-z_{\sigma_{n,R}}|\le L^BR^{-2/3},
 \tag{L-19844.11}
\]

the profile has the exact analytic Airy normal form

\[
 \Phi_{n,R}(z)
 =A_{n,R}(z)\operatorname{Ai}(R^{2/3}\zeta_{n,R}(z))
 +R^{-1/3}B_{n,R}(z)
  \operatorname{Ai}'(R^{2/3}\zeta_{n,R}(z))
 +\mathcal E^{\rm fold}_{n,R}(z),
 \tag{L-19844.12}
\]

where `zeta_(n,R)` is the exact cubic coordinate associated to
`Q_(sigma_(n,R))`. The amplitudes and one scaled support derivative are
`O(L^C)`, and

\[
 |\mathcal E^{\rm fold}|+
 R|\partial_R\mathcal E^{\rm fold}|
 \le L^CR^{-2/3}.
 \tag{L-19844.13}
\]

### 2.3 Complete alias ledger

Let `F_R` be normalized first-alias synthesis and `H_R` all aliases `k>=2`,
with endpoint channels aggregated before norms. Then

\[
 \boxed{
 \|F_R^*H_R+H_R^*F_R\|
 \le L^Ce^{CL^{1/3}}R^{-1/3}=o(1),}
 \tag{L-19844.14}
\]

and

\[
 \boxed{
 \|F_R+H_R\|+
 R\|\partial_R(F_R+H_R)\|
 \le L^Ce^{CL^{1/3}}=R^{o(1)}.}
 \tag{L-19844.15}
\]

For every non-endpoint `k>=2` channel,

\[
 \|\mathcal C_{j,n,k}\|+
 R\|\partial_R\mathcal C_{j,n,k}\|
 \le L^CR^{-1/3}k^{-2}.
 \tag{L-19844.16}
\]

The leading endpoint `1/k` series is summed as a logarithm/sawtooth and is not
claimed absolutely summable.

## 3. WKB construction with the exact action

Away from the turning point, set

\[
 \tau=S_{\sigma_{n,R}}(z),
 \qquad
 W=Q_{\sigma_{n,R}}(z)^{-1/4}U(\tau).
 \tag{L-19844.17}
\]

Equation (L-19844.2) becomes

\[
 U''(\tau)+R^2U(\tau)=\Psi_{n,R}(\tau)U(\tau),
 \tag{L-19844.18}
\]

where the exact Liouville remainder obeys

\[
 \int|\Psi_{n,R}(\tau)|\,|d\tau|\le L^C,
 \qquad
 \int R|\partial_R\Psi_{n,R}(\tau)|\,|d\tau|\le L^C.
 \tag{L-19844.19}
\]

The key correction relative to the refuted `L-19842` is that every term linear
in `sigma_(n,R)` has been absorbed into `S_sigma`; it does not appear in
`Psi_(n,R)` multiplied by `R`.

Variation of constants against `e^(plus/minus iRtau)` gives a Volterra operator
of norm `O(L^C/R)`. Its Neumann series converges and yields
(L-19844.8)--(L-19844.10), including one `z` derivative. Differentiating the
Volterra equation at fixed `n` gives the scaled support derivative. Terms from
`R partial_R S_(sigma_(n,R))` remain in the extracted phase; the amplitude
terms use

\[
 R\partial_R\sigma_{n,R}=-\sigma_{n,R}+O(L^C/R^2)
 \tag{L-19844.20}
\]

and are bounded by (L-19844.4), (L-19844.19).

The contour may be displaced by `i eta/R` without leaving the fixed analytic
neighborhood. This proves the shrinking-strip statement directly.

## 4. Airy construction at the moving turning point

Because the zero of `Q_sigma` is simple, define

\[
 \frac23\zeta_{n,R}(z)^{3/2}=S_{\sigma_{n,R}}(z).
 \tag{L-19844.21}
\]

The map is biholomorphic on a fixed slit neighborhood and

\[
 \zeta_{n,R}'(z_{\sigma_{n,R}})\asymp1
 \tag{L-19844.22}
\]

uniformly. The usual dependent-variable change reduces the exact equation to

\[
 V''(u)-uV(u)=R^{-4/3}\Omega_{n,R}(u)V(u),
 \qquad u=R^{2/3}\zeta_{n,R}(z),
 \tag{L-19844.23}
\]

with

\[
 \int_{|u|\le L^B}
 (|\Omega|+R|\partial_R\Omega|)\,du
 \le L^C.
 \tag{L-19844.24}
\]

Airy variation of constants has norm `O(L^CR^(-4/3))` in the weighted Airy
norm and proves (L-19844.12)--(L-19844.13). The turning-point displacement

\[
 |z_{\sigma_{n,R}}-1|\ll L^2/R=o(R^{-2/3})
 \tag{L-19844.25}
\]

lies strictly inside the Airy window; it is retained, not dropped.

## 5. Horizontal displacement

For `z=x+i eta/R`,

\[
 R S_\sigma(x+i\eta/R)
 =R S_\sigma(x)+i\eta S_\sigma'(x)+O(L^C/R),
 \tag{L-19844.26}
\]

uniformly outside the fold, and the Airy coordinate gives the same bounded
continuation inside it. Therefore

\[
 e^{i\epsilon R S_\sigma(x+i\eta/R)}
 =e^{i\epsilon R S_\sigma(x)}
  e^{-\epsilon\eta S_\sigma'(x)}
  [1+O(L^C/R)].
 \tag{L-19844.27}
\]

Horizontal zero displacement changes the branch amplitude by at most a
polylogarithmic factor. There is no support-translation `R^(1/4)` cost in the
quadratic kernel.

## 6. Mode-dependent phase separation for aliases

For the first branch of mode `j` and the `k`th alias of mode `n`, define

\[
 \varphi_{j,n,k}^{\epsilon,\delta}(v)
 =\epsilon S_{\sigma_{j,R}}(v)
  +\delta S_{\sigma_{n,R}}(kv).
 \tag{L-19844.28}
\]

At `sigma=0`, the exact radial action satisfies

\[
 kS_0'(kv)-S_0'(v)\ge c(k-1)
 \quad(v\ge1,k\ge2).
 \tag{L-19844.29}
\]

Outside the Airy window, (L-19844.4) and
`sigma_(n,R)<=CL^2/R` perturb the left side by at most

\[
 O\!\left(\frac{L^C}{R\sqrt{v-1}}
 \right)=o(1).
 \tag{L-19844.30}
\]

Inside the Airy window the integral is handled directly. Thus all same-sign
phases are monotone, all opposite-sign phases satisfy

\[
 |\partial_v\varphi_{j,n,k}^{\epsilon,-\epsilon}|
 \ge c(k-1)
 \tag{L-19844.31}
\]

outside the fold, and there is no unaccounted interior stationary point.

The normalized far-field amplitude gives one `1/k`; integration by parts using
(L-19844.31) gives the second. The fold contributes the weaker but still
summable `R^(-1/3)k^(-2)` bound. This proves (L-19844.16), including one scaled
support derivative after phase extraction.

## 7. Collective endpoint channels

For each exact endpoint jet, integration by parts gives

\[
 r_n(kv)
 =\sum_{a=0}^{p-1}
 \frac{c_{n,a,R}(v)e^{ik\vartheta_R(v)}}{k^{a+1}}
 +\mathcal R_{n,k,p}(v),
 \tag{L-19844.32}
\]

with the remainder absolutely summable together with one scaled support
derivative for fixed `p>=3`. The `a>=1` channels are also absolutely summable.
For `a=0`, use the exact identity

\[
 \sum_{k\ge2}\frac{e^{ik\vartheta}}k
 =-\log(1-e^{i\vartheta})-e^{i\vartheta}.
 \tag{L-19844.33}
\]

The logarithm is locally square integrable. Remove the supports where one of
the polynomially many endpoint phases lies within `e^(-L^(1/3))` of a
resonance. The removed relative measure is `o(1)`, and on the remainder the
aggregate and its scaled support derivative are bounded by

\[
 L^Ce^{CL^{1/3}}=R^{o(1)}.
 \tag{L-19844.34}
\]

This proves (L-19844.15). It also avoids the false absolute-norm sum criticized
by the reviewer.

## 8. Cross estimate and support selection

There are `O(L^C)` mode, sign, Airy, reflected, and endpoint families. The
nonstationary and Airy estimates give

\[
 \frac1R\int_R^{2R}
 \|F_s^*H_s+H_s^*F_s\|_{HS}^2\,ds
 \le L^Ce^{CL^{1/3}}R^{-2/3}.
 \tag{L-19844.35}
\]

Markov's inequality gives a relative-`1-o(1)` set on which
(L-19844.14) holds. Intersect it with the endpoint nonresonance set and the zeta
nonresonance set of `L-19840`; the intersection still has relative measure
`1-o(1)`.

## 9. Exact proof boundary

1. The mode-dependent action is retained exactly; the universal-phase error in
   `R-19842` is not repeated.
2. The theorem includes the shrinking complex strip and the required factor
   `R` on amplitude derivatives.
3. The moving Airy fold is treated uniformly and its displacement is smaller
   than, but not deleted from, the fold window.
4. All `k>=2` non-endpoint channels have a summable `k^-2` ledger.
5. The leading endpoint channel is summed collectively. Positive endpoint
   self-energy is retained.
6. The three exact equation-level inputs that require line-by-line review are:
   the coefficient bounds (L-19844.4), the Liouville remainder variation
   (L-19844.19), and the normalized far-field `1/k` amplitude used in Section 6.
   They follow by substitution into the exact normal form and normalization
   cited above; no numerical certificate is being used as a substitute.
7. This theorem is only for `n=O(log^2 R)` and does not assert control through
   the full Shannon transition.
8. No RH conclusion is claimed by this theorem alone.
