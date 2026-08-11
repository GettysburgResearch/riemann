# T-91006 — RH is one fixed safe-scale Lévy–Hardy Gram positivity theorem

Claim ID: `T-91006`  
Status: **PROPOSED COMPLETE EXACT RH-EQUIVALENT FIXED-SCALE CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91028`, `L-91029`, `L-91030`; Suzuki's screw criterion  
RH status: **unproved**

## 1. Statement

Fix **one arbitrary scale**

\[
 a_0>\frac12.
\]

Let

\[
 \mathfrak I=(\{+,-\}\times\mathbb R)\sqcup\{\star\}
\]

and let `F_(epsilon,x)` be the causal/anti-causal wavelets of
`L-91029.14` at scale `a_0`; let `F_star=b_(a_0)` be the bridge of
`L-91030.12`.

Define the Hermitian kernel

\[
 \boxed{
 \mathbb K_{a_0}(i,j)
 =\iint_{\mathbb R^2}
 G_\zeta(t,u)F_i(t)\overline{F_j(u)}dtdu,
 \qquad i,j\in\mathfrak I,
 }
 \tag{T-91006.1}

where

\[
 G_\zeta(t,u)
 =g_\zeta(t-u)-g_\zeta(t)-g_\zeta(-u)+g_\zeta(0).
\]

Then, subject to independent review of the form-core passage,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathbb K_{a_0}\succeq0
 \text{ on every finite subset of }\mathfrak I.
 }
 \tag{T-91006.2}

The quantifier over the scale has disappeared.  Any single fixed
`a_0>1/2` is complete.

## 2. RH gives a literal Lévy Gram

Under RH, the Nakamura--Suzuki Lévy measure is

\[
 \nu_\zeta
 =\sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_\gamma.
\]

For every mean-zero test `F_i`,

\[
 \mathbb K_{a_0}(i,j)
 =\int\widehat F_i(\lambda)
  \overline{\widehat F_j(\lambda)}d\nu_\zeta(\lambda).
 \tag{T-91006.3}

For the two Hardy families this is

\[
 \boxed{
 \mathbb K_{a_0}((\epsilon,x),(\delta,y))
 =\sum_\gamma m_\gamma
 \Psi_{a_0}^\epsilon(\gamma-x)
 \overline{\Psi_{a_0}^\delta(\gamma-y)}.
 }
 \tag{T-91006.4}

The bridge entries are obtained from the same Gram formula.  Therefore every
finite matrix is positive semidefinite.

## 3. Fixed-scale positivity gives the whole screw form

Assume the right side of (T-91006.2).  Positivity holds on the algebraic span
of the indexed tests.  `L-91030` proves that this span is dense in

\[
 \mathcal H_{\eta,0}
 =\left\{f\in L^2(e^{\eta|t|}dt):\int f=0\right\}
\]

for any

\[
 1<\eta<2a_0.
\]

The screw form is continuous in that norm.  It is therefore nonnegative on all
of `H_(eta,0)`, and in particular on every compactly supported smooth
mean-zero test.  Suzuki's theorem then gives RH.

No zero selection, terminal-pair argument, Gram inversion, growing support or
cofinal scale hierarchy is required in this final implication.

## 4. Relation to the resident Cauchy recurrence

For the causal diagonal,

\[
 \boxed{
 \mathbb K_{a_0}((+,x),(+,x))
 =a_0^4\mathcal R_x(a_0),
 }
 \tag{T-91006.5
}

where `R_x(a)` is the nonnegative three-square residual that would imply the
sixteenfold recurrence in `T-91005`.

Hence the previous scalar route observes only

\[
 \operatorname{diag}\mathbb K_{a_0}.
\]

The cross-carrier and causal/anti-causal blocks are not optional decoration:
they are precisely the polarization needed to recover the complete screw/Weil
form.

The radical replacement is therefore

```text
infinitely many scale-by-scale scalar gates
    -> one fixed-scale matrix kernel;

terminal-pair isolation
    -> Hardy-Wiener completeness;

moving prime cutoffs and asymptotics
    -> absolutely convergent Euler entries.
```

## 5. Prime-side form at the fixed safe scale

Every `F_i` is a finite one-sided exponential-polynomial combination with
rates among

\[
 a_0,\ 2a_0,\ 4a_0.
\]

The Guinand--Weil expression for an entry has the form

\[
 \boxed{
 \mathbb K_{a_0}(i,j)
 =\mathbb K_{\Gamma,\mathrm{pole}}(i,j)
 -2\Re\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}\,
 \mathcal W_{i,j}(\log n),
 }
 \tag{T-91006.6}

where `W_(i,j)` is explicit and

\[
 \mathcal W_{i,j}(t)
 =O_{i,j}(\operatorname{poly}(t)e^{-a_0t}).
\]

Since `a_0>1/2`, the prime series converges absolutely.  Each entry may also be
written as a finite algebraic combination of `-zeta'/zeta` and its derivatives
at fixed points in `Re(s)>1`, plus explicit rational/polygamma terms.

Thus the remaining theorem is a fixed, source-explicit matrix factorization:

\[
 \boxed{
 \mathbb K_{\Gamma,\mathrm{pole}}
 \succeq
 \mathbb K_{\mathrm{prime}}
 }
 \tag{T-91006.7}

on the complete two-Hardy-channel carrier space.

## 6. The Fock route to the remaining inequality

`L-91028` gives an explicit bosonic product system for the positive Jordan
source.  Its boundary correlation channel is compound Poisson and its
Stinespring environment is no longer abstract.  `L-91029/L-91030` give an
explicit causal/anti-causal Hardy form core for the completed screw output.

A conclusion-producing proof can now be formulated as one conservative
colligation problem:

> Construct a scale-fixed isometry from the completed gamma/pole input plus the
> prime-power Poisson Fock environment onto the two Hardy output channels so
> that its transfer kernel is `mathbb K_(a_0)`.

If such an isometry is constructed, (T-91006.7) is automatic and RH follows.
Conversely, positivity of `mathbb K_(a_0)` provides a Kolmogorov/Stinespring
factorization, so this colligation target is exactly sharp.

## 7. Countable reduction and finite countercertificates

Continuity in the carriers implies that rational `x,y` suffice.  Every finite
matrix entry is an absolutely convergent Euler expression and can be enclosed
outward after a finite prime-power cutoff.

Therefore

\[
 \boxed{
 \neg\mathrm{RH}
 \Longrightarrow
 \begin{array}{c}
 \text{one finite set of rational carriers and orientations},\\
 \text{one finite prime-power cutoff},\\
 \text{one strictly negative directed eigenvalue interval}.
 \end{array}
 }
 \tag{T-91006.8
}

No negative Riemann-data matrix is claimed to have been found.

## 8. Exact boundary

Closed, subject to independent review:

```text
one arbitrary fixed safe scale a_0>1/2 is complete;
RH -> explicit Levy Gram;
fixed-scale Gram PSD -> full Suzuki screw positivity -> RH;
resident Cauchy residual = one diagonal;
all entries absolutely Eulerian at fixed safe points;
false RH has a finite rational-carrier finite-prime matrix witness;
remaining theorem = one conservative Poisson-Fock/Hardy colligation.
```

Open:

```text
construction of that conservative completed colligation;
unconditional fixed-scale cross-Gram PSD;
Riemann Hypothesis.
```
