# L-24503 — Discrete carry-resolvent stability

Claim ID: `L-24503`  
Title: A boundary-stable positive discretization of the exact carry resolvent gives the sharp aggregate carry mass with only polylogarithmic blocker debt  
Status: **PROPOSED CLOSING THEOREM / RH-BEARING HINGE — NOT PROVED HERE**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-24501`, `L-24502`; square-screw transfer on PR #202; comparison with the Digital Blocker Theorem on PR #244  
Scope: one scalar cofinal theorem; no packet, face-count, or generic-operator hypothesis

## 1. Exact finite objects

Let `d_X` be the deterministic greedy minorant of `L-24502`, and put

\[
 M_X=\sum_{n=2}^{X}n\,d_X(n),
 \qquad
 L_X=\sum_{n=2}^{X}d_X(n)[\log(n+1)+3].
 \tag{L-24503.1}
\]

Define the complete blocker debt

\[
\boxed{
 \mathfrak D_X
 =8\sqrt X-M_X+L_X.}
 \tag{L-24503.2}
\]

Every symbol in (L-24503.2) is finite and algorithmic. There is no omitted
prime, zero, tail, or limiting packet in its definition.

## 2. Stability theorem

The proposed theorem is:

> **Discrete Carry-Resolvent Stability (DCRS).** There exist absolute constants
> `A,C` such that, for every integer `X>=2`,
> \[
> \boxed{
>  \mathfrak D_X\le C\log^A(2X).}
> \tag{L-24503.3}
> \]

Equivalently, it is enough to prove the two estimates

\[
\boxed{
 M_X\ge8\sqrt X-C\log^A(2X),}
 \tag{L-24503.4}
\]

and

\[
\boxed{
 L_X\le C\log^A(2X).}
 \tag{L-24503.5}
\]

This is the same aggregate conclusion sought by PR #244's Digital Blocker
Theorem, but `L-24501` now supplies its canonical continuum resolvent, exact
constant eight, and shifted-zero firewall.

## 3. Proposed proof decomposition

A proof of DCRS must emit three independent ledgers.

### 3.1 Continuum ledger

Let `g` be the exact state of (L-24501.14). Construct a nonnegative, finite-horizon
profile `g_X^+` on `[0,log X]` such that

\[
 (k*g_X^+)(u)\le u
 \tag{L-24503.6}
\]

at every carry grid point `u=log(X/q)`, and

\[
\boxed{
 \sqrt X\int_0^{\log X}e^{-u/2}g_X^+(u)du
 \ge8\sqrt X-C\log^A(2X).}
 \tag{L-24503.7}
\]

The construction must include the right endpoint/Abel boundary layer. Merely
quoting `G(1/2)=8` does not prove (L-24503.7).

### 3.2 Discretization ledger

Convert `g_X^+` into a nonnegative vector `\widetilde d_X`. The one-sided exact
identity

\[
 0\le b(n/q)-\beta_{nq}\le2/q
 \tag{L-24503.8}
\]

must be used with its correct orientation. The ledger must prove

\[
 B_X^T\widetilde d_X\le w_X
 \tag{L-24503.9}
\]

and

\[
 \sum n\widetilde d_X(n)
 \ge8\sqrt X-C\log^A(2X).
 \tag{L-24503.10}
\]

Every cell-quadrature, diagonal, and small-`n` correction must be explicit.

### 3.3 Greedy/blocker ledger

Because `d_X` is the canonical backward maximum under its declared tie rule,
the final finite comparison must show that it captures at least the mass in
(L-24503.10), or charge any loss to a nonnegative blocker potential. The complete
potential must telescope and satisfy

\[
 \text{mass loss}+L_X\le C\log^A(2X).
 \tag{L-24503.11}
\]

This is the only genuinely discrete step. It may use quotient layers, digit
martingales, or the reflected Selberg square, but every blocker and every
lower-endpoint route must be listed.

## 4. Why the three ledgers cannot be conflated

The following implications are invalid and are explicitly forbidden:

```text
Abel mass eight
=> positive finite profile;

beta <= b
=> a continuum equality solution is a discrete minorant;

bounded output rank
=> small coefficient mass;

few terminal contacts
=> control of a long Mobius shell;

aggregate reflected positivity
=> positivity of every packet component.
```

A proof must establish (L-24503.7), (L-24503.9), and (L-24503.11) separately.

## 5. Rightmost-zero firewall

The continuum inverse has transform

\[
 G(s)=\frac{(s+1/2)(s+3/2)}
 {s^2(s-1/2)\zeta(s+1/2)}.
 \tag{L-24503.12}
\]

A zero `rho=1/2+delta+i gamma` produces a pole at `delta+i gamma`. Hence a proof
of (L-24503.7) by claiming unconditional positivity or uniformly tame boundary
behavior of the unmodified infinite state `g` must explain why this pole does
not create the corresponding oscillatory mode. The permitted object is the
finite positive profile `g_X^+` with a fully charged boundary correction.

This firewall prevents DCRS from being proved by simply renaming RH as
"renewal positivity."

## 6. Fixed-ratio Möbius mutation

The proof object must also consume the `c=2/3` shell from PR #234:

\[
 Q_{2/3}(t)
 =e^{-t/2}
 [M(e^t)-M((2/3)e^t)].
 \tag{L-24503.13}
\]

Its compact inverse-zeta transform has the same open-strip poles. A complete
DCRS proof must give an explicit bounded map from its carry/blocker ledger to a
subexponential block-energy bound for (L-24503.13), or an independently audited
square-screw implication. A statement about generic matrix rank or terminal
coordinates is not such a map.

## 7. Consequence for the prime ramp

Assuming DCRS, `L-24502.22` gives

\[
\begin{aligned}
 P(X)
 &\ge\frac12M_X-L_X\\
 &\ge4\sqrt X-C'\log^A(2X).
\end{aligned}
 \tag{L-24503.14}
\]

The exact square-screw/prime-ramp transfer then gives a polylogarithmic negative
part and hence rightmost-zero exponent zero.

## 8. Fail-closed production object

For each test endpoint, a DCRS proof producer must emit:

```text
exact carry matrix and target;
all greedy blockers and ties;
continuum profile cells;
convolution upper endpoints at every q;
discretization error by q;
finite mass lower endpoint;
entropy-debt upper endpoint;
blocker potential and telescope;
lower-scale routes;
fixed-ratio shell mutation;
final prime-ramp lower endpoint.
```

The symbolic theorem must prove uniform polylogarithmic bounds; finitely many
passing endpoints are reconnaissance only.

## 9. Proof boundary

This file states the corrected single closing theorem and a mandatory proof
schema. It does not prove DCRS.

Current status:

```text
continuum carry symbol and inverse state     proposed exact
finite carry/greedy algebra                  proposed exact
DCRS                                         open
DCRS -> prime-ramp lower bound               exact
prime-ramp lower bound -> RH                 imported proposed transfer
Riemann Hypothesis                           unproved
```
