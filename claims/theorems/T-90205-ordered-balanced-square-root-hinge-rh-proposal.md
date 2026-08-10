# T-90205 — Ordered quarter-balanced square-root hinge positivity would give an explicit exact fragmentation proof of RH

Claim ID: `T-90205`  
Status: **FULL CONDITIONAL PROPOSAL — ONE EXPLICIT HINGE THEOREM OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90209`; exact carry/divergence equivalence `L-23810`; positive hinge decomposition of the critical target; resident positive-fragmentation/RH consumer  
Scope: explicit replacement for the refuted frozen producer; RH is not claimed

## 1. Square-root hinge target

For every integer `T>=3`, define

\[
 \boxed{
 h_T(q)=
 \left(q^{-1/2}-T^{-1/2}\right)\mathbf1_{2\le q\le T}.
 }
\tag{T-90205.1}
\]

Let `r^(T)` be its unique Möbius node divergence:

\[
 U_T(m)=\sum_{k\le T/m}\mu(k)h_T(mk),
 \qquad
 r^{(T)}_m=U_T(m)-U_T(m+1).
\tag{T-90205.2}
\]

Apply the ordered quarter-balanced policy of `L-90209` and let `M^(T)` be its
exact occupation:

\[
 \boxed{
 M_n^{(T)}
 =nr_n^{(T)}+
 \sum_{m=\lceil4n/3\rceil}^{\min(4n,T)}
 \frac{2n}{mN_m}M_m^{(T)}.
 }
\tag{T-90205.3}
\]

## 2. Sole load-bearing theorem — OBH

The proposed theorem is

> **Ordered Balanced Hinge positivity (OBH).** For every `T>=3` and every
> `2<=n<=T`,
> \[
> \boxed{M_n^{(T)}\ge0.}
> \tag{T-90205.4}
> \]

By `L-90209/L-33107`, OBH is exactly the assertion that the fixed explicit
policy emits a nonnegative quarter-balanced fragmentation of every square-root
hinge.

This is not a generic convex-target theorem.  `O-90209` records the exact step
target counterexample

\[
 w(q)=\mathbf1_{2\le q\le8},
 \qquad
 M_4=-\frac43
\]

for the same policy.  Any proof of OBH must therefore use the arithmetic and
square-root structure of (T-90205.1).

## 3. Exact positive hinge decomposition of the critical target

Fix a final endpoint `X` and put

\[
 x_q=q^{-1/2},
 \qquad
 f_X(x)=2x\log\frac{x}{x_X}.
\tag{T-90205.5}
\]

Then

\[
 f_X(x_q)=q^{-1/2}\log\frac Xq=w_X(q).
\tag{T-90205.6}
\]

Moreover

\[
 f_X''(x)=\frac2x>0,
 \qquad
 f_X'(x)=2\left(1+\log\frac{x}{x_X}\right)>0
 \quad(x\ge x_X).
\tag{T-90205.7}
\]

Let

\[
 s_T=rac{f_X(x_T)-f_X(x_{T+1})}{x_T-x_{T+1}}
 \qquad(2\le T\le X-1).
\tag{T-90205.8}
\]

Convexity gives

\[
 s_{T-1}-s_T\ge0,
 \qquad
 s_{X-1}>0.
\]

The exact nodal hinge representation is

\[
 \boxed{
 w_X(q)
 =s_{X-1}h_X(q)
 +\sum_{T=3}^{X-1}(s_{T-1}-s_T)h_T(q).
 }
\tag{T-90205.9}
\]

This is simply the piecewise-linear convex interpolation formula evaluated at
the nodes `x_q`; no approximation is involved.

Thus the critical logarithmic target is a **positive superposition of the
square-root hinges**.

## 4. OBH gives one explicit nonnegative critical flow

Embed the OBH flow for a hinge `h_T` into the endpoint `X>=T` by setting every
parent coefficient above `T` to zero.  Triangularity shows it remains the same
exact hinge realization.

All hinge flows use the same split policy `pi_n` of `L-90209`.  Therefore the
positive linear combination in (T-90205.9) is again a flow using that same
policy, with total occupation

\[
 \boxed{
 M_n^{(X),\mathrm{crit}}
 =s_{X-1}M_n^{(X)}
 +\sum_{T=3}^{X-1}(s_{T-1}-s_T)M_n^{(T)}.
 }
\tag{T-90205.10}
\]

Under OBH every term is nonnegative, so

\[
 M_n^{(X),\mathrm{crit}}\ge0.
\]

Linearity of the carry loads and (T-90205.9) give exact saturation

\[
 \boxed{
 \sum_{n,j}d_{n,j}\chi_{n,j}(q)
 =q^{-1/2}\log\frac Xq
 \qquad(2\le q\le X).
 }
\tag{T-90205.11}
\]

Hence OBH constructs a nonnegative exact quarter-balanced fragmentation of the
critical target at every endpoint.

## 5. RH consequence

There are two already-resident consumers.

1. The carry/binomial route converts a nonnegative exact balanced saturation
   into the sharp complete prime-power ramp and then applies the Landau pole
   exclusion.
2. More directly, the affine potential firewall `L-32302` shows that any
   cofinal nonnegative exact fragmentation of the critical target already
   forces the reciprocal-zeta one-sign criterion and hence RH.

Therefore

\[
 \boxed{
 \mathrm{OBH}\Longrightarrow\mathrm{RH}.
 }
\tag{T-90205.12}
\]

Every arrow after OBH is already exact/standard; the entire new arithmetic
burden is the single sign theorem (T-90205.4).

## 6. Why this route survives the new resonance refutation

`T-90204` refutes the frozen half-binary/half-ternary producer because its
finite scale menu has almost-periodic deterministic resonances with real part
arbitrarily close to the conservation line.

The ordered policy is qualitatively different:

- every parent uses a whole balanced interval of splits;
- the continuum selected-child law is absolutely continuous;
- `L-90209` proves a strict deterministic spectral gap for that continuum law;
- no finite-ratio resonance mechanism pre-refutes OBH.

Thus OBH is not a relabeling of the dead producer theorem.

## 7. Finite evidence and automatic rejection tests

`O-90209/X-90205` retain the following reconnaissance:

- exhaustive hinge scan at every `3<=T<=2000`: zero negative occupations;
- smallest strictly positive nonterminal coordinate in that sweep:
  `M_1999^(2000)=0.0111789419955...`;
- spot hinges through `T=10^6`: zero negative coordinates;
- direct critical target at `X=10^3,10^4,10^5,10^6`: zero negative coordinates;
- generic step target `1_(q<=8)`: exact failure `M_4=-4/3`.

These are evidence and mutation tests, not a proof of OBH.

Reject a proposed proof if it:

- proves positivity for every decreasing/convex target (false by the step
  counterexample);
- replaces the Möbius divergence by an unsigned majorant;
- silently imports positivity of the full internal-Pascal inverse (SHARP);
- uses only the continuum spectral gap without controlling finite arithmetic
  errors;
- extrapolates the finite scan.

## 8. Exact boundary

```text
ordered quarter-balanced policy                 PROVED EXACT
sliding-band Markov recurrence                  PROVED EXACT
continuum nonlattice spectral gap               PROVED
critical target positive hinge decomposition    PROVED EXACT
OBH square-root hinge positivity                OPEN / RH-BEARING
OBH -> exact critical fragmentation -> RH       COMPLETE CONDITIONAL
Riemann Hypothesis                              UNPROVED
```
