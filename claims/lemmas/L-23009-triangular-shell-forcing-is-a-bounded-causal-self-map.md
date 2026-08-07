# L-23009 — The triangular shell forcing is a bounded causal self-map

Claim ID: `L-23009`  
Title: The Volterra forcing in the fixed-ratio prime-renewal equation is a causal average of subratio shells and has cumulative `L2` norm at most four times the original shell norm  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: PR #234 `L-23402`; `L-23008`  
Scope: the triangular forcing only; the signed prime-convolution term remains open

## 1. Triangular forcing

For `0<c<1`, retain

\[
I_c(x)=M(x)-M(cx)
\]

and define

\[
J_c(x)=
\sum_{cx<n\le x}
\mu(n)\log{x\over n}.
\tag{L-23009.1}

PR #234 `L-23402` proves the exact Volterra form

\[
\boxed{
J_c(x)=
\int_{cx}^{x}{M(u)-M(cx)\over u}\,du.}
\tag{L-23009.2}

Put

\[
Q_c(t)=e^{-t/2}I_c(e^t),
\qquad
R_c(t)=e^{-t/2}J_c(e^t).
\tag{L-23009.3}

## 2. Exact subratio decomposition

In (L-23009.2), write `u=rx`, with `c<=r<=1`.  Then

\[
M(rx)-M(cx)
=I_{c/r}(rx).
\]

If `x=e^t`, the square-root normalization gives

\[
e^{-t/2}I_{c/r}(re^t)
=r^{1/2}Q_{c/r}(t+\log r).
\]

Consequently

\[
\boxed{
R_c(t)=
\int_c^1 r^{-1/2}
Q_{c/r}(t+\log r)\,dr.}
\tag{L-23009.4}

Every argument on the right is causal: `t+log r<=t`.

## 3. Reduction to the original ratio

Apply `L-23008` to transfer the ratio `c/r` back to `c`.  Its causal filter has
total variation at most

\[
{1+\sqrt{c/r}\over1-\sqrt c}.
\tag{L-23009.5}

Let

\[
\mathcal A_c(X)=
\int_{-\infty}^{X}|Q_c(t)|^2dt,
\qquad
\mathcal R_c(X)=
\int_{-\infty}^{X}|R_c(t)|^2dt.
\tag{L-23009.6}

Minkowski's inequality, causality, and (L-23009.5) give

\[
\begin{aligned}
\mathcal R_c(X)^{1/2}
&\le
{1\over1-\sqrt c}
\int_c^1
\left(r^{-1/2}+\sqrt c\,r^{-1}\right)dr
\,\mathcal A_c(X)^{1/2}\\
&=
\left[
2+{\sqrt c\log(1/c)\over1-\sqrt c}
\right]
\mathcal A_c(X)^{1/2}.
\end{aligned}
\tag{L-23009.7}

Since

\[
\sqrt c\log(1/c)
\le2(1-\sqrt c),
\]

one obtains the uniform bound

\[
\boxed{
\mathcal R_c(X)^{1/2}
\le4\mathcal A_c(X)^{1/2}.}
\tag{L-23009.8}

Equivalently,

\[
\boxed{
\mathcal R_c(X)
\le16\mathcal A_c(X).}
\tag{L-23009.9}

No asymptotic estimate for `M` enters this inequality.

## 4. Damped version

The same calculation after multiplication by `e^(-sigma t)`, `sigma>=0`, gives
an explicit bounded causal operator on every damped `L2` space.  One may use the
ratio-transfer constant from `L-23008.15` inside (L-23009.4); for every fixed
`sigma` and `c` the resulting norm is finite.

Thus `R_c` and `Q_c` have the same possible rightmost exponential obstruction.
The triangular integration does not create a new arithmetic gate.

## 5. Consequence for the prime-renewal equation

The exact shell renewal equation is

\[
\log x\,I_c(x)
+
\sum_{a\le x}\Lambda(a)I_c(x/a)
=J_c(x).
\tag{L-23009.10}

After square-root normalization, its right-hand side is controlled by
(L-23009.8).  Therefore any completion should focus on the signed reflected
prime-convolution channel.  Charging `J_c` as an unrelated endpoint error is
unnecessary and loses structure.

In particular, the dyadic Euler-aligned proposal may treat the triangular
forcing as a bounded source term in the same shell-energy space.  The sole
remaining analytic issue is a one-sided or reflected estimate for

\[
\sum_a{\Lambda_2(a)\over\sqrt a}
Q_{1/2}(t-\log a)
\]

with every common-cell cross term retained.

## 6. Proof boundary

Closed exactly:

- the subratio-shell representation of the triangular forcing;
- its causal transfer to one fixed shell ratio;
- the uniform cumulative-energy bound by four in norm.

Open:

- a contraction for the signed prime-renewal term;
- the dyadic shell energy theorem;
- RH.
