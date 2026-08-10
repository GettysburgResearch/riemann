# L-32404 — Critical Euler–Blaschke factors with positive Dirichlet inverse

Claim ID: `L-32404`  
Title: Every dyadic prime-power radix carries an explicit local Euler Blaschke factor which kills the zeta main pole, is all-pass on the critical line, strictly contractive to its right, and has positive inverse and generalized-prime coefficients  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/DIRICHLET LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: elementary Blaschke algebra and Euler products  
Scope: exact source/filter theorem; no RH conclusion or energy estimate

## 1. Definition

Fix an integer

\[
 Q=2^d,\qquad d\ge1.
\]

Put

\[
 \boxed{
 E_Q(s)={1-Q^{1-s}\over1-Q^{-s}}
 }
\tag{L-32404.1}
\]

and normalize

\[
 \boxed{
 \Phi_Q(s)=Q^{-1/2}E_Q(s).
 }
\tag{L-32404.2}
\]

Let

\[
 B_Q(s)={E_Q(s)\over\zeta(s)},
 \qquad
 A_Q(s)=B_Q(s)^{-1}
 =\zeta(s){1-Q^{-s}\over1-Q^{1-s}}.
\tag{L-32404.3}
\]

## 2. Exact critical-line all-pass identity

Write

\[
 w=Q^{-s}.
\]

On `Re(s)=1/2`,

\[
 |w|^2=Q^{-1}.
\]

Then

\[
\begin{aligned}
 |1-Qw|^2
 &=1+Q^2|w|^2-2Q\operatorname{Re}w\\
 &=Q+1-2Q\operatorname{Re}w\\
 &=Q|1-w|^2.
\end{aligned}
\]

Therefore

\[
 \boxed{
 |\Phi_Q(1/2+it)|=1
 \qquad(t\in\mathbb R).
 }
\tag{L-32404.4}
\]

If `Re(s)>1/2`, then `Q|w|^2<1` and

\[
\begin{aligned}
 Q|1-w|^2-|1-Qw|^2
 &=(Q-1)(1-Q|w|^2)>0.
\end{aligned}
\]

Hence

\[
 \boxed{
 |\Phi_Q(s)|<1
 \qquad(\operatorname{Re}s>1/2).
 }
\tag{L-32404.5}
\]

Thus `Phi_Q` is the elementary dyadic Euler analogue of a Blaschke factor for
the critical half-plane: neutral on the critical boundary and strictly smaller
inside the right half-plane.

## 3. Positive inverse coefficients

Set `x=Q^(-s)`. The local factor of `A_Q` is

\[
 {1-x\over1-Qx}
 =1+\sum_{r\ge1}(Q-1)Q^{r-1}x^r.
\tag{L-32404.6}
\]

Every coefficient is nonnegative. Convolution with the ordinary zeta
coefficients gives

\[
 \boxed{
 a_Q(n)=Q^{v_Q(n)}>0,
 }
\tag{L-32404.7}

where

\[
 v_Q(n)=\max\{r:Q^r\mid n\}.
\]

Indeed

\[
 1+\sum_{r=1}^{v_Q(n)}(Q-1)Q^{r-1}=Q^{v_Q(n)}.
\]

## 4. Nonnegative generalized-prime coefficients

The local logarithmic derivative of (L-32404.6) contributes only at the powers
`Q^r`:

\[
 \boxed{
 \Lambda_Q(n)
 =\Lambda(n)
  +(\log Q)\sum_{r\ge1}(Q^r-1)
    \mathbf1_{n=Q^r}
 \ge0.
 }
\tag{L-32404.8}
\]

Thus the complete modified Dirichlet system retains a nonnegative generalized
von Mangoldt sequence.

## 5. Exact source comb

The local factor on the inverse/source side expands as

\[
 {1-Qx\over1-x}
 =1-(Q-1)\sum_{r\ge1}x^r.
\tag{L-32404.9}
\]

Hence

\[
 \boxed{
 b_Q=\mu*e_Q,
 \quad
 e_Q(1)=1,
 \quad
 e_Q(Q^r)=-(Q-1)\ (r\ge1),
 }
\tag{L-32404.10}
\]

with all other local coefficients zero.

Since `1*b_Q=e_Q`, source convolution of the atomized carry row gives the finite
endpoint formula

\[
 \boxed{
 Y^{(Q)}_{X,m}(\theta)
 =J_{m/X}(\theta)
  -(Q-1)\sum_{r\ge1}J_{Q^r m/X}(\theta),
 }
\tag{L-32404.11}
\]

where the sum stops automatically once `Q^r m>X`.

At critical square-root normalization the absolute coefficients of the delayed
comb are summable:

\[
 \boxed{
 (Q-1)\sum_{r\ge1}Q^{-r/2}
 =\sqrt Q+1.
 }
\tag{L-32404.12}
\]

Thus the source comb itself is a fixed causal bounded filter in the physical
critical normalization, even though its inverse is deliberately noncontractive
off the critical line.

## 6. The main pole and artificial local poles disappear physically

Let

\[
 L_Q=-{A_Q'\over A_Q}
 =-{\zeta'\over\zeta}+{E_Q'\over E_Q}.
\tag{L-32404.13}
\]

The physical source-convolved logarithmic derivative is

\[
 \boxed{
 E_Q(s)L_Q(s)
 =-E_Q(s){\zeta'(s)\over\zeta(s)}+E_Q'(s).
 }
\tag{L-32404.14}
\]

The numerator `1-Q^(1-s)` has a simple zero at `s=1`, while
`-zeta'/zeta` has residue `+1` there. Equation (L-32404.14) is therefore
holomorphic at the main pole.

More generally the other zeros of `1-Q^(1-s)` lie on `Re(s)=1`. The apparent
local poles of `E_Q'/E_Q` cancel after multiplication by `E_Q`; the physical
combination (L-32404.14) is analytic there as long as zeta is nonzero. Classical
zero-freeness of zeta on `Re(s)=1` supplies that fact.

The denominator zeros `1-Q^(-s)=0` lie on `Re(s)=0`, outside the open critical
strip.

## 7. Every nontrivial zeta zero is retained

If `rho` is a nontrivial zeta zero, then

\[
 0<\operatorname{Re}\rho<1.
\]

Every zero of `1-Q^(1-s)` has real part one, and every zero of
`1-Q^(-s)` has real part zero. Hence

\[
 E_Q(\rho)\ne0.
\]

For multiplicity `m_rho`,

\[
 \boxed{
 \operatorname*{Res}_{s=\rho}
 [E_Q(s)L_Q(s)]
 =-m_\rho E_Q(\rho)\ne0.
 }
\tag{L-32404.15}
\]

Thus the filter removes the deterministic `s=1` pole without deleting any
nontrivial zeta-zero pole.

## 8. Why dyadic `Q` is preferred

The construction itself makes sense for every integer `Q>=2`. Restricting to
`Q=2^d` keeps the entire source on the 2-adic valuation tower and introduces no
nonprincipal residue-character sector. This is compatible with the radix
firewall identified on PR #323.

The two smallest useful choices have different geometry:

```text
Q=2:
    densest dyadic comb;

Q=4:
    first local correction occurs at powers 4^r,
    while the main pole is still removed and critical-line neutrality remains exact.
```

The `Q=4` system is therefore a natural candidate for a source-specific Selberg
reserve with fewer low-scale collisions.

## 9. Proof boundary

Closed exactly here, subject to review:

- critical-line all-pass identity;
- strict right-half-plane attenuation;
- positive inverse coefficients;
- nonnegative generalized-prime coefficients;
- explicit finite source comb;
- removal of the main pole and artificial local poles;
- retention of every nontrivial zeta-zero pole.

Open:

- an unconditional source-specific energy estimate;
- a reflected Selberg/carry reserve for the complete `Q=4` source;
- RH.