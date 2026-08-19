# Canonical scalar reconstruction after the latest hostile audits

**Scientific status:** exact hostile reconstruction. **RH remains unproved.**

## 1. Binding source correction

PR #652 proves that the contracted alpha-child tree does not reproduce the native rough Euler coefficients. In one prime its shifted coefficient is zero, whereas the native factor `(I-p^{-1/2}U_p)` requires `-p^{-1/2}`. A bounded calibration cannot repair that macroscopic source mismatch unless it is propagated through the native operator. Consequently the component-row candidates stacked on that promotion cannot be assembled into a valid proof.

The strongest live conclusion-facing object is therefore the scalar factor-67 SHARP defect

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n),
\]

where

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\]

Its exact Mellin transform is

\[
\int_1^\infty h(x)x^{-s-1}\,dx
=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\]

## 2. The negative-mass criterion is equivalent to RH

Put

\[
M_-(X)=\int_1^X h_-(t)\frac{dt}{t}.
\]

PR #653 proves

\[
M_-(X)=O_\varepsilon(X^\varepsilon)\ \forall\varepsilon>0
\quad\Longrightarrow\quad RH.
\]

The converse also holds. Under RH, truncated Perron inversion on every fixed line `Re(s)=1/2+delta` gives

\[
M(x)=\sum_{n\le x}\mu(n)=O_\delta(x^{1/2+\delta}).
\]

Since

\[
B_\beta(x)=\sum_{n\le x}\beta(n)=M(x)-M(x/67),
\]

partial summation gives

\[
A_\beta(x)=\sum_{n\le x}\frac{\beta(n)}n
=O_\delta(x^{-1/2+\delta}),
\]

and

\[
C_\beta(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}
=O_\delta(x^\delta).
\]

Because

\[
h(x)=4\sqrt x\,A_\beta(x)-3C_\beta(x),
\]

we have `h(x)=O_delta(x^delta)`, and therefore `M_-(X)=O_epsilon(X^epsilon)` for every epsilon. Thus

\[
\boxed{RH\iff M_-(X)=X^{o(1)}.}
\]

The scalar criterion is weaker than pointwise positivity, but not weaker in logical strength.

## 3. Exact owner martingale

Let

\[
g(n)=v_{67}(n)+1,
\qquad
G(s)=\frac{\zeta(s)}{1-67^{-s}},
\qquad
B(s)=G(s)^{-1}.
\]

Write `n=67^e m`, `67 not| m`. Then

\[
\beta(67^em)=
\begin{cases}
\mu(m),&e=0,\\
-2\mu(m),&e=1,\\
\mu(m),&e=2,\\
0,&e\ge3.
\end{cases}
\]

Put `f(n)=beta(n)/g(n)`. Define

\[
\Lambda_g(q)=
\begin{cases}
2\log67,&q=67^a,\\
\log p,&q=p^a,\ p\ne67,\\
0,&\text{otherwise}.
\end{cases}
\]

Coefficient comparison in the logarithmic derivatives of `G` and `B=1/G` gives

\[
g(n)\log n=\sum_{q\mid n}\Lambda_g(q)g(n/q),
\]

\[
-\beta(n)\log n=\sum_{q\mid n}\Lambda_g(q)\beta(n/q).
\]

Hence

\[
\mathbb P_n(q)=
\frac{\Lambda_g(q)g(n/q)}{g(n)\log n}
\]

is a probability distribution and

\[
f(n)=-\sum_{q\mid n}\mathbb P_n(q)f(n/q).
\]

If `N_{t+1}=N_t/q_t` is the resulting divisor chain, then

\[
M_t=(-1)^t f(N_t)
\]

is a bounded martingale. Its exact quadratic variation is

\[
\boxed{
1-f(n)^2
=
\mathbb E_n\sum_{t<\tau}
\bigl(f(N_t)+f(N_{t+1})\bigr)^2.
}
\]

## 4. Exact degeneracy on the difficult source

If `m` is squarefree and `e=0` or `e=1`, then `|f(67^e m)|=1`. Every positive-probability owner removes one prime factor and satisfies

\[
f(n/q)=-f(n).
\]

Thus every martingale increment is zero, and the quadratic variation vanishes identically on the two bands carrying coefficients `mu(m)` and `-2mu(m)`.

Therefore one-chain quadratic variation, one-chain Poincare energy, one-chain entropy production, or randomness in the owner choice cannot control the hard Möbius cancellation. The remaining theorem must correlate different squarefree cores.

## 5. Exact Selberg prime-continuum identity

Put

\[
k(u)=\sqrt u+1-u^{-3/2}.
\]

Direct integration gives

\[
\log y\,T(y)
=
\int_1^yT(y/u)k(u)\frac{du}{u}.
\]

Combining this with the beta logarithmic-owner identity yields

\[
\boxed{
\log x\,h(x)
=
\int_1^xh(x/u)k(u)\frac{du}{u}
-
\sum_{q\le x}\frac{\Lambda_g(q)}{\sqrt q}h(x/q).
}
\]

The exact driver is the signed measure

\[
d\nu_g(u)=k(u)\frac{du}{u}
-
\sum_q\frac{\Lambda_g(q)}{\sqrt q}\delta_q(du).
\]

Its cumulative discrepancy is

\[
R_g(X)=2\sqrt X+\log X-\frac83+\frac{2}{3}X^{-3/2}
-
\sum_{q\le X}\frac{\Lambda_g(q)}{\sqrt q}.
\]

The atomic and continuous parts are mutually singular. A source-blind positive completion pays total variation and destroys the required cancellation.

## 6. Three-band squarefree-core theorem

Define

\[
\Phi(y)=T(y)-\frac2{\sqrt{67}}T(y/67)+\frac1{67}T(y/67^2).
\]

Then

\[
\boxed{
h(x)=
\sum_{\substack{m\le x\\(m,67)=1}}
\frac{\mu(m)}{\sqrt m}\Phi(x/m).
}
\]

For one multiplicative block put

\[
\mathcal E(X)=\int_X^{67X}|h(t)|^2\frac{dt}{t}.
\]

Its exact Gram expansion is

\[
\mathcal E(X)=
\sum_{m,n}
\frac{\mu(m)\mu(n)}{\sqrt{mn}}
\int_X^{67X}\Phi(t/m)\Phi(t/n)\frac{dt}{t}.
\]

The kernel is positive semidefinite, but smallness requires the off-diagonal squarefree-core signs before absolute values.

Moreover

\[
\boxed{RH\iff \mathcal E(X)=X^{o(1)}.}
\]

The forward implication follows from `h(x)=O_epsilon(x^epsilon)`. For the reverse implication, Cauchy-Schwarz gives subpower negative mass on every 67-adic block, and summing the blocks invokes the equivalent criterion above.

## 7. Binding verdict

```text
native alpha-child promotion             false
sequential first-owner coefficient law   exact
future-completed current sign FCHD67      open / RH-bearing
scalar Mellin and Landau consumer         exact
subpower negative mass                    equivalent to RH
one-chain owner martingale                exact but degenerate
prime-continuum Selberg balance           exact
three-band cross-core square              equivalent to RH
complete proof of RH in repository        no
```

No bulletproof full proof can presently be assembled from the live repository. The first unsupported theorem is the nonlocal squarefree-core correlation, now exposed without source-ownership, calibration, or entropy ambiguity.
