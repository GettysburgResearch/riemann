# L-90019 — Fractional endpoints are positive Gamma smoothings of one prime–radical flux

Claim ID: `L-90019` (provisional branch range)  
Title: After critical normalization and one integration by parts, every fractional prime endpoint is a positive Gamma-kernel potential of an explicit signed measure with positive prime atoms and radical cell density  
Status: **PROPOSED COMPLETE EXACT STIELTJES/GAMMA THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-90016/L-90017`; PR #352 `T-90010`  
Scope: exact positive-kernel representation; no sign theorem for the flux potential and no RH conclusion

## 1. Critically normalized source

For a nonnegative arithmetic weight `lambda`, retain the positive occupancy source

\[
 \mathcal Q_\lambda(t)
 =e^{-t/2}\sum_{q\le e^t}\lambda(q)\Delta_q(e^t).
\]

Define its critical normalization

\[
\boxed{
 R_\lambda(t)=e^{-t/2}\mathcal Q_\lambda(t)
 =e^{-t}\sum_{q\le e^t}\lambda(q)\Delta_q(e^t).
}
\tag{L-90019.1}
\]

It is nonnegative and right-continuous. For the prime weight, write simply `R_P`.

## 2. The Gamma kernel

For `sigma>1`, define

\[
\boxed{
 G_\sigma(a)
 ={a^{\sigma-1}e^{-a/2}\over\Gamma(\sigma)},
 \qquad a\ge0.
}
\tag{L-90019.2}
\]

This is positive. Its derivative is exactly the critically normalized one-sign-change kernel of `L-90016`:

\[
\boxed{
 G_\sigma'(a)
 =e^{-a/2}
 {a^{\sigma-2}\over\Gamma(\sigma-1)}
 \left(1-{a\over2(\sigma-1)}\right)
 =e^{-a/2}h_\sigma(a).
}
\tag{L-90019.3}
\]

For `sigma=2`,

\[
 G_2(a)=ae^{-a/2}.
\]

Up to the harmless normalizing factor `2^sigma`, `G_sigma` is the density kernel of a Gamma distribution with shape `sigma` and rate `1/2`.

## 3. Positive-kernel Stieltjes identity

`L-90016.17` gives

\[
 -\mathscr F_{\lambda,\sigma}(t)
 =\int_0^t h_\sigma(t-u)\mathcal Q_\lambda(u)\,du.
\]

Multiply by `e^{-t/2}` and use (L-90019.1)--(L-90019.3):

\[
 -e^{-t/2}\mathscr F_{\lambda,\sigma}(t)
 =\int_0^tG_\sigma'(t-u)R_\lambda(u)\,du.
\tag{L-90019.4}
\]

Since `G_sigma(0)=0` and the source vanishes before its first arithmetic activation, Stieltjes integration by parts gives

\[
\boxed{
 -e^{-t/2}\mathscr F_{\lambda,\sigma}(t)
 =\int_{[0,t]}G_\sigma(t-u)\,dR_\lambda(u).
}
\tag{L-90019.5}
\]

Thus the one-sign-change Green kernel has disappeared. The full sign problem is a positive Gamma potential of the signed derivative measure of one nonnegative normalized source.

At `sigma=2`,

\[
\boxed{
 -e^{-t/2}A(e^t)
 =\int_{[0,t]}(t-u)e^{-(t-u)/2}\,dR_{\mathbb P}(u).
}
\tag{L-90019.6}
\]

## 4. Exact prime–radical flux

For the prime source, `L-90017` gives on the open cell

\[
 \log N<u<\log(N+1)
\]

that

\[
 \mathcal Q_{\mathbb P}'(u)
 ={1\over2}\mathcal Q_{\mathbb P}(u)
  -e^{-u/2}S_1(N).
\]

Therefore

\[
\boxed{
 R_{\mathbb P}'(u)=-e^{-u}S_1(N)
 \qquad(\log N<u<\log(N+1)).
}
\tag{L-90019.7}
\]

At a prime `p`, `L-90017.6` gives

\[
\boxed{
 \Delta R_{\mathbb P}(\log p)
 ={\log p\over p}.
}
\tag{L-90019.8}
\]

Hence, exactly as a signed locally finite measure,

\[
\boxed{
 dR_{\mathbb P}(u)
 =\sum_p{\log p\over p}\,\delta_{\log p}(du)
  -e^{-u}S_1(\lfloor e^u\rfloor)\,du.
}
\tag{L-90019.9}
\]

The atom stream is positive and purely prime. The continuous cell density is the signed radical moment from `L-90017`.

## 5. Explicit Gamma-potential formula

Substitute (L-90019.9) into (L-90019.5):

\[
\boxed{
\begin{aligned}
 -e^{-t/2}\mathscr A_\sigma(t)
 ={}&\sum_{p\le e^t}{\log p\over p}
      G_\sigma(t-\log p)\\
 &-\sum_{N<e^t}S_1(N)
   \int_{\log N}^{\min(\log(N+1),t)}
   e^{-u}G_\sigma(t-u)\,du.
\end{aligned}}
\tag{L-90019.10}
\]

Every kernel appearing here is nonnegative. All cancellation is now confined to the explicit competition between prime atoms and radical cell charges.

For `sigma=2`, eventual positivity of the right side is exactly the prime endpoint criterion and hence RH. For every fixed `sigma>1`, the analogous eventual sign is the fractional criterion of `T-90010`.

## 6. Connection to Gamma/Pascal routes

The natural age kernel in the endpoint programme is not merely reminiscent of a Gamma law: it is exactly the Gamma shape-`sigma`, rate-`1/2` kernel after critical normalization.

In particular:

```text
sigma=2 endpoint:
    Gamma(2,1/2) potential of the prime-radical flux;

sigma=3/2 half derivative:
    Gamma(3/2,1/2) potential;

sigma down to 1:
    the critical monotonicity boundary.
```

This places the endpoint route in the same positive-kernel geometry as the Gamma-carry and martingale-Pascal programmes, but with a different remaining lift: here the unresolved object is the sign of an explicit arithmetic flux potential, not existence of a continuum coupling.

No claim is made that the probability theorems on those branches automatically sign (L-90019.10). Any import must preserve the prime atoms and the radical density exactly.

## 7. Proof-facing target

The minimal new target may be stated without `A`, Mellin transforms, or signed Green kernels:

> **Prime–radical Gamma potential.** Prove that the right side of (L-90019.10) is positive eventually for one, equivalently every RH-equivalent, fixed `sigma>1`.

At `sigma=2` this is exactly RH-equivalent. A valid proof may exploit variation diminution or martingale transport, but it must act on the complete signed flux (L-90019.9) before separating its positive and negative parts.

## 8. Proof boundary

Closed exactly:

1. the positive Gamma kernel and its derivative identity;
2. Stieltjes conversion of every fractional endpoint;
3. the explicit prime-atom/radical-density flux;
4. the complete Gamma-potential formula;
5. the exact structural bridge to the Gamma/Pascal geometry.

Open:

1. eventual positivity of the Gamma potential;
2. the endpoint or fractional endpoint sign;
3. RH.