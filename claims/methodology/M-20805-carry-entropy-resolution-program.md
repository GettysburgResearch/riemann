# M-20805 — Carry-entropy resolution programme

Methodology ID: `M-20805`  
Title: Prove one finite triangular positivity theorem, then close RH through an exact binomial carry factorization  
Status: **FULL RESOLUTION PROGRAMME — CARRY SATURATION LEMMA OPEN**  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: `T-20805`; `L-20815`; `L-20816`; `R-20805`; `X-20809`

## 1. The one remaining theorem

For every integer `X>=2`, emit the unique coefficients

\[
 c_X(n)={n+1\over n-1}
 \left[
  {\log(X/n)\over\sqrt n}
  -\sum_{m=n+1}^Xc_X(m)\beta_{mn}
 \right]
 \tag{M-20805.1}
\]

in descending order. The complete programme is to prove

\[
 \boxed{c_X(n)\ge0\quad(2\le n\le X).}
 \tag{M-20805.2}
\]

Everything else in the proposed RH proof is already reduced to explicit finite
identities and elementary estimates.

## 2. Recommended proof attacks on the positivity hinge

### 2.1 Direct residual-ratio induction

Before emitting `c_X(n)`, define the residual

\[
 \rho_n(q)=w_X(q)-\sum_{m=n+1}^Xc_X(m)\beta_{mq}
 \qquad(q\le n).
 \tag{M-20805.3}
\]

Then

\[
 c_X(n)={\rho_n(n)\over\beta_{nn}}.
\]

It is enough to prove the stronger invariant

\[
 \boxed{
 {\rho_n(q)\over\beta_{nq}}
 \ge {\rho_n(n)\over\beta_{nn}}
 \quad(q<n,\ \beta_{nq}>0),}
 \tag{M-20805.4}
\]

with `rho_n(q)>=0`. This says the diagonal row is always the first saturated
constraint. It was observed in every direct backward run through `X=10000`.

A successful proof should exploit the quotient-cell formula

\[
 \beta_{nq}
 ={a((a+1)q-n-1)\over n+1},
 \qquad a=\lfloor n/q\rfloor,
 \tag{M-20805.5}
\]

rather than treating the matrix as generic.

### 2.2 Positive formula for the adjoint smoothing

Use `R-20805`:

\[
 u_m={1\over\sqrt m}
 \sum_{k\le X/m}{\mu(k)\over\sqrt k}\log{X/m\over k},
 \tag{M-20805.6}
\]

\[
 C_j={j u_j+\sum_{m>j}u_m\over j(j-1)},
 \qquad
 c_X(j)=(j+1)(C_j-C_{j+1}).
 \tag{M-20805.7}
\]

The task is not to make `u_m` positive; it is visibly signed. The correct target
is a monotonicity theorem for the smoothed quantities `C_j`.

A useful finite formulation is

\[
 \boxed{
 {j u_j+\sum_{m>j}u_m\over j(j-1)}
 \ge
 {(j+1)u_{j+1}+\sum_{m>j+1}u_m\over j(j+1)}.}
 \tag{M-20805.8}
\]

Every term is explicit.

### 2.3 Total-positivity / variation-diminishing route

The continuum kernel has Mellin transform

\[
 {s-1\over s(s+1)}\zeta(s).
\]

A direct total-positivity assertion must therefore be stated carefully: a claim
strong enough to make the inverse variation diminishing may already exclude
off-line zeros. The intended theorem is only positivity on the one logarithmic
Riesz target, not positivity of the inverse on an arbitrary cone.

A reviewer should reject an argument which silently replaces this one-target
statement by generic total positivity.

### 2.4 Finite sum-of-squares certificate

Search for an identity of the form

\[
 c_X(j)
 =\sum_{r}\alpha_{X,j,r}\,
  \left(\sqrt{r+1}-\sqrt r\right)^2
 +\sum_s\gamma_{X,j,s}\log\left(1+{1\over s}\right),
 \tag{M-20805.9}
\]

with rational nonnegative coefficients. The recurrence uses only logarithms of
rational ratios and inverse square roots, so a telescoping positive basis is
plausible. Such an identity would give the cleanest independent proof object.

## 3. Required adversarial tests

Any proposed proof of (M-20805.2) must survive:

1. replacement of `log(X/q)` by an arbitrary decreasing target — positivity is
   not generic;
2. deletion of the factor `q^-1/2` — the critical scaling is load bearing;
3. perturbation of the diagonal `beta_(nn)`;
4. composite `q`, even though only prime powers survive after contraction;
5. the signed intermediate Möbius values of `R-20805`;
6. integer-boundary cases `n mod q=q-1`, where `beta_(nq)=0`;
7. a proof at symbolic `X`, not extrapolation from a finite scan.

## 4. Once positivity is proved

No additional research conjecture is required. The exact chain is:

```text
CS
-> R(X)=sum c_X(n) G_n
-> entropy lower bound for G_n
-> elementary carry dual gives 4 sqrt(X)-O(log^2 X)
-> exact screw upper envelope O(log^2 X)
-> L-20814
-> RH.
```

The reviewer may verify each arrow independently from `L-20815/L-20816`.

## 5. Production protocol

A proof-producing implementation should emit, for symbolic or arbitrary finite
`X`:

```text
beta matrix formula
backward residuals rho_n(q)
coefficients c_X(n)
positivity decomposition or induction invariant
saturation residuals
factorial G_n producer
prime-power ramp producer
dual-row and budget ledgers
final screw upper interval
```

The prime and factorial contractions must be retained as independent replays.

## 6. Honest stop rule

If a negative `c_X(n)` is found with a directed interval, the Carry Saturation
Lemma is rejected and `T-20805` is not a proof. The exact carry identities remain
valid and the counterexample should be committed.

If positivity is proved only for `X<=X_0`, that is a finite result and does not
advance the global quantifier.

The branch may be promoted to a proof claim only after a symbolic all-`X`
argument for (M-20805.2) and an independent audit of `L-20814`.