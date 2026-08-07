# T-24501 — Review-hardened carry-resolvent proposal for RH

Claim ID: `T-24501`  
Title: An exact carry continuum resolvent and one finite aggregate stability theorem imply the Riemann Hypothesis without packet-face counting  
Status: **FULL PROPOSAL PENDING ADVERSARIAL REVIEW — `L-24503` OPEN; RH IS NOT CLAIMED PROVED**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Base repair: PR #241 at `3a227e7595e1fe9e38956048297aa97531c80e4e`  
Frozen external inputs: PR #202 square-screw transfer; PR #234 fixed-ratio shell firewall; PR #244 finite carry algebra  
Scope: complete proposed deduction with one scalar cofinal hinge

## 1. Disposition of the former PR #226 proposal

This theorem does not defend or silently repair the frozen terminal-face proof
at

```text
63a4d7c0f482a57893db420e64b22f6a605c72e6.
```

The adversarial verdict on PR #241 is accepted:

```text
reflected Selberg coefficient algebra         retained with sign fix;
two-frequency physical-block identity         retained;
balanced Type-II elimination                  rejected;
terminal O(1)-face count -> full recurrence   rejected;
packet-level Mertens mutation                  not established;
T-9509 as a proof of RH                       rejected.
```

No proposed repair retroactively verifies `L-9517` or `T-9509`.

## 2. Repaired reflected component

`L-9518` on the base PR gives the correct independent-frequency identity

\[
 \mathcal C_{t,-s}-\mathcal C_t-\mathcal C_{-s}
 =2\Lambda_t*\Lambda_{-s}
 \tag{T-24501.1}
\]

and the exact physical-block formula

\[
 \mathcal B_J(H)
 =\frac1{(2\pi)^2}\iint
 F_\alpha(t)\overline{F_\alpha(s)}
 \Phi_{J,\alpha}(t-s)\,dt\,ds.
 \tag{T-24501.2}
\]

This is the correct localized normal Gram. It is retained as an independent
cross-check and as an optional payment mechanism for a blocker potential. It is
not used to delete balanced rows or infer packetwise positivity.

## 3. Exact carry continuum

Define

\[
 b(t)=\frac{\lfloor t\rfloor(\lfloor t\rfloor+1-t)}t,
 \qquad
 k(u)=e^{-u/2}b(e^u).
 \tag{T-24501.3}
\]

`L-24501` proves

\[
\boxed{
 \widehat k(s)
 =\zeta(s+1/2)
  \frac{s-1/2}{(s+1/2)(s+3/2)}.}
 \tag{T-24501.4}
\]

The causal inverse of `k*g=u` has transform

\[
\boxed{
 G(s)=\frac{(s+1/2)(s+3/2)}
 {s^2(s-1/2)\zeta(s+1/2)}.}
 \tag{T-24501.5}
\]

It is the explicit finite Möbius state

\[
\boxed{
 g(u)=\sum_{n\le e^u}\frac{\mu(n)}{\sqrt n}
 \left[8e^{(u-\log n)/2}-7-\frac32(u-\log n)\right].}
 \tag{T-24501.6}
\]

The critical Abel mass is exactly

\[
\boxed{G(1/2)=8.}
 \tag{T-24501.7}
\]

Every off-line zero produces an uncancelled pole of `G` at
`s=rho-1/2`. This makes the rightmost-zero content visible before any asymptotic
claim is made.

## 4. Exact finite carry minorant

For integers `2<=q<=n<=X`, define

\[
 \beta_{nq}
 =\frac{\lfloor n/q\rfloor
 [q-1-(n\bmod q)]}{n+1}.
 \tag{T-24501.8}
\]

`L-24502` proves the exact one-sided comparison

\[
\boxed{
 0\le b(n/q)-\beta_{nq}
 =\frac{k(n+q-r)}{n(n+1)}
 \le\frac2q,}
 \tag{T-24501.9}
\]

where `n=qk+r`.

For the target

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \tag{T-24501.10}
\]

the backward minimum-ratio algorithm constructs a canonical vector `d_X>=0`
with

\[
 B_X^Td_X\le w_X.
 \tag{T-24501.11}
\]

Legendre's formula gives

\[
 P(X)
 :=\sum_{q=p^a\le X}\Lambda(q)w_X(q)
 \ge\sum_{n\le X}d_X(n)G_n,
 \tag{T-24501.12}
\]

where

\[
 G_n=\frac1{n+1}\sum_{j=0}^{n}\log\binom nj.
 \]

With

\[
 M_X=\sum n d_X(n),
 \qquad
 L_X=\sum d_X(n)[\log(n+1)+3],
 \tag{T-24501.13}
\]

the elementary entropy bound gives

\[
\boxed{P(X)\ge\frac12M_X-L_X.}
 \tag{T-24501.14}
\]

## 5. The sole closing theorem

Assume `L-24503`, Discrete Carry-Resolvent Stability:

\[
\boxed{
 8\sqrt X-M_X+L_X
 \le C\log^A(2X).}
 \tag{T-24501.15}
\]

The theorem is finite and scalar. It contains no balanced packet class, generic
operator norm, polyhedral face count, source right inverse, or unbounded matrix
hierarchy.

Its required producer is fail closed: it must expose the continuum boundary
layer, every discretization error, every greedy blocker and tie, the entropy
debt, all lower-endpoint routes, and the fixed-ratio Möbius mutation.

## 6. Prime-ramp consequence

Equations (T-24501.14)--(T-24501.15) give

\[
\begin{aligned}
 P(X)
 &\ge\frac12M_X-L_X\\
 &\ge4\sqrt X-C'\log^A(2X).
\end{aligned}
 \tag{T-24501.16}
\]

No upper estimate is needed for the negative screw direction: the exact
archimedean/polar side of the square-screw formula supplies the comparison
threshold.

## 7. Square-screw transfer to RH

Use the square-screw normalization frozen on PR #202. Its finite prime-power
formula has the form

\[
 S(N)=\text{explicit archimedean/polar threshold}
      -P(N^2),
 \tag{T-24501.17}
\]

with all lower-order terms explicit. Equation (T-24501.16), at `X=N^2`, gives

\[
 (-S(N))_+\le\log^{O(1)}N=N^{o(1)}.
 \tag{T-24501.18}
\]

The reviewed Landau/square-sampling transfer then yields

\[
 \Theta_\zeta=0.
 \tag{T-24501.19}
\]

Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
 \tag{T-24501.20}
\]

Thus

\[
\boxed{L\text{-24503}\Longrightarrow\mathrm{RH}.}
 \tag{T-24501.21}
\]

## 8. Independent fixed-ratio firewall

PR #234 identifies

\[
 Q_{2/3}(t)
 =e^{-t/2}[M(e^t)-M((2/3)e^t)]
 \tag{T-24501.22}
\]

as a compact safe inverse-zeta signal whose subexponential block energy is
RH-equivalent.

A valid proof of DCRS must either:

1. export an explicit bounded contraction from the complete carry/blocker ledger
to (T-24501.22); or
2. use the independently audited square-screw transfer without claiming that a
terminal or fixed-rank subfamily contains the shell.

This mutation prevents the coherent Möbius mode from being discarded inside a
combinatorial simplification.

## 9. Why this proposal is easier to review

The complete dependency graph is:

```text
L-9518 repaired local reflected identity       exact adapter, optional;
L-24501 continuum carry transform               exact scalar algebra;
L-24502 finite carry/greedy minorant             exact finite algebra;
L-24503 discrete carry-resolvent stability       one open scalar theorem;
T-24501.16 prime-ramp lower bound                immediate;
PR #202 square-screw/Landau transfer             frozen imported theorem;
RH                                                conclusion.
```

There is no inference of the form

```text
aggregate positivity -> packet positivity,
finite rank -> small coefficient,
few faces -> small Mobius sum,
full-period energy -> critical local energy.
```

## 10. Binary rejection tests

A timid reviewer can reject the proposal by finding any one of:

1. an error in the transform (T-24501.4);
2. a canceled zero pole in (T-24501.5);
3. an incorrect carry residue in (T-24501.8);
4. the wrong orientation in (T-24501.9);
5. a greedy residual becoming negative;
6. an omitted prime-power carry row in (T-24501.12);
7. a DCRS proof that uses Abel mass without a finite boundary ledger;
8. an uncharged blocker or tie;
9. failure of the fixed-ratio mutation;
10. a normalization mismatch with the frozen square-screw formula.

Passing finitely many numerical endpoints verifies none of the cofinal steps.

## 11. Exact status

```text
former L-9517/T-9509 proof                    rejected and not reused
repaired two-frequency reflected identity      proposed exact
continuum carry kernel/resolvent                proposed exact
finite carry/greedy algebra                     proposed exact
DCRS                                            open RH-bearing theorem
DCRS -> prime ramp -> square screw -> RH         complete proposed deduction
independently verified proof of RH               no
```

This is a new, separate proposal. It is intended to be harder to
misinterpret—not easier to approve without checking `L-24503`.
