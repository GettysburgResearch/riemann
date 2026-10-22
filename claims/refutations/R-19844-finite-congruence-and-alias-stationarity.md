# R-19844 — The finite tail congruence fails, and every later alias has one stationary point

Claim ID: `R-19844`  
Status: **VERIFIED REFUTATION OF `T-19810.18` AND `L-19844` AS WRITTEN**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: exact residual identity `L-19832`; exact radial action of `L-16222/L-19829`  
Scope: adversarial response to the second review of the quotient-energy proposal

## 1. The finite congruence in `T-19810.18` is false

Let

\[
 J=E(f),\qquad g=P_\lambda J,\qquad t=(I-P_\lambda)J,
\]

and let the finite CCM vector be

\[
 v=P_Ng,\qquad q=(I-P_N)g.
\]

Since the global arithmetic image `J` lies in the weak Weil radical,

\[
 \widehat J(s_\rho)=0
\]

at every nontrivial-zero parameter. Therefore

\[
 J-v=t+q,
\]

and the exact finite zero-side matrix is

\[
 \boxed{A_{\rm fin}=Z(t+q,t+q).}
\]

It is not `Z(t,t)` unless `q=0` in the complete zero-side form. Consequently

\[
 A_{\rm fin}
 =Z(t,t)+Z(t,q)+Z(q,t)+Z(q,q).
\]

This is the identity already proved in `L-19832`. Hence the assertion

\[
 A_R^V=S_R^{-*}A_R^US_R^{-1}
\]

in `T-19810.18`, where `A_R^U` is built only from the omitted support tail, is not the exact finite CCM matrix.

**Disposition.** `T-19810.18` is rejected. The quotient-energy theorem survives, but it must either use the complete residual `e=t+q` or avoid finite Fourier projection altogether.

## 2. The later-alias phase is stationary

At separation parameter `sigma=0`, the radial action satisfies

\[
 \xi_0'(v)=\frac{v}{\sqrt{v^2-1}},\qquad v>1.
\]

For the first-versus-`k` difference phase

\[
 \phi_k(v)=\xi_0(v)-\xi_0(kv),\qquad k\ge2,
\]

one has

\[
 \phi_k'(v)
 =\frac{v}{\sqrt{v^2-1}}
 -\frac{k^2v}{\sqrt{k^2v^2-1}}.
\]

The equation `phi_k'(v)=0` is equivalent to

\[
 \frac1{v^2-1}=\frac{k^4}{k^2v^2-1},
\]

and therefore has the unique solution

\[
 \boxed{v_k^2=1+\frac1{k^2}.}
\]

Thus the blanket nonstationarity assertion in current `L-19844` is false.

For nonzero packet parameters `sigma_j,sigma_n`, `L-19829` derives the exact stationary equation and proves a unique perturbation with

\[
 v_{jnk}^2-1=\Theta(k^{-2}),
\qquad
 |\phi_{jnk}''(v_{jnk})|\asymp k^3.
\]

The stationary contribution is not fatal: normalized stationary phase gives

\[
 O\!\left(R^{-1/2}k^{-2}(\log R)^C\right),
\]

which is summable over `k`. But it must be retained.

## 3. The radial endpoint is Bessel, not Airy

The singular endpoint `v=1` in the radial prolate equation is treated by the simple-pole/Bessel normalization used in `L-16222/L-16229`. The Airy normal form belongs to the later fold of the Mellin stationary-frequency map. Conflating these two geometries invalidates the endpoint paragraph of `L-19844`.

The corrected architecture is:

```text
radial endpoint v=1       -> Bessel/simple-pole model;
first-versus-k alias      -> one nondegenerate stationary point;
Mellin frequency fold     -> Airy/cubic model;
far endpoint aliases      -> collective Fourier-series summation.
```

## 4. What is not refuted

This file does not refute:

- the signed `d_4,d_6` pure-prolate hierarchy;
- the exact quotient-energy min--max theorem;
- the stationary estimate of `L-19829`;
- the possibility of a projection-free continuous localized-Weil proof.

It refutes only the finite omitted-tail congruence and the stated alias geometry. No RH conclusion is made here.
