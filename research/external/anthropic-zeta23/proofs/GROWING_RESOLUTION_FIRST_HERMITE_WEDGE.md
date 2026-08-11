# Growing-resolution first-Hermite positivity up to the universal `4 log log` frontier

**Status:** `PROPOSED COMPLETE UNCONDITIONAL GROWING-WEDGE THEOREM — INDEPENDENT REVIEW REQUIRED`  
**RH status:** **unproved**  
**Depends on:** PR #379 first-Hermite criterion; PR #384 macroscopic positivity; the standard Guinand--Weil/Stirling normalisation used in Anthropic Zeta23  

## 1. Main theorem

Let

\[
 \mathcal M(q,x)
 =\sum_\rho m_\rho(\gamma_\rho-x)^2
 e^{-q(\gamma_\rho-x)^2}.
 \tag{DW.1}
\]

For every fixed `epsilon>0`, there is an effective `X_epsilon` such that

\[
 \boxed{
 \mathcal M(q,x)>0
 }
 \tag{DW.2}
\]

whenever

\[
 |x|\ge X_\epsilon,
 \qquad
 0<q\le(4-\epsilon)\log\log(2+|x|).
 \tag{DW.3}
\]

Thus every sequence of negative witnesses with `|x|->infinity` must satisfy

\[
 \boxed{
 \liminf {q\over\log\log|x|}\ge4.
 }
 \tag{DW.4}
\]

The constant four is the reciprocal of the largest possible squared off-line depth `(1/2)^2`. It also arises as the exact saddle constant in the phase-blind all-prime envelope.

This theorem does not prove positivity at or above the boundary `(4+o(1)) log log |x|`.

## 2. Uniform gamma reserve in the growing regime

Use the PR #379 decomposition

\[
 \mathcal M(q,x)=P(q,x)+G(q,x)-\mathcal P(q,x),
 \tag{DW.5}
\]

and the effective bound

\[
 \mu(\tau)\ge c_0\log(2+|\tau|)-C_0.
 \tag{DW.6}
\]

Put `u=tau-x`. If

\[
 |x|\ge2q^{-1/2},
 \tag{DW.7}
\]

then on `|u|<=q^-1/2`,

\[
 |x+u|\ge|x|/2.
\]

Hence

\[
 \begin{aligned}
 \int_\mathbb R u^2e^{-qu^2}
 \log(2+|x+u|)du
 &\ge c_1q^{-3/2}\log(2+|x|),
 \end{aligned}
 \tag{DW.8}
\]

where

\[
 c_1=\int_{-1}^{1}v^2e^{-v^2}dv>0.
\]

The negative constant in `(DW.6)` costs only

\[
 C_0\int_\mathbb R u^2e^{-qu^2}du
 =O(q^{-3/2}).
\]

Therefore

\[
 \boxed{
 G(q,x)
 \ge c_2q^{-3/2}\log(2+|x|)-C_2q^{-3/2}
 }
 \tag{DW.9}
\]

uniformly whenever `(DW.7)` holds.

## 3. Global all-prime envelope at growing q

From the exact first-Hermite prime formula,

\[
 \begin{aligned}
 |\mathcal P(q,x)|
 \le{1\over2\sqrt\pi q^{3/2}}
 \sum_{n\ge2}{\log n\over\sqrt n}
 \left(1+{(\log n)^2\over2q}\right)
 e^{-(\log n)^2/(4q)}.
 \end{aligned}
 \tag{DW.10}
\]

This bound is independent of `x`.

For `m>=0`, group integers with

\[
 e^m\le n<e^{m+1}.
\]

There are at most `e^(m+1)` such integers, while

\[
 n^{-1/2}\le e^{-m/2},
 \quad
 \log n\le m+1,
 \quad
 e^{-(\log n)^2/(4q)}\le e^{-m^2/(4q)}.
\]

Thus the unnormalised sum in `(DW.10)` is at most a constant times

\[
 \sum_{m\ge0}
 (m+1)\left(1+{(m+1)^2\over q}\right)
 e^{m/2-m^2/(4q)}.
 \tag{DW.11}
\]

The exponent has the exact completed-square form

\[
 \boxed{
 {m\over2}-{m^2\over4q}
 ={q\over4}-{(m-q)^2\over4q}.
 }
 \tag{DW.12}
\]

Gaussian moment bounds around `m=q` give, for `q>=1`,

\[
 \sum_{m\ge0}
 (m+1)\left(1+{(m+1)^2\over q}\right)
 e^{-(m-q)^2/(4q)}
 \ll q^{5/2}.
 \tag{DW.13}
\]

After the prefactor in `(DW.10)`,

\[
 \boxed{
 |\mathcal P(q,x)|
 \ll q e^{q/4}
 \qquad(q\ge1),
 }
 \tag{DW.14}
\]

uniformly in `x`.

This is deliberately phase blind. The oscillation `cos(x log n)` is not used.

## 4. Pole term

The exact pole contribution obeys

\[
 \boxed{
 |P(q,x)|
 \le2e^{q/4}(x^2+1/4)e^{-qx^2}.
 }
 \tag{DW.15}
\]

For `q` bounded below and `|x|->infinity`, this is smaller than every inverse power of `|x|`, uniformly throughout the wedge `(DW.3)`.

## 5. Proof of the growing wedge

Put

\[
 L=\log(2+|x|),
 \qquad
 \ell=\log L.
\]

For `q>=1`, combine `(DW.9)`, `(DW.14)`, and `(DW.15)`:

\[
 \mathcal M(q,x)
 \ge q^{-3/2}(c_2L-C_2)
 -C_3q e^{q/4}
 -|P(q,x)|.
 \tag{DW.16}
\]

After multiplying by `q^(3/2)`, the adverse prime term is

\[
 C_3q^{5/2}e^{q/4}.
 \tag{DW.17}
\]

If

\[
 q\le(4-\epsilon)\ell,
\]

then

\[
 \begin{aligned}
 {q^{5/2}e^{q/4}\over L}
 &\le C_\epsilon\ell^{5/2}e^{-\epsilon\ell/4}
 \longrightarrow0.
 \end{aligned}
 \tag{DW.18}
\]

The pole term is also `o(q^(-3/2)L)`. Thus `(DW.16)` is positive uniformly in the stated wedge for large `|x|`.

The compact range of `q` below one is covered uniformly by PR #384: sufficiently small `q` is positive for every centre, and the remaining compact `q` interval has uniform exterior positivity by the same gamma/prime estimates. This proves `(DW.2)`--`(DW.3)`.

## 6. Resolution lower bound for a hypothetical pair

Let a terminal pair at ordinate `t_0` and depth `y_0` produce a negative first-Hermite witness. PR #379 gives the target scale

\[
 -2m_0y_0^2e^{qy_0^2}.
 \tag{DW.19}
\]

The gamma background at height `t_0` has scale

\[
 q^{-3/2}\log|t_0|.
 \tag{DW.20}
\]

Balancing exponents suggests the depth-sensitive resolution

\[
 q\gtrsim {\log\log|t_0|\over y_0^2}.
 \tag{DW.21}
\]

The rigorous universal theorem `(DW.4)` is the consequence of `y_0^2<1/4`. For shallower pairs the required resolution is correspondingly larger.

Equation `(DW.21)` is recorded as scale guidance; the proved statement is the wedge `(DW.3)` and its corollary `(DW.4)`.

## 7. Prime scale at the frontier

The phase-blind prime envelope in `(DW.10)` is concentrated near the saddle

\[
 \log n\asymp q.
 \tag{DW.22}
\]

At the universal boundary

\[
 q\asymp4\log\log|x|,
\]

this corresponds to

\[
 \boxed{
 n\asymp e^q\asymp(\log|x|)^4.
 }
 \tag{DW.23}
\]

Thus the remaining diagonal theorem can be stated arithmetically:

> exploit the oscillation and source structure of the first-Hermite prime sum at prime-power scale about `(log |x|)^4` strongly enough to beat its absolute envelope.

This is much more specific than an unrestricted all-prime positivity problem.

## 8. The constant-four firewall

If instead

\[
 q=(4+\epsilon)\ell,
\]

then the phase-blind ratio is

\[
 {q^{5/2}e^{q/4}\over L}
 \asymp\ell^{5/2}e^{\epsilon\ell/4},
 \tag{DW.24}
\]

which grows. Therefore the argument cannot cross the constant four without using the oscillatory factor

\[
 \cos(x\log n)
\]

or some equivalent signed arithmetic structure.

This is a method firewall, not a counterexample to positivity beyond the wedge.

## 9. Relation to Claude and the repository

Claude's theorem uses first and second traces at fixed normalized support and explicitly cannot distinguish a positive proportion from all zeros. The present route is pair-sensitive rather than trace-averaged, but the same fixed-resolution wall reappears in pointwise form. The new theorem pushes beyond fixed resolution to a growing window and identifies the first unresolved scale.

Repository interfaces:

```text
PR #379: exact first-Hermite RH criterion;
PR #384: broad/fixed-resolution positivity;
this PR: q <= (4-epsilon) log log |x| positivity;
PR #373: all-order Gaussian Fredholm criterion;
PR #343: Brownian cofinal stability, which would need control in this same diagonal scale.
```

## 10. Verification and exact boundary

The finite replay checks the completed-square saddle, the `q exp(q/4)` prime-envelope scale, decay throughout the subcritical wedge, growth above the constant-four phase-blind boundary, and the depth-sensitive resolution law.

Proposed complete, pending review:

```text
all-prime envelope O(q exp(q/4))
growing gamma reserve q^-3/2 log |x|
unconditional positivity for q <= (4-epsilon) log log |x|
necessary q/log log |x| >= 4 for negative witnesses
prime saddle n about (log |x|)^4 at the frontier
constant-four phase-blind firewall
```

Open:

```text
signed prime cancellation at/above the constant-four boundary
diagonal first-Hermite positivity
corrected-kernel floor
Riemann Hypothesis
```
