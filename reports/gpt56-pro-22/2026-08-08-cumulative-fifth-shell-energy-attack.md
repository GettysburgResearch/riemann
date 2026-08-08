# Cumulative fifth-shell energy attack

Date: 2026-08-08  
Agent: `gpt56-pro-22`  
Branch: `agent/gpt56-pro-22/237-greedy-carry-parity`  
Status: **new exact reductions and one finite directed certificate; RH remains unproved**

## Executive result

The Greedy Slack/DCRS route now has a second, direct arithmetic coordinate. Instead of trying to prove pointwise positivity of the exact carry coefficient profile whose proposed conditional-Hankel kernel was refuted, pass once to the cumulative Green state

\[
s_{X,m}=\sum_{n=m}^{X}\frac{c_X(n)}{n+1}.
\]

Its continuum profile is

\[
\mathfrak S(y)=
\sum_{n\le y}\frac{\mu(n)}{\sqrt n}
[4\sqrt{y/n}-4-\log(y/n)].
\]

The fifth-aligned shell

\[
C(y)=\mathfrak S(y)-5^{-1/2}\mathfrak S(y/5)
\]

has three new features:

1. two exact positive forcing primitives;
2. a proof-grade positive annulus through `y=100`;
3. an exact first-zero energy barrier of order `(log y)^2`.

The remaining theorem is one source-specific upper bound for the corresponding finite logarithmic Dirichlet energy in the reviewed two-frequency reflected orientation.

## New exact identities

### Cumulative kernel and transform

For

\[
p(y)=4\sqrt y-4-\log y,
\]

\[
C(y)=
\sum_{n\le y}
\frac{b_5(n)}{\sqrt n}p(y/n),
\qquad
b_5(n)=\mu(n)-\mathbf1_{5\mid n}\mu(n/5).
\]

Its Mellin transform is

\[
\int_1^\infty C(y)y^{-z-1}dy
=
\frac{(1-5^{-(z+1/2)})(z+1/2)}
 {z^2(z-1/2)\zeta(z+1/2)}.
\]

No hypothetical off-line zero is canceled.

### Two positive forcing equations

The ordinary convolution `1*b_5=delta_1-delta_5` gives

\[
\sum_{m\le y}m^{-1/2}C(y/m)
=p(y)-5^{-1/2}p(y/5)>0.
\]

The base-five digital sequence

\[
c_5(n)=1-4v_5(n),
\qquad
\sum_{n\le N}c_5(n)=s_5(N)\ge0,
\]

satisfies `c_5*b_5=delta_1-5delta_5`, and therefore

\[
\sum_{m\le y}\frac{c_5(m)}{\sqrt m}C(y/m)
=p(y)-\sqrt5p(y/5)>0.
\]

These are exact source-bound identities, not generic kernel inequalities.

## Exact finite annulus

On `N<=y<N+1`, put

\[
A_N=\sum_{n\le N}\frac{b_5(n)}n,
\quad
B_N=\sum_{n\le N}\frac{b_5(n)}{\sqrt n},
\quad
C_N=\sum_{n\le N}\frac{b_5(n)\log n}{\sqrt n}.
\]

Then

\[
C(y)=4A_N\sqrt y-(4+\log y)B_N+C_N
\]

and

\[
C'(y)=\frac{2A_N\sqrt y-B_N}{y}.
\]

The derivative numerator has at most one zero per cell. `X-23704` uses outward rational brackets for every square root and logarithm and certifies

```text
C(y)>=0 for 1<=y<=100,
C(y)>0 for 1<y<=100,
minimum endpoint lower bound >9637/10000,
unresolved derivative cells 0.
```

This is a finite theorem only.

## Digital Abel identity and first-zero barrier

For

\[
Y_m(y)=m^{-1/2}C(y/m),
\qquad M=\lfloor y\rfloor,
\]

finite Abel summation gives

\[
\begin{aligned}
C(y)={}&R_5(y)+Y_2(y)-s_5(M)Y_M(y)\\
&-\sum_{m=2}^{M-1}s_5(m)[Y_m(y)-Y_{m+1}(y)].
\end{aligned}
\]

The endpoint term is explicit and tiny:

\[
0\le s_5(M)Y_M(y)\le s_5(M)M^{-3/2}.
\]

Put

\[
\mathcal E_5(y)=
\sum_{m=2}^{M-1}m^2|Y_m-Y_{m+1}|^2
\]

and

\[
\kappa_5^2=\sum_{m=2}^{\infty}s_5(m)^2/m^2<\infty.
\]

At a first zero beyond the certified annulus,

\[
\mathcal E_5(y_0)
\ge
\frac{[R_5(y_0)+Y_2(y_0)-s_5(M)Y_M(y_0)]_+^2}
 {\kappa_5^2}
\gg(\log y_0)^2.
\]

Thus any sign failure has a compulsory physical energy cost.

## Full conditional proposal

The sole proposed upper estimate is

\[
\mathcal E_5(y)=o((\log y)^2).
\]

It must be proved for the exact aligned source by mapping the trace-zero digital boundary vector into the two-frequency physical reflected block of PR #241. The global endpoint-projected Green norm is forbidden because its logarithmic mode is the prime-ramp discrepancy itself.

The implication chain is then:

```text
source-specific reflected energy upper bound
-> no first zero of C
-> C(y)>=0 globally
-> Landau continuation of its explicit inverse-zeta transform
-> no zeta zero with real part >1/2
-> functional-equation symmetry
-> RH.
```

## Review order

1. `L-23709-cumulative-green-profile-and-fifth-aligned-forcing.md`
2. `L-23710-fifth-aligned-shell-cell-calculus.md`
3. `X-23704-fifth-aligned-shell/`
4. `L-23711-digital-abel-first-crossing-energy-barrier.md`
5. `T-23704-cumulative-fifth-shell-reflected-energy-rh-proposal.md`
6. PR #241 two-frequency reflected block
7. PR #248 endpoint-projected Green algebra and scalar-mode firewall
8. `L-23707/L-23708/T-23703`
9. `L-23705/L-23706/T-23702`
10. square-screw/Landau consumers on PRs #202/#218

## Exact status

```text
cumulative profile and transform                proposed exact
fifth-aligned forcing identities                proposed exact
finite annulus                                  exact directed certificate
first-zero energy barrier                       proposed exact
source-specific reflected energy upper bound    open
Riemann Hypothesis                              unproved
```

There is no unconditional RH claim in this report.
