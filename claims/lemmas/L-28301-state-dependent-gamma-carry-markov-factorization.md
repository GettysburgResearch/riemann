# L-28301 — State-dependent Gamma–carry Markov factorization

Claim ID: `L-28301`  
Title: The sharp Gamma target is an exact positive Markov-additive image of the carry law, although it is not known to be an independent convolution factor  
Status: **PROPOSED COMPLETE EXACT PROBABILITY/OPERATOR LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #283  
Dependencies: PR #247 `L-23804`, `R-23802`  
Scope: continuum state-augmented positivity; no finite arithmetic discretization and no RH conclusion

## 1. Explicit coupling

Let `U,V` be independent random variables with density

\[
2u\,\mathbf1_{0<u<1}\,du.
\]

Put

\[
M=\lfloor V^{-2}\rfloor,
\tag{L-28301.1}
\]

\[
T=\log\frac{M(M+1)}{M+U},
\tag{L-28301.2}
\]

and

\[
G=-4\log(UV).
\tag{L-28301.3}
\]

PR #247 proves that `T` has the carry density

\[
 p(t)=2e^{-t}K(e^t),
 \qquad
 K(x)=\frac{\lfloor x\rfloor(\lfloor x\rfloor+1-x)}x,
\tag{L-28301.4}
\]

and that

\[
G\sim\operatorname{Gamma}(2,1/2),
\qquad
 g(y)=\frac y4e^{-y/2}\mathbf1_{y\ge0}.
\tag{L-28301.5}
\]

Moreover

\[
\boxed{G\ge T\quad\text{almost surely}.}
\tag{L-28301.6}
\]

Define the residual state

\[
S=G-T\ge0.
\tag{L-28301.7}
\]

## 2. Exact joint measure

For every nonnegative measurable function `Phi`, define

\[
\boxed{
\int\Phi(t,s)\,d\Pi(t,s)
=
\int_0^1\!\int_0^1
4uv\,
\Phi\left(
 \log\frac{m(m+1)}{m+u},
 -4\log(uv)-\log\frac{m(m+1)}{m+u}
\right)du\,dv,
}
\tag{L-28301.8}
\]

where `m=floor(v^{-2})` in the integrand.

Then `Pi` is a probability measure supported on

\[
\{(t,s):t\ge0,\ s\ge0\}.
\]

Its first marginal is `p(t)dt`, and the pushforward under

\[
(t,s)\longmapsto t+s
\]

is `g(y)dy`.

Equivalently, for every nonnegative measurable `F`,

\[
\boxed{
\int_0^\infty F(y)g(y)\,dy
=
\iint F(t+s)\,d\Pi(t,s).
}
\tag{L-28301.9}
\]

This is an exact positive factorization of the sharp target through the carry
state.

## 3. Markov-kernel form

By disintegration there is a measurable probability kernel

\[
\kappa_t(ds)
\]

such that

\[
d\Pi(t,s)=p(t)dt\,\kappa_t(ds).
\]

Define

\[
(\mathcal KF)(t)=\int_0^\infty F(t+s)\,\kappa_t(ds).
\tag{L-28301.10}
\]

Then `mathcal K` is positive, unital, and contractive on bounded functions, and

\[
\boxed{
\int F(y)g(y)dy
=
\int p(t)(\mathcal KF)(t)dt.
}
\tag{L-28301.11}
\]

Thus the Gamma law is a **Markov-additive image** of the carry law.

The scalar convolution-factor theorem `GCF` would require

\[
\kappa_t=\nu
\quad\text{independent of }t.
\]

That is not asserted here.

## 4. The state dependence is genuine

On the layer `M=m`, recover

\[
u=m(m+1)e^{-t}-m.
\]

Conditionally on `T=t`, the residual support is

\[
\boxed{
\begin{aligned}
I_m(t)=\big[&2\log m-4\log u-t,\\
            &2\log(m+1)-4\log u-t\big).
\end{aligned}}
\tag{L-28301.12}
\]

Both endpoints vary with `t`.  Hence the exact coupling is not secretly an
independent scalar residual.

This is the feature, not a defect, for the atomized carry programme: the finite
split coordinate retains state information which scalar log convolution had
averaged away.

## 5. Vector-valued and two-frequency lift

Let `H:[0,infinity)->C^d` be measurable with finite quadratic integral.  Applying
(L-28301.9) entrywise gives

\[
\boxed{
\int g(y)H(y)H(y)^*dy
=
\int p(t)\int\kappa_t(ds)
 H(t+s)H(t+s)^*.
}
\tag{L-28301.13}
\]

The identity is an equality of positive semidefinite matrices.  More generally,
for two vector-valued functions `H_1,H_2`, polarization retains every mixed
cross term.

Therefore the state-dependent factorization is compatible with the independent-
frequency physical normal block of PR #241.  It may be lifted through a common
arithmetic fiber by the congruence principle of PR #282 without replacing a
Hermitian square by a scalar analytic square.

## 6. Why this changes the proof search

The earlier scalar route asked for

\[
g=\nu*p
\]

with one translation-invariant positive measure `nu`.  Sharp scalar finite
minorants compactify to that same problem, so they do not evade GCF.

The exact identity above instead supplies

\[
g=p\mathcal K
\]

with a positive state-dependent kernel.  The corresponding finite task is not
to prove complete monotonicity of one reciprocal-zeta quotient.  It is to retain
the hidden quotient/split state while realizing the Markov transport in the
Pascal fragmentation cone.

That finite realization is the `SAPC` theorem of `T-28301`.

## 7. Proof boundary

Closed exactly:

- the explicit joint coupling;
- positivity and support `S>=0`;
- the carry and Gamma marginals;
- the Markov-kernel identity;
- the matrix-valued completely positive lift;
- the distinction from independent convolution.

Open:

- a finite source-bound Pascal realization of this state kernel;
- a subpower cycle-debt recurrence;
- RH.