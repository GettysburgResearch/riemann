# T-14303 — Dilation profiles identify the growing low-block obstruction with Weil positivity

Claim ID: `T-14303`  
Title: The noncompact scaled profiles of the localized Weil operators carry the full global Weil quadratic form exactly  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: consistency and unitary scaling of the localized Weil forms; Weil's positivity criterion; `T-14302`, `L-14315`  
Scope: exact interpretation of the final growing-low-matrix blocker  
Related counterexample candidates: none

## Setup

Let `D_c` be a smooth compactly supported core for the global Weil form `Q` in
logarithmic coordinates. Let `Q_a` be its restriction to functions supported
in `(-a,a)`. Thus for `f in D_c` supported in `(-A,A)`,

\[
 Q_a(f,f)=Q(f,f)
 \qquad(a\ge A).
 \tag{T-14303.1}
\]

Let

\[
 U_a f(x)=\sqrt a\,f(ax),
 \qquad -1<x<1,
 \tag{T-14303.2}
\]

and let `q_a` be the unitarily scaled form on `L^2(-1,1)`:

\[
 q_a(U_af,U_ag)=Q_a(f,g).
 \tag{T-14303.3}
\]

## Exact profile identity

For every `f in D_c` and every sufficiently large `a`,

\[
 \boxed{
 q_a(U_af,U_af)=Q(f,f),
 \qquad
 \|U_af\|_2=\|f\|_2.}
 \tag{T-14303.4}
\]

Moreover, if `a->infinity`,

\[
 U_af\rightharpoonup0
 \quad\text{in }L^2(-1,1).
 \tag{T-14303.5}
\]

Thus the full global Weil form appears exactly as the energy of weakly escaping
profiles of the scaled localized operators.

## Equivalence theorem

The following statements are equivalent.

1. The Riemann hypothesis is true.
2. The global Weil form is nonnegative on `D_c`:
   \[
     Q(f,f)\ge0\qquad(f\in D_c).
     \tag{T-14303.6}
   \]
3. Every compact-support dilation profile is nonnegative:
   \[
     \liminf_{a\to\infty}q_a(U_af,U_af)\ge0
     \qquad(f\in D_c).
     \tag{T-14303.7}
   \]
4. There is no `f in D_c`, `c>0`, and cofinal sequence `a_j` for which
   \[
     U_{a_j}f\rightharpoonup0,
     \qquad
     q_{a_j}(U_{a_j}f,U_{a_j}f)
     \le-c\|f\|_2^2.
     \tag{T-14303.8}
   \]

### Proof

Weil's criterion gives the equivalence of 1 and 2. Identity (T-14303.4) makes
2 and 3 identical. `L-14315` gives the weak convergence, so the negation of 3
is exactly 4. QED.

## Consequence for the corrected low matrix

Suppose each scaled form has an exact block decomposition

\[
 A_a=\begin{pmatrix}B_a&R_a^*\\R_a&C_a\end{pmatrix}
\]

with complete complement coercivity, and put

\[
 K_a=B_a-h_a^{-1}R_a^*M_a^{-1}R_a.
 \tag{T-14303.9}
\]

If a cofinal proof establishes

\[
 \lambda_{\min}(K_a)\ge-o(1),
 \qquad
 \gamma_a\ge-o(1),
 \qquad
 \delta_a^{assembly}=o(1),
 \tag{T-14303.10}
\]

then `T-14302` and the equivalence above prove RH.

Conversely, if RH is false, one compactly supported negative `f` produces the
weakly escaping sequence in (T-14303.8). Once the complement is nonnegative,
`L-14314` shows that the corrected low matrices retain a negative spectral
depth bounded away from zero. Therefore one of the following must fail:

- common-frame negative-part tightness;
- whole-packet radical tail-norm decay;
- the declared complete complement/assembly gates.

The final low-block theorem is therefore not a routine estimate left after the
finite calculations. It is an operator-theoretic reformulation of the full
Weil positivity problem.

## Concentration-compactness interpretation

The scaled sequence has two qualitatively different behaviors.

1. **Compact modes:** vectors remain tight in a fixed scaled frame. These are
   accessible to fixed-mode and finite-compression calculations.
2. **Concentrating profiles:** vectors of the form `U_af` become weakly null and
   move to frequency scale `a`. Their exact limiting energy is `Q(f,f)`.

An off-critical zero is detected in the second channel by some negative Weil
test. Any successful positive proof must rule out that channel by a genuinely
global analytic argument; fixed-row convergence addresses only the first.

## Proof-producing implication

A finite checker can verify any proposed common-frame or radical-frame bound,
but a completed proof must supply a symbolic cofinal theorem. Suitable final
interfaces are:

\[
 \sup_{\substack{x\in\operatorname{Ran}(K_a)_-\\\|x\|=1}}
 \|(I-P_m)x\|
 \longrightarrow0
 \quad\text{uniformly as }m\to\infty,
 \tag{T-14303.11}
\]

or the stronger exact-radical synthesis estimate

\[
 \|V_a\|_{coeff\to X}^2/h_a\longrightarrow0.
 \tag{T-14303.12}
\]

By `L-14314` or `L-14313`, respectively, either one closes the corrected low
matrix. By the present theorem, proving such an interface for the actual
complete packets is already an RH-resolving result.

## Gap audit

- The profile identity and equivalence are exact once the localized-form
  normalization is fixed.
- This theorem does not prove (T-14303.11) or (T-14303.12).
- A finite sequence of successful low-block computations cannot establish the
  cofinal statement.
- The result explains why no argument based solely on fixed rows, matching
  digits, or growing finite rank can complete the proof.
- No proof of RH is claimed here.
