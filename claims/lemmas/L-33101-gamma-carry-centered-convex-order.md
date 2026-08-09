# L-33101 — Gamma–carry centered convex order

Claim ID: `L-33101`  
Title: The exact carry law, shifted to the Gamma mean, is dominated by `Gamma(2,1/2)` in convex order  
Status: **PROPOSED COMPLETE EXACT PROBABILITY THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Issue: #331  
Dependencies: PR #247 `L-23804/R-23802` only for the identification of the carry and Gamma variables  
Scope: exact probability/stop-loss theorem; no finite Pascal lift and no RH conclusion

## 1. Variables

Let `U,V` be independent with density

\[
2u\,\mathbf 1_{0<u<1}\,du.
\]

Put

\[
M=\lfloor V^{-2}\rfloor,
\qquad
T=\log\frac{M(M+1)}{M+U},
\]

and

\[
G=-4\log(UV).
\]

PR #247 identifies `T` with the continuum carry law and proves

\[
G\sim\operatorname{Gamma}(2,1/2).
\]

The present theorem does **not** use the already-known coupling inequality `G>=T`; it derives a stronger centered distributional order directly from the exact law of `T`.

## 2. Exact tail of the carry law

Since `V^2` is uniform on `(0,1)`,

\[
\mathbb P(M=m)
=
\frac1m-\frac1{m+1}
=
\frac1{m(m+1)}.
\tag{L-33101.1}
\]

Fix `t>=0`, write

\[
x=e^t,
\qquad
m=\lfloor x\rfloor,
\qquad m\le x<m+1.
\]

All layers `M>=m+1` automatically satisfy `T>t`, and their total mass is

\[
\sum_{r\ge m+1}\frac1{r(r+1)}=rac1{m+1}.
\]

On the layer `M=m`,

\[
T>t
\iff
U<\frac{m(m+1)}x-m
=:\,u_x.
\]

The `Beta(2,1)` distribution has CDF `u^2`. Hence

\[
\boxed{
\mathbb P(T>t)
=
\frac1{m+1}
+
\frac{u_x^2}{m(m+1)},
\qquad
u_x:=\frac{m(m+1-x)}x.
}
\tag{L-33101.2}
\]

(Here `u_x=nu_x`; the second symbol is introduced only to make the next algebra shorter.)

Multiplying by `x`, the desired exponential-tail comparison is equivalent to

\[
x^2+m(m+1-x)^2\le(m+1)x.
\]

Write `x=m+y`, `0<=y<1`. The left side minus the right side is exactly

\[
(m+1)y(y-1)\le0.
\]

Therefore

\[
\boxed{
\mathbb P(T>t)\le e^{-t}
\qquad(t\ge0).
}
\tag{L-33101.3}
\]

Thus `T` is stochastically dominated by an `Exp(1)` variable. Equality occurs at the logarithmic integer knots.

## 3. Exact mean

The Laplace transform from the carry law is

\[
P(s)=\mathbb E[e^{-sT}]
=
\frac{2s\zeta(s+1)}{(s+1)(s+2)}.
\]

Using

\[
\zeta(1+s)=\frac1s+\gamma+O(s)
\]

at the origin gives

\[
P(s)=1+(\gamma-3/2)s+O(s^2).
\]

Hence

\[
\boxed{
\mathbb E T=\frac32-\gamma.
}
\tag{L-33101.4}
\]

Since `G~Gamma(2,1/2)`, `E G=4`. Define the exact mean correction

\[
\boxed{
C=4-\mathbb ET=\frac52+\gamma.
}
\tag{L-33101.5}
\]

Then

\[
\mathbb E(T+C)=\mathbb E G=4.
\]

## 4. Stop-loss bound for `T`

For `b>=0`, the tail formula for a nonnegative variable gives

\[
\operatorname{SL}_T(b)
:=\mathbb E[(T-b)_+]
=
\int_b^\infty\mathbb P(T>t)\,dt.
\]

By (L-33101.3),

\[
\boxed{
\operatorname{SL}_T(b)\le e^{-b}.
}
\tag{L-33101.6}
\]

## 5. Gamma stop-loss

The `Gamma(2,1/2)` survival function is

\[
\mathbb P(G>a)=e^{-a/2}\left(1+\frac a2\right),
\qquad a\ge0.
\]

Integrating once,

\[
\boxed{
\operatorname{SL}_G(a)
=(a+4)e^{-a/2}
\qquad(a\ge0).
}
\tag{L-33101.7}
\]

For `a<0`, both `G` and `T+C` are nonnegative and the stop-loss is simply the mean minus `a` whenever the threshold lies below the support.

## 6. Convex-order comparison

We prove

\[
\boxed{
T+C\le_{\rm cx}G.
}
\tag{L-33101.8}
\]

Since the two variables have equal finite means, it is enough to compare their stop-loss transforms at every real threshold.

### Thresholds `a<=C`

Because `T>=0`,

\[
\operatorname{SL}_{T+C}(a)=4-a.
\]

For `a<=0` this equals `SL_G(a)`. For `0<=a<=C`, put

\[
d(a)=(a+4)e^{-a/2}-(4-a).
\]

Then `d(0)=0` and

\[
d'(a)=1-\mathbb P(G>a)=\mathbb P(G\le a)\ge0.
\]

Thus

\[
\operatorname{SL}_{T+C}(a)\le\operatorname{SL}_G(a).
\tag{L-33101.9}
\]

### Thresholds `a>C`

Write `a=C+b`, `b>0`. By (L-33101.6),

\[
\operatorname{SL}_{T+C}(a)
=
\operatorname{SL}_T(b)
\le e^{-b}.
\]

On the other hand

\[
\frac{\operatorname{SL}_G(C+b)}{e^{-b}}
=(C+b+4)e^{b/2-C/2},
\]

which is increasing in `b`. Hence it is enough to prove

\[
(C+4)e^{-C/2}>1.
\tag{L-33101.10}
\]

The elementary bound `0<gamma<1` gives `C<7/2`. The function

\[
x\mapsto(x+4)e^{-x/2}
\]

is decreasing for `x>0`, so

\[
(C+4)e^{-C/2}
>
\frac{15}{2}e^{-7/4}.
\]

Finally `e^{7/4}<e^2<15/2`. For completeness, the last strict inequality follows directly from the exponential series:

\[
\sum_{n=0}^{5}\frac{2^n}{n!}=\frac{109}{15},
\]

while for `n>=6` successive terms have ratio at most `2/7`, so

\[
\sum_{n=6}^\infty\frac{2^n}{n!}
\le
\frac{4/45}{1-2/7}
=
\frac{28}{225}.
\]

Thus

\[
e^2<\frac{109}{15}+\frac{28}{225}<\frac{15}{2}.
\]

This proves (L-33101.10), hence the stop-loss inequality for every `a>C`.

Combining the two threshold ranges proves (L-33101.8).

## 7. Martingale consequence

By the standard one-dimensional Strassen characterization of convex order, there exists a coupling `(X,Y)` with

\[
X\overset d=T+C,
\qquad
Y\overset d=G,
\qquad
\boxed{\mathbb E[Y\mid X]=X.}
\tag{L-33101.11}
\]

Thus the sharp Gamma target is a mean-preserving spread of the centered carry law.

This is strictly different from both previous couplings:

- `G>=T` is a monotone but non-centered coupling;
- `G=T+S` with `S` independent is the still-open scalar convolution-factor statement `GCF`.

The theorem here supplies the exact intermediate structure the atomized/Pascal programme had been seeking: a positive **state-dependent martingale transport**.

## 8. Proof boundary

Established here:

1. the exact tail of the carry law;
2. `T <=_st Exp(1)`;
3. the exact carry mean;
4. the complete stop-loss comparison;
5. `T+C <=_cx G`;
6. existence of a martingale coupling to the sharp Gamma law.

Not established here:

1. an exact finite Pascal realization of the martingale kernel;
2. a subpower Cycle-Debt estimate from this coupling;
3. RH.
